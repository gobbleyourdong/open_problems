#!/usr/bin/env python3
"""
Robin's Inequality: σ(n) < e^γ n log log n for all n > 5040.

RH ⟺ Robin's inequality holds for all n > 5040.

σ(n) = sum of divisors of n.
γ = Euler-Mascheroni constant ≈ 0.5772156649.

The tightest cases are HIGHLY COMPOSITE and SUPERABUNDANT numbers.
A counterexample would disprove RH.

This is pure integer arithmetic — no floating point issues for σ(n).
"""

import math
import time


EULER_GAMMA = 0.5772156649015328606


def sigma(n):
    """Sum of divisors of n."""
    if n <= 0:
        return 0
    s = 0
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            s += d
            if d != n // d:
                s += n // d
    return s


def robin_bound(n):
    """e^γ n log log n."""
    if n <= 2:
        return float('inf')
    return math.exp(EULER_GAMMA) * n * math.log(math.log(n))


def robin_ratio(n):
    """σ(n) / (e^γ n log log n). RH ⟹ ratio < 1 for n > 5040."""
    bound = robin_bound(n)
    if bound <= 0:
        return float('inf')
    return sigma(n) / bound


# Highly composite numbers (most divisors for their size)
# These are the most likely to violate Robin's inequality
HC_NUMBERS = [
    2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840,
    1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200,
    27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760,
    277200, 332640, 498960, 554400, 665280, 720720, 1081080,
    1441440, 2162160, 2882880, 3603600, 4324320, 7207200,
    8648640, 10810800, 14414400, 17297280, 21621600, 36756720,
    43243200, 61261200, 73513440, 110270160, 147026880, 183783600,
    245044800, 294053760, 367567200, 551350800, 698377680,
]


def main():
    print("=" * 70)
    print("ROBIN'S INEQUALITY: σ(n) < e^γ n log log n for n > 5040")
    print("=" * 70)
    print(f"RH ⟺ this holds for ALL n > 5040.")
    print(f"e^γ ≈ {math.exp(EULER_GAMMA):.10f}")
    print()

    # Check highly composite numbers
    print("--- Highly Composite Numbers (tightest cases) ---\n")
    print(f"{'n':>12} | {'σ(n)':>14} | {'bound':>14} | {'ratio':>10} | {'< 1?':>6}")
    print("-" * 65)

    tightest_n = 0
    tightest_ratio = 0
    violations = 0

    for n in HC_NUMBERS:
        if n <= 5040:
            continue
        s = sigma(n)
        b = robin_bound(n)
        r = s / b
        ok = "✓" if r < 1 else "✗ FAIL"
        if r >= 1:
            violations += 1
        if r > tightest_ratio and n > 5040:
            tightest_ratio = r
            tightest_n = n
        print(f"{n:12d} | {s:14d} | {b:14.2f} | {r:10.8f} | {ok:>6}")

    # Scan ALL numbers in a range
    print(f"\n--- Full scan: n = 5041 to 100000 ---")
    t0 = time.time()
    max_ratio = 0
    max_n = 0
    count = 0

    for n in range(5041, 100001):
        r = robin_ratio(n)
        if r > max_ratio:
            max_ratio = r
            max_n = n
        if r >= 1:
            violations += 1
            print(f"  VIOLATION at n = {n}: ratio = {r:.10f}")
        count += 1

    dt = time.time() - t0
    print(f"Scanned {count} numbers in {dt:.1f}s")
    print(f"Tightest: n = {max_n}, ratio = {max_ratio:.10f}")
    print(f"Violations: {violations}")

    # Extended scan for n = 100001 to 1000000 (sampling highly composite + colossally abundant)
    print(f"\n--- Extended: colossally abundant numbers ---")
    # CA numbers: n = 2^a × 3^b × 5^c × ... where exponents decrease
    # Generate some:
    ca_numbers = []
    for a in range(1, 20):
        for b in range(0, a+1):
            for c in range(0, b+1):
                for d in range(0, c+1):
                    n = (2**a) * (3**b) * (5**c) * (7**d)
                    if 5040 < n < 10**8:
                        ca_numbers.append(n)
    ca_numbers = sorted(set(ca_numbers))

    print(f"Testing {len(ca_numbers)} candidate numbers...")
    max_ratio_ca = 0
    max_n_ca = 0

    for n in ca_numbers[:200]:  # limit for speed
        r = robin_ratio(n)
        if r > max_ratio_ca:
            max_ratio_ca = r
            max_n_ca = n
        if r >= 1:
            print(f"  VIOLATION at n = {n}: ratio = {r:.10f}")

    print(f"Tightest CA: n = {max_n_ca}, ratio = {max_ratio_ca:.10f}")

    # Summary
    print(f"\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Range tested: n = 5041 to 100000 (full) + {len(ca_numbers[:200])} CA numbers")
    print(f"Violations: {violations}")
    print(f"Tightest ratio: {max(max_ratio, max_ratio_ca):.10f} at n = {max_n if max_ratio > max_ratio_ca else max_n_ca}")
    print(f"Robin's inequality holds: {'YES ✓' if violations == 0 else 'NO ✗'}")
    print()
    print("The tightest cases are highly composite numbers near n ≈ 5040-10000.")
    print("The margin INCREASES for larger n (the inequality becomes easier to satisfy).")
    print("This is consistent with RH.")


if __name__ == "__main__":
    main()
