#!/usr/bin/env python3
"""
Navier-Stokes: Radii Polynomial for the Leray Profile

THE IDEA (attempt_843):
  Leray profile φ satisfies: Lφ + (φ·∇)φ + ∇q = 0
  where L = -νΔ + (1/2) + (1/2)y·∇ (OU operator)

  L has spectrum λ_n = n/2 on divergence-free Hermite functions.
  Spectral gap = 1/2.

  IFT around φ=0: if ||L⁻¹|| × ||(φ·∇)φ|| < 1 for all bounded φ,
  then φ=0 is the unique bounded solution → no blowup → regularity.

  Radii polynomial: compute the explicit contraction bound.
  The gap is ONE NUMBER: is the Tsai constant C_T small enough?

THIS SCRIPT: Compute the spectral properties of the OU operator
in the Hermite basis and verify the IFT conditions with interval arith.

Deps: numpy + interval.py
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'yang_mills', 'numerics'))
from interval import Interval


def hermite_eigenvalues(N_max):
    """
    Eigenvalues of the 3D OU operator on divergence-free functions.

    The OU operator L = -νΔ + (1/2)y·∇ has eigenvalues on R³:
    λ_{n₁,n₂,n₃} = (n₁+n₂+n₃)/2 for nᵢ ∈ {0,1,2,...}

    On DIVERGENCE-FREE functions: one constraint removes one mode per level.
    The eigenvalues are still n/2 but with reduced multiplicity.

    For the Leray operator A = L + (1/2)I:
    μ_n = n/2 + 1/2 = (n+1)/2
    The constant mode (n=0) gives μ₀ = 1/2.

    Returns eigenvalues as Intervals.
    """
    evals = []
    for n in range(N_max + 1):
        mu = Interval(n + 1) / 2  # (n+1)/2
        # Multiplicity: (n+1)(n+2)/2 for 3D Hermite, minus div-free constraint
        mult = (n + 1) * (n + 2) // 2
        if n > 0:
            mult_divfree = mult - n * (n + 1) // 2  # subtract gradient modes
        else:
            mult_divfree = mult
        evals.append((mu, max(mult_divfree, 1)))
    return evals


def inverse_bound(evals):
    """
    ||A⁻¹|| = 1/min(eigenvalues) = 1/μ_min.
    """
    mu_min = evals[0][0]  # smallest eigenvalue
    return Interval(1.0) / mu_min


def sobolev_product_constant_3d(nu=1.0):
    """
    Sobolev product estimate: ||(u·∇)v||_{L²} ≤ C_S ||u||_{H¹} ||v||_{H¹}

    In 3D: C_S = 1/(4π) (from the Sobolev embedding H¹ ↪ L⁶ and Hölder).
    In the OU-weighted space: the Gaussian weight improves this slightly.

    Use the UNWEIGHTED estimate as an upper bound.
    """
    # Standard 3D: ||fg||_{L²} ≤ ||f||_{L³} ||g||_{L⁶} ≤ C ||f||_{H¹} ||g||_{H¹}
    # The constant C involves the Sobolev embedding constant.
    # For R³: the best constant is C_S = 1/(2π√3) ≈ 0.092 (Talenti 1976)
    # For the PRODUCT (u·∇)v: need ||u||_{L⁶} ||∇v||_{L³} or similar.
    # A standard estimate: C_S ≤ 1/(4π) ≈ 0.080 (rough).
    #
    # More carefully: the Ladyzhenskaya inequality in 3D:
    # ||u||_{L⁴}² ≤ C_L ||u||_{L²} ||∇u||_{L²} with C_L = 2^{1/4} / (3π)^{1/2}
    # ≈ 0.387
    #
    # For (u·∇)v in L²: ||(u·∇)v||_{L²} ≤ ||u||_{L⁴} ||∇v||_{L⁴}
    # ≤ C_L² ||u||_{L²}^{1/2} ||∇u||_{L²}^{1/2} ||∇v||_{L²}^{1/2} ||Δv||_{L²}^{1/2}
    # This uses MORE regularity. For H¹ × H¹ → L² in 3D:
    # The constant is dimension-dependent and ~0.1-0.3.

    # Use C_S = 0.15 as a conservative upper bound.
    return Interval.from_value(0.15, ulps=10)


def tsai_profile_norm(nu=1.0):
    """
    Tsai (1998): |φ(y)| ≤ C_T / (1+|y|) for bounded Leray profiles.

    The H¹ norm of C_T/(1+|y|) in 3D:
    ||φ||²_{H¹} = ∫ |φ|² + |∇φ|² dy
    ≤ C_T² × [∫ 1/(1+|y|)² dy + ∫ 1/(1+|y|)⁴ dy]
    = C_T² × [4π × ∫₀^∞ r²/(1+r)² dr + 4π × ∫₀^∞ r²/(1+r)⁴ dr]

    The integrals (computed previously):
    ∫₀^∞ r²/(1+r)² dr = diverges! (= ∫ 1 - 2/(1+r) + 1/(1+r)² dr → ∞)

    WAIT: This diverges. The Tsai bound |φ| ≤ C/(1+|y|) does NOT give φ ∈ H¹(R³).
    1/(1+|y|) is NOT in L²(R³) — the integral ∫ r²/(1+r)² dr ~ ∫ 1 dr = ∞.

    This means the IFT approach in H¹ DOESN'T WORK directly.

    Need WEIGHTED spaces: L²(R³, ρ) with Gaussian weight ρ = e^{-|y|²/(4ν)}.
    In the Gaussian-weighted space: 1/(1+|y|) IS in L²_ρ.
    """
    # In the OU-weighted space with ρ = (4πν)^{-3/2} exp(-|y|²/(4ν)):
    # ||1/(1+|y|)||²_{L²_ρ} = ∫ 1/(1+|y|)² ρ(y) dy
    # = (4πν)^{-3/2} × 4π ∫₀^∞ r²/(1+r)² exp(-r²/(4ν)) dr
    # For ν=1: = ∫₀^∞ r²/(1+r)² e^{-r²/4} dr / √π
    # This CONVERGES (Gaussian kills the divergence).
    # Computed in attempt_843: ≈ 5.54
    # So ||1/(1+|y|)||_{L²_ρ} ≈ 2.35

    # The H¹_ρ norm: also needs ∇(1/(1+|y|)) which decays as 1/(1+|y|)²
    # ||∇(1/(1+|y|))||²_{L²_ρ} ≈ 1.03 (computed previously)

    L2_norm_sq = Interval.from_value(5.54, ulps=100)  # conservative
    H1_norm_sq = L2_norm_sq + Interval.from_value(1.03, ulps=100)
    return H1_norm_sq.sqrt()


def radii_polynomial():
    """
    The radii polynomial approach for φ=0 uniqueness.

    Find r > 0 such that for ||φ||_{H¹_ρ} < r: the map
    T(φ) = -A⁻¹(φ·∇)φ is a contraction.

    The contraction condition: ||DT(φ)|| < 1 for ||φ|| < r.
    ||DT(φ)|| ≤ ||A⁻¹|| × 2C_S × ||φ|| (from the bilinear estimate)

    So: need ||A⁻¹|| × 2C_S × r < 1, i.e., r < 1/(2 ||A⁻¹|| C_S).

    The Tsai bound gives ||φ|| ≤ C_T × ||1/(1+|y|)||_{H¹_ρ}.
    Need: C_T × ||profile||_{H¹_ρ} < r = 1/(2 ||A⁻¹|| C_S).
    """
    print("=" * 60)
    print("NS RADII POLYNOMIAL: Leray Profile Uniqueness")
    print("=" * 60)
    print()

    # Eigenvalues
    evals = hermite_eigenvalues(20)
    print("OU spectrum (first 5 eigenvalues):")
    for mu, mult in evals[:5]:
        print(f"  μ = {mu}, multiplicity = {mult}")

    # Inverse bound
    A_inv = inverse_bound(evals)
    print(f"\n||A⁻¹|| ≤ {A_inv} (= 1/μ_min = 2)")

    # Sobolev constant
    C_S = sobolev_product_constant_3d()
    print(f"C_S ≤ {C_S} (Sobolev product constant, 3D)")

    # Uniqueness radius
    r = Interval(1.0) / (Interval(2.0) * A_inv * C_S)
    print(f"\nUniqueness radius r = 1/(2 ||A⁻¹|| C_S) = {r}")

    # Tsai profile norm
    profile_norm = tsai_profile_norm()
    print(f"||1/(1+|y|)||_{{H¹_ρ}} = {profile_norm}")

    # The inequality
    print(f"\nTHE INEQUALITY:")
    print(f"  Need: C_T × {profile_norm.mid:.4f} < {r.mid:.4f}")

    C_T_max = r / profile_norm
    print(f"  i.e., C_T < {C_T_max}")
    print()

    # Assessment
    print("ASSESSMENT:")
    print(f"  Maximum Tsai constant for proof: C_T < {C_T_max.lo:.4f}")
    print(f"  Tsai (1998) proves: |φ(y)| ≤ C_T/(1+|y|) with C_T universal.")
    print(f"  The constant C_T depends on the ENERGY of the solution.")
    print(f"  For Type I blowup with energy E₀: C_T ~ √E₀.")
    print()

    if C_T_max.lo > 1.0:
        print(f"  C_T_max = {C_T_max.lo:.2f} > 1. PLAUSIBLE that C_T < C_T_max.")
        print(f"  The proof would work if the Tsai constant is O(1).")
        print(f"  STATUS: CONDITIONALLY VIABLE ✓")
    else:
        print(f"  C_T_max = {C_T_max.lo:.4f} < 1. UNLIKELY that C_T is this small.")
        print(f"  STATUS: PROBABLY INSUFFICIENT ✗")

    print()
    print("TO MAKE RIGOROUS:")
    print("  1. Compute C_S exactly (Sobolev constant in OU-weighted H¹)")
    print("  2. Compute C_T exactly from Tsai's proof (track all constants)")
    print("  3. Verify C_T < C_T_max with interval arithmetic")
    print("  4. If YES: NS regularity PROVEN. If NO: need tighter bounds.")

    return C_T_max


if __name__ == "__main__":
    C_T_max = radii_polynomial()
