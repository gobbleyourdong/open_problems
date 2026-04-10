"""
Hardy-Ramanujan & Erdős-Kac: distribution of ω(n).

ω(n) = number of distinct prime factors of n.

Hardy-Ramanujan (1917): ω(n) ~ log log n typically.
Erdős-Kac (1939): (ω(n) - log log n) / sqrt(log log n) → N(0,1) as n → ∞.

The Erdős-Kac convergence is asymptotic in log log n, which grows very slowly.
At n = 10⁷, log log n ≈ 2.78 — far from the asymptotic regime.

This script verifies:
- Mean ω(n) ≈ log log x (Hardy-Ramanujan, leading order)
- Variance ω(n) → log log x (Erdős-Kac, slowly)
- Maximum ω(n) is at primorials
"""
import numpy as np
from math import log
from collections import Counter
from sieve_core import sieve


def compute_omega(N):
    """ω(n) for n = 0..N via sieve. ω(p) increments for each prime p ≤ N."""
    omega = np.zeros(N + 1, dtype=np.int16)
    is_prime = sieve(N)
    for p in range(2, N + 1):
        if is_prime[p]:
            omega[p::p] += 1
    return omega


def main():
    N = 10**7
    print(f"ω(n) for n in [2, {N}]")
    print("=" * 60)

    omega = compute_omega(N)
    mean = float(np.mean(omega[2:]))
    var = float(np.var(omega[2:]))
    ll_x = log(log(N))

    print(f"Mean ω(n) = {mean:.4f}")
    print(f"Var  ω(n) = {var:.4f}")
    print(f"log log N = {ll_x:.4f}")
    print(f"Mean - log log N = {mean - ll_x:.4f} (Hardy-Ramanujan O(1) correction)")
    print(f"Var/log log N    = {var/ll_x:.4f} (Erdős-Kac: → 1 slowly)")
    print()

    # Distribution of ω
    hist = Counter(omega[2:])
    total = N - 1
    print("Distribution:")
    for k in sorted(hist.keys()):
        c = hist[k]
        bar = "█" * int(c / total * 100)
        print(f"  ω = {k}: {c:>10} ({c/total:.4%}) {bar}")
    print()

    # Maximum
    max_k = int(np.max(omega))
    n_max = int(np.argmax(omega[:N + 1]))
    print(f"Max ω(n) = {max_k} at n = {n_max}")
    # Factor n_max
    factors = []
    nt = n_max
    for p in range(2, int(np.sqrt(n_max)) + 2):
        while nt % p == 0:
            factors.append(p)
            nt //= p
    if nt > 1:
        factors.append(nt)
    print(f"  {n_max} = {' × '.join(str(f) for f in sorted(set(factors)))}")
    print(f"  This is primorial 19# = {2*3*5*7*11*13*17*19}")
    print()

    # Variance growth
    print("Variance growth (Erdős-Kac):")
    print(f"{'x':>10} {'var(ω)':>10} {'log log x':>10} {'ratio':>10}")
    for x in [10**k for k in range(2, 8)]:
        sub = omega[2:x + 1]
        v = float(np.var(sub))
        ll = log(log(x))
        print(f"{x:>10} {v:>10.4f} {ll:>10.4f} {v/ll:>10.4f}")


if __name__ == '__main__':
    main()
