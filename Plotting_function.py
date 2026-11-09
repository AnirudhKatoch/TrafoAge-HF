"""
Plotting functions of the transformer assessment (working figures, png, 300 dpi).
The column-width paper figures (pdf) are made separately by paper_figures.py.

No physics is done here: every function only draws arrays that
Calculation_functions.py has computed. What each figure is for:

    Fig_1   apparent power and current over the mission profile   -> is the input what I meant?
    Fig_2   ambient temperature and THD over the profile
    Fig_3   per-unit spectrum (log), with 2.5 kHz and 9 kHz marked   -> where is the emission?
    Fig_4   harmonic loss factors F_HL and F_HL-STR over the profile
    Fig_5   total loss                     Fig_6  hot-spot temperature
    Fig_7   loss of life and equivalent life
    Fig_8   F_HL and life for each truncation (h <= 50, h <= 180, full)   -> what is missed by stopping early?
    Fig_9/10  Monte Carlo life distribution and B10 (TODO: arbitrary 1 % spreads)
    Fig_11  single-harmonic life map, square law                -> the heat map
    Fig_12  eddy-loss weighting w(h) per model and thickness    -> how much the corrections bend h^2
    Fig_13  life map for every eddy-loss model
    Fig_14  tolerable current I_h* per model against the IEEE 519 limits   -> the main result
    Fig_15/16  sensitivity of I_h* to sigma and to the loading
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")   # non-interactive backend, no windows
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.colors import LogNorm

# Times New Roman to match IEEE figures; falls back to similar serif fonts on machines without it
plt.rcParams.update({"font.size": 15, "font.family": "serif",
                     "font.serif": ["Times New Roman", "Nimbus Roman", "STIXGeneral", "DejaVu Serif"],
                     "mathtext.fontset": "stix", "axes.labelsize": 15, "axes.titlesize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

Y_MARGIN = 0.05   # fractional padding above/below the data range on linear axes

def _ylim(*arrs):
    """Min/max across the given arrays with a fractional margin."""
    lo = min(np.nanmin(a) for a in arrs)
    hi = max(np.nanmax(a) for a in arrs)
    pad = (abs(lo) * Y_MARGIN or 1.0) if lo == hi else (hi - lo) * Y_MARGIN
    return lo - pad, hi + pad


def _draw_emission_limits(ax, limits, I_R, h_max, color="tab:red"):
    """
    Per-order current limits as a step line (in A, % of I_R converted with the
    transformer rated current), and the band above the last limit shaded: there
    IEEE 519-2022 Table 2 and IEEE 1547-2018 Table 26 set no individual limit.
    """
    if not limits:
        return
    bands = limits["bands"]
    xs, ys = [], []
    for h0, h1, pct in bands:
        xs += [h0, h1]
        ys += [pct / 100.0 * I_R] * 2
    ax.plot(xs, ys, color=color, linewidth=1.8, label=limits.get("label", "Emission limit"))
    h_top = bands[-1][1]
    ax.axvspan(h_top, h_max, color=color, alpha=0.06, lw=0)
    ax.text(0.5 * (h_top + h_max), 0.03, "no individual current limit", color=color,
            ha="center", va="bottom", fontsize=11, transform=ax.get_xaxis_transform())


def _x_axis(n):
    x = np.arange(n)
    return x, (x[0], x[-1] if n > 1 else 1)


class Plotting_functions_class:

    @staticmethod
    def plot_mission_profile(df_1_mission_profile, figures_dir, xlabel):
        """
            Fig_1 : S_RMS / I_RMS        (2 stacked subplots)
            Fig_2 : T_amb / THD          (2 stacked subplots)
        """
        df = df_1_mission_profile
        x, x_range = _x_axis(len(df))

        fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(6.4, 4.8 * 1.5), sharex=True)
        S_kVA = df["S_RMS"].to_numpy() / 1e3
        ax_a.plot(x, S_kVA, color="tab:blue")
        ax_a.set_ylabel("Apparent power [kVA]")
        ax_a.set_title("Apparent power")
        ax_a.set_ylim(_ylim(S_kVA))
        ax_a.grid(True, alpha=0.3)

        ax_b.plot(x, df["I_1"], color="tab:orange", label="Fundamental")
        ax_b.plot(x, df["I_RMS"], color="tab:red", linestyle="--", label="Total RMS")
        ax_b.set_xlabel(xlabel)
        ax_b.set_ylabel("Current [A]")
        ax_b.set_title("Current entering the transformer")
        ax_b.set_ylim(_ylim(df["I_1"], df["I_RMS"]))
        ax_b.set_xlim(x_range)
        ax_b.legend()
        ax_b.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_1_power_current.png", dpi=300)
        plt.close(fig)

        fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(6.4, 4.8 * 1.5), sharex=True)
        T_C = df["T_amb"].to_numpy() - 273.15
        ax_a.plot(x, T_C, color="tab:blue")
        ax_a.set_ylabel("Temperature [°C]")
        ax_a.set_title("Ambient temperature")
        ax_a.set_ylim(_ylim(T_C))
        ax_a.grid(True, alpha=0.3)

        thd = df["THD"].to_numpy()
        ax_b.plot(x, thd, color="tab:green")
        ax_b.set_xlabel(xlabel)
        ax_b.set_ylabel("THD [%]")
        ax_b.set_title("Current distortion (full spectrum)")
        if np.any(np.isfinite(thd)):
            ax_b.set_ylim(_ylim(thd[np.isfinite(thd)]))
        ax_b.set_xlim(x_range)
        ax_b.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_2_Tamb_THD.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_harmonic_spectrum(spectrum_pu, figures_dir, f, truncation_orders=(50, 180), floor=1e-6):
        """
            Fig_3 : I_h / I_1 on a log axis, with the truncation orders marked
        """
        spectrum_pu = np.asarray(spectrum_pu, dtype=float)
        orders = np.arange(1, spectrum_pu.size + 1)

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        ax.bar(orders, np.maximum(spectrum_pu, floor), width=1.0, color="tab:green", edgecolor="tab:green")
        ax.set_yscale("log")
        ax.set_ylim(floor, 2.0)

        for h in truncation_orders:
            if h is not None and h <= orders[-1]:
                ax.axvline(h, color="black", linestyle="--", linewidth=1.0)
                ax.text(h, 0.3, f" {h * f / 1e3:g} kHz", rotation=90, va="top", ha="right", fontsize=12)

        ax.set_xlabel("Harmonic order [-]")
        ax.set_ylabel("$I_h / I_1$  [-]")
        ax.set_title("Spectrum of the current entering the transformer")
        ax.set_xlim(0, orders[-1])
        ax.grid(True, alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_3_spectrum.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_trafo_profile(df_3_trafo, figures_dir, xlabel):
        """
            Fig_4 : F_HL / F_HL_STR      (2 stacked subplots)
            Fig_5 : P_T
            Fig_6 : Theta_H
            Fig_7 : loss of life and equivalent life (bars)
        """
        df = df_3_trafo
        x, x_range = _x_axis(len(df))

        fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(6.4, 4.8 * 1.5), sharex=True)
        ax_a.plot(x, df["F_HL"], color="tab:blue")
        ax_a.set_ylabel("$F_{HL}$ [-]")
        ax_a.set_title("Harmonic loss factor, winding eddy")
        ax_a.set_ylim(_ylim(df["F_HL"]))
        ax_a.grid(True, alpha=0.3)
        ax_b.plot(x, df["F_HL_STR"], color="tab:purple")
        ax_b.set_xlabel(xlabel)
        ax_b.set_ylabel("$F_{HL-STR}$ [-]")
        ax_b.set_title("Harmonic loss factor, other stray")
        ax_b.set_ylim(_ylim(df["F_HL_STR"]))
        ax_b.set_xlim(x_range)
        ax_b.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_4_harmonic_loss_factors.png", dpi=300)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        ax.plot(x, df["P_T"], color="tab:blue")
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Losses [W]")
        ax.set_title("Total transformer losses")
        ax.set_xlim(x_range)
        ax.set_ylim(_ylim(df["P_T"]))
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_5_losses_P_T.png", dpi=300)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        ax.plot(x, df["Theta_H"], color="tab:red")
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Temperature [°C]")
        ax.set_title("Transformer hot-spot temperature")
        ax.set_xlim(x_range)
        ax.set_ylim(_ylim(df["Theta_H"]))
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_6_hotspot_Theta_H.png", dpi=300)
        plt.close(fig)

        LOL_value = float(df["LOL_trafo"].iloc[-1]) * 100.0
        Life_value = float(df["Lifetime_trafo"].iloc[-1])

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        ax_r = ax.twinx()
        bar_LOL = ax.bar(0, LOL_value, width=0.5, color="red")
        bar_life = ax_r.bar(1, Life_value, width=0.5, color="blue")
        ax.set_ylabel("Life consumed [%]")
        ax_r.set_ylabel("Equivalent life [years]")
        ax.set_ylim(0, LOL_value * (1 + 4 * Y_MARGIN) if LOL_value > 0 else 1.0)
        ax_r.set_ylim(0, Life_value * (1 + 4 * Y_MARGIN) if np.isfinite(Life_value) and Life_value > 0 else 1.0)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Life consumed", "Equivalent life"])
        ax.set_xlim(-0.6, 1.6)
        ax.set_title("Transformer loss of life")
        ax.bar_label(bar_LOL, fmt="%.4f", padding=3)
        ax_r.bar_label(bar_life, fmt="%.2f", padding=3)
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_7_loss_of_life.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_truncation_comparison(df_5_truncation, figures_dir):
        """
            Fig_8 : F_HL and equivalent life for each truncation of the spectrum
        """
        df = df_5_truncation
        labels = df["label"].tolist()
        pos = np.arange(len(labels))

        fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(6.4, 4.8 * 1.5), sharex=True)

        bars = ax_a.bar(pos, df["F_HL_mean"], color="tab:blue", edgecolor="black", width=0.5)
        ax_a.bar_label(bars, fmt="%.2f", padding=3)
        ax_a.set_ylabel("$F_{HL}$ [-]")
        ax_a.set_title("Harmonic loss factor by evaluated band")
        ax_a.set_ylim(0, df["F_HL_mean"].max() * 1.2)

        bars = ax_b.bar(pos, df["Lifetime_trafo"], color="tab:red", edgecolor="black", width=0.5)
        ax_b.bar_label(bars, fmt="%.2f", padding=3)
        ax_b.set_ylabel("Equivalent life [years]")
        ax_b.set_title("Predicted life by evaluated band")
        ax_b.set_ylim(0, df["Lifetime_trafo"].max() * 1.2)
        ax_b.set_xticks(pos)
        ax_b.set_xticklabels(labels)

        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_8_truncation_comparison.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_harmonic_heatmap(h_orders, I_h_values, Life_years, I_R, figures_dir, f, fname,
                              life_floor=0.1, life_contours=(20, 10, 5, 1), truncation_orders=(50, 180),
                              y_scale="linear", h_max_plot=500):
        """
            Fig_11 : equivalent life against harmonic order (x) and harmonic
                     current (y), log colour scale, iso-life contours and the
                     2.5 kHz / 9 kHz assessment limits marked.
        """
        h = np.asarray(h_orders, dtype=float)
        I_h = np.asarray(I_h_values, dtype=float)
        Life = np.asarray(Life_years, dtype=float)

        life_top = np.nanmax(Life)
        Life_plot = np.clip(Life, life_floor, life_top)

        fig, ax = plt.subplots(figsize=(6.4 * 1.25, 4.8 * 1.15))
        mesh = ax.pcolormesh(h, I_h, Life_plot, shading="nearest", cmap="inferno",
                             norm=LogNorm(vmin=life_floor, vmax=life_top), rasterized=True)
        cbar = fig.colorbar(mesh, ax=ax, extend="min", pad=0.13)
        cbar.set_label("Equivalent life [years]")

        levels = sorted(l for l in life_contours if life_floor < l < life_top)
        if levels:
            cs = ax.contour(h, I_h, Life, levels=levels, colors="white", linewidths=1.0)
            ax.clabel(cs, fmt=lambda v: f"{v:g} yr", fontsize=11)

        for ho in truncation_orders:
            if ho is not None and ho <= h_max_plot:
                ax.axvline(ho, color="cyan", linestyle="--", linewidth=1.0)
                ax.text(ho, I_h[-1], f" {ho * f / 1e3:g} kHz", color="cyan", rotation=90,
                        va="top", ha="right", fontsize=12)

        ax.set_yscale(y_scale)
        ax.set_xlim(0, h_max_plot)
        ax.set_ylim(I_h[0], I_h[-1])
        ax.set_xlabel("Harmonic order [-]")
        ax.set_ylabel("Harmonic current $I_h$ [A]")
        ax.set_title("Transformer life under a single harmonic")

        sec = ax.secondary_yaxis("right", functions=(lambda I: 100.0 * I / I_R, lambda p: p * I_R / 100.0))
        sec.set_ylabel("$I_h$ [% of $I_R$]")

        fig.tight_layout()
        fig.savefig(f"{figures_dir}/{fname}.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_eddy_weighting(h_orders, weight_curves, figures_dir, f):
        """
            Fig_12 : winding eddy-loss weighting w(h) per conductor thickness,
                     against the h^2 of IEEE C57.110 (log-log)
        """
        h = np.asarray(h_orders, dtype=float)
        colors = plt.cm.viridis(np.linspace(0.0, 0.85, len(weight_curves)))

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        for (label, w), c in zip(weight_curves.items(), colors):
            style = dict(color="black", linestyle="--", linewidth=1.8) if "C57" in label else dict(color=c, linewidth=1.6)
            ax.plot(h, w, label=label, **style)

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(1, h[-1])
        ax.set_xlabel("Harmonic order $h$ [-]")
        ax.set_ylabel("Eddy-loss weighting $w(h)$ [-]")
        ax.set_title("Winding eddy loss per unit current$^2$")
        ax.grid(True, alpha=0.3, which="both")
        ax.legend(fontsize=12)

        sec = ax.secondary_xaxis("top", functions=(lambda x: x * f / 1e3, lambda k: k * 1e3 / f))
        sec.set_xlabel("Frequency [kHz]")

        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_12_eddy_weighting.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_heatmap_sweep(h_orders, I_h_values, Life_maps, labels, I_R, figures_dir, f, life_floor=0.1,
                           L_iso=None, truncation_orders=(50, 180)):
        """
            Fig_13 : the single-harmonic life map for every eddy-loss model of
                     the sweep, on one shared log colour scale (log current axis)
        """
        h = np.asarray(h_orders, dtype=float)
        I_h = np.asarray(I_h_values, dtype=float)
        life_top = max(np.nanmax(L) for L in Life_maps)
        norm = LogNorm(vmin=life_floor, vmax=life_top)

        n = len(Life_maps)
        ncols = 3
        nrows = int(np.ceil((n + 1) / ncols))   # one free cell for the colour bar
        fig, axes = plt.subplots(nrows, ncols, figsize=(6.0 * ncols, 4.6 * nrows), sharex=True, sharey=True)
        axes = np.atleast_1d(axes).ravel()

        for ax, L, lab in zip(axes, Life_maps, labels):
            mesh = ax.pcolormesh(h, I_h, np.clip(L, life_floor, life_top), shading="nearest",
                                 cmap="inferno", norm=norm, rasterized=True)
            if L_iso is not None and life_floor < L_iso < life_top:
                ax.contour(h, I_h, L, levels=[L_iso], colors="white", linewidths=1.4)
            for ho in truncation_orders:
                ax.axvline(ho, color="cyan", linestyle="--", linewidth=0.9)
            ax.set_yscale("log")
            ax.set_xlim(0, h[-1])
            ax.set_ylim(I_h[0], I_h[-1])
            ax.set_title(lab)

        for ax in axes[n:]:
            ax.axis("off")

        for i, ax in enumerate(axes[:n]):
            if i % ncols == 0:
                ax.set_ylabel("$I_h$ [A]")
            if i + ncols >= n:                      # nothing drawn below this panel
                ax.set_xlabel("Harmonic order [-]")
                ax.xaxis.set_tick_params(labelbottom=True)

        cbar = fig.colorbar(mesh, ax=axes.tolist(), extend="min", fraction=0.025, pad=0.02)
        cbar.set_label("Equivalent life [years]")
        fig.suptitle("Single-harmonic life map by winding eddy-loss model "
                     "(white: hot spot at reference, normal ageing)", fontsize=16)
        fig.savefig(f"{figures_dir}/Fig_13_heatmap_sweep.png", dpi=250, bbox_inches="tight")
        plt.close(fig)

    @staticmethod
    def plot_iso_life_boundaries(h_orders, iso_currents, I_R, figures_dir, f, truncation_orders=(50, 180),
                                 limits=None, fname="Fig_14_iso_life_boundaries", title=None):
        """
            Fig_14 : harmonic current at which the transformer reaches its
                     normal ageing rate, against harmonic order, one line per
                     eddy-loss model. Below a line the harmonic is tolerable,
                     above it the transformer ages faster than normal. The
                     per-order emission limits are overlaid when given.
            Also used for the sensitivity figures (Fig_15, Fig_16).
        """
        h = np.asarray(h_orders, dtype=float)
        colors = plt.cm.viridis(np.linspace(0.0, 0.85, len(iso_currents)))

        fig, ax = plt.subplots(figsize=(6.4 * 1.15, 4.8 * 1.1))
        for (label, I_iso), c in zip(iso_currents.items(), colors):
            style = dict(color="black", linestyle="--", linewidth=1.8) if "C57" in label else dict(color=c, linewidth=1.6)
            ax.plot(h, I_iso, label=label, **style)

        _draw_emission_limits(ax, limits, I_R, h[-1])

        for ho in truncation_orders:
            ax.axvline(ho, color="grey", linestyle=":", linewidth=1.2)
            ax.text(ho, I_R, f" {ho * f / 1e3:g} kHz", rotation=90,
                    va="top", ha="right", fontsize=11, color="grey")

        ax.set_yscale("log")
        ax.set_xlim(0, h[-1])
        ax.set_ylim(top=I_R)
        ax.set_xlabel("Harmonic order [-]")
        ax.set_ylabel("Tolerable harmonic current $I_h$ [A]")
        ax.set_title(title or "Harmonic current that brings the hot spot to its reference")
        ax.grid(True, alpha=0.3, which="both")
        ax.legend(fontsize=11, loc="upper right")

        sec = ax.secondary_yaxis("right", functions=(lambda I: 100.0 * I / I_R, lambda p: p * I_R / 100.0))
        sec.set_ylabel("$I_h$ [% of $I_R$]")

        fig.tight_layout()
        fig.savefig(f"{figures_dir}/{fname}.png", dpi=300)
        plt.close(fig)

    @staticmethod
    def plot_lifetime_monte_carlo_trafo(Lifetime_trafo_MC, figures_dir, B10_trafo=None, plot_type="histogram", bins=50):
        """
            Fig_9  : distribution of the Monte Carlo lifetimes
            Fig_10 : unreliability curve with the B10 point marked
        """
        data = np.asarray(Lifetime_trafo_MC, dtype=float)
        data = data[np.isfinite(data)]
        if data.size == 0:
            raise ValueError("No finite Monte Carlo samples to plot for the transformer.")

        if B10_trafo is None:
            B10_trafo = np.percentile(data, 10)

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        if plot_type == "histogram":
            ax.hist(data, bins=bins, color="red", edgecolor="black", linewidth=0.8)
            ax.set_ylabel("Count")
        elif plot_type == "line":
            kde = gaussian_kde(data)
            xs = np.linspace(data.min(), data.max(), 200)
            ax.plot(xs, kde(xs), color="red")
            ax.set_ylabel("Probability density")
        else:
            raise ValueError("plot_type must be 'histogram' or 'line'.")
        ax.set_title("Transformer")
        ax.set_xlabel("Lifetime [years]")
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_9_lifetime_MC_trafo.png", dpi=300)
        plt.close(fig)

        years = np.sort(data)
        unreliability = np.arange(1, years.size + 1) / years.size

        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        ax.plot(years, unreliability, color="red", linewidth=1.5)
        ax.axhline(0.1, color="black", linestyle="--", linewidth=1.2)
        ax.axvline(B10_trafo, color="black", linestyle="--", linewidth=1.2)
        ax.plot(B10_trafo, 0.1, "ko", markersize=5)
        ax.set_xlabel("Lifetime [years]")
        ax.set_ylabel("Unreliability")
        ax.set_title("Transformer")
        ax.set_xlim(years[0], B10_trafo * 1.05)
        ax.set_ylim(0, 0.11)
        fig.tight_layout()
        fig.savefig(f"{figures_dir}/Fig_10_unreliability_trafo.png", dpi=300)
        plt.close(fig)
