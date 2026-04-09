#!/usr/bin/env python3
"""
anthropic_window.py — Weinberg anthropic window for the cosmological constant.

Two tasks:
  1. Compute the Weinberg anthropic window: what is the maximum Λ consistent
     with galaxy formation, and where does the observed Λ sit in that window?
  2. Compute the Casimir vacuum energy density in a Planck-size box and compare
     to ρ_Λ and ρ_Planck.

References:
  - Weinberg (1987) Phys. Rev. Lett. 59, 2607
  - Planck 2018: Ω_m = 0.315, Ω_Λ = 0.685, H₀ = 67.4 km/s/Mpc
"""

import math
import json
import os

# ────────────────────────────────────────────────────────────────────────────
# Physical constants (SI)
# ────────────────────────────────────────────────────────────────────────────
hbar  = 1.054571817e-34   # J·s
c     = 2.998e8           # m/s
G     = 6.674e-11         # m³/(kg·s²)
eV    = 1.602e-19         # J
GeV   = 1e9 * eV          # J

# Cosmological parameters
H0_kms_Mpc = 67.4                        # km/s/Mpc
Mpc_in_m   = 3.0857e22                   # m per Mpc
H0         = H0_kms_Mpc * 1e3 / Mpc_in_m  # s⁻¹  ≈ 2.184e-18 s⁻¹

Omega_m    = 0.315
Omega_Lam  = 0.685

# Critical density today
rho_crit = 3 * H0**2 / (8 * math.pi * G)  # J/m³

# Component densities today
rho_m_today  = Omega_m   * rho_crit        # matter
rho_Lam_obs  = Omega_Lam * rho_crit        # dark energy (observed)
rho_Lam_obs_given = 5.924e-27              # J/m³  (direct from prompt)

# Planck length and Planck energy density
l_P        = math.sqrt(hbar * G / c**3)   # m  ≈ 1.616e-35 m
rho_Planck = hbar * c / l_P**4            # J/m³  (natural Planck density = ħc/l_P⁴)

print("=" * 65)
print("ANTHROPIC WINDOW FOR THE COSMOLOGICAL CONSTANT")
print("=" * 65)

# ────────────────────────────────────────────────────────────────────────────
# TASK 1 — Weinberg Anthropic Window
# ────────────────────────────────────────────────────────────────────────────

print("\n── Cosmological parameters ──")
print(f"  H₀            = {H0:.4e} s⁻¹")
print(f"  ρ_crit        = {rho_crit:.4e} J/m³")
print(f"  ρ_m today     = {rho_m_today:.4e} J/m³")
print(f"  ρ_Λ observed  = {rho_Lam_obs:.4e} J/m³  (derived from Ω_Λ)")
print(f"  ρ_Λ observed  = {rho_Lam_obs_given:.4e} J/m³  (given directly)")

# ── Step 1: Matter-Λ equality redshift ──────────────────────────────────────
# ρ_m(z) = ρ_m0 (1+z)³ = ρ_Λ  →  z_eq = (ρ_Λ/ρ_m0)^(1/3) - 1
z_eq_LM = (rho_Lam_obs / rho_m_today)**(1/3) - 1.0

print(f"\n── Step 1: Λ-matter equality ──")
print(f"  z_eq (Λ=matter)  = {z_eq_LM:.3f}")
print(f"  (Today Ω_Λ/Ω_m ≈ {Omega_Lam/Omega_m:.2f}, so equality was recent)")

# ── Step 2: Maximum Λ from galaxy formation ──────────────────────────────────
# Galaxies need to form before dark energy dominates.
# Conservative threshold: Λ-matter equality must happen at z ≥ z_min_form.
# Weinberg's argument uses z_min_form ≈ 2 (structure has time to collapse).

z_min_form = 2.0        # minimum redshift for Λ-matter equality

# ρ_Λ_max = ρ_m(z_min_form) = ρ_m0 × (1 + z_min_form)³
rho_Lam_max = rho_m_today * (1 + z_min_form)**3

print(f"\n── Step 2: Maximum Λ for galaxy formation ──")
print(f"  Require z_Λm ≥ {z_min_form:.1f} (structure forms before DE dominates)")
print(f"  ρ_Λ_max = ρ_m0 × (1+{z_min_form:.0f})³ = ρ_m0 × {(1+z_min_form)**3:.1f}")
print(f"  ρ_Λ_max = {rho_Lam_max:.4e} J/m³")

# Also compute for z_min = 5 (aggressive)
z_min_form_5 = 5.0
rho_Lam_max_z5 = rho_m_today * (1 + z_min_form_5)**3
print(f"\n  For z_min = 5 (first galaxies, aggressive):")
print(f"  ρ_Λ_max(z=5) = ρ_m0 × (1+5)³ = ρ_m0 × 216")
print(f"  ρ_Λ_max(z=5) = {rho_Lam_max_z5:.4e} J/m³")

# ── Step 3: Compare to observed ──────────────────────────────────────────────
ratio_max_to_obs_z2 = rho_Lam_max    / rho_Lam_obs_given
ratio_max_to_obs_z5 = rho_Lam_max_z5 / rho_Lam_obs_given

print(f"\n── Step 3: Anthropic window width ──")
print(f"  ρ_Λ_max(z=2) / ρ_Λ_obs = {ratio_max_to_obs_z2:.1f}")
print(f"  ρ_Λ_max(z=5) / ρ_Λ_obs = {ratio_max_to_obs_z5:.1f}")
print(f"  → Weinberg window spans ~{ratio_max_to_obs_z2:.0f}–{ratio_max_to_obs_z5:.0f}× observed Λ")

# ── Step 4: Anthropic prior probability ──────────────────────────────────────
# Uniform prior on Λ ∈ [0, ρ_Λ_max]:
#   P(Λ ≤ Λ_obs | Λ ≤ Λ_max) = Λ_obs / Λ_max
P_anthropic_z2 = rho_Lam_obs_given / rho_Lam_max
P_anthropic_z5 = rho_Lam_obs_given / rho_Lam_max_z5

print(f"\n── Step 4: Anthropic selection probability ──")
print(f"  Uniform prior on [0, ρ_Λ_max(z=2)]:")
print(f"    P(Λ_obs | window z=2) = 1 / {ratio_max_to_obs_z2:.1f} ≈ {P_anthropic_z2:.3f}")
print(f"  Uniform prior on [0, ρ_Λ_max(z=5)]:")
print(f"    P(Λ_obs | window z=5) = 1 / {ratio_max_to_obs_z5:.1f} ≈ {P_anthropic_z5:.4f}")

# ── Step 5: Compare to ρ_Planck ──────────────────────────────────────────────
ratio_Planck_to_obs  = rho_Planck / rho_Lam_obs_given
ratio_Planck_to_max  = rho_Planck / rho_Lam_max
log10_gap_Planck_obs = math.log10(ratio_Planck_to_obs)

print(f"\n── Step 5: Context vs Planck density ──")
print(f"  ρ_Planck      = {rho_Planck:.4e} J/m³")
print(f"  ρ_Planck/ρ_Λ  = {ratio_Planck_to_obs:.2e}  (the CC problem: ~10^{log10_gap_Planck_obs:.0f})")
print(f"  Anthropic window closes {math.log10(ratio_max_to_obs_z2):.1f} orders of magnitude of this gap")
print(f"  Remaining fine-tuning beyond window: ~10^{log10_gap_Planck_obs - math.log10(ratio_max_to_obs_z2):.1f}")

# ────────────────────────────────────────────────────────────────────────────
# TASK 2 — Casimir energy density in a Planck-size box
# ────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("CASIMIR ENERGY DENSITY IN A PLANCK-SIZE BOX")
print("=" * 65)

# Casimir energy for a massless scalar field in a cube of side L:
#   E_Casimir ≈ -ħ c × 0.09636 / L    (numerical coefficient from zeta-function regularisation)
# The commonly quoted result for a 3D cubic box is:
#   E_Casimir = -A × ħ c / L
# where A ≈ 0.09636 for a scalar field (Lukosz 1971; Ambjorn & Wolfram 1983).
# For the EM field (2 polarisations) the prefactor is roughly 2× the scalar.
# We use the scalar result as the base case.

A_scalar = 0.09636   # dimensionless Casimir coefficient for cubic box, scalar field
A_EM     = 2 * A_scalar  # two polarisation modes (rough)

L = l_P   # box side = Planck length

E_Casimir_scalar = -A_scalar * hbar * c / L   # J  (negative = attractive)
E_Casimir_EM     = -A_EM     * hbar * c / L   # J

V_box = L**3   # m³

# Energy density = |E_Casimir| / V
rho_Casimir_scalar = abs(E_Casimir_scalar) / V_box
rho_Casimir_EM     = abs(E_Casimir_EM)     / V_box

print(f"\n  Planck length l_P  = {l_P:.4e} m")
print(f"  Box volume  V      = l_P³ = {V_box:.4e} m³")
print(f"\n  Casimir energy (scalar field, cubic box):")
print(f"    E_Casimir = -A·ħc/l_P  where A = {A_scalar}")
print(f"    E_Casimir = {E_Casimir_scalar:.4e} J")
print(f"    ρ_Casimir = |E|/V = {rho_Casimir_scalar:.4e} J/m³")
print(f"\n  Casimir energy (EM, 2 polarisations):")
print(f"    E_Casimir = {E_Casimir_EM:.4e} J")
print(f"    ρ_Casimir = |E|/V = {rho_Casimir_EM:.4e} J/m³")

# Compare to ρ_Λ and ρ_Planck
ratio_casimir_to_Lam    = rho_Casimir_scalar / rho_Lam_obs_given
ratio_casimir_to_Planck = rho_Casimir_scalar / rho_Planck

print(f"\n  ρ_Planck              = {rho_Planck:.4e} J/m³")
print(f"  ρ_Λ observed          = {rho_Lam_obs_given:.4e} J/m³")
print(f"\n  Ratios (scalar Casimir):")
print(f"    ρ_Casimir / ρ_Λ       = {ratio_casimir_to_Lam:.2e}  (10^{math.log10(ratio_casimir_to_Lam):.1f})")
print(f"    ρ_Casimir / ρ_Planck  = {ratio_casimir_to_Planck:.4f}")
print(f"    → Casimir density at l_P is ~order-of-magnitude of ρ_Planck (expected)")
print(f"    → Casimir density exceeds ρ_Λ by 10^{math.log10(ratio_casimir_to_Lam):.0f}")

# ────────────────────────────────────────────────────────────────────────────
# Summary and physical interpretation
# ────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)
print(f"""
Anthropic window:
  • Weinberg threshold (z=2): ρ_Λ_max = {rho_Lam_max:.3e} J/m³
  • Observed Λ is {ratio_max_to_obs_z2:.0f}× below that threshold → YES, inside window
  • Uniform-prior probability: P ≈ 1/{ratio_max_to_obs_z2:.0f} ≈ {P_anthropic_z2:.2f}
  • The window explains O(1) orders of magnitude, not the full ~10^{log10_gap_Planck_obs:.0f}
  • Residual puzzle: why is Λ/Λ_Planck ~ 10^{log10_gap_Planck_obs:.0f} still unexplained

Casimir vacuum energy at l_P:
  • ρ_Casimir(l_P) ≈ {rho_Casimir_scalar:.2e} J/m³  ≈ {ratio_casimir_to_Planck:.2f} × ρ_Planck
  • Exceeds ρ_Λ_obs by ~10^{math.log10(ratio_casimir_to_Lam):.0f}
  • This is the heart of the CC problem: Planck-scale quantum corrections
    are 10^{math.log10(ratio_casimir_to_Lam):.0f} times the observed dark energy density.
""")

# ────────────────────────────────────────────────────────────────────────────
# Save results/anthropic_data.json
# ────────────────────────────────────────────────────────────────────────────
data = {
    "cosmological_parameters": {
        "H0_km_s_Mpc":      H0_kms_Mpc,
        "H0_SI":            H0,
        "Omega_m":          Omega_m,
        "Omega_Lambda":     Omega_Lam,
        "rho_crit_J_m3":    rho_crit,
        "rho_m_today_J_m3": rho_m_today,
        "rho_Lambda_obs_J_m3": rho_Lam_obs_given,
        "rho_Planck_J_m3":  rho_Planck,
        "l_P_m":            l_P,
    },
    "anthropic_window": {
        "z_eq_Lambda_matter_today":    z_eq_LM,
        "z_min_galaxy_formation_conservative": z_min_form,
        "z_min_galaxy_formation_aggressive":   z_min_form_5,
        "rho_Lambda_max_z2_J_m3":     rho_Lam_max,
        "rho_Lambda_max_z5_J_m3":     rho_Lam_max_z5,
        "window_width_z2_ratio":      ratio_max_to_obs_z2,
        "window_width_z5_ratio":      ratio_max_to_obs_z5,
        "P_anthropic_uniform_prior_z2": P_anthropic_z2,
        "P_anthropic_uniform_prior_z5": P_anthropic_z5,
        "observed_Lambda_in_window_z2": True,
        "observed_Lambda_in_window_z5": True,
        "log10_Planck_to_obs_gap":    log10_gap_Planck_obs,
        "log10_window_closes":        math.log10(ratio_max_to_obs_z2),
        "log10_residual_fine_tuning": log10_gap_Planck_obs - math.log10(ratio_max_to_obs_z2),
    },
    "casimir_planck_box": {
        "box_side_m":               l_P,
        "box_volume_m3":            V_box,
        "casimir_coeff_scalar":     A_scalar,
        "casimir_energy_scalar_J":  E_Casimir_scalar,
        "rho_casimir_scalar_J_m3":  rho_Casimir_scalar,
        "casimir_coeff_EM":         A_EM,
        "casimir_energy_EM_J":      E_Casimir_EM,
        "rho_casimir_EM_J_m3":      rho_Casimir_EM,
        "ratio_casimir_to_rho_Lam": ratio_casimir_to_Lam,
        "ratio_casimir_to_rho_Planck": ratio_casimir_to_Planck,
        "log10_casimir_over_Lam":   math.log10(ratio_casimir_to_Lam),
    },
}

results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(results_dir, exist_ok=True)
json_path = os.path.join(results_dir, "anthropic_data.json")
with open(json_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"Saved: {json_path}")
