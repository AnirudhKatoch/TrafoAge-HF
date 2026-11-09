"""
Equivalent_current_3d.py

Equivalent current with the ambient temperature (paper, Eq. budget):

    I_eq = I_R * ( (Th_TO + Th_g) / (Th_ref - Th_amb) )^(1/(2x))

    Th_TO, Th_g : top-oil rise and hot-spot gradient of the window, Eqs. (5), (6), from I_RMS, F_HL, F_HL-STR
    I_eq = I_R  <=>  hot spot = Th_ref, at any ambient and for any spectrum (exact by construction)
    Inverse     :  Th_H = Th_amb + (Th_ref - Th_amb) (I_eq / I_R)^(2x)

    Reference (not the paper formula): I_sin = sinusoidal current with the same hot-spot rise (bisection),
    used only to show how close I_eq is to a "true" current, e.g. I_eq = I_RMS for a sinusoid.

    check_scenarios   formula against the full C57.110 / C57.91 chain over many scenarios, and pure sinusoids
    plot_2d           hot spot vs current at one ambient, formula band over an ambient range
    plot_3d           current, ambient, hot spot in 3D
    plot_map          current vs ambient, colour = hot spot (2D version of the 3D plot)
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

F_FUND = Input_parameters_class().f   # [Hz] 60 Hz, from Input_parameters
FIG_DIR = r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"


def constants(d, model, h_max):
    """Transformer constants and the per-order weightings."""
    trafo = Input_parameters_class().trafo_specs
    sigma, c = trafo["sigma"], trafo["eddy_hotspot_factor"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma,
                                                      eddy_share=trafo["eddy_share"])
    K = dict(trafo=trafo, I_R=trafo["I_R"], P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, P_LL_R=trafo["P_LL_R"],
             P_NL=trafo["P_NL"], x=trafo["x_oil"], y=trafo["y_winding"], Th_TO_R=trafo["Theta_TO_R"],
             Th_g_R=trafo["Theta_g_R"], Theta_ref=trafo["Theta_ref"], sigma=sigma, c=c)
    h_all = np.arange(1, h_max + 1)
    K["w"] = CF.calculate_eddy_loss_weighting(harmonic_orders=h_all.astype(float), f=F_FUND, conductor_thickness=d,
                                              rho=trafo["conductor_resistivity"], model=model)
    K["str"] = h_all ** trafo["k_F_HL_STR"]
    return K


def random_spectra(n, K, rng, loading_range, harm_range_pct, max_orders):
    """I_RMS [A], F_HL, F_HL-STR of n random spectra (fundamental plus 1 to max_orders harmonics)."""
    I_R, h_max = K["I_R"], K["w"].size
    I1 = rng.uniform(*loading_range, n) * I_R
    m = rng.integers(1, max_orders + 1, n)
    idx = np.argsort(rng.random((n, h_max - 1)), axis=1)[:, :max_orders] + 1      # index j = order j + 1
    share = rng.random((n, max_orders)) * (np.arange(max_orders) < m[:, None])
    share /= np.linalg.norm(share, axis=1, keepdims=True)
    I_h = share * (rng.uniform(*harm_range_pct, n) / 100.0 * I_R)[:, None]
    S = I1 ** 2 + np.sum(I_h ** 2, axis=1)
    S_w = I1 ** 2 + np.sum(I_h ** 2 * K["w"][idx], axis=1)
    S_str = I1 ** 2 + np.sum(I_h ** 2 * K["str"][idx], axis=1)
    return np.sqrt(S), S_w / S, S_str / S


def full_chain(I_RMS, F_HL, F_HL_STR, K):
    """Hot-spot rise over ambient [K], Th_TO + Th_g, from the full C57.110 / C57.91 chain, Eqs. (2), (5), (6)."""
    P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=K["I_R"], P_R=K["P_R"], P_EC=K["P_EC"],
                                              P_OSL=K["P_OSL"], F_HL=F_HL, F_HL_STR=F_HL_STR)
    Th_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=K["P_LL_R"], P_NL=K["P_NL"],
                                                  Theta_TO_R=K["Th_TO_R"], x_oil=K["x"])
    Th_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=K["I_R"], P_R=K["P_R"], P_EC=K["P_EC"],
                                                     F_HL=F_HL, Theta_g_R=K["Th_g_R"], y_winding=K["y"],
                                                     eddy_hotspot_factor=K["c"])
    return Th_TO + Th_g


def ieq(rise, T_amb_C, K):
    """Equivalent current [A], paper Eq. budget."""
    head = K["Theta_ref"] - np.asarray(T_amb_C, float)
    return K["I_R"] * (np.asarray(rise, float) / head) ** (1.0 / (2.0 * K["x"]))


def hotspot_from_ieq(I_eq, T_amb_C, K):
    """Hot spot [degC] from I_eq, inverse of Eq. budget."""
    T_amb_C = np.asarray(T_amb_C, float)
    return T_amb_C + (K["Theta_ref"] - T_amb_C) * (np.asarray(I_eq, float) / K["I_R"]) ** (2.0 * K["x"])


def isin(rise, K, j_hi=3.0, n_iter=60):
    """Reference only: sinusoidal current [A] with the same hot-spot rise, bisection on the full chain."""
    rise = np.asarray(rise, float)
    lo, hi = np.zeros_like(rise), np.full_like(rise, j_hi)
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        over = full_chain(mid * K["I_R"], np.ones_like(mid), np.ones_like(mid), K) > rise
        hi, lo = np.where(over, mid, hi), np.where(over, lo, mid)
    return K["I_R"] * 0.5 * (lo + hi)


#################################################################################
# Check: does the formula match the physics of the methodology in every scenario
#################################################################################

def check_scenarios(
        T_amb_list=(15.0, 20.0, 25.0, 30.0, 35.0, 40.0),          # [degC]
        loading_list=((0.3, 0.7), (0.5, 1.0), (0.8, 1.2)),         # [pu] fundamental ranges
        harm_list=((0.0, 5.0), (0.0, 10.0), (0.0, 20.0)),          # [% of I_R] total harmonic current ranges
        d_list=(1.0e-3, 2.5e-3, 4.0e-3),                           # [m]
        sin_loads=(0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2),             # [pu] pure sinusoids
        model="dowell",
        h_max=334,
        max_orders=10,
        n_spectra=2000,
        seed=1):

    """Formula vs full chain over all scenario combinations, and I_eq / I_RMS for pure sinusoids."""
    rng = np.random.default_rng(seed)
    worst = dict(safe=0.0, alarm=0.0, dTH=0.0, dev=0.0, rms=0, n_safe=0, n_alarm=0)
    print(f"\n Scenario check ({model}, f = {F_FUND:g} Hz, {n_spectra} spectra per scenario)")
    print("   RMS miss    = I_RMS <= I_R but full hot spot > Theta_ref")
    print("   false safe  = I_eq  <= I_R but full hot spot > Theta_ref  (count / K above)")
    print("   false alarm = I_eq  >  I_R but full hot spot <= Theta_ref (count / K below)")
    print("   dTH         = max |hot spot from I_eq - full hot spot| [K]")
    print("   dev         = max |I_eq / I_sin - 1| [%] at 30 degC, I_sin = sinusoid with the same hot spot (reference)")
    print(f"   {'d[mm]':>5} {'amb':>4} {'I1[pu]':>9} {'Ih[%]':>7} | {'RMS miss':>8} | {'safe':>9} {'alarm':>9} "
          f"{'dTH':>8} {'dev[%]':>7}")
    for d in d_list:
        K = constants(d, model, h_max)
        for T_amb in T_amb_list:
            for ld in loading_list:
                for hr in harm_list:
                    I_RMS, F_HL, F_HL_STR = random_spectra(n_spectra, K, rng, ld, hr, max_orders)
                    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)
                    TH = T_amb + rise
                    hot = TH > K["Theta_ref"]
                    I_eq = ieq(rise, T_amb, K)
                    I_eq30, I_s = ieq(rise, 30.0, K), isin(rise, K)          # both at the rated ambient
                    fs, fa = (I_eq <= K["I_R"]) & hot, (I_eq > K["I_R"]) & ~hot
                    k_fs = (TH[fs].max() - K["Theta_ref"]) if fs.any() else 0.0
                    k_fa = (K["Theta_ref"] - TH[fa].min()) if fa.any() else 0.0
                    dTH = np.max(np.abs(hotspot_from_ieq(I_eq, T_amb, K) - TH))
                    dev = 100.0 * np.max(np.abs(I_eq30 / I_s - 1.0))
                    rms_miss = np.sum((I_RMS <= K["I_R"]) & hot)
                    print(f"   {d * 1e3:5.1f} {T_amb:4.0f} {ld[0]:4.1f}-{ld[1]:<4.1f} {hr[0]:3.0f}-{hr[1]:<3.0f} | "
                          f"{rms_miss:8d} | {fs.sum():4d}/{k_fs:4.2f} {fa.sum():4d}/{k_fa:4.2f} {dTH:8.1e} {dev:7.2f}")
                    worst["safe"], worst["alarm"] = max(worst["safe"], k_fs), max(worst["alarm"], k_fa)
                    worst["dTH"], worst["dev"] = max(worst["dTH"], dTH), max(worst["dev"], dev)
                    worst["rms"] += rms_miss
                    worst["n_safe"] += fs.sum()
                    worst["n_alarm"] += fa.sum()

    # Pure sinusoids: I_eq against I_RMS, and the hot spot at I_R
    K = constants(d_list[0], model, h_max)
    print("\n   Pure sinusoids, I_eq / I_RMS (rows: ambient [degC], columns: I_RMS [pu])")
    print("   amb   " + "".join(f"{j:8.2f}" for j in sin_loads) + "   hot spot at I_R [degC]")
    for T_amb in T_amb_list:
        j = np.asarray(sin_loads, float)
        rise = full_chain(j * K["I_R"], np.ones_like(j), np.ones_like(j), K)
        r = ieq(rise, T_amb, K) / (j * K["I_R"])
        TH_R = T_amb + float(full_chain(np.array([K["I_R"]]), np.ones(1), np.ones(1), K)[0])
        print(f"   {T_amb:4.0f}  " + "".join(f"{v:8.4f}" for v in r) + f"   {TH_R:8.2f}")

    print("\n   Worst case over all scenarios")
    print(f"     RMS check misses in total: {worst['rms']} spectra")
    print(f"     I_eq false safe: {worst['n_safe']} spectra, up to {worst['safe']:.2f} K")
    print(f"     I_eq false alarm: {worst['n_alarm']} spectra, up to {worst['alarm']:.2f} K")
    print(f"     hot spot from I_eq vs full chain: up to {worst['dTH']:.1e} K")
    print(f"     I_eq vs sinusoid-equivalent current: up to {worst['dev']:.2f} %")


#check_scenarios()


def plot_ieq_paper(
        T_amb_C=30.0,                         # [degC] ambient of the scatter
        amb_curves=(25.0, 30.0, 35.0),        # [degC] sinusoid curves and their I_max
        curve_colors=("orange", "blue", "purple"),
        n_spectra=3000,
        loading_range=(0.75, 1.25),           # [pu]
        harm_range_pct=(0.0, 10.0),           # [% of I_R]
        max_orders=10,
        d=2.5e-3,
        model="dowell",
        h_max=334,
        seed=1,
        xlim_pu=(0.75, 1.25),
        ylim_C=(70.0, 150.0),
        figsize=(6.4, 4.8 * 0.75),
        color_rms="grey",
        color_hidden="red",
        color_eq="blue",
        color_ref="green",
        dpi=600,
        fname="equivalent_current_paper",
        figures_dir=FIG_DIR):

    """Hot spot vs I_RMS and I_eq (sinusoid with the same rise) at T_amb_C, with sinusoid curves and I_max."""
    K = constants(d, model, h_max)
    I_R, Th_ref = K["I_R"], K["Theta_ref"]
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR = random_spectra(n_spectra, K, rng, loading_range, harm_range_pct, max_orders)
    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)               # measured rise, with harmonics
    TH = T_amb_C + rise
    I_eq = isin(rise, K)                                       # sinusoid with the same rise
    hidden = (I_RMS <= I_R) & (TH > Th_ref)

    I_grid = np.linspace(xlim_pu[0], xlim_pu[1], 300) * I_R
    rise_grid = full_chain(I_grid, np.ones_like(I_grid), np.ones_like(I_grid), K)    # sinusoid rise

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    p_rms = ax.scatter(I_RMS[~hidden], TH[~hidden], s=5, c=color_rms, alpha=0.45, linewidths=0, zorder=2)
    p_hid = ax.scatter(I_RMS[hidden], TH[hidden], s=5, c=color_hidden, alpha=0.9, linewidths=0, zorder=3)
    p_eq = ax.scatter(I_eq, TH, s=5, c=color_eq, alpha=0.9, linewidths=0, zorder=4)
    ref = ax.axhline(Th_ref, color=color_ref, linestyle="--", linewidth=1.5, zorder=1)

    handles, labels = [p_rms, p_hid, p_eq, ref], [f"$I_{{RMS}}$, {T_amb_C:g} °C", "Missed by $I_{RMS}$",
                                                  f"$I_{{eq}}$, {T_amb_C:g} °C", f"$\\Theta_{{ref}}$ = {Th_ref:g} °C"]
    print(f"\n Paper figure ({model}, d = {d * 1e3:g} mm, ambient {T_amb_C:g} degC, {n_spectra} spectra)")
    print(f"   RMS misses {hidden.sum()}, I_eq <= I_R but > {Th_ref:g}: {np.sum((I_eq <= I_R) & (TH > Th_ref))}, "
          f"I_eq > I_R but <= {Th_ref:g}: {np.sum((I_eq > I_R) & (TH <= Th_ref))}")
    for a, col in zip(amb_curves, curve_colors):
        I_max = float(isin(np.array([Th_ref - a]), K)[0])      # sinusoid that reaches Th_ref at ambient a
        ax.plot(I_grid, a + rise_grid, color=col, linewidth=1.6, alpha=0.8, zorder=1)
        h = ax.axvline(I_max, color=col, linestyle=":", linewidth=1.6, zorder=1)
        ax.plot(I_max, Th_ref, "o", color=col, markeredgecolor="black", markersize=6, zorder=5)
        handles.append(h)
        labels.append(f"$I_{{max}}$, {a:g} °C")
        print(f"   I_max at {a:g} degC: {I_max:.0f} A = {I_max / I_R:.4f} I_R")

    ax.set_xlim(xlim_pu[0] * I_R, xlim_pu[1] * I_R)
    ax.set_ylim(*ylim_C)
    ax.set_xlabel("Current [A]")
    ax.set_ylabel("Hot spot [°C]")
    ax.grid(True, which="major", alpha=0.3)
    ax.legend(handles=handles, labels=labels, ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0),
              frameon=True, fontsize=12.5, markerscale=3, handlelength=1.25, handletextpad=0.4,
              columnspacing=0.8, borderpad=0.5, labelspacing=0.25)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_ieq_paper()


def plot_sinusoid_map(
        amb_range=(0.0, 50.0),                # [degC] y axis
        j_max=1.25,                           # [pu]   x axis upper end; 1.0 = rated only (110 degC line then appears from 30 degC)
        n=400,                                # [-]    grid resolution
        levels_C=(80.0, 90.0, 100.0, 120.0, 130.0),  # [degC] dashed hot-spot contours
        vlim_C=(30.0, 150.0),                 # [degC] colour range
        figsize=(6.4, 4.8 * 0.75),
        cmap="viridis",
        color_ref="white",                    # hot spot = Theta_ref
        dpi=600,
        fname="sinusoid_map",
        figures_dir=FIG_DIR):

    """Sinusoidal current (x) vs ambient (y), colour = hot spot. The Theta_ref contour is the allowable current."""
    trafo = Input_parameters_class().trafo_specs
    I_R, Th_ref = trafo["I_R"], trafo["Theta_ref"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=trafo["sigma"],
                                                      eddy_share=trafo["eddy_share"])

    # Hot-spot rise of a pure sinusoid against its per-unit current (F_HL = F_HL-STR = 1)
    j = np.linspace(0.0, j_max, n)
    I, one = j * I_R, np.ones_like(j)
    P_LL = CF.calculate_transformer_load_loss(I_RMS=I, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=one, F_HL_STR=one)
    Th_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                  Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Th_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=one,
                                                     Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                     eddy_hotspot_factor=trafo["eddy_hotspot_factor"])
    rise_sin = Th_TO + Th_g

    # Grid: hot spot = ambient + rise of the sinusoid
    amb = np.linspace(*amb_range, n)
    J, A = np.meshgrid(j, amb)
    TH = A + rise_sin[np.newaxis, :]

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    mesh = ax.pcolormesh(J, A, TH, cmap=cmap, vmin=vlim_C[0], vmax=vlim_C[1], shading="auto", rasterized=True)
    cs = ax.contour(J, A, TH, levels=sorted(levels_C), colors="white", linewidths=0.8, linestyles="--")
    ax.clabel(cs, fmt="%g °C", fontsize=10)
    cs_ref = ax.contour(J, A, TH, levels=[Th_ref], colors=color_ref, linewidths=2.0)
    ax.clabel(cs_ref, fmt="%g °C", fontsize=11)
    ax.axvline(1.0, color="black", linestyle="--", linewidth=1.25)

    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("Hot spot [°C]")
    ax.set_xlim(0.0, j_max)
    ax.set_ylim(*amb_range)
    ax.set_xlabel("Sinusoidal current [pu of $I_R$]")
    ax.set_ylabel("Ambient [°C]")

    # Numbers for the text: allowable sinusoidal current per ambient (hot spot = Theta_ref)
    print("\n Allowable sinusoidal current (hot spot = Theta_ref)")
    for a in (0.0, 15.0, 25.0, 30.0, 40.0, 50.0):
        need = Th_ref - a
        txt = f"{float(np.interp(need, rise_sin, j)):.3f} pu" if need <= rise_sin[-1] else f"> {j_max:g} pu"
        print(f"   ambient {a:4.0f} degC: {txt}")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_sinusoid_map()



#################################################################################
# 2D: hot spot vs current at one ambient, formula band over an ambient range
#################################################################################

def plot_2d(
        T_amb_C=30.0,                         # [degC] ambient of the scatter
        amb_band=(15.0, 40.0),                # [degC] band of the formula curve
        n_spectra=3000,
        loading_range=(0.5, 1.0),             # [pu]
        harm_range_pct=(0.0, 10.0),           # [% of I_R]
        max_orders=10,
        d=2.5e-3,
        model="dowell",
        h_max=334,
        seed=1,
        xlim_pu=(0.0, 1.25),
        ylim_C=(50.0, 150.0),
        figsize=(6.4, 4.8 * 0.75),
        color_rms="grey",
        color_eq="blue",
        color_hidden="red",
        color_band="orange",
        dpi=600,
        fname="equivalent_current_2d",
        figures_dir=FIG_DIR):

    """Scatter of I_RMS and I_eq at T_amb_C, with the hot spot of Eq. budget over amb_band as a shaded area."""
    K = constants(d, model, h_max)
    I_R, Th_ref = K["I_R"], K["Theta_ref"]
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR = random_spectra(n_spectra, K, rng, loading_range, harm_range_pct, max_orders)
    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)
    TH = T_amb_C + rise
    I_eq = ieq(rise, T_amb_C, K)
    hidden = (I_RMS <= I_R) & (TH > Th_ref)

    I_grid = np.linspace(xlim_pu[0], xlim_pu[1], 300) * I_R
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    band = ax.fill_between(I_grid, hotspot_from_ieq(I_grid, amb_band[0], K), hotspot_from_ieq(I_grid, amb_band[1], K),
                           color=color_band, alpha=0.2, linewidth=0, zorder=0)
    line, = ax.plot(I_grid, hotspot_from_ieq(I_grid, T_amb_C, K), color=color_band, linewidth=1.8, zorder=1)
    ax.axhline(Th_ref, color="purple", linestyle="--", linewidth=1.5, zorder=1)
    ax.axvline(I_R, color="black", linestyle="--", linewidth=1.5, zorder=1)
    p_rms = ax.scatter(I_RMS[~hidden], TH[~hidden], s=6, c=color_rms, alpha=0.35, linewidths=0, zorder=2)
    p_hid = ax.scatter(I_RMS[hidden], TH[hidden], s=6, c=color_hidden, alpha=0.6, linewidths=0, zorder=3)
    p_eq = ax.scatter(I_eq, TH, s=6, c=color_eq, alpha=0.6, linewidths=0, zorder=4)

    ax.set_xlim(xlim_pu[0] * I_R, xlim_pu[1] * I_R)
    ax.set_ylim(*ylim_C)
    ax.set_xlabel("Current [A]")
    ax.set_ylabel("Hot spot [°C]")
    ax.grid(True, which="major", alpha=0.3)
    ax.legend(handles=[p_rms, p_hid, p_eq, line, band],
              labels=["$I_{RMS}$", "$I_{RMS}\\leq I_R$, $>110$ °C", "$I_{eq}$",
                      f"$I_{{eq}}$, {T_amb_C:g} °C", f"$I_{{eq}}$, {amb_band[0]:g} to {amb_band[1]:g} °C"],
              ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), frameon=True, fontsize=12.5, markerscale=3,
              handlelength=1.0, handletextpad=0.4, columnspacing=0.8, borderpad=0.5, labelspacing=0.25)

    print(f"\n 2D plot (ambient {T_amb_C:g} degC): RMS misses {hidden.sum()} of {n_spectra}, "
          f"I_eq <= I_R but > {Th_ref:g} degC: {np.sum((I_eq <= I_R) & (TH > Th_ref))}, "
          f"I_eq > I_R but <= {Th_ref:g} degC: {np.sum((I_eq > I_R) & (TH <= Th_ref))}")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_2d()


#################################################################################
# 3D: current, ambient, hot spot
#################################################################################

def plot_3d(
        amb_range=(15.0, 40.0),               # [degC] ambient drawn uniformly per spectrum
        n_spectra=2000,
        loading_range=(0.5, 1.0),
        harm_range_pct=(0.0, 10.0),
        max_orders=10,
        d=2.5e-3,
        model="dowell",
        h_max=334,
        show_rms=True,                        # also plot the spectra against I_RMS
        seed=2,
        xlim_pu=(0.0, 1.25),
        zlim_C=(30.0, 160.0),
        view=(20, -60),                       # (elevation, azimuth) [deg]
        figsize=(7.5, 6.0),
        cmap="viridis",
        color_rms="grey",
        color_eq="blue",
        color_limit="red",
        dpi=600,
        fname="equivalent_current_3d",
        figures_dir=FIG_DIR):

    """Hot-spot surface of Eq. budget over current and ambient, spectra at random ambients, and the limit line."""
    K = constants(d, model, h_max)
    I_R, Th_ref = K["I_R"], K["Theta_ref"]
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR = random_spectra(n_spectra, K, rng, loading_range, harm_range_pct, max_orders)
    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)
    T_amb = rng.uniform(*amb_range, n_spectra)
    TH = T_amb + rise
    I_eq = ieq(rise, T_amb, K)

    I_g, A_g = np.meshgrid(np.linspace(xlim_pu[0], xlim_pu[1], 60) * I_R, np.linspace(*amb_range, 40))
    TH_g = hotspot_from_ieq(I_g, A_g, K)
    amb_line = np.linspace(*amb_range, 100)

    fig = plt.figure(figsize=figsize, constrained_layout=True)
    ax = fig.add_subplot(projection="3d")
    ax.plot(np.full_like(amb_line, I_R), amb_line, np.full_like(amb_line, Th_ref), color=color_limit,
            linewidth=2.5, label="$I_{eq}=I_R$, 110 °C")
    ax.plot_surface(I_g, A_g, TH_g, cmap=cmap, alpha=0.35, linewidth=0, antialiased=True)
    if show_rms:
        ax.scatter(I_RMS, T_amb, TH, s=3, c=color_rms, alpha=0.25, depthshade=False, label="$I_{RMS}$")
    ax.scatter(I_eq, T_amb, TH, s=3, c=color_eq, alpha=0.6, depthshade=False, label="$I_{eq}$")

    ax.set_xlim(xlim_pu[0] * I_R, xlim_pu[1] * I_R)
    ax.set_zlim(*zlim_C)
    ax.set_xlabel("Current [A]", labelpad=10)
    ax.set_ylabel("Ambient [°C]", labelpad=10)
    ax.set_zlabel("Hot spot [°C]", labelpad=10)
    ax.view_init(*view)
    ax.legend(loc="upper left", fontsize=12.5, markerscale=4, frameon=True)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


plot_3d()


#################################################################################
# 2D map: current vs ambient, colour = hot spot (2D version of the 3D plot)
#################################################################################

def plot_map(
        amb_range=(15.0, 40.0),
        n_spectra=2000,
        loading_range=(0.5, 1.0),
        harm_range_pct=(0.0, 10.0),
        max_orders=10,
        d=2.5e-3,
        model="dowell",
        h_max=334,
        seed=2,
        xlim_pu=(0.5, 1.25),
        levels_C=(80.0, 90.0, 100.0, 110.0, 120.0, 130.0),
        vlim_C=(60.0, 150.0),                 # [degC] colour range
        figsize=(6.4, 4.8 * 0.75),
        cmap="viridis",
        color_limit="red",
        dpi=600,
        fname="equivalent_current_map",
        figures_dir=FIG_DIR):

    """Background = hot spot from Eq. budget, dots = full hot spot of random spectra at (I_eq, ambient)."""
    K = constants(d, model, h_max)
    I_R = K["I_R"]
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR = random_spectra(n_spectra, K, rng, loading_range, harm_range_pct, max_orders)
    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)
    T_amb = rng.uniform(*amb_range, n_spectra)
    TH = T_amb + rise
    I_eq = ieq(rise, T_amb, K)

    I_g, A_g = np.meshgrid(np.linspace(xlim_pu[0], xlim_pu[1], 300) * I_R, np.linspace(*amb_range, 200))
    TH_g = hotspot_from_ieq(I_g, A_g, K)

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    mesh = ax.pcolormesh(I_g, A_g, TH_g, cmap=cmap, vmin=vlim_C[0], vmax=vlim_C[1], shading="auto", rasterized=True)
    cs = ax.contour(I_g, A_g, TH_g, levels=list(levels_C), colors="white", linewidths=0.8, linestyles="--")
    ax.clabel(cs, fmt="%g °C", fontsize=10)
    ax.scatter(I_eq, T_amb, s=8, c=TH, cmap=cmap, vmin=vlim_C[0], vmax=vlim_C[1], edgecolors="black",
               linewidths=0.2, zorder=3)
    ax.axvline(I_R, color=color_limit, linewidth=2.0, zorder=4, label="$I_{eq}=I_R$, 110 °C")
    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("Hot spot [°C]")
    ax.set_xlim(xlim_pu[0] * I_R, xlim_pu[1] * I_R)
    ax.set_ylim(*amb_range)
    ax.set_xlabel("Equivalent current $I_{eq}$ [A]")
    ax.set_ylabel("Ambient [°C]")
    ax.legend(loc="lower left", fontsize=11, frameon=True)

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.png", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


plot_map()
