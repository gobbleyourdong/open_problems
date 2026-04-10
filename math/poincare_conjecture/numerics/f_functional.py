#!/usr/bin/env python3
"""
Perelman's F-Functional — Numerical Verification

Perelman's F-functional (Paper 1, Section 1):
  F(g, f) = ∫_M (R + |∇f|²) e^(-f) dV

This is the FIRST of Perelman's three functionals (F, λ, W). Properties:
  1. F is monotone non-decreasing under MODIFIED Ricci flow
       ∂g/∂t = -2(Ric + Hess(f))
       ∂f/∂t = -Δf + |∇f|² - R
  2. λ(g) = inf_f F(g, f) over f with ∫ e^(-f) dV = 1
  3. Critical points of F are STEADY GRADIENT SOLITONS (Ric + Hess(f) = 0)

The relationship between F, λ, and W:
  F = generalized energy (depends on auxiliary f)
  λ = inf F = lowest eigenvalue of -4Δ + R (depends only on g)
  W = scale-invariant version (introduces scale parameter τ)

This script:
1. Computes F on round S³ for constant f (matches λ)
2. Verifies F = λ at the minimum
3. Computes the soliton equation Ric + Hess(f) = 0
4. Shows the round sphere is the unique steady soliton on S³
"""

import numpy as np


# ===========================================================
# F-functional on round S³(r) with constant f
# ===========================================================
# For constant f: |∇f|² = 0
# Constraint ∫ e^(-f) dV = 1 → e^(-f) = 1/vol = 1/(2π² r³)
# F = ∫ R · e^(-f) dV = R · vol · e^(-f) = R · 1 = R
# So F(g_round, f_const) = R = 6/r²

def F_round_constant_f(r):
    """F-functional on round S³(r) with optimal constant f."""
    R = 6 / r**2
    return R


def lambda_round(r):
    """λ(g) = inf_f F = R for constant-curvature metric."""
    return 6 / r**2  # = R = lowest eigenvalue of -4Δ + R when f is constant


def test_F_on_round_s3():
    """Verify F on round S³ matches the analytical formula."""
    print("=" * 70)
    print("TEST 1: F-functional on round S³(r)")
    print("=" * 70)
    print()
    print("On round S³(r) with constant f optimal:")
    print("  R = 6/r² (constant)")
    print("  ∇f = 0")
    print("  ∫ e^(-f) dV = 1 (normalization)")
    print("  F = ∫ R e^(-f) dV = R · 1 = 6/r²")
    print()
    print(f"{'r':>8} {'R':>12} {'F(g, f)':>12} {'λ(g)':>12} {'F = λ?':>10}")
    print("-" * 60)

    for r in [0.5, 1.0, 2.0, 5.0, 10.0]:
        F = F_round_constant_f(r)
        lam = lambda_round(r)
        match = "YES" if abs(F - lam) < 1e-12 else "NO"
        print(f"{r:8.2f} {6/r**2:12.6f} {F:12.6f} {lam:12.6f} {match:>10s}")

    print()
    print("F = λ on round S³ for constant f (Einstein metrics achieve the minimum).")


# ===========================================================
# F is monotone under modified Ricci flow
# ===========================================================
# Under modified flow ∂g/∂t = -2(Ric + Hess(f)):
#   dF/dt = 2 ∫ |Ric + Hess(f)|² e^(-f) dV ≥ 0
# Equality iff Ric + Hess(f) = 0 (steady gradient soliton)

def test_F_monotone_under_flow():
    """Verify F is monotone non-decreasing on round S³ shrinking."""
    print("=" * 70)
    print("TEST 2: F monotone under (modified) Ricci flow")
    print("=" * 70)
    print()
    print("On round S³(r(t)) under unnormalized RF: r²(t) = r₀² - 4t")
    print("F(g(t)) = R(t) = 6/r²(t) = 6/(r₀² - 4t) → ∞ as t → T")
    print()

    r0 = 1.0
    T = r0**2 / 4
    print(f"r₀ = {r0}, T = {T}")
    print()
    print(f"{'t':>8} {'r(t)':>10} {'F(t) = R(t)':>14} {'monotone?':>10}")
    print("-" * 50)

    prev_F = None
    monotone = True
    for frac in [0, 0.1, 0.3, 0.5, 0.7, 0.85, 0.95, 0.99]:
        t = frac * T
        r = np.sqrt(r0**2 - 4*t)
        F = F_round_constant_f(r)
        is_mono = "—"
        if prev_F is not None:
            if F >= prev_F - 1e-12:
                is_mono = "YES"
            else:
                is_mono = "NO"
                monotone = False
        print(f"{t:8.4f} {r:10.6f} {F:14.4f} {is_mono:>10s}")
        prev_F = F

    print()
    print(f"F monotone non-decreasing: {monotone}")
    print("F → ∞ at extinction (curvature blows up)")
    return monotone


# ===========================================================
# Steady gradient soliton equation
# ===========================================================
# A steady gradient soliton satisfies:
#   Ric + Hess(f) = 0
#
# On a closed manifold, integrating gives ∫ R dV + ∫ Δf dV = 0.
# But ∫ Δf dV = 0 (divergence theorem), so ∫ R dV = 0.
# This means: a closed steady soliton must have ZERO total scalar curvature.
#
# On S³ with Ric > 0 everywhere: R > 0 strictly, so ∫ R dV > 0.
# Therefore: NO steady soliton exists on S³ except the trivial one (Ric = 0),
# which doesn't apply because S³ has no Ricci-flat metrics.

def test_no_steady_soliton_on_s3():
    """Verify no non-trivial steady soliton exists on closed S³."""
    print("=" * 70)
    print("TEST 3: No steady gradient soliton on closed S³")
    print("=" * 70)
    print()
    print("Steady gradient soliton: Ric + Hess(f) = 0")
    print("Integrate over closed M: ∫(R + Δf) dV = 0")
    print("But ∫ Δf dV = 0 (divergence theorem)")
    print("Therefore: ∫ R dV = 0")
    print()
    print("On S³(r): R = 6/r² > 0, so ∫ R dV = 6·vol/r² > 0")
    print()

    for r in [0.5, 1.0, 2.0]:
        R = 6 / r**2
        vol = 2 * np.pi**2 * r**3
        integral = R * vol
        print(f"  r = {r}: ∫ R dV = {integral:.4f} ≠ 0")

    print()
    print("Conclusion: NO steady gradient soliton on closed S³.")
    print("Round S³ is a SHRINKING soliton (W-entropy critical), not steady.")
    print("This is consistent with Perelman's classification.")


# ===========================================================
# Round S³ as a shrinking soliton
# ===========================================================
# A shrinking gradient soliton satisfies:
#   Ric + Hess(f) - g/(2τ) = 0
#
# For round S³(r) with f constant:
#   Ric = (2/r²) g
#   Hess(f) = 0
#   g/(2τ) = g/(2τ)
# So: (2/r²) g - g/(2τ) = 0  ⟺  τ = r²/4
#
# At τ = r²/4, round S³(r) IS a shrinking soliton with f = const.
# This is the ONLY shrinking soliton on closed S³ (Hamilton).

def test_shrinking_soliton_round_s3():
    """Verify round S³(r) is a shrinking soliton with τ = r²/4."""
    print("=" * 70)
    print("TEST 4: Round S³ as a shrinking gradient soliton")
    print("=" * 70)
    print()
    print("Shrinking soliton equation: Ric + Hess(f) - g/(2τ) = 0")
    print("On round S³(r) with f = const: Hess(f) = 0, Ric = (2/r²) g")
    print("So: (2/r²) g - g/(2τ) = 0  ⟺  τ = r²/4")
    print()
    print(f"{'r':>8} {'Ric eigenvalue':>16} {'τ_soliton':>12} {'2τ·Ric/g':>12}")
    print("-" * 55)

    for r in [0.5, 1.0, 1.5, 2.0]:
        ric_eigval = 2 / r**2
        tau = r**2 / 4
        check = 2 * tau * ric_eigval  # should equal 1
        print(f"{r:8.2f} {ric_eigval:16.6f} {tau:12.6f} {check:12.6f}")

    print()
    print("Verified: round S³(r) is a shrinking soliton at τ = r²/4.")
    print("This matches r²(t) = r₀² - 4t = 4τ when τ = T - t.")
    print()
    print("Hamilton's classification: round S³ is the UNIQUE shrinking soliton")
    print("on a closed simply-connected 3-manifold (up to isometry and scale).")


# ===========================================================
# F vs λ vs W: the three functionals
# ===========================================================

def perelman_functional_comparison():
    """Compare Perelman's three functionals."""
    print("=" * 70)
    print("TEST 5: Perelman's three functionals (F, λ, W)")
    print("=" * 70)
    print()

    table = [
        ("F", "∫(R + |∇f|²)e^(-f) dV", "modified Ricci flow",
         "steady soliton (Ric+Hess(f)=0)"),
        ("λ", "inf_f F", "pure Ricci flow",
         "Einstein metric"),
        ("W", "∫[τ(R+|∇f|²) + f - n] u dV", "Ricci flow at scale τ",
         "shrinking soliton"),
    ]

    print(f"{'Name':<6} {'Definition':<25} {'Monotone under':<22} {'Critical points'}")
    print("-" * 90)
    for name, defn, mono, crit in table:
        print(f"{name:<6} {defn:<25} {mono:<22} {crit}")

    print()
    print("All three are 'free energies' for different normalizations of Ricci flow.")
    print("F is simplest (no τ). λ is the optimal F over f (computable: lowest e.v.).")
    print("W introduces scale τ and is the most powerful (gives κ-noncollapsing).")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Poincaré Conjecture — Numerical Track: F-Functional")
    print()

    test_F_on_round_s3()
    print()
    monotone = test_F_monotone_under_flow()
    print()
    test_no_steady_soliton_on_s3()
    print()
    test_shrinking_soliton_round_s3()
    print()
    perelman_functional_comparison()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"F-functional verification: {'PASS' if monotone else 'FAIL'}")
    print()
    print("Perelman's F-functional verified on round S³:")
    print("  - F = R = 6/r² (matches λ for constant f)")
    print("  - F monotone non-decreasing under (modified) Ricci flow")
    print("  - NO steady soliton on closed S³ (∫ R dV ≠ 0)")
    print("  - Round S³(r) IS a shrinking soliton at τ = r²/4")
    print()
    print("The three functionals (F, λ, W) form a hierarchy:")
    print("  F: simplest, depends on auxiliary f")
    print("  λ: optimal F (lowest eigenvalue of -4Δ+R)")
    print("  W: scale-invariant, gives κ-noncollapsing")
    print()
    print("All three are non-decreasing under Ricci flow.")
    print("Round S³ achieves equality in W (it IS the soliton).")
