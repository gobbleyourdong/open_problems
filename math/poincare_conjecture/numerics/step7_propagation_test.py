#!/usr/bin/env python3
"""
Step 7 propagation test: Does F_v > 0 survive MK decimation backwards?

The proof (attempt_028) shows F_v > 0 at step n₀ (cluster expansion).
Step 7 asks: does F_v > 0 at step n₀ imply F_v > 0 at step 0?

Test: Compute the EXACT vortex free energy F_v(β) on the 2D torus
(where we have exact formulas), then apply MK decimation and check
F_v at each step. If F_v is monotonically increasing under decimation
(toward strong coupling), then F_v(0) ≤ F_v(n₀) and the propagation
works in the CORRECT direction.

Key insight: MK decimation flows toward STRONG coupling, where F_v is LARGE.
So F_v should INCREASE under decimation, not decrease.
If F_v(step 0) ≤ F_v(step 1) ≤ ... ≤ F_v(step n₀), then
F_v(step 0) > 0 follows from F_v(step n₀) > 0.

BUT: the MK decimation is NOT the exact RG. The exact RG might behave
differently. This test checks the MK approximation to see if the
monotonicity is at least approximately correct.
"""

import numpy as np
from scipy.special import iv as bessel_i


def su2_coeffs(beta, j_max=6):
    coeffs = {}
    for j2 in range(0, int(2*j_max)+1):
        j = j2/2.0
        d = int(2*j+1)
        coeffs[j] = bessel_i(d, beta) / bessel_i(1, beta)
    return coeffs


def F_v_from_coeffs(coeffs, L):
    """
    Compute F_v = ln(Z_per/Z_anti) on L×L 2D torus.
    Z = Σ_j c_j^{L²}, Z⁻ = Σ_j (-1)^{2j} c_j^{L²}
    """
    F = L * L
    Z_per = sum(c**F for j, c in coeffs.items())
    Z_anti = sum(((-1)**int(2*j)) * c**F for j, c in coeffs.items())
    if Z_anti <= 0:
        return float('inf'), Z_per, Z_anti
    return np.log(Z_per / Z_anti), Z_per, Z_anti


def F_v_single_plaquette(coeffs):
    """
    Single-plaquette vortex cost: F_v = ln(S_per/S_anti).
    S_per = Σ_j d_j c_j, S_anti = Σ_j d_j (-1)^{2j} c_j.
    """
    S_per = sum((2*j+1) * c for j, c in coeffs.items())
    S_anti = sum((2*j+1) * ((-1)**int(2*j)) * c for j, c in coeffs.items())
    if S_anti <= 0:
        return float('inf'), S_per, S_anti
    return np.log(S_per / S_anti), S_per, S_anti


def mk_step(coeffs):
    """MK decimation: c_j → c_j^6 (d=4, b=2)."""
    return {j: c**6 for j, c in coeffs.items()}


def main():
    print("=" * 70)
    print("STEP 7 TEST: F_v MONOTONICITY UNDER MK DECIMATION")
    print("=" * 70)
    print()
    print("If F_v increases under MK (toward strong coupling):")
    print("  F_v(step 0) ≤ F_v(step n₀) and since F_v(n₀) > 0 (cluster exp),")
    print("  this does NOT help (wrong direction).")
    print()
    print("If F_v decreases under MK but stays > 0:")
    print("  F_v(step 0) ≥ F_v(step 1) ≥ ... ≥ F_v(n₀) > 0.")
    print("  Then F_v(0) > 0 follows! This is what we NEED.")
    print()

    # Single-plaquette F_v under MK
    print("--- Single-plaquette F_v under MK decimation ---")
    print(f"{'β':>6} | {'step 0':>10} | {'step 1':>10} | {'step 2':>10} | {'Direction':>10}")
    print("-" * 55)

    for beta in [1.0, 1.5, 2.0, 2.3, 3.0, 4.0, 6.0, 8.0]:
        coeffs = su2_coeffs(beta)
        fvs = []
        c = dict(coeffs)
        for step in range(3):
            fv, _, _ = F_v_single_plaquette(c)
            fvs.append(fv)
            c = mk_step(c)

        direction = "DECREASING" if fvs[0] > fvs[1] else "INCREASING"
        print(f"{beta:6.1f} | {fvs[0]:10.4f} | {fvs[1]:10.4f} | {fvs[2]:10.4f} | {direction:>10}")

    # 2D torus F_v under MK
    print("\n--- 2D Torus (L=3, odd) F_v under MK ---")
    print(f"{'β':>6} | {'step 0':>10} | {'step 1':>10} | {'step 2':>10} | {'Direction':>10}")
    print("-" * 55)

    for beta in [1.0, 2.0, 3.0, 4.0, 8.0]:
        coeffs = su2_coeffs(beta)
        fvs = []
        c = dict(coeffs)
        for step in range(3):
            fv, _, _ = F_v_from_coeffs(c, L=3)
            fvs.append(fv)
            c = mk_step(c)

        direction = "DECREASING ✓" if fvs[0] >= fvs[1] - 1e-10 else "INCREASING ✗"
        print(f"{beta:6.1f} | {fvs[0]:10.4f} | {fvs[1]:10.4f} | {fvs[2]:10.4f} | {direction:>12}")

    # THE KEY TEST: Is F_v(original) > F_v(decimated)?
    print("\n--- THE KEY QUESTION ---")
    print("Does MK decimation INCREASE or DECREASE F_v?")
    print()
    print("If F_v decreases: propagation works (F_v(0) ≥ F_v(n₀) > 0)")
    print("If F_v increases: propagation goes wrong direction")
    print()

    # Deeper analysis: what happens to σ = F_v / Area under MK?
    print("--- String tension σ per plaquette under MK ---")
    print(f"{'β':>6} | {'σ(step 0)':>10} | {'σ(step 1)':>10} | {'σ(step 2)':>10}")
    print("-" * 45)

    for beta in [1.0, 2.0, 2.3, 3.0, 4.0, 8.0, 16.0]:
        coeffs = su2_coeffs(beta)
        sigmas = []
        c = dict(coeffs)
        for step in range(3):
            fv, sp, sa = F_v_single_plaquette(c)
            sigmas.append(fv)
            c = mk_step(c)
        print(f"{beta:6.1f} | {sigmas[0]:10.4f} | {sigmas[1]:10.4f} | {sigmas[2]:10.4f}")

    # The answer
    print("\n" + "=" * 70)
    print("FINDING")
    print("=" * 70)
    print("""
F_v INCREASES under MK decimation (toward strong coupling).
This means: F_v(step 0) < F_v(step 1) < ... < F_v(step n₀).

This is the WRONG DIRECTION for direct propagation!
We can't conclude F_v(0) > 0 from F_v(n₀) > 0 using monotonicity.

HOWEVER: this makes physical sense. At strong coupling (after many MK steps),
the vortex cost is HUGE (F_v ~ -ln(c_{1/2}) → ∞). At the original coupling,
the vortex cost is SMALLER but still positive.

The proof needs a DIFFERENT argument for Step 7:
(a) Show F_v > 0 at step 0 directly (not via decimation), or
(b) Use the MK LOWER bound (not upper) to show F_v(0) ≥ F_v^L > 0, or
(c) Use the Z₂ symmetry (attempt_019) to avoid Step 7 entirely.

OPTION (c) is most promising: for EVEN L, Z_per = Z_anti by Z₂ symmetry,
so F_v = 0 (not > 0). The inequality (5.15) becomes an equality.
For ODD L: F_v > 0 by explicit computation (the half-integer sector
contributes with a definite sign).

Actually wait — F_v = 0 for even L means the vortex is FREE (no cost).
That contradicts confinement! Let me recheck...
""")

    # Recheck: is F_v really 0 for even L?
    print("--- F_v for even vs odd L (2D torus, β=2.0) ---")
    for L in range(2, 9):
        coeffs = su2_coeffs(2.0)
        fv, Zp, Za = F_v_from_coeffs(coeffs, L)
        print(f"  L={L}: F_v = {fv:.8f}, Z_per = {Zp:.8e}, Z_anti = {Za:.8e}")


if __name__ == "__main__":
    main()
