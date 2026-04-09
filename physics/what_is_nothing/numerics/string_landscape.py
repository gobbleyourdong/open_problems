#!/usr/bin/env python3
"""
string_landscape.py — String landscape statistics for the cosmological constant.

Models the Bousso-Polchinski landscape of ~10^500 flux vacua and asks:
given that N_vacua random vacua exist, how many land inside the anthropic
window?  Three prior distributions on Λ are considered.

References:
  - Bousso & Polchinski (2000) JHEP 06, 006  — flux vacua estimate N ~ 10^500
  - Susskind (2003) hep-th/0302219           — landscape + anthropic selection
  - Weinberg (1987) Phys. Rev. Lett. 59, 2607 — original anthropic window
  - Douglas (2003) hep-ph/0401004            — landscape statistics review
"""

import math
import json
import os

# ─────────────────────────────────────────────────────────────────────────────
# Physical constants (SI)
# ─────────────────────────────────────────────────────────────────────────────
hbar  = 1.054571817e-34   # J·s
c     = 2.998e8           # m/s
G     = 6.674e-11         # m³ kg⁻¹ s⁻²

# Key densities
rho_Lam_obs = 5.924e-27   # J/m³  observed dark energy density (Planck 2018)
rho_Planck  = 4.634e113   # J/m³  Planck energy density ħc/l_P⁴

# Anthropic window upper bound: Λ ≤ 30 × Λ_obs (from anthropic_window.py;
# the galaxy-formation threshold is ~12–98 × Λ_obs; we use 30 as a round
# representative value midway in the range, matching the task specification)
window_factor = 30.0
rho_Lam_max   = window_factor * rho_Lam_obs   # 1.777×10⁻²⁵ J/m³

# ─────────────────────────────────────────────────────────────────────────────
# Landscape parameters
# ─────────────────────────────────────────────────────────────────────────────
# Bousso-Polchinski: N_fluxes independent flux quanta, each taking O(10) values
# → N_vacua ~ 10^(N_fluxes).  Standard estimate: N_fluxes ≈ 500.
N_fluxes           = 500
values_per_flux    = 10          # order-of-magnitude estimate
log10_N_vacua      = N_fluxes   # log10(10^500) = 500
N_vacua_log10      = 500         # explicit for clarity

# ─────────────────────────────────────────────────────────────────────────────
# Compute prior probabilities P(Λ ≤ Λ_max) for each distribution
# Working in log10 throughout to handle the extreme ranges safely.
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("STRING LANDSCAPE STATISTICS — COSMOLOGICAL CONSTANT")
print("=" * 70)

print(f"\n── Key scales ──")
print(f"  ρ_Λ observed       = {rho_Lam_obs:.4e} J/m³")
print(f"  ρ_Λ max (window)   = {rho_Lam_max:.4e} J/m³  (= {window_factor:.0f} × ρ_Λ_obs)")
print(f"  ρ_Planck           = {rho_Planck:.4e} J/m³")
print(f"  N_vacua            = 10^{N_vacua_log10}")

# ── Ratio of window to Planck scale ─────────────────────────────────────────
log10_window_over_Planck = math.log10(rho_Lam_max) - math.log10(rho_Planck)
# log10(1.777e-25 / 4.634e113) = log10(1.777e-25) - log10(4.634e113)
#   = (-25 + log10(1.777)) - (113 + log10(4.634))
#   ≈ -24.75 - 113.67 ≈ -138.42   → fraction ~3.8×10⁻¹³⁹

print(f"\n  log10(Λ_max / ρ_Planck) = {log10_window_over_Planck:.2f}")
print(f"  → Window fraction of Planck range ≈ 10^{log10_window_over_Planck:.1f} ≈ {10**log10_window_over_Planck:.2e}")

# ─────────────────────────────────────────────────────────────────────────────
# Distribution A — Log-uniform (Jeffreys) prior on [ε, ρ_Planck]
#
# P(Λ ≤ Λ_max) = log(Λ_max / ε) / log(ρ_Planck / ε)
#
# For ε → 0⁺ both logarithms diverge but their ratio approaches:
#   log(Λ_max) / log(ρ_Planck)   (using any fixed ε ≪ Λ_max)
#
# In practice we set ε = 1 J/m³ (a reference density far below Λ_max
# but representable as a concrete number).  The ratio converges because
# log(Λ_max/ε) / log(ρ_Planck/ε) = (log Λ_max - log ε)/(log ρ_Planck - log ε)
# → log Λ_max / log ρ_Planck   when log ε is negligible.
#
# We do the calculation exactly in natural log:
#   log(Λ_max)   = log(1.777e-25) ≈ -57.07    (base e)
#   log(ρ_Planck)= log(4.634e113) ≈ 261.7
# Note: Λ_max < 1 in SI so ln(Λ_max) < 0; the log-uniform distribution
# covers both sub-unity and super-unity values.  The proper interpretation
# is that the distribution is flat in ln Λ over [ε, ρ_Planck], so:
#   P(Λ ≤ Λ_max) = [ln(Λ_max) - ln(ε)] / [ln(ρ_Planck) - ln(ε)]
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("DISTRIBUTION A — LOG-UNIFORM (JEFFREYS) PRIOR")
print("=" * 70)

# Use ε = 1e-200 J/m³ (far below Λ_obs, ensures ln(ε) dominates neither side)
epsilon = 1e-200   # J/m³ — IR cutoff, chosen well below Λ_obs

ln_Lam_max   = math.log(rho_Lam_max)   # natural log; negative since Λ_max < 1
ln_rho_P     = math.log(rho_Planck)
ln_eps       = math.log(epsilon)

P_log_uniform = (ln_Lam_max - ln_eps) / (ln_rho_P - ln_eps)

# Convert to log10 for the expected-vacuum count
log10_P_log  = math.log10(P_log_uniform)
log10_N_exp_log = N_vacua_log10 + log10_P_log   # log10(N_vacua × P)

print(f"\n  ε (IR cutoff)         = {epsilon:.0e} J/m³")
print(f"  ln(Λ_max)             = {ln_Lam_max:.3f}")
print(f"  ln(ρ_Planck)          = {ln_rho_P:.3f}")
print(f"  ln(ε)                 = {ln_eps:.3f}")
print(f"  P(Λ ≤ Λ_max)          = {P_log_uniform:.4f}  ≈ {P_log_uniform*100:.1f}%")
print(f"  → log10 P             = {log10_P_log:.3f}")
print(f"\n  N_expected (log-unif) = 10^{N_vacua_log10} × {P_log_uniform:.4f}")
print(f"                        = 10^{log10_N_exp_log:.1f}")
if log10_N_exp_log > 0:
    print(f"  → VASTLY > 1 : anthropic selection VIABLE (many vacua in window)")
else:
    print(f"  → << 1 : anthropic selection FAILS for log-uniform prior")

# ─────────────────────────────────────────────────────────────────────────────
# Distribution B — Uniform prior on [0, ρ_Planck]
#
# P(Λ ≤ Λ_max) = Λ_max / ρ_Planck
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("DISTRIBUTION B — UNIFORM PRIOR")
print("=" * 70)

P_uniform    = rho_Lam_max / rho_Planck   # extremely small number
log10_P_unif = math.log10(P_uniform)      # ≈ -138.4

log10_N_exp_unif = N_vacua_log10 + log10_P_unif   # 500 - 138.4 ≈ 361.6

# Compute the mantissa for pretty-printing: 10^361.6 = 10^0.6 × 10^361
exponent_int = int(log10_N_exp_unif)
mantissa     = 10 ** (log10_N_exp_unif - exponent_int)

print(f"\n  P(Λ ≤ Λ_max)          = Λ_max / ρ_Planck")
print(f"                        = {rho_Lam_max:.4e} / {rho_Planck:.4e}")
print(f"                        = {P_uniform:.3e}")
print(f"  → log10 P             = {log10_P_unif:.2f}")
print(f"\n  N_expected (uniform)  = 10^{N_vacua_log10} × 10^{log10_P_unif:.2f}")
print(f"                        = 10^{log10_N_exp_unif:.1f}")
print(f"                        ≈ {mantissa:.2f} × 10^{exponent_int}")
if log10_N_exp_unif > 0:
    print(f"  → VASTLY > 1 : anthropic selection VIABLE (many vacua in window)")
else:
    print(f"  → << 1 : anthropic selection FAILS for uniform prior")

# ─────────────────────────────────────────────────────────────────────────────
# Distribution C — Gaussian centred on 0 with width σ = ρ_Planck
#
# P(Λ ∈ [0, Λ_max]) = Φ(Λ_max / σ) − Φ(0)
#                    = Φ(Λ_max / σ) − 0.5
# For Λ_max ≪ σ:
#   Φ(x) ≈ 0.5 + x/√(2π)   (first-order Taylor)
#   P ≈ Λ_max / (σ √(2π))
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("DISTRIBUTION C — GAUSSIAN (σ = ρ_Planck, centred on 0)")
print("=" * 70)

sigma_gauss  = rho_Planck
# P ≈ Λ_max / (σ √(2π))  since Λ_max / σ = 10^{-138.4} ≪ 1
P_gauss      = rho_Lam_max / (sigma_gauss * math.sqrt(2 * math.pi))
log10_P_gauss = math.log10(P_gauss)

log10_N_exp_gauss = N_vacua_log10 + log10_P_gauss

print(f"\n  σ = ρ_Planck          = {sigma_gauss:.4e} J/m³")
print(f"  x = Λ_max/σ           = {rho_Lam_max/sigma_gauss:.3e}  (≪ 1 → linear regime)")
print(f"  P(Λ ∈ [0,Λ_max])      ≈ Λ_max / (σ√(2π))")
print(f"                        = {P_gauss:.3e}")
print(f"  → log10 P             = {log10_P_gauss:.2f}")
print(f"\n  N_expected (Gaussian) = 10^{N_vacua_log10} × 10^{log10_P_gauss:.2f}")
print(f"                        = 10^{log10_N_exp_gauss:.1f}")
if log10_N_exp_gauss > 0:
    print(f"  → VASTLY > 1 : anthropic selection VIABLE")
else:
    print(f"  → << 1 : anthropic selection FAILS for Gaussian prior")

# ─────────────────────────────────────────────────────────────────────────────
# Landscape resolution — the key quantitative finding
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("LANDSCAPE RESOLUTION — KEY FINDING")
print("=" * 70)

print(f"""
  Anthropic window:      Λ ∈ [0, {rho_Lam_max:.3e} J/m³]
  Window width fraction: Λ_max/ρ_Planck = {P_uniform:.2e}  (= 10^{log10_P_unif:.1f})

  Despite a prior probability of only 10^{log10_P_unif:.0f} for any single
  vacuum to fall in the window, the 10^{N_vacua_log10} vacua give:

    N_in_window ≈ 10^{log10_N_exp_unif:.0f}  (uniform prior)
    N_in_window ≈ 10^{log10_N_exp_log:.0f}   (log-uniform prior)
    N_in_window ≈ 10^{log10_N_exp_gauss:.0f} (Gaussian prior)

  All three priors agree: the landscape provides an enormous number of
  vacua inside the anthropic window. Anthropic selection is NUMERICALLY
  VIABLE — there are vastly more than enough candidate vacua.

  The apparent fine-tuning (10^{-log10_P_unif:.0f} suppression) is entirely
  swamped by the combinatorial richness of the landscape (10^{N_vacua_log10}).
""")

# ─────────────────────────────────────────────────────────────────────────────
# K-information (Kolmogorov complexity) perspective
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("K-INFORMATION PERSPECTIVE")
print("=" * 70)

bits_per_flux   = math.log2(values_per_flux)              # bits to specify one flux quantum
K_landscape     = N_fluxes * bits_per_flux                # bits to describe the full landscape
# Use log identity to avoid overflow: log2(10^x) = x * log2(10)
K_address       = N_vacua_log10     * math.log2(10)       # bits to address one vacuum
K_in_window     = log10_N_exp_unif  * math.log2(10)       # bits to address a window vacuum

print(f"""
  Landscape specification (Kolmogorov content):
    N_fluxes                    = {N_fluxes}
    values per flux             = {values_per_flux}  (O(1) integers)
    bits per flux quantum       = log₂({values_per_flux}) = {bits_per_flux:.2f}
    K(landscape)                = {N_fluxes} × {bits_per_flux:.2f} ≈ {K_landscape:.0f} bits

  Addressing a specific vacuum:
    K(address our vacuum)       = log₂(10^{N_vacua_log10}) ≈ {K_address:.0f} bits
    This is the number of bits needed to specify WHICH vacuum we inhabit.

  Structure of the anthropic window:
    Vacua in window             ≈ 10^{log10_N_exp_unif:.0f}
    log₂(vacua in window)       ≈ {K_in_window:.0f} bits (to address any window vacuum)
    Extra specificity beyond window: {K_address:.0f} - {K_in_window:.0f} ≈ {K_address-K_in_window:.0f} bits

  K-complexity verdict:
    Our universe's vacuum is K-SHORT in the landscape:
      • Only {K_landscape:.0f} bits describe the full flux landscape (the "codebook")
      • Only {K_address:.0f} bits "address" our specific vacuum within it
      • This {K_address:.0f}-bit address is the COMPLETE physical specification of our
        vacuum's Λ — no additional fine-tuning information is needed.
    The landscape makes our specific Λ K-COMPACT: a {K_address:.0f}-bit string
    selects our vacuum from {N_vacua_log10} decades of choices.
""")

# ─────────────────────────────────────────────────────────────────────────────
# Summary table
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print(f"""
  Quantity                          Value
  ─────────────────────────────────────────────────────────────
  ρ_Λ observed                      {rho_Lam_obs:.3e} J/m³
  ρ_Λ max (anthropic window)        {rho_Lam_max:.3e} J/m³
  ρ_Planck                          {rho_Planck:.3e} J/m³
  N_vacua (landscape)               10^{N_vacua_log10}
  ─────────────────────────────────────────────────────────────
  P(window | uniform prior)         {P_uniform:.2e}  (10^{log10_P_unif:.1f})
  P(window | log-uniform prior)     {P_log_uniform:.4f}  ({P_log_uniform*100:.1f}%)
  P(window | Gaussian prior)        {P_gauss:.2e}
  ─────────────────────────────────────────────────────────────
  N_expected (uniform)              10^{log10_N_exp_unif:.1f}
  N_expected (log-uniform)          10^{log10_N_exp_log:.1f}
  N_expected (Gaussian)             10^{log10_N_exp_gauss:.1f}
  ─────────────────────────────────────────────────────────────
  Anthropic selection viable?       YES (all priors give N >> 1)
  ─────────────────────────────────────────────────────────────
  K(landscape codebook)             {K_landscape:.0f} bits
  K(our vacuum address)             {K_address:.0f} bits
  K(window address)                 {K_in_window:.0f} bits
  ─────────────────────────────────────────────────────────────
""")

# ─────────────────────────────────────────────────────────────────────────────
# Save results/landscape_data.json
# ─────────────────────────────────────────────────────────────────────────────

data = {
    "physical_constants": {
        "rho_Lambda_obs_J_m3":   rho_Lam_obs,
        "rho_Lambda_max_J_m3":   rho_Lam_max,
        "rho_Planck_J_m3":       rho_Planck,
        "window_factor":         window_factor,
    },
    "landscape_parameters": {
        "N_fluxes":              N_fluxes,
        "values_per_flux":       values_per_flux,
        "log10_N_vacua":         N_vacua_log10,
    },
    "window_geometry": {
        "log10_window_over_Planck":   log10_window_over_Planck,
        "window_fraction_uniform":    P_uniform,
        "log10_window_fraction":      log10_P_unif,
    },
    "distribution_A_log_uniform": {
        "epsilon_IR_cutoff_J_m3":     epsilon,
        "P_Lambda_leq_max":           P_log_uniform,
        "log10_P":                    log10_P_log,
        "log10_N_expected":           log10_N_exp_log,
        "anthropic_viable":           log10_N_exp_log > 0,
    },
    "distribution_B_uniform": {
        "P_Lambda_leq_max":           P_uniform,
        "log10_P":                    log10_P_unif,
        "log10_N_expected":           log10_N_exp_unif,
        "N_expected_mantissa":        mantissa,
        "N_expected_exponent":        exponent_int,
        "anthropic_viable":           log10_N_exp_unif > 0,
    },
    "distribution_C_gaussian": {
        "sigma_J_m3":                 sigma_gauss,
        "x_Lam_max_over_sigma":       rho_Lam_max / sigma_gauss,
        "P_Lambda_leq_max":           P_gauss,
        "log10_P":                    log10_P_gauss,
        "log10_N_expected":           log10_N_exp_gauss,
        "anthropic_viable":           log10_N_exp_gauss > 0,
    },
    "k_information": {
        "bits_per_flux":              bits_per_flux,
        "K_landscape_bits":           K_landscape,
        "K_vacuum_address_bits":      K_address,
        "K_window_address_bits":      K_in_window,
        "extra_bits_beyond_window":   K_address - K_in_window,
    },
    "key_finding": (
        f"The string landscape provides ~10^{log10_N_exp_unif:.0f} vacua inside the "
        f"anthropic window (uniform prior), making anthropic selection numerically "
        f"viable. The specific vacuum giving our observed Λ can be addressed with "
        f"~{K_address:.0f} bits of K-information (the flux configuration). "
        f"Our universe is K-compact within the landscape."
    ),
}

results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(results_dir, exist_ok=True)
json_path = os.path.join(results_dir, "landscape_data.json")
with open(json_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"Saved: {json_path}")
