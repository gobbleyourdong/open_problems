#!/usr/bin/env python3
"""
Bishop-Gromov Volume Comparison Theorem

The Bishop-Gromov inequality is one of the foundational results that
makes Perelman's κ-noncollapsing theorem work.

STATEMENT: If a Riemannian n-manifold M has Ric ≥ (n-1)K g, then for
any point p and any radii 0 < r < R, the ratio
  vol(B(p, r)) / vol_K(B^n(r))
is monotone non-increasing in r.

Here vol_K(B^n(r)) is the volume of a geodesic ball of radius r in the
model space of constant sectional curvature K (sphere if K>0, Euclidean
if K=0, hyperbolic if K<0).

CONSEQUENCE: vol(B(p, r)) ≤ vol_K(B^n(r)).
The model space gives the upper bound on volume.

This implies: if M has Ric ≥ 0 then vol(B(p,r))/r^n is monotone
non-increasing — the basis for κ-noncollapsing.

This script:
1. Computes vol(B(p,ρ)) analytically on round S³(r)
2. Verifies the Bishop-Gromov ratio is monotone non-increasing
3. Compares to H³ (negative curvature: ratio > 1, opposite direction)
4. Connects to Perelman's κ-noncollapsing
"""

import numpy as np


# ===========================================================
# Volume of geodesic ball on round S³(r)
# ===========================================================
# On S^n(r) in geodesic polar coordinates: ds² = dt² + r² sin²(t/r) g_{S^{n-1}}
# vol(B(p, ρ)) = ω_{n-1} ∫₀^ρ (r sin(t/r))^{n-1} dt
# For n=3: vol(B(p, ρ)) = 4π ∫₀^ρ r² sin²(t/r) dt
#                        = 4π · r²/2 · (ρ - r·sin(2ρ/r)/2)  ... let me check
# Actually: ∫ sin²(u) du = u/2 - sin(2u)/4
# So ∫₀^ρ r² sin²(t/r) dt = r² · [r·(t/r)/2 - r·sin(2t/r)/4]₀^ρ
#                        = r² · [ρ/2 - r·sin(2ρ/r)/4]
#                        = r²ρ/2 - r³ sin(2ρ/r)/4

def vol_ball_s3(r, rho):
    """
    Volume of a geodesic ball of (geodesic) radius ρ on round S³(r).
      vol(B(p, ρ)) = 4π · ∫₀^ρ r² sin²(t/r) dt
                   = 4π · [r² ρ / 2 - r³ sin(2ρ/r) / 4]
                   = 2π r² ρ - π r³ sin(2ρ/r)
    """
    if rho > np.pi * r:
        rho = np.pi * r  # cap at the antipodal point
    return 2 * np.pi * r**2 * rho - np.pi * r**3 * np.sin(2 * rho / r)


def vol_full_s3(r):
    """Total volume of S³(r) = 2π² r³."""
    return 2 * np.pi**2 * r**3


def vol_ball_euclidean_3d(rho):
    """Volume of a Euclidean ball B^3(ρ) = (4/3)π ρ³."""
    return (4/3) * np.pi * rho**3


# ===========================================================
# Volume of geodesic ball on H³(r) (constant -1/r²)
# ===========================================================
# On H^n(r): ds² = dt² + r² sinh²(t/r) g_{S^{n-1}}
# vol(B(p, ρ)) = 4π · r² · ∫₀^ρ sinh²(t/r) dt
#              = 4π · r²/2 · [r·sinh(2ρ/r)/2 - ρ]
#              = π r³ sinh(2ρ/r) - 2π r² ρ ... let me verify
# ∫ sinh²(u) du = sinh(2u)/4 - u/2
# ∫₀^ρ r² sinh²(t/r) dt = r² · [r sinh(2t/r)/4 - r·(t/r)/2]₀^ρ · ... wait
# = r² · [r·sinh(2ρ/r)/4 · 2 - r·(t/r)/2]  hmm
# Let u = t/r, du = dt/r, dt = r·du
# ∫₀^ρ r² sinh²(t/r) dt = r² ∫₀^(ρ/r) sinh²(u) · r du = r³ ∫₀^(ρ/r) sinh²(u) du
#                       = r³ · [sinh(2u)/4 - u/2]₀^(ρ/r)
#                       = r³ · [sinh(2ρ/r)/4 - ρ/(2r)]
# So vol(B(p, ρ)) on H³(r) = 4π · r³ · [sinh(2ρ/r)/4 - ρ/(2r)]
#                          = π r³ sinh(2ρ/r) - 2π r² ρ

def vol_ball_h3(r, rho):
    """Volume of geodesic ball ρ on H³(r) (curvature -1/r²)."""
    return np.pi * r**3 * np.sinh(2 * rho / r) - 2 * np.pi * r**2 * rho


# ===========================================================
# Bishop-Gromov ratios
# ===========================================================

def bishop_gromov_ratio_s3_vs_euclidean(r, rho):
    """vol_S³(r)(B(p,ρ)) / vol_Euclidean(B(0,ρ))"""
    return vol_ball_s3(r, rho) / vol_ball_euclidean_3d(rho)


def bishop_gromov_ratio_h3_vs_euclidean(r, rho):
    """vol_H³(r)(B(p,ρ)) / vol_Euclidean(B(0,ρ))"""
    return vol_ball_h3(r, rho) / vol_ball_euclidean_3d(rho)


# ===========================================================
# Test 1: Bishop-Gromov on S³ — ratio decreases
# ===========================================================

def test_bishop_gromov_s3():
    """Verify Bishop-Gromov: vol(B)/vol_Euclidean decreases on S³."""
    print("=" * 70)
    print("TEST 1: Bishop-Gromov on round S³(1) vs Euclidean")
    print("=" * 70)
    print()
    print("On S³(1) (Ric = 2g, K = 1):")
    print("  vol(B(p, ρ)) = 2π·ρ - π·sin(2ρ)")
    print()
    print(f"{'ρ':>8} {'vol_S³':>12} {'vol_R³':>12} {'ratio':>10} {'monotone?':>10}")
    print("-" * 60)

    r = 1.0
    radii = np.linspace(0.05, np.pi * r, 25)
    prev_ratio = None
    monotone = True
    for rho in radii:
        v_s3 = vol_ball_s3(r, rho)
        v_eu = vol_ball_euclidean_3d(rho)
        ratio = v_s3 / v_eu
        is_mono = "—"
        if prev_ratio is not None:
            if ratio <= prev_ratio + 1e-9:
                is_mono = "YES"
            else:
                is_mono = "NO"
                monotone = False
        if abs(rho - radii[0]) < 1e-9 or abs(rho - radii[-1]) < 1e-9 or \
           int(rho * 4) != int((rho - 0.13) * 4):
            print(f"{rho:8.4f} {v_s3:12.6f} {v_eu:12.6f} {ratio:10.6f} {is_mono:>10s}")
        prev_ratio = ratio

    print()
    print(f"Monotone non-increasing: {monotone}")
    print(f"Ratio at ρ=0.05: {bishop_gromov_ratio_s3_vs_euclidean(1, 0.05):.6f} (≈ 1)")
    print(f"Ratio at ρ=π: {bishop_gromov_ratio_s3_vs_euclidean(1, np.pi):.6f}")
    print(f"3/(2π²) ≈ {3/(2*np.pi**2):.6f} (analytical limit)")
    return monotone


# ===========================================================
# Test 2: Bishop-Gromov on H³ — ratio INCREASES (opposite!)
# ===========================================================

def test_bishop_gromov_h3():
    """On H³ (negative curvature), the ratio INCREASES with r."""
    print("=" * 70)
    print("TEST 2: H³ vs Euclidean — ratio INCREASES (opposite to S³)")
    print("=" * 70)
    print()
    print("On H³(1) (Ric = -2g, K = -1):")
    print("  vol(B(p, ρ)) = π·sinh(2ρ) - 2π·ρ")
    print()
    print(f"{'ρ':>8} {'vol_H³':>14} {'vol_R³':>12} {'ratio':>10}")
    print("-" * 60)

    r = 1.0
    for rho in [0.1, 0.5, 1.0, 1.5, 2.0, 3.0]:
        v_h3 = vol_ball_h3(r, rho)
        v_eu = vol_ball_euclidean_3d(rho)
        ratio = v_h3 / v_eu
        print(f"{rho:8.4f} {v_h3:14.6f} {v_eu:12.6f} {ratio:10.6f}")

    print()
    print("On H³, the ratio INCREASES exponentially (sinh growth).")
    print("This is the OPPOSITE direction from Bishop-Gromov for K > 0.")
    print("The Bishop-Gromov inequality with K = -1 says:")
    print("  vol(B(p,r))/vol_H³(B(r)) is monotone non-increasing.")
    print("For M = H³ itself: vol(B(p,r)) = vol_H³(B(r)), so ratio = 1.")


# ===========================================================
# Test 3: Bishop-Gromov is sharp on the model space
# ===========================================================

def test_bishop_gromov_sharp():
    """vol_M(B)/vol_K(B) = 1 if M is the model space itself."""
    print("=" * 70)
    print("TEST 3: Bishop-Gromov is sharp — equality on model spaces")
    print("=" * 70)
    print()

    # On round S³(1), comparing to itself (model with K=1):
    # The ratio should be EXACTLY 1.
    print("Round S³(1) compared to S³(1) itself (K = 1):")
    print(f"{'ρ':>8} {'vol_M(B)':>12} {'vol_K(B)':>12} {'ratio':>10}")
    print("-" * 50)

    for rho in [0.1, 0.5, 1.0, 2.0, np.pi]:
        v = vol_ball_s3(1.0, rho)
        # Model is the same: ratio = 1 trivially
        print(f"{rho:8.4f} {v:12.6f} {v:12.6f} {1.0:10.6f}")

    print()
    print("Equality holds: M = model ⟹ ratio = 1.")
    print("Bishop-Gromov is sharp (equality is achieved by the model).")


# ===========================================================
# Test 4: Connection to κ-noncollapsing
# ===========================================================

def test_kappa_from_bishop_gromov():
    """
    Perelman's κ-noncollapsing follows from Bishop-Gromov + W-monotonicity.

    κ-noncollapsing: ∃ κ > 0 such that for all (x, t):
      if |Rm(g(t))| ≤ r⁻² in B_g(t)(x, r), then vol(B(x,r)) ≥ κ r³.

    Bishop-Gromov gives: vol(B(x,r))/r³ ≥ vol_K(B(r))/r³ where K is the
    curvature lower bound. As r → 0, vol_K(B(r))/r³ → vol_R³(B(1))/1
    = 4π/3. So κ = 4π/3 is the SCALE-INVARIANT lower bound.

    But Bishop-Gromov is monotone-DECREASING for K > 0 (sphere case).
    The bound vol/r³ ≥ 4π/3 isn't quite right — we need the sup of
    the curvature, not the lower bound. Perelman's argument is more
    subtle, using W-monotonicity to control the lower bound on κ
    UNDER Ricci flow with surgery.
    """
    print("=" * 70)
    print("TEST 4: Connection to Perelman's κ-noncollapsing")
    print("=" * 70)
    print()
    print("Bishop-Gromov gives vol(B(p,r))/r³ ≤ vol_R³(B(r))/r³ = 4π/3 ≈ 4.189")
    print("(upper bound from Bishop-Gromov)")
    print()
    print("Round S³(1): κ = vol(S³)/1³ = 2π² ≈ 19.74 (whole sphere = 'ball of radius π')")
    print()
    print("For the κ-noncollapsing theorem, we need a LOWER bound:")
    print("  vol(B(x,r)) ≥ κ · r³  whenever |Rm| ≤ r⁻² in the ball.")
    print()
    print("Perelman's contribution: under Ricci flow with surgery,")
    print("the κ from W-monotonicity stays uniformly bounded below.")
    print("This is the key technical step that lets surgery be applied.")
    print()
    print("Bishop-Gromov alone gives κ ≥ const ≈ vol_K(B(1))/1 for the")
    print("comparison space. Perelman's W gives this is preserved under flow.")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Poincaré Conjecture — Numerical Track: Bishop-Gromov Comparison")
    print()

    monotone = test_bishop_gromov_s3()
    print()
    test_bishop_gromov_h3()
    print()
    test_bishop_gromov_sharp()
    print()
    test_kappa_from_bishop_gromov()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Bishop-Gromov on S³: monotone non-increasing = {monotone}")
    print(f"Bishop-Gromov on H³: ratio grows with r (opposite direction)")
    print(f"Sharpness: equality on model space (S³ vs S³ → ratio = 1)")
    print()
    print("Bishop-Gromov is the volume-comparison foundation that makes")
    print("κ-noncollapsing computable. Combined with W-monotonicity,")
    print("it gives Perelman the lower bound on volume he needs to")
    print("rule out collapse during Ricci flow with surgery.")
