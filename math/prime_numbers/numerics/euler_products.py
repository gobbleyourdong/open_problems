"""
Euler products — the definitive bridge between primes and ζ(s).

EULER (1737): For Re(s) > 1,
    ζ(s) = Σ_{n=1}^∞ 1/n^s = Π_{p prime} 1/(1 - p^{-s})

This identity is THE foundational equation connecting primes to analysis.
It encodes the Fundamental Theorem of Arithmetic (unique factorization)
into a single analytic formula.

PROOF (Euler, informal): expand each factor
    1/(1 - p^{-s}) = 1 + 1/p^s + 1/p^{2s} + ...
Multiply over all p: by unique factorization, each n appears exactly once
in the product, giving Σ 1/n^s.

MERTENS' THIRD THEOREM (1874): The partial Euler product for s = 1:
    Π_{p ≤ x} (1 - 1/p) = e^{-γ} / log x · (1 + O(1/log x))
where γ ≈ 0.5772 is Euler's constant. Since Σ 1/n diverges (ζ(1) = ∞),
the product goes to 0 — but at a precisely controlled rate e^{-γ}/log x.

This script:
1. Computes the Euler product Π_{p ≤ N} (1 - p^{-s})^{-1} for s = 2..8
2. Compares to ζ(s) (mpmath reference)
3. Verifies Mertens' third theorem at multiple scales
4. Shows convergence rates for each s
"""
import numpy as np
import mpmath
from math import log, exp, sqrt
from sieve_core import sieve


def euler_product_partial(primes, s):
    """Π_{p in primes} (1 - p^{-s})^{-1}, computed in log space for stability."""
    log_prod = 0.0
    for p in primes:
        log_prod -= log(1 - p ** (-s))
    return exp(log_prod)


def mertens_product(primes, x):
    """Π_{p ≤ x} (1 - 1/p), Mertens' third theorem product."""
    log_prod = 0.0
    for p in primes:
        if p > x:
            break
        log_prod += log(1 - 1.0 / p)
    return exp(log_prod)


def main():
    N = 10**8
    print(f"Euler products: ζ(s) = Π_p (1 - p^{{-s}})^{{-1}}, primes ≤ {N}")
    print("=" * 76)

    print("Building sieve...")
    sp = sieve(N)
    primes = [i for i in range(2, N + 1) if sp[i]]
    n_primes = len(primes)
    print(f"  {n_primes} primes ≤ {N}")
    print()

    # ==============================
    # EULER PRODUCT FOR ζ(s), s = 2..8
    # ==============================
    mpmath.mp.dps = 30
    print("EULER PRODUCT verification: Π_{p ≤ 10⁸} (1 - p^{-s})^{-1} vs ζ(s)")
    print(f"{'s':>3} {'Euler product':>20} {'ζ(s) ref':>20} {'Δ':>14} {'tail est':>14}")
    print("-" * 76)
    for s in range(2, 9):
        ep = euler_product_partial(primes, s)
        zeta_s = float(mpmath.zeta(s))
        delta = ep - zeta_s
        # Tail estimate: Π_{p > N} (1 - p^{-s})^{-1} ≈ exp(Σ_{p>N} p^{-s})
        # Σ_{p > N} 1/p^s ≈ N^{1-s}/((s-1) log N) (PNT tail)
        if s > 1:
            tail = N ** (1 - s) / ((s - 1) * log(N))
        else:
            tail = float('inf')
        print(f"{s:>3} {ep:>20.15f} {zeta_s:>20.15f} {delta:>+14.3e} {tail:>14.2e}")
    print()
    print("For s ≥ 3, the Euler product matches ζ(s) to float precision (Δ ~ 0).")
    print("For s = 2, the tail Σ_{p > 10⁸} 1/p² ≈ 5.4×10⁻¹⁰ explains the Δ.")
    print()

    # Show convergence at s = 2 as we add more primes
    print("CONVERGENCE of the s = 2 Euler product as more primes are included:")
    print(f"{'primes ≤ x':>14} {'product':>20} {'Δ vs π²/6':>14}")
    print("-" * 52)
    zeta2 = float(mpmath.zeta(2))
    partial = 1.0
    checkpoints = [10, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]
    c_idx = 0
    for p in primes:
        partial /= (1 - 1.0 / p ** 2)
        while c_idx < len(checkpoints) and p >= checkpoints[c_idx]:
            print(f"{checkpoints[c_idx]:>14} {partial:>20.15f} {partial - zeta2:>+14.3e}")
            c_idx += 1
            break
    # Final
    print(f"{'10^8':>14} {partial:>20.15f} {partial - zeta2:>+14.3e}")
    print(f"{'∞ (exact)':>14} {zeta2:>20.15f} {'0':>14}")
    print()

    # ==============================
    # MERTENS' THIRD THEOREM
    # ==============================
    print("=" * 76)
    print("MERTENS' THIRD THEOREM (1874)")
    print("Π_{p ≤ x} (1 - 1/p) ~ e^{-γ} / log x")
    print("=" * 76)
    print()
    gamma = 0.5772156649015329
    e_neg_gamma = exp(-gamma)
    print(f"Euler constant γ = {gamma:.16f}")
    print(f"e^{{-γ}} = {e_neg_gamma:.16f}")
    print()
    print(f"{'x':>12} {'Π(1-1/p)':>18} {'e^(-γ)/log x':>18} {'ratio':>12}")
    print("-" * 64)
    for x in [10, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]:
        prod = mertens_product(primes, x)
        mertens_pred = e_neg_gamma / log(x)
        ratio = prod / mertens_pred
        print(f"{x:>12} {prod:>18.12f} {mertens_pred:>18.12f} {ratio:>12.8f}")
    print()
    print("Mertens: ratio → 1 as x → ∞. The convergence is O(1/log x).")
    print("At x = 10⁸, ratio ≈ 1 + O(1/18) — matches beautifully.")
    print()

    # The RECIPROCAL product (more familiar form):
    print("EQUIVALENT: Π_{p ≤ x} (1 - 1/p)^{-1} ~ e^γ · log x")
    print(f"{'x':>12} {'Π(1-1/p)^{-1}':>18} {'e^γ · log x':>18} {'ratio':>12}")
    print("-" * 64)
    e_gamma = exp(gamma)
    for x in [10, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]:
        prod = 1.0 / mertens_product(primes, x)
        pred = e_gamma * log(x)
        ratio = prod / pred
        print(f"{x:>12} {prod:>18.8f} {pred:>18.8f} {ratio:>12.8f}")
    print()

    # Mertens' SECOND theorem: Σ 1/p ~ log log x + M (Meissel-Mertens constant)
    # M = γ + Σ_p (log(1-1/p) + 1/p) ≈ 0.2614972128476...
    # NOT γ itself! The difference is Σ_p (-1/(2p²) - 1/(3p³) - ...)
    M_meissel = gamma + sum(log(1 - 1.0/p) + 1.0/p for p in primes)
    M_ref = 0.2614972128476427837554268386086958590516
    print("MERTENS' SECOND THEOREM: Σ_{p ≤ x} 1/p ~ log log x + M")
    print(f"M (Meissel-Mertens constant) = {M_meissel:.16f}")
    print(f"M reference                   = {M_ref:.16f}")
    print(f"Δ = {abs(M_meissel - M_ref):.2e}")
    print()
    print(f"{'x':>12} {'Σ 1/p':>14} {'log log x + M':>16} {'Δ':>12}")
    print("-" * 58)
    running = 0.0
    c_idx = 0
    checkpoints2 = [10, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]
    for p in primes:
        running += 1.0 / p
        while c_idx < len(checkpoints2) and p >= checkpoints2[c_idx]:
            x = checkpoints2[c_idx]
            pred = log(log(x)) + M_ref
            delta = running - pred
            print(f"{x:>12} {running:>14.8f} {pred:>16.8f} {delta:>+12.6f}")
            c_idx += 1
            break
    print()
    print("The Meissel-Mertens constant M ≈ 0.2615 is NOT the same as γ ≈ 0.5772.")
    print("The difference: M = γ + Σ_p (log(1 - 1/p) + 1/p) — a convergent prime sum.")


if __name__ == '__main__':
    main()
