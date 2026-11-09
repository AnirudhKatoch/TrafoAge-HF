"""
heatmap_fixed_rms.py

Single-harmonic life maps with the TOTAL RMS current held at the rated current I_R.

    I_RMS = I_R                                  (always 3608 A for the 2.5 MVA, 400 V unit)
    I_1   = sqrt(I_R^2 - I_h^2)                  (the fundamental gives way as the harmonic grows)

Compare heatmap_study.py, where the FUNDAMENTAL is held at I_R and the total RMS
current rises to sqrt(I_R^2 + I_h^2). Here the ohmic loss stays exactly at its rated
value, so any loss of life comes only from the frequency weighting of the harmonic
(w(h) for the winding eddy loss, h^0.8 for the other stray loss).

Same transformer data (Input_parameters.py) and same physics (Calculation_functions.py)
as heatmap_study.py. Files carry the suffix _fixedRMS so nothing of heatmap_study.py is
overwritten.

Outputs
    Dataframes/heatmap_fixedRMS_<model>.csv     every map point (order, I_h, I_1, hot spot, life)
    Dataframes/tolerable_current_fixedRMS.csv   I_h* per order for every model
    Figures/life_maps_fixedRMS.png              three life maps side by side
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF


# ==================================================================== #
# Settings
# ==================================================================== #

RESULTS_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Dataframes")
FIGURES_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures")

F_OVERRIDE = None         # [Hz]   None = use params.f; set 60 or 50 to force
D_CONDUCTOR = 2.5e-3      # [m]    conductor thickness for Annex C and diffusion
H_MIN, H_MAX = 2, 333     # [-]    orders on the map (333 x 60 Hz = 20 kHz)
N_CURRENT = 500           # [-]    current steps
I_MIN_PU = 1e-4           # [pu]   smallest harmonic current, fraction of I_R
I_MAX_PU = 1.0            # [pu]   largest harmonic current; at 1.0 the fundamental is zero
YLIM_PCT = (0.25, 100.0)  # [% of I_R] y-axis of the figure
REPORT_ORDERS = [50, 100, 200, 333]

MODELS = [
    ("C57110_h2",  None,        "dowell", "C57.110, $w(h) = h^2$"),
    ("AnnexC_nom", D_CONDUCTOR, "annexC", f"Annex C, $d$ = {D_CONDUCTOR * 1e3:g} mm"),
    ("Dowell_nom", D_CONDUCTOR, "dowell", f"Diffusion, $d$ = {D_CONDUCTOR * 1e3:g} mm"),
]


# ==================================================================== #
# Physics: one harmonic, total RMS fixed at I_R
# ==================================================================== #

def life_map_fixed_rms(trafo, h, I_h, w, T_amb_C):
    """
    Hot spot [degC] and life [years] on the grid (I_h x h) with I_RMS = I_R.

        I_1^2    = I_R^2 - I_h^2
        F_HL     = (I_1^2 + I_h^2 w(h))  / I_R^2
        F_HL_STR = (I_1^2 + I_h^2 h^0.8) / I_R^2
    then the same C57.110 / C57.91 chain as heatmap_study.py.
    """
    I_R = trafo["I_R"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(trafo["P_LL_R"], trafo["sigma"], trafo["eddy_share"])

    hh = np.asarray(h, float)[np.newaxis, :]
    Ih2 = (np.asarray(I_h, float) ** 2)[:, np.newaxis]
    I1_sq = I_R ** 2 - Ih2                                   # fundamental gives way
    if np.any(I1_sq < -1e-9):
        raise ValueError("I_h may not exceed I_R when the total RMS current is fixed at I_R.")
    I1_sq = np.maximum(I1_sq, 0.0)

    w_row = np.asarray(w, float)[np.newaxis, :]
    F_HL = (I1_sq + Ih2 * w_row) / I_R ** 2
    F_HL_STR = (I1_sq + Ih2 * hh ** trafo["k_F_HL_STR"]) / I_R ** 2
    I_RMS = np.full_like(F_HL, I_R)                          # constant by construction

    P_LL = CF.calculate_transformer_load_loss(I_RMS, I_R, P_R, P_EC, P_OSL, F_HL, F_HL_STR)
    Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL, trafo["P_LL_R"], trafo["P_NL"],
                                                     trafo["Theta_TO_R"], trafo["x_oil"])
    Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS, I_R, P_R, P_EC, F_HL, trafo["Theta_g_R"],
                                                        trafo["y_winding"], trafo["eddy_hotspot_factor"])
    Theta_H = T_amb_C + Theta_TO.reshape(F_HL.shape) + Theta_g.reshape(F_HL.shape)

    with np.errstate(over="ignore"):
        F_AA = np.exp(15000.0 / (trafo["Theta_ref"] + 273.0) - 15000.0 / (Theta_H + 273.0))
        Life = trafo["L_normal"] / (F_AA * 8760.0)
    return Theta_H, Life


# ==================================================================== #
# Main
# ==================================================================== #

def main():
    CF.self_test(verbose=False)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    params = Input_parameters_class()
    trafo = params.trafo_specs
    f = F_OVERRIDE or params.f
    I_R = trafo["I_R"]
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    L_n = trafo["L_normal"] / 8760.0

    h = np.arange(H_MIN, H_MAX + 1)
    I_h = np.geomspace(I_MIN_PU * I_R, I_MAX_PU * I_R, N_CURRENT)

    print(f"\n Fixed total RMS current: I_RMS = I_R = {I_R:.1f} A, f = {f:g} Hz, "
          f"ambient {T_amb_C:g} degC, d = {D_CONDUCTOR * 1e3:g} mm")

    # Maps and tolerable currents
    maps, iso = [], {}
    for tag, d, model, title in MODELS:
        w = CF.calculate_eddy_loss_weighting(h, f, d, trafo["conductor_resistivity"], model)
        Theta_H, Life = life_map_fixed_rms(trafo, h, I_h, w, T_amb_C)
        iso[tag] = CF.iso_life_current(I_h, Life, L_n)
        maps.append((tag, title, Life))
        pd.DataFrame({
            "order": np.tile(h, I_h.size),
            "f_Hz": np.tile(h, I_h.size) * f,
            "I_h_A": np.repeat(I_h, h.size),
            "I_h_pct_IR": np.repeat(100 * I_h / I_R, h.size),
            "I_1_A": np.repeat(np.sqrt(np.maximum(I_R ** 2 - I_h ** 2, 0)), h.size),
            "Theta_H_C": Theta_H.ravel(),
            "Life_years": Life.ravel(),
        }).to_csv(RESULTS_DIR / f"heatmap_fixedRMS_{tag}.csv", index=False)

    # Tolerable current table
    print("\n Tolerable harmonic current I_h* (life = normal life), total RMS fixed at I_R")
    print("  order  f [kHz]" + "".join(f"{t[3].replace('$', '')[:22]:>26s}" for t in MODELS))
    for o in REPORT_ORDERS:
        j = int(np.where(h == o)[0][0])
        print(f"  {o:5d} {o * f / 1e3:8.2f}" + "".join(
            f"{iso[t][j]:12.1f} A ({100 * iso[t][j] / I_R:5.2f}%)" for t, *_ in MODELS))
    pd.DataFrame({"order": h, "f_Hz": h * f,
                  **{f"I_star_{t}_A": v for t, v in iso.items()},
                  **{f"I_star_{t}_pct_IR": 100 * v / I_R for t, v in iso.items()}}
                 ).to_csv(RESULTS_DIR / "tolerable_current_fixedRMS.csv", index=False)

    # Figure: same layout as life_maps of heatmap_study.py
    life_top = max(np.nanmax(L) for *_, L in maps)
    norm = LogNorm(vmin=0.1, vmax=life_top)
    fig, axes = plt.subplots(1, 3, figsize=(6.4 * 2, 4.8 * 0.75), sharey=True, constrained_layout=True)
    I_pct = 100 * I_h / I_R
    for ax, (tag, title, L) in zip(axes, maps):
        mesh = ax.pcolormesh(h, I_pct, np.clip(L, 0.1, life_top), shading="nearest",
                             cmap="inferno", norm=norm, rasterized=True)
        ax.contour(h, I_pct, L, levels=[L_n], colors="white", linewidths=1.5)
        ax.contour(h, I_pct, L, levels=[1, 5], colors="white", linewidths=1.0, linestyles="--")
        for ho in [o for o in params.truncation_orders if o is not None]:
            ax.axvline(ho, color="cyan", linestyle="--", linewidth=1.0)
        ax.set_yscale("log")
        ax.set_ylim(*YLIM_PCT)
        ax.set_xlim(h[0], h[-1])
        ax.set_xlabel("Harmonic order $h$")
        ax.set_title(title)
        top = ax.secondary_xaxis("top", functions=(lambda x: x * f / 1e3, lambda k: k * 1e3 / f))
        top.set_xlabel("Frequency [kHz]")
    axes[0].set_ylabel("Harmonic current [% of $I_R$]")
    fig.colorbar(mesh, ax=axes, extend="min", pad=0.01).set_label("Equivalent life [years]")
    fig.savefig(FIGURES_DIR / "life_maps_fixedRMS.png", dpi=300)
    plt.close(fig)

    print(f"\n Data written to   {RESULTS_DIR}")
    print(f" Figure written to {FIGURES_DIR / 'life_maps_fixedRMS.png'}")


if __name__ == "__main__":
    main()