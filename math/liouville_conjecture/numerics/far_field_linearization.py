#!/usr/bin/env python3
"""
Far-Field Linearization Test — Theory Track Urgent Request

From SCRATCHPAD Apr 10 09:20: verify that |(u·∇)u| / |Δu| → 0 as |x| → ∞
for a BOUNDED NS-like velocity field. This justifies treating the far field
as approximately solving the heat equation.

Burgers won't work (unbounded: u_z = αz). Need a bounded test case.

Test cases:
1. Lamb-Oseen vortex at fixed t (bounded, decays as 1/r at ∞)
2. A bounded smooth compactly-supported vorticity (constructed explicitly)
3. The Gaussian vortex ring (bounded, decays exponentially)

The ratio |(u·∇)u| / |Δu| should → 0 as |x| → ∞ for bounded flows
because ∇u decays (parabolic regularity) while Δu may also decay but
the nonlinear term has an EXTRA factor of |u| ≤ M times ∇u.
"""

import numpy as np


# ===========================================================
# Test 1: Lamb-Oseen at fixed t (2D, embedded in 3D)
# ===========================================================
# u_θ(r) = Γ/(2πr) (1 - e^{-r²/σ²}) with σ² = 4νt
# u_r = u_z = 0
# This is bounded: max u_θ ~ Γ/(2π·σ·e^{1/2}) at r = σ
# Decays as 1/r at infinity

def lamb_oseen_test():
    """Test the nonlinear/linear ratio on Lamb-Oseen."""
    print("=" * 70)
    print("TEST 1: Lamb-Oseen vortex (2D, bounded)")
    print("=" * 70)
    print()

    Gamma = 1.0
    nu = 1.0
    t = 1.0
    sigma2 = 4 * nu * t

    def u_theta(r):
        if r < 1e-10:
            return 0.0
        return Gamma / (2 * np.pi * r) * (1 - np.exp(-r**2 / sigma2))

    def du_dr(r):
        """∂u_θ/∂r"""
        if r < 1e-10:
            return Gamma / (2 * np.pi * sigma2)
        exp_term = np.exp(-r**2 / sigma2)
        return -Gamma / (2 * np.pi * r**2) * (1 - exp_term) + \
               Gamma / (2 * np.pi * r) * (2 * r / sigma2) * exp_term

    def laplacian_u_theta(r):
        """Δu_θ - u_θ/r² (the relevant Laplacian for cylindrical)"""
        if r < 1e-10:
            return 0.0
        # Δu_θ = d²u/dr² + (1/r)du/dr - u/r²
        # For Lamb-Oseen: Δu_θ = -(Γ/(πσ⁴)) r exp(-r²/σ²) (from direct computation)
        return -Gamma / (np.pi * sigma2**2) * r * np.exp(-r**2 / sigma2)

    print(f"Γ = {Gamma}, ν = {nu}, σ² = {sigma2}")
    print(f"max|u_θ| ≈ {Gamma / (2*np.pi*np.sqrt(sigma2)*np.e**0.5):.4f} at r ≈ {np.sqrt(sigma2):.2f}")
    print()

    print(f"{'r':>8} {'|u|':>10} {'|∇u|':>10} {'|(u·∇)u|':>12} {'|Δu|':>10} {'ratio':>10}")
    print("-" * 65)

    for r in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]:
        u = abs(u_theta(r))
        grad_u = abs(du_dr(r))
        # (u·∇)u in cylindrical for pure azimuthal flow: -u_θ²/r ê_r
        nonlinear = u**2 / r if r > 0 else 0
        # Δu component
        lap = abs(laplacian_u_theta(r))

        ratio = nonlinear / lap if lap > 1e-30 else float('inf')
        print(f"{r:8.1f} {u:10.6f} {grad_u:10.6f} {nonlinear:12.6e} {lap:10.6e} {ratio:10.4f}")

    print()
    print("KEY: at large r, |u| ~ 1/r, |(u·∇)u| ~ 1/r³, |Δu| ~ r·exp(-r²/σ²)")
    print("The ratio |(u·∇)u|/|Δu| = (1/r³)/(r·exp(-r²)) = exp(r²)/r⁴ → ∞!")
    print()
    print("WAIT — Lamb-Oseen has exponentially decaying Laplacian but algebraically")
    print("decaying nonlinearity. The ratio DIVERGES at large r.")
    print()
    print("This means: the far-field linearization FAILS for Lamb-Oseen!")
    print("The nonlinear term DOMINATES the Laplacian at large r.")
    print()
    print("BUT: this is because Lamb-Oseen has u ~ 1/r (slow algebraic decay).")
    print("For a solution with u → const at infinity, both terms would be smaller.")


# ===========================================================
# Test 2: Bounded flow with CONSTANT far-field value
# ===========================================================
# u(x) = ū + w(x) where w is compactly supported or exponentially decaying
# At |x| > R: u ≈ ū (constant), so (u·∇)u ≈ 0, Δu ≈ 0
# The ratio is 0/0 — ill-defined but harmless (both terms negligible)

def bounded_constant_farfield():
    """For bounded flows approaching a constant at ∞."""
    print("=" * 70)
    print("TEST 2: Bounded flow with u → ū at |x| → ∞")
    print("=" * 70)
    print()
    print("If u = ū + w(x) with w exponentially decaying:")
    print("  |w(x)| ≤ A exp(-|x|²/L²)")
    print("  |(u·∇)u| = |(ū + w)·∇w| ≤ (M + A)·|∇w| ≤ C exp(-|x|²/L²)/L")
    print("  |Δu| = |Δw| ≤ C exp(-|x|²/L²)/L²")
    print()
    print("Ratio: |(u·∇)u|/|Δu| ≤ (M + A)·L / 1 = (M + A)·L")
    print()
    print("This is BOUNDED (not → 0). The nonlinear term is of the SAME ORDER")
    print("as the Laplacian in the far field — both decay exponentially.")
    print()

    M = 1.0  # bound on |u|
    L = 1.0  # decay scale

    print(f"{'|x|':>8} {'|w|':>10} {'|(u·∇)u|':>12} {'|Δu|':>12} {'ratio':>10}")
    print("-" * 55)

    for x in [1.0, 2.0, 5.0, 10.0, 20.0]:
        w = np.exp(-x**2 / L**2)
        grad_w = 2 * x / L**2 * w
        nonlinear = (M + w) * grad_w  # |(ū + w)·∇w|
        laplacian = (4 * x**2 / L**4 - 2 / L**2) * w  # |Δ(exp(-x²/L²))|
        laplacian = abs(laplacian)
        ratio = nonlinear / laplacian if laplacian > 1e-30 else float('inf')
        print(f"{x:8.1f} {w:10.6f} {nonlinear:12.6e} {laplacian:12.6e} {ratio:10.4f}")

    print()
    print("The ratio stays O(1) — not → 0.")
    print()
    print("CORRECTION to the theory track's chain:")
    print("Step 2 says |(u·∇)u| ≤ M·C(M)/R → 0. This is TRUE for |∇u| ~ 1/R")
    print("But BOTH the nonlinear term AND the Laplacian decay at the same rate.")
    print("The RATIO doesn't → 0 — both terms are small, but comparably small.")
    print()
    print("For the linearization to work, we need:")
    print("  |(u·∇)u| << |∂u/∂t - Δu|  (nonlinear << parabolic part)")
    print("If u = ū + w with small w: |(u·∇)u| ~ M|∇w| while |Δw| ~ |∇²w|.")
    print("The ratio is M·|∇w|/|∇²w| ~ M·L (where L is the gradient scale).")
    print("For this < 1: need L < 1/M (the gradient scale must be smaller than 1/M).")
    print()
    print("On R³ at large |x|: parabolic regularity gives |∇w| ≤ C/|x| (at best).")
    print("So L ~ |x| and the ratio ~ M·|x|. This GROWS — linearization FAILS at ∞.")
    print()
    print("THE ACTUAL SITUATION:")
    print("The far-field linearization step (theory chain step 3) is NOT automatic.")
    print("The nonlinear term is comparable to the Laplacian at all distances.")
    print("The error is O(M/R) × O(C(M)/R) = O(M·C(M)/R²), and the Laplacian")
    print("is O(C(M)/R²). The RATIO is O(M) — bounded but not small.")


# ===========================================================
# The honest assessment
# ===========================================================

def honest_assessment():
    """What the numerics say about the theory track's chain."""
    print("=" * 70)
    print("HONEST ASSESSMENT FOR THEORY TRACK")
    print("=" * 70)
    print()
    print("The 7-step chain from SCRATCHPAD (Apr 10, 09:20):")
    print()
    print("Step 1: |∇u| ≤ C(M)/R at far field ← TRUE (parabolic regularity)")
    print("Step 2: |(u·∇)u| ≤ M·C(M)/R → 0 ← TRUE (both factors bounded)")
    print("Step 3: u approximately heat equation at large |x| ← PROBLEMATIC")
    print("  The nonlinear term is O(M·C(M)/R), but so is |Δu|.")
    print("  The RATIO |(u·∇)u|/|Δu| does NOT → 0.")
    print("  Both terms decay at the same rate.")
    print()
    print("Step 4: Bounded ancient heat → constant ← TRUE (classical)")
    print("Step 5: u → const at ∞ ← DOES NOT FOLLOW from step 3")
    print()
    print("THE GAP in the chain: step 3 → step 5.")
    print("The nonlinear term is SMALL at large |x|, but it's the SAME SIZE")
    print("as the linear term. You can't drop it.")
    print()
    print("HOWEVER: the chain might still work via a PERTURBATIVE argument.")
    print("Write u = ū + w. At large |x|: w satisfies")
    print("  ∂w/∂t = Δw + (w·∇)w + (ū·∇)w + (w·∇)ū")
    print("Since ū is constant: (ū·∇)w is just advection (removable by Galilean).")
    print("(w·∇)ū = 0. So w satisfies:")
    print("  ∂w/∂t = Δw + (w·∇)w  (the same equation as u!)")
    print()
    print("The ancient condition + Koch-Tataru: if ||w||_∞ < ε₀ somewhere,")
    print("then w = 0. But this is the ORIGINAL problem (backward entry).")
    print()
    print("CONCLUSION: the far-field route doesn't shortcut the problem.")
    print("The nonlinearity at infinity is just as hard as at the origin.")
    print("Agent 4's pressure-gauge obstruction is REAL and cannot be")
    print("bypassed by far-field linearization.")


if __name__ == "__main__":
    print("Liouville — Far-Field Linearization Test")
    print()
    lamb_oseen_test()
    print()
    bounded_constant_farfield()
    print()
    honest_assessment()
