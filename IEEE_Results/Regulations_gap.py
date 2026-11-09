"""
plot_compliant_life.py

Equivalent life of the transformer when a converter that complies with
IEEE 519 and IEEE 1547 places the largest current it may legally inject
at one harmonic order, scanned order by order.

    h <= 50 : the order sits at its own IEEE 519-2022 Table 2 limit (Isc/IL < 20),
              footnote a (even h <= 6 at 50 %)
    h  > 50 : the full 5 % TRD of IEEE 1547-2018 sits at that order

One order at a time on top of the fundamental, steady state, rated load,
nominal ambient. Every point is compliant with both standards. The band
comes only from the transformer, which the standards do not see.

Right axis: hot spot, exact (Arrhenius of C57.91 Eq. (2) inverted).
Shaded: hot spot above 140 C, where C57.91 warns of gassing.

The common section holds only imports and physics. Everything that sets
how a figure looks lives inside its own function.
"""

#################################################################################
# Common: imports and physics only
#################################################################################

import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CODE_DIR = Path(r"E:\IEEE_GM_2027_Transformer")
sys.path.insert(0, str(CODE_DIR))

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF

plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})



B_AGE = 15000.0      # [K] C57.91 Eq. (2)

def compliant_limit_pct(h, trd_pct):
    """Largest compliant current per order [% of I_R]: IEEE 519 Table 2 up to h = 50, the full TRD above."""
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], trd_pct)
    return np.where((h % 2 == 0) & (h <= 6), 0.5 * lim, lim)

def hotspot_and_life(h, I_pct, trafo, d, sigma, c, T_amb_C, loading, model):
    """
    Hot spot [degC] and equivalent life [yr] for ONE harmonic of order h (array) and
    current I_pct [% of I_R] (one value per order) on top of the fundamental.
    Same chain as calculate_harmonic_sensitivity_map, evaluated along a path instead of a grid.
    """
    h = np.asarray(h, dtype=float)
    I_R = trafo["I_R"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                      eddy_share=trafo["eddy_share"])
    w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=50, conductor_thickness=d,
                                         rho=trafo["conductor_resistivity"], model=model)

    I1_sq = (loading * I_R) ** 2
    Ih_sq = (np.asarray(I_pct) / 100.0 * I_R) ** 2
    F_HL = (I1_sq + Ih_sq * w) / (I1_sq + Ih_sq)
    F_HL_STR = (I1_sq + Ih_sq * h ** trafo["k_F_HL_STR"]) / (I1_sq + Ih_sq)
    I_RMS = np.sqrt(I1_sq + Ih_sq)

    P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=F_HL, F_HL_STR=F_HL_STR)
    Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                     Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                        Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                        eddy_hotspot_factor=c)
    Theta_H = T_amb_C + Theta_TO + Theta_g
    F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (Theta_H + 273.0))
    Life = trafo["L_normal"] / (F_AA * 8760.0)
    return Theta_H, Life

def life_to_hotspot(L, trafo):
    """Exact inverse of the Arrhenius law: life [yr] -> hot spot [degC]."""
    F_AA = trafo["L_normal"] / (np.asarray(L, dtype=float) * 8760.0)
    return B_AGE / (B_AGE / (trafo["Theta_ref"] + 273.0) - np.log(F_AA)) - 273.0

def hotspot_to_life(T, trafo):
    """Hot spot [degC] -> life [yr]."""
    F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (np.asarray(T, dtype=float) + 273.0))
    return trafo["L_normal"] / (F_AA * 8760.0)

#################################################################################
# Figure 1: conductor thickness d
#################################################################################

def plot_compliant_life_d(
        d_band=(1.0e-3, 4.0e-3),             # [m]   band
        d_nom=2.5e-3,                         # [m]   bold line
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=400,                            # [-]   20 kHz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD
        yscale="linear",                      # "log" or "linear"
        ylim_years=(0.0, 40),                 # [yr]
        figsize=(6.4, 4.8*0.75),
        color="blue",
        legend_kw=dict(loc="upper right", fontsize=12.5, frameon=True),
        dpi=600,
        fname="compliant_life_d",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Band over d_band, line at d_nom, sigma and c nominal."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    _, L_nom = hotspot_and_life(h, I_pct, trafo, d_nom, sigma, c, T_amb_C, loading, model)
    _, L_a = hotspot_and_life(h, I_pct, trafo, d_band[0], sigma, c, T_amb_C, loading, model)
    _, L_b = hotspot_and_life(h, I_pct, trafo, d_band[1], sigma, c, T_amb_C, loading, model)
    L0 = float(hotspot_and_life(np.array([2]), np.array([0.0]), trafo, d_nom, sigma, c, T_amb_C, loading, model)[1][0])

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.fill_between(h, np.clip(np.minimum(L_a, L_b), *ylim_years), np.clip(np.maximum(L_a, L_b), *ylim_years),
                    color=color, alpha=0.25, linewidth=0, zorder=2,
                    label=f"$d$ = {d_band[0] * 1e3:g} to {d_band[1] * 1e3:g} mm")
    ax.plot(h, np.clip(L_nom, *ylim_years), color=color, linewidth=2.2, zorder=3,
            label=f"$d$ = {d_nom * 1e3:g} mm (nominal)")
    ax.axhline(L0, color="black", linestyle="--", linewidth=1.5, zorder=1, label="No harmonics")
    ax.axhline(L_n, color="orange", linestyle="--", linewidth=1.5, zorder=1, label=f"Normal life")
    ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)
    ax.text(47.5, 0.975, "IEEE 519", transform=ax.get_xaxis_transform(), ha="right", va="top", fontsize=12.5, color="grey")
    ax.text(52.5, 0.975, "IEEE 1547 TRD", transform=ax.get_xaxis_transform(), ha="left", va="top", fontsize=12.5, color="grey")

    ax.set_yscale(yscale)
    ax.set_ylim(*ylim_years)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Equivalent life [years]")
    ax.grid(True, which="major", alpha=0.3)
    top = ax.secondary_xaxis("top", functions=(lambda x: x * 50.0 / 1e3, lambda k: k * 1e3 / 50.0))
    top.set_xlabel("Frequency [kHz]")

    handles, labels = ax.get_legend_handles_labels()
    #ax.legend(handles=handles, labels=labels, ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.15),
    #          frameon=True, fontsize=12.5,
    #          handlelength=2, borderpad=0.5, columnspacing=1, labelspacing=0.25)

    ax.legend(handles=handles, labels=labels, ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.25),
              frameon=True, fontsize=12.5,
              handlelength=1.25, handletextpad=0.5, columnspacing=0.5, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi)
    plt.close(fig)


#plot_compliant_life_d()


#################################################################################
# Figure 2: stray fraction sigma
#################################################################################

def plot_compliant_life_sigma(
        sigma_band=(0.03, 0.15),              # [-]   band
        d=2.5e-3,                             # [m]
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=400,                            # [-]   20 kHz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD
        yscale="linear",                      # "log" or "linear"
        ylim_years=(0.0, 40),                 # [yr]
        figsize=(6.4, 4.8*0.75),
        color="red",
        legend_kw=dict(loc="upper right", fontsize=12.5, frameon=True),
        dpi=600,
        fname="compliant_life_sigma",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Band over sigma_band, line at nominal sigma, d and c nominal."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma_nom, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    _, L_nom = hotspot_and_life(h, I_pct, trafo, d, sigma_nom, c, T_amb_C, loading, model)
    _, L_a = hotspot_and_life(h, I_pct, trafo, d, sigma_band[0], c, T_amb_C, loading, model)
    _, L_b = hotspot_and_life(h, I_pct, trafo, d, sigma_band[1], c, T_amb_C, loading, model)
    L0 = float(hotspot_and_life(np.array([2]), np.array([0.0]), trafo, d, sigma_nom, c, T_amb_C, loading, model)[1][0])

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.fill_between(h, np.clip(np.minimum(L_a, L_b), *ylim_years), np.clip(np.maximum(L_a, L_b), *ylim_years),
                    color=color, alpha=0.25, linewidth=0, zorder=2,
                    label=f"$\\sigma$ = {sigma_band[0] * 100:g} to {sigma_band[1] * 100:g} %")
    ax.plot(h, np.clip(L_nom, *ylim_years), color=color, linewidth=2.2, zorder=3,
            label=f"$\\sigma$ = {sigma_nom * 100:g} % (nominal)")
    ax.axhline(L0, color="black", linestyle="--", linewidth=1.5, zorder=1, label="No harmonics")
    ax.axhline(L_n, color="orange", linestyle="--", linewidth=1.5, zorder=1, label=f"Normal life")
    ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)
    ax.text(47.5, 0.975, "IEEE 519", transform=ax.get_xaxis_transform(), ha="right", va="top", fontsize=12.5, color="grey")
    ax.text(52.5, 0.975, "IEEE 1547 TRD", transform=ax.get_xaxis_transform(), ha="left", va="top", fontsize=12.5, color="grey")

    ax.set_yscale(yscale)
    ax.set_ylim(*ylim_years)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Equivalent life [years]")
    ax.grid(True, which="major", alpha=0.3)
    top = ax.secondary_xaxis("top", functions=(lambda x: x * 50.0 / 1e3, lambda k: k * 1e3 / 50.0))
    top.set_xlabel("Frequency [kHz]")

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=labels, ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.25),
              frameon=True, fontsize=12.5,
              handlelength=1.25, handletextpad=0.5, columnspacing=0.5, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi)
    plt.close(fig)


#plot_compliant_life_sigma()


#################################################################################
# Figure 3: eddy concentration c
#################################################################################

def plot_compliant_life_c(
        c_band=(3.0, 8.0),                    # [-]   band
        d=2.5e-3,                             # [m]
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=400,                            # [-]   20 kHz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD
        yscale="linear",                      # "log" or "linear"
        ylim_years=(0.0, 40),                 # [yr]
        figsize=(6.4, 4.8*0.75),
        color="green",
        legend_kw=dict(loc="upper right", fontsize=12.5, frameon=True),
        dpi=600,
        fname="compliant_life_c",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Band over c_band, line at nominal c, d and sigma nominal."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma, c_nom = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    _, L_nom = hotspot_and_life(h, I_pct, trafo, d, sigma, c_nom, T_amb_C, loading, model)
    _, L_a = hotspot_and_life(h, I_pct, trafo, d, sigma, c_band[0], T_amb_C, loading, model)
    _, L_b = hotspot_and_life(h, I_pct, trafo, d, sigma, c_band[1], T_amb_C, loading, model)
    L0 = float(hotspot_and_life(np.array([2]), np.array([0.0]), trafo, d, sigma, c_nom, T_amb_C, loading, model)[1][0])

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.fill_between(h, np.clip(np.minimum(L_a, L_b), *ylim_years), np.clip(np.maximum(L_a, L_b), *ylim_years),
                    color=color, alpha=0.25, linewidth=0, zorder=2,
                    label=f"$c$ = {c_band[0]:g} to {c_band[1]:g}")
    ax.plot(h, np.clip(L_nom, *ylim_years), color=color, linewidth=2.2, zorder=3,
            label=f"$c$ = {c_nom:.3g} (nominal)")
    ax.axhline(L0, color="black", linestyle="--", linewidth=1.5, zorder=1, label="No harmonics")
    ax.axhline(L_n, color="orange", linestyle="--", linewidth=1.5, zorder=1, label=f"Normal life")
    ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)
    ax.text(47.5, 0.975, "IEEE 519", transform=ax.get_xaxis_transform(), ha="right", va="top", fontsize=12.5, color="grey")
    ax.text(52.5, 0.975, "IEEE 1547 TRD", transform=ax.get_xaxis_transform(), ha="left", va="top", fontsize=12.5, color="grey")

    ax.set_yscale(yscale)
    ax.set_ylim(*ylim_years)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Equivalent life [years]")
    ax.grid(True, which="major", alpha=0.3)
    top = ax.secondary_xaxis("top", functions=(lambda x: x * 50.0 / 1e3, lambda k: k * 1e3 / 50.0))
    top.set_xlabel("Frequency [kHz]")

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=labels, ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.25),
              frameon=True, fontsize=12.5,
              handlelength=1.25, handletextpad=0.5, columnspacing=0.5, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi)
    plt.close(fig)


#plot_compliant_life_c()


#################################################################################
# Figure 4: d, sigma and c side by side in one row
#################################################################################

def plot_compliant_life_row(
        d_band=(1.0e-3, 4.0e-3),              # [m]   band, panel (a)
        sigma_band=(0.03, 0.15),              # [-]   band, panel (b)
        c_band=(3.0, 8.0),                    # [-]   band, panel (c)
        d_nom=2.5e-3,                         # [m]   nominal thickness
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=400,                            # [-]   20 kHz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD
        yscale="linear",                      # "log" or "linear"
        ylim_years=(0.0, 40),                 # [yr]
        hotspot_ticks=(105, 110, 120, 140),   # [degC] ticks of the right axis
        figsize=(6.4 * 2, 4.8 * 0.75),
        colors=("blue", "red", "green"),      # panels (a), (b), (c)
        region_519=dict(color="grey", alpha=0.125),  # shading h <= 50
        region_1547=dict(color="khaki", alpha=0.125*2),        # shading h > 50
        dpi=600,
        fname="compliant_life_row",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Three panels in one row: band over d, sigma and c, the other two nominal in each panel."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma_nom, c_nom = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0
    B = 15000.0

    def life_to_hotspot(L):
        F_AA = trafo["L_normal"] / (np.maximum(np.asarray(L, dtype=float), 1e-12) * 8760.0)
        return B / (B / (trafo["Theta_ref"] + 273.0) - np.log(F_AA)) - 273.0

    def hotspot_to_life(T):
        F_AA = np.exp(B / (trafo["Theta_ref"] + 273.0) - B / (np.asarray(T, dtype=float) + 273.0))
        return trafo["L_normal"] / (F_AA * 8760.0)

    def life(**change):
        p = {"d": d_nom, "sigma": sigma_nom, "c": c_nom}
        p.update(change)
        return hotspot_and_life(h, I_pct, trafo, p["d"], p["sigma"], p["c"], T_amb_C, loading, model)[1]

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    L_nom = life()
    L0 = float(hotspot_and_life(np.array([2]), np.array([0.0]), trafo, d_nom, sigma_nom, c_nom,
                                T_amb_C, loading, model)[1][0])

    # Band edges and legend text per panel
    panels = [
        (dict(d=d_band[0]), dict(d=d_band[1]),
         f"$d$ = {d_band[0] * 1e3:g} to {d_band[1] * 1e3:g} mm", f"$d$ = {d_nom * 1e3:g} mm (nominal)"),
        (dict(sigma=sigma_band[0]), dict(sigma=sigma_band[1]),
         f"$\\sigma$ = {sigma_band[0] * 100:g} to {sigma_band[1] * 100:g} %", f"$\\sigma$ = {sigma_nom * 100:g} % (nominal)"),
        (dict(c=c_band[0]), dict(c=c_band[1]),
         f"$c$ = {c_band[0]:g} to {c_band[1]:g}", f"$c$ = {c_nom:.3g} (nominal)"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=figsize, sharey=True, constrained_layout=True)

    for i, (ax, (edge_a, edge_b, band_label, line_label), color) in enumerate(zip(axes, panels, colors)):
        L_a, L_b = life(**edge_a), life(**edge_b)

        # Regions of the two standards
        span_519 = ax.axvspan(0, 50, linewidth=0, zorder=0, **region_519)
        span_1547 = ax.axvspan(50, h_max, linewidth=0, zorder=0, **region_1547)
        ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)

        # Band and nominal line of this panel
        band = ax.fill_between(h, np.clip(np.minimum(L_a, L_b), *ylim_years), np.clip(np.maximum(L_a, L_b), *ylim_years),
                               color=color, alpha=0.25, linewidth=0, zorder=2)
        line, = ax.plot(h, np.clip(L_nom, *ylim_years), color=color, linewidth=2.2, zorder=3)

        # Reference lines
        no_harm = ax.axhline(L0, color="black", linestyle="--", linewidth=1.5, zorder=1)
        normal = ax.axhline(L_n, color="purple", linestyle="--", linewidth=1.5, zorder=1)

        ax.set_yscale(yscale)
        ax.set_ylim(*ylim_years)
        ax.set_xlim(0, h_max)
        ax.set_xlabel("Harmonic order $h$")
        top = ax.secondary_xaxis("top", functions=(lambda x: x * 50.0 / 1e3, lambda k: k * 1e3 / 50.0))
        top.set_xlabel("Frequency [kHz]")

        # Legend of this panel, above it
        ax.legend(handles=[band, line], labels=[band_label, line_label], ncol=2,
                  loc="lower center", bbox_to_anchor=(0.5, 1.275),
                  frameon=True, fontsize=12.5,
                  handlelength=1.25, handletextpad=0.5, columnspacing=0.5, borderpad=0.5, labelspacing=0.25)

        if i == 0:
            ax.set_ylabel("Equivalent life [years]")
        if i == len(axes) - 1:
            right = ax.secondary_yaxis("right", functions=(life_to_hotspot, hotspot_to_life))
            right.set_yticks([t for t in hotspot_ticks
                              if ylim_years[0] < hotspot_to_life(t) < ylim_years[1]])
            #right.set_ylabel("Hot spot [$^\\circ$C]")
            right.set_ylabel("Hot spot [°C]")

    # Legend common to all panels, once, below the figure
    fig.legend(handles=[span_519, span_1547, no_harm, normal],
               labels=["Per-order limits (IEEE 519, 1547)", "TRD only (IEEE 1547)", "No harmonics",
                       "Normal insulat\u200cion life"],
               ncol=4, loc="upper center", bbox_to_anchor=(0.5,0.0),
               frameon=True, fontsize=12.5,
               handlelength=1.25, handletextpad=0.5, columnspacing=1.0, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    #fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi)
    fig.savefig(Path(figures_dir) / f"{fname}.pdf", dpi=dpi, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


#plot_compliant_life_row()


#################################################################################
# Table: numbers behind the compliant-life figures (printed, for writing the text)
#################################################################################

def table_compliant_life(
        d_values=(1.0e-3, 1.5e-3, 2.0e-3, 2.5e-3, 3.0e-3, 3.5e-3, 4.0e-3),   # [m]
        sigma_values=(0.03, 0.05, 0.075, 0.10, 0.15),                        # [-]
        c_values=(3.0, 4.0, 5.33, 6.5, 8.0),                                 # [-]
        d_nom=2.5e-3,                         # [m]
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=400,                            # [-]   20 kHz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD
        report_orders=(51, 100, 200, 400),    # [-]   orders printed as columns (2.55, 5, 10, 20 kHz)
        csv_path=None):                       # e.g. r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Dataframes\compliant_life_table.csv"
    """
    One row per parameter value, the other two parameters nominal. Columns:
      L_519_min     lowest life over h <= 50, each order at its own IEEE 519 limit   [yr]
      L_h<n>        life with the full 5 % TRD at order n                           [yr]
      TH_h<n>       hot spot at that order                                          [degC]
      L_1547_min    lowest life over h > 50 (full TRD at one order)                 [yr]
      below_Ln_kHz  first frequency above 2.5 kHz where life < normal life (NaN = never)
      x_faster      normal life / L at 20 kHz: how many times faster than normal the insulation ages
    """
    import pandas as pd

    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma_nom, c_nom = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    low, high = h <= 50, h > 50

    def run(**change):
        p = {"d": d_nom, "sigma": sigma_nom, "c": c_nom}
        p.update(change)
        return hotspot_and_life(h, I_pct, trafo, p["d"], p["sigma"], p["c"], T_amb_C, loading, model)

    rows = []
    for param, values in (("d", d_values), ("sigma", sigma_values), ("c", c_values)):
        for v in values:
            TH, L = run(**{param: v})
            nominal = np.isclose(v, {"d": d_nom, "sigma": sigma_nom, "c": c_nom}[param], rtol=1e-2)
            below = h[high & (L < L_n)]
            r = {"param": param,
                 "value": f"{v * 1e3:g} mm" if param == "d" else (f"{v * 100:g} %" if param == "sigma" else f"{v:g}"),
                 "nom": "*" if nominal else "",
                 "L_519_min": L[low].min()}
            for o in report_orders:
                j = int(np.where(h == o)[0][0])
                r[f"L_h{o}"] = L[j]
                r[f"TH_h{o}"] = TH[j]
            r["L_1547_min"] = L[high].min()
            r["below_Ln_kHz"] = below[0] * 0.05 if below.size else np.nan
            r["x_faster"] = L_n / L[h == h_max][0]
            rows.append(r)

    df = pd.DataFrame(rows)

    TH0, L0 = hotspot_and_life(np.array([2]), np.array([0.0]), trafo, d_nom, sigma_nom, c_nom, T_amb_C, loading, model)
    print(f"\n Reference: no harmonics {float(L0[0]):.1f} yr ({float(TH0[0]):.1f} degC), "
          f"normal life {L_n:.1f} yr (110 degC), loading {loading:g} pu, ambient {T_amb_C:g} degC, {model}")
    print(" Each row: one parameter varied, the other two nominal (* = nominal row)")
    print(" L in years, TH in degC, below_Ln_kHz = first frequency where a TRD-compliant converter over-ages the unit\n")
    for param in ("d", "sigma", "c"):
        print(df[df.param == param].drop(columns="param").round(2).to_string(index=False))
        print()

    #if csv_path:
    #    df.to_csv(csv_path, index=False)
    return df


#table_compliant_life()




#################################################################################
# Figure 5: single panel, nominal d, sigma and c, frequency from Input_parameters
#################################################################################

def plot_compliant_life_single(
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=334,                            # [-]   highest order on the plot
        trd_pct=5.0,                          # [%]   5 % total above the 50th order
        ylim_years=(0.0, 40),                 # [yr]
        hotspot_ticks=(105, 110, 120, 140),   # [degC] ticks of the right axis
        figsize=(6.4, 4.8*0.66 ),
        color="blue",                         # life line
        region_519=dict(color="grey", alpha=0.125*2),        # shading h <= 50
        region_1547=dict(color="khaki", alpha=0.125 * 4),  # shading h > 50
        dpi=600,
        fname="compliant_life_single",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """One panel: life with the largest compliant current at each order, d, sigma and c at their nominal values."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    f = params.f                                             # fundamental frequency, 60 Hz
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    d, sigma, c = 2.5e-3, trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    def life(h, I_pct):
        """Same chain as hotspot_and_life, with the eddy weighting evaluated at f from Input_parameters."""
        h = np.asarray(h, dtype=float)
        I_R = trafo["I_R"]
        P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                          eddy_share=trafo["eddy_share"])
        w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=f, conductor_thickness=d,
                                             rho=trafo["conductor_resistivity"], model=model)
        I1_sq = (loading * I_R) ** 2
        Ih_sq = (np.asarray(I_pct) / 100.0 * I_R) ** 2
        F_HL = (I1_sq + Ih_sq * w) / (I1_sq + Ih_sq)
        F_HL_STR = (I1_sq + Ih_sq * h ** trafo["k_F_HL_STR"]) / (I1_sq + Ih_sq)
        I_RMS = np.sqrt(I1_sq + Ih_sq)
        P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                  F_HL=F_HL, F_HL_STR=F_HL_STR)
        Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                         Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
        Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                            Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                            eddy_hotspot_factor=c)
        Theta_H = T_amb_C + Theta_TO + Theta_g
        F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (Theta_H + 273.0))
        return trafo["L_normal"] / (F_AA * 8760.0)

    def to_hotspot(L):
        F_AA = trafo["L_normal"] / (np.maximum(np.asarray(L, dtype=float), 1e-12) * 8760.0)
        return B_AGE / (B_AGE / (trafo["Theta_ref"] + 273.0) - np.log(F_AA)) - 273.0

    def to_life(T):
        F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (np.asarray(T, dtype=float) + 273.0))
        return trafo["L_normal"] / (F_AA * 8760.0)

    h = np.arange(2, h_max + 1)
    L = life(h, compliant_limit_pct(h, trd_pct))
    L0 = float(life(np.array([2]), np.array([0.0]))[0])

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)

    # Regions of the standards
    span_519 = ax.axvspan(0, 50, linewidth=0, zorder=0, **region_519)
    span_1547 = ax.axvspan(50, h_max, linewidth=0, zorder=0, **region_1547)
    ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)

    # Life line and reference lines
    ax.plot(h, np.clip(L, *ylim_years), color=color, linewidth=2.2, zorder=3)
    no_harm = ax.axhline(L0, color="green", linestyle="--", linewidth=1.5, zorder=1)
    normal = ax.axhline(L_n, color="red", linestyle="--", linewidth=1.5, zorder=1)

    ax.set_ylim(*ylim_years)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Equivalent life [years]")
    top = ax.secondary_xaxis("top", functions=(lambda x: x * f / 1e3, lambda k: k * 1e3 / f))
    top.set_xlabel("Frequency [kHz]")
    right = ax.secondary_yaxis("right", functions=(to_hotspot, to_life))
    right.set_yticks([t for t in hotspot_ticks if ylim_years[0] < to_life(t) < ylim_years[1]])
    right.set_ylabel("Hot spot [°C]")

    # Legend on top, two columns
    ax.legend(handles=[span_519, span_1547, no_harm, normal],
              labels=["Per-order limits (IEEE 519, 1547)", "TRD only (IEEE 1547)", "No harmonics",
                      "Normal insulat\u200cion life"],
              ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.3),
              frameon=True, fontsize=12.5,
              handlelength=1.25, handletextpad=0.5, columnspacing=1.0, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.pdf", dpi=dpi, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


plot_compliant_life_single()


#################################################################################
# Table 2: numbers behind the single-panel figure (printed, for writing the text)
#################################################################################

def table_compliant_life_single(
        d=2.5e-3,                             # [m]   conductor thickness (nominal)
        loading=1.0,                          # [pu]
        model="dowell",                       # "dowell" or "annexC"
        h_max=334,                            # [-]   highest order, same as the figure
        trd_pct=5.0,                          # [%]   5 % total above the 50th order
        report_orders=(51, 100, 167, 250, 334)):  # [-] orders printed (at 60 Hz: 3.06, 6, 10, 15, 20 kHz)
    """
    Same chain and inputs as plot_compliant_life_single, printed as numbers.
    Frequency from Input_parameters (params.f), d set here, sigma and c nominal.
    """
    params = Input_parameters_class()
    trafo = params.trafo_specs
    f = params.f
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    L_n = trafo["L_normal"] / 8760.0

    def hotspot_life(h, I_pct):
        """Hot spot [degC] and life [yr], eddy weighting evaluated at f from Input_parameters."""
        h = np.asarray(h, dtype=float)
        I_R = trafo["I_R"]
        P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                          eddy_share=trafo["eddy_share"])
        w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=f, conductor_thickness=d,
                                             rho=trafo["conductor_resistivity"], model=model)
        I1_sq = (loading * I_R) ** 2
        Ih_sq = (np.asarray(I_pct) / 100.0 * I_R) ** 2
        F_HL = (I1_sq + Ih_sq * w) / (I1_sq + Ih_sq)
        F_HL_STR = (I1_sq + Ih_sq * h ** trafo["k_F_HL_STR"]) / (I1_sq + Ih_sq)
        I_RMS = np.sqrt(I1_sq + Ih_sq)
        P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                  F_HL=F_HL, F_HL_STR=F_HL_STR)
        Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                         Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
        Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                            Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                            eddy_hotspot_factor=c)
        Theta_H = T_amb_C + Theta_TO + Theta_g
        F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (Theta_H + 273.0))
        return Theta_H, trafo["L_normal"] / (F_AA * 8760.0)

    h = np.arange(2, h_max + 1)
    I_pct = compliant_limit_pct(h, trd_pct)
    TH, L = hotspot_life(h, I_pct)
    TH0, L0 = (float(x[0]) for x in hotspot_life(np.array([2]), np.array([0.0])))
    low, high = h <= 50, h > 50
    below = h[high & (L < L_n)]

    print(f"\n Single-panel figure: f = {f:g} Hz, d = {d * 1e3:g} mm, sigma = {sigma * 100:g} %, c = {c:.3g}, "
          f"loading {loading:g} pu, ambient {T_amb_C:g} degC, {model}")
    print(f"  No harmonics                 {L0:6.2f} yr  ({TH0:.1f} degC)")
    print(f"  Normal life                  {L_n:6.2f} yr  ({trafo['Theta_ref']:.0f} degC)")
    print(f"  Per-order limits, h <= 50    {L[low].min():6.2f} to {L[low].max():.2f} yr "
          f"(lowest at h = {int(h[low][np.argmin(L[low])])})")
    print(f"  5 % total, h > 50            {L[high].min():6.2f} to {L[high].max():.2f} yr")
    print(f"  First order below normal     "
          + (f"h = {int(below[0])} ({below[0] * f / 1e3:.2f} kHz)" if below.size else "never"))
    print(f"  Ageing faster than normal at h = {h_max} ({h_max * f / 1e3:.1f} kHz): {L_n / L[-1]:.1f} x")
    print("\n  order   f [kHz]   I_h [% of I_R]   hot spot [degC]   life [yr]")
    for o in report_orders:
        if 2 <= o <= h_max:
            j = int(np.where(h == o)[0][0])
            print(f"  {o:5d}   {o * f / 1e3:7.2f}   {I_pct[j]:14.2f}   {TH[j]:15.1f}   {L[j]:9.2f}")

table_compliant_life_single()