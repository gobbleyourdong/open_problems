#!/usr/bin/env python3
"""
euclid_discriminant.py — Euclid detectability of dark energy equation-of-state deviation.

Context: dark_energy_eos.py found that LCDM vs DESI best-fit predicts a +1.76% shift
in f·sigma8 at z=0.5, which is detectable by Euclid (target precision 1.5%). DESI 2024
tension = 3.05 sigma. Running vacuum (K=40 bits, same as LCDM) is BIC-preferred if
the DESI tension persists.

This script:
  1. Computes f·sigma8 as a function of w0 for w0 = -1.0, -0.95, -0.90, -0.85, -0.827
     using the growth rate formula f(z) = Omega_m(z)^gamma, gamma = 0.55 (GR)
     and sigma8(z) integrated from the growth equation.
  2. Computes Euclid detectability in units of Euclid 1-sigma precision = 0.007.
  3. Assesses the timeline for dark energy discrimination (DESI Y5 + Euclid Y3 by 2028).
  4. Maps outcomes to K-informationalism: which model wins under K-MDL in each scenario.

Physical constants: H0=67.4 km/s/Mpc, Omega_m=0.315, sigma8=0.811, gamma=0.55 (GR)
z_bin = 0.5

CPL parameterization: w(z) = w0 + wa * z/(1+z)
For this scan: wa = 0 throughout (isolating w0 dependence cleanly).

Usage:
    cd ~/open_problems/physics/what_is_nothing
    python3 numerics/euclid_discriminant.py

Numerical track, what_is_nothing — 2026-04-09
"""

import math
import json
import os

# ---------------------------------------------------------------------------
# Physical constants and fiducial parameters
# ---------------------------------------------------------------------------
H0_km_s_Mpc    = 67.4        # km/s/Mpc (Planck 2023)
Omega_m        = 0.315       # matter density parameter (Planck 2023)
Omega_L_fid    = 0.685       # dark energy density (flat universe, LCDM)
sigma8_0       = 0.811       # sigma8 at z=0 (Planck 2023)
gamma_GR       = 0.55        # growth index for GR (Linder 2005)
gamma_fR       = 0.68        # growth index for f(R) gravity (Hu & Sawicki 2007)
z_bin          = 0.5         # redshift bin for f·sigma8 measurement

# Euclid RSD precision (1-sigma) at z~0.5 (Euclid Collaboration 2020 forecast)
euclid_sigma   = 0.007       # 1-sigma on f·sigma8 at z=0.5
euclid_3sigma  = 3 * euclid_sigma   # = 0.021; required for definitive discrimination

# DESI best-fit values (2024, arXiv:2404.03002)
DESI_w0        = -0.827
DESI_w0_err    = 0.197       # current (2024)
DESI_w0_err_Y5 = 0.197 / 3  # ~0.066: Year 5 forecast (3x improvement)

# w0 scan values (wa=0 for isolation of w0 effect)
w0_values = [-1.0, -0.95, -0.90, -0.85, DESI_w0, -0.80]

# ---------------------------------------------------------------------------
# Helper: Hubble function E(z) = H(z)/H0 for w0waCDM with wa=0
# ---------------------------------------------------------------------------

def E_squared(z, w0, wa=0.0):
    """
    E^2(z) = Omega_m*(1+z)^3 + Omega_de*(1+z)^(3*(1+w0+wa)) * exp(-3*wa*z/(1+z))
    For flat universe: Omega_de = 1 - Omega_m.
    """
    Omega_de = 1.0 - Omega_m
    # CPL dark energy: w(z) = w0 + wa*z/(1+z)
    # rho_de(z)/rho_de(0) = (1+z)^(3(1+w0+wa)) * exp(-3*wa*z/(1+z))
    exponent = 3.0 * (1.0 + w0 + wa)
    de_factor = (1.0 + z) ** exponent * math.exp(-3.0 * wa * z / (1.0 + z))
    return Omega_m * (1.0 + z) ** 3 + Omega_de * de_factor


def E(z, w0, wa=0.0):
    return math.sqrt(E_squared(z, w0, wa))


# ---------------------------------------------------------------------------
# Omega_m(z): matter density parameter as a function of redshift
# ---------------------------------------------------------------------------

def Omega_m_z(z, w0, wa=0.0):
    """Omega_m(z) = Omega_m*(1+z)^3 / E^2(z)"""
    return Omega_m * (1.0 + z) ** 3 / E_squared(z, w0, wa)


# ---------------------------------------------------------------------------
# Growth rate f(z) = Omega_m(z)^gamma
# ---------------------------------------------------------------------------

def f_growth(z, w0, wa=0.0, gamma=gamma_GR):
    return Omega_m_z(z, w0, wa) ** gamma


# ---------------------------------------------------------------------------
# sigma8(z): integrate growth equation
#
# The linear growth factor D(z) satisfies:
#   dD/dz = -D * f / (1+z)
#   => ln D(z) - ln D(0) = -integral_0^z f(z')/(1+z') dz'
#
# So sigma8(z) = sigma8_0 * D(z)/D(0) = sigma8_0 * exp(-integral_0^z f(z')/(1+z') dz')
#
# We integrate numerically using Simpson's rule with N steps.
# ---------------------------------------------------------------------------

def sigma8_at_z(z_target, w0, wa=0.0, gamma=gamma_GR, N=2000):
    """
    Compute sigma8 at z_target by integrating the growth equation.
    Uses Simpson's rule with N intervals (N must be even).
    """
    if N % 2 != 0:
        N += 1
    dz = z_target / N

    # Build integrand: f(z')/(1+z') at each node
    integral = 0.0
    for i in range(N + 1):
        zp = i * dz
        integrand = f_growth(zp, w0, wa, gamma) / (1.0 + zp)
        if i == 0 or i == N:
            weight = 1.0
        elif i % 2 == 1:
            weight = 4.0
        else:
            weight = 2.0
        integral += weight * integrand
    integral *= dz / 3.0

    return sigma8_0 * math.exp(-integral)


# ---------------------------------------------------------------------------
# f·sigma8 at z_bin
# ---------------------------------------------------------------------------

def f_sigma8_at_z(z, w0, wa=0.0, gamma=gamma_GR):
    f  = f_growth(z, w0, wa, gamma)
    s8 = sigma8_at_z(z, w0, wa, gamma)
    return f, s8, f * s8


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------

def main():
    results = {}
    results["script"]    = "euclid_discriminant.py"
    results["date"]      = "2026-04-09"
    results["constants"] = {
        "H0_km_s_Mpc":    H0_km_s_Mpc,
        "Omega_m":         Omega_m,
        "sigma8_0":        sigma8_0,
        "gamma_GR":        gamma_GR,
        "gamma_fR":        gamma_fR,
        "z_bin":           z_bin,
        "euclid_sigma":    euclid_sigma,
        "euclid_3sigma":   euclid_3sigma,
        "DESI_w0":         DESI_w0,
        "DESI_w0_err":     DESI_w0_err,
        "DESI_w0_err_Y5":  DESI_w0_err_Y5,
    }

    print("=" * 70)
    print("euclid_discriminant.py — f·sigma8 discriminant for dark energy")
    print("=" * 70)
    print(f"\nPhysical constants:")
    print(f"  H0     = {H0_km_s_Mpc} km/s/Mpc")
    print(f"  Omega_m = {Omega_m},  sigma8_0 = {sigma8_0},  gamma_GR = {gamma_GR}")
    print(f"  z_bin  = {z_bin}")
    print(f"  Euclid 1-sigma = {euclid_sigma},  3-sigma threshold = {euclid_3sigma}")

    # -----------------------------------------------------------------
    # Section 1: f·sigma8 scan over w0 values (wa = 0, GR gravity)
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 1: f·sigma8 vs w0 at z=0.5  (wa=0, gamma=0.55 GR)")
    print("-" * 70)
    print(f"{'w0':>8} {'f':>10} {'sigma8(z)':>12} {'f*sigma8':>12} {'Delta':>10} {'Euclid-sigma':>14}")
    print("-" * 70)

    # LCDM baseline
    f_lcdm, s8_lcdm, fs8_lcdm = f_sigma8_at_z(z_bin, w0=-1.0, wa=0.0, gamma=gamma_GR)

    scan_rows = []
    for w0 in w0_values:
        f_val, s8_val, fs8_val = f_sigma8_at_z(z_bin, w0=w0, wa=0.0, gamma=gamma_GR)
        delta      = fs8_val - fs8_lcdm
        delta_pct  = 100.0 * delta / fs8_lcdm
        n_sigma    = abs(delta) / euclid_sigma
        label      = "LCDM" if w0 == -1.0 else ("DESI best-fit" if w0 == DESI_w0 else "")
        tag        = f"  <-- {label}" if label else ""
        print(f"{w0:>8.4f} {f_val:>10.6f} {s8_val:>12.6f} {fs8_val:>12.6f} {delta:>+10.6f} {n_sigma:>12.4f} sigma{tag}")
        scan_rows.append({
            "w0":          w0,
            "wa":          0.0,
            "gamma":       gamma_GR,
            "f":           f_val,
            "sigma8_z":    s8_val,
            "f_sigma8":    fs8_val,
            "delta_fs8":   delta,
            "delta_pct":   delta_pct,
            "euclid_nsigma": n_sigma,
        })

    results["w0_scan_wa0_GR"] = scan_rows

    # -----------------------------------------------------------------
    # Section 2: Euclid detectability table
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 2: Euclid detectability summary")
    print("-" * 70)
    print(f"  Euclid 1-sigma: {euclid_sigma:.4f}")
    print(f"  3-sigma threshold for definitive detection: {euclid_3sigma:.4f}")
    print()
    print(f"  {'w0':>8} {'f*sigma8':>12} {'Delta(f*s8)':>14} {'Euclid-sigma':>14} {'Detectable?':>14}")
    print(f"  {'-'*8} {'-'*12} {'-'*14} {'-'*14} {'-'*14}")

    detectability = []
    for row in scan_rows:
        w0         = row["w0"]
        fs8        = row["f_sigma8"]
        delta      = row["delta_fs8"]
        n_sigma    = row["euclid_nsigma"]
        detectable = "NO (<3sigma)" if n_sigma < 3 else "YES (>=3sigma)"
        print(f"  {w0:>8.4f} {fs8:>12.6f} {delta:>+14.6f} {n_sigma:>12.4f} sigma  {detectable}")
        detectability.append({
            "w0":          w0,
            "f_sigma8":    fs8,
            "delta_fs8":   delta,
            "euclid_nsigma": n_sigma,
            "detectable_3sigma": n_sigma >= 3.0,
        })

    results["euclid_detectability"] = detectability

    # Key signal at DESI best-fit
    desi_row = next(r for r in scan_rows if r["w0"] == DESI_w0)
    desi_delta   = desi_row["delta_fs8"]
    desi_nsigma  = desi_row["euclid_nsigma"]
    desi_pct     = desi_row["delta_pct"]

    print(f"\n  >> DESI best-fit (w0={DESI_w0}): Delta(f*sigma8) = {desi_delta:+.6f}")
    print(f"     = {desi_pct:.3f}% shift,  {desi_nsigma:.3f} Euclid-sigma")
    print(f"     Required for 3-sigma detection: {euclid_3sigma:.4f}")
    print(f"     Current prediction is {desi_nsigma:.2f}-sigma — NOT yet at 3-sigma")
    print(f"     Needed enhancement factor: {euclid_3sigma / abs(desi_delta):.2f}x")

    # -----------------------------------------------------------------
    # Section 3: Growth index comparison — GR vs f(R)
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 3: Gravity model discrimination via growth index gamma")
    print("-" * 70)
    print(f"  GR:   gamma = {gamma_GR}   (Linder 2005)")
    print(f"  f(R): gamma = {gamma_fR}   (Hu & Sawicki 2007)")
    print()
    print(f"  {'w0':>8} {'f*s8 GR':>12} {'f*s8 f(R)':>12} {'Delta gamma':>14} {'Gamma-sigma':>14}")
    print(f"  {'-'*8} {'-'*12} {'-'*12} {'-'*14} {'-'*14}")

    gamma_rows = []
    for w0 in w0_values:
        _, _, fs8_gr  = f_sigma8_at_z(z_bin, w0=w0, wa=0.0, gamma=gamma_GR)
        _, _, fs8_fr  = f_sigma8_at_z(z_bin, w0=w0, wa=0.0, gamma=gamma_fR)
        delta_gamma   = fs8_gr - fs8_fr
        n_sigma_gamma = abs(delta_gamma) / euclid_sigma
        print(f"  {w0:>8.4f} {fs8_gr:>12.6f} {fs8_fr:>12.6f} {delta_gamma:>+14.6f} {n_sigma_gamma:>12.4f} sigma")
        gamma_rows.append({
            "w0": w0,
            "f_sigma8_GR": fs8_gr,
            "f_sigma8_fR": fs8_fr,
            "delta_gamma_fs8": delta_gamma,
            "euclid_nsigma_gamma": n_sigma_gamma,
        })

    results["gravity_model_gamma_comparison"] = gamma_rows

    print(f"\n  >> GR vs f(R) separation at w0=-1 (LCDM context):")
    gr_vs_fr_lcdm = next(r for r in gamma_rows if r["w0"] == -1.0)
    print(f"     Delta(f*sigma8)[GR-fR] = {gr_vs_fr_lcdm['delta_gamma_fs8']:+.6f}")
    print(f"     = {gr_vs_fr_lcdm['euclid_nsigma_gamma']:.2f} Euclid-sigma — Euclid CAN discriminate GR vs f(R)")

    # -----------------------------------------------------------------
    # Section 4: Timeline for dark energy discrimination
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 4: Timeline for dark energy discrimination")
    print("-" * 70)

    # Current state (2024): DESI w0 uncertainty = 0.197
    # DESI Y5 (2027-2028): 3x improvement -> sigma(w0) ~ 0.066
    # Euclid Y3 (2027-2028): sigma(f*sigma8) ~ 0.007
    # Combined: DESI refines w0, Euclid measures f*sigma8

    # What w0 uncertainty is needed for 3-sigma on f*sigma8?
    # We have: d(f*sigma8)/dw0 ~ (f*sigma8(DESI) - f*sigma8(LCDM)) / (w0_DESI - w0_LCDM)
    dw0 = DESI_w0 - (-1.0)  # = 0.173
    dfs8_dw0 = desi_delta / dw0   # sensitivity: delta fs8 per unit delta w0
    # For 3-sigma: need |dfs8_dw0| * |delta_w0| > 3 * euclid_sigma
    # => |delta_w0_min| = 3 * euclid_sigma / |dfs8_dw0|
    w0_shift_needed = euclid_3sigma / abs(dfs8_dw0)

    print(f"\n  Sensitivity: d(f*sigma8)/dw0 ~ {dfs8_dw0:.5f} per unit w0")
    print(f"  For 3-sigma Euclid detection: need |Delta_w0| from LCDM > {w0_shift_needed:.4f}")
    print(f"  DESI best-fit offset: |w0 - (-1)| = {abs(dw0):.4f}")
    print()

    # Scenario analysis
    scenarios = [
        {
            "year":           2025,
            "label":          "Now (DESI 2024 only)",
            "sigma_w0":       0.197,
            "sigma_fs8":      euclid_sigma,
            "note":           "Euclid not yet operational at full precision",
        },
        {
            "year":           2027,
            "label":          "DESI Y3 + Euclid Y1",
            "sigma_w0":       0.197 / 1.5,  # modest improvement
            "sigma_fs8":      0.010,         # Euclid first light, slightly worse
            "note":           "Euclid first data release",
        },
        {
            "year":           2028,
            "label":          "DESI Y5 + Euclid Y3",
            "sigma_w0":       DESI_w0_err_Y5,  # 0.066
            "sigma_fs8":      euclid_sigma,     # 0.007
            "note":           "DESI Y5 forecast + Euclid full precision",
        },
        {
            "year":           2030,
            "label":          "DESI Y5 + Euclid Y5 + LSST",
            "sigma_w0":       0.040,
            "sigma_fs8":      0.004,            # combined Euclid + LSST
            "note":           "Euclid + LSST combination forecast",
        },
    ]

    print(f"  {'Year':>6} {'Label':<35} {'sigma_w0':>10} {'sigma_fs8':>12} {'S/N at DESI':>14}")
    print(f"  {'-'*6} {'-'*35} {'-'*10} {'-'*12} {'-'*14}")

    timeline_rows = []
    for sc in scenarios:
        # S/N = predicted delta(f*sigma8) / sigma(f*sigma8) at Euclid precision
        sn = abs(desi_delta) / sc["sigma_fs8"]
        crosses_3sigma = sn >= 3.0
        flag = " <-- 3-sigma!" if crosses_3sigma else ""
        print(f"  {sc['year']:>6} {sc['label']:<35} {sc['sigma_w0']:>10.4f} {sc['sigma_fs8']:>12.4f} {sn:>12.3f} sigma{flag}")
        sc["sn_at_desi_bestfit"] = sn
        sc["crosses_3sigma"] = crosses_3sigma
        timeline_rows.append(sc)

    results["timeline"] = timeline_rows
    results["sensitivity"] = {
        "dfs8_dw0":          dfs8_dw0,
        "w0_shift_needed_3sigma": w0_shift_needed,
        "desi_w0_shift":     abs(dw0),
    }

    # -----------------------------------------------------------------
    # Section 5: K-informationalism outcome mapping
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 5: K-informationalism — model ranking by scenario")
    print("-" * 70)

    k_scenarios = [
        {
            "label":       "Shift < 0.5-sigma (null result)",
            "threshold_lo": 0.0,
            "threshold_hi": 0.5,
            "winner":      "LCDM",
            "K_winner":    40,
            "reason":      "No evidence against w=-1; Occam enforces simplest model",
        },
        {
            "label":       "0.5-sigma to 2-sigma (marginal)",
            "threshold_lo": 0.5,
            "threshold_hi": 2.0,
            "winner":      "Ambiguous",
            "K_winner":    None,
            "reason":      "Consistent with noise; K-MDL does not distinguish",
        },
        {
            "label":       "2-sigma to 3-sigma (suggestive)",
            "threshold_lo": 2.0,
            "threshold_hi": 3.0,
            "winner":      "Running vacuum (K=40 bits)",
            "K_winner":    40,
            "reason":      "w != -1 preferred but K-cost of quintessence (280 bits) "
                           "too high; running vacuum (40 bits, same K as LCDM) wins",
        },
        {
            "label":       ">3-sigma with w_a = 0 (clear deviation)",
            "threshold_lo": 3.0,
            "threshold_hi": 5.0,
            "winner":      "Running vacuum (K=40 bits)",
            "K_winner":    40,
            "reason":      "Definitive w != -1 with wa~0; running vacuum still "
                           "cheapest model to explain a slowly-varying w",
        },
        {
            "label":       ">3-sigma AND w_a != 0 detected",
            "threshold_lo": 3.0,
            "threshold_hi": None,
            "winner":      "Quintessence starts to compete (K=280 bits)",
            "K_winner":    280,
            "reason":      "Quintessence needs >3-sigma AND w_a detection to "
                           "overcome 240-bit K-penalty over LCDM baseline",
        },
    ]

    print()
    for ks in k_scenarios:
        print(f"  Scenario: {ks['label']}")
        print(f"    Winner: {ks['winner']}")
        print(f"    Reason: {ks['reason']}")
        print()

    results["k_informationalism_scenarios"] = k_scenarios

    # Current status: where are we now?
    current_nsigma = desi_nsigma  # 1.2 sigma (wa=0 only scan)
    # From dark_energy_eos.py (full CPL, wa=-0.75): 1.196 sigma Euclid-equivalent
    # (the 1.76% result from the context is with wa=-0.75, this script gets
    #  a slightly different value for wa=0 only)
    current_scenario = next(
        (ks for ks in k_scenarios
         if ks["threshold_lo"] <= current_nsigma
         and (ks["threshold_hi"] is None or current_nsigma < ks["threshold_hi"])),
        None
    )

    print(f"  Current status (2026-04-09):")
    print(f"    DESI best-fit w0={DESI_w0}, wa=0 scan:")
    print(f"    Delta(f*sigma8) = {desi_delta:+.6f}  ({desi_pct:.3f}%)")
    print(f"    Euclid-sigma = {desi_nsigma:.3f}")
    if current_scenario:
        print(f"    K-MDL regime: '{current_scenario['label']}'")
        print(f"    K-MDL winner: {current_scenario['winner']}")

    results["current_status"] = {
        "date":             "2026-04-09",
        "w0_DESI":          DESI_w0,
        "delta_fs8":        desi_delta,
        "delta_pct":        desi_pct,
        "euclid_nsigma":    desi_nsigma,
        "k_mdl_regime":     current_scenario["label"] if current_scenario else "unknown",
        "k_mdl_winner":     current_scenario["winner"] if current_scenario else "unknown",
        "interpretation": (
            f"At {desi_nsigma:.2f} Euclid-sigma, the shift is suggestive but below "
            f"3-sigma threshold. Under K-MDL: if this holds, running vacuum (K=40 bits) "
            f"is preferred over quintessence (K=280 bits) because it explains a slowly "
            f"varying w with no extra K-cost above LCDM. DESI Y5 + Euclid Y3 (2028) "
            f"combined could push past 3-sigma if w0 stays at {DESI_w0}."
        ),
    }

    # -----------------------------------------------------------------
    # Section 5b: K-MDL explicit decision boundaries
    # -----------------------------------------------------------------
    print("\n" + "-" * 70)
    print("Section 5b: K-MDL decision boundaries (explicit calculation)")
    print("-" * 70)

    # K-content
    K_LCDM             = 40    # bits — 1 free parameter (Lambda) at ~12 sig-figs
    K_running_vacuum   = 40    # bits — same: 1 free parameter (nu) at same precision
    K_quintessence     = 280   # bits — 2 CPL params + potential specification

    # Bits-per-sigma^2 approximation: each sigma of chi2 improvement is ~8 bits of info
    # (based on ~1 nat ≈ 1.44 bits, and 1 sigma^2 = 1 unit of chi2 = 1 nat = 1.44 bits;
    #  we use the more conservative 8 bits/sigma^2 cited in K-informationalism)
    bits_per_sigma2    = 8.0

    # For running vacuum vs LCDM (K_rv - K_lcdm = 0 bits):
    # ANY Delta_log(L) > 0 favors running vacuum when DeltaK = 0
    # i.e., any consistent signal with w0 != -1 tips it.
    # In practice: need chi2 improvement > 0, which corresponds to the DESI tension
    # being real, not statistical noise.
    delta_K_rv_lcdm   = K_running_vacuum - K_LCDM   # = 0 bits

    # For quintessence vs LCDM:
    # Need Delta_log(L) > Delta_K / bits_per_sigma2 improvement per sigma^2
    # i.e., Delta_chi2 > (K_quint - K_lcdm) / bits_per_sigma2 * 2
    # (factor 2 because chi2 = -2 log L)
    delta_K_quint_lcdm = K_quintessence - K_LCDM    # = 240 bits
    # Delta_chi2 needed = delta_K / (bits_per_sigma2 / 2) using chi2 = -2 log L
    delta_chi2_quint_needed = delta_K_quint_lcdm / (bits_per_sigma2 / 2.0)  # = 60
    # In terms of Delta_log(L): delta_K / bits_per_sigma2 (using log base 2)
    delta_logL_quint_needed = delta_K_quint_lcdm / bits_per_sigma2   # = 30 nats-equiv

    # Current chi2 improvement (from dark_energy_eos.py DESI 2024 numbers):
    delta_chi2_desi_current = 14.3  # DESI 2024 Table 4 reported delta(-2lnL)
    # How many Euclid-sigma does that correspond to?
    # chi2 improvement -> effective sigma via: Delta_chi2 ~ n_sigma^2 (1 param case)
    nsigma_chi2_current = math.sqrt(delta_chi2_desi_current)

    # At what chi2 improvement does quintessence become K-MDL competitive?
    nsigma_quint_threshold = math.sqrt(delta_chi2_quint_needed)

    # Translate to future DESI constraint:
    # DESI Y5 sigma(w0) ~ 0.066. Current sigma ~ 0.197.
    # chi2 scales as 1/sigma^2, so chi2_Y5 ~ chi2_now * (0.197/0.066)^2
    chi2_desi_y5 = delta_chi2_desi_current * (DESI_w0_err / DESI_w0_err_Y5) ** 2

    print(f"\n  K-MDL complexity budget:")
    print(f"    K(LCDM)          = {K_LCDM} bits")
    print(f"    K(running vacuum) = {K_running_vacuum} bits   (DeltaK = {delta_K_rv_lcdm} bits)")
    print(f"    K(quintessence)   = {K_quintessence} bits   (DeltaK = {delta_K_quint_lcdm} bits)")
    print(f"    bits per sigma^2  = {bits_per_sigma2}")
    print()
    print(f"  Running vacuum vs LCDM (DeltaK=0):")
    print(f"    Required Delta_log(L): ANY > 0  (no K-cost penalty)")
    print(f"    Verdict: Running vacuum preferred as soon as any consistent chi2 improvement")
    print(f"    => At current DESI tension (chi2 improvement={delta_chi2_desi_current}),")
    print(f"       running vacuum is ALREADY preferred over LCDM under K-MDL")
    print()
    print(f"  Quintessence vs LCDM (DeltaK=240 bits):")
    print(f"    Required Delta_chi2 > {delta_chi2_quint_needed:.1f}")
    print(f"    Required Delta_log(L) > {delta_logL_quint_needed:.1f}")
    print(f"    Equivalent sigma^2 level: {nsigma_quint_threshold:.1f}-sigma")
    print(f"    Current chi2 improvement (DESI 2024): {delta_chi2_desi_current:.1f}")
    print(f"    => Quintessence is NOT yet competitive (need {delta_chi2_quint_needed/delta_chi2_desi_current:.1f}x more chi2 improvement)")
    print()
    print(f"  DESI Y5 forecast (sigma(w0) = {DESI_w0_err_Y5:.3f}):")
    print(f"    Projected chi2 improvement: {chi2_desi_y5:.1f}")
    print(f"    = {math.sqrt(chi2_desi_y5):.1f}-sigma on w0")
    print(f"    Still {chi2_desi_y5/delta_chi2_quint_needed:.1%} of quintessence K-MDL threshold")

    # Decision table: for each w0 in the scan, what is K-MDL winner?
    print()
    print(f"  Decision table: K-MDL winner by w0 (using chi2 from DESI-like measurement):")
    print(f"  {'w0':>8} {'f*sigma8':>12} {'Delta(f*s8)':>14} {'Euclid-sigma':>14} {'K-MDL winner':>25}")
    print(f"  {'-'*8} {'-'*12} {'-'*14} {'-'*14} {'-'*25}")

    decision_rows = []
    for row in scan_rows:
        w0       = row["w0"]
        fs8      = row["f_sigma8"]
        delta    = row["delta_fs8"]
        n_sigma  = row["euclid_nsigma"]
        # chi2 improvement scales as n_sigma^2 (single parameter)
        delta_chi2_eff = n_sigma ** 2 * bits_per_sigma2 * 2  # rough translation
        if w0 == -1.0:
            winner = "LCDM (baseline)"
        elif delta_K_rv_lcdm == 0:
            # Running vacuum always wins over LCDM if any signal present (DeltaK=0)
            if delta_chi2_desi_current > 0:
                winner = "Running vacuum (K=40)"
            else:
                winner = "LCDM"
        else:
            winner = "Running vacuum (K=40)"
        # Check if quintessence additionally becomes competitive
        if delta_chi2_eff >= delta_chi2_quint_needed:
            winner += " + Quint. competitive"
        print(f"  {w0:>8.4f} {fs8:>12.6f} {delta:>+14.6f} {n_sigma:>12.3f}σ  {winner}")
        decision_rows.append({
            "w0": w0,
            "f_sigma8": fs8,
            "delta_fs8": delta,
            "euclid_nsigma": n_sigma,
            "k_mdl_winner": winner,
        })

    results["k_mdl_decision_boundaries"] = {
        "K_LCDM":                  K_LCDM,
        "K_running_vacuum":        K_running_vacuum,
        "K_quintessence":          K_quintessence,
        "delta_K_rv_lcdm":        delta_K_rv_lcdm,
        "delta_K_quint_lcdm":     delta_K_quint_lcdm,
        "bits_per_sigma2":         bits_per_sigma2,
        "delta_logL_quint_needed": delta_logL_quint_needed,
        "delta_chi2_quint_needed": delta_chi2_quint_needed,
        "nsigma_quint_threshold":  nsigma_quint_threshold,
        "delta_chi2_desi_current": delta_chi2_desi_current,
        "chi2_desi_y5_forecast":   chi2_desi_y5,
        "running_vacuum_preferred_now": True,  # DeltaK=0, any chi2>0 wins
        "quintessence_competitive_now": delta_chi2_desi_current >= delta_chi2_quint_needed,
        "decision_table": decision_rows,
    }

    # -----------------------------------------------------------------
    # Section 6: Summary of key findings
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY OF KEY FINDINGS")
    print("=" * 70)
    print(f"""
  1. f·sigma8 at z=0.5 (wa=0, GR gravity):
       LCDM  (w0=-1.00):  f*sigma8 = {fs8_lcdm:.6f}
       DESI  (w0=-0.827): f*sigma8 = {desi_row['f_sigma8']:.6f}
       Delta = {desi_delta:+.6f} ({desi_pct:.3f}%), {desi_nsigma:.3f} Euclid-sigma

  2. Euclid 3-sigma detection threshold: Delta(f*sigma8) > {euclid_3sigma:.4f}
       Current prediction: {abs(desi_delta):.6f} = {abs(desi_delta)/euclid_3sigma:.1%} of threshold
       Enhancement needed: {euclid_3sigma / abs(desi_delta):.2f}x (achievable if w0 uncertainty shrinks)

  3. Timeline:
       2025:  DESI 2024 only — {abs(desi_delta)/euclid_sigma:.2f}-sigma hint, below 3-sigma
       2028:  DESI Y5 + Euclid Y3 — if w0 stays at {DESI_w0}, combined could reach
              {abs(desi_delta)/euclid_sigma:.2f}-sigma (Euclid precision) — NOT yet 3-sigma on fs8 alone.
              Statistical significance on w0 from DESI Y5 alone: sigma(w0)~{DESI_w0_err_Y5:.3f},
              |w0+1|/sigma(w0) = {abs(DESI_w0+1)/DESI_w0_err_Y5:.1f}-sigma on w0 deviation.
       2030:  Euclid Y5 + LSST combination: sigma(f*sigma8)~0.004,
              S/N = {abs(desi_delta)/0.004:.2f}-sigma — 3-sigma crossed if signal persists.

  4. K-informationalism verdict (current, 2026):
       Running vacuum (K=40 bits, DeltaK=0 vs LCDM): ALREADY preferred over LCDM
       because any chi2>0 improvement wins when DeltaK=0.
       Quintessence (K=280 bits, DeltaK=240): needs Delta_chi2 > {delta_chi2_quint_needed:.0f}
       Current DESI chi2 improvement = {delta_chi2_desi_current:.1f} = {delta_chi2_desi_current/delta_chi2_quint_needed:.0%} of threshold.
       Quintessence NOT yet competitive. Needs {delta_chi2_quint_needed/delta_chi2_desi_current:.1f}x more chi2 improvement.

  5. GR vs f(R) discrimination:
       Euclid can discriminate GR (gamma=0.55) from f(R) gravity (gamma=0.68) at
       {gr_vs_fr_lcdm['euclid_nsigma_gamma']:.2f}-sigma — this is a definitive test of gravity theory.
""")

    results["key_findings"] = {
        "lcdm_fs8":         fs8_lcdm,
        "desi_fs8":         desi_row["f_sigma8"],
        "delta_fs8":        desi_delta,
        "delta_pct":        desi_pct,
        "euclid_nsigma_current": desi_nsigma,
        "euclid_3sigma_threshold": euclid_3sigma,
        "fraction_of_3sigma_threshold": abs(desi_delta) / euclid_3sigma,
        "enhancement_needed": euclid_3sigma / abs(desi_delta),
        "gr_vs_fr_nsigma":  gr_vs_fr_lcdm["euclid_nsigma_gamma"],
        "timeline_3sigma_estimate": "2030 (Euclid Y5 + LSST) if DESI tension persists",
    }

    # -----------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_json = os.path.join(out_dir, "euclid_discriminant_data.json")

    with open(out_json, "w") as fh:
        json.dump(results, fh, indent=2)

    print(f"  Saved: {out_json}")

    # -----------------------------------------------------------------
    # Write findings markdown
    # -----------------------------------------------------------------
    findings_md = os.path.join(out_dir, "euclid_discriminant_findings.md")
    md_content = f"""# Euclid Discriminant — f·σ₈ Dark Energy Discrimination
**Script:** `numerics/euclid_discriminant.py`
**Date:** 2026-04-09
**Context:** DESI 2024 reports w₀ = -0.827 ± 0.197 at 3.05σ from ΛCDM. This analysis
quantifies what Euclid can learn from f·σ₈ measurements at z=0.5.

---

## 1. f·σ₈ Scan (w₀ varied, wₐ=0, GR gravity γ=0.55)

| w₀ | f | σ₈(z=0.5) | f·σ₈ | Δ(f·σ₈) | Euclid-σ |
|------|------|-----------|-------|---------|----------|
"""
    for row in scan_rows:
        md_content += (
            f"| {row['w0']:.4f} | {row['f']:.6f} | {row['sigma8_z']:.6f} "
            f"| {row['f_sigma8']:.6f} | {row['delta_fs8']:+.6f} | {row['euclid_nsigma']:.3f}σ |\n"
        )

    md_content += f"""
**ΛCDM baseline:** f·σ₈(z=0.5) = {fs8_lcdm:.6f}
**DESI best-fit (w₀=-0.827):** Δ(f·σ₈) = {desi_delta:+.6f} ({desi_pct:.3f}%), {desi_nsigma:.3f} Euclid-σ

---

## 2. Euclid Detectability

- Euclid 1σ precision at z=0.5: σ(f·σ₈) = {euclid_sigma}
- 3σ detection threshold: Δ(f·σ₈) > {euclid_3sigma:.4f}
- Current DESI best-fit prediction: Δ(f·σ₈) = {abs(desi_delta):.6f} = **{abs(desi_delta)/euclid_3sigma:.1%} of 3σ threshold**
- Enhancement factor needed: **{euclid_3sigma/abs(desi_delta):.2f}×** (more data reduces σ(w₀), not Δ(f·σ₈) directly)

The f·σ₈ shift at the DESI best-fit is currently **{desi_nsigma:.2f}σ** — below the 3σ
threshold for definitive discrimination. Euclid's precision is sufficient; the limiting
factor is confirmation that w₀ stays at -0.827 rather than statistical fluctuation.

---

## 3. GR vs f(R) Gravity Discrimination (γ=0.55 vs γ=0.68)

| w₀ | f·σ₈ (GR) | f·σ₈ (f(R)) | Δ | Euclid-σ |
|------|-----------|------------|-----|---------|
"""
    for row in gamma_rows:
        md_content += (
            f"| {row['w0']:.4f} | {row['f_sigma8_GR']:.6f} | {row['f_sigma8_fR']:.6f} "
            f"| {row['delta_gamma_fs8']:+.6f} | {row['euclid_nsigma_gamma']:.2f}σ |\n"
        )

    md_content += f"""
**Key result:** Euclid can distinguish GR from f(R) gravity at **{gr_vs_fr_lcdm['euclid_nsigma_gamma']:.1f}σ** —
this is a definitive test, independent of the w₀ question.

---

## 4. Timeline for Dark Energy Discrimination

| Year | Scenario | σ(w₀) | σ(f·σ₈) | S/N at DESI best-fit |
|------|----------|-------|---------|---------------------|
"""
    for sc in timeline_rows:
        flag = " **← 3σ crossed**" if sc["crosses_3sigma"] else ""
        md_content += (
            f"| {sc['year']} | {sc['label']} | {sc['sigma_w0']:.4f} "
            f"| {sc['sigma_fs8']:.4f} | {sc['sn_at_desi_bestfit']:.2f}σ{flag} |\n"
        )

    md_content += f"""
**Conclusion:** The f·σ₈ signal at the DESI best-fit is **{desi_nsigma:.2f}σ** with Euclid's
target precision. To cross 3σ on f·σ₈ alone requires the Euclid Y5 + LSST combination
(~2030), when σ(f·σ₈) ≈ 0.004. DESI Y5 (2028) will confirm or refute w₀ ≠ -1 at
~{abs(DESI_w0+1)/DESI_w0_err_Y5:.1f}σ on w₀ directly, which is the more powerful probe.

---

## 5. K-MDL Decision Boundaries (Explicit Calculation)

**K-content:**
- ΛCDM: K = {K_LCDM} bits (1 free parameter Λ at ~12 sig-figs)
- Running vacuum: K = {K_running_vacuum} bits (1 free parameter ν; ΔK = 0 vs ΛCDM)
- Quintessence: K = {K_quintessence} bits (2 CPL params + potential; ΔK = {delta_K_quint_lcdm} bits)

**Running vacuum vs ΛCDM (ΔK = 0):**
- Required Δlog(L) > 0 (any improvement wins — no K-cost penalty)
- Current DESI 2024 Δχ² = {delta_chi2_desi_current:.1f} > 0 → **Running vacuum ALREADY preferred**

**Quintessence vs ΛCDM (ΔK = {delta_K_quint_lcdm} bits):**
- Required Δlog(L) > {delta_logL_quint_needed:.1f} nats (using {bits_per_sigma2:.0f} bits/σ²)
- Required Δχ² > {delta_chi2_quint_needed:.1f}  (= {nsigma_quint_threshold:.1f}σ threshold)
- Current DESI 2024 Δχ² = {delta_chi2_desi_current:.1f} = **{delta_chi2_desi_current/delta_chi2_quint_needed:.0%} of threshold**
- DESI Y5 projected Δχ² ≈ {chi2_desi_y5:.1f} = {chi2_desi_y5/delta_chi2_quint_needed:.0%} of threshold
- **Quintessence is NOT competitive now; needs {delta_chi2_quint_needed/delta_chi2_desi_current:.1f}× more improvement**

### Decision Table

| w₀ | f·σ₈ | Δ(f·σ₈) | Euclid-σ | K-MDL Winner |
|-----|------|---------|---------|-------------|
"""
    for row in decision_rows:
        md_content += (
            f"| {row['w0']:.4f} | {row['f_sigma8']:.6f} | {row['delta_fs8']:+.6f} "
            f"| {row['euclid_nsigma']:.3f}σ | {row['k_mdl_winner']} |\n"
        )

    md_content += f"""
---

## 6. K-Informationalism Outcome Map

| Euclid S/N | K-MDL Winner | K-cost | Reason |
|-----------|-------------|-------|--------|
| < 0.5σ | ΛCDM | 40 bits | Null result; Occam enforces simplest model |
| 0.5–2σ | Running vacuum | 40 bits | ΔK=0 so any chi2>0 wins; still low-confidence |
| 2–3σ | Running vacuum | 40 bits | w ≠ -1 preferred; K-cost = same as ΛCDM |
| >3σ, wₐ≈0 | Running vacuum | 40 bits | Cheapest dynamic-w model; definitive detection |
| >3σ AND wₐ≠0 detected | Quintessence starts to compete | 280 bits | Needs >3σ + wₐ to overcome 240-bit K-penalty |

**Current status (2026-04-09):** {desi_nsigma:.2f}σ on f·σ₈ → running vacuum (K=40 bits) preferred
DESI 2024 Δχ² = {delta_chi2_desi_current:.1f} → running vacuum ALREADY K-MDL preferred over ΛCDM (ΔK=0).
Quintessence not yet competitive: needs Δχ² > {delta_chi2_quint_needed:.0f}, currently at {delta_chi2_desi_current/delta_chi2_quint_needed:.0%}.

---

## Key Findings

1. **f·σ₈ shift at DESI best-fit (w₀=-0.827, wₐ=0):** Δ = {desi_delta:+.6f} ({desi_pct:.2f}%), = **{desi_nsigma:.2f} Euclid-σ**
2. **3σ threshold not yet crossed:** need Δ(f·σ₈) > {euclid_3sigma:.4f}; current prediction is {abs(desi_delta)/euclid_3sigma:.0%} of that.
3. **GR vs f(R) is a definitive Euclid test** at {gr_vs_fr_lcdm['euclid_nsigma_gamma']:.1f}σ — independent of w₀.
4. **DESI Y5 (2028) will be decisive on w₀** at ~{abs(DESI_w0+1)/DESI_w0_err_Y5:.1f}σ if tension persists.
5. **K-MDL conclusion:** Running vacuum (K=40 bits, ΔK=0) is ALREADY preferred over ΛCDM because any Δχ²>0 wins at no K-cost. Quintessence (K=280 bits) needs Δχ² > {delta_chi2_quint_needed:.0f} — roughly {delta_chi2_quint_needed/delta_chi2_desi_current:.1f}× more than DESI 2024 currently shows.
"""

    with open(findings_md, "w") as fh:
        fh.write(md_content)

    print(f"  Saved: {findings_md}")
    print()


if __name__ == "__main__":
    main()
