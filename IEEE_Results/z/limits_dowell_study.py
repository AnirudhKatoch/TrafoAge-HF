"""
limits_dowell_study.py

Tolerable harmonic current I_h* under the Dowell diffusion weighting only,
against the emission limits. Figures and numbers for Sec. "Tolerable Current
Against Emission Limits" (sec:EmissionLimits).

    I_h* = harmonic current of order h which, on top of the fundamental, brings
           the hot spot to Theta_ref (life = normal life). Steady state.

Why Dowell only: for a given thickness it gives the lowest eddy loss of the three
weightings, so any excess over a limit found here also holds under h^2 and Annex C.

Cases (all Dowell unless stated)
    thickness  d = 1.0, 1.5, ... 4.0 mm                rated load, nominal sigma
    sigma      sigma = 3 % and 15 % at d = 1, 2.5, 4 mm  rated load
    loading    I_1 = 0.5 and 0.75 pu at d = 2.5 mm       nominal sigma
    reference  C57.110 h^2                              rated load, nominal sigma

Limit lines
    IEEE 519-2022 Table 2, row Isc/IL < 20 (footnote c), footnote a (even h <= 6 at 50 %), up to h = 50
    0.3 % of 35 <= h <= 50 extended to h_max (no standard sets it, reference only)
    5 % TRD of IEEE 1547-2018 Sec. 7.3
Limits in % of the transformer rated current (converter or load rated at the transformer rating, assumed).

All physics comes from Calculation_functions.py.

Outputs
    IEEE_Results/Dataframes/dowell_tolerable_current.csv   I_h* of every case, long format
    IEEE_Results/Dataframes/dowell_limits.csv              limit lines per order
    IEEE_Results/Dataframes/dowell_summary.csv             numbers of Table tab:limits
    IEEE_Results/Figures/limits_dowell.png/.pdf            main figure (fig:tolerance_gap)
    IEEE_Results/Figures/limits_dowell_loading.png/.pdf    optional, loading at d = 2.5 mm
    IEEE_Results/Figures/limits_dowell_sigma.png/.pdf      optional, sigma bands at d = 1, 2.5, 4 mm
"""
import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF

plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15, "axes.titlesize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 13})


# ==================================================================== #
# Settings
# ==================================================================== #

RESULTS_DIR = Path(os.environ.get("IEEE_RESULTS_DIR", r"E:\IEEE_GM_2027_Transformer\IEEE_Results"))
FIGURES_DIR = RESULTS_DIR / "Figures"
DATAFRAMES_DIR = RESULTS_DIR / "Dataframes"

H_MIN = 2                                   # [-]  lowest order
N_CURRENT = 2000                            # [-]  current steps of the map behind I_h*
I_MIN_PU, I_MAX_PU = 1e-4, 3.0              # [pu] current range; above 1 pu so part-load boundaries stay inside

D_NOMINAL = 2.5e-3                          # [m]  nominal conductor thickness
D_SWEEP = np.round(np.arange(1.0, 4.0 + 1e-9, 0.5), 2) * 1e-3   # [m] 1.0 ... 4.0 mm
D_SIGMA = [1.0e-3, 2.5e-3, 4.0e-3]          # [m]  thicknesses of the sigma cases
SIGMA_LOW, SIGMA_HIGH = 0.03, 0.15          # [-]  stray fraction range
LOADINGS = [0.5, 0.75, 1.0]                 # [pu] fundamental current / I_R

TRD_PCT = 5.0                               # [%]  IEEE 1547-2018 TRD
EXT_PCT = 0.3                               # [%]  IEEE 519 Table 2, 35 <= h <= 50, extended
F_REPORT_KHZ = 10.0                         # [kHz] frequency of the TRD / I_h* column

YLIM_PCT = (0.1, 100.0)                     # [% of I_R] y-axis limits
FIGSIZE = (6.4, 4.8 * 1.25)                 # one column after scaling (legend below)
SHOW_H2_REFERENCE = True                    # grey dotted h^2 curve on the main figure
SHOW_SIGMA_BAND = False                     # sigma 3 to 15 % band at d = 2.5 mm on the main figure
LEGEND_KW = dict(fontsize=11, handlelength=1.5, columnspacing=0.8, handletextpad=0.4)   # keeps three columns inside the figure


# ==================================================================== #
# Setup
# ==================================================================== #

def make_output_dirs():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    DATAFRAMES_DIR.mkdir(parents=True, exist_ok=True)


def load_inputs():
    params = Input_parameters_class()
    return params, params.trafo_specs


def print_inputs(trafo, f, T_amb_C):
    print("\n Inputs")
    print(f"  Rated power / LV voltage   {trafo['S_r'] / 1e6:.2f} MVA / {trafo['V_LV']:.0f} V")
    print(f"  Rated LV current I_R       {trafo['I_R']:.1f} A")
    print(f"  Load / no-load loss        {trafo['P_LL_R']:.0f} W / {trafo['P_NL']:.0f} W")
    print(f"  sigma (nominal) / eps      {trafo['sigma']:.3f} / {trafo['eddy_share']:.3f}")
    print(f"  Concentration c            {trafo['eddy_hotspot_factor']:.2f}")
    print(f"  Exponents x / y (loss)     {trafo['x_oil']:.2f} / {trafo['y_winding']:.2f}")
    print(f"  Rated rises TO / g         {trafo['Theta_TO_R']:.0f} K / {trafo['Theta_g_R']:.0f} K")
    print(f"  Ambient                    {T_amb_C:.1f} degC")
    print(f"  Theta_ref / L_normal       {trafo['Theta_ref']:.0f} degC / {trafo['L_normal']:.0f} h")
    print(f"  d nominal / sweep          {D_NOMINAL * 1e3:g} mm / {D_SWEEP[0] * 1e3:g} to {D_SWEEP[-1] * 1e3:g} mm")


# ==================================================================== #
# Limits
# ==================================================================== #

def ieee519_limit_pct(h, bands):
    """IEEE 519-2022 Table 2 (Isc/IL < 20) per order in %, NaN above the last band. Footnote a: even h <= 6 at 50 %."""
    h = np.asarray(h)
    lim = np.full(h.shape, np.nan)
    for h0, h1, pct in bands:
        lim[(h >= h0) & (h < h1)] = pct
    lim[(h % 2 == 0) & (h <= 6)] *= 0.5
    return lim


def limits_table(h, bands, f):
    lim519 = ieee519_limit_pct(h, bands)
    h_last = bands[-1][1] - 1
    return pd.DataFrame({"order": h, "f_Hz": h * f, "ieee519_pct": lim519,
                         "ext03_pct": np.where(h > h_last, EXT_PCT, np.nan), "trd_pct": TRD_PCT})


# ==================================================================== #
# Calculation
# ==================================================================== #

def define_cases(sigma_nom):
    """Unique (model, d, sigma, loading) combinations."""
    cases = [("dowell", d, sigma_nom, 1.0) for d in D_SWEEP]
    cases += [("dowell", d, s, 1.0) for d in D_SIGMA for s in (SIGMA_LOW, SIGMA_HIGH)]
    cases += [("dowell", D_NOMINAL, sigma_nom, k) for k in LOADINGS if k != 1.0]
    cases += [("h2", None, sigma_nom, 1.0)]
    return cases


def tolerable_current(trafo, h, I_h, f, T_amb_C, L_normal_years, model, thickness, sigma, loading):
    """I_h* [A] per order for one case."""
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma, eddy_share=trafo["eddy_share"])
    w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=f, conductor_thickness=thickness,
                                         rho=trafo["conductor_resistivity"], model="dowell")
    _, Life = CF.calculate_harmonic_sensitivity_map(trafo_specs=trafo, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                    h_orders=h, I_h_values=I_h, I_1=loading * trafo["I_R"],
                                                    T_amb_C=T_amb_C, eddy_weights=w)
    return CF.iso_life_current(I_h_values=I_h, Life_years=Life, L_target=L_normal_years)


def run_cases(trafo, h, I_h, f, T_amb_C, L_normal_years):
    I_R = trafo["I_R"]
    cases = define_cases(trafo["sigma"])
    frames = []
    for n, (model, d, sigma, loading) in enumerate(cases, 1):
        thickness = None if model == "h2" else d
        I_star = tolerable_current(trafo, h, I_h, f, T_amb_C, L_normal_years, model, thickness, sigma, loading)
        frames.append(pd.DataFrame({
            "model": model, "d_mm": np.nan if thickness is None else round(d * 1e3, 2),
            "sigma": sigma, "loading_pu": loading, "order": h, "f_Hz": h * f,
            "I_star_A": I_star, "I_star_pct": 100.0 * I_star / I_R}))
        print(f"  [{n:2d}/{len(cases)}] {model:6s} d = {'-' if thickness is None else f'{d * 1e3:g} mm':7s} "
              f"sigma = {sigma * 100:4.1f} %  I1 = {loading:.2f} pu")
    return pd.concat(frames, ignore_index=True)


def case_label(model, d_mm, sigma, loading, sigma_nom):
    """LaTeX row label for Table tab:limits."""
    s = "$h^2$" if model == "h2" else f"$d={d_mm:g}$\\,mm"
    if not np.isclose(sigma, sigma_nom):
        s += f", $\\sigma={sigma * 100:g}\\%$"
    if not np.isclose(loading, 1.0):
        s += f", {loading:g}\\,pu"
    return s


def summarise(df, limits, f, sigma_nom):
    """
    Per case:
      margin_519      smallest I_h* / IEEE 519 limit over h <= 50
      h_margin        order of that margin
      f_below03_kHz   first frequency above h = 50 with I_h* below the extended 0.3 % (NaN = not up to h_max)
      f_trd_kHz       first frequency above h = 50 with I_h* below the 5 % TRD
      trd_x_10kHz     5 % TRD / I_h* at F_REPORT_KHZ
    """
    lim519 = limits.set_index("order")["ieee519_pct"]
    h_last = int(lim519.dropna().index.max())
    h_rep = int(round(F_REPORT_KHZ * 1e3 / f))
    rows = []
    for (model, d_mm, sigma, loading), g in df.groupby(["model", "d_mm", "sigma", "loading_pu"], dropna=False, sort=False):
        I = g.set_index("order")["I_star_pct"]
        low = I.index <= h_last
        margin = (I[low] / lim519.reindex(I.index[low])).dropna()
        high = I.index > h_last
        below03 = I.index[high & (I.values < EXT_PCT)]
        trd = I.index[high & (I.values < TRD_PCT)]
        rows.append({
            "label": case_label(model, d_mm, sigma, loading, sigma_nom),
            "model": model, "d_mm": d_mm, "sigma": sigma, "loading_pu": loading,
            "margin_519": margin.min(), "h_margin": int(margin.idxmin()),
            "f_below03_kHz": below03[0] * f / 1e3 if below03.size else np.nan,
            "f_trd_kHz": trd[0] * f / 1e3 if trd.size else np.nan,
            "I_star_10kHz_pct": I.get(h_rep, np.nan),
            "trd_x_10kHz": TRD_PCT / I.get(h_rep, np.nan),
        })
    s = pd.DataFrame(rows)
    s["_h2"] = s["model"] == "h2"
    return s.sort_values(["_h2", "loading_pu", "sigma", "d_mm"], ascending=[True, False, True, True]).drop(columns="_h2")


def print_summary(s):
    print("\n Summary (Table tab:limits)")
    with pd.option_context("display.width", 250, "display.max_columns", 20):
        print(s.drop(columns="label").round(3).to_string(index=False))

    def fmt(v):
        return "--" if not np.isfinite(v) else f"{v:.3g}"

    print("\n LaTeX rows: Case & Margin to 519 & Below 0.3% from [kHz] & TRD exceeded from [kHz] & TRD/I* at 10 kHz")
    for _, r in s.iterrows():
        print(f"{r['label']} & {r['margin_519']:.1f} & {fmt(r['f_below03_kHz'])} & {fmt(r['f_trd_kHz'])} "
              f"& {r['trd_x_10kHz']:.1f} \\\\")


# ==================================================================== #
# Main (computation only)
# ==================================================================== #

def main():
    CF.self_test(verbose=True)
    make_output_dirs()

    params, trafo = load_inputs()
    f, h_max = params.f, params.h_max
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    L_normal_years = trafo["L_normal"] / (365.0 * 24.0)
    print_inputs(trafo, f, T_amb_C)

    h = np.arange(H_MIN, h_max + 1)
    I_h = np.geomspace(I_MIN_PU * trafo["I_R"], I_MAX_PU * trafo["I_R"], N_CURRENT)
    limits = limits_table(h, params.emission_limits["bands"], f)
    limits.to_csv(DATAFRAMES_DIR / "dowell_limits.csv", index=False)

    print("\n Computing tolerable currents")
    df = run_cases(trafo, h, I_h, f, T_amb_C, L_normal_years)
    df.to_csv(DATAFRAMES_DIR / "dowell_tolerable_current.csv", index=False)

    s = summarise(df, limits, f, trafo["sigma"])
    s.to_csv(DATAFRAMES_DIR / "dowell_summary.csv", index=False)
    print_summary(s)
    print(f"\n Dataframes written to {DATAFRAMES_DIR}")


# ==================================================================== #
# Plotting (reads the saved CSVs, independent of main)
# ==================================================================== #

def curve(df, model, d_mm, sigma, loading_pu):
    """One I_h* curve, NaN-safe for d_mm (h^2)."""
    m = (df["model"] == model) & np.isclose(df["sigma"], sigma) & np.isclose(df["loading_pu"], loading_pu)
    m &= df["d_mm"].isna() if d_mm is None else np.isclose(df["d_mm"].fillna(-1), d_mm)
    g = df[m].sort_values("order")
    return g["order"].to_numpy(), g["I_star_pct"].to_numpy()


def draw_limits(ax, limits, h_max):
    """IEEE 519 step line to h = 50, the 0.3 % limit extended, the 5 % TRD."""
    lim = limits.dropna(subset=["ieee519_pct"])
    x = np.append(lim["order"].to_numpy(), lim["order"].iloc[-1] + 1)
    ax.stairs(lim["ieee519_pct"].to_numpy(), x - 0.5, baseline=None, color="tab:red", linewidth=2.0, zorder=4)
    ax.plot([lim["order"].iloc[-1] + 0.5, h_max], [EXT_PCT, EXT_PCT], color="tab:red", linestyle="--", linewidth=1.6, zorder=4)
    ax.axhline(TRD_PCT, color="black", linestyle="-.", linewidth=1.4, zorder=4)


def limit_handles():
    return [Line2D([], [], color="tab:red", linewidth=2.0, label="IEEE 519 limit"),
            Line2D([], [], color="tab:red", linestyle="--", linewidth=1.6, label="0.3 % extended"),
            Line2D([], [], color="black", linestyle="-.", linewidth=1.4, label="IEEE 1547 TRD")]


def style_axis(ax, h_max, ylim_pct):
    ax.set_yscale("log")
    ax.set_ylim(*ylim_pct)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Tolerable current $I_h^*$ [% of Rated Current]")
    ax.grid(True, which="major", alpha=0.3)


def save(fig, fname):
    for ext in ("png","png"):
        fig.savefig(FIGURES_DIR / f"{fname}.{ext}", dpi=600)
    plt.close(fig)


def plot_main(df, limits, h_max, sigma_nom, ylim_pct=YLIM_PCT, fname="limits_dowell"):
    """d = 1 to 4 mm at rated load and nominal sigma, nominal thickness bold."""
    fig, ax = plt.subplots(figsize=FIGSIZE, constrained_layout=True)
    draw_limits(ax, limits, h_max)

    ds = sorted(df.loc[(df.model == "dowell") & np.isclose(df.sigma, sigma_nom) & np.isclose(df.loading_pu, 1.0), "d_mm"].unique())
    colors = plt.cm.viridis(np.linspace(0.0, 0.88, len(ds)))
    handles = []
    for d, c in zip(ds, colors):
        nominal = np.isclose(d, D_NOMINAL * 1e3)
        x, y = curve(df, "dowell", d, sigma_nom, 1.0)
        ax.plot(x, y, color=c, linewidth=3.0 if nominal else 1.4, zorder=5 if nominal else 3)
        handles.append(Line2D([], [], color=c, linewidth=3.0 if nominal else 1.4,
                              label=f"$d$ = {d:g} mm" + (" (nominal)" if nominal else "")))

    if SHOW_SIGMA_BAND:
        x, lo = curve(df, "dowell", D_NOMINAL * 1e3, SIGMA_HIGH, 1.0)
        _, hi = curve(df, "dowell", D_NOMINAL * 1e3, SIGMA_LOW, 1.0)
        ax.fill_between(x, lo, hi, color="grey", alpha=0.2, linewidth=0, zorder=2)
        handles.append(Patch(facecolor="grey", alpha=0.3,
                             label=f"$\\sigma$ = {SIGMA_LOW * 100:g} to {SIGMA_HIGH * 100:g} %"))

    if SHOW_H2_REFERENCE:
        x, y = curve(df, "h2", None, sigma_nom, 1.0)
        ax.plot(x, y, color="grey", linestyle=":", linewidth=1.8, zorder=3)
        handles.append(Line2D([], [], color="grey", linestyle=":", linewidth=1.8, label="$h^2$ reference"))

    style_axis(ax, h_max, ylim_pct)
    fig.legend(handles=handles + limit_handles(), loc="outside lower center", ncol=3, frameon=False, **LEGEND_KW)
    save(fig, fname)


def plot_loading(df, limits, h_max, sigma_nom, ylim_pct=YLIM_PCT, fname="limits_dowell_loading"):
    """Fundamental loading 0.5, 0.75, 1 pu at the nominal thickness."""
    fig, ax = plt.subplots(figsize=FIGSIZE, constrained_layout=True)
    draw_limits(ax, limits, h_max)
    colors = plt.cm.plasma(np.linspace(0.05, 0.75, len(LOADINGS)))
    handles = []
    for k, c in zip(LOADINGS, colors):
        x, y = curve(df, "dowell", D_NOMINAL * 1e3, sigma_nom, k)
        ax.plot(x, y, color=c, linewidth=2.0)
        handles.append(Line2D([], [], color=c, linewidth=2.0, label=f"$I_1$ = {k:g} pu"))
    style_axis(ax, h_max, ylim_pct)
    ax.set_title(f"Diffusion, $d$ = {D_NOMINAL * 1e3:g} mm")
    fig.legend(handles=handles + limit_handles(), loc="outside lower center", ncol=3, frameon=False, **LEGEND_KW)
    save(fig, fname)


def plot_sigma(df, limits, h_max, sigma_nom, ylim_pct=YLIM_PCT, fname="limits_dowell_sigma"):
    """Band between sigma = 3 and 15 %, line at nominal sigma, for d = 1, 2.5, 4 mm."""
    fig, ax = plt.subplots(figsize=FIGSIZE, constrained_layout=True)
    draw_limits(ax, limits, h_max)
    colors = plt.cm.viridis(np.linspace(0.0, 0.88, len(D_SIGMA)))
    handles = []
    for d, c in zip(D_SIGMA, colors):
        d_mm = d * 1e3
        x, lo = curve(df, "dowell", d_mm, SIGMA_HIGH, 1.0)      # larger sigma -> lower I_h*
        _, hi = curve(df, "dowell", d_mm, SIGMA_LOW, 1.0)
        _, mid = curve(df, "dowell", d_mm, sigma_nom, 1.0)
        ax.fill_between(x, lo, hi, color=c, alpha=0.25, linewidth=0)
        ax.plot(x, mid, color=c, linewidth=1.9)
        handles.append(Patch(facecolor=c, alpha=0.4, edgecolor=c, label=f"$d$ = {d_mm:g} mm"))
    handles.append(Line2D([], [], color="grey", linewidth=1.9, label=f"line: $\\sigma$ = {sigma_nom * 100:g} %"))
    style_axis(ax, h_max, ylim_pct)
    ax.set_title(f"Diffusion, $\\sigma$ = {SIGMA_LOW * 100:g} to {SIGMA_HIGH * 100:g} %")
    fig.legend(handles=handles + limit_handles(), loc="outside lower center", ncol=3, frameon=False, **LEGEND_KW)
    save(fig, fname)


def plot_results(ylim_pct=YLIM_PCT):
    params, trafo = load_inputs()
    df = pd.read_csv(DATAFRAMES_DIR / "dowell_tolerable_current.csv")
    limits = pd.read_csv(DATAFRAMES_DIR / "dowell_limits.csv")
    sigma_nom = trafo["sigma"]
    plot_main(df, limits, params.h_max, sigma_nom, ylim_pct)
    plot_loading(df, limits, params.h_max, sigma_nom, ylim_pct)
    plot_sigma(df, limits, params.h_max, sigma_nom, ylim_pct)
    print(f" Figures written to {FIGURES_DIR}")


if __name__ == "__main__":
    main()
    plot_results()
