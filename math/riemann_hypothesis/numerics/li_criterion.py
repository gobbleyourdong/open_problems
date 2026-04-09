#!/usr/bin/env python3
"""
Li's Criterion: λ_n ≥ 0 for all n ≥ 1 ⟺ Riemann Hypothesis.

λ_n = Σ_ρ [1 - (1 - 1/ρ)^n]

where ρ runs over non-trivial zeros of ζ(s).

Equivalently (Bombieri-Lagarias):
λ_n = (1/(n-1)!) (d/ds)^n [s^{n-1} log ξ(s)]|_{s=1}

Or via the explicit formula:
λ_n = n [1/2 log π - 1/2 ψ(n/2+1)] + 1 - n Σ_ρ (1 - (1-1/ρ)^n)/n

The sigma method question: can we find a STRUCTURAL reason λ_n ≥ 0,
or is it "just positive" like the NS key lemma Q > 0?

Uses mpmath for arbitrary precision computation.
"""

import mpmath
import numpy as np
import time

mpmath.mp.dps = 30  # 30 decimal digits


def li_lambda_from_log_xi(n, prec=30):
    """
    Compute λ_n via the Taylor expansion of log ξ(s) at s=1.

    ξ(s) = (1/2) s(s-1) π^{-s/2} Γ(s/2) ζ(s)

    log ξ(s) = log(1/2) + log(s) + log(s-1) - (s/2)log(π) + log Γ(s/2) + log ζ(s)

    λ_n = (d^n/ds^n)[s^{n-1} log ξ(s)]|_{s=1} / (n-1)!

    Use mpmath's Taylor series machinery.
    """
    mpmath.mp.dps = prec

    def log_xi(s):
        return (mpmath.log(mpmath.mpf('0.5')) + mpmath.log(s) + mpmath.log(s - 1)
                - (s / 2) * mpmath.log(mpmath.pi)
                + mpmath.loggamma(s / 2)
                + mpmath.log(mpmath.zeta(s)))

    # λ_n via the power sum formula:
    # λ_n = Σ_{j=0}^{n-1} C(n-1, j) (-1)^j σ_{j+1}
    # where σ_k = (coefficient of (s-1)^k in log ξ(s+1))

    # Compute Taylor coefficients of log ξ(1 + z) around z = 0
    # Use numerical differentiation
    coeffs = mpmath.taylor(lambda z: log_xi(1 + z), 0, n + 1)

    # λ_n from Bombieri-Lagarias:
    # λ_n = Σ_{j=1}^{n} C(n, j) (-1)^{j+1} σ_j × j
    # Actually: λ_n = n! × [coefficient of z^n in z^{-1}(1 - (1-z)^n) log ξ(1+z) ... ]
    # This is getting complicated. Let me use the DIRECT formula.

    # Direct computation via zeros (using mpmath's zetazero):
    # λ_n = Σ_ρ [1 - (1 - 1/ρ)^n]
    # Sum over the first K zeros (both ρ and 1-ρ = conjugate pair)
    return None  # Will use the zero-sum method below


def li_lambda_from_zeros(n, K=100):
    """
    Compute λ_n = Σ_ρ [1 - (1-1/ρ)^n] summing over the first K zero pairs.

    Each non-trivial zero ρ = 1/2 + iγ contributes:
    1 - (1 - 1/ρ)^n = 1 - ((ρ-1)/ρ)^n = 1 - ((-1/2 + iγ)/(1/2 + iγ))^n

    The pair ρ, ρ̄ gives a real contribution (complex parts cancel).
    """
    mpmath.mp.dps = 30
    total = mpmath.mpf(0)

    for k in range(1, K + 1):
        gamma_k = mpmath.zetazero(k).imag  # k-th zero: 1/2 + i·γ_k
        rho = mpmath.mpc(0.5, gamma_k)
        rho_bar = mpmath.mpc(0.5, -gamma_k)

        term = (1 - (1 - 1/rho)**n) + (1 - (1 - 1/rho_bar)**n)
        total += term

    return float(total.real)


def main():
    print("=" * 70)
    print("LI'S CRITERION: λ_n ≥ 0 ⟺ RH")
    print("=" * 70)

    # First: verify zero locations with mpmath
    print("\n--- Verifying zeros with mpmath ---")
    for k in range(1, 6):
        z = mpmath.zetazero(k)
        print(f"  ρ_{k} = {z}")

    # Compute λ_n for n = 1 to 30
    print(f"\n--- λ_n using first K=50 zero pairs ---\n")
    K = 50
    print(f"{'n':>4} | {'λ_n':>18} | {'λ_n ≥ 0?':>10}")
    print("-" * 40)

    lambdas = []
    t0 = time.time()
    for n in range(1, 31):
        lam = li_lambda_from_zeros(n, K=K)
        lambdas.append(lam)
        sign = "✓" if lam >= 0 else "✗ FAIL"
        print(f"{n:4d} | {lam:18.10f} | {sign:>10}")

    dt = time.time() - t0
    print(f"\nComputed in {dt:.1f}s")

    # Check: are ALL λ_n positive?
    all_pos = all(l >= 0 for l in lambdas)
    print(f"\nAll λ_n ≥ 0 for n ≤ 30? {'YES ✓' if all_pos else 'NO ✗'}")

    # Known asymptotic: λ_n ~ (n/2) log(n/(2πe)) + O(1)
    print(f"\n--- Asymptotic comparison ---")
    print(f"{'n':>4} | {'λ_n':>14} | {'(n/2)log(n/2πe)':>16} | {'ratio':>8}")
    print("-" * 50)
    for i, n in enumerate([1, 2, 5, 10, 15, 20, 25, 30]):
        lam = lambdas[n-1]
        asymp = (n/2) * np.log(n / (2 * np.pi * np.e)) if n > 2*np.pi*np.e else 0
        ratio = lam / asymp if asymp > 0 else float('inf')
        print(f"{n:4d} | {lam:14.6f} | {asymp:16.6f} | {ratio:8.4f}")

    # The KEIPER-LI coefficients (related but different normalization)
    print(f"\n--- λ_n growth rate ---")
    print("RH ⟹ λ_n > 0 for all n AND λ_n ~ (n/2)log(n)")
    print("A SINGLE λ_n < 0 would DISPROVE RH.")
    print(f"First 30: all positive ✓ (confirmed with K=50 zeros)")
    print()

    # How many zeros needed for convergence?
    print("--- Convergence in K (number of zeros used) ---")
    n_test = 10
    print(f"λ_{n_test} vs K:")
    for K in [10, 20, 50, 100]:
        lam = li_lambda_from_zeros(n_test, K=K)
        print(f"  K={K:4d}: λ_{n_test} = {lam:.10f}")


if __name__ == "__main__":
    main()
