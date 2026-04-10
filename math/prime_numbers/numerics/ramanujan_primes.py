"""
Ramanujan primes — Ramanujan's strengthening of Bertrand's postulate.

Bertrand's postulate (Chebyshev 1850): For every integer n ≥ 1, there
is at least one prime in the interval (n, 2n].

RAMANUJAN'S STRENGTHENING (1919): For each n ≥ 1, define
    R_n = smallest integer such that for all x ≥ R_n,
          π(x) - π(x/2) ≥ n.
Then R_n is always PRIME, and R_1, R_2, R_3, ... is a sequence of "Ramanujan
primes". The first few:
    R_1 = 2     (Bertrand's postulate: ≥ 1 prime in (n, 2n])
    R_2 = 11    (≥ 2 primes in (n, 2n] for all n ≥ 11)
    R_3 = 17
    R_4 = 29
    R_5 = 41
    ...
(OEIS A104272)

Ramanujan's original 1919 paper introduces the concept and proves bounds
on R_n. Modern references: Sondow (2009) gave the asymptotic
    R_n ~ p_{2n}    as n → ∞,
where p_k is the k-th prime. Recently, Laishram (2010) proved
    R_n < p_{3n}    for all n ≥ 1.

This script:
1. Computes R_n for n ≤ ~700 via the definition (sieve to 10^4)
2. Verifies against OEIS A104272
3. Shows the asymptotic R_n / p_{2n} → 1
4. Discusses the Bertrand-Ramanujan strengthening chain
"""
import numpy as np
from math import log
from sieve_core import sieve, primes_up_to


def compute_ramanujan_primes(N, n_max):
    """Compute the first n_max Ramanujan primes using sieve up to N.

    Method: cumulative π(x) - π(x/2) for x in [2, N], find where each
    'level n' was last violated, then R_n = (x_violated + 1) which is prime."""
    is_prime = np.frombuffer(sieve(N), dtype=np.uint8).astype(np.int32)
    cumpi = np.cumsum(is_prime)  # cumpi[x] = π(x)
    # c(x) = π(x) - π(floor(x/2)) for x in [2, N]
    c = np.zeros(N + 1, dtype=np.int32)
    for x in range(2, N + 1):
        c[x] = cumpi[x] - cumpi[x // 2]

    # Find R_n: the smallest integer such that c(x) ≥ n for all x ≥ R_n.
    # Equivalently: largest x with c(x) < n, then R_n = x + 1.
    # We want R_n for n = 1, 2, ..., n_max.
    R = []
    # The maximum c(x) we'll encounter:
    c_max = int(c.max())
    # For each n, find the largest x in [2, N] with c(x) < n
    # Then R_n = (largest_x + 1) which should be prime
    last_below = np.zeros(c_max + 2, dtype=np.int64)
    for x in range(2, N + 1):
        cx = int(c[x])
        # All n > cx require c(x) < n at this x
        # last_below[n] should be max x with c(x) < n
        # For n in (cx, c_max+1], current x has c(x) < n → update
        for n in range(cx + 1, c_max + 2):
            last_below[n] = x
    for n in range(1, min(c_max, n_max) + 1):
        R_n = int(last_below[n] + 1)
        if R_n > N:
            break
        R.append(R_n)
    return R


def compute_ramanujan_fast(N, n_max):
    """Vectorized version of compute_ramanujan_primes."""
    is_prime = np.frombuffer(sieve(N), dtype=np.uint8).astype(np.int32)
    cumpi = np.cumsum(is_prime)
    xs = np.arange(N + 1)
    half_xs = xs // 2
    c = cumpi[xs] - cumpi[half_xs]  # c[x] = π(x) - π(x/2)
    # For each n, R_n = max{x : c(x) < n} + 1
    # Equivalently: scan from N down, the largest c value drops with x
    # R_n = first x going DOWN where c(x) >= n is the last x with c(x) >= n
    # No, simpler: walk x=2..N tracking the maximum needed.
    # Or: for each x, "raise" R_n for all n ≤ c(x)+1 if x+1 < current R_n
    # Cleanest: for each x, the constraint "c(x) < n" makes R_n ≥ x+1 if violated.
    # So R_n = max(R_n, x + 1) for each n > c(x).
    # We need: R_n = max over x ∈ [2, N] of {x+1 if c(x) < n else 0}
    #        = max over x with c(x) < n of (x + 1)
    # If we scan backwards, the first x where c(x) >= n is the answer:
    #   R_n = (x + 1) where x is the largest x with c(x) < n
    # Equivalently: walk backwards from N and watch c(x); for each n,
    # R_n = (smallest x walking backwards) + 1 when we encounter c(x) < n
    R_dict = {}
    n_max_seen = 0
    # Walk forward — for each new x where c(x) drops below an n_max threshold...
    # Easier: just iterate backwards
    # R_n = max{x : c(x) < n} + 1
    # = N if c(N) < n, otherwise the largest x ≤ N with c(x) < n
    for n in range(1, n_max + 1):
        # find largest x with c(x) < n
        # use np.where
        below = np.where(c[2:] < n)[0]
        if len(below) == 0:
            R_dict[n] = 2  # technically c(2)=1, c(1)=0, and R_1 = 2
        else:
            largest_x = int(below.max() + 2)  # +2 because we sliced [2:]
            R_dict[n] = largest_x + 1
        if R_dict[n] > N:
            del R_dict[n]
            break
    return [R_dict[n] for n in sorted(R_dict.keys())]


def main():
    N = 10000
    print(f"Ramanujan primes via π(x) - π(x/2) ≥ n criterion, N = {N}")
    print("=" * 76)

    n_max = 1000
    R = compute_ramanujan_fast(N, n_max)
    print(f"Found {len(R)} Ramanujan primes R_n ≤ {N}")
    print()

    # Verify all R_n are prime
    primes_set = set(primes_up_to(N))
    all_prime = all(r in primes_set for r in R)
    print(f"All R_n are prime: {all_prime}")
    print()

    # Show first 20
    print("First 20 Ramanujan primes (R_1, R_2, ..., R_20):")
    print("  " + ", ".join(str(r) for r in R[:20]))
    print()

    # OEIS A104272 first 50 (verified against OEIS b-file)
    oeis_A104272 = [
        2, 11, 17, 29, 41, 47, 59, 67, 71, 97, 101, 107, 127, 149, 151, 167,
        179, 181, 227, 229, 233, 239, 241, 263, 269, 281, 307, 311, 347, 349,
        367, 373, 401, 409, 419, 431, 433, 439, 461, 487, 491, 503, 569, 571,
        587, 593, 599, 601, 607, 641
    ]
    n_check = min(len(oeis_A104272), len(R))
    matches = sum(1 for a, b in zip(R[:n_check], oeis_A104272[:n_check]) if a == b)
    print(f"OEIS A104272 verification: {matches}/{n_check} match")
    if matches == n_check:
        print("✓ EXACT match for first 50 Ramanujan primes")
    else:
        print(f"✗ Discrepancy: ours = {R[:n_check]}, OEIS = {oeis_A104272[:n_check]}")
    print()

    # Asymptotic: R_n ~ p_{2n}
    primes_list = primes_up_to(N)
    print("Asymptotic: R_n / p_{2n} → 1 (Sondow 2009)")
    print(f"{'n':>6} {'R_n':>8} {'p_{2n}':>10} {'R_n / p_{2n}':>14}")
    print("-" * 42)
    for n in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]:
        if n - 1 >= len(R):
            break
        R_n = R[n - 1]
        if 2 * n - 1 >= len(primes_list):
            break
        p_2n = primes_list[2 * n - 1]  # p_k is primes_list[k-1]
        ratio = R_n / p_2n
        print(f"{n:>6} {R_n:>8} {p_2n:>10} {ratio:>14.4f}")
    print()
    print("Ratios approach 1 as n grows (Sondow 2009 asymptotic).")
    print()

    # Laishram bound: R_n < p_{3n}
    print("Laishram (2010): R_n < p_{3n} for all n ≥ 1")
    print(f"{'n':>6} {'R_n':>8} {'p_{3n}':>10} {'satisfies?':>12}")
    print("-" * 38)
    failures = 0
    for n in [1, 5, 10, 50, 100, 500, 1000]:
        if n - 1 >= len(R):
            break
        R_n = R[n - 1]
        if 3 * n - 1 >= len(primes_list):
            break
        p_3n = primes_list[3 * n - 1]
        ok = R_n < p_3n
        if not ok:
            failures += 1
        print(f"{n:>6} {R_n:>8} {p_3n:>10} {'✓' if ok else '✗':>12}")
    print()
    print(f"Total Laishram failures: {failures}/{len(R)} (should be 0)")
    print()

    # Connection to Bertrand
    print("=" * 76)
    print("CONNECTION TO BERTRAND'S POSTULATE")
    print("=" * 76)
    print()
    print("Bertrand (Chebyshev 1850): for every n ≥ 1, ∃ prime p in (n, 2n].")
    print("Equivalently: π(2n) - π(n) ≥ 1 for all n ≥ 1.")
    print()
    print("Substituting x = 2n: π(x) - π(x/2) ≥ 1 for all x ≥ 2.")
    print()
    print("So R_1 (smallest x where this is ≥ 1 from there on) is just R_1 = 2.")
    print("Indeed, our computation gives R_1 =", R[0])
    print()
    print("Ramanujan's strengthening: ≥ 2 primes in (n, 2n] for n ≥ 5.5")
    print("(equivalently, π(x) - π(x/2) ≥ 2 for x ≥ 11, so R_2 = 11)")
    print(f"Our computation gives R_2 = {R[1]}")
    print()
    print("Higher R_n correspond to: 'every large enough interval (n, 2n] contains")
    print("at least n primes'. This is a quantitative refinement of Bertrand.")


if __name__ == '__main__':
    main()
