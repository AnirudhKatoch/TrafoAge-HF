"""
limits_study.py

Tolerable harmonic current I_h* of the transformer against the emission limits.

    I_h* = harmonic current of order h which, on top of the fundamental, brings
           the hot spot to Theta_ref (life = normal life). Steady state.

Three sweeps, each evaluated for the three winding eddy-loss weightings
(C57.110 square law h^2, C57.110 Annex C, Dowell diffusion):

    1. thickness  d = 1.0, 1.5, ... 4.0 mm            rated load, nominal sigma
    2. loading    I_1 = 0.5, 0.75, 1.0 pu             d = 2.5 mm, nominal sigma
    3. sigma      3 to 15 % shown as a band           d = 1, 2.5, 4 mm, rated load

The square law does not depend on d, so it appears once in sweeps 1 and 3.

Every figure carries
    - the IEEE 519-2022 Table 2 limits, row Isc/IL < 20 (binds generation, footnote c),
      with footnote a (even h <= 6 at 50 %), up to h = 50
    - the 0.3 % limit of 35 <= h <= 50 extended (dashed) to h_max. No standard sets it,
      it only shows where I_h* falls below the strictest existing per-order limit
    - the 5 % TRD of IEEE 1547-2018 Sec. 7.3, the only limit above h = 50

Limits are drawn in % of the transformer rated current, i.e. the converter or load
is taken to be rated at the transformer rating (assumed).

All physics comes from Calculation_functions.py. This script only sweeps, saves and plots.

Outputs
    IEEE_Results/Dataframes/tolerable_current_all.csv   I_h* of every case, long format
    IEEE_Results/Dataframes/limits.csv                   limit lines per order
    IEEE_Results/Dataframes/crossing_summary.csv         where each case crosses each limit
    IEEE_Results/Figures/limits_<group>_<model>.png/.pdf 9 single figures
    IEEE_Results/Figures/limits_<group>.png/.pdf         3 figures with three panels each
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
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})


# ==================================================================== #
# Settings
# ==================================================================== #

RESULTS_DIR = Path(os.environ.get("IEEE_RESULTS_DIR", r"E:\IEEE_GM_2027_Transformer\IEEE_Results"))
FIGURES_DIR = RESULTS_DIR / "Figures"
DATAFRAMES_DIR = RESULTS_DIR / "Dataframes"

H_MIN = 2                                   # [-]  lowest order (h = 1 is the fundamental itself)
N_CURRENT = 2000                            # [-]  current steps of the map behind I_h* (fine, so interpolation error is negligible)
I_MIN_PU, I_MAX_PU = 1e-4, 3.0              # [pu] current range of that map; above 1 pu so part-load boundaries stay inside

D_NOMINAL = 2.5e-3                          # [m]  nominal conductor thickness
D_SWEEP = np.round(np.arange(1.0, 4.0 + 1e-9, 0.5), 2) * 1e-3   # [m] 1.0, 1.5, ... 4.0 mm
D_BANDS = [1.0e-3, 2.5e-3, 4.0e-3]          # [m]  thicknesses shown in the sigma-band figures
LOADING_SWEEP = [0.5, 0.75, 1.0]            # [pu] fundamental current / I_R
SIGMA_RANGE = (0.03, 0.15)                  # [-]  stray fraction band

TRD_PCT = 5.0                               # [%]  IEEE 1547-2018 Table 26, total rated-current distortion
EXT_PCT = 0.3                               # [%]  last per-order limit of IEEE 519 Table 2 (35 <= h <= 50), extended
REPORT_KHZ = [10.0, 25.0]                   # [kHz] frequencies at which the TRD exceedance is reported

MODELS = [                                  # (key, model passed to the weighting, short title)
    ("h2",     None,     "C57.110, $w(h) = h^2$"),
    ("annexC", "annexC", "Annex C"),
    ("dowell", "dowell", "Diffusion"),
]

YLIM_PCT = (0.1, 100.0)                     # [% of I_R] y-axis limits of all figures
FIGSIZE_ROW = (6.4 * 2, 4.8 * 1.25)         # three panels side by side
FIGSIZE_SINGLE = (6.4, 4.8 * 1.45)          # one panel, legend below


# ==================================================================== #
# Setup
# ==================================================================== #

def make_output_dirs():
    """Create IEEE_Results/Figures and IEEE_Results/Dataframes if they do not exist."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    DATAFRAMES_DIR.mkdir(parents=True, exist_ok=True)


def load_inputs():
    """Transformer data and study settings from Input_parameters.py."""
    params = Input_parameters_class()
    return params, params.trafo_specs


def print_inputs(trafo, f, T_amb_C):
    """Print every input the boundaries depend on, so a wrong value is seen before the run."""
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
    print(f"  Frequency                  {f:.0f} Hz")


# ==================================================================== #
# Limits
# ==================================================================== #

def ieee519_limit_pct(h, bands):
    """
    IEEE 519-2022 Table 2 (Isc/IL < 20) per order, in % of I_L, NaN above the last band.
    Footnote a: even harmonics h <= 6 limited to 50 % of the table values.
    """
    h = np.asarray(h)
    lim = np.full(h.shape, np.nan)
    for h0, h1, pct in bands:
        lim[(h >= h0) & (h < h1)] = pct
    lim[(h % 2 == 0) & (h <= 6)] *= 0.5
    return lim


def limits_table(h, bands, f):
    """Every limit line per order, saved once and reused by the plots."""
    lim519 = ieee519_limit_pct(h, bands)
    h_last = bands[-1][1] - 1
    return pd.DataFrame({
        "order": h, "f_Hz": h * f,
        "ieee519_pct": lim519,
        "ext03_pct": np.where(h > h_last, EXT_PCT, np.nan),
        "trd_pct": TRD_PCT,
    })


# ==================================================================== #
# Calculation
# ==================================================================== #

def build_grids(h_max, I_R):
    """Orders H_MIN ... h_max and log-spaced harmonic currents [A] of the map behind I_h*."""
    return np.arange(H_MIN, h_max + 1), np.geomspace(I_MIN_PU * I_R, I_MAX_PU * I_R, N_CURRENT)


def tolerable_current(trafo, h, I_h, f, T_amb_C, L_normal_years, model, thickness, sigma, loading):
    """I_h* [A] per order for one case (model, thickness, sigma, loading)."""
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma, eddy_share=trafo["eddy_share"])
    w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=f, conductor_thickness=thickness,
                                         rho=trafo["conductor_resistivity"], model=model or "dowell")
    _, Life = CF.calculate_harmonic_sensitivity_map(trafo_specs=trafo, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                    h_orders=h, I_h_values=I_h, I_1=loading * trafo["I_R"],
                                                    T_amb_C=T_amb_C, eddy_weights=w)
    return CF.iso_life_current(I_h_values=I_h, Life_years=Life, L_target=L_normal_years)


def define_cases(sigma_nominal):
    """Every (group, model, thickness, sigma, loading) combination of the three sweeps."""
    cases = []
    for key, model, _ in MODELS:
        ds = [None] if model is None else list(D_SWEEP)
        cases += [("thickness", key, model, d, sigma_nominal, 1.0) for d in ds]

        d = None if model is None else D_NOMINAL
        cases += [("loading", key, model, d, sigma_nominal, k) for k in LOADING_SWEEP]

        ds = [None] if model is None else D_BANDS
        for d in ds:
            cases += [("sigma", key, model, d, s, 1.0) for s in (SIGMA_RANGE[0], sigma_nominal, SIGMA_RANGE[1])]
    return cases


def run_cases(trafo, h, I_h, f, T_amb_C, L_normal_years):
    """Compute I_h* for every case and return them in long format."""
    I_R = trafo["I_R"]
    frames = []
    cases = define_cases(trafo["sigma"])
    for n, (group, key, model, d, sigma, loading) in enumerate(cases, 1):
        I_star = tolerable_current(trafo, h, I_h, f, T_amb_C, L_normal_years, model, d, sigma, loading)
        frames.append(pd.DataFrame({
            "group": group, "model": key,
            "d_mm": np.nan if d is None else round(d * 1e3, 2),
            "sigma": sigma, "loading_pu": loading,
            "order": h, "f_Hz": h * f,
            "I_star_A": I_star, "I_star_pct": 100.0 * I_star / I_R,
        }))
        print(f"  [{n:2d}/{len(cases)}] {group:9s} {key:6s} d = {'-' if d is None else f'{d * 1e3:g} mm':7s} "
              f"sigma = {sigma * 100:4.1f} %  I1 = {loading:.2f} pu")
    return pd.concat(frames, ignore_index=True)


def crossing_summary(df, limits, f):
    """
    For every case, where it meets each limit:
      margin_519_min   smallest I_h* / IEEE 519 limit over h <= 50 (below 1 = the limit itself is not protective)
      h_margin_min     order of that smallest margin
      h_cross_ext03    first order above 50 with I_h* below the extended 0.3 % (NaN = never up to h_max)
      h_trd_from       first order above 50 with I_h* below the 5 % TRD
      trd_x_<f>kHz     5 % TRD / I_h* at that frequency (above 1 = a TRD-compliant converter can over-age the unit)
    """
    lim = limits.set_index("order")
    h_last519 = int(limits.loc[limits["ieee519_pct"].notna(), "order"].max())
    rows = []
    for keys, g in df.groupby(["group", "model", "d_mm", "sigma", "loading_pu"], dropna=False, sort=False):
        g = g.set_index("order")
        I = g["I_star_pct"]
        low = I.index <= h_last519
        margin = (I[low] / lim.loc[I.index[low], "ieee519_pct"]).dropna()
        high = I.index > h_last519
        cross03 = I.index[high & (I.values < EXT_PCT)]
        crosstrd = I.index[high & (I.values < TRD_PCT)]
        r = dict(zip(["group", "model", "d_mm", "sigma", "loading_pu"], keys))
        r.update({
            "margin_519_min": margin.min(), "h_margin_min": int(margin.idxmin()),
            "fails_519": bool(margin.min() < 1.0),
            "h_cross_ext03": int(cross03[0]) if cross03.size else np.nan,
            "f_cross_ext03_kHz": cross03[0] * f / 1e3 if cross03.size else np.nan,
            "h_trd_from": int(crosstrd[0]) if crosstrd.size else np.nan,
        })
        for k in REPORT_KHZ:
            ho = int(round(k * 1e3 / f))
            r[f"trd_x_{k:g}kHz"] = TRD_PCT / I.get(ho, np.nan)
            r[f"I_star_{k:g}kHz_pct"] = I.get(ho, np.nan)
        rows.append(r)
    return pd.DataFrame(rows)


def print_summary(summary):
    cols = ["group", "model", "d_mm", "sigma", "loading_pu", "margin_519_min", "h_margin_min",
            "h_cross_ext03", "f_cross_ext03_kHz", "h_trd_from"] + \
           [c for c in summary.columns if c.startswith("trd_x_") or c.startswith("I_star_")]
    print("\n Where each case meets the limits")
    with pd.option_context("display.width", 250, "display.max_columns", 30, "display.max_rows", 200):
        print(summary[cols].round(3).to_string(index=False))


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

    h, I_h = build_grids(h_max, trafo["I_R"])
    limits = limits_table(h, params.emission_limits["bands"], f)
    limits.to_csv(DATAFRAMES_DIR / "limits.csv", index=False)

    print("\n Computing tolerable currents")
    df = run_cases(trafo, h, I_h, f, T_amb_C, L_normal_years)
    df.to_csv(DATAFRAMES_DIR / "tolerable_current_all.csv", index=False)

    summary = crossing_summary(df, limits, f)
    summary.to_csv(DATAFRAMES_DIR / "crossing_summary.csv", index=False)
    print_summary(summary)
    print(f"\n Dataframes written to {DATAFRAMES_DIR}")


# ==================================================================== #
# Plotting (reads the saved CSVs, independent of main)
# ==================================================================== #

def draw_limits(ax, limits, h_max):
    """IEEE 519 step line to h = 50, the 0.3 % limit extended to h_max, and the 5 % TRD."""
    lim = limits.dropna(subset=["ieee519_pct"])
    x = np.append(lim["order"].to_numpy(), lim["order"].iloc[-1] + 1)
    ax.stairs(lim["ieee519_pct"].to_numpy(), x - 0.5, baseline=None, color="tab:red", linewidth=2.0, zorder=4)
    ax.plot([lim["order"].iloc[-1] + 0.5, h_max], [EXT_PCT, EXT_PCT], color="tab:red", linestyle="--", linewidth=1.6, zorder=4)
    ax.axhline(TRD_PCT, color="black", linestyle="-.", linewidth=1.4, zorder=4)


def limit_handles():
    return [Line2D([], [], color="tab:red", linewidth=2.0, label="IEEE 519 limit"),
            Line2D([], [], color="tab:red", linestyle="--", linewidth=1.6, label="0.3 % extended"),
            Line2D([], [], color="black", linestyle="-.", linewidth=1.4, label="IEEE 1547 TRD")]


def mark_crossing(ax, h, I_pct, color, h_last519=50):
    """Dot where the curve first drops below the extended 0.3 % line."""
    m = (h > h_last519) & (I_pct < EXT_PCT)
    if m.any():
        ax.plot(h[m][0], EXT_PCT, "o", color=color, markeredgecolor="black", markersize=8, zorder=6)


def style_axis(ax, h_max, ylim_pct, title, ylabel):
    ax.set_yscale("log")
    ax.set_ylim(*ylim_pct)
    ax.set_xlim(0, h_max)
    ax.set_title(title)
    ax.set_xlabel("Harmonic order $h$")
    if ylabel:
        ax.set_ylabel("Tolerable current $I_h^*$ [% of Rated Current]")
    ax.grid(True, which="major", alpha=0.3)


def curve(df, **sel):
    """One I_h* curve selected by column values (NaN-safe for d_mm)."""
    m = np.ones(len(df), dtype=bool)
    for k, v in sel.items():
        m &= df[k].isna().to_numpy() if (v is None or (isinstance(v, float) and np.isnan(v))) else np.isclose(df[k], v)
    g = df[m].sort_values("order")
    return g["order"].to_numpy(), g["I_star_pct"].to_numpy()


def panel_thickness(ax, df, key, title_base, h_max):
    """d = 1 ... 4 mm, coloured by thickness. The square law is d-independent."""
    g = df[(df.group == "thickness")]
    hh, Ih2 = curve(g[g.model == "h2"], d_mm=None)
    handles = []
    if key == "h2":
        ax.plot(hh, Ih2, color="black", linewidth=2.2)
        mark_crossing(ax, hh, Ih2, "black")
        handles.append(Line2D([], [], color="black", linewidth=2.2, label="$h^2$ (independent of $d$)"))
        title = title_base
    else:
        ds = sorted(g.loc[g.model == key, "d_mm"].unique())
        colors = plt.cm.viridis(np.linspace(0.0, 0.88, len(ds)))
        ax.plot(hh, Ih2, color="grey", linestyle=":", linewidth=1.8)
        for d, c in zip(ds, colors):
            x, y = curve(g[g.model == key], d_mm=d)
            ax.plot(x, y, color=c, linewidth=1.8)
            mark_crossing(ax, x, y, c)
            handles.append(Line2D([], [], color=c, linewidth=1.8, label=f"$d$ = {d:g} mm"))
        handles.append(Line2D([], [], color="grey", linestyle=":", linewidth=1.8, label="$h^2$ reference"))
        title = f"{title_base}, $d$ = {ds[0]:g} to {ds[-1]:g} mm"
    return title, handles


def panel_loading(ax, df, key, title_base, h_max):
    """Fundamental loading 0.5, 0.75, 1.0 pu at the nominal thickness."""
    g = df[(df.group == "loading") & (df.model == key)]
    ks = sorted(g["loading_pu"].unique())
    colors = plt.cm.plasma(np.linspace(0.05, 0.75, len(ks)))
    handles = []
    for k, c in zip(ks, colors):
        x, y = curve(g, loading_pu=k)
        ax.plot(x, y, color=c, linewidth=1.9)
        mark_crossing(ax, x, y, c)
        handles.append(Line2D([], [], color=c, linewidth=1.9, label=f"$I_1$ = {k:g} pu"))
    d = g["d_mm"].dropna().unique()
    title = title_base if key == "h2" else f"{title_base}, $d$ = {d[0]:g} mm"
    return title, handles


def panel_sigma(ax, df, key, title_base, h_max):
    """Band between sigma = 3 and 15 %, line at the nominal sigma, one band per thickness."""
    g = df[(df.group == "sigma") & (df.model == key)]
    s_lo, s_hi = SIGMA_RANGE
    s_nom = [s for s in g["sigma"].unique() if not np.isclose(s, s_lo) and not np.isclose(s, s_hi)][0]
    ds = [None] if key == "h2" else sorted(g["d_mm"].dropna().unique())
    colors = ["black"] if key == "h2" else plt.cm.viridis(np.linspace(0.0, 0.88, len(ds)))
    handles = []
    for d, c in zip(ds, colors):
        x, lo = curve(g, d_mm=d, sigma=s_hi)          # larger sigma -> more eddy loss -> lower I_h*
        _, hi = curve(g, d_mm=d, sigma=s_lo)
        _, mid = curve(g, d_mm=d, sigma=s_nom)
        ax.fill_between(x, lo, hi, color=c, alpha=0.25, linewidth=0)
        ax.plot(x, mid, color=c, linewidth=1.9)
        mark_crossing(ax, x, mid, c)
        m = (x > 50) & (lo < EXT_PCT)                   # band edge (largest sigma) crossing the extended 0.3 %
        if m.any():
            ax.plot(x[m][0], EXT_PCT, "o", markerfacecolor="white", markeredgecolor=c, markeredgewidth=2,
                    markersize=8, zorder=6)
        lab = "$h^2$" if d is None else f"$d$ = {d:g} mm"
        handles.append(Patch(facecolor=c, alpha=0.4, edgecolor=c, label=lab))
    handles.append(Line2D([], [], color="grey", linewidth=1.9, label=f"line: $\\sigma$ = {s_nom * 100:g} %"))
    title = f"{title_base}, $\\sigma$ = {s_lo * 100:g} to {s_hi * 100:g} %"
    return title, handles


PANELS = {"thickness": panel_thickness, "loading": panel_loading, "sigma": panel_sigma}


def plot_group(group, df, limits, h_max, ylim_pct=YLIM_PCT):
    """Three panels side by side (h^2, Annex C, Diffusion), plus each panel as its own figure."""
    draw = PANELS[group]

    # Row of three panels, one shared legend below
    fig, axes = plt.subplots(1, 3, figsize=FIGSIZE_ROW, sharey=True, constrained_layout=True)
    legend = {}
    for i, (ax, (key, _, title_base)) in enumerate(zip(axes, MODELS)):
        draw_limits(ax, limits, h_max)
        title, handles = draw(ax, df, key, title_base, h_max)
        style_axis(ax, h_max, ylim_pct, title, ylabel=(i == 0))
        for hd in handles:
            legend.setdefault(hd.get_label(), hd)
    for hd in limit_handles():
        legend[hd.get_label()] = hd
    fig.legend(handles=list(legend.values()), loc="outside lower center", ncol=min(5, len(legend)), frameon=False)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES_DIR / f"limits_{group}.{ext}", dpi=300)

    plt.close(fig)

    # The same three panels as single figures
    for key, _, title_base in MODELS:
        fig, ax = plt.subplots(figsize=FIGSIZE_SINGLE, constrained_layout=True)
        draw_limits(ax, limits, h_max)
        title, handles = draw(ax, df, key, title_base, h_max)
        style_axis(ax, h_max, ylim_pct, title, ylabel=True)
        fig.legend(handles=handles + limit_handles(), loc="outside lower center", ncol=3, frameon=False)
        for ext in ("png", "pdf"):
            fig.savefig(FIGURES_DIR / f"limits_{group}_{key}.{ext}", dpi=300)
        plt.close(fig)


def plot_results(ylim_pct=YLIM_PCT):
    """Read the saved CSVs and make all nine single figures and the three row figures."""
    params = Input_parameters_class()
    df = pd.read_csv(DATAFRAMES_DIR / "tolerable_current_all.csv")
    limits = pd.read_csv(DATAFRAMES_DIR / "limits.csv")
    for group in PANELS:
        plot_group(group, df, limits, params.h_max, ylim_pct)
    print(f" Figures written to {FIGURES_DIR}")


if __name__ == "__main__":
    main()
    plot_results()
