import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF


def ieee519_limit_pu(h, multiplier=1.0, odd_only=False):
    """IEEE 519-2022 Table 2, row Isc/IL < 20, in pu of the rated current. Footnote a: even h <= 6 at 50 %."""
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], 0.0) / 100.0
    lim = np.where((h % 2 == 0) & (h <= 6), 0.5 * lim, lim)
    if odd_only:
        lim = np.where(h % 2 == 0, 0.0, lim)
    lim = lim * multiplier                      # Table 5 multiplier (up to 2.2), 1.0 = Table 2 as is
    lim[h == 1] = 0.0                            # fundamental is not a harmonic
    return lim


def hotspot_rise(I_pu, h, trafo, sigma, d, loading, model="dowell"):
    """Top-oil rise + gradient [K] for a spectrum I_pu (pu of I_R per order, index 0 = fundamental)."""
    I_R = trafo["I_R"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=sigma, eddy_share=trafo["eddy_share"])
    w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=50, conductor_thickness=d,
                                         rho=trafo["conductor_resistivity"], model=model)

    I = np.array(I_pu, dtype=float)
    I[0] = loading
    I_A = I[np.newaxis, :] * I_R

    F_HL = CF.calculate_harmonic_loss_factor(I_A, h, k=2, weights=w)
    F_HL_STR = CF.calculate_harmonic_loss_factor(I_A, h, k=trafo["k_F_HL_STR"])
    I_RMS = np.sqrt(np.sum(I_A ** 2, axis=1))

    P_LL = CF.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=F_HL, F_HL_STR=F_HL_STR)
    Theta_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                     Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Theta_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=F_HL,
                                                        Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                        eddy_hotspot_factor=trafo["eddy_hotspot_factor"])
    return float(np.ravel(Theta_TO + Theta_g)[0])


def worst_case_519(sigma=None, d=2.5e-3, loading=1.0, multiplier=1.0, odd_only=False,
                   tdd=0.05, model="dowell", trafo=None):
    """
    Worst IEEE 519-compliant spectrum: every order may sit at its limit as long as the TDD holds.
    Loss is linear in I_h^2, so the worst spectrum fills the most heating orders first (greedy).

    Returns dict
        dTheta_K        hot-spot rise caused by the worst compliant spectrum [K]
        single_max_K    largest rise from one order alone at its limit [K]
        Theta_H0_C      hot spot without harmonics at 25 degC ambient [degC]
        T_amb_fail_C    ambient above which the spectrum ages the insulation faster than normal [degC]
        spectrum        DataFrame of the orders used and their current [% of I_R]
    """
    if trafo is None:
        trafo = Input_parameters_class().trafo_specs
    if sigma is None:
        sigma = trafo["sigma"]

    h = np.arange(1, 51)
    zero = np.zeros(h.size)
    rise0 = hotspot_rise(zero, h, trafo, sigma, d, loading, model)

    # Hot-spot rise per unit I_h^2 of every order
    k_test = 1e-3
    sens = np.zeros(h.size)
    for j in range(1, h.size):
        x = zero.copy()
        x[j] = k_test
        sens[j] = (hotspot_rise(x, h, trafo, sigma, d, loading, model) - rise0) / k_test ** 2

    # Greedy fill: most heating orders first, each up to its limit, until the TDD is used
    lim = ieee519_limit_pu(h, multiplier, odd_only)
    budget = tdd ** 2
    k2 = np.zeros(h.size)
    for j in np.argsort(-sens):
        if j == 0 or lim[j] == 0.0:
            continue
        k2[j] = min(lim[j] ** 2, budget)
        budget -= k2[j]
        if budget <= 0.0:
            break
    spectrum = np.sqrt(k2)

    dTheta = hotspot_rise(spectrum, h, trafo, sigma, d, loading, model) - rise0
    single = max(hotspot_rise(np.where(h == hj, lim, 0.0), h, trafo, sigma, d, loading, model) - rise0
                 for hj in h[1:] if lim[hj - 1] > 0)

    return {
        "dTheta_K": dTheta,
        "single_max_K": single,
        "Theta_H0_C": 25.0 + rise0,
        "T_amb_fail_C": trafo["Theta_ref"] - rise0 - dTheta,
        "spectrum": pd.DataFrame({"order": h[spectrum > 0], "I_pct": 100.0 * spectrum[spectrum > 0]}),
    }


def ambient_sweep(T_amb_C=(15, 20, 25, 30, 35), sigmas=(0.03, 0.05, 0.15), d=2.5e-3,
                  loading=1.0, multiplier=1.0, odd_only=False):
    """Hot spot with no harmonics and with the worst compliant IEEE 519 spectrum, per ambient and sigma."""
    trafo = Input_parameters_class().trafo_specs
    rows = []
    for s in sigmas:
        r = worst_case_519(sigma=s, d=d, loading=loading, multiplier=multiplier, odd_only=odd_only, trafo=trafo)
        rise0 = r["Theta_H0_C"] - 25.0
        for T in T_amb_C:
            rows.append({"sigma": s, "T_amb_C": T,
                         "Theta_H_no_harm_C": T + rise0,
                         "Theta_H_519_C": T + rise0 + r["dTheta_K"],
                         "exceeds_ref": T + rise0 + r["dTheta_K"] > trafo["Theta_ref"],
                         "T_amb_fail_C": r["T_amb_fail_C"]})
    df = pd.DataFrame(rows)
    print(df.round(2).to_string(index=False))
    return df


def plot_ambient(T_range=(15, 35), sigma_band=(0.03, 0.15), sigma_nom=None, d=2.5e-3, loading=1.0,
                 multipliers=(1.0, 2.2), fname="ieee519_worst_case_ambient", figures_dir="."):
    """
    Hot spot against ambient: no harmonics, and the worst IEEE 519-compliant spectrum
    (line at nominal sigma, band over sigma_band) for each Table 5 multiplier.
    Dot = ambient above which compliance no longer protects the transformer.
    """
    plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15,
                         "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 12})

    trafo = Input_parameters_class().trafo_specs
    if sigma_nom is None:
        sigma_nom = trafo["sigma"]
    T = np.linspace(*T_range, 101)

    fig, ax = plt.subplots(figsize=(6.4, 4.8), constrained_layout=True)

    r_nom = worst_case_519(sigma=sigma_nom, d=d, loading=loading, trafo=trafo)
    rise0 = r_nom["Theta_H0_C"] - 25.0
    ax.plot(T, T + rise0, color="black", linewidth=2.0, label="No harmonics")

    colors = ["tab:blue", "tab:orange", "tab:green"]
    for m, c in zip(multipliers, colors):
        lo = worst_case_519(sigma=sigma_band[0], d=d, loading=loading, multiplier=m, trafo=trafo)["dTheta_K"]
        hi = worst_case_519(sigma=sigma_band[1], d=d, loading=loading, multiplier=m, trafo=trafo)["dTheta_K"]
        r = worst_case_519(sigma=sigma_nom, d=d, loading=loading, multiplier=m, trafo=trafo)
        lab = "IEEE 519 worst case" if m == 1.0 else f"IEEE 519 worst case, x{m:g}"
        ax.fill_between(T, T + rise0 + lo, T + rise0 + hi, color=c, alpha=0.2, linewidth=0)
        ax.plot(T, T + rise0 + r["dTheta_K"], color=c, linewidth=2.0, label=lab)
        ax.plot(r["T_amb_fail_C"], trafo["Theta_ref"], "o", color=c, markeredgecolor="black", zorder=5)

    ax.axhline(trafo["Theta_ref"], color="tab:red", linestyle="--", linewidth=1.5,
               label=f"$\\Theta_{{ref}}$ = {trafo['Theta_ref']:g} $^\\circ$C")
    ax.set_xlim(*T_range)
    ax.set_xlabel("Ambient temperature [$^\\circ$C]")
    ax.set_ylabel("Hot spot [$^\\circ$C]")
    ax.set_title(f"$d$ = {d * 1e3:g} mm, {loading:g} pu, band $\\sigma$ = "
                 f"{sigma_band[0] * 100:g} to {sigma_band[1] * 100:g} %")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", frameon=False)

    out = Path(figures_dir)
    out.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(out / f"{fname}.{ext}", dpi=300)
    plt.close(fig)
    print(f" Figure written to {out / fname}.png / .pdf")


# 1. Nominal case: rise, worst single order, failing ambient, spectrum used
r = worst_case_519()
print(f"Worst compliant spectrum: +{r['dTheta_K']:.2f} K")
print(f"Worst single order:       +{r['single_max_K']:.2f} K")
print(f"Fails above ambient:       {r['T_amb_fail_C']:.1f} degC")
print(r["spectrum"].to_string(index=False))

# 2. Table: hot spot against ambient and sigma
ambient_sweep()

# 3. Figure

plot_ambient(figures_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures")


worst_case_519(sigma=0.15)                 # lossy transformer
worst_case_519(multiplier=2.2)             # IEEE 519 Table 5 relaxation
worst_case_519(odd_only=True)              # odd harmonics only
worst_case_519(loading=0.75)               # part load
worst_case_519(d=1e-3)                     # thin conductor
ambient_sweep(multiplier=2.2, odd_only=True)
#plot_ambient(d=4e-3, loading=0.75, figures_dir="Figures")