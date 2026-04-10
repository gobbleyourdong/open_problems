"""
Kummer's irregular primes — Bernoulli numbers, cyclotomic class groups,
and Fermat's Last Theorem.

DEFINITION (Kummer 1850): An odd prime p is REGULAR if p does not divide
the class number h(Q(ζ_p)) of the p-th cyclotomic field. Otherwise it
is IRREGULAR.

KUMMER'S CRITERION (Kummer 1850): p is regular iff p does NOT divide the
numerator of any Bernoulli number B_{2k} for 2 ≤ 2k ≤ p − 3.

Equivalently, the irregularity index of p is the number of even integers
2k ∈ [2, p − 3] such that p | numerator(B_{2k}).
- Irregularity index = 0 ⇔ p is regular.
- Irregularity index ≥ 1 ⇔ p is irregular.

KUMMER'S FLT THEOREM (1850): If p is a regular odd prime, then Fermat's
Last Theorem holds for p — i.e., x^p + y^p = z^p has no positive integer
solutions.

This was the first general result on FLT for an infinite family of primes,
predating Wiles by 145 years. Kummer used unique factorization in the
ring Z[ζ_p] (which fails when p is irregular, controlled by p | h).

SIEGEL'S CONJECTURE (1964): The density of irregular primes among all
primes is 1 − e^(−1/2) ≈ 0.39347.

Heuristic: each B_{2k} mod p is "random" in [0, p), so P(p | B_{2k}) ≈ 1/p.
There are (p − 3)/2 candidate 2k. Probability of zero hits:
    P(regular) ≈ (1 − 1/p)^((p−3)/2) → e^(−1/2) as p → ∞
So density of irregular primes → 1 − e^(−1/2) ≈ 0.3935.

This script computes irregular primes ≤ 500 using mpmath.bernfrac.
"""
import mpmath
from sieve_core import primes_up_to


def bernoulli_numerators(max_2k):
    """Return dict mapping 2k to numerator(B_{2k}) for 2 ≤ 2k ≤ max_2k.
    Uses mpmath.bernfrac which returns exact (num, den) pairs."""
    out = {}
    for k in range(1, max_2k // 2 + 1):
        idx = 2 * k
        num, den = mpmath.bernfrac(idx)
        out[idx] = (int(num), int(den))
    return out


def irregularity_index(p, bern_dict):
    """For prime p, count even 2k in [2, p-3] with p | numerator(B_{2k}).

    The von Staudt-Clausen theorem makes B_{2k} mod p well-defined when
    (p-1) ∤ 2k. When (p-1) | 2k, we should add 1/p to make it integer
    p-adically and then check, but for the standard "Kummer irregularity
    index" we just check if p | numerator (the literal numerator, NOT
    the p-adic version).
    """
    count = 0
    bad_indices = []
    for k_idx in range(2, p - 2, 2):  # 2, 4, ..., p-3
        num, _den = bern_dict[k_idx]
        if num % p == 0:
            count += 1
            bad_indices.append(k_idx)
    return count, bad_indices


def main():
    P_MAX = 500
    print(f"Kummer's irregular primes, p ≤ {P_MAX}")
    print("=" * 76)

    print(f"Computing Bernoulli numerators B_2, B_4, ..., B_{P_MAX - 3}...")
    bern = bernoulli_numerators(P_MAX - 3)
    print(f"  Done — {len(bern)} even Bernoulli numbers computed.")
    print()

    odd_primes = [p for p in primes_up_to(P_MAX) if p > 2]
    print(f"Testing {len(odd_primes)} odd primes ≤ {P_MAX} for irregularity...")
    print()

    irregular = []
    irreg_index = {}
    for p in odd_primes:
        i, bad = irregularity_index(p, bern)
        if i > 0:
            irregular.append(p)
            irreg_index[p] = (i, bad)

    print(f"Found {len(irregular)} irregular primes ≤ {P_MAX}.")
    print(f"Regular primes ≤ {P_MAX}: {len(odd_primes) - len(irregular)}")
    print()

    # OEIS A000928: irregular primes
    oeis_A000928_to_500 = [
        37, 59, 67, 101, 103, 131, 149, 157, 233, 257, 263, 271, 283, 293,
        307, 311, 347, 353, 379, 389, 401, 409, 421, 433, 461, 463, 467, 491
    ]
    print(f"OEIS A000928 (irregular primes ≤ {P_MAX}):")
    print(f"  expected: {oeis_A000928_to_500}")
    print(f"  observed: {irregular}")
    if irregular == oeis_A000928_to_500:
        print("  ✓ EXACT match")
    else:
        diff = set(irregular) ^ set(oeis_A000928_to_500)
        print(f"  ✗ differ by: {sorted(diff)}")
    print()

    # Show irregularity indices
    print("Irregular primes with their irregularity indices and Bernoulli witnesses:")
    print(f"{'p':>6} {'index':>8} {'bad B_{2k}':>40}")
    print("-" * 56)
    for p in irregular:
        i, bad = irreg_index[p]
        bad_str = ", ".join(f"B_{k}" for k in bad)
        print(f"{p:>6} {i:>8} {bad_str:>40}")
    print()

    # Density vs Siegel's conjecture
    print("Cumulative density of irregular primes vs Siegel's heuristic:")
    print(f"{'X':>6} {'irregular':>10} {'odd primes':>12} {'density':>10} "
          f"{'Siegel pred':>14}")
    print("-" * 58)
    import math
    siegel = 1 - math.exp(-0.5)
    for X in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        n_irreg = sum(1 for p in irregular if p <= X)
        n_odd = sum(1 for p in odd_primes if p <= X)
        density = n_irreg / n_odd if n_odd > 0 else 0
        print(f"{X:>6} {n_irreg:>10} {n_odd:>12} {density:>10.4f} "
              f"{siegel:>14.4f}")
    print()

    # The famous 691 case (just outside our range, but illustrative)
    print("HISTORICAL: The 691 connection")
    print("-" * 60)
    print("B_12 = -691/2730. Since 691 is prime and divides the numerator,")
    print("  691 is an irregular prime (irregularity index 1).")
    print("This was discovered by Kummer himself.")
    # Let's compute B_12 to verify
    n12, d12 = mpmath.bernfrac(12)
    print(f"  Verification: B_12 = {int(n12)} / {int(d12)}")
    print(f"  Numerator divisible by 691: {int(n12) % 691 == 0}")
    print()

    # FLT exponents covered by Kummer's regular prime theorem
    print("FLT exponents covered by Kummer's regular prime theorem (≤ 500):")
    regular = sorted(set(odd_primes) - set(irregular))
    print(f"  Number of regular primes (FLT exponents Kummer proved): {len(regular)}")
    print(f"  Number of irregular primes (FLT not proved by Kummer):  {len(irregular)}")
    print()
    print(f"  First 10 regular primes: {regular[:10]}")
    print(f"  Smallest irregular prime: {irregular[0]} (Kummer 1850)")
    print()

    # Note that Kummer's theorem WAS extended for irregular primes by:
    # - Vandiver (1929): proved FLT for many small irregular primes via
    #   the "Vandiver criterion"
    # - Wiles (1995): proved FLT in full generality
    print("Note: Kummer's theorem was extended to many irregular primes by")
    print("Vandiver (1929) using a refined criterion, and proven in full")
    print("generality by Wiles (1995) via modularity.")


if __name__ == '__main__':
    main()
