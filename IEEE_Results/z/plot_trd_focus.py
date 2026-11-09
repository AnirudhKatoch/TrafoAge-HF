from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

RESULTS_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results")
DATAFRAMES_DIR = RESULTS_DIR / "Dataframes"
FIGURES_DIR = RESULTS_DIR / "Figures"

F_HZ = 50.0
H_MAX = 400                      # 20 kHz, validity limit
TRD_PCT = 5.0                    # IEEE 1547 TRD
EXT_PCT = 0.3                    # IEEE 519 35 <= h <= 50, extended
D_LIST = [1.0, 2.5, 4.0]         # [mm] bands shown
D_NOM = 2.5                      # [mm] curve the shaded gap and the ratio refer to
SIGMA_LO, SIGMA_NOM, SIGMA_HI = 0.03, 0.05, 0.15
H_REPORT = 200                   # 10 kHz, order of the ratio annotation
YLIM_PCT = (0.1, 100.0)

plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})


def ieee519_pct(h):
    """IEEE 519-2022 Table 2 (Isc/IL < 20) up to h = 50, footnote a (even h <= 6 at 50 %), NaN above."""
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], np.nan)
    return np.where((h % 2 == 0) & (h <= 6), 0.5 * lim, lim)


def curve(df, d_mm, sigma):
    """One I_h* curve [% of I_R] of the sigma group, Dowell, rated load."""
    m = ((df.group == "sigma") & (df.model == "dowell") & np.isclose(df.d_mm, d_mm)
         & np.isclose(df.sigma, sigma) & np.isclose(df.loading_pu, 1.0))
    g = df[m].sort_values("order")
    g = g[g.order <= H_MAX]
    return g["order"].to_numpy(), g["I_star_pct"].to_numpy()


def plot_trd_focus(fname="limits_trd_focus"):
    df = pd.read_csv(DATAFRAMES_DIR / "tolerable_current_all.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8 * 1.3), constrained_layout=True)
    colors = plt.cm.viridis(np.linspace(0.0, 0.88, len(D_LIST)))
    handles = []

    # Tolerable current: band over sigma, line at nominal sigma
    for d, c in zip(D_LIST, colors):
        x, lo = curve(df, d, SIGMA_HI)
        _, hi = curve(df, d, SIGMA_LO)
        _, mid = curve(df, d, SIGMA_NOM)
        ax.fill_between(x, lo, hi, color=c, alpha=0.2, linewidth=0, zorder=2)
        ax.plot(x, mid, color=c, linewidth=2.6 if np.isclose(d, D_NOM) else 1.6, zorder=3)
        handles.append(Patch(facecolor=c, alpha=0.4, edgecolor=c, label=f"$d$ = {d:g} mm"))

    # Gap a TRD-compliant converter can use beyond the tolerable current (nominal d, h > 50)
    x, mid = curve(df, D_NOM, SIGMA_NOM)
    gap = (x > 50) & (mid < TRD_PCT)
    ax.fill_between(x, mid, TRD_PCT, where=gap, color="tab:red", alpha=0.18, linewidth=0, zorder=1)
    handles.append(Patch(facecolor="tab:red", alpha=0.3,
                         label=f"Compliant, ages faster ($d$ = {D_NOM:g} mm)"))

    # Ratio TRD / I_h* at H_REPORT
    j = int(np.where(x == H_REPORT)[0][0])
    ratio = TRD_PCT / mid[j]
    ax.annotate("", xy=(H_REPORT, mid[j]), xytext=(H_REPORT, TRD_PCT),
                arrowprops=dict(arrowstyle="<->", color="tab:red", linewidth=1.6), zorder=6)
    ax.text(H_REPORT + 6, np.sqrt(mid[j] * TRD_PCT), f"{ratio:.1f}$\\times$",
            color="tab:red", va="center", ha="left", fontsize=14, fontweight="bold")

    # IEEE 1547 TRD: the limit in focus
    ax.axhline(TRD_PCT, color="black", linestyle="-.", linewidth=2.4, zorder=5)
    handles.append(Line2D([], [], color="black", linestyle="-.", linewidth=2.4, label="IEEE 1547 TRD, 5 %"))

    # IEEE 519 and its extension: context only
    h519 = np.arange(2, 51)
    ax.stairs(ieee519_pct(h519), np.append(h519, 51) - 0.5, baseline=None,
              color="tab:red", linewidth=1.2, alpha=0.6, zorder=4)
    ax.plot([50.5, H_MAX], [EXT_PCT, EXT_PCT], color="tab:red", linestyle="--", linewidth=1.0, alpha=0.6, zorder=4)
    handles.append(Line2D([], [], color="tab:red", linewidth=1.2, alpha=0.6, label="IEEE 519, $h \\leq$ 50"))
    handles.append(Line2D([], [], color="tab:red", linestyle="--", linewidth=1.0, alpha=0.6, label="0.3 % extended"))

    # Where per-order limits end
    ax.axvline(50, color="grey", linestyle=":", linewidth=1.2, zorder=1)
    ax.text(52, 60, "per-order limits end", color="grey", fontsize=11, va="top", ha="left")

    ax.set_yscale("log")
    ax.set_ylim(*YLIM_PCT)
    ax.set_xlim(0, H_MAX)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Tolerable current $I_h^*$ [% of rated current]")
    ax.grid(True, which="major", alpha=0.3)

    top = ax.secondary_xaxis("top", functions=(lambda h: h * F_HZ / 1e3, lambda k: k * 1e3 / F_HZ))
    top.set_xlabel("Frequency [kHz]")

    handles.append(Line2D([], [], color="grey", linewidth=2.0, label=f"line: $\\sigma$ = {SIGMA_NOM * 100:g} %, band 3 to 15 %"))
    fig.legend(handles=handles, loc="outside lower center", ncol=2, frameon=False)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES_DIR / f"{fname}.{ext}", dpi=600)
    plt.close(fig)
    print(f" Figure written to {FIGURES_DIR / fname}.png / .pdf")
    print(f" TRD / I_h* at h = {H_REPORT} ({H_REPORT * F_HZ / 1e3:g} kHz), d = {D_NOM:g} mm: {ratio:.2f}")


# ==================================================================== #
# Run
# ==================================================================== #

plot_trd_focus()