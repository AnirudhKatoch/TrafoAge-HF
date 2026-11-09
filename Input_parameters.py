import numpy as np


class Input_parameters_class:

    def __init__(self):

        '''
        Inputs of the transformer assessment.

        The transformer is assessed from the current entering its low-voltage
        (LV) winding. That current is described by two things:

            1. Its MAGNITUDE, fixed at each mission-profile sample by the
               apparent power and the line-to-line voltage at the connection
               point:  I_1 = S / (sqrt(3) * V_LL).

            2. Its SHAPE, a per-unit harmonic spectrum I_h / I_1, supplied either
               parametrically (a dictionary of orders and magnitudes) or from a
               file produced by a converter simulation or a measurement
               (for example df_7_harmonics.parquet written by the PEARL LCL code).

        Everything downstream, namely the harmonic loss factors, the load and
        total losses, the top-oil and hot-spot temperatures, the ageing
        acceleration and the loss of life, follows from those two inputs and
        the transformer data below.

        '''

        # ----------------------------------------#
        # System parameters
        # ----------------------------------------#

        self.f = 60          # [Hz] Fundamental frequency. European grid (the Siemens data are for a 60 Hz market).
        self.phases = 3      # [-]  Number of phases on the LV side (1 or 3). The unit is three-phase, Dyn5 [Siemens].

        # ----------------------------------------#
        # Mission profile
        # ----------------------------------------#
        # One sample per day for a year. For the paper only a CONSTANT profile is
        # used (rated load, 25 °C), so the "mission profile" reduces to one
        # operating point repeated 365 times. A real profile (PV, data centre)
        # can be dropped in here without changing anything else.

        self.Profile_size = 365                    # [-] Number of mission-profile samples
        self.seconds_per_sample = 24 * 3600        # [s] Wall-clock duration each sample represents (86400 = one sample per day)

        self.S_RMS = np.full(self.Profile_size, 2.5e6)             # [VA] Apparent power through the transformer: rated, 1 MVA (worst steady case)
        self.V_LL_RMS = np.full(self.Profile_size, 400.0)        # [V]  Line-to-line RMS voltage at the LV terminal (see V_LV below)
        # Ambient 25 °C: assumed
        # IEEE C57.12.00 (30 °C average, 40 °C maximum; NOT READ, only quoted in C57.91)
        # would be the rating basis. At 30 °C this unit already sits at its 110 °C
        # reference with no harmonics.
        self.T_amb = np.full(self.Profile_size, 273.15 + 25)     # [K]  Ambient temperature around the transformer

        # Multiplier on the non-fundamental part of the spectrum at each sample [-].
        # 1.0 reproduces the spectrum as given; values above 1 emulate a growing
        # emission (e.g. an ageing upstream filter), 0 a purely sinusoidal current.
        self.harmonic_scale = np.full(self.Profile_size, 1.0)

        # ----------------------------------------#
        # Harmonic spectrum of the current entering the transformer
        # ----------------------------------------#

        # 500 x 50 Hz = 25 kHz. Above ~25 kHz the winding capacitances start to
        # shape the current distribution and a loss model of resistive windings
        # stops being meaningful.
        # not from a source; the first winding resonance of a real 1 MVA unit
        # would set it.
        self.h_max = 500                     # [-] Highest harmonic order retained
        self.spectrum_source = "parametric"  # ["parametric" or "file"]

        # Per-unit spectrum I_h / I_1 used when spectrum_source = "parametric".
        # Illustrative spectrum of a two-level SPWM inverter at fsw = 10 kHz and
        # f = 50 Hz (frequency modulation ratio mf = fsw/f = 200): small low-order
        # content, the first carrier group at mf±2, mf±4 and the second at 2mf±1.
        # (Sideband positions: standard PWM theory, e.g. Holmes & Lipo; NOT READ.)
        # to the grid-side current of the PEARL LCL study". They are not a
        # measurement. Replace with a measured or simulated spectrum.
        self.harmonics_pu = {
            5: 0.0020, 7: 0.0015, 11: 0.0010, 13: 0.0008,        # low-order characteristic harmonics
            196: 0.0015, 198: 0.0055, 202: 0.0055, 204: 0.0015,  # first switching sideband group (~10 kHz)
            397: 0.0012, 401: 0.0012,                            # second switching sideband group (~20 kHz)
        }

        # File input used when spectrum_source = "file". Parquet or CSV with
        # columns "order" and "I_rms" (absolute or per-unit); optional columns
        # "component" and "second" are filtered on if present. The spectrum is
        # normalised to its own fundamental and applied to every sample.
        self.spectrum_file = {
            "path": "Results/Simulation_1/Dataframes/df_7_harmonics.parquet",
            "component": "L2",   # None to skip the filter
            "second": -1,        # -1 = last second in the file
        }

        # Truncations at which the harmonic loss factor is also evaluated, to
        # compare established practice against the full spectrum:
        #   50   -> 2.5 kHz: per-order limits of IEEE 519-2022 Table 2 (35 <= h <= 50)
        #           and IEEE 1547-2018 Table 26 (h < 50) stop here; 519 Clause 4 requires
        #           measurement "at least up to the 50th order".
        #   180  -> 9 kHz: IEC 61000-4-7 Annex B (informative, provisional) measures up to
        #           about 9 kHz [DIN EN 61000-4-7:2009-12, Clause 1 and Annex B, read].
        #   None -> full spectrum up to h_max
        self.truncation_orders = [50, 180, None]

        # ----------------------------------------#
        # Harmonic sensitivity heat map
        # ----------------------------------------#
        # A single harmonic of order h and RMS current I_h is placed on top of
        # a sinusoidal fundamental; colour = equivalent life of the transformer.

        self.heatmap = {
            "I_1_pu": 1.0,           # [-] Fundamental current as a fraction of I_R (rated load: smallest headroom)
            "n_current": 400,        # [-] Number of current steps between 0 and I_R (resolution of the map)
            "life_floor_years": 0.1, # [years] Lower end of the colour scale; shorter lives are shown saturated
            "life_contours": [20, 10, 5, 1],  # [years] Iso-life lines drawn on the map

            # Conductor thicknesses [m] for the skin-depth sweep; None = IEEE C57.110 (h^2).
            # Crossover h_c = (delta_50Hz / d)^2 for copper at 75 °C (delta = 10.31 mm):
            # 0.5 mm -> 426, 1 mm -> 106, 2 mm -> 27, 3 mm -> 12.
            # Range: published strip thicknesses are 1.6 and 3.6 mm (Thango 2020, two
            # oil-immersed units, 14.2 x 1.6 and 12.1 x 3.6 mm) and 3.65 mm (C57.110
            # Annex C example, 3.65 x 11 mm).
            "thickness_sweep": [None, 0.5e-3, 1e-3, 2e-3, 3e-3, 4e-3],
        }

        # ----------------------------------------#
        # Sensitivity of the tolerable-current boundary
        # ----------------------------------------#

        self.sensitivity = {
            "sigma_sweep": [0.03, 0.05, 0.10, 0.15],   # [-] Total stray loss / rated load loss. Assumed range,
            "loading_sweep": [0.5, 0.75, 1.0],         # [pu] Fundamental current as a fraction of I_R
            "thicknesses": [None, 2.0e-3],             # [m] Eddy models the sweeps are shown for (None = C57.110)
            "hotspot_factor_sweep": [1.0, 6.4],        # [-] Uniform eddy distribution vs. C57.110 Sec. 6.2 concentration
        }

        # ----------------------------------------#
        # Current emission limits (per harmonic order)
        # ----------------------------------------#
        # IEEE Std 519-2022 Table 2, row Isc/IL < 20, 120 V - 69 kV, in % of I_L
        # (maximum demand current). Footnote c: power generation facilities are
        # held to this row whatever their Isc/IL. The first band starts at h = 2
        # in the 2022 edition (h = 3 in 2014). Footnote a: even h <= 6 are limited
        # to 50 % of these values (not modelled; only matters below h = 7).
        # IEEE 1547-2018 Table 26 gives the same values for DER, in % of the DER
        # rated current, for h < 50; its TRD of 5 % is defined on the full RMS.
        # Above h = 50 no individual current limit applies in either standard.
        # The limits are drawn in % of I_R of the transformer, i.e. the converter
        # is taken to be rated at the transformer rating (assumed).
        self.emission_limits = {
            "label": "IEEE 519 limit",
            "bands": [(2, 11, 4.0), (11, 17, 2.0), (17, 23, 1.5), (23, 35, 0.6), (35, 51, 0.3)],  # (h_from, h_to_excl, % of I_R)
        }

        # ----------------------------------------#
        # Transformer specs
        # ----------------------------------------#

        self.trafo_specs = {

            # References
            # [C] Siemens AG, "Planning data for oil-immersed transformers FITformer®", Erlangen, Germany, Jun. 2020.
            #     1,000 kVA row, AA0-Ak loss series, EN 50588-1 / IEC TS 60076-20 level 2,
            #     10 kV / 400 V, Dyn5, u_k = 6 %, P0 = 693 W, Pk75 = 7600 W.        READ
            # [D] IEEE Std C57.110-2018                                               READ
            # [E] IEC 60076-7:2018 (only Table 4 read)                                PARTLY READ
            # [F] IEEE Std C57.91-2011                                                READ

            # ── Ratings ──────────────────────────────────────────────────────
            'S_r': 2.5e6,                          # [VA] Rated apparent power.                                      from [C]
            # The data sheet unit is 400 V. 690 V is ASSUMED, to match a converter
            # terminal (large PV inverters and drives use 690 V). The losses are
            # carried over unchanged.
            # so its loss split would differ; the assumption is that the totals stay.
            'V_LV': 400,                         # [V]  Rated line-to-line voltage of the LV winding
            'I_R': 2.5e6 / (np.sqrt(3) * 400),   # = 3608.4 A

            # ── Losses ───────────────────────────────────────────────────────
            'P_LL_R': 18500,   # [W] Rated load loss at the reference winding temperature of 75 °C.       from [C] column Pk75
            'P_NL': 1575,      # [W] No-load (core) loss; voltage-driven, enters the total unmodified.  from [C] column P0
                              #     Core loss under voltage harmonics is ignored ([D] Annex B: "operating experience
                              #     has not indicated that core temperature rise will ever be the limiting parameter").

            # ── Load-loss split (C57.110) ────────────────────────────────────
            # sigma = total stray loss / rated load loss. NOT on the data sheet; [D] Eq. (22)
            # would get it from a test report. ASSUMED 5 % and swept 3-15 %.
            # 4060 / 31 881 = 12.7 % (a larger unit).
            'sigma': 0.05,
            'eddy_share': 0.3,  # [-] Share of the total stray loss in the windings, liquid-immersed 1000 kVA.
                                 #     [D] Eq. (24) and Table 14 (>300 to <=1000 kVA: LV 40 %, HV 10 %, other stray 50 %)
                                 #     [D] calls Table 14 "conservative estimates ... should not be followed if better
                                 #     data is available from the manufacturer".

            # ── Harmonic loss factor exponents (C57.110) ─────────────────────
            'k_F_HL': 2.0,       # [-] Winding eddy loss exponent: P_EC ~ h^2.           [D] Sec. 4.1.2, Eq. (3)

            # ── Winding eddy-loss frequency model ────────────────────────────
            # "C57.110"    : w(h) = h^2, the standard; exact only for conductors thinner than the skin depth at h
            # "annexC"     : w(h) = h^2 F(xi_h)/F(xi_1) of [D] Annex C, tends to h^1.5 at high order
            # "skin_depth" : w(h) from the 1-D field-diffusion (Dowell 1966) solution for a conductor of
            #                thickness d, tends to h^2 below h_c = (delta_50Hz / d)^2 and to sqrt(h) above it
            'eddy_model': "C57.110",
            'conductor_thickness': 3.0e-3,   # [m] Effective conductor dimension perpendicular to the leakage field
                                             #     (foil thickness / strip radial width). Not on the data sheet; swept.
                                             #
            # Copper resistivity at 75 °C: 1.7241e-8 Ohm m at 20 °C (annealed copper standard)
            # x (234.5 + 75)/(234.5 + 20) = 2.10e-8. 75 °C because P_LL_R is quoted at 75 °C [C].
            # The skin depth it gives (10.3 mm at 50 Hz) matches [D] Annex C (9.4 mm at 60 Hz).
            # NOT READ in this work. Aluminium windings would be ~3.4e-8.
            'conductor_resistivity': 2.1e-8, # [Ohm m]
            'k_F_HL_STR': 0.8,   # [-] Other stray loss exponent: "0.8 or less ... as a conservative estimate". [D] Sec. 4.1.3
            'h_max_used': None,  # [-] Highest order in the summation for the main run; None = full spectrum

            # ── Thermal model (ONAN, steady state) ───────────────────────────
            'x_oil': 0.8,            # [-] Top-oil exponent on the TOTAL-LOSS ratio. [E] Table 4 (small ONAN),
                                     #     [F] Table 4 (n = 0.8, ONAN), [D] Eq. (18)
            'y_winding': 0.8,        # [-] Winding exponent on the LOSS ratio (= C57.91 m, = IEC y/2 on the current ratio)
            'Theta_TO_R': 55,        # [K] Rated top-oil rise above ambient. [F] Annex G example printout
                                     #     ("TOP FLUID RISE OVER AMBIENT = 55 °C", 65 °C-rise unit).
                                     #
            'Theta_g_R': 25,         # [K] Rated hot-spot gradient = hot-spot rise 80 K ([F] text under Eq. (19):
                                     #     "Assume 80 °C for 65 °C average winding rise") minus 55 K.
            # Weight c of the eddy loss in the hot-spot gradient, (P_R + c P_EC F_HL)/(P_R + c P_EC). The gradient
            # follows the LOCAL loss at the hot spot ([D] Eq. (21) uses the hot-spot eddy loss per unit of local I2R).
            # [D] 6.2 defaults: LV winding holds 40/50 = 0.8 of the winding eddy loss (Table 14), its peak density
            # is 4x its average (assumption e):  c = 4 * 0.8 / (LV share of P_R).
            # distribution ([D] 6.2 e: "smaller ratings may show a uniform distribution"). Swept in sensitivity.
            'eddy_hotspot_factor': 5.33,

            # ── Lifetime ─────────────────────────────────────────────────────
            'Theta_ref': 110,      # [°C] Reference hot spot of thermally upgraded paper, 65 °C-rise units. [F] Clause 5, Eq. (2)
                                   #      and a different law (not implemented).
            'L_normal': 180000,    # [h]  Normal insulation life at Theta_ref (20.55 years). [F] Clause 5, quoting
                                   #      IEEE C57.12.00-2010 5.11.3
        }

        # ----------------------------------------#
        # Monte Carlo inputs
        # ----------------------------------------#
        # Draws Theta_H, Theta_ref and L_normal from normal distributions around
        # their nominal values and reports the B10 life (10 % percentile).
        # paper). A real uncertainty study would use the spread of sigma, d and c.
        self.Monte_carlo_inputs = {
            "number_of_samples": 10000,
            "normal_distribution": 0.01,      # [-] Standard deviation as a fraction of each nominal value
            "rng_original": np.random.default_rng(42),   # fixed seed: same result on every run
        }
