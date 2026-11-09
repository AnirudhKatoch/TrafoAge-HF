"""
Mother function: runs the whole transformer assessment and writes every result
to Results/Simulation_N/ (dataframes as parquet, figures as png).

Order of the work, and why it is in this order:

  0. Self-test       - reproduce published numbers from C57.91 / C57.110 first, so a
                       broken formula stops the run before it produces results.
  1. Current         - magnitude (from S and V) times shape (per-unit spectrum).
  2. Loss split      - the rated load loss split into I^2R, winding eddy, other stray.
  3. Chain           - losses -> top oil -> gradient -> hot spot -> ageing -> life,
                       for the full spectrum and for the truncations (h <= 50, 180)
                       that established practice would evaluate.
  4. Monte Carlo     - spread of the life
  5. Heat maps       - the single-harmonic life map, for every eddy-loss model.
  6. Boundary        - the tolerable current I_h* (life = normal life) per order.
  7. Sensitivity     - of I_h* to the stray split sigma and to the loading.

The paper figures come from paper_figures.py, which calls the same functions.
"""

import numpy as np
import pandas as pd
from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class
from Plotting_function import Plotting_functions_class

params = Input_parameters_class()
Calculation_functions = Calculation_functions_class()
Plotting_function = Plotting_functions_class()

# Unpack the inputs once, so the code below reads like the equations
f = params.f; phases = params.phases
Profile_size = params.Profile_size; seconds_per_sample = params.seconds_per_sample
S_RMS = params.S_RMS; V_LL_RMS = params.V_LL_RMS; T_amb = params.T_amb; harmonic_scale = params.harmonic_scale
h_max = params.h_max; spectrum_source = params.spectrum_source; harmonics_pu = params.harmonics_pu; spectrum_file = params.spectrum_file
truncation_orders = params.truncation_orders
trafo_specs = params.trafo_specs; Monte_carlo_inputs = params.Monte_carlo_inputs

# ----------------------------------------#
# 0. Self-test against published values (C57.91 Table 1, C57.110 6.1.2 example, Annex C Table C.2)
# ----------------------------------------#

Calculation_functions.self_test(verbose=True)

#sim_dir, dataframes_dir, figures_dir = Calculation_functions.create_simulation_folders(base="Results")

sim_dir = "Results\Simulation_1"
dataframes_dir = "Results\Simulation_1\Dataframes"
figures_dir = "Results\Simulation_1\Figures"

print("sim_dir",sim_dir)
print("dataframes_dir",dataframes_dir)
print("figures_dir",figures_dir)

# ----------------------------------------#
# Input validation
# ----------------------------------------#

Calculation_functions.validate_mission_profile(Profile_size=Profile_size, S_RMS=S_RMS, V_LL_RMS=V_LL_RMS, T_amb=T_amb, harmonic_scale=harmonic_scale)

# ----------------------------------------#
# 1. Current entering the transformer
# ----------------------------------------#

# Shape: per-unit spectrum I_h / I_1
if spectrum_source == "parametric":
    spectrum_pu = Calculation_functions.build_harmonic_spectrum_pu(h_max=h_max, harmonics_pu=harmonics_pu)
elif spectrum_source == "file":
    spectrum_pu = Calculation_functions.load_harmonic_spectrum_pu_from_file(path=spectrum_file["path"], h_max=h_max, component=spectrum_file["component"], second=spectrum_file["second"])
else:
    raise ValueError("spectrum_source must be 'parametric' or 'file'.")

# Magnitude: fundamental from apparent power and voltage
I_1 = Calculation_functions.compute_fundamental_current(S_RMS=S_RMS, V_LL_RMS=V_LL_RMS, phases=phases)  # [A]

# Spectrum of every mission-profile sample: I_h(t) = I_1(t) * spectrum_pu[h] * harmonic_scale(t)
I_RMS_harmonics, harmonic_orders = Calculation_functions.build_harmonic_current_matrix(I_1=I_1, spectrum_pu=spectrum_pu, harmonic_scale=harmonic_scale)  # [A], shape (Profile_size, h_max)
THD = Calculation_functions.calculate_THD_from_spectrum(I_RMS_harmonics=I_RMS_harmonics, harmonic_orders=harmonic_orders)  # [%] over the full spectrum

# ----------------------------------------#
# 2. Rated load-loss split (independent of the operating point)
# ----------------------------------------#
# P_LL_R = P_R + P_EC + P_OSL, C57.110 Eq. (1), (24), (25). With sigma = 5 % and
# eddy_share = 0.5: P_R = 7220 W, P_EC = 190 W, P_OSL = 190 W.

P_R, P_EC, P_OSL = Calculation_functions.split_transformer_load_loss(P_LL_R=trafo_specs["P_LL_R"], sigma=trafo_specs["sigma"], eddy_share=trafo_specs["eddy_share"])

# ----------------------------------------#
# 3. Transformer chain: current -> losses -> temperature -> life
# ----------------------------------------#

# Winding eddy-loss weighting w(h) used by the main run: h^2 (C57.110), Annex C, or Dowell diffusion
def eddy_weights_for(thickness, model="dowell"):
    return Calculation_functions.calculate_eddy_loss_weighting(harmonic_orders=harmonic_orders, f=f, conductor_thickness=thickness, rho=trafo_specs["conductor_resistivity"], model=model)

if trafo_specs["eddy_model"] == "C57.110":
    eddy_weights_main = eddy_weights_for(None)
elif trafo_specs["eddy_model"] == "skin_depth":
    eddy_weights_main = eddy_weights_for(trafo_specs["conductor_thickness"])
elif trafo_specs["eddy_model"] == "annexC":
    eddy_weights_main = eddy_weights_for(trafo_specs["conductor_thickness"], model="annexC")
else:
    raise ValueError("eddy_model must be 'C57.110', 'annexC' or 'skin_depth'.")

def run_transformer(h_max_used, eddy_weights=None):
    #Evaluate the full transformer chain over the spectrum truncated at h_max_used (None = full).

    if eddy_weights is None:
        eddy_weights = eddy_weights_main

    # Magnitude and shape over the SAME band: the RMS and the loss factors must
    # both stop at h_max_used, otherwise the truncation is inconsistent (C57.110 Eq. (4), (12)).
    I_RMS = Calculation_functions.calculate_RMS_from_spectrum(I_RMS_harmonics=I_RMS_harmonics, harmonic_orders=harmonic_orders, h_max_used=h_max_used)  # [A]
    F_HL = Calculation_functions.calculate_harmonic_loss_factor(I_RMS_harmonics, harmonic_orders, k=trafo_specs["k_F_HL"], h_max_used=h_max_used, weights=eddy_weights)
    F_HL_STR = Calculation_functions.calculate_harmonic_loss_factor(I_RMS_harmonics, harmonic_orders, k=trafo_specs["k_F_HL_STR"], h_max_used=h_max_used)

    # Losses: C57.110 Eq. (19); total adds the voltage-driven core loss
    P_LL = Calculation_functions.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=trafo_specs["I_R"], P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, F_HL=F_HL, F_HL_STR=F_HL_STR)  # [W]
    P_T = P_LL + trafo_specs["P_NL"]  # [W]

    # Temperature: top oil (C57.110 Eq. (18)) + gradient (C57.110 Eq. (21)) on top of the ambient
    Theta_TO = Calculation_functions.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo_specs["P_LL_R"], P_NL=trafo_specs["P_NL"], Theta_TO_R=trafo_specs["Theta_TO_R"], x_oil=trafo_specs["x_oil"])  # [K]
    Theta_g = Calculation_functions.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=trafo_specs["I_R"], P_R=P_R, P_EC=P_EC, F_HL=F_HL, Theta_g_R=trafo_specs["Theta_g_R"], y_winding=trafo_specs["y_winding"], eddy_hotspot_factor=trafo_specs["eddy_hotspot_factor"])  # [K]
    Theta_H = (T_amb - 273.15) + Theta_TO + Theta_g  # [°C]

    # Life: C57.91 Eq. (2) per sample, Eq. (3)-(4) over the profile
    F_AA = Calculation_functions.calculate_transformer_ageing_acceleration(Theta_H=Theta_H, Theta_ref=trafo_specs["Theta_ref"])
    F_EQA, LOL, Lifetime = Calculation_functions.calculate_transformer_loss_of_life(F_AA=F_AA, seconds_per_sample=seconds_per_sample, L_normal=trafo_specs["L_normal"])

    return dict(I_RMS=I_RMS, F_HL=F_HL, F_HL_STR=F_HL_STR, P_LL=P_LL, P_T=P_T, Theta_TO=Theta_TO, Theta_g=Theta_g, Theta_H=Theta_H, F_AA=F_AA, F_EQA=F_EQA, LOL=LOL, Lifetime=Lifetime)

# Main run
res = run_transformer(trafo_specs["h_max_used"])

# Same chain over the bands established practice would evaluate (h <= 50, h <= 180, full)
truncation_rows = []
for h_cut in truncation_orders:
    r = run_transformer(h_cut)
    h_eff = h_max if h_cut is None else min(h_cut, h_max)
    truncation_rows.append({
        "label": "Full" if h_cut is None else f"h ≤ {h_cut}",
        "h_max_used": h_eff,
        "f_upper_Hz": h_eff * f,
        "F_HL_mean": np.mean(r["F_HL"]),
        "F_HL_STR_mean": np.mean(r["F_HL_STR"]),
        "P_T_mean": np.mean(r["P_T"]),
        "Theta_H_mean": np.mean(r["Theta_H"]),
        "Theta_H_max": np.max(r["Theta_H"]),
        "LOL_trafo": r["LOL"],
        "Lifetime_trafo": r["Lifetime"],
    })
df_5_truncation = pd.DataFrame(truncation_rows)

# Same chain for the mission-profile spectrum under each eddy-loss model
def thickness_label(d, model="dowell"):
    if d is None:
        return "C57.110 ($h^2$)"
    return f"Annex C, d = {d * 1e3:g} mm" if model == "annexC" else f"d = {d * 1e3:g} mm"

def thickness_label_plain(d, model="dowell"):
    if d is None:
        return "C57.110 (h^2)"
    return f"AnnexC d = {d * 1e3:g} mm" if model == "annexC" else f"d = {d * 1e3:g} mm"

delta_50 = Calculation_functions.skin_depth(f, trafo_specs["conductor_resistivity"])
thickness_rows = []
for d in params.heatmap["thickness_sweep"]:
    for model in (("dowell",) if d is None else ("dowell", "annexC")):
        r = run_transformer(None, eddy_weights=eddy_weights_for(d, model))
        thickness_rows.append({
            "label": thickness_label_plain(d, model),
            "thickness_m": np.nan if d is None else d,
            "h_crossover": np.inf if d is None else (delta_50 / d) ** 2,   # h_c = (delta_1/d)^2
            "F_HL_mean": np.mean(r["F_HL"]),
            "Theta_H_mean": np.mean(r["Theta_H"]),
            "LOL_trafo": r["LOL"],
            "Lifetime_trafo": r["Lifetime"],
        })
df_7_thickness = pd.DataFrame(thickness_rows)



# ----------------------------------------#
# 4. Monte Carlo
# ----------------------------------------#
# framework for continuity; not used in the paper.

rng = Monte_carlo_inputs["rng_original"]
n_MC = Monte_carlo_inputs["number_of_samples"]
sigma_MC = Monte_carlo_inputs["normal_distribution"]

Theta_H_eq = Calculation_functions.equivalent_temperature_transformer(L_eq_years=res["Lifetime"], Theta_ref=trafo_specs["Theta_ref"], L_normal=trafo_specs["L_normal"])
Theta_H_samples = Calculation_functions.normal_distribution_function(Theta_H_eq, sigma_MC, n_MC, rng)
Theta_ref_samples = Calculation_functions.normal_distribution_function(trafo_specs["Theta_ref"], sigma_MC, n_MC, rng)
L_normal_samples = Calculation_functions.normal_distribution_function(trafo_specs["L_normal"], sigma_MC, n_MC, rng)
F_AA_MC = Calculation_functions.calculate_transformer_ageing_acceleration(Theta_H=Theta_H_samples, Theta_ref=Theta_ref_samples)
Lifetime_trafo_MC = L_normal_samples / (F_AA_MC * 365.0 * 24.0)  # [years]
B10_trafo = np.percentile(Lifetime_trafo_MC, 10)  # [years] life by which 10 % of the draws have failed

# ----------------------------------------#
# Report
# ----------------------------------------#

Calculation_functions.report_transformer(trafo_specs=trafo_specs, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, F_HL=res["F_HL"], F_HL_STR=res["F_HL_STR"], P_LL=res["P_LL"], P_T=res["P_T"], Theta_TO=res["Theta_TO"], Theta_g=res["Theta_g"], Theta_H=res["Theta_H"], F_AA=res["F_AA"], F_EQA=res["F_EQA"], LOL=res["LOL"], Lifetime_years=res["Lifetime"], I_RMS=res["I_RMS"], THD=THD, T_amb=T_amb, B10=B10_trafo)

print(" Harmonic loss factor by evaluated band")
print(df_5_truncation[["label", "f_upper_Hz", "F_HL_mean", "Theta_H_mean", "Lifetime_trafo"]].to_string(index=False))
print()
print(f" Winding eddy-loss model (full spectrum)   [skin depth at {f:g} Hz = {delta_50 * 1e3:.2f} mm]")
print(df_7_thickness[["label", "h_crossover", "F_HL_mean", "Theta_H_mean", "Lifetime_trafo"]].round(3).to_string(index=False))
print()

# ----------------------------------------#
# Save and plot
# ----------------------------------------#

df_1_mission_profile = pd.DataFrame({
    "S_RMS": S_RMS,                 # [VA]
    "V_LL_RMS": V_LL_RMS,           # [V]
    "T_amb": T_amb,                 # [K]
    "harmonic_scale": harmonic_scale,  # [-]
    "I_1": I_1,                     # [A] fundamental
    "I_RMS": res["I_RMS"],          # [A] total over the main-run band
    "THD": THD,                     # [%] full spectrum
})
df_1_mission_profile.to_parquet(f"{dataframes_dir}/df_1_mission_profile.parquet")
Plotting_function.plot_mission_profile(df_1_mission_profile=df_1_mission_profile, figures_dir=figures_dir, xlabel="Time [day]")

df_2_harmonics = pd.DataFrame({
    "second": np.repeat(np.arange(Profile_size), h_max),
    "order": np.tile(harmonic_orders, Profile_size),
    "I_rms": I_RMS_harmonics.ravel(),  # [A]
})
df_2_harmonics.to_parquet(f"{dataframes_dir}/df_2_harmonics.parquet")
spectrum_last = I_RMS_harmonics[-1] / I_RMS_harmonics[-1, 0] if I_RMS_harmonics[-1, 0] > 0 else spectrum_pu
Plotting_function.plot_harmonic_spectrum(spectrum_pu=spectrum_last, figures_dir=figures_dir, f=f, truncation_orders=[h for h in truncation_orders if h is not None])

last = Calculation_functions.last_of_column
df_3_trafo = pd.DataFrame({
    # --- per-sample ---
    "I_RMS": res["I_RMS"],          # [A]    Total RMS current entering the transformer
    "F_HL": res["F_HL"],            # [-]    Harmonic loss factor, winding eddy loss
    "F_HL_STR": res["F_HL_STR"],    # [-]    Harmonic loss factor, other stray loss (k = 0.8)
    "P_LL": res["P_LL"],            # [W]    Load loss under the distorted current
    "P_T": res["P_T"],              # [W]    Total loss, load plus no-load
    "Theta_TO": res["Theta_TO"],    # [K]    Top-oil rise above ambient
    "Theta_g": res["Theta_g"],      # [K]    Hot-spot gradient above top oil
    "Theta_H": res["Theta_H"],      # [degC] Winding hot-spot temperature
    "F_AA": res["F_AA"],            # [-]    Ageing acceleration factor
    # --- scalars: last row only ---
    "P_R": last(P_R, Profile_size),
    "P_EC": last(P_EC, Profile_size),
    "P_OSL": last(P_OSL, Profile_size),
    "P_LL_R": last(trafo_specs["P_LL_R"], Profile_size),
    "P_NL": last(trafo_specs["P_NL"], Profile_size),
    "I_R": last(trafo_specs["I_R"], Profile_size),
    "sigma": last(trafo_specs["sigma"], Profile_size),
    "eddy_share": last(trafo_specs["eddy_share"], Profile_size),
    "Theta_TO_R": last(trafo_specs["Theta_TO_R"], Profile_size),
    "Theta_g_R": last(trafo_specs["Theta_g_R"], Profile_size),
    "eddy_hotspot_factor": last(trafo_specs["eddy_hotspot_factor"], Profile_size),
    "x_oil": last(trafo_specs["x_oil"], Profile_size),
    "y_winding": last(trafo_specs["y_winding"], Profile_size),
    "Theta_ref": last(trafo_specs["Theta_ref"], Profile_size),
    "L_normal": last(trafo_specs["L_normal"], Profile_size),
    "F_EQA": last(res["F_EQA"], Profile_size),
    "LOL_trafo": last(res["LOL"], Profile_size),
    "Lifetime_trafo": last(res["Lifetime"], Profile_size),
})
df_3_trafo.to_parquet(f"{dataframes_dir}/df_3_trafo.parquet")
Plotting_function.plot_trafo_profile(df_3_trafo=df_3_trafo, figures_dir=figures_dir, xlabel="Time [day]")

df_4_MC_trafo = pd.DataFrame({
    "Lifetime_trafo_MC": Lifetime_trafo_MC,  # [years]
    "B10_trafo": B10_trafo,                  # [years]
})
df_4_MC_trafo.to_parquet(f"{dataframes_dir}/df_4_MC_trafo.parquet")
Plotting_function.plot_lifetime_monte_carlo_trafo(Lifetime_trafo_MC=Lifetime_trafo_MC, figures_dir=figures_dir, B10_trafo=B10_trafo, plot_type="histogram", bins=50)

df_5_truncation.to_parquet(f"{dataframes_dir}/df_5_truncation.parquet")
Plotting_function.plot_truncation_comparison(df_5_truncation=df_5_truncation, figures_dir=figures_dir)



# ----------------------------------------#
# 5. Harmonic sensitivity heat map (square law)
# ----------------------------------------#
# One harmonic at a time on top of a rated sinusoidal fundamental. Uses the
# C57.110 h^2 weighting (no eddy_weights passed); the corrected models follow below.

heatmap = params.heatmap
I_R = trafo_specs["I_R"]
h_map = np.arange(1, h_max + 1)
T_amb_map_C = np.mean(T_amb) - 273.15  # [°C] constant ambient for the map

for y_scale, I_h_map, fname in [
        ("linear", np.linspace(0.0, I_R, heatmap["n_current"]), "Fig_11_heatmap_life"),
        ("log", np.geomspace(1e-4 * I_R, I_R, heatmap["n_current"]), "Fig_11b_heatmap_life_logI")]:

    Theta_H_map, Life_map = Calculation_functions.calculate_harmonic_sensitivity_map(trafo_specs=trafo_specs, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, h_orders=h_map, I_h_values=I_h_map, I_1=heatmap["I_1_pu"] * I_R, T_amb_C=T_amb_map_C)

    pd.DataFrame({
        "order": np.tile(h_map, I_h_map.size),
        "I_h": np.repeat(I_h_map, h_map.size),          # [A]
        "Theta_H": Theta_H_map.ravel(),                 # [°C]
        "Life_years": Life_map.ravel(),                 # [years]
    }).to_parquet(f"{dataframes_dir}/df_6_heatmap_{y_scale}.parquet")

    Plotting_function.plot_harmonic_heatmap(h_orders=h_map, I_h_values=I_h_map, Life_years=Life_map, I_R=I_R, figures_dir=figures_dir, f=f, fname=fname, life_floor=heatmap["life_floor_years"], life_contours=heatmap["life_contours"], truncation_orders=[h for h in truncation_orders if h is not None], y_scale=y_scale, h_max_plot=h_max)


# ----------------------------------------#
# 6. Heat map for every eddy-loss model, and the tolerable-current boundary
# ----------------------------------------#
# Same single-harmonic map, with the winding eddy loss weighted by w(h) for
# each conductor thickness (Dowell) instead of h^2, and Annex C for 2 and 3 mm.
# The iso-life boundary is the harmonic current at which the hot spot reaches
# its reference temperature, i.e. the transformer ages at exactly its normal
# rate (life = L_normal): the TOLERABLE CURRENT I_h*.

I_h_log = np.geomspace(1e-4 * I_R, I_R, heatmap["n_current"])   # log grid: resolves 0.01 % to 100 % of I_R
L_normal_years = trafo_specs["L_normal"] / (365.0 * 24.0)       # 20.55 years

sweep_cases = [(d, "dowell") for d in heatmap["thickness_sweep"]] + [(2e-3, "annexC"), (3e-3, "annexC")]
sweep_maps, sweep_labels, iso_rows, weight_curves = [], [], {}, {}
for d, model in sweep_cases:
    w_map = Calculation_functions.calculate_eddy_loss_weighting(harmonic_orders=h_map, f=f, conductor_thickness=d, rho=trafo_specs["conductor_resistivity"], model=model)
    _, Life_d = Calculation_functions.calculate_harmonic_sensitivity_map(trafo_specs=trafo_specs, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, h_orders=h_map, I_h_values=I_h_log, I_1=heatmap["I_1_pu"] * I_R, T_amb_C=T_amb_map_C, eddy_weights=w_map)
    sweep_maps.append(Life_d)
    sweep_labels.append(thickness_label(d, model))
    iso_rows[thickness_label_plain(d, model)] = Calculation_functions.iso_life_current(I_h_values=I_h_log, Life_years=Life_d, L_target=L_normal_years)
    weight_curves[thickness_label(d, model)] = w_map

df_8_iso_life = pd.DataFrame({"order": h_map, "f_Hz": h_map * f, **{f"I_iso_{k}": v for k, v in iso_rows.items()}})
df_8_iso_life.to_parquet(f"{dataframes_dir}/df_8_iso_life.parquet")
df_7_thickness.to_parquet(f"{dataframes_dir}/df_7_thickness_sweep.parquet")

Plotting_function.plot_eddy_weighting(h_orders=h_map, weight_curves=weight_curves, figures_dir=figures_dir, f=f)
Plotting_function.plot_heatmap_sweep(h_orders=h_map, I_h_values=I_h_log, Life_maps=sweep_maps, labels=sweep_labels, I_R=I_R, figures_dir=figures_dir, f=f, life_floor=heatmap["life_floor_years"], L_iso=L_normal_years, truncation_orders=[h for h in truncation_orders if h is not None])
Plotting_function.plot_iso_life_boundaries(h_orders=h_map, iso_currents={lab: iso_rows[thickness_label_plain(d, m)] for lab, (d, m) in zip(sweep_labels, sweep_cases)}, I_R=I_R, figures_dir=figures_dir, f=f, truncation_orders=[h for h in truncation_orders if h is not None], limits=params.emission_limits)

# ----------------------------------------#
# 7. Sensitivity of the boundary: stray-loss split sigma and fundamental loading
# ----------------------------------------#
# sigma sets the rated winding eddy loss P_EC = eddy_share * sigma * P_LL_R,
# which is not on the data sheet; the loading sets the thermal headroom the
# harmonic has to consume before the hot spot reaches its reference.

sens = params.sensitivity

def iso_boundary(sigma, I_1_pu, thickness):
    P_R_s, P_EC_s, P_OSL_s = Calculation_functions.split_transformer_load_loss(P_LL_R=trafo_specs["P_LL_R"], sigma=sigma, eddy_share=trafo_specs["eddy_share"])
    w_s = Calculation_functions.calculate_eddy_loss_weighting(harmonic_orders=h_map, f=f, conductor_thickness=thickness, rho=trafo_specs["conductor_resistivity"])
    _, L_s = Calculation_functions.calculate_harmonic_sensitivity_map(trafo_specs=trafo_specs, P_R=P_R_s, P_EC=P_EC_s, P_OSL=P_OSL_s, h_orders=h_map, I_h_values=I_h_log, I_1=I_1_pu * I_R, T_amb_C=T_amb_map_C, eddy_weights=w_s)
    return Calculation_functions.iso_life_current(I_h_values=I_h_log, Life_years=L_s, L_target=L_normal_years)

sens_rows = {"order": h_map, "f_Hz": h_map * f}
for d in sens["thicknesses"]:
    tag = "C57" if d is None else f"d{d * 1e3:g}mm"
    curves_sigma = {}
    for s in sens["sigma_sweep"]:
        I_iso = iso_boundary(s, heatmap["I_1_pu"], d)
        curves_sigma[f"$\\sigma$ = {s * 100:g} %"] = I_iso
        sens_rows[f"I_iso_sigma{s:g}_{tag}"] = I_iso
    Plotting_function.plot_iso_life_boundaries(h_orders=h_map, iso_currents=curves_sigma, I_R=I_R, figures_dir=figures_dir, f=f, truncation_orders=[h for h in truncation_orders if h is not None], limits=params.emission_limits, fname=f"Fig_15_sigma_sensitivity_{tag}", title=f"Stray-loss split, {thickness_label(d)}")

    curves_load = {}
    for k_load in sens["loading_sweep"]:
        I_iso = iso_boundary(trafo_specs["sigma"], k_load, d)
        curves_load[f"$I_1$ = {k_load:g} pu"] = I_iso
        sens_rows[f"I_iso_load{k_load:g}_{tag}"] = I_iso
    Plotting_function.plot_iso_life_boundaries(h_orders=h_map, iso_currents=curves_load, I_R=I_R, figures_dir=figures_dir, f=f, truncation_orders=[h for h in truncation_orders if h is not None], limits=params.emission_limits, fname=f"Fig_16_loading_sensitivity_{tag}", title=f"Fundamental loading, {thickness_label(d)}")

df_9_sensitivity = pd.DataFrame(sens_rows)
df_9_sensitivity.to_parquet(f"{dataframes_dir}/df_9_sensitivity.parquet")

print(" Tolerable harmonic current at the normal ageing rate [A]")
print(df_9_sensitivity[df_9_sensitivity["order"].isin([50, 100, 200, 400, 500])].round(1).T.to_string(header=False))
print()

print("Results written to", sim_dir)


