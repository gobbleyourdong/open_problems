"""
Lehmer's totient problem (1932).

For Euler's totient function φ(n) = #{k ∈ [1, n] : gcd(k, n) = 1},
we have:
    n is prime ⇔ φ(n) = n - 1 ⇔ φ(n) | (n - 1)  trivially.

LEHMER'S QUESTION: Are there COMPOSITE n with φ(n) | (n - 1)?

LEHMER'S 1932 RESULT: If such an n exists, then n must be:
    1. odd
    2. squarefree
    3. divisible by at least 7 distinct primes
    4. n > 6 × 10^9 (Lehmer's original bound)

Subsequent improvements (Cohen-Hagis 1980, Pinch 2006, Hagis 2009 et al.):
    - n must have ≥ 14 distinct prime factors
    - n > 10^22

Conjecturally, NO SUCH n EXISTS — but no proof is known.

This is one of the cleanest open problems in elementary number theory:
the question is simple, computational verification is feasible to large
bounds, and the conjectured answer is "no" — yet no proof exists.

CONNECTION TO CARMICHAEL: Lehmer's problem is "harder" than Carmichael's
totient conjecture (every value of φ is taken by ≥ 2 inputs, proved by
Ford 1999 unconditionally).

This script:
1. Builds totient sieve to N = 10⁷
2. Searches for composite n with φ(n) | (n - 1) — finds NONE
3. Records the smallest 'φ-quotient' (n - 1) / φ(n) for composite n
4. Shows the structure of "near-misses"
"""
import numpy as np
from sieve_core import sieve


def totient_sieve(N):
    """Compute Euler's totient φ(n) for all n ≤ N via sieve."""
    phi = np.arange(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if phi[p] == p:  # p is prime
            phi[p::p] -= phi[p::p] // p
    return phi


def main():
    N = 10**7
    print(f"Lehmer's totient problem search: composite n ≤ {N} with φ(n) | (n−1)")
    print("=" * 76)

    print(f"Building totient sieve to {N}...")
    phi = totient_sieve(N)
    print()

    # Sanity: φ(p) = p - 1 for prime p
    print("Sanity check: φ(p) = p - 1 for primes p ∈ {2, 3, 5, 7, 11, ...}")
    primes_check = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for p in primes_check:
        print(f"  φ({p}) = {phi[p]}, p - 1 = {p - 1}, match: {phi[p] == p - 1}")
    print()

    # The search
    print(f"Searching all composite n ∈ [4, {N}] for φ(n) | (n-1)...")
    n_arr = np.arange(2, N + 1, dtype=np.int64)
    phi_arr = phi[2:N + 1]
    n_minus_1 = n_arr - 1
    # Composite means φ(n) < n - 1 (equivalently, φ(n) ≠ n - 1)
    is_composite = phi_arr < n_minus_1
    # Divides means (n - 1) % φ(n) == 0
    # WARNING: φ(2) = 1 for n=2, n−1=1, divides → but 2 is prime, OK
    divides = (n_minus_1 % phi_arr) == 0
    candidates = is_composite & divides
    n_found = n_arr[candidates]

    print(f"  Composite n ≤ {N} with φ(n) | (n−1): {len(n_found)}")
    if len(n_found) == 0:
        print(f"  ✓ NO COUNTEREXAMPLE FOUND in [4, {N}]")
        print(f"  Lehmer's problem holds (no solutions) up to 10⁷.")
    else:
        print(f"  ✗ Found counterexamples: {list(n_found[:10])}...")
    print()

    # Sanity check: every prime IS in the "divides" set (as expected)
    n_prime_check = n_arr[(~is_composite) & divides]
    n_prime_check_total = n_arr[~is_composite]
    print(f"  All primes p ≤ {N} satisfy φ(p) | (p-1) (by definition):")
    print(f"    primes detected: {len(n_prime_check_total)}")
    print(f"    primes also in 'divides' set: {len(n_prime_check)}")
    print(f"    match: {len(n_prime_check) == len(n_prime_check_total)}")
    print()

    # Look for "near-misses": composite n with smallest (n−1)/φ(n)
    print("=" * 76)
    print("'NEAR-MISSES': composites with the smallest (n−1)/φ(n) ratios")
    print("=" * 76)
    print()
    print("Lehmer's question is whether (n−1)/φ(n) can ever be an INTEGER for")
    print("composite n. We can find composites where (n−1)/φ(n) is closest to")
    print("an integer — these are the 'near-misses'.")
    print()
    # ratio = (n - 1) / phi(n)
    composite_idx = is_composite
    composite_n = n_arr[composite_idx]
    composite_phi = phi_arr[composite_idx]
    ratios = (composite_n - 1) / composite_phi
    # Distance from nearest integer
    int_dist = np.abs(ratios - np.round(ratios))
    # Find composites with the smallest int_dist (closest to integer ratio)
    sorted_idx = np.argsort(int_dist)
    print("Top 15 'near-miss' composites (closest (n−1)/φ(n) to integer):")
    print(f"{'n':>10} {'φ(n)':>10} {'(n−1)/φ(n)':>16} {'fractional':>14}")
    print("-" * 56)
    for i in sorted_idx[:15]:
        n = int(composite_n[i])
        phin = int(composite_phi[i])
        ratio = (n - 1) / phin
        frac = abs(ratio - round(ratio))
        print(f"{n:>10} {phin:>10} {ratio:>16.6f} {frac:>14.2e}")
    print()
    print("Note: the closest 'near-misses' have (n−1)/φ(n) very close to an")
    print("integer but not exactly equal. The conjectured truth (no composite")
    print("has integer ratio) is consistent with these arbitrarily close approaches.")
    print()

    # Distribution of (n-1)/φ(n) ratios
    print("=" * 76)
    print("DISTRIBUTION of (n−1)/φ(n) for composites")
    print("=" * 76)
    print()
    print("For n prime:    (n−1)/φ(n) = 1 exactly")
    print("For n = 2p:     φ(2p) = p−1, so (2p−1)/(p−1) = 2 + 1/(p−1) → 2")
    print("For n = pq:     φ(pq) = (p−1)(q−1), generically not integer")
    print()
    # Histogram of ratios for composites
    print("Histogram of (n−1)/φ(n) for composites n ≤ 10⁷:")
    bins = np.arange(1.0, 4.5, 0.25)
    counts, _ = np.histogram(ratios, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2
    for c, n in zip(centers, counts):
        bar = "█" * int(np.log10(max(n, 1)) * 4)
        print(f"  ratio ≈ {c:.2f}: {int(n):>10}  {bar}")
    print()
    print("Mean (n−1)/φ(n) over composites: "
          f"{ratios.mean():.4f}")
    print("Min  (n−1)/φ(n) over composites: "
          f"{ratios.min():.4f}")
    print("Max  (n−1)/φ(n) over composites: "
          f"{ratios.max():.4f}")
    print()

    # Cohen-Hagis structural constraints
    print("=" * 76)
    print("LEHMER'S STRUCTURAL CONSTRAINTS")
    print("=" * 76)
    print()
    print("If a composite n with φ(n) | (n-1) exists, Lehmer (1932) proved:")
    print("  1. n is odd")
    print("     Reason: if 2 | n then φ(n) is even, but n - 1 is odd, contradiction.")
    print("  2. n is squarefree")
    print("     Reason: if p² | n then p | φ(n), but p ∤ (n-1) (since p | n).")
    print("  3. n has ≥ 7 distinct prime factors  (Lehmer 1932)")
    print("     Improved to ≥ 14 by Cohen-Hagis (1980) and later authors.")
    print()
    print("If n = p₁ p₂ ... p_k (squarefree odd), then")
    print("  φ(n) = ∏ (pᵢ - 1)")
    print("And the requirement is")
    print("  ∏ (pᵢ - 1)  |  ∏ pᵢ - 1")
    print("This is a strong Diophantine condition that's why no examples exist.")
    print()
    print("Modern bound (Pinch 2006, Hagis 2009 et al.):")
    print("  Any counterexample n > 10²².")


if __name__ == '__main__':
    main()
