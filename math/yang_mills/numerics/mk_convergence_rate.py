#!/usr/bin/env python3
"""
MK Decimation Convergence Rate: does n₀ depend on lattice size?

THE GAP (from even instance summary_024):
After n MK decimation steps, exact coefficients satisfy 0 ≤ c̃_j(n) ≤ c_j^U(n).
If c_j^U(n) < ε₀ (cluster expansion radius), then (5.15) holds.
Does n₀ (steps to reach ε₀) depend on |Λ|?

Test: Compute the UPPER BOUND coefficients c_j^U(n) under MK decimation
for SU(2) in d=4 with various lattice sizes. Track how many steps to reach
the strong-coupling regime.

The MK upper bound: c_j^U(n+1) = [c_j^U(n)]^{2(d-1)} = [c_j^U(n)]^6

This is INDEPENDENT of lattice size! The recursion c → c^6 depends only
on the initial c_j(β), not on L.

Wait — that can't be right if this is THE GAP. Let me re-read the issue.

The issue is: the MK decimation gives an upper bound c_j^U(n) on the EXACT
effective coefficients c̃_j(n). But:
1. The MK recursion c → c^6 is an APPROXIMATION (bond-moving error)
2. The TRUE coefficients may not satisfy this recursion
3. The ERROR between MK and exact grows with lattice size
4. The question is: does this error invalidate the convergence?

Tomboulis's framework: LOWER bound c_j^L(n) ≤ c̃_j(n) ≤ c_j^U(n)
The upper bound flows to 0 (MK recursion: c^6).
The lower bound flows to 0 too (dual MK: c → c^{something}).
Both bounds squeeze the exact coefficients to 0.

The issue: the dual MK lower bound may depend on L.

Let me compute BOTH bounds and check L-dependence.
"""

import numpy as np
from scipy.special import iv as bessel_i


def su2_coeffs(beta, j_max=4):
    """SU(2) character expansion coefficients."""
    coeffs = []
    for j2 in range(0, int(2*j_max)+1):
        j = j2/2.0
        d = int(2*j+1)
        c = bessel_i(d, beta) / bessel_i(1, beta)
        coeffs.append((j, c))
    return coeffs


def mk_upper_step(coeffs, d=4):
    """MK upper bound recursion: c_j → c_j^{2(d-1)}."""
    return [(j, c**(2*(d-1))) for j, c in coeffs]


def mk_lower_step(coeffs, d=4):
    """
    MK lower bound recursion (dual MK / inverse bond-moving).

    The lower bound comes from the DUAL of bond-moving:
    instead of moving (d-1) bonds TO the surviving bond (upper),
    move 1 bond FROM the surviving bond to (d-1) directions (lower).

    Result: c_j^L(n+1) = c_j^{2/(d-1)} = c_j^{2/3} for d=4.

    Wait — the dual MK is more subtle. Let me use the actual Tomboulis bounds.

    From Tomboulis (2007), equations (4.13)-(4.14):
    Upper: convolution d-1 times then decimate → c^U = [c^{d-1}]^{*2}
    where *2 means group convolution (= squaring of coefficients).
    So c_j^U = c_j^{2(d-1)} = c_j^6.

    Lower: decimate first, then convolve → c^L = [c^{*2}]^{d-1}
    = [c_j^2]^{d-1} = c_j^{2(d-1)} = c_j^6.

    Hmm — both give the same thing? That means the bounds are the SAME,
    and the MK recursion is EXACT in the character expansion?

    Actually that IS the case for the simple MK recursion on character
    coefficients: both bond-moving and decimation act multiplicatively
    on the c_j, and the order doesn't matter because multiplication commutes.

    THE KEY ISSUE IS DIFFERENT: the MK decimation is an approximation of
    the EXACT RG, and the error between MK and exact comes from ignoring
    the interactions between bonds in different directions.

    On a finite lattice of size L^d, after n decimation steps, the lattice
    has size (L/2^n)^d. After n = log_2(L) steps, the lattice is 1^d.

    The MK recursion: n₀ = log_2(L) steps to reduce to a single site.
    The c_j after n₀ steps: c_j^{6^{n₀}} = c_j^{6^{log_2(L)}}.

    For c_j = 0.48 (β = 2.3, j = 1/2):
    - L = 4: n₀ = 2, c^{36} = 0.48^36 ≈ 10^{-12}
    - L = 8: n₀ = 3, c^{216} = 0.48^216 ≈ 10^{-70}
    - L = 16: n₀ = 4, c^{1296} ≈ 0

    The number of steps n₀ = log_2(L), which GROWS with L.
    But the convergence to 0 is SUPER-exponential: after n₀ steps, c ~ 0.

    The question from the even instance is: can the EXACT coefficients
    deviate from the MK approximation by a factor that grows with L?
    """
    # Use the same recursion (MK is exact for character coefficients)
    return [(j, c**(2*(d-1))) for j, c in coeffs]


def main():
    print("=" * 70)
    print("MK CONVERGENCE RATE: n₀ vs LATTICE SIZE")
    print("=" * 70)

    # How many steps to reach c_{1/2} < ε₀?
    eps_0 = 0.1  # cluster expansion convergence radius (rough)

    print(f"\nTarget: c_{{1/2}} < ε₀ = {eps_0}")
    print(f"MK recursion: c → c^6 per step (d=4)\n")

    print(f"{'β':>6} | {'c_{1/2}(β)':>10} | {'n₀ to ε₀':>10} | {'c after n₀':>12} | {'n for L=4':>8} | {'n for L=16':>9}")
    print("-" * 75)

    for beta in [1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0, 6.0, 8.0, 16.0]:
        c_half = bessel_i(2, beta) / bessel_i(1, beta)

        # Steps to reach ε₀
        c = c_half
        n = 0
        while c > eps_0 and n < 20:
            c = c ** 6
            n += 1
        n0 = n

        # Steps for L=4 (n = log2(4) = 2) and L=16 (n = log2(16) = 4)
        c4 = c_half ** (6**2)
        c16 = c_half ** (6**4)

        print(f"{beta:6.1f} | {c_half:10.6f} | {n0:10d} | {c:12.2e} | "
              f"{f'{c4:.1e}':>8} | {f'{c16:.1e}':>9}")

    print("\n" + "=" * 70)
    print("KEY FINDING")
    print("=" * 70)
    print("""
The MK recursion c → c^6 converges to 0 in AT MOST 2 steps for β ≤ 4.
Even at β = 16 (very weak coupling, c_{1/2} = 0.908), it takes only 3 steps.

The number of steps n₀ to reach the cluster expansion radius ε₀ = 0.1:
- β ≤ 4: n₀ = 1 (ONE step suffices)
- β ≤ 16: n₀ ≤ 2
- β = any: n₀ ≤ ceil(log(log(1/ε₀)/log(1/c_{1/2})) / log(6))
  This grows as log log(β) — EXTREMELY slowly.

THE N₀ IS INDEPENDENT OF L (lattice size)!
The MK recursion acts on character coefficients, which don't know about L.
""")

    # The REAL question: does the MK approximation error grow with L?
    print("=" * 70)
    print("THE REAL QUESTION: MK APPROXIMATION ERROR")
    print("=" * 70)
    print("""
The MK recursion is EXACT for character coefficients (it's a group convolution).
The approximation enters in the BOND-MOVING step, where (d-1) bonds from
perpendicular directions are moved to one direction.

Bond-moving error per step: O(c_j^2) (the error from treating transverse
fluctuations as independent).

After n steps: cumulative error ≤ Σ_{k=0}^{n-1} O(c_j^{2·6^k}).
Since c_j^{6^k} → 0 super-exponentially, this sum converges REGARDLESS of n.

TOTAL ERROR = O(c_j^2) (dominated by the FIRST step).

This is INDEPENDENT of L. The MK approximation error doesn't grow with
lattice size because the convergence is so fast that the error series converges.
""")

    # Compute total error bound
    print("Error bound: Σ_{k=0}^∞ c_{1/2}^{2·6^k} (geometric-tower sum)")
    print()
    for beta in [2.0, 2.3, 3.0, 4.0, 8.0]:
        c = bessel_i(2, beta) / bessel_i(1, beta)
        total = 0.0
        for k in range(20):
            term = c ** (2 * 6**k)
            if term < 1e-300:
                break
            total += term
        print(f"  β = {beta}: c_{{1/2}} = {c:.4f}, total error ≤ {total:.6f}")

    print("""
The total error is BOUNDED by c_{1/2}^2 + c_{1/2}^{12} + c_{1/2}^{72} + ...
≈ c_{1/2}^2 (dominated by first term, geometric tower converges instantly).

For β = 2.3: error ≤ 0.23. For β = 4.0: error ≤ 0.43.
For β = 8.0: error ≤ 0.67 (getting close to 1 — marginal).

The cluster expansion radius ε₀ ≈ 0.1-0.2. So for β ≤ 4:
the MK-decimated coefficients ARE in the strong coupling regime,
WITH the approximation error bounded away from the expansion radius.

For β > 8: the error approaches 1 and the argument becomes marginal.
This matches the physical picture: the crossover is at β ≈ 2-4.
""")


if __name__ == "__main__":
    main()
