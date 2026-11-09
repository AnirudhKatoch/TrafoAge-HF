"""
heatmap_study.py

Life maps of the transformer, one per winding eddy-loss model:

    1. C57.110 square law            w(h) = h^2
    2. C57.110 Annex C               w(h) = h^1.5 G(xi_1 sqrt h) / G(xi_1),  s = -1, d = 2.5 mm
    3. Dowell diffusion solution     w(h) = h^0.5 G(xi_1 sqrt h) / G(xi_1),  s = +1, d = 2.5 mm

Each map places ONE current of order h and RMS value I_h on the transformer, with
NO other current flowing (no fundamental), and evaluates the steady-state chain

    losses -> top oil -> hot-spot gradient -> hot spot -> ageing -> life

h = 1 is the fundamental itself, so every order, the fundamental included, is
treated the same way. The colour is the equivalent life if that current flowed
indefinitely. The maximum current I_h,max (hot spot at Theta_ref, life = L_normal)
is extracted for every order and model. These are the currents of the harmonic budget.

All transformer data are read from Input_parameters.py. All physics comes
from Calculation_functions.py, so this script contains no new equations.

Outputs
    Dataframes/heatmap_<model>.csv      every map point (order, I_h, hot spot, life)
    Dataframes/tolerable_current.csv    I_h,max per order for every model
    Figures/heatmap_<model>.png         one map per model
    Figures/life_maps.png / .pdf        three maps side by side
"""
from pathlib import Path

import numpy as np
import pandas as pd

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF
from Plotting_function import Plotting_functions_class as PF

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})


# ==================================================================== #
# Settings
# ==================================================================== #

RESULTS_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Dataframes")
FIGURES_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures")

D_CONDUCTOR = 2.5e-3      # [m]  Conductor (LV foil) thickness used by Annex C and Dowell
I_1 = 0.0                 # [A]  No fundamental: each order flows alone
H_MIN = 1                 # [-]  Lowest order on the map (h = 1 is the fundamental)
H_MAX = 334               # [-]  Highest order, 20 kHz at 60 Hz, validity limit of the diffusion solution
N_CURRENT = 500           # [-]  Number of current steps on the map
I_MIN_PU = 1e-4           # [pu] Smallest current, as a fraction of I_R
I_MAX_PU = 1.0            # [pu] Largest current, as a fraction of I_R
                          #      (the h = 1 line lies just above I_R, set 1.2 to show it)

D_SWEEP = np.arange(1.0e-3, 4.0e-3 + 1e-9, 0.5e-3)     # [m] 1.0, 1.5, ..., 4.0 mm

MODELS = [
    ("C57110_h2",   None,        "dowell", "C57.110 (h^2)"),
    ("AnnexC_nom",  D_CONDUCTOR, "annexC", f"Annex C, d = {D_CONDUCTOR * 1e3:g} mm"),
    ("Dowell_nom",  D_CONDUCTOR, "dowell", f"Diffusion, d = {D_CONDUCTOR * 1e3:g} mm"),
]

YLIM_PCT = (0.25, 100.0)      # [% of I_R] y-axis limits of the life maps

PLOT_TITLES = {               # panel headings, in the order h^2, Annex C, Dowell
    "C57110_h2":  "C57.110 square law",
    "AnnexC_nom": "C57.110 Annex C",
    "Dowell_nom": "Dowell diffusion",
}

REPORT_ORDERS = [1, 2, 50, 100, 167, 250, 334]   # orders at which I_h,max is printed (334 = 20 kHz at 60 Hz)


# ==================================================================== #
# Setup
# ==================================================================== #

def make_output_dirs():
    """Create the result and figure folders if they do not exist."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_inputs():
    """Read the transformer data and study settings from Input_parameters.py."""
    params = Input_parameters_class()
    return params, params.trafo_specs


def print_inputs(trafo, f, T_amb_C):
    """Print the inputs the maps depend on, so a wrong value is seen before the run."""
    print("\n Inputs of the life maps")
    print(f"  Rated power                {trafo['S_r'] / 1e6:.2f} MVA")
    print(f"  LV voltage                 {trafo['V_LV']:.0f} V")
    print(f"  Rated LV current I_R       {trafo['I_R']:.1f} A")
    print(f"  Other current on the map   {I_1:.1f} A (each order alone)")
    print(f"  Load / no-load loss        {trafo['P_LL_R']:.0f} W / {trafo['P_NL']:.0f} W")
    print(f"  sigma / eddy share         {trafo['sigma']:.3f} / {trafo['eddy_share']:.3f}")
    print(f"  Concentration c            {trafo['eddy_hotspot_factor']:.2f}")
    print(f"  Exponents x / y (loss)     {trafo['x_oil']:.2f} / {trafo['y_winding']:.2f}")
    print(f"  Rated rises TO / g         {trafo['Theta_TO_R']:.0f} K / {trafo['Theta_g_R']:.0f} K")
    print(f"  Ambient                    {T_amb_C:.1f} degC")
    print(f"  Theta_ref / L_normal       {trafo['Theta_ref']:.0f} degC / {trafo['L_normal']:.0f} h")
    print(f"  Conductor thickness d      {D_CONDUCTOR * 1e3:.1f} mm")
    print(f"  Frequency                  {f:.0f} Hz")
    print(f"  Orders                     {H_MIN} to {H_MAX} ({H_MAX * f / 1e3:.2f} kHz)")


# ==================================================================== #
# Calculation
# ==================================================================== #

def split_losses(trafo):
    """Rated load loss split into P_R, P_EC, P_OSL (C57.110 Eq. (1))."""
    return CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=trafo["sigma"],
                                          eddy_share=trafo["eddy_share"])


def build_grids(I_R):
    """Orders H_MIN ... H_MAX and log-spaced currents in A."""
    h = np.arange(H_MIN, H_MAX + 1)
    I_h = np.geomspace(I_MIN_PU * I_R, I_MAX_PU * I_R, N_CURRENT)
    return h, I_h


def eddy_weighting(h, f, thickness, model, rho):
    """Winding eddy-loss weighting w(h) for one model (h^2, Annex C or Dowell)."""
    return CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=f, conductor_thickness=thickness,
                                            rho=rho, model=model)


def life_map(trafo, losses, h, I_h, T_amb_C, w):
    """Hot spot [degC] and equivalent life [years] on the grid (I_h x h), each order alone."""
    P_R, P_EC, P_OSL = losses
    return CF.calculate_harmonic_sensitivity_map(trafo_specs=trafo, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                 h_orders=h, I_h_values=I_h, I_1=I_1,
                                                 T_amb_C=T_amb_C, eddy_weights=w)


def maximum_current(I_h, Life, L_normal_years):
    """Current per order at which the life equals the normal life, I_h,max [A] (NaN if not on the map)."""
    return CF.iso_life_current(I_h_values=I_h, Life_years=Life, L_target=L_normal_years)


# ==================================================================== #
# Output
# ==================================================================== #

def save_map(tag, h, I_h, I_R, f, Theta_H, Life):
    """Save every map point of one model as CSV."""
    pd.DataFrame({
        "order": np.tile(h, I_h.size),
        "f_Hz": np.tile(h, I_h.size) * f,
        "I_h_A": np.repeat(I_h, h.size),
        "I_h_pct_IR": np.repeat(100.0 * I_h / I_R, h.size),
        "Theta_H_C": Theta_H.ravel(),
        "Life_years": Life.ravel(),
    }).to_csv(RESULTS_DIR / f"heatmap_{tag}.csv", index=False)


def plot_map(tag, h, I_h, Life, I_R, f, L_normal_years, truncation_orders):
    """Plot one life map with the normal-life contour."""
    PF.plot_harmonic_heatmap(h_orders=h, I_h_values=I_h, Life_years=Life, I_R=I_R,
                             figures_dir=FIGURES_DIR, f=f, fname=f"heatmap_{tag}",
                             life_floor=0.1, life_contours=[L_normal_years, 5, 1],
                             truncation_orders=truncation_orders, y_scale="log", h_max_plot=H_MAX)


def save_maximum_currents(h, f, I_R, iso):
    """Save I_h,max of every model in one CSV, in A and in % of I_R."""
    data = {"order": h, "f_Hz": h * f}
    for tag, I_iso in iso.items():
        data[f"I_max_{tag}_A"] = I_iso
        data[f"I_max_{tag}_pct_IR"] = 100.0 * I_iso / I_R
    pd.DataFrame(data).to_csv(RESULTS_DIR / "tolerable_current.csv", index=False)


def print_maximum_currents(h, f, I_R, iso, labels):
    """Print I_h,max at a few orders for every model."""
    print("\n Maximum current I_h,max, each order alone (life = normal life)")
    header = "  " + "order".rjust(6) + "f [kHz]".rjust(9)
    for tag in iso:
        header += labels[tag].rjust(24)
    print(header)
    for order in REPORT_ORDERS:
        if order < h[0] or order > h[-1]:
            continue
        j = int(np.where(h == order)[0][0])
        row = "  " + f"{order:6d}" + f"{order * f / 1e3:9.2f}"
        for tag, I_iso in iso.items():
            row += f"{I_iso[j]:10.1f} A ({100 * I_iso[j] / I_R:6.2f}%)".rjust(24)
        print(row)


def sweep_thickness(trafo, losses, h, I_h, T_amb_C, f, L_normal_years):
    """
    I_h,max at REPORT_ORDERS for every thickness in D_SWEEP, under Annex C and Dowell,
    against the h^2 reference. Prints the table and saves Dataframes/thickness_sweep.csv.

    Extra column:
      ratio_hmax = I_h,max(model) / I_h,max(h^2) at H_MAX, how much the model relaxes the square law
    """
    rho = trafo["conductor_resistivity"]
    delta_1 = CF.skin_depth(f, rho)
    orders = [o for o in REPORT_ORDERS if h[0] <= o <= h[-1]]
    idx = {o: int(np.where(h == o)[0][0]) for o in orders}
    j_max = int(np.where(h == H_MAX)[0][0])

    def boundary(thickness, model):
        w = eddy_weighting(h, f, thickness, model, rho)
        _, Life = life_map(trafo, losses, h, I_h, T_amb_C, w)
        return maximum_current(I_h, Life, L_normal_years)

    def row(name, d, I_max, I_ref):
        r = {"model": name,
             "d_mm": np.nan if d is None else d * 1e3,
             "h_c": np.inf if d is None else (delta_1 / d) ** 2}
        for o in orders:
            r[f"I_max_h{o}_A"] = I_max[idx[o]]
        r["ratio_hmax"] = I_max[j_max] / I_ref[j_max]
        return r

    I_ref = boundary(None, "dowell")                     # h^2
    rows = [row("C57.110 (h^2)", None, I_ref, I_ref)]
    for d in D_SWEEP:
        for model, name in (("annexC", "Annex C"), ("dowell", "Diffusion")):
            rows.append(row(name, d, boundary(d, model), I_ref))

    df = pd.DataFrame(rows)
    df.to_csv(RESULTS_DIR / "thickness_sweep.csv", index=False)

    print("\n Thickness sweep: maximum current I_h,max [A], each order alone")
    print(df.round({"d_mm": 1, "h_c": 1, "ratio_hmax": 2,
                    **{f"I_max_h{o}_A": 1 for o in orders}}).to_string(index=False))
    return df


# ==================================================================== #
# Main
# ==================================================================== #

def main():
    CF.self_test(verbose=True)
    make_output_dirs()

    params, trafo = load_inputs()
    f = params.f
    I_R = trafo["I_R"]
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    L_normal_years = trafo["L_normal"] / (365.0 * 24.0)
    truncation_orders = [o for o in params.truncation_orders if o is not None]

    print_inputs(trafo, f, T_amb_C)

    losses = split_losses(trafo)
    h, I_h = build_grids(I_R)

    iso, labels = {}, {}
    for tag, thickness, model, label in MODELS:
        print(f"\n Computing map: {label}")
        w = eddy_weighting(h, f, thickness, model, trafo["conductor_resistivity"])
        Theta_H, Life = life_map(trafo, losses, h, I_h, T_amb_C, w)
        save_map(tag, h, I_h, I_R, f, Theta_H, Life)
        #plot_map(tag, h, I_h, Life, I_R, f, L_normal_years, truncation_orders)
        iso[tag] = maximum_current(I_h, Life, L_normal_years)
        labels[tag] = label

    save_maximum_currents(h, f, I_R, iso)
    print_maximum_currents(h, f, I_R, iso, labels)
    #sweep_thickness(trafo, losses, h, I_h, T_amb_C, f, L_normal_years)
    print(f"\n Results written to {RESULTS_DIR}")

main()


# ==================================================================== #
# Plotting (reads the saved CSVs, independent of main)
# ==================================================================== #

def shifted_positions(cs, labels, dx=-50):
    """Move each contour label dx orders along its own line (y follows the line)."""
    segs = [s for level in cs.allsegs for s in level if len(s)]
    pos = []
    for t in labels:
        x, y = t.get_position()
        seg = min(segs, key=lambda s: np.min(np.hypot(s[:, 0] - x, np.log10(s[:, 1]) - np.log10(y))))
        i = np.argsort(seg[:, 0])
        x_new = x + dx
        y_new = 10 ** np.interp(x_new, seg[i, 0], np.log10(seg[i, 1]))
        pos.append((x_new, y_new))
    return pos


def load_map(tag):
    """Read one saved map and return orders, current in % of I_R, and life as a grid."""
    df = pd.read_csv(RESULTS_DIR / f"heatmap_{tag}.csv")
    grid = df.pivot(index="I_h_pct_IR", columns="order", values="Life_years")
    return grid.columns.to_numpy(), grid.index.to_numpy(), grid.to_numpy()


def plot_results(ylim_pct=YLIM_PCT, fname="life_maps", life_floor=0.1, contours=(5, 1), cmap="inferno",
                 title_pad=7.5, figsize=(6.4 * 2, 4.8 * 0.75)):
    """
    Three life maps side by side (h^2, Annex C, Dowell) on one shared colour scale.

    y-axis : current of order h in % of I_R, log scale, each order alone
    x-axis : order (bottom), frequency in kHz (top)
    colour : equivalent life [years], one colour bar for all three panels
    lines  : solid white = normal life (I_h,max), dashed white = 5 and 1 years
    title_pad : distance of the panel titles above the plot [pt], clears the kHz axis
    """
    params = Input_parameters_class()
    f = params.f
    L_normal_years = params.trafo_specs["L_normal"] / (365.0 * 24.0)

    maps = []
    for tag, *_ in MODELS:
        h, I_pct, L = load_map(tag)
        keep = h <= H_MAX
        maps.append((h[keep], I_pct, L[:, keep]))
    titles = [PLOT_TITLES[tag] for tag, *_ in MODELS]

    life_top = max(np.nanmax(L) for _, _, L in maps)
    norm = LogNorm(vmin=life_floor, vmax=life_top)
    levels = sorted(c for c in contours if life_floor < c < life_top)

    fig, axes = plt.subplots(1, 3, figsize=figsize, sharey=True, constrained_layout=True)

    def life_label(v):
        """Text written on the white contours."""
        return f"{v:.1f} yr" if abs(v - L_normal_years) < 1e-6 else f"{v:g} yr"

    for ax, (h, I_pct, L), title in zip(axes, maps, titles):
        mesh = ax.pcolormesh(h, I_pct, np.clip(L, life_floor, life_top), shading="nearest",
                             cmap=cmap, norm=norm, rasterized=True)

        # White contours: normal life (solid) and 5 / 1 years (dashed), labels moved 50 orders left
        cs = ax.contour(h, I_pct, L, levels=[L_normal_years], colors="white", linewidths=1.5)
        auto = ax.clabel(cs, fmt=life_label, inline=False)
        pos = shifted_positions(cs, auto, dx=-50)
        for t in auto:
            t.remove()
        ax.clabel(cs, fmt=life_label, inline=True, manual=pos)
        if levels:
            cs2 = ax.contour(h, I_pct, L, levels=levels, colors="white", linewidths=1.0, linestyles="--")
            auto2 = ax.clabel(cs2, fmt=life_label, inline=False)
            pos2 = shifted_positions(cs2, auto2, dx=-50)
            for t in auto2:
                t.remove()
            ax.clabel(cs2, fmt=life_label, inline=True, manual=pos2)

        ax.set_yscale("log")
        ax.set_ylim(1)
        ax.set_xlim(0, h[-1])
        ax.set_xlabel("Harmonic order $h$")

        # Frequency on the top axis, title above it
        top = ax.secondary_xaxis("top", functions=(lambda x: x * f / 1e3, lambda k: k * 1e3 / f))
        top.set_xlabel("Frequency [kHz]")
        ax.set_title(title, pad=title_pad)

    axes[0].set_ylabel("Current [% of rated current]")

    cbar = fig.colorbar(mesh, ax=axes, extend="min", pad=0.01)
    cbar.set_label("Equivalent life [years]")

    fig.savefig(FIGURES_DIR / f"{fname}.png", dpi=600)
    fig.savefig(FIGURES_DIR / f"{fname}.pdf")
    plt.close(fig)
    print(f"\n Figure written to {FIGURES_DIR / fname}.png / .pdf")

#plot_results()



def plot_results_new(ylim_pct=YLIM_PCT, fname="life_maps_new", life_floor=0.1, cmap="inferno",
                 title_pad=7.5, figsize=(6.4 * 2, 4.8 * 0.66)):
    """
    Three life maps side by side (h^2, Annex C, Dowell) on one shared colour scale.

    y-axis : current of order h in % of I_R, log scale, each order alone
    x-axis : order (bottom), frequency in kHz (top)
    colour : equivalent life [years], one colour bar for all three panels
    line   : solid white = normal life (I_h,max)
    title_pad : distance of the panel titles above the plot [pt], clears the kHz axis
    """
    params = Input_parameters_class()
    f = params.f
    L_normal_years = params.trafo_specs["L_normal"] / (365.0 * 24.0)

    maps = []
    for tag, *_ in MODELS:
        h, I_pct, L = load_map(tag)
        keep = h <= H_MAX
        maps.append((h[keep], I_pct, L[:, keep]))
    titles = [PLOT_TITLES[tag] for tag, *_ in MODELS]

    life_top = max(np.nanmax(L) for _, _, L in maps)
    norm = LogNorm(vmin=life_floor, vmax=life_top)

    fig, axes = plt.subplots(1, 3, figsize=figsize, sharey=True, constrained_layout=True)

    def life_label(v):
        """Text written on the white contour."""
        return f"{v:.1f} yr"

    for ax, (h, I_pct, L), title in zip(axes, maps, titles):
        mesh = ax.pcolormesh(h, I_pct, np.clip(L, life_floor, life_top), shading="nearest",
                             cmap=cmap, norm=norm, rasterized=True)

        # White contour: normal life, label moved 50 orders left
        cs = ax.contour(h, I_pct, L, levels=[L_normal_years], colors="white", linewidths=1.5)
        auto = ax.clabel(cs, fmt=life_label, inline=False)
        pos = shifted_positions(cs, auto, dx=-50)
        for t in auto:
            t.remove()
        ax.clabel(cs, fmt=life_label, inline=True, manual=pos)

        ax.set_yscale("log")
        ax.set_ylim(1)
        ax.set_xlim(0, h[-1])
        ax.set_xlabel("Harmonic order $h$")

        # Frequency on the top axis, title above it
        top = ax.secondary_xaxis("top", functions=(lambda x: x * f / 1e3, lambda k: k * 1e3 / f))
        top.set_xlabel("Frequency [kHz]")
        ax.set_title(title, pad=title_pad)

    axes[0].set_ylabel("Current [% of rated current]")

    cbar = fig.colorbar(mesh, ax=axes, extend="min", pad=0.01)
    cbar.set_label("Equivalent life [years]")

    fig.savefig(FIGURES_DIR / f"{fname}.png", dpi=600)
    fig.savefig(FIGURES_DIR / f"{fname}.pdf")
    plt.close(fig)
    print(f"\n Figure written to {FIGURES_DIR / fname}.png / .pdf")

plot_results_new()


# ==================================================================== #
# Parameter sweep (print only, independent of main)
# ==================================================================== #

SIGMA_SWEEP = np.array([0.03, 0.05, 0.10, 0.13])           # [-]    stray fraction of the load loss
C_SWEEP = np.array([3.0, 4.0, 5.33, 6.5, 8.0])             # [-]    hot-spot concentration of the eddy loss
T_AMB_SWEEP = np.array([15.0, 20.0, 25.0, 30.0, 35.0])     # [degC] ambient temperature
SWEEP_ORDERS = [1, 50, 167, 334]                           # [-]    orders at which I_h,max is printed


def sweep_parameters(model="dowell"):
    """
    One-at-a-time sensitivity of the maximum current I_h,max to the four assumed inputs:
    conductor thickness d, stray fraction sigma, concentration factor c and ambient temperature.
    Each parameter is swept while the other three stay at their nominal values.
    Prints I_h,max [% of I_R] at SWEEP_ORDERS, each order alone.
    """
    params, trafo = load_inputs()
    f = params.f
    rho = trafo["conductor_resistivity"]
    T_amb_nom = float(np.mean(params.T_amb)) - 273.15
    L_normal_years = trafo["L_normal"] / (365.0 * 24.0)
    h, I_h = build_grids(trafo["I_R"])

    nominal = {"d": D_CONDUCTOR, "sigma": trafo["sigma"],
               "c": trafo["eddy_hotspot_factor"], "T_amb": T_amb_nom}
    sweeps = {"d": D_SWEEP, "sigma": SIGMA_SWEEP, "c": C_SWEEP, "T_amb": T_AMB_SWEEP}
    fmt = {"d": lambda v: f"{v * 1e3:g} mm", "sigma": lambda v: f"{v * 100:g} %",
           "c": lambda v: f"{v:g}", "T_amb": lambda v: f"{v:g} degC"}

    def maximum(d, sigma, c, T_amb):
        tr = dict(trafo)
        tr["sigma"] = sigma
        tr["eddy_hotspot_factor"] = c
        w = eddy_weighting(h, f, d, model, rho)
        _, Life = life_map(tr, split_losses(tr), h, I_h, T_amb, w)
        return 100.0 * maximum_current(I_h, Life, L_normal_years) / trafo["I_R"]   # [% of I_R]

    rows = []
    for name, values in sweeps.items():
        for v in values:
            args = dict(nominal)
            args[name] = v
            I_max = maximum(**args)
            r = {"parameter": name, "value": fmt[name](v),
                 "nominal": "*" if np.isclose(v, nominal[name], rtol=1e-2) else ""}
            for o in SWEEP_ORDERS:
                r[f"h{o} [%]"] = I_max[h == o][0]
            rows.append(r)

    print(f"\n Parameter sweep ({model}), maximum current I_h,max in % of I_R, each order alone")
    print(pd.DataFrame(rows).round(2).to_string(index=False))


#sweep_parameters()