"""
Harmonic_budget.py

Two figures for the proposed transformer-side addition to IEEE C57.110.

Budget definition (paper, Eq. budget):
    B = sum_{h=1}^{h_max} (I_h / I_h,max)^2
    I_h,max = current of order h that, flowing ALONE (no fundamental, no other order),
              brings the hot spot to Theta_ref at the reference ambient.
    The fundamental is order 1 and is a term of the budget like any other order.

    Figure 1  plot_max_current
              I_h,max of every order (alone), and the current each order may still carry
              on top of a given fundamental, I_h,max * sqrt(1 - B_1), against the largest
              current IEEE 519 / IEEE 1547 allow at that order.

    Figure 2  plot_budget_vs_trd
              Hot spot of many random compliant spectra (fundamental drawn in a loading
              range, 1 to max_orders harmonics, TRD up to 5 %) through the full
              C57.110 / C57.91 chain, against the TRD (left) and against B (right).
              B = 1 is exact for a single order. The printout gives how far mixed
              spectra deviate from Theta_ref near B = 1.

The common section holds only imports and physics. Everything that sets how a
figure looks lives inside its own function.
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

B_AGE = 15000.0                       # [K] C57.91 Eq. (2)
F_FUND = Input_parameters_class().f   # [Hz] 60 Hz, from Input_parameters


def compliant_limit_pct(h, trd_pct):
    """Largest compliant current per order [% of I_R]: IEEE 519 Table 2 up to h = 50, the full TRD above."""
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], trd_pct)
    return np.where((h % 2 == 0) & (h <= 6), 0.5 * lim, lim)


def hotspot_from_sums(S, S_w, S_str, trafo, sigma, c, T_amb_C):
    """
    Hot spot [degC] of any spectrum, the fundamental included, from three sums over ALL its
    orders (currents in % of I_R):
        S     = sum I_h^2
        S_w   = sum I_h^2 w(h)          winding eddy weighting, w(1) = 1
        S_str = sum I_h^2 h^0.8         other stray weighting
    No separate fundamental: order 1 is a term of the sums. S = 0 gives the no-current hot spot.
    """
    I_R = trafo["I_R"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                      eddy_share=trafo["eddy_share"])
    S, S_w, S_str = (np.atleast_1d(np.asarray(x, float)) for x in (S, S_w, S_str))
    ok = S > 0
    F_HL = np.where(ok, S_w / np.where(ok, S, 1.0), 1.0)
    F_HL_STR = np.where(ok, S_str / np.where(ok, S, 1.0), 1.0)
    I_RMS = np.sqrt(S) * I_R / 100.0

    P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=F_HL, F_HL_STR=F_HL_STR)
    Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                     Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                        Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                        eddy_hotspot_factor=c)
    return T_amb_C + Theta_TO + Theta_g


def eddy_weighting(h, trafo, d, model):
    """w(h) of the winding eddy loss (h^2 of C57.110 replaced by the chosen model), w(1) = 1."""
    return CF.calculate_eddy_loss_weighting(harmonic_orders=np.asarray(h, float), f=F_FUND, conductor_thickness=d,
                                            rho=trafo["conductor_resistivity"], model=model)


def max_current_pct(h, trafo, d, sigma, c, T_amb_C, model, I_hi=300.0, n_iter=60):
    """
    I_h,max [% of I_R]: the current that, flowing ALONE at order h (h = 1 is the fundamental),
    brings the hot spot to Theta_ref. Bisection, one value per order.
    """
    h = np.asarray(h, float)
    w, h_str = eddy_weighting(h, trafo, d, model), h ** trafo["k_F_HL_STR"]
    TH = lambda I: hotspot_from_sums(I ** 2, I ** 2 * w, I ** 2 * h_str, trafo, sigma, c, T_amb_C)

    if np.ravel(hotspot_from_sums(0.0, 0.0, 0.0, trafo, sigma, c, T_amb_C))[0] >= trafo["Theta_ref"]:
        raise ValueError("No headroom: the hot spot without current already reaches Theta_ref.")

    lo, hi = np.zeros_like(h), np.full_like(h, I_hi)
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        over = TH(mid) > trafo["Theta_ref"]
        hi, lo = np.where(over, mid, hi), np.where(over, lo, mid)
    return 0.5 * (lo + hi)


def hotspot_to_life(T, trafo):
    """Hot spot [degC] -> equivalent life [yr], C57.91 Eq. (2)."""
    F_AA = np.exp(B_AGE / (trafo["Theta_ref"] + 273.0) - B_AGE / (np.asarray(T, dtype=float) + 273.0))
    return trafo["L_normal"] / (F_AA * 8760.0)


def life_to_hotspot(L, trafo):
    """Equivalent life [yr] -> hot spot [degC]."""
    F_AA = trafo["L_normal"] / (np.maximum(np.asarray(L, dtype=float), 1e-12) * 8760.0)
    return B_AGE / (B_AGE / (trafo["Theta_ref"] + 273.0) - np.log(F_AA)) - 273.0


#################################################################################
# Figure 1: what the transformer can carry against what the standards allow
#################################################################################

def plot_max_current(
        d_nom=2.5e-3,                         # [m]
        loading=1.0,                          # [pu]  fundamental for the "on top" line
        model="dowell",                       # "dowell" or "annexC"
        h_max=334,                            # [-]   20 kHz at 60 Hz
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD / IEEE 519 TDD
        ylim_pct=(0.1, 200.0),                # [% of I_R]
        figsize=(6.4, 4.8 * 0.75),
        color_alone="blue",                   # I_h,max, order alone
        color_ontop="green",                  # what is left on top of the fundamental
        color_limit="grey",                   # compliant limit
        color_gap="red",                      # compliant but over-aged
        dpi=600,
        fname="max_current",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """I_h,max alone, the remainder on top of the fundamental, and the compliant limit."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]

    h_all = np.arange(1, h_max + 1)
    I_max_all = max_current_pct(h_all, trafo, d_nom, sigma, c, T_amb_C, model)
    I1_max = I_max_all[0]
    B1 = (100.0 * loading / I1_max) ** 2                      # budget used by the fundamental
    h, I_max = h_all[1:], I_max_all[1:]
    I_left = I_max * np.sqrt(max(1.0 - B1, 0.0))               # one order on top of the fundamental, B = 1
    I_lim = compliant_limit_pct(h, trd_pct)

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.plot(h, I_max, color=color_alone, linewidth=2.2, zorder=3, label="$I_{h,\\mathrm{max}}$, order alone")
    ax.plot(h, I_left, color=color_ontop, linewidth=2.2, zorder=3,
            label=f"On top of $I_1$ = {loading:g} pu")
    ax.step(h, I_lim, where="mid", color=color_limit, linewidth=1.8, zorder=3, label="Compliant limit")
    ax.fill_between(h, I_left, I_lim, where=I_lim > I_left, step="mid", color=color_gap, alpha=0.3, linewidth=0,
                    zorder=1, label="Compliant but over-aged")
    ax.axvline(50, color="grey", linestyle="--", linewidth=1.25, zorder=1)

    ax.set_yscale("log")
    ax.set_ylim(*ylim_pct)
    ax.set_xlim(0, h_max)
    ax.set_xlabel("Harmonic order $h$")
    ax.set_ylabel("Current [% of $I_R$]")
    ax.grid(True, which="major", alpha=0.3)
    top = ax.secondary_xaxis("top", functions=(lambda x: x * F_FUND / 1e3, lambda k: k * 1e3 / F_FUND))
    top.set_xlabel("Frequency [kHz]")
    ax.legend(ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.25), frameon=True, fontsize=12.5,
              handlelength=1.25, handletextpad=0.5, columnspacing=0.5, borderpad=0.5, labelspacing=0.25)

    gap = h[I_lim > I_left]
    print(f"\n Figure 1 ({model}, d = {d_nom * 1e3:g} mm, f = {F_FUND:g} Hz, ambient {T_amb_C:g} degC)")
    print(f"   I_1,max (fundamental alone) {I1_max:.2f} % of I_R, budget used by I_1 = {loading:g} pu: B_1 = {B1:.3f}")
    print("   order   f [kHz]   I_h,max alone [%]   on top of I_1 [%]   limit [%]")
    for o in (5, 50, 51, 100, 167, 250, 334):
        if o <= h_max:
            j = int(np.where(h == o)[0][0])
            print(f"   {o:5d}   {o * F_FUND / 1e3:7.2f}   {I_max[j]:17.2f}   {I_left[j]:17.2f}   {I_lim[j]:9.2f}")
    print(f"   compliant limit above the remainder from h = {gap[0]} ({gap[0] * F_FUND / 1e3:g} kHz)" if gap.size
          else "   compliant limit never above the remainder")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_max_current()


#################################################################################
# Figure 2: hot spot of random compliant spectra against TRD and against B
#################################################################################

def plot_budget_vs_trd(
        n_spectra=3000,                       # [-]   random spectra
        max_orders=10,                        # [-]   harmonic orders per spectrum, 1 to max_orders
        loading_range=(0.8, 1.05),            # [pu]  fundamental drawn uniformly in this range
        d=2.5e-3,                             # [m]
        model="dowell",                       # "dowell" or "annexC"
        h_max=334,                            # [-]   20 kHz at 60 Hz
        trd_pct=5.0,                          # [%]   upper end of the random TRD
        example_loading=1.0,                  # [pu]  fundamental of the highlighted spectrum
        example={5: 3.0, 165: 2.0, 169: 2.0}, # order: current [% of I_R], ~10 kHz sidebands at 60 Hz
        seed=1,
        ylim_C=(90.0, 150.0),                 # [degC]
        life_ticks=(100, 40, 20, 10, 5, 2, 1),  # [yr] ticks of the right axis
        figsize=(6.4 * 2, 4.8 * 0.75),
        color="blue",
        color_example="red",
        dpi=600,
        fname="budget_vs_trd",
        figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"):

    """Left: hot spot against TRD. Right: hot spot against B (fundamental included)."""
    params = Input_parameters_class()
    trafo = params.trafo_specs
    T_amb_C = float(np.mean(params.T_amb)) - 273.15
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    Theta_ref = trafo["Theta_ref"]

    h_all = np.arange(1, h_max + 1)                          # index j holds order j + 1
    w_all = eddy_weighting(h_all, trafo, d, model)
    str_all = h_all ** trafo["k_F_HL_STR"]
    lim_all = compliant_limit_pct(h_all, trd_pct)
    Imax_all = max_current_pct(h_all, trafo, d, sigma, c, T_amb_C, model)

    def evaluate(I1_pct, idx, I):
        """TRD [%], B [-], hot spot [degC] of one spectrum: fundamental I1_pct plus harmonics I at indices idx."""
        idx_f = np.concatenate(([0], idx))
        I_f = np.concatenate(([I1_pct], I))
        S = np.sum(I_f ** 2)
        S_w = np.sum(I_f ** 2 * w_all[idx_f])
        S_str = np.sum(I_f ** 2 * str_all[idx_f])
        TH = float(np.ravel(hotspot_from_sums(S, S_w, S_str, trafo, sigma, c, T_amb_C))[0])
        return np.sqrt(np.sum(I ** 2)), np.sum((I_f / Imax_all[idx_f]) ** 2), TH

    # Random compliant spectra: fundamental in loading_range, random harmonic orders and shares,
    # TRD up to trd_pct, every order clipped to its own IEEE 519 limit up to h = 50
    rng = np.random.default_rng(seed)
    TRD, B, TH, LD = (np.empty(n_spectra) for _ in range(4))
    for n in range(n_spectra):
        LD[n] = rng.uniform(*loading_range)
        m = rng.integers(1, max_orders + 1)
        idx = rng.choice(np.arange(1, h_all.size), size=m, replace=False)
        share = rng.random(m)
        I = share / np.linalg.norm(share) * rng.uniform(0.0, trd_pct)
        I = np.minimum(I, lim_all[idx])
        TRD[n], B[n], TH[n] = evaluate(100.0 * LD[n], idx, I)

    ex_idx = np.array([o - 1 for o in example])
    ex_TRD, ex_B, ex_TH = evaluate(100.0 * example_loading, ex_idx, np.array(list(example.values()), float))
    TH_rated = float(np.ravel(hotspot_from_sums(1e4, 1e4, 1e4, trafo, sigma, c, T_amb_C))[0])   # 100 % fundamental
    B_rated = (100.0 / Imax_all[0]) ** 2

    fig, (ax_t, ax_b) = plt.subplots(1, 2, figsize=figsize, sharey=True, constrained_layout=True)
    for ax in (ax_t, ax_b):
        normal = ax.axhline(Theta_ref, color="purple", linestyle="--", linewidth=1.5, zorder=1)
        rated = ax.axhline(TH_rated, color="black", linestyle="--", linewidth=1.5, zorder=1)
        ax.grid(True, which="major", alpha=0.3)
        ax.set_ylim(*ylim_C)

    pts = ax_t.scatter(TRD, TH, s=6, c=color, alpha=0.35, linewidths=0, zorder=2)
    ex = ax_t.scatter(ex_TRD, ex_TH, s=180, marker="*", color=color_example, edgecolors="black",
                      linewidths=0.6, zorder=4)
    ax_t.axvline(trd_pct, color="grey", linestyle="--", linewidth=1.25, zorder=1)
    ax_t.set_xlim(0, trd_pct * 1.05)
    ax_t.set_xlabel("TRD [% of $I_R$]")
    ax_t.set_ylabel("Hot spot [°C]")

    ax_b.scatter(B, TH, s=6, c=color, alpha=0.35, linewidths=0, zorder=2)
    ax_b.scatter(ex_B, ex_TH, s=180, marker="*", color=color_example, edgecolors="black", linewidths=0.6, zorder=4)
    ax_b.axvline(1.0, color="grey", linestyle="--", linewidth=1.25, zorder=1)
    ax_b.set_xlim(0, max(3.0, np.percentile(B, 99)))
    ax_b.set_xlabel("Harmonic budget $B$")
    right = ax_b.secondary_yaxis("right", functions=(lambda T: hotspot_to_life(T, trafo),
                                                     lambda L: life_to_hotspot(L, trafo)))
    right.set_yticks([L for L in life_ticks if ylim_C[0] < life_to_hotspot(L, trafo) < ylim_C[1]])
    right.set_ylabel("Equivalent life [years]")

    fig.legend(handles=[pts, ex, rated, normal],
               labels=["Random compliant spectra", "Example spectrum", "Rated load, no harmonics",
                       "Normal insulat\u200cion life"],
               ncol=4, loc="upper center", bbox_to_anchor=(0.5, 0.0),
               frameon=True, fontsize=12.5, markerscale=2,
               handlelength=1.25, handletextpad=0.5, columnspacing=1.0, borderpad=0.5, labelspacing=0.25)

    # Numbers for the text
    near = np.abs(B - 1.0) < 0.02
    wrong_low = (B < 1.0) & (TH > Theta_ref)                   # B says fine, hot spot above Theta_ref
    wrong_high = (B > 1.0) & (TH < Theta_ref)                  # B says over, hot spot below Theta_ref
    band = TRD > 0.8 * trd_pct
    print(f"\n Figure 2 ({model}, d = {d * 1e3:g} mm, f = {F_FUND:g} Hz, ambient {T_amb_C:g} degC, "
          f"{n_spectra} spectra, I_1 = {loading_range[0]:g} to {loading_range[1]:g} pu)")
    print(f"   I_1,max {Imax_all[0]:.2f} % of I_R, rated fundamental alone: B = {B_rated:.3f}, "
          f"hot spot {TH_rated:.2f} degC, life {float(hotspot_to_life(TH_rated, trafo)):.1f} yr")
    print(f"   example I_1 = {example_loading:g} pu + {example}: TRD {ex_TRD:.2f} %, B {ex_B:.2f}, "
          f"hot spot {ex_TH:.1f} degC, life {float(hotspot_to_life(ex_TH, trafo)):.1f} yr")
    print(f"   spectra with TRD {0.8 * trd_pct:g} to {trd_pct:g} %: hot spot {TH[band].min():.1f} to {TH[band].max():.1f} degC")
    if near.any():
        print(f"   spectra with B = 0.98 to 1.02: hot spot {TH[near].min():.2f} to {TH[near].max():.2f} degC "
              f"(Theta_ref {Theta_ref:g})")
    print(f"   B < 1 but hot spot > Theta_ref: {wrong_low.sum()} spectra"
          + (f", up to {TH[wrong_low].max() - Theta_ref:.2f} K above" if wrong_low.any() else ""))
    print(f"   B > 1 but hot spot < Theta_ref: {wrong_high.sum()} spectra"
          + (f", up to {Theta_ref - TH[wrong_high].min():.2f} K below" if wrong_high.any() else ""))

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_budget_vs_trd()