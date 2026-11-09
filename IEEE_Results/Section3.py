import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import RegularGridInterpolator
from matplotlib.colors import TwoSlopeNorm
from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF
import pandas as pd

CODE_DIR = Path(r"E:\IEEE_GM_2027_Transformer")
sys.path.insert(0, str(CODE_DIR))

F_FUND = Input_parameters_class().f   # [Hz] 60 Hz, from Input_parameters
FIG_DIR = r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Figures"

plt.rcParams.update({"font.size": 15, "font.family": ["Calibri"], "axes.labelsize": 15,"xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

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



def plot_ieq_map(
        amb_range=(0.0, 50.0),                # [degC] x axis
        rise_range=(80-50, 80+50),              # [K]    y axis, Theta_TO + Theta_g of the measured spectrum
        j_max=2.0,                            # [pu]   sinusoid curve computed up to this current
        n=500,                                # [-]    grid resolution of the map
        levels_pu=(0.8, 0.9, 1.1, 1.2),  # [pu]   dashed I_eq / I_R contours (1.0 drawn separately)
        vlim_pu=(0.4, 1.6),                   # [pu]   colour range, centred at 1
        mark_rated=False,                      # mark the rated point (30 degC, rated rise)
        table_amb_step=5.0,                   # [degC] column step of the lookup table (CSV)
        table_rise_step=5.0,                  # [K]    row step of the lookup table (CSV)
        save_full_grid=False,                 # also save every map point in long format (n x n rows)
        figsize=(6.4, 4.8 * 0.5),
        cmap="RdYlBu_r",
        color_limit="black",                  # I_eq = I_R contour
        dpi=600,
        fname="ieq_map",
        label_amb=35.0,  # [degC] ambient at which the dashed contour labels sit (larger = further right)
        label_amb_limit=20.0,
        figures_dir=FIG_DIR,
        csv_dir=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Dataframes"):

    """
    Lookup map: ambient (x) and hot-spot rise of the measured spectrum (y) -> I_eq / I_R (colour).
        I_eq = I_R * I_sin(rise) / I_allow(T_amb)
        I_sin   : sinusoidal current with the same rise as the spectrum
        I_allow : sinusoidal current that brings the hot spot to Theta_ref at this ambient
    I_eq = I_R exactly where T_amb + rise = Theta_ref.

    CSV outputs (csv_dir):
        ieq_lookup_table.csv        rows dTheta_H [K], columns ambient [degC], values I_eq / I_R
        ieq_sinusoid_curve.csv      I / I_R against Theta_TO, Theta_g and dTheta_H of a pure sinusoid
        ieq_allowable_current.csv   I_allow / I_R and the allowed rise per ambient
        ieq_map_full_grid.csv       every map point (only if save_full_grid)
    """


    trafo = Input_parameters_class().trafo_specs
    I_R, Th_ref = trafo["I_R"], trafo["Theta_ref"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=trafo["sigma"],
                                                      eddy_share=trafo["eddy_share"])

    # Sinusoid curve: rise against per-unit current (F_HL = F_HL-STR = 1), monotonic
    j = np.linspace(0.0, j_max, 8001)
    I, one = j * I_R, np.ones_like(j)
    P_LL = CF.calculate_transformer_load_loss(I_RMS=I, I_R=I_R, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                              F_HL=one, F_HL_STR=one)
    Th_TO = CF.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo["P_LL_R"], P_NL=trafo["P_NL"],
                                                  Theta_TO_R=trafo["Theta_TO_R"], x_oil=trafo["x_oil"])
    Th_g = CF.calculate_transformer_hotspot_gradient(I_RMS=I, I_R=I_R, P_R=P_R, P_EC=P_EC, F_HL=one,
                                                     Theta_g_R=trafo["Theta_g_R"], y_winding=trafo["y_winding"],
                                                     eddy_hotspot_factor=trafo["eddy_hotspot_factor"])
    rise_sin = Th_TO + Th_g
    rise_0 = float(rise_sin[0])                               # no-load rise, no spectrum can be below it
    rise_R = float(np.interp(1.0, j, rise_sin))               # rated rise

    def I_sin_pu(rise):                                       # rise -> sinusoidal current [pu]
        return np.interp(rise, rise_sin, j, left=np.nan, right=np.nan)

    def I_eq_pu(amb, rise):                                   # (ambient, rise) -> I_eq / I_R
        return I_sin_pu(rise) / I_sin_pu(Th_ref - amb)

    # Grid and lookup
    A, R = np.meshgrid(np.linspace(*amb_range, n), np.linspace(*rise_range, n))
    I_eq = np.ma.masked_invalid(I_eq_pu(A, R))                # [pu of I_R]

    # ------------------------------------------------------------------ #
    # CSV output
    # ------------------------------------------------------------------ #
    csv_dir = Path(csv_dir)
    csv_dir.mkdir(parents=True, exist_ok=True)

    # 1. Datasheet lookup table: rows rise, columns ambient
    amb_tab = np.arange(amb_range[0], amb_range[1] + 1e-9, table_amb_step)
    rise_tab = np.arange(rise_range[0], rise_range[1] + 1e-9, table_rise_step)
    At, Rt = np.meshgrid(amb_tab, rise_tab)
    table = pd.DataFrame(np.round(I_eq_pu(At, Rt), 3),
                         index=pd.Index(rise_tab, name="dTheta_H [K] / Theta_amb [degC]"),
                         columns=[f"{a:g}" for a in amb_tab])
    table.to_csv(csv_dir / "ieq_lookup_table.csv")

    # 2. Sinusoid curve behind the table (every 0.01 pu)
    j_out = np.round(np.arange(0.0, j_max + 1e-9, 0.01), 2)
    pd.DataFrame({
        "I_over_I_R": j_out,
        "I_A": np.round(j_out * I_R, 1),
        "Theta_TO_K": np.round(np.interp(j_out, j, Th_TO), 3),
        "Theta_g_K": np.round(np.interp(j_out, j, Th_g), 3),
        "dTheta_H_K": np.round(np.interp(j_out, j, rise_sin), 3),
    }).to_csv(csv_dir / "ieq_sinusoid_curve.csv", index=False)

    # 3. Allowable sinusoidal current per ambient (every 1 degC)
    amb_out = np.arange(amb_range[0], amb_range[1] + 1e-9, 1.0)
    pd.DataFrame({
        "Theta_amb_degC": amb_out,
        "allowed_rise_K": Th_ref - amb_out,
        "I_allow_over_I_R": np.round(I_sin_pu(Th_ref - amb_out), 4),
        "I_allow_A": np.round(I_sin_pu(Th_ref - amb_out) * I_R, 1),
    }).to_csv(csv_dir / "ieq_allowable_current.csv", index=False)

    # 4. Optional: every map point
    if save_full_grid:
        pd.DataFrame({
            "Theta_amb_degC": A.ravel(),
            "dTheta_H_K": R.ravel(),
            "Theta_H_degC": (A + R).ravel(),
            "I_eq_over_I_R": I_eq.filled(np.nan).ravel(),
        }).to_csv(csv_dir / "ieq_map_full_grid.csv", index=False)

    # ------------------------------------------------------------------ #
    # Figure
    # ------------------------------------------------------------------ #
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    norm = TwoSlopeNorm(vmin=vlim_pu[0], vcenter=1.0, vmax=vlim_pu[1])
    mesh = ax.pcolormesh(A, R, I_eq, cmap=cmap, norm=norm, shading="auto", rasterized=True)


    cs = ax.contour(A, R, I_eq, levels=sorted(levels_pu), colors="black",alpha=0.75, linewidths=0.75, linestyles="--")

    # Labels of the dashed contours placed at label_amb: rise where I_eq / I_R = v at that ambient
    pos = []
    for v in sorted(levels_pu):
        r = float(np.interp(v * I_sin_pu(Th_ref - label_amb), j, rise_sin))  # rise of the sinusoid v * I_allow
        if rise_range[0] < r < rise_range[1]:
            pos.append((label_amb, r))
    ax.clabel(cs, fmt=lambda v: f"{v:g}", fontsize=12.5, manual=pos)



    cs1 = ax.contour(A, R, I_eq, levels=[1.0], colors=color_limit, linewidths=2.0)




    ax.clabel(cs1, fmt=lambda v: f"$I_{{eq}}=I_R$ ({Th_ref:g} °C)", fontsize=12.5,
              manual=[(label_amb_limit, Th_ref - label_amb_limit)], inline_spacing=12)



    if mark_rated:
        ax.plot(Th_ref - rise_R, rise_R, "o", color="white", markeredgecolor="black", markersize=7, zorder=4)

    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("$I_{eq}/I_R$ [-]")
    ax.set_xlim(*amb_range)
    ax.set_ylim(*rise_range)
    ax.set_xlabel("Ambient [°C]")
    #ax.set_ylabel("Hot-spot rise $\\Delta\\Theta_H=\\Theta_{TO}+\\Theta_g$ [K]")
    ax.set_ylabel("Hot-spot rise [K]")

    # Numbers for the text
    print(f"\n I_eq map: no-load rise {rise_0:.2f} K, rated rise {rise_R:.2f} K, "
          f"rated point at {Th_ref - rise_R:.2f} degC")
    print("   I_allow [pu] per ambient:", ", ".join(
        f"{a:g} degC {float(I_sin_pu(Th_ref - a)):.3f}" for a in (0, 15, 25, 30, 40, 50)))
    print("   I_eq / I_R for (ambient, rise):")
    for a, r in ((40, 75), (30, 80), (15, 90), (25, 100), (25, 60)):
        print(f"     {a:3g} degC, {r:3g} K -> hot spot {a + r:5.1f} degC, "
              f"I_eq = {float(I_eq_pu(a, r)):.3f} I_R")
    print(f"   CSV files written to {csv_dir}")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.pdf", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

plot_ieq_map()





def load_ieq_table(path):
    """Datasheet table -> interpolator f(rise [K], ambient [degC]) = I_eq / I_R, plus its rise and ambient axes."""
    df = pd.read_csv(path, index_col=0)
    rise = df.index.to_numpy(dtype=float)
    amb = df.columns.to_numpy(dtype=float)
    f = RegularGridInterpolator((rise, amb), df.to_numpy(dtype=float), bounds_error=False, fill_value=np.nan)
    return f, rise, amb


def ieee_limit_pct(h, trd_pct=5.0):
    """
    Largest compliant current per order [% of I_R], stricter of IEEE 519-2022 Table 2 (Isc/IL < 20)
    and IEEE 1547-2018 Tables 26/27. Above h = 50 no individual limit: the full TRD.
        odd and even h >= 8 : 4.0 (h < 11), 2.0 (< 17), 1.5 (< 23), 0.6 (< 35), 0.3 (<= 50)
        even h = 2, 4, 6    : 1.0, 2.0, 2.0   (1547 Table 27: 1, 2, 3; 519 footnote a: 50 % of 4.0 = 2)
    """
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], trd_pct)
    lim = np.where(h == 2, 1.0, lim)
    lim = np.where((h == 4) | (h == 6), 2.0, lim)
    return lim


def compliant_spectra(n, K, rng, loading_range, trd_pct, max_orders):
    """
    n random spectra that comply with IEEE 519 and IEEE 1547:
        fundamental in loading_range (<= 1 pu), 1 to max_orders harmonics at random orders 2 ... h_max,
        random shares scaled to a random total up to trd_pct, every order clipped to its own limit.
    Returns I_RMS [A], F_HL, F_HL-STR, TRD [% of I_R], largest order with current [-].
    """
    I_R, h_max = K["I_R"], K["w"].size
    #if loading_range[1] > 1.0:
    #    raise ValueError("A converter rated at the transformer rating cannot exceed 1 pu fundamental.")

    I1_pct = rng.uniform(*loading_range, n) * 100.0
    m = rng.integers(1, max_orders + 1, n)
    idx = np.argsort(rng.random((n, h_max - 1)), axis=1)[:, :max_orders] + 1   # index j = order j + 1
    share = rng.random((n, max_orders)) * (np.arange(max_orders) < m[:, None])
    share /= np.linalg.norm(share, axis=1, keepdims=True)
    I_h_pct = share * rng.uniform(0.0, trd_pct, n)[:, None]
    I_h_pct = np.minimum(I_h_pct, ieee_limit_pct(idx + 1, trd_pct))           # per-order limits up to h = 50

    TRD = np.sqrt(np.sum(I_h_pct ** 2, axis=1))
    assert np.all(TRD <= trd_pct + 1e-9)

    S = I1_pct ** 2 + np.sum(I_h_pct ** 2, axis=1)
    S_w = I1_pct ** 2 + np.sum(I_h_pct ** 2 * K["w"][idx], axis=1)
    S_str = I1_pct ** 2 + np.sum(I_h_pct ** 2 * K["str"][idx], axis=1)
    h_top = np.max(np.where(I_h_pct > 0, idx + 1, 0), axis=1)
    return np.sqrt(S) / 100.0 * I_R, S_w / S, S_str / S, TRD, h_top


def plot_ieq_datasheet_test(
        table_path=r"E:\IEEE_GM_2027_Transformer\IEEE_Results\Dataframes\ieq_lookup_table.csv",
        amb_range=(10.0, 40.0),               # [degC] ambient drawn uniformly per spectrum
        n_spectra=5000,
        loading_range=(0.75, 1.25),             # [pu]  fundamental, at most rated
        trd_pct=5.0,                          # [%]   IEEE 1547 TRD / IEEE 519 TDD
        max_orders=10,
        d=2.5e-3,
        model="dowell",
        h_max=334,
        seed=1,
        xlim_pu=(0.75, 1.25),                   # I_eq beyond the right edge is drawn at the edge
        ylim_C=(110-50, 110+50),
        figsize=(6.4, 4.8 * 0.66),
        color_rms="grey",                     # I_RMS, judged correctly
        color_miss="red",                     # I_RMS <= I_R but hot spot > Theta_ref
        color_alarm="orange",                 # I_RMS >  I_R but hot spot <= Theta_ref
        color_eq="blue",                      # I_eq from the datasheet table
        color_lines="black",
        dpi=600,
        fname="ieq_datasheet_test",
        figures_dir=FIG_DIR):

    """
    Operator test of the datasheet table with spectra that comply with IEEE 519 and IEEE 1547:
        spectrum -> Delta Theta_H (methodology) -> table at (ambient, Delta Theta_H) -> I_eq / I_R
    I_RMS and I_eq are both judged against the true hot spot of the full chain.
    """
    K = constants(d, model, h_max)
    I_R, Th_ref = K["I_R"], K["Theta_ref"]

    # 1. Datasheet
    table, rise_tab, amb_tab = load_ieq_table(table_path)
    if amb_range[0] < amb_tab.min() or amb_range[1] > amb_tab.max():
        raise ValueError(f"Ambient range {amb_range} lies outside the table ({amb_tab.min():g} to {amb_tab.max():g} degC).")
    if rise_tab.max() + amb_range[0] < Th_ref:
        raise ValueError("Table rise range too small: a rise above the table would not certainly exceed Theta_ref.")

    # 2. Measured: compliant spectra and random ambients
    rng = np.random.default_rng(seed)
    I_RMS, F_HL, F_HL_STR, TRD, h_top = compliant_spectra(n_spectra, K, rng, loading_range, trd_pct, max_orders)
    T_amb = rng.uniform(*amb_range, n_spectra)

    # 3. Operator: rise from the methodology; truth: hot spot
    rise = full_chain(I_RMS, F_HL, F_HL_STR, K)
    TH = T_amb + rise
    hot = TH > Th_ref

    # 4. Lookup. Rise above the table top: beyond the datasheet, hence over the limit (I_eq = inf)
    I_eq = table(np.column_stack([rise, T_amb]))
    above = rise > rise_tab.max()
    I_eq[above] = np.inf
    if np.any(np.isnan(I_eq)):
        raise ValueError(f"{np.isnan(I_eq).sum()} spectra fall in empty table cells (below the no-load rise).")

    # Exact I_eq (no table) to quantify the interpolation error of the datasheet resolution
    I_eq_exact = isin(rise, K) / isin(Th_ref - T_amb, K)
    inside = ~above
    tab_err = np.max(np.abs(I_eq[inside] - I_eq_exact[inside]))

    # 5. Judge both against the true hot spot
    j_rms = I_RMS / I_R
    def judge(x):
        miss, alarm = (x <= 1.0) & hot, (x > 1.0) & ~hot
        k_miss = TH[miss].max() - Th_ref if miss.any() else 0.0
        k_alarm = Th_ref - TH[alarm].min() if alarm.any() else 0.0
        return miss, alarm, k_miss, k_alarm
    rms_miss, rms_alarm, rms_kmiss, rms_kalarm = judge(j_rms)
    eq_miss, eq_alarm, eq_kmiss, eq_kalarm = judge(I_eq)

    # Figure
    ok = ~rms_miss & ~rms_alarm
    I_eq_plot = np.where(np.isfinite(I_eq), I_eq, np.nan)   # points beyond the axis are simply not drawn

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    p_rms = ax.scatter(j_rms[ok], TH[ok], s=5, c=color_rms, alpha=0.4, linewidths=0, zorder=2)
    p_miss = ax.scatter(j_rms[rms_miss], TH[rms_miss], s=5, c=color_miss, alpha=0.9, linewidths=0, zorder=3)
    p_alarm = ax.scatter(j_rms[rms_alarm], TH[rms_alarm], s=5, c=color_alarm, alpha=0.9, linewidths=0, zorder=3)
    p_eq = ax.scatter(I_eq_plot, TH, s=5, c=color_eq, alpha=0.8, linewidths=0, zorder=4)

    ref = ax.axhline(Th_ref, color="green", linestyle="--", linewidth=1.5, zorder=1)
    rated = ax.axvline(1.0, color=color_lines, linestyle="--", linewidth=1.5, zorder=1)

    ax.set_xlim(*xlim_pu)
    ax.set_ylim(*ylim_C)
    ax.set_xlabel("$I_{RMS}$ and $I_{eq}$ [pu of $I_R$]")
    ax.set_ylabel("Hot-spot temperature $\\Theta_H$ [°C]")
    #ax.grid(True, which="major", alpha=0.3)
    handles = [p_rms, p_miss, p_eq] + ([p_alarm] if rms_alarm.any() else []) + [ref, rated]
    labels = ["$I_{RMS}$", "Missed by $I_{RMS}$", "$I_{eq}$ (datasheet table)"] + \
             (["False alarm of $I_{RMS}$"] if rms_alarm.any() else []) + \
             [f"$\\Theta_{{ref}}$ = {Th_ref:g} °C", "Rated current $I_R$"]
    ax.legend(handles=handles, labels=labels, ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0),
              frameon=True, fontsize=12.5, markerscale=3, handlelength=1.25, handletextpad=0.4,
              columnspacing=0.8, borderpad=0.5, labelspacing=0.25)

    # Numbers for the text
    high = h_top > 50
    print(f"\n Datasheet test, compliant spectra ({model}, d = {d * 1e3:g} mm, {n_spectra} spectra, ambient "
          f"{amb_range[0]:g} to {amb_range[1]:g} degC, I_1 {loading_range[0]:g} to {loading_range[1]:g} pu, "
          f"TRD <= {trd_pct:g} %)")
    print(f"   table: rise {rise_tab.min():g} to {rise_tab.max():g} K in {rise_tab[1] - rise_tab[0]:g} K steps, "
          f"ambient {amb_tab.min():g} to {amb_tab.max():g} degC in {amb_tab[1] - amb_tab[0]:g} degC steps")
    print(f"   TRD {TRD.min():.2f} to {TRD.max():.2f} %, spectra with an order above 50: {high.sum()}")
    print(f"   spectra above {Th_ref:g} degC: {hot.sum()}, beyond the table (flagged as over the limit): {above.sum()}")
    print(f"   {'':6s} {'missed':>8s} {'max K above':>12s} {'false alarm':>12s} {'max K below':>12s}")
    print(f"   {'I_RMS':6s} {rms_miss.sum():8d} {rms_kmiss:12.2f} {rms_alarm.sum():12d} {rms_kalarm:12.2f}")
    print(f"   {'I_eq':6s} {eq_miss.sum():8d} {eq_kmiss:12.2f} {eq_alarm.sum():12d} {eq_kalarm:12.2f}")
    print(f"   missed by I_RMS with an order above 50: {np.sum(rms_miss & high)}, "
          f"with orders <= 50 only: {np.sum(rms_miss & ~high)}")
    print(f"   table interpolation vs exact I_eq: max error {tab_err:.4f} pu")

    # Split I_RMS failures: would the same I_RMS as a pure sinusoid also fail? (ambient) or not? (harmonics)
    rise_sin_same = full_chain(I_RMS, np.ones_like(I_RMS), np.ones_like(I_RMS), K)
    hot_sin = (T_amb + rise_sin_same) > Th_ref
    miss_harm, miss_amb = rms_miss & ~hot_sin, rms_miss & hot_sin
    alarm_harm, alarm_amb = rms_alarm & hot_sin, rms_alarm & ~hot_sin
    print(f"   I_RMS missed: {miss_harm.sum()} caused by harmonics "
          f"(up to {(TH[miss_harm].max() - Th_ref) if miss_harm.any() else 0:.2f} K above), "
          f"{miss_amb.sum()} caused by the ambient")
    print(f"   I_RMS false alarms: {alarm_amb.sum()} caused by the ambient, {alarm_harm.sum()} other")
    print(f"   harmonic-caused misses at ambient <= 30 degC: {np.sum(miss_harm & (T_amb <= 30))}")
    print(f"   I_eq false alarms: hot spots {np.sort(TH[eq_alarm]).round(2)} degC, "
          f"I_eq {np.sort(I_eq[eq_alarm]).round(4)} pu")

    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(figures_dir) / f"{fname}.pdf", dpi=dpi, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

plot_ieq_datasheet_test()