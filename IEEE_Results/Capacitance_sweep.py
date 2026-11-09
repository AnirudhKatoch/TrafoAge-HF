"""
Capacitance_sweep.py

First LV resonance of the transformer as a function of the insulation gap (x) and the
facing area (y) of the winding surfaces.

    Leakage inductance from the data sheet (referred to the LV side):
        Z_base = U^2 / S
        u_x    = sqrt(u_k^2 - u_r^2),  u_r = P_k / S
        L      = u_x * Z_base / (2 pi f_rated)
    Capacitance of two facing surfaces (parallel plate):
        C = eps0 * eps_r * A / gap
    Resonance:
        f_r = 1 / (2 pi sqrt(L C))

Colour = f_r. White line = 20 kHz (upper end of the study). Dashed lines = further levels.
Markers = the two assumed cases of the paper (paper layer between LV foils, LV to HV duct).
Everything to the right of / below the 20 kHz line resonates above 20 kHz.
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

EPS0 = 8.854e-12   # [F/m]


def leakage_inductance(S=2.5e6, U=400.0, u_k=0.06, P_k=18500.0, f_rated=50.0):
    """Leakage inductance referred to the LV side [H] from the data sheet."""
    Z_base = U ** 2 / S
    u_r = P_k / S
    u_x = np.sqrt(u_k ** 2 - u_r ** 2)
    return u_x * Z_base / (2 * np.pi * f_rated)


def resonance(L, gap_m, area_m2, eps_r):
    """Resonance frequency [Hz] of L with the plate capacitance of the given gap and area."""
    C = EPS0 * eps_r * area_m2 / gap_m
    return 1.0 / (2 * np.pi * np.sqrt(L * C)), C


def plot_resonance_sweep(
        gap_range_m=(1e-6, 5e-2),             # [m]   x axis, 1 um to 50 mm
        area_range_m2=(0.05, 100.0),          # [m^2] y axis
        eps_r=3.5,                            # [-]   oil-impregnated paper; oil alone ~2.2
        f_study=20e3,                         # [Hz]  upper end of the study, white line
        f_levels=(40e3, 60e3, 150e3, 1e6),    # [Hz]  further dashed lines
        cases={"Paper layer": (0.25e-3, 0.75), "LV to HV duct": (15e-3, 0.75)},  # name: (gap [m], area [m^2])
        n=400,
        cmap="viridis",
        figsize=(6.4, 4.8),
        dpi=600,
        fname="resonance_sweep",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Map of the first LV resonance over insulation gap and facing area."""
    L = leakage_inductance()
    gap = np.geomspace(*gap_range_m, n)
    area = np.geomspace(*area_range_m2, n)
    G, A = np.meshgrid(gap, area)
    F, _ = resonance(L, G, A, eps_r)

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    mesh = ax.pcolormesh(G * 1e3, A, F, shading="auto", cmap=cmap,
                         norm=LogNorm(vmin=F.min(), vmax=F.max()), rasterized=True)
    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("First LV resonance [Hz]")

    cs = ax.contour(G * 1e3, A, F, levels=[f_study], colors="white", linewidths=2.0)
    ax.clabel(cs, fmt=lambda v: f"{v / 1e3:g} kHz", fontsize=12)
    cs2 = ax.contour(G * 1e3, A, F, levels=sorted(f_levels), colors="white", linewidths=1.0, linestyles="--")
    ax.clabel(cs2, fmt=lambda v: f"{v / 1e3:g} kHz" if v < 1e6 else f"{v / 1e6:g} MHz", fontsize=11)

    for name, (g, a) in cases.items():
        f_r, C = resonance(L, g, a, eps_r)
        ax.plot(g * 1e3, a, "o", color="red", markeredgecolor="black", markersize=8)
        ax.annotate(name, (g * 1e3, a), xytext=(6, 6), textcoords="offset points", color="white", fontsize=12)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Insulation gap [mm]")
    ax.set_ylabel("Facing area [m$^2$]")

    # Numbers for the text
    print(f"\n Leakage inductance (LV side) {L * 1e6:.2f} uH, eps_r = {eps_r:g}")
    C_needed = 1.0 / ((2 * np.pi * f_study) ** 2 * L)
    print(f"   capacitance for resonance at {f_study / 1e3:g} kHz: {C_needed * 1e6:.2f} uF")
    for name, (g, a) in cases.items():
        f_r, C = resonance(L, g, a, eps_r)
        k = C_needed / C
        print(f"   {name:14s} gap {g * 1e3:6.2f} mm, area {a:5.2f} m^2: C {C * 1e9:8.2f} nF, "
              f"f_r {f_r / 1e3:9.1f} kHz, capacitance would need to be {k:7.0f}x larger "
              f"(area {a * k:7.1f} m^2 or gap {g / k * 1e6:7.2f} um) to reach {f_study / 1e3:g} kHz")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


#plot_resonance_sweep()
