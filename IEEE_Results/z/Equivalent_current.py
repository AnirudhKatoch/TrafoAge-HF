"""
Equivalent_current.py

Hot spot of many random spectra against the RMS current and against the equivalent current.

    I_eq = I_RMS * sqrt((1 + P_EC-R * F_HL) / (1 + P_EC-R)),   P_EC-R = c * P_EC / P_R

    Grey  : hot spot vs I_RMS  -> wide cloud, the RMS current does not tell the temperature
    Blue  : hot spot vs I_eq   -> collapses onto one thin curve through (I_R, Theta_ref)
    Red   : I_RMS <= I_R but hot spot > Theta_ref, overloaded although the RMS check passes

Run at the rated ambient (30 degC), where the rated hot spot is Theta_ref = 110 degC, so the
blue curve passes through (I_R, 110 degC). The small width of the blue curve comes from the
top-oil rise, which follows the total loss and not the hot-spot loss.
"""

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

F_FUND = Input_parameters_class().f   # [Hz] 60 Hz, from Input_parameters


def plot_equivalent_current(
        n_spectra=3000,                       # [-]   random spectra
        max_orders=10,                        # [-]   harmonic orders per spectrum, 1 to max_orders
        loading_range=(0.6, 1.1),             # [pu]  fundamental drawn uniformly in this range
        harm_range_pct=(0.0, 10.0),           # [% of I_R] total harmonic current drawn uniformly in this range
        d=2.5e-3,                             # [m]
        model="dowell",                       # "dowell" or "annexC"
        h_max=334,                            # [-]   20 kHz at 60 Hz
        T_amb_C=30.0,                         # [degC] rated ambient, rated hot spot = Theta_ref
        ieq_method="linear",                  # "old" (winding only), "linear" (formula), "exact" (bisection)
        seed=1,
        ylim_C=(50.0, 150.0),                 # [degC] None = automatic
        xlim_pu=(0.0, 1.25),                  # [pu of I_R] x axis range
        figsize=(6.4, 4.8 * 0.75),
        color_rms="grey",
        color_eq="blue",
        color_hidden="red",
        dpi=600,
        fname="equivalent_current",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Hot spot of random spectra against I_RMS and against I_eq."""
    trafo = Input_parameters_class().trafo_specs
    I_R, Theta_ref = trafo["I_R"], trafo["Theta_ref"]
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                      eddy_share=trafo["eddy_share"])
    P_EC_R = c * P_EC / P_R                                    # rated hot-spot eddy loss per unit ohmic loss

    h_all = np.arange(1, h_max + 1)                            # index j holds order j + 1
    w_all = CF.calculate_eddy_loss_weighting(harmonic_orders=h_all.astype(float), f=F_FUND,
                                             conductor_thickness=d, rho=trafo["conductor_resistivity"],
                                             model=model)
    str_all = h_all ** trafo["k_F_HL_STR"]

    # Random spectra: fundamental in loading_range, 1 to max_orders random harmonic orders,
    # total harmonic current in harm_range_pct, split randomly among them
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR = (np.empty(n_spectra) for _ in range(3))
    for n in range(n_spectra):
        m = rng.integers(1, max_orders + 1)
        idx = rng.choice(np.arange(1, h_max), size=m, replace=False)
        share = rng.random(m)
        I_h = share / np.linalg.norm(share) * rng.uniform(*harm_range_pct) / 100.0 * I_R
        I = np.concatenate(([rng.uniform(*loading_range) * I_R], I_h))      # [A], order 1 first
        j = np.concatenate(([0], idx))
        S = np.sum(I ** 2)
        I_RMS[n] = np.sqrt(S)
        F_HL[n] = np.sum(I ** 2 * w_all[j]) / S
        F_HL_STR[n] = np.sum(I ** 2 * str_all[j]) / S

    # Full C57.110 / C57.91 chain
    P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=F_HL, F_HL_STR=F_HL_STR)
    Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                     Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                        Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                        eddy_hotspot_factor=c)
    TH = T_amb_C + Theta_TO + Theta_g

    # Equivalent current
    #   old    : winding part only
    #   linear : top-oil part (total load loss) and winding part, weighted by their share of the
    #            hot-spot rise at rated load, exact for sinusoids, linear in I_h^2
    #   exact  : sinusoidal current with the same hot spot, solved by bisection
    x, y = trafo["x_oil"], trafo["y_winding"]
    Th_TO_R, Th_g_R, P_LL_R, P_NL = trafo["Theta_TO_R"], trafo["Theta_g_R"], trafo["P_LL_R"], trafo["P_NL"]
    a_TO = x * Th_TO_R * P_LL_R / (P_LL_R + P_NL)
    a_g = y * Th_g_R
    alpha = a_TO / (a_TO + a_g)

    L_TO = P_LL / P_LL_R                                                   # total load loss per unit
    L_g = (I_RMS / I_R) ** 2 * (1.0 + P_EC_R * F_HL) / (1.0 + P_EC_R)      # hot-spot winding loss per unit
    I_eq_old = I_R * np.sqrt(L_g)
    I_eq_lin = I_R * np.sqrt(alpha * L_TO + (1.0 - alpha) * L_g)

    rise = Theta_TO + Theta_g
    rise_sin = lambda j: (Th_TO_R * ((j ** 2 * P_LL_R + P_NL) / (P_LL_R + P_NL)) ** x
                          + Th_g_R * (j ** 2) ** y)
    lo, hi = np.zeros_like(rise), np.full_like(rise, 3.0)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        over = rise_sin(mid) > rise
        hi, lo = np.where(over, mid, hi), np.where(over, lo, mid)
    I_eq_exact = I_R * 0.5 * (lo + hi)

    I_eq = {"old": I_eq_old, "linear": I_eq_lin, "exact": I_eq_exact}[ieq_method]

    hidden = (I_RMS <= I_R) & (TH > Theta_ref)                 # RMS check passes, hot spot too high
    eq_low = (I_eq <= I_R) & (TH > Theta_ref)                  # I_eq check passes, hot spot too high
    eq_high = (I_eq > I_R) & (TH <= Theta_ref)                 # I_eq check fails, hot spot fine

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.axhline(Theta_ref, color="purple", linestyle="--", linewidth=1.5, zorder=1)
    ax.axvline(I_R, color="black", linestyle="--", linewidth=1.5, zorder=1)
    p_rms = ax.scatter(I_RMS[~hidden], TH[~hidden], s=6, c=color_rms, alpha=0.35, linewidths=0, zorder=2)
    p_hid = ax.scatter(I_RMS[hidden], TH[hidden], s=6, c=color_hidden, alpha=0.6, linewidths=0, zorder=3)
    p_eq = ax.scatter(I_eq, TH, s=6, c=color_eq, alpha=0.6, linewidths=0, zorder=4)

    ax.set_xlabel("Current [A]")
    ax.set_ylabel("Hot spot [°C]")
    if ylim_C is not None:
        ax.set_ylim(*ylim_C)
    ax.set_xlim(xlim_pu[0] * I_R, xlim_pu[1] * I_R)
    ax.grid(True, which="major", alpha=0.3)
    ax.legend(handles=[p_rms, p_hid, p_eq],
              labels=["$I_{RMS}$", "$I_{RMS}\\leq I_R$, hot spot $>110$ °C", "$I_{eq}$"],
              ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), frameon=True, fontsize=12.5, markerscale=3,
              handlelength=1.0, handletextpad=0.4, columnspacing=0.8, borderpad=0.5, labelspacing=0.25)

    # Numbers for the text
    near_rms = np.abs(I_RMS / I_R - 1.0) < 0.01
    near_eq = np.abs(I_eq / I_R - 1.0) < 0.01
    print(f"\n Equivalent current ({model}, d = {d * 1e3:g} mm, f = {F_FUND:g} Hz, ambient {T_amb_C:g} degC, "
          f"{n_spectra} spectra)")
    print(f"   P_EC-R = c P_EC / P_R = {P_EC_R:.4f}, alpha = {alpha:.4f}, I_R = {I_R:.1f} A, plotted: {ieq_method}")
    print(f"   per-unit losses: p_R = {P_R / P_LL_R:.4f}, p_EC = {P_EC / P_LL_R:.4f}, p_OSL = {P_OSL / P_LL_R:.4f}")
    if near_rms.any():
        print(f"   I_RMS within 1 % of I_R: hot spot {TH[near_rms].min():.2f} to {TH[near_rms].max():.2f} degC")
    print(f"   I_RMS <= I_R but hot spot > {Theta_ref:g} degC: {hidden.sum()} of {n_spectra} spectra"
          + (f", up to {TH[hidden].max() - Theta_ref:.2f} K above" if hidden.any() else ""))
    for name, Ie in (("old", I_eq_old), ("linear", I_eq_lin), ("exact", I_eq_exact)):
        nr = np.abs(Ie / I_R - 1.0) < 0.01
        lo_ = (Ie <= I_R) & (TH > Theta_ref)
        hi_ = (Ie > I_R) & (TH <= Theta_ref)
        print(f"   I_eq {name:6s}: within 1 % of I_R hot spot "
              + (f"{TH[nr].min():.2f} to {TH[nr].max():.2f} degC" if nr.any() else "n/a")
              + f" | <= I_R but > {Theta_ref:g}: {lo_.sum()}"
              + (f" (up to {TH[lo_].max() - Theta_ref:.2f} K)" if lo_.any() else "")
              + f" | > I_R but <= {Theta_ref:g}: {hi_.sum()}"
              + (f" (up to {Theta_ref - TH[hi_].min():.2f} K)" if hi_.any() else ""))

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_equivalent_current()
