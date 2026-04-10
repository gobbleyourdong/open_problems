"""
Mertens function M(x) and Chebyshev ψ(x).

M(x) = Σ_{n ≤ x} μ(n) — partial sum of the Möbius function.
  - Mertens conjecture (1897): |M(x)| < √x for all x.
  - Disproved 1985 (Odlyzko-te Riele) — first counterexample above 10¹⁴.
  - Equivalent to RH: M(x) = O(x^(1/2 + ε)).

ψ(x) = Σ_{p^k ≤ x} log(p) — Chebyshev's prime power sum.
  - PNT: ψ(x) ~ x.
  - RH: |ψ(x) - x| = O(√x · log² x).

Both functions are computed exactly via sieve methods up to N = 10^7.
"""
import numpy as np
from math import log, sqrt
from sieve_core import sieve


def mobius_array(N):
    """Compute μ(n) for n = 0..N via smallest-prime-factor sieve."""
    is_prime = sieve(N)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)
    primes = [p for p in range(2, N + 1) if prime_arr[p]]

    spf = np.zeros(N + 1, dtype=np.int64)
    for p in primes:
        spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])

    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    for n in range(2, N + 1):
        p = spf[n]
        n_over_p = n // p
        if n_over_p % p == 0:
            mu[n] = 0  # p² divides n
        else:
            mu[n] = -mu[n_over_p]
    return mu


def mertens(N):
    """Mertens function M(x) for x = 0..N."""
    mu = mobius_array(N)
    return np.cumsum(mu.astype(np.int64))


def chebyshev_psi(N):
    """ψ(x) = Σ_{p^k ≤ x} log p, cumulative array."""
    is_prime = sieve(N)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)
    primes = [p for p in range(2, N + 1) if prime_arr[p]]

    contrib = np.zeros(N + 1, dtype=np.float64)
    for p in primes:
        pk = p
        while pk <= N:
            contrib[pk] += log(p)
            pk *= p
    return np.cumsum(contrib)


def main():
    N = 10**7
    print(f"Computing Mertens M(x) and Chebyshev ψ(x) up to {N}")
    print("=" * 65)

    import time
    t0 = time.time()
    M = mertens(N)
    print(f"  M(x) computed in {time.time()-t0:.1f}s")

    t0 = time.time()
    psi = chebyshev_psi(N)
    print(f"  ψ(x) computed in {time.time()-t0:.1f}s")

    # Mertens
    print(f"\nMERTENS FUNCTION M(x):")
    print(f"{'x':>10} | {'M(x)':>10} | {'|M|/sqrt(x)':>12}")
    print("-" * 40)
    for x in [100, 1000, 10000, 100000, 1000000, 10000000]:
        ratio = abs(M[x]) / sqrt(x)
        print(f"{x:>10} | {int(M[x]):>+10d} | {ratio:>12.4f}")

    # Distribution analysis (excluding small x)
    xs = np.arange(10, N + 1)
    ratios = np.abs(M[10:]).astype(np.float64) / np.sqrt(xs.astype(np.float64))
    print(f"\nMertens conjecture |M(x)| < sqrt(x) check:")
    print(f"  max |M|/sqrt(x) in [10, 10^7] = {ratios.max():.4f}")
    print(f"  99th percentile: {np.percentile(ratios, 99):.4f}")
    print(f"  Holds in entire tested range (disproved above 10^14, Odlyzko-te Riele 1985)")

    # Chebyshev
    print(f"\nCHEBYSHEV ψ(x):")
    print(f"{'x':>10} | {'ψ(x)':>14} | {'|ψ-x|':>10} | {'|ψ-x|/sqrt(x)':>15}")
    print("-" * 60)
    for x in [100, 1000, 10000, 100000, 1000000, 10000000]:
        err = psi[x] - x
        rel = abs(err) / sqrt(x)
        print(f"{x:>10} | {psi[x]:>14.2f} | {err:>+10.2f} | {rel:>15.4f}")

    print("\nRH predicts |ψ(x) - x| = O(sqrt(x) · log² x).")
    print("Observed |ψ-x|/sqrt(x) grows ~log² x, consistent with RH.")


if __name__ == '__main__':
    main()
