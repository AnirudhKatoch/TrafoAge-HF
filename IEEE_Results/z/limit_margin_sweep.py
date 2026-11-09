import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

CODE_DIR = Path(r"E:\IEEE_GM_2027_Transformer")
RESULTS_DIR = Path(r"E:\IEEE_GM_2027_Transformer\IEEE_Results")
FIGURES_DIR = RESULTS_DIR / "Figures"
DATAFRAMES_DIR = RESULTS_DIR / "Dataframes"
sys.path.insert(0, str(CODE_DIR))

from Input_parameters import Input_parameters_class
from Calculation_functions import Calculation_functions_class as CF


# Parameters of Table I that are swept: (key in trafo_specs or "d"/"T_amb", label for the plot)
PARAMS = [
    ("P_NL",                  "$P_{NL}$"),
    ("P_LL_R",                "$P_{LL\\text{-}R}$"),
    ("sigma",                 "$\\sigma$"),
    ("eddy_share",            "$\\varepsilon$"),
    ("conductor_resistivity", "$\\rho$"),
    ("d",                     "$d$"),
    ("Theta_TO_R",            "$\\Theta_{TO\\text{-}R}$"),
    ("Theta_g_R",             "$\\Theta_{g\\text{-}R}$"),
    ("x_oil",                 "$x$"),
    ("y_winding",             "$y$"),
    ("eddy_hotspot_factor",   "$c$"),
    ("T_amb",                 "$\\Theta_{amb}$"),
    ("Theta_ref",             "$\\Theta_{ref}$"),
    ("L_normal",              "$L_n$"),
]

# Multiplication factors on the nominal value: 1/5 ... 5 times
FACTORS = np.array([0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0])

# Physical upper bounds a factor may not exceed
CAPS = {"eddy_share": 1.0, "sigma": 0.99}


def limit_curve_pct(h, ext_pct=0.3):
    """IEEE 519-2022 Table 2 (Isc/IL < 20) for h <= 50, footnote a (even h <= 6 at 50 %), ext_pct above h = 50 [% of I_R]."""
    h = np.asarray(h)
    lim = np.select([h < 11, h < 17, h < 23, h < 35, h <= 50], [4.0, 2.0, 1.5, 0.6, 0.3], ext_pct)
    lim = np.where((h % 2 == 0) & (h <= 6), 0.5 * lim, lim)
    return lim


def tolerable_current_pct(trafo, d, T_amb_C, h, loading=1.0, model="dowell", n_current=1500):
    """
    I_h* [% of I_R] per order for one parameter set (hot spot at Theta_ref, single harmonic on the fundamental).
    Returns (I_star_pct, no_headroom). no_headroom is True when the hot spot is at or above Theta_ref
    without any harmonic, so every order fails.
    """
    I_R = trafo["I_R"]
    P_R, P_EC, P_OSL = CF.split_transformer_load_loss(P_LL_R=trafo["P_LL_R"], sigma=trafo["sigma"],
                                                      eddy_share=trafo["eddy_share"])
    w = CF.calculate_eddy_loss_weighting(harmonic_orders=h, f=50, conductor_thickness=d,
                                         rho=trafo["conductor_resistivity"], model=model)

    Theta_0, _ = CF.calculate_harmonic_sensitivity_map(trafo_specs=trafo, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                       h_orders=h[:1], I_h_values=np.array([0.0]), I_1=loading * I_R,
                                                       T_amb_C=T_amb_C, eddy_weights=w[:1])
    if float(Theta_0.ravel()[0]) >= trafo["Theta_ref"]:
        return np.zeros(h.size), True

    I_h = np.geomspace(1e-5 * I_R, 3.0 * I_R, n_current)
    _, Life = CF.calculate_harmonic_sensitivity_map(trafo_specs=trafo, P_R=P_R, P_EC=P_EC, P_OSL=P_OSL,
                                                    h_orders=h, I_h_values=I_h, I_1=loading * I_R,
                                                    T_amb_C=T_amb_C, eddy_weights=w)
    I_star = CF.iso_life_current(I_h_values=I_h, Life_years=Life, L_target=trafo["L_normal"] / 8760.0)
    return 100.0 * I_star / I_R, False


def margin_summary(I_star_pct, h, ext_pct=0.3):
    """
    Margin M(h) = I_h* / limit(h).
    Returns the smallest margin, the order where it occurs, and the first order where M < 1
    (the limit crosses the transformer curve), or None if they never cross.
    """
    M = I_star_pct / limit_curve_pct(h, ext_pct)
    j = int(np.nanargmin(M))
    cross = np.where(M < 1.0)[0]
    h_cross = int(h[cross[0]]) if cross.size else None
    return float(M[j]), int(h[j]), h_cross


def sweep_one_at_a_time(factors=FACTORS, h_max=400, d_nom=2.5e-3, loading=1.0,
                        ext_pct=0.3, model="dowell", params=PARAMS):
    """
    Multiply every parameter of Table I by each factor while all others stay nominal, and record
    the smallest margin to the IEEE 519 limit (h <= 50) and its extension (h > 50), and where they first cross.

    Returns DataFrame: param, label, factor, value, M_min, h_min, h_cross, no_headroom, fails
    """
    params_in = Input_parameters_class()
    base = dict(params_in.trafo_specs)
    T_nom = float(np.mean(params_in.T_amb)) - 273.15
    h = np.arange(2, h_max + 1)

    rows = []
    for key, label in params:
        for f in factors:
            trafo = dict(base)
            d, T_amb = d_nom, T_nom
            if key == "d":
                d = d_nom * f
                value = d * 1e3
            elif key == "T_amb":
                T_amb = T_nom * f
                value = T_amb
            else:
                trafo[key] = min(base[key] * f, CAPS.get(key, np.inf))
                value = trafo[key]
            I_star, no_headroom = tolerable_current_pct(trafo, d, T_amb, h, loading, model)
            M, h_min, h_cross = margin_summary(I_star, h, ext_pct)
            rows.append({"param": key, "label": label, "factor": f, "value": value,
                         "M_min": M, "h_min": h_min, "h_cross": h_cross,
                         "no_headroom": no_headroom, "fails": M < 1.0})
        print(f"  {key} done")
    return pd.DataFrame(rows)


def plot_margin_map(df, fname="limit_margin_sweep", figures_dir=FIGURES_DIR, M_range=(0.1, 10.0)):
    """
    Heat map: x = parameter, y = factor on the nominal value, colour = smallest margin to the limit (log scale).
    Blue = limit far below the transformer's tolerable current (safe), white = touching (M = 1), red = exceeded.
    Cell text:
        none    the limit and the transformer curve never cross
        all     no headroom without harmonics, every order fails
        h / h*  first order where the limit crosses the curve, * where h <= 50 (IEEE 519 itself)
    """
    plt.rcParams.update({"font.size": 13, "font.family": ["Calibri"]})

    keys = list(dict.fromkeys(df["param"]))
    labels = [df.loc[df.param == k, "label"].iloc[0] for k in keys]
    factors = np.sort(df["factor"].unique())

    logM = np.full((factors.size, len(keys)), np.nan)
    text = np.empty((factors.size, len(keys)), dtype=object)
    for j, k in enumerate(keys):
        g = df[df.param == k].set_index("factor")
        for i, f in enumerate(factors):
            r = g.loc[f]
            logM[i, j] = np.log10(max(r["M_min"], 1e-3))
            if r["no_headroom"]:
                text[i, j] = "all"
            elif pd.isna(r["h_cross"]):
                text[i, j] = "none"
            else:
                hc = int(r["h_cross"])
                text[i, j] = f"{hc}" + ("*" if hc <= 50 else "")

    norm = TwoSlopeNorm(vmin=np.log10(M_range[0]), vcenter=0.0, vmax=np.log10(M_range[1]))
    fig, ax = plt.subplots(figsize=(1.0 * len(keys) + 2, 0.45 * factors.size + 2), constrained_layout=True)
    im = ax.imshow(np.clip(logM, *np.log10(M_range)), cmap="RdBu", norm=norm, aspect="auto", origin="lower")

    for i in range(factors.size):
        for j in range(len(keys)):
            ax.text(j, i, text[i, j], ha="center", va="center", fontsize=8,
                    color="white" if abs(logM[i, j]) > 0.6 else "black")

    ax.set_xticks(range(len(keys)))
    ax.set_xticklabels(labels)
    ax.set_yticks(range(factors.size))
    ax.set_yticklabels([f"x{f:g}" for f in factors])
    ax.axhline(np.where(np.isclose(factors, 1.0))[0][0], color="black", linewidth=0.8, alpha=0.4)
    ax.set_xlabel("Parameter (all others nominal)")
    ax.set_ylabel("Factor on nominal value")

    cb = fig.colorbar(im, ax=ax)
    ticks = [M_range[0], 0.3, 1, 3, M_range[1]]
    cb.set_ticks(np.log10(ticks))
    cb.set_ticklabels([f"{t:g}" for t in ticks])
    cb.set_label("Smallest margin $I_h^*$ / limit")

    out = Path(figures_dir)
    out.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(out / f"{fname}.{ext}", dpi=300)
    plt.close(fig)
    print(f" Figure written to {out / fname}.png / .pdf")


# ==================================================================== #
# Run
# ==================================================================== #

DATAFRAMES_DIR.mkdir(parents=True, exist_ok=True)

df = sweep_one_at_a_time()
df.to_csv(DATAFRAMES_DIR / "margin_sweep.csv", index=False)
plot_margin_map(df)

loss_only = [p for p in PARAMS if p[0] not in ("T_amb", "Theta_TO_R", "Theta_g_R", "Theta_ref", "L_normal")]
df_loss = sweep_one_at_a_time(params=loss_only)
df_loss.to_csv(DATAFRAMES_DIR / "margin_sweep_loss.csv", index=False)
plot_margin_map(df_loss, fname="limit_margin_sweep_loss")