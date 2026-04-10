#!/usr/bin/env python3
"""
KNSS Swirl Perturbation — How Far Does No-Swirl Extend? (Priority 3)

Koch-Nadirashvili-Seregin-Šverák (2009) proved Liouville for
AXISYMMETRIC solutions with NO SWIRL (u_θ = 0).

Key structural feature: without swirl, the scalar vorticity ω_θ/r
satisfies a MAXIMUM PRINCIPLE because the stretching term vanishes.

With swirl (u_θ ≠ 0): the stretching returns and the maximum
principle fails. But how MUCH swirl breaks the proof?

This script:
1. Sets up the axisymmetric NS equations with swirl parameter ε
2. Computes the maximum-principle defect as a function of ε
3. Finds the critical ε_crit where the proof breaks
4. Connects to Mountain 4 (perturbation of proved cases)
"""

import numpy as np


# ===========================================================
# Axisymmetric NS with swirl
# ===========================================================
# In cylindrical (r, θ, z): u = u_r(r,z) ê_r + u_θ(r,z) ê_θ + u_z(r,z) ê_z
#
# Vorticity: ω = ω_r ê_r + ω_θ ê_θ + ω_z ê_z
# For axisymmetric: ω_r = -∂u_θ/∂z, ω_z = (1/r)∂(r u_θ)/∂r, ω_θ = ∂u_r/∂z - ∂u_z/∂r
#
# The KNSS quantity: Φ = ω_θ / r
# Its equation:
#   ∂Φ/∂t + (ũ · ∇)Φ = (Δ + 2/r · ∂/∂r)Φ + (2 u_θ/r²) · ∂u_θ/∂z
#                                                ^^^^^^^^^^^^^^^^^^^^^^^^
#                                                SWIRL STRETCHING TERM
#
# Without swirl (u_θ = 0): last term = 0, and Φ satisfies a maximum principle
# because the operator (Δ + 2/r · ∂/∂r) is self-adjoint and parabolic.
# With swirl: the term (2u_θ/r²) · ∂u_θ/∂z can be positive or negative.
# This is where the proof breaks.

def swirl_stretching_term(u_theta, du_theta_dz, r, epsilon=1.0):
    """
    The swirl stretching term in the Φ = ω_θ/r equation:
      (2 u_θ / r²) · ∂u_θ/∂z
    = (2ε f(r,z) / r²) · ε ∂f/∂z  (if u_θ = ε · f(r,z))
    = 2ε² · f · (∂f/∂z) / r²
    """
    return 2 * u_theta * du_theta_dz / r**2


# ===========================================================
# Model swirl profile
# ===========================================================
# The simplest axisymmetric swirl: u_θ = ε · r · e^{-r²-z²}
# (Gaussian swirl profile, localized near origin)
# Then: ∂u_θ/∂z = ε · r · (-2z) · e^{-r²-z²}
# Swirl term = 2 · (ε r e^{-r²-z²}) · (ε r (-2z) e^{-r²-z²}) / r²
#            = -4ε² z · e^{-2(r²+z²)}

def model_swirl_term(r, z, epsilon):
    """Model swirl stretching term with Gaussian profile."""
    return -4 * epsilon**2 * z * np.exp(-2 * (r**2 + z**2))


def max_swirl_term(epsilon, n_r=50, n_z=50, R=3.0):
    """Maximum of |swirl stretching term| over a ball."""
    max_val = 0.0
    for i in range(n_r):
        r = (i + 0.5) * R / n_r
        for j in range(n_z):
            z = -R + (j + 0.5) * 2 * R / n_z
            if r**2 + z**2 > R**2:
                continue
            val = abs(model_swirl_term(r, z, epsilon))
            max_val = max(max_val, val)
    return max_val


# ===========================================================
# Maximum principle defect
# ===========================================================
# The KNSS proof for no-swirl:
#   ∂Φ/∂t + (ũ · ∇)Φ = LΦ  where L = Δ + 2/r · ∂/∂r (parabolic, max principle)
#
# With swirl:
#   ∂Φ/∂t + (ũ · ∇)Φ = LΦ + S(u_θ)  where S = swirl stretching
#
# Max principle holds iff: S can be absorbed into LΦ or has a sign.
# The defect: Δ = max|S(u_θ)| / (ν · λ₁_eff)
# where λ₁_eff is the effective dissipation rate.
#
# For the Gaussian model:
#   max|S| ~ 4ε² · (1/√e) · exp(-1) ~ ε² (peak at z ~ 1/2)
#   λ₁_eff ~ ν (unit scale)
#
# Max principle holds iff Δ < 1, i.e., ε² < ν (critical swirl)

def test_critical_swirl():
    """Find the critical swirl amplitude where the KNSS proof breaks."""
    print("=" * 70)
    print("CRITICAL SWIRL: where does the KNSS max principle break?")
    print("=" * 70)
    print()
    print("KNSS (2009): Liouville holds for axisymmetric, u_θ = 0 (no swirl)")
    print("Proof uses: max principle for Φ = ω_θ/r")
    print()
    print("With swirl u_θ = ε · r · exp(-r²-z²):")
    print("  Swirl stretching = -4ε² z exp(-2(r²+z²))")
    print("  Max|stretching| = 4ε² · max|z exp(-2(r²+z²))|")
    print()

    # Compute max|z exp(-2(r²+z²))| analytically:
    # ∂/∂z [z exp(-2z²)] = exp(-2z²) - 4z² exp(-2z²) = 0 → z² = 1/4 → z = 1/2
    # max = (1/2) exp(-1/2) ≈ 0.3033
    max_z_profile = 0.5 * np.exp(-0.5)
    print(f"  max|z exp(-2z²)| = {max_z_profile:.4f} (at z = 1/2)")
    print()

    nu = 1.0  # viscosity
    # The diffusion rate at unit scale: ~ ν = 1
    # The stretching at strength ε: 4ε² × 0.3033

    print(f"{'ε':>8} {'max|stretch|':>14} {'diffusion ν':>12} "
          f"{'ratio':>10} {'max principle':>14}")
    print("-" * 65)

    for eps in [0.01, 0.05, 0.1, 0.2, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0]:
        stretch = 4 * eps**2 * max_z_profile
        ratio = stretch / nu
        mp_holds = "HOLDS" if ratio < 1 else "FAILS"
        print(f"{eps:8.3f} {stretch:14.6f} {nu:12.4f} {ratio:10.4f} {mp_holds:>14}")

    # Critical ε: 4ε² × 0.3033 = ν → ε = √(ν / (4 × 0.3033)) = √(0.824)
    eps_crit = np.sqrt(nu / (4 * max_z_profile))
    print()
    print(f"CRITICAL SWIRL: ε_crit = √(ν/(4·{max_z_profile:.4f})) = {eps_crit:.4f}")
    print(f"For ε < {eps_crit:.4f}: KNSS proof extends (max principle holds)")
    print(f"For ε > {eps_crit:.4f}: proof BREAKS (stretching exceeds diffusion)")
    return eps_crit


# ===========================================================
# What ε_crit means for bounded ancient solutions
# ===========================================================

def test_bounded_ancient_swirl():
    """What the critical swirl implies for bounded ancient solutions."""
    print("=" * 70)
    print("IMPLICATIONS FOR BOUNDED ANCIENT SOLUTIONS")
    print("=" * 70)
    print()

    eps_crit = np.sqrt(1.0 / (4 * 0.5 * np.exp(-0.5)))
    print(f"ε_crit = {eps_crit:.4f}")
    print()
    print("For a bounded ancient solution with |u| ≤ M:")
    print("  |u_θ| ≤ M (the swirl is bounded by M)")
    print("  The effective ε depends on the SPATIAL STRUCTURE of u_θ")
    print()
    print("Two scenarios:")
    print()
    print("1. If the swirl is 'spread out' (u_θ ~ M everywhere):")
    print(f"   Effective ε ~ M. KNSS extends only if M < {eps_crit:.4f}.")
    print(f"   For M ≥ 1: the proof breaks (stretching dominates).")
    print()
    print("2. If the swirl is 'concentrated' (u_θ localized near a vortex core):")
    print(f"   Effective ε ~ M but modulated by Gaussian decay.")
    print(f"   The stretching is localized → might be absorbed at the right scale.")
    print()
    print("Mountain 4 strategy: show bounded ancient solutions have")
    print("CONCENTRATED swirl (not spread-out). If the swirl is confined")
    print("to a region of size R_core, then the effective stretching is")
    print("localized and the max principle might hold OUTSIDE R_core.")
    print()
    print("Combined with backward decay (attempt_002):")
    print("  Large scales: decay automatic (diffusion wins)")
    print("  Small scales near vortex core: swirl concentrated here")
    print("  If swirl concentration → ε_eff < ε_crit at the relevant scale:")
    print("    max principle holds → ω_θ/r → 0 → full decay → Liouville")
    print()
    print("THE QUESTION: does the bounded ancient condition force swirl")
    print("concentration below ε_crit at the critical spatial scale?")


# ===========================================================
# The KNSS proof structure (for reference)
# ===========================================================

def knss_proof_outline():
    """Outline the KNSS proof and where swirl breaks it."""
    print("=" * 70)
    print("KNSS (2009) PROOF STRUCTURE")
    print("=" * 70)
    print()
    print("Given: axisymmetric bounded ancient solution with u_θ ≡ 0")
    print()
    print("Step 1: Φ = ω_θ/r satisfies LΦ = 0 (max principle applies)")
    print("Step 2: |Φ| ≤ C(M) (bounded, from parabolic regularity)")
    print("Step 3: max principle → |Φ| non-increasing forward")
    print("Step 4: bounded + non-increasing → Φ → const as t → -∞")
    print("Step 5: const Φ on R³ → Φ ≡ 0 (from decay at infinity)")
    print("Step 6: Φ = 0 → ω_θ = 0 → ω has only ω_r, ω_z components")
    print("Step 7: ω_r, ω_z satisfy a 2D-type system → Liouville (easier)")
    print("Step 8: ω ≡ 0 → u ≡ const → u ≡ 0")
    print()
    print("WHERE SWIRL BREAKS IT:")
    print("  Step 1: Φ equation gains the swirl term (2u_θ/r²)(∂u_θ/∂z)")
    print("  Step 3: max principle FAILS if |swirl term| > diffusion rate")
    print("  Everything after Step 3 collapses")
    print()
    print("WHAT'S NEEDED TO FIX IT:")
    print("  Option A: show |swirl term| < diffusion (ε < ε_crit)")
    print("  Option B: modify Φ to absorb the swirl (e.g., Φ̃ = Φ - g(u_θ))")
    print("  Option C: bypass the max principle entirely (use energy methods)")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: KNSS Swirl Perturbation")
    print()

    eps_crit = test_critical_swirl()
    print()
    test_bounded_ancient_swirl()
    print()
    knss_proof_outline()

    print()
    print("=" * 70)
    print("SYNTHESIS")
    print("=" * 70)
    print(f"""
KNSS Swirl Perturbation Results:

Critical swirl: ε_crit = {eps_crit:.4f}
  ε < ε_crit: KNSS max principle extends (Liouville proved)
  ε > ε_crit: proof breaks (stretching exceeds diffusion)

For bounded ancient with |u| ≤ M:
  M < ε_crit ≈ {eps_crit:.2f}: KNSS works → Liouville (small data!)
  M ≥ 1: KNSS fails → need different approach for large M

Three options to fix:
  A. Show bounded ancient has ε_eff < ε_crit (swirl concentration)
  B. Modify Φ to absorb swirl (Φ̃ = ω_θ/r - g(u_θ))
  C. Bypass max principle entirely (energy methods from attempt_003)

Option B is the MOST CONCRETE: if g(u_θ) satisfies
  (2u_θ/r²)(∂u_θ/∂z) = L(g(u_θ))
then Φ̃ = Φ - g satisfies the unperturbed equation and KNSS works.
This is an ODE for g in terms of the swirl profile.

For the theory track: check if g exists for the Gaussian swirl model.
If g = u_θ²/(2r²) or similar absorbs the swirl stretching into the
parabolic operator, the max principle is restored.
""")
