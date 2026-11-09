"""
Calculation functions of the transformer assessment.

The chain follows the current entering the low-voltage (LV) winding:

    current spectrum  ->  harmonic loss factors  ->  load loss  ->  top-oil rise
                      ->  hot-spot gradient       ->  hot spot   ->  ageing rate  ->  life

Every formula below carries the source it comes from. The sources were read in
the versions listed here (clause / equation numbers refer to these editions):

    [C57.110]  IEEE Std C57.110-2018, Recommended Practice for Establishing
               Liquid-Immersed and Dry-Type Power and Distribution Transformer
               Capability When Supplying Nonsinusoidal Load Currents.      READ
    [C57.91]   IEEE Std C57.91-2011, Guide for Loading Mineral-Oil-Immersed
               Transformers and Step-Voltage Regulators.                    READ
    [IEC76-7]  IEC 60076-7:2018, Loading guide for mineral-oil-immersed power
               transformers. Only Table 4 (exponents) was read, via the TUM
               VDE NormenBibliothek. The equation forms are taken from C57.91
               and C57.110, which use the same structure.         PARTLY READ
    [Dowell]   P. L. Dowell, "Effects of eddy currents in transformer windings",
               Proc. IEE, vol. 113, no. 8, pp. 1387-1394, Aug. 1966.        READ
    [519]      IEEE Std 519-2022, Standard for Harmonic Control.            READ
    [1547]     IEEE Std 1547-2018, Interconnection of DER.                   READ

"TODO" marks every place where a value or formula is assumed, unverified, or
where I (the author of these comments) am not sure. Search for it.
"""
import numpy as np
import pandas as pd
from pathlib import Path


class Calculation_functions_class:

    # ==================================================================== #
    # Housekeeping
    # ==================================================================== #

    @staticmethod
    def create_simulation_folders(base="Results"):
        """
        Create Results/Simulation_N/{Dataframes,Figures}, with N auto-incremented,
        so that a new run never overwrites an old one.

        Returns
        -------
        sim_dir, dataframes_dir, figures_dir : pathlib.Path
        """
        base_dir = Path(base)
        base_dir.mkdir(exist_ok=True)

        # Find the highest existing Simulation_N so the new folder gets N + 1
        existing = []
        for p in base_dir.iterdir():
            if p.is_dir() and p.name.startswith("Simulation_"):
                try:
                    existing.append(int(p.name.split("_")[1]))
                except (IndexError, ValueError):
                    pass                                   # ignore folders such as "Simulation_old"

        next_n = max(existing) + 1 if existing else 1

        sim_dir = base_dir / f"Simulation_{next_n}"
        dataframes_dir = sim_dir / "Dataframes"
        figures_dir = sim_dir / "Figures"
        for d in (sim_dir, dataframes_dir, figures_dir):
            d.mkdir(exist_ok=True)

        return sim_dir, dataframes_dir, figures_dir

    @staticmethod
    def last_of_column(val, Profile_size):
        """
        Column of NaN with `val` in the last row. Lets a scalar (e.g. the rated
        load loss) be stored in the same per-sample dataframe as the time series.
        """
        col = np.full(Profile_size, np.nan)
        col[-1] = val
        return col

    # ==================================================================== #
    # Input validation
    # ==================================================================== #

    @staticmethod
    def validate_mission_profile(Profile_size, S_RMS, V_LL_RMS, T_amb, harmonic_scale):
        """
        Check that every mission-profile array has length Profile_size and lies
        in a physically meaningful range. Catches the two most common input
        mistakes: arrays of the wrong length, and temperatures in °C instead of K.
        """
        profiles = {"S_RMS": S_RMS, "V_LL_RMS": V_LL_RMS, "T_amb": T_amb, "harmonic_scale": harmonic_scale}

        for name, values in profiles.items():
            values = np.asarray(values)
            if values.ndim != 1 or len(values) != Profile_size:
                raise ValueError(
                    f"Invalid mission-profile length for {name}: expected {Profile_size}, got {values.shape}.")

        if np.any(np.asarray(S_RMS) < 0):
            raise ValueError("S_RMS must be non-negative at every sample.")

        if np.any(np.asarray(V_LL_RMS) <= 0):
            raise ValueError("V_LL_RMS must be positive at every sample.")

        if np.any(np.asarray(harmonic_scale) < 0):
            raise ValueError("harmonic_scale must be non-negative at every sample.")

        # 200-400 K covers -73 °C to +127 °C; a value like 25 means someone passed °C
        T = np.asarray(T_amb)
        if np.any(T < 200) or np.any(T > 400):
            raise ValueError(
                "T_amb lies outside 200–400 K. It is expected in kelvin; "
                "a common cause is passing it in degrees Celsius.")

    # ==================================================================== #
    # Current entering the transformer
    # ==================================================================== #

    @staticmethod
    def build_harmonic_spectrum_pu(h_max, harmonics_pu):
        """
        Build a per-unit spectrum I_h / I_1 over orders 1 ... h_max from a
        dictionary {order: magnitude}. The fundamental is fixed at 1 and every
        order not listed is zero.

        Why per unit: C57.110 Eq. (4)-(6) work with I_h / I_1 (or I_h / I_R), so
        the SHAPE of the spectrum and its MAGNITUDE can be set independently.

        Returns
        -------
        spectrum_pu : np.ndarray, shape (h_max,)   index j holds order j + 1
        """
        spectrum_pu = np.zeros(int(h_max))
        spectrum_pu[0] = 1.0                                     # the fundamental is the reference, 1 pu

        for order, magnitude in harmonics_pu.items():
            order = int(order)
            if order < 2:
                raise ValueError(f"Harmonic orders must be >= 2, got {order}. The fundamental is fixed at 1 pu.")
            if order > h_max:
                raise ValueError(f"Harmonic order {order} exceeds h_max = {h_max}. Raise h_max or drop the order.")
            if magnitude < 0:
                raise ValueError(f"Harmonic magnitude at order {order} must be non-negative.")
            spectrum_pu[order - 1] = magnitude

        return spectrum_pu

    @staticmethod
    def load_harmonic_spectrum_pu_from_file(path, h_max, component=None, second=-1):
        """
        Read a harmonic spectrum from a parquet or CSV file and return it per
        unit of its own fundamental, over orders 1 ... h_max.

        Expected columns: "order" and "I_rms". Optional columns "component" and
        "second" are filtered on when present, which makes the long-format
        df_7_harmonics.parquet of the PEARL LCL code directly usable
        (component = "L2" is the current entering the transformer).

        Orders above h_max are discarded. Only integer orders are kept, i.e.
        interharmonics in the file are ignored.
        TODO: switching sidebands of an asynchronous PWM fall between integer
        orders. IEEE 519-2022 (Sec. 4) and IEEE 1547-2018 (footnote 108) group
        +-5 Hz around each order into that order; a file with 5 Hz resolution
        should be grouped that way before it is read here.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Spectrum file not found: {path}")

        df = pd.read_parquet(path) if path.suffix == ".parquet" else pd.read_csv(path)

        for col in ("order", "I_rms"):
            if col not in df.columns:
                raise ValueError(f"Spectrum file must contain a column '{col}'.")

        if component is not None and "component" in df.columns:
            df = df[df["component"].astype(str) == str(component)]

        if "second" in df.columns:
            sec = df["second"].max() if second == -1 else second     # -1 = take the last second in the file
            df = df[df["second"] == sec]

        if df.empty:
            raise ValueError("No rows left in the spectrum file after filtering on component/second.")

        spectrum = np.zeros(int(h_max))
        for order, I in zip(df["order"].to_numpy(dtype=int), df["I_rms"].to_numpy(dtype=float)):
            if 1 <= order <= h_max:
                spectrum[order - 1] = I

        if spectrum[0] <= 0:
            raise ValueError("The spectrum in the file carries no fundamental, so it cannot be normalised.")

        return spectrum / spectrum[0]

    @staticmethod
    def compute_fundamental_current(S_RMS, V_LL_RMS, phases=3):
        """
        Fundamental RMS current per phase from apparent power and line-to-line
        voltage (textbook power relation, no source needed):

            three-phase : I_1 = S / (sqrt(3) * V_LL)
            single-phase: I_1 = S / V

        This takes all of S as fundamental power. With a few percent distortion
        the error is below 0.1 % and is ignored.
        """
        S_RMS = np.asarray(S_RMS, dtype=float)
        V_LL_RMS = np.asarray(V_LL_RMS, dtype=float)

        if phases == 3:
            return S_RMS / (np.sqrt(3) * V_LL_RMS)
        if phases == 1:
            return S_RMS / V_LL_RMS
        raise ValueError("phases must be 1 or 3.")

    @staticmethod
    def build_harmonic_current_matrix(I_1, spectrum_pu, harmonic_scale):
        """
        Combine the fundamental current of every sample with the per-unit
        spectrum, scaling the non-fundamental part by harmonic_scale:

            I_h(t) = I_1(t) * spectrum_pu[h] * harmonic_scale(t)      (h >= 2)

        Parameters
        ----------
        I_1 : np.ndarray, shape (Profile_size,)            Fundamental RMS current [A]
        spectrum_pu : np.ndarray, shape (h_max,) or (Profile_size, h_max)
        harmonic_scale : np.ndarray, shape (Profile_size,)

        Returns
        -------
        I_RMS_harmonics : np.ndarray, shape (Profile_size, h_max)   RMS current per order [A]
        harmonic_orders : np.ndarray, shape (h_max,)                orders 1 ... h_max
        """
        I_1 = np.asarray(I_1, dtype=float)
        scale = np.asarray(harmonic_scale, dtype=float)

        pu = np.atleast_2d(np.asarray(spectrum_pu, dtype=float))
        if pu.shape[0] == 1:
            pu = np.repeat(pu, I_1.size, axis=0)                    # same spectrum shape for every sample
        if pu.shape[0] != I_1.size:
            raise ValueError("spectrum_pu must have one row, or one row per mission-profile sample.")

        pu = pu.copy()
        pu[:, 0] = 1.0                                               # fundamental never scaled
        pu[:, 1:] *= scale[:, np.newaxis]

        I_RMS_harmonics = I_1[:, np.newaxis] * pu
        harmonic_orders = np.arange(1, pu.shape[1] + 1)

        return I_RMS_harmonics, harmonic_orders

    @staticmethod
    def compute_RMS_per_harmonic(I, f, resolution_per_cycle, Profile_size, h_max):
        """
        Decompose a time-domain current (measured or simulated) into RMS values
        for every order 1 ... h_max, one row per one-second sample. Use this to
        obtain the spectrum when a waveform rather than a spectrum is available.

        Over a one-second window the signal completes f cycles, so the frequency
        resolution is 1 Hz and order h sits exactly in FFT bin h * f.
        RMS of a sinusoid from its one-sided FFT amplitude: |X_k| * 2 / N / sqrt(2).

        Note: IEC 61000-4-7 (Clause 3, via IEEE 519-2022 Sec. 4) prescribes a
        10/12-cycle (~200 ms, 5 Hz) window instead. A 1 s window gives finer
        resolution; harmonic RMS values are the same for a stationary signal.
        """
        N = int(resolution_per_cycle * f)                          # samples in one second

        if h_max > resolution_per_cycle // 2:
            raise ValueError(f"h_max = {h_max} exceeds the Nyquist limit of {resolution_per_cycle // 2}.")

        I_matrix = np.asarray(I, dtype=float).reshape(Profile_size, N)
        fft_vals = np.fft.rfft(I_matrix, axis=1)

        harmonic_orders = np.arange(1, h_max + 1)
        bin_indices = harmonic_orders * int(f)

        I_RMS_harmonics = (2 * np.abs(fft_vals[:, bin_indices]) / N) / np.sqrt(2)

        return I_RMS_harmonics, harmonic_orders

    @staticmethod
    def _truncate(I_RMS_harmonics, harmonic_orders, h_max_used):
        """Keep only orders <= h_max_used (None keeps all). Used to mimic assessments that stop at h = 50 etc."""
        I = np.atleast_2d(np.asarray(I_RMS_harmonics, dtype=float))
        h = np.asarray(harmonic_orders, dtype=float)

        if h.size != I.shape[1]:
            raise ValueError(f"harmonic_orders has length {h.size} but the spectrum has {I.shape[1]} columns.")
        if np.any(h <= 0):
            raise ValueError("Harmonic orders must all be positive; remove any DC (order 0) bin.")

        if h_max_used is not None:
            mask = h <= h_max_used
            if not np.any(mask):
                raise ValueError(f"h_max_used = {h_max_used} excludes every harmonic in the spectrum.")
            I, h = I[:, mask], h[mask]

        return I, h

    @staticmethod
    def calculate_RMS_from_spectrum(I_RMS_harmonics, harmonic_orders, h_max_used=None):
        """
        Total RMS current [A] per sample: I_RMS = sqrt(sum_h I_h^2), C57.110 Eq. (4).
        Components at different frequencies are orthogonal, so their squares add.
        """
        I, _ = Calculation_functions_class._truncate(I_RMS_harmonics, harmonic_orders, h_max_used)
        return np.sqrt(np.sum(I ** 2, axis=1))

    @staticmethod
    def calculate_THD_from_spectrum(I_RMS_harmonics, harmonic_orders, h_max_used=None):
        """
        Total harmonic distortion [%] per sample, over orders 2 ... h_max_used:

            THD = sqrt(sum_{h>=2} I_h^2) / I_1 * 100         (IEEE 519-2022 Clause 3 definition,
                                                              which stops at h = 50 unless stated)
        Samples without fundamental current return NaN.
        """
        I, h = Calculation_functions_class._truncate(I_RMS_harmonics, harmonic_orders, h_max_used)

        I_1 = I[:, h == 1].sum(axis=1)
        I_h = np.sqrt(np.sum(I[:, h > 1] ** 2, axis=1))

        THD = np.full(I.shape[0], np.nan)
        ok = I_1 > 0
        THD[ok] = 100.0 * I_h[ok] / I_1[ok]

        return THD

    # ==================================================================== #
    # Losses (IEEE C57.110)
    # ==================================================================== #

    @staticmethod
    def skin_depth(f_Hz, rho, mu_r=1.0):
        """
        Electromagnetic skin depth of a conductor [m]:

            delta = sqrt( rho / (pi * f * mu_0 * mu_r) )          [C57.110] Annex C, under Eq. (C.1)

        Copper at 75 °C (rho = 2.1e-8 Ohm m) gives 10.3 mm at 50 Hz, 1.46 mm at
        2.5 kHz, 0.73 mm at 10 kHz and 0.46 mm at 25 kHz. C57.110 Annex C quotes
        9.4 mm at 60 Hz, which is the same value scaled by sqrt(50/60).
        """
        mu_0 = 4e-7 * np.pi                                       # vacuum permeability [H/m]
        return np.sqrt(rho / (np.pi * np.asarray(f_Hz, dtype=float) * mu_0 * mu_r))

    @staticmethod
    def calculate_eddy_loss_weighting(harmonic_orders, f, conductor_thickness=None, rho=2.1e-8, model="dowell"):
        """
        Relative winding eddy loss of harmonic h per unit of squared current,
        normalised to the fundamental, w(h):

            P_EC(h) = P_EC_R * (I_h / I_R)^2 * w(h)

        It replaces the h^2 of [C57.110] Eq. (3) in the harmonic loss factor F_HL.
        Three models are available.

        1) conductor_thickness = None  ->  w(h) = h^2
           [C57.110] Eq. (3), Sec. 4.1.2: eddy loss "approximately proportional to
           the square of frequency". Valid while the conductor is thin compared
           with the skin depth; Sec. 4.5 a) and footnote 9 say it becomes
           conservative (overestimates) for large conductors and high harmonics.

        2) model = "dowell"  (1-D field diffusion, the default correction)
           A conductor of thickness d (dimension perpendicular to the leakage
           field) sits in a field H fixed by the winding current. Dowell's
           solution [Dowell] Eq. (8)-(10) gives the extra (proximity) loss through
               D' = Re{ 2 alpha h tanh(alpha h / 2) } = 2 xi G(xi),
               G(xi) = (sinh xi - sin xi) / (cosh xi + cos xi),      xi = d / delta
           (Dowell's Appendix, Eq. (33), defines D = 2 alpha h tanh(alpha h/2);
           with alpha h = (1 + j) xi its real part is the expression above.)
           Loss of harmonic h relative to the fundamental at equal current:
               w(h) = xi_h G(xi_h) / (xi_1 G(xi_1)) = sqrt(h) G(xi_1 sqrt h) / G(xi_1)
           since xi_h = xi_1 sqrt(h) (delta falls as 1/sqrt f).
           Limits: G ~ xi^3/6 for xi << 1  -> w = h^2   (same as C57.110)
                   G -> 1     for xi >> 1  -> w ~ sqrt(h) (conductor screened)
           Crossover order where the two meet: h_c = (delta_1 / d)^2.

           Only the D' (proximity) shape is used here; the M' (skin effect of the
           conductor's own current) term is dropped. That is fine for many layers
           (weight (m^2 - 1)/3 >> 1) and is an assumption otherwise.

        3) model = "annexC"  ([C57.110] Annex C, Eq. (C.1)-(C.5), after Elmoudi et al. 2005)
               F(xi) = (3 / xi) (sinh xi - sin xi) / (cosh xi - cos xi)
               w(h)  = h^2 F(xi_1 sqrt h) / F(xi_1)
           F -> 1 for small xi and -> 3/xi for large xi, so w grows as h^1.5.
           The function reproduces the standard's own Table C.2 to 0.3 % with the
           11 mm strand width of its example (see self_test()).
           Note the MINUS sign in the denominator: this is not the same function
           as Dowell's, and the two disagree strongly at high order.
           UNREAD; reading it would settle which model is right for which case.

        Limitations of 2) and 3): one effective thickness represents both
        windings; the field is uniform and parallel to the conductor face (the
        standard 1-D assumption). At the winding ends the radial field crosses the
        conductor WIDTH, 3-5 times the thickness ([C57.110] Annex B).

        Parameters
        ----------
        harmonic_orders : array          orders h (>= 1)
        f : float                        fundamental frequency [Hz]
        conductor_thickness : float or None
            Effective conductor thickness d [m]. None (or 0) returns h^2.
        rho : float                      conductor resistivity at operating temperature [Ohm m]
        model : "dowell" or "annexC"

        Returns
        -------
        w : np.ndarray, same shape as harmonic_orders
        """
        h = np.asarray(harmonic_orders, dtype=float)

        if conductor_thickness is None or conductor_thickness <= 0:
            return h ** 2                                          # C57.110 Eq. (3)

        xi_1 = conductor_thickness / Calculation_functions_class.skin_depth(f, rho)   # d / delta at 50 Hz

        if model == "annexC":
            def F(xi):
                xi = np.atleast_1d(np.asarray(xi, dtype=float))
                out = 3.0 / np.maximum(xi, 1e-300)             # large-xi limit; exact to machine precision beyond ~20
                small = xi < 1e-2
                # Taylor series: (sinh x - sin x) = x^3/3 + x^7/2520, (cosh x - cos x) = x^2 + x^6/360
                # -> F = 1 - x^4/630. Avoids 0/0 cancellation for very thin conductors.
                out[small] = 1.0 - xi[small] ** 4 / 630.0
                m = (~small) & (xi < 20.0)
                x = xi[m]
                out[m] = 3.0 / x * (np.sinh(x) - np.sin(x)) / (np.cosh(x) - np.cos(x))
                return out

            return h ** 2 * F(xi_1 * np.sqrt(h)) / F(np.array([xi_1]))[0]

        if model != "dowell":
            raise ValueError(f"model must be 'dowell' or 'annexC'. Received {model}.")

        def G(xi):
            xi = np.asarray(xi, dtype=float)
            out = np.ones_like(xi)                                 # G -> 1 beyond xi ~ 20 (sinh/cosh -> 1)
            m = xi < 20.0                                          # also avoids overflow of cosh at large xi
            x = xi[m]
            out[m] = (np.sinh(x) - np.sin(x)) / (np.cosh(x) + np.cos(x))
            return out

        return np.sqrt(h) * G(xi_1 * np.sqrt(h)) / G(np.array([xi_1]))[0]

    @staticmethod
    def calculate_harmonic_loss_factor(I_RMS_harmonics, harmonic_orders, k, h_max_used=None, weights=None):
        """
        Harmonic loss factor for each mission-profile sample:

            F = sum_h (I_h / I_1)^2 h^k  /  sum_h (I_h / I_1)^2          [C57.110] Eq. (12)   (k = 2, F_HL)
              = sum_h I_h^2 h^k          /  sum_h I_h^2                    Eq. (10)-(11); Eq. (14)-(15) for k = 0.8

        The second form, in which the fundamental cancels, is used here. F is
        the energy-weighted mean of h^k: it describes the SHAPE of the spectrum
        only; the magnitude enters separately through (I_RMS / I_R)^2 in the
        load loss. F = 1 for an undistorted current.

            k = 2    winding eddy-current loss  -> F_HL       ([C57.110] Sec. 4.1.2)
            k = 0.8  other stray loss           -> F_HL_STR   ([C57.110] Sec. 4.1.3)

        For comparison: C57.110 itself does NOT go on to temperature. Its
        Eq. (16)-(17) give the maximum current I_max at which the local loss
        density stays at its rated value. The tolerable current of this study is
        the temperature-based analogue (hot spot at its reference).

        A frequency weighting other than h^k (e.g. w(h) from
        calculate_eddy_loss_weighting) may be passed as `weights`, one value per
        column of the spectrum; k is then ignored. This is exactly the
        "corrected harmonic loss factor" structure of [C57.110] Eq. (C.5).

        Samples that carry no current (e.g. a PV plant at night) are assigned
        F = 1, since there is no loss for the factor to scale.

        Returns
        -------
        F : np.ndarray, shape (Profile_size,)
        """
        h_all = np.asarray(harmonic_orders, dtype=float)
        I, h = Calculation_functions_class._truncate(I_RMS_harmonics, harmonic_orders, h_max_used)

        if weights is None:
            wt = h ** k
        else:
            weights = np.asarray(weights, dtype=float)
            if weights.size != h_all.size:
                raise ValueError("weights must have one value per harmonic order.")
            wt = weights if h_max_used is None else weights[h_all <= h_max_used]

        w = I ** 2                                                  # energy of each order
        denominator = w.sum(axis=1)
        numerator = w @ wt

        F = np.ones(I.shape[0])
        ok = denominator > 0
        F[ok] = numerator[ok] / denominator[ok]

        return F

    @staticmethod
    def split_transformer_load_loss(P_LL_R, sigma, eddy_share):
        """
        Split the rated load loss into ohmic, winding eddy and other stray parts,
        following the structure of [C57.110] Eq. (1), (22), (24), (25):

            P_LL_R = P_R + P_EC + P_OSL                         Eq. (1) at rated load
            P_TSL  = sigma * P_LL_R                             total stray loss (Eq. (22) gets it from test data)
            P_R    = (1 - sigma) * P_LL_R                       I^2 R loss, no harmonic correction
            P_EC   = eddy_share * P_TSL                         Eq. (24): eddy_share = 0.50 at 1000 kVA
            P_OSL  = (1 - eddy_share) * P_TSL                   Eq. (25)

        C57.110 gets P_TSL from the test report (load loss minus the I^2R computed
        from measured resistances, Eq. (22)). Planning data quote only P_LL_R, so
        sigma is an ASSUMPTION of this study and is swept (3-15 %).
        would replace it.
        """
        if not 0.0 <= sigma < 1.0:
            raise ValueError(f"sigma must lie in [0, 1). Received {sigma}.")
        if not 0.0 <= eddy_share <= 1.0:
            raise ValueError(f"eddy_share must lie in [0, 1]. Received {eddy_share}.")
        if P_LL_R <= 0.0:
            raise ValueError(f"P_LL_R must be positive. Received {P_LL_R} W.")

        P_TSL = sigma * P_LL_R
        P_R = (1.0 - sigma) * P_LL_R
        P_EC = eddy_share * P_TSL
        P_OSL = (1.0 - eddy_share) * P_TSL

        return P_R, P_EC, P_OSL

    @staticmethod
    def calculate_transformer_load_loss(I_RMS, I_R, P_R, P_EC, P_OSL, F_HL, F_HL_STR):
        """
        Load loss under a distorted current:

            P_LL = (I_RMS / I_R)^2 * [ P_R + P_EC * F_HL + P_OSL * F_HL_STR ]     [C57.110] Eq. (19)

        (Eq. (19) writes P_LL = P + F_HL P_EC + F_HL-STR P_OSL with every term at
        the operating current; factoring out (I_RMS/I_R)^2 is the same thing.)
        The loading carries the magnitude and the factors carry the shape, so
        multiplying them does not double count the harmonic content. Where the
        factors are evaluated over a truncated spectrum, I_RMS must be the RMS
        of the same truncated spectrum (C57.110 consistency).
        """
        I_RMS = np.atleast_1d(np.asarray(I_RMS, dtype=float))
        F_HL = np.atleast_1d(np.asarray(F_HL, dtype=float))
        F_HL_STR = np.atleast_1d(np.asarray(F_HL_STR, dtype=float))

        if I_R <= 0.0:
            raise ValueError(f"I_R must be positive. Received {I_R} A.")
        if np.any(I_RMS < 0.0):
            raise ValueError("I_RMS must be non-negative at every sample.")
        if np.any(F_HL < 1.0 - 1e-12) or np.any(F_HL_STR < 1.0 - 1e-12):
            raise ValueError("A harmonic loss factor below unity is non-physical; "
                             "check that the spectrum includes the fundamental.")

        return (I_RMS / I_R) ** 2 * (P_R + P_EC * F_HL + P_OSL * F_HL_STR)

    # ==================================================================== #
    # Thermal model (steady state)
    # ==================================================================== #

    @staticmethod
    def calculate_transformer_top_oil_rise(P_LL, P_LL_R, P_NL, Theta_TO_R, x_oil):
        """
        Steady-state top-oil rise above ambient [K]:

            Theta_TO = Theta_TO_R * [ (P_LL + P_NL) / (P_LL_R + P_NL) ]^x          [C57.110] Eq. (18)

        This is the ultimate top-oil rise of [C57.91] Eq. (11),
        Theta_TO_R [(K^2 R + 1)/(R + 1)]^n, with the sinusoidal load loss K^2 P_LL_R
        replaced by the harmonic load loss P_LL. Same form in IEC 60076-7.
        Exponent x = n = 0.8 for ONAN: [C57.91] Table 4, [IEC76-7] Table 4.

        Why the total loss: the oil is heated by everything, core (P_NL),
        winding (P_R, P_EC) and tank/clamps (P_OSL).
        """
        P_LL = np.atleast_1d(np.asarray(P_LL, dtype=float))

        if P_LL_R <= 0.0:
            raise ValueError(f"P_LL_R must be positive. Received {P_LL_R} W.")
        if P_NL < 0.0:
            raise ValueError(f"P_NL must be non-negative. Received {P_NL} W.")
        if Theta_TO_R <= 0.0:
            raise ValueError(f"Theta_TO_R must be positive. Received {Theta_TO_R} K.")
        if np.any(P_LL < 0.0):
            raise ValueError("P_LL must be non-negative at every sample.")

        return Theta_TO_R * ((P_LL + P_NL) / (P_LL_R + P_NL)) ** x_oil

    @staticmethod
    def calculate_transformer_hotspot_gradient(I_RMS, I_R, P_R, P_EC, F_HL, Theta_g_R, y_winding,
                                               eddy_hotspot_factor=1.0):
        """
        Steady-state winding hot-spot rise above top oil [K]:

            Theta_g = Theta_g_R * [ (I_RMS/I_R)^2 (P_R + c P_EC F_HL) / (P_R + c P_EC) ]^(y/2)

        Source of the form: [C57.110] Eq. (20)-(21),
            theta_g = theta_g-R [ I^2(pu) (1 + F_HL P_EC-R(pu)) / (1 + P_EC-R(pu)) ]^0.8,
        where P_EC-R(pu) is the eddy loss AT THE HOT SPOT per unit of the local
        I^2R loss. Writing P_EC-R(pu) = c P_EC / P_R gives the expression above.

        THE EXPONENT. IEC 60076-7 writes the gradient as g_r K^y with y = 1.6 for
        ONAN ([IEC76-7] Table 4), K being the CURRENT ratio. C57.91 writes it as
        Delta_Theta_H,R K^(2m) with m = 0.8 ([C57.91] Eq. (17), Table 4), and
        C57.110 Eq. (21) applies 0.8 to the LOSS ratio. All three agree: the loss
        ratio goes as K^2, so the exponent on the loss ratio is y/2 = m = 0.8.
        (An earlier version of this code applied y = 1.6 to the loss ratio, which
        squared the load dependence. self_test() reproduces the C57.110 worked
        example, 12.3 K, to catch this.)

        THE CONCENTRATION FACTOR c (eddy_hotspot_factor). The eddy loss is not
        uniform: [C57.110] Sec. 6.2 assumption e) puts its peak density at the
        hot spot at 4x the winding average, and Table 14 puts 40 of the 50 % of
        stray loss that is in the windings into the LV winding (share 0.8).
        Per unit of the LV winding's own I^2R loss:
            c = 4 * 0.8 / (LV share of P_R)
        TODO: the LV share of P_R is taken as 0.5 (equal I^2R in both windings),
        which gives c = 6.4. This is my assumption, no source. c = 1 is a uniform
        distribution, which C57.110 6.2 e) says is possible for small ratings.

        Only the winding losses enter: the other stray loss (tank, clamps) and
        the core loss heat the oil, not the winding-to-oil gradient, so they
        appear only in the top-oil stage. C57.110 Eq. (21) does the same.
        """
        I_RMS = np.atleast_1d(np.asarray(I_RMS, dtype=float))
        F_HL = np.atleast_1d(np.asarray(F_HL, dtype=float))

        if I_R <= 0.0:
            raise ValueError(f"I_R must be positive. Received {I_R} A.")
        if Theta_g_R <= 0.0:
            raise ValueError(f"Theta_g_R must be positive. Received {Theta_g_R} K.")

        c = eddy_hotspot_factor
        denominator = P_R + c * P_EC                                 # local winding loss at rated sine current
        if denominator <= 0.0:
            raise ValueError("The rated winding loss P_R + c * P_EC must be positive.")

        loading_sq = (I_RMS / I_R) ** 2                               # (I_RMS / I_R)^2 = K^2 for a sinusoid
        numerator = loading_sq * P_R + c * loading_sq * P_EC * F_HL   # local winding loss now

        exponent_on_loss_ratio = y_winding
        return Theta_g_R * (numerator / denominator) ** exponent_on_loss_ratio

    # ==================================================================== #
    # Ageing and life (IEEE C57.91)
    # ==================================================================== #

    @staticmethod
    def calculate_transformer_ageing_acceleration(Theta_H, Theta_ref, B=15000.0):
        """
        Ageing acceleration factor of thermally upgraded paper:

            F_AA = exp( B / (Theta_ref + 273) - B / (Theta_H + 273) ),  B = 15000 K     [C57.91] Eq. (2)

        With Theta_ref = 110 °C this is Eq. (2) exactly (15000/383). It is the
        Arrhenius law of chemical reaction rates: paper depolymerises faster
        when hotter. [C57.91] Table 1 lists F_AA = 0.5957 at 105 °C and 1 at
        110 °C (checked in self_test()). Around 110 °C it doubles roughly every
        6-7 K; the "6 K rule" 2^((Theta-98)/6) of IEC 60076-7 is for
        non-upgraded paper and is NOT used here.

        A RATE relative to the reference hot spot. Theta_H in °C.
        """
        Theta_H = np.atleast_1d(np.asarray(Theta_H, dtype=float))

        if np.any(Theta_H > 300.0) or np.any(Theta_H < -100.0):
            raise ValueError("Theta_H lies outside any plausible range in °C; "
                             "a common cause is passing it in kelvin.")

        with np.errstate(over="ignore"):
            return np.exp(B / (np.asarray(Theta_ref, dtype=float) + 273.0) - B / (Theta_H + 273.0))

    @staticmethod
    def calculate_transformer_loss_of_life(F_AA, seconds_per_sample, L_normal):
        """
        Accumulate the ageing over the mission profile:

            F_EQA = sum(F_AA_i dt_i) / sum(dt_i)            [C57.91] Eq. (3), equivalent ageing factor
            LOL   = sum(F_AA_i dt_i) / L_normal             [C57.91] Eq. (4), loss of life (fraction)
            L_eq  = Profile_duration / LOL                  life if the profile repeats forever

        L_normal = 180 000 h: [C57.91] Clause 5 quotes 5.11.3 of IEEE C57.12.00-2010
        (20.55 years, [C57.91] 8.1.2). Eq. (4) of C57.91 gives the same LOL in percent.

        Returns
        -------
        F_EQA : float       equivalent ageing factor [-]
        LOL : float         fraction of normal life consumed per profile run [-]
        L_eq_years : float  equivalent life [years]
        """
        F_AA = np.atleast_1d(np.asarray(F_AA, dtype=float))

        if L_normal <= 0.0:
            raise ValueError(f"L_normal must be positive. Received {L_normal} h.")
        if np.any(F_AA < 0.0):
            raise ValueError("F_AA must be non-negative at every sample.")

        hours_per_sample = np.broadcast_to(np.asarray(seconds_per_sample, dtype=float) / 3600.0, F_AA.shape)
        duration_h = hours_per_sample.sum()
        if duration_h <= 0.0:
            raise ValueError("The mission profile has zero duration; check seconds_per_sample.")

        ageing_h = np.sum(F_AA * hours_per_sample)                 # "equivalent hours at 110 °C" consumed

        F_EQA = ageing_h / duration_h
        LOL = ageing_h / L_normal
        L_eq_years = np.inf if LOL <= 0.0 else (duration_h / LOL) / (365.0 * 24.0)

        return F_EQA, LOL, L_eq_years

    @staticmethod
    def equivalent_temperature_transformer(L_eq_years, Theta_ref, L_normal, B=15000.0):
        """
        Constant hot spot [°C] that consumes the insulation at the same rate as
        the mission profile, by inverting [C57.91] Eq. (2):

            F_AA_eq    = L_normal / L_eq
            Theta_H_eq = B / ( B / (Theta_ref + 273) - ln F_AA_eq ) - 273

        Lies above the mean hot spot whenever the profile varies, since ageing is
        exponential in temperature (Jensen's inequality). Used as the nominal
        point of the Monte Carlo.
        """
        if L_eq_years <= 0.0:
            raise ValueError(f"L_eq_years must be positive. Received {L_eq_years} years.")
        if L_normal <= 0.0:
            raise ValueError(f"L_normal must be positive. Received {L_normal} h.")

        F_AA_eq = L_normal / (L_eq_years * 365.0 * 24.0)
        return B / (B / (Theta_ref + 273.0) - np.log(F_AA_eq)) - 273.0

    # ==================================================================== #
    # Harmonic sensitivity map
    # ==================================================================== #

    @staticmethod
    def calculate_harmonic_sensitivity_map(trafo_specs, P_R, P_EC, P_OSL, h_orders, I_h_values, I_1, T_amb_C,
                                           eddy_weights=None):
        """
        Transformer response to a SINGLE harmonic of order h and RMS current
        I_h superimposed on a sinusoidal fundamental I_1, evaluated on the grid
        (I_h_values x h_orders) at a constant ambient. This is the heat map.

        For one harmonic on top of the fundamental the C57.110 sums have only
        two terms, so
            F_HL     = (I_1^2 + I_h^2 w(h))  / (I_1^2 + I_h^2)
            F_HL_STR = (I_1^2 + I_h^2 h^0.8) / (I_1^2 + I_h^2)
            I_RMS^2  =  I_1^2 + I_h^2
        with w(h) = h^2 (default) or the corrected weighting passed as
        eddy_weights (one value per entry of h_orders). The losses, top-oil rise,
        hot-spot gradient and hot spot then follow from the same functions as the
        mission-profile run. The equivalent life is that of a transformer held at
        the resulting hot spot indefinitely, L_normal / F_AA.

        The ageing factor is evaluated inline (not through
        calculate_transformer_ageing_acceleration) because much of the grid
        drives the hot spot far beyond any physical value and would trip that
        function's range check; those cells just return a life of ~0 and are
        shown saturated. The steady-state model is an extrapolation there, not a
        prediction.

        Returns
        -------
        Theta_H : np.ndarray, shape (len(I_h_values), len(h_orders))   hot spot [°C]
        Life_years : np.ndarray, same shape                            equivalent life [years]
        """
        h = np.asarray(h_orders, dtype=float)[np.newaxis, :]
        I_h = np.asarray(I_h_values, dtype=float)[:, np.newaxis]

        w1 = I_1 ** 2
        wh = I_h ** 2
        w_eddy = h ** trafo_specs["k_F_HL"] if eddy_weights is None else np.asarray(eddy_weights, dtype=float)[np.newaxis, :]
        # Column h = 1 adds in phase to the fundamental: w(1) = 1 and 1^0.8 = 1 keep both factors at unity
        F_HL = (w1 + wh * w_eddy) / (w1 + wh)
        F_HL_STR = (w1 + wh * h ** trafo_specs["k_F_HL_STR"]) / (w1 + wh)
        I_RMS = np.sqrt(w1 + wh) * np.ones_like(F_HL)

        P_LL = Calculation_functions_class.calculate_transformer_load_loss(I_RMS=I_RMS, I_R=trafo_specs["I_R"], P_R=P_R, P_EC=P_EC, P_OSL=P_OSL, F_HL=F_HL, F_HL_STR=F_HL_STR)
        Theta_TO = Calculation_functions_class.calculate_transformer_top_oil_rise(P_LL=P_LL, P_LL_R=trafo_specs["P_LL_R"], P_NL=trafo_specs["P_NL"], Theta_TO_R=trafo_specs["Theta_TO_R"], x_oil=trafo_specs["x_oil"])
        Theta_g = Calculation_functions_class.calculate_transformer_hotspot_gradient(I_RMS=I_RMS, I_R=trafo_specs["I_R"], P_R=P_R, P_EC=P_EC, F_HL=F_HL, Theta_g_R=trafo_specs["Theta_g_R"], y_winding=trafo_specs["y_winding"], eddy_hotspot_factor=trafo_specs["eddy_hotspot_factor"])
        Theta_H = T_amb_C + Theta_TO + Theta_g                         # hot spot = ambient + oil rise + gradient

        with np.errstate(over="ignore"):
            # [C57.91] Eq. (2), inline for the reason given above
            F_AA = np.exp(15000.0 / (trafo_specs["Theta_ref"] + 273.0) - 15000.0 / (Theta_H + 273.0))
            Life_years = trafo_specs["L_normal"] / (F_AA * 365.0 * 24.0)

        return Theta_H, Life_years

    @staticmethod
    def iso_life_current(I_h_values, Life_years, L_target):
        """
        For every harmonic order (column) of a sensitivity map, the harmonic
        current at which the life falls to L_target. With L_target = L_normal
        this is the TOLERABLE CURRENT I_h*: the hot spot sits exactly at
        Theta_ref and the transformer ages at its normal rate.

        Life falls monotonically with current in each column, so the first grid
        point below the target brackets the crossing; the crossing is then
        interpolated linearly in log(I) - log(L), where both vary smoothly.
        NaN where the target is not reached inside the grid.

        Returns
        -------
        I_iso : np.ndarray, shape (n_orders,)   [A]
        """
        I = np.asarray(I_h_values, dtype=float)
        L = np.asarray(Life_years, dtype=float)
        I_iso = np.full(L.shape[1], np.nan)

        for j in range(L.shape[1]):
            col = L[:, j]
            below = np.where(col <= L_target)[0]
            if below.size == 0 or below[0] == 0:
                continue                                           # never reached, or already exceeded at the first point
            i = below[0]
            x0, x1 = np.log(max(I[i - 1], 1e-12)), np.log(I[i])
            y0, y1 = np.log(col[i - 1]), np.log(max(col[i], 1e-300))
            t = (np.log(L_target) - y0) / (y1 - y0)
            I_iso[j] = np.exp(x0 + t * (x1 - x0))

        return I_iso

    @staticmethod
    def harmonic_budget(I_RMS_harmonics, harmonic_orders, I_iso, h_min=2):
        """
        Share of the transformer's harmonic budget used by a spectrum:

            B = sum_h ( I_h / I_h* )^2,     h >= h_min

        where I_h* is the single-harmonic tolerable current from
        iso_life_current (one value per order). B = 1 brings the hot spot to
        Theta_ref (normal ageing); B < 1 leaves margin.

        Why it works (derivation, my own, no source): every loss term is linear
        in the squared harmonic currents I_h^2. The hot spot depends on two such
        sums, the total loss (top oil) and the local winding loss (gradient),
        through the exponents 0.8. Linearised around the operating point,
            Theta_H ~ Theta_H0 + sum_h I_h^2 * s(h),
        with s(h) the temperature sensitivity per A^2 of order h. The single
        harmonic I_h* is defined by I_h*^2 s(h) = Theta_ref - Theta_H0, so
        Theta_H - Theta_H0 = (Theta_ref - Theta_H0) * B.
        The rule is therefore exact to FIRST ORDER in the temperature increment;
        the curvature of the 0.8 exponents gives a small error, checked
        numerically in paper_figures.py (a few mK for the spectra tested).
        TODO: the error grows when the headroom Theta_ref - Theta_H0 is large
        (part load); check before relying on B at part load.

        Returns
        -------
        B : np.ndarray, shape (Profile_size,)
        """
        I = np.atleast_2d(np.asarray(I_RMS_harmonics, dtype=float))
        h = np.asarray(harmonic_orders, dtype=float)
        I_iso = np.asarray(I_iso, dtype=float)
        m = (h >= h_min) & np.isfinite(I_iso) & (I_iso > 0)
        return np.sum((I[:, m] / I_iso[m]) ** 2, axis=1)

    # ==================================================================== #
    # Self-test against published numbers
    # ==================================================================== #

    @staticmethod
    def self_test(verbose=True):
        """
        Reproduce numbers printed in the standards, so that a wrong formula
        cannot hide. Raises AssertionError if any check fails.

        1. [C57.91] Table 1: F_AA(105 °C) = 0.5957.                                  Eq. (2)
        2. [C57.110] 6.1.2 worked example (liquid-immersed, Tables 10-12):
           top-oil rise 47.2 K * (45 782 / 35 953)^0.8 = 57.3 K                      Eq. (18)
           gradient (55.3 - 47.2) [1.19 (1 + 6.53*0.08)/(1 + 0.08)]^0.8 = 12.3 K     Eq. (21)
           The exponent 0.8 acts on the LOSS ratio (y = 0.8 in the paper, = C57.91 m,
           = IEC 60076-7 y/2 on the current ratio). Exponent 1.6 here would give 18.5 K.
        3. [C57.110] Annex C Table C.2: h^2 F(xi_h)/F(xi_R) = 23.39 (h = 5),
           215.70 (h = 19) for an 11 mm strand, delta_R = 9.4 mm at 60 Hz.
        4. Dowell identity: Re{2 a tanh(a/2)} with a = (1+j) xi equals 2 xi G(xi).
        """
        CF = Calculation_functions_class
        out = {}

        # 1. Arrhenius ageing, C57.91 Table 1
        faa = float(CF.calculate_transformer_ageing_acceleration(105.0, 110.0)[0])
        out["F_AA(105 C) [C57.91 Tab.1: 0.5957]"] = faa
        assert abs(faa - 0.5957) < 5e-4, faa

        # 2a. Top oil, C57.110 Eq. (18) example: P_NL + P_LL = 45 782 W vs rated 35 953 W (both incl. 4072 W no-load)
        TO = float(CF.calculate_transformer_top_oil_rise(P_LL=45782 - 4072, P_LL_R=35953 - 4072, P_NL=4072,
                                                         Theta_TO_R=47.2, x_oil=0.8)[0])
        out["Top oil [C57.110 ex.: 57.3 K]"] = TO
        assert abs(TO - 57.3) < 0.05, TO

        # 2b. Gradient, C57.110 Eq. (21) example: P_EC-R(pu) = 0.08 at the hot spot, F_HL = 6.53, I^2 = 1.19
        #     -> in our notation P_R = 1, c * P_EC = 0.08 (c = 1), (I/I_R)^2 = 1.19, y = 0.8 on the loss ratio
        g = float(CF.calculate_transformer_hotspot_gradient(I_RMS=np.sqrt(1.19), I_R=1.0, P_R=1.0, P_EC=0.08,
                                                            F_HL=6.53, Theta_g_R=55.3 - 47.2, y_winding=0.8,
                                                            eddy_hotspot_factor=1.0)[0])
        out["Gradient [C57.110 ex.: 12.3 K]"] = g
        assert abs(g - 12.3) < 0.06, g

        # 3. Annex C Table C.2; rho chosen so that delta = 9.4 mm at 60 Hz
        rho_60 = (9.4e-3) ** 2 * np.pi * 60 * 4e-7 * np.pi
        w = CF.calculate_eddy_loss_weighting(np.array([5, 19]), 60, 11e-3, rho_60, model="annexC")
        out["Annex C h=5 [Tab. C.2: 23.39]"] = float(w[0])
        out["Annex C h=19 [Tab. C.2: 215.70]"] = float(w[1])
        assert abs(w[0] / 23.39 - 1) < 0.005 and abs(w[1] / 215.70 - 1) < 0.005, w

        # 4. Dowell identity behind G(xi)
        xi = np.array([0.3, 1.0, 3.0])
        a = (1 + 1j) * xi
        lhs = np.real(2 * a * np.tanh(a / 2))
        rhs = 2 * xi * (np.sinh(xi) - np.sin(xi)) / (np.cosh(xi) + np.cos(xi))
        out["Dowell identity max error"] = float(np.max(np.abs(lhs - rhs)))
        assert np.allclose(lhs, rhs), (lhs, rhs)

        if verbose:
            print("\n Self-test against published values")
            for k, v in out.items():
                print(f"  {k:<42s} {v:.4f}")
        return out

    # ==================================================================== #
    # Monte Carlo
    # ==================================================================== #

    @staticmethod
    def normal_distribution_function(value, frac_sigma, n_samples, rng):
        """Draw n_samples ~ N(value, (frac_sigma * |value|)^2)."""
        return rng.normal(value, frac_sigma * abs(value), n_samples)

    # ==================================================================== #
    # Reporting
    # ==================================================================== #

    @staticmethod
    def report_transformer(trafo_specs, P_R, P_EC, P_OSL, F_HL, F_HL_STR, P_LL, P_T,
                           Theta_TO, Theta_g, Theta_H, F_AA, F_EQA, LOL, Lifetime_years,
                           I_RMS=None, THD=None, T_amb=None, B10=None):
        """
        Print a summary of the transformer chain. Per-sample quantities are
        reported as mean (min, max); currents as RMS over the profile. The mean
        of F_AA is for orientation only, F_EQA is the duration-weighted
        equivalent that sets the loss of life.
        """

        def stats(x):
            a = np.atleast_1d(np.asarray(x, dtype=float))
            return np.nanmean(a), np.nanmin(a), np.nanmax(a)

        def line(label, value, unit, spread=None, fmt="{:.4f}"):
            text = "  " + label.ljust(34) + fmt.format(value) + " " + unit
            if spread is not None:
                text += "   (min " + fmt.format(spread[0]) + ", max " + fmt.format(spread[1]) + ")"
            print(text)

        I_R = trafo_specs["I_R"]
        P_LL_R = trafo_specs["P_LL_R"]

        print("\n" + "=" * 78)
        print("  TRANSFORMER AT THE CONNECTION POINT")
        print("=" * 78)

        print("\n Ratings and model settings")
        line("Rated apparent power", trafo_specs["S_r"] / 1e3, "kVA", fmt="{:.1f}")
        line("Rated LV voltage", trafo_specs["V_LV"], "V", fmt="{:.0f}")
        line("Rated LV current  I_R", I_R, "A", fmt="{:.1f}")
        line("Rated load loss   P_LL_R", P_LL_R, "W", fmt="{:.1f}")
        line("No-load loss      P_NL", trafo_specs["P_NL"], "W", fmt="{:.1f}")
        line("Oil exponent      x", trafo_specs["x_oil"], "-", fmt="{:.2f}")
        line("Winding exponent  y (on loss)", trafo_specs["y_winding"], "-", fmt="{:.2f}")
        line("Rated top-oil rise", trafo_specs["Theta_TO_R"], "K", fmt="{:.1f}")
        line("Rated hotspot gradient", trafo_specs["Theta_g_R"], "K", fmt="{:.1f}")
        line("Eddy concentration c", trafo_specs["eddy_hotspot_factor"], "-", fmt="{:.1f}")
        line("Insulation reference", trafo_specs["Theta_ref"], "degC", fmt="{:.0f}")
        line("Normal insulation life", trafo_specs["L_normal"], "h", fmt="{:.0f}")

        print("\n Rated load loss split")
        line("Stray fraction    sigma", trafo_specs["sigma"], "-", fmt="{:.3f}")
        line("Eddy share of stray", trafo_specs["eddy_share"], "-", fmt="{:.3f}")
        line("Ohmic loss        P_R", P_R, "W", fmt="{:.1f}")
        line("Winding eddy loss P_EC", P_EC, "W", fmt="{:.1f}")
        line("Other stray loss  P_OSL", P_OSL, "W", fmt="{:.1f}")

        print("\n Current and harmonic loss factors")
        if I_RMS is not None:
            I_rms = np.sqrt(np.mean(np.asarray(I_RMS, dtype=float) ** 2))
            line("Current entering  I_RMS", I_rms, "A", fmt="{:.2f}")
            line("Per-unit loading", I_rms / I_R, "-", fmt="{:.4f}")
        if THD is not None:
            m, lo, hi = stats(THD)
            line("THD of current", m, "%", (lo, hi), fmt="{:.3f}")
        m, lo, hi = stats(F_HL)
        line("Winding eddy      F_HL", m, "-", (lo, hi))
        m, lo, hi = stats(F_HL_STR)
        line("Other stray   F_HL_STR", m, "-", (lo, hi))

        print("\n Losses")
        m, lo, hi = stats(P_LL)
        line("Load loss         P_LL", m, "W", (lo, hi), fmt="{:.1f}")
        line("Load loss vs rated", m / P_LL_R, "-", fmt="{:.4f}")
        m, lo, hi = stats(P_T)
        line("Total loss        P_T", m, "W", (lo, hi), fmt="{:.1f}")

        print("\n Temperatures")
        if T_amb is not None:
            m, lo, hi = stats(np.asarray(T_amb, dtype=float) - 273.15)
            line("Ambient", m, "degC", (lo, hi), fmt="{:.2f}")
        m, lo, hi = stats(Theta_TO)
        line("Top-oil rise      Theta_TO", m, "K", (lo, hi), fmt="{:.2f}")
        m, lo, hi = stats(Theta_g)
        line("Hotspot gradient  Theta_g", m, "K", (lo, hi), fmt="{:.2f}")
        m, lo, hi = stats(Theta_H)
        line("Hotspot           Theta_H", m, "degC", (lo, hi), fmt="{:.2f}")
        line("Above reference", m - trafo_specs["Theta_ref"], "K", fmt="{:+.2f}")

        print("\n Ageing and life")
        m, lo, hi = stats(F_AA)
        line("Ageing factor     F_AA", m, "-", (lo, hi))
        line("Equivalent ageing F_EQA", F_EQA, "-")
        line("Life consumed     LOL", LOL * 100.0, "%", fmt="{:.6f}")
        line("Equivalent life", Lifetime_years, "years", fmt="{:.2f}")
        if B10 is not None:
            line("B10 lifetime (Monte Carlo)", B10, "years", fmt="{:.2f}")

        print("=" * 78 + "\n")
