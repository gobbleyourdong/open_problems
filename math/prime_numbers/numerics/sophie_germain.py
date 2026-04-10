"""
Sophie Germain primes and Cunningham chains.

A SOPHIE GERMAIN PRIME is a prime p such that 2p + 1 is also prime.
The corresponding 2p + 1 is called a SAFE PRIME.

Sophie Germain (1823) introduced these in her partial proof of FLT for
exponent 5: if p is a Sophie Germain prime, then the first case of FLT
holds for p (i.e., x^p + y^p = z^p has no solutions with p ∤ xyz). This
was the first major result on FLT after Fermat himself.

Hardy-Littlewood prediction (Bateman-Horn for f_1(n) = n, f_2(n) = 2n+1):
    π_SG(N) := #{p ≤ N : p, 2p+1 both prime}
            ~ 2 C_2 · ∫_2^N dt / (log t · log(2t+1))
            ≈ 2 C_2 · Li_2(N)
where C_2 ≈ 0.6601618 is the same twin prime constant!

Both polynomials are linear; ω(p) = 2 for p ≥ 3 (n = 0 makes f_1 = 0,
n = (p-1)/2 makes f_2 = 0); ω(2) = 1. The singular series is identical
to that of twin primes.

CUNNINGHAM CHAINS OF THE FIRST KIND: a sequence of primes
    p_0, p_1, p_2, ... where p_{i+1} = 2 p_i + 1.
Each consecutive pair is a SG-pair. The chain length is the number of
primes in the longest such sequence starting from p_0.

The smallest chain of length k is recorded in OEIS A005602:
    k=2: 2  (chain 2 → 5)
    k=3: 2  (2 → 5 → 11)
    k=4: 2  (2 → 5 → 11 → 23)
    k=5: 2  (2 → 5 → 11 → 23 → 47)
    k=6: 89 (89 → 179 → 359 → 719 → 1439 → 2879)
    k=7: 1,122,659
    k=8: 19,099,919
    k=9: 85,864,769
    ...

This script finds all SG primes ≤ 10^8 and the longest Cunningham chains
in the range.
"""
import numpy as np
from math import log
from sieve_core import sieve
from scipy.integrate import quad


def main():
    N = 10**8
    print(f"Sophie Germain primes & Cunningham chains, primes ≤ {N}")
    print("=" * 76)

    print("Building sieve...")
    sp = sieve(N)
    is_prime = np.frombuffer(sp, dtype=np.uint8).astype(bool)
    print(f"  {is_prime.sum()} primes ≤ {N}")
    print()

    # ==============================
    # FIND ALL SOPHIE GERMAIN PRIMES
    # ==============================
    print(f"[SOPHIE GERMAIN] p prime AND 2p+1 prime, p ≤ {N}")
    print("-" * 60)
    # SG: p ≤ N AND 2p+1 ≤ 2N+1, so we need is_prime up to 2N+1
    # But our sieve only goes to N. We need to either re-sieve to 2N or
    # restrict to p ≤ N/2 - 1. Let's do the latter (still substantial).

    # Actually let's re-sieve to 2N+1 since we want p ≤ N/2 → 2p+1 ≤ N+1
    # This means we get SG primes up to N/2, not N.
    # OR we sieve to 2N+1 and find SG primes up to N. Sieve to 2N+1 is 200MB
    # and probably workable.

    # Use the quicker approach: SG primes p ≤ N/2 (so 2p+1 ≤ N+1)
    half_N = N // 2
    primes_below_half = np.array([i for i in range(2, half_N + 1) if is_prime[i]],
                                 dtype=np.int64)
    sg_mask = is_prime[2 * primes_below_half + 1]
    sg_primes = primes_below_half[sg_mask].tolist()
    print(f"  Sophie Germain primes p ≤ {half_N}: {len(sg_primes)}")
    print(f"  First 20: {sg_primes[:20]}")
    print(f"  Largest: {sg_primes[-1]}")
    print()

    # OEIS A092816 (number of SG primes < 10^k):
    oeis_A092816 = {
        1: 3,    # SG primes < 10: 2, 3, 5
        2: 10,   # < 100
        3: 37,   # < 1000
        4: 190,
        5: 1171,
        6: 7746,
        7: 56032,
        8: 423140,
    }
    print("Verification against OEIS A092816 (SG primes < 10^k):")
    print(f"{'X':>10} {'observed':>10} {'OEIS':>10} {'match':>8}")
    print("-" * 46)
    for k in range(1, 9):
        X = 10 ** k
        if X > half_N:
            break
        obs = sum(1 for p in sg_primes if p < X)
        oeis = oeis_A092816.get(k, None)
        if oeis is not None:
            match = "✓" if obs == oeis else f"✗ (Δ={obs-oeis})"
            print(f"{X:>10} {obs:>10} {oeis:>10} {match:>8}")
    print()

    # Hardy-Littlewood prediction
    C_2 = 0.6601618158468695
    Li2_N, _ = quad(lambda t: 1.0 / (log(t) * log(2 * t + 1)), 2, half_N, limit=200)
    pred = 2 * C_2 * Li2_N
    obs = len(sg_primes)
    print(f"Hardy-Littlewood prediction:")
    print(f"  π_SG({half_N}) ~ 2 C_2 · ∫_2^N dt/(log t · log(2t+1))")
    print(f"  C_2 = {C_2:.10f}")
    print(f"  Integral = {Li2_N:.2f}")
    print(f"  Predicted: {pred:.0f}")
    print(f"  Observed:  {obs}")
    print(f"  Ratio:     {obs / pred:.4f}")
    print()

    # ==============================
    # CUNNINGHAM CHAINS OF THE 1ST KIND
    # ==============================
    print("[CUNNINGHAM CHAINS] Sequences p_{i+1} = 2 p_i + 1")
    print("-" * 60)
    sg_set = set(sg_primes)
    is_sg = np.zeros(half_N + 2, dtype=bool)
    for p in sg_primes:
        is_sg[p] = True

    # For each starting prime p, follow the chain
    # A "starting" prime p is one such that (p-1)/2 is NOT prime (so p is the
    # smallest prime of its chain). This avoids counting the same chain twice.
    print("Smallest chain of each length, comparing to OEIS A005602:")
    oeis_A005602 = {
        2: 2,
        3: 2,
        4: 2,
        5: 2,
        6: 89,
        7: 1122659,
        8: 19099919,
        9: 85864769,
    }

    chain_lengths = {}
    primes_check = np.array([i for i in range(2, half_N + 1) if is_prime[i]],
                            dtype=np.int64)
    for p in primes_check:
        # Check if p is the start of a chain (i.e., (p-1)/2 is not prime)
        if p > 2 and (p - 1) % 2 == 0:
            half = (p - 1) // 2
            if half >= 2 and is_prime[half]:
                continue  # not the start
        # Follow the chain
        length = 1
        q = p
        while 2 * q + 1 <= N and is_prime[2 * q + 1]:
            length += 1
            q = 2 * q + 1
        # chain_lengths[k] = smallest p starting a chain of length ≥ k
        for k in range(2, length + 1):
            if k not in chain_lengths or p < chain_lengths[k]:
                chain_lengths[k] = p

    print(f"{'k':>4} {'smallest start':>16} {'OEIS A005602':>16} {'match':>8}")
    print("-" * 50)
    for k in sorted(chain_lengths.keys()):
        smallest = chain_lengths[k]
        oeis = oeis_A005602.get(k, None)
        marker = "✓" if oeis == smallest else (f"OEIS={oeis}" if oeis else "")
        print(f"{k:>4} {smallest:>16} {str(oeis or '—'):>16} {marker:>8}")
    print()

    # Show the actual longest chain found
    if chain_lengths:
        max_k = max(chain_lengths.keys())
        start = chain_lengths[max_k]
        print(f"Longest chain found (length {max_k}, starting at {start}):")
        chain = [start]
        q = start
        for _ in range(max_k - 1):
            q = 2 * q + 1
            chain.append(q)
        print(f"  {' → '.join(str(c) for c in chain)}")


if __name__ == '__main__':
    main()
