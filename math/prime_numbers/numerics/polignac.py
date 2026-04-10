"""
Polignac's conjecture (1849).

For every positive even integer d, there are infinitely many prime pairs
(p, p+d). The d = 2 case is the twin prime conjecture.

Hardy-Littlewood (1923) sharpened: the count
    π_d(x) := #{p ≤ x : p and p+d both prime}
satisfies the asymptotic
    π_d(x) ~ C_d · x / (log x)²
where the singular series is
    C_d = 2 C_2 · ∏_{q > 2, q | d} (q - 1) / (q - 2)
and C_2 = ∏_{p ≥ 3} (1 - 1/(p-1)²) ≈ 0.6601618158... is the twin prime constant.

Notable consequences:
- d = 2 (twins): C_2_HL = 2 C_2 ≈ 1.3203
- d = 4 (cousins): no odd prime divides 4, so C_4 = 2 C_2 ≈ 1.3203
  → twin and cousin prime counts should be EQUAL
- d = 6 (sexy): 3 | 6 → C_6 = 2 C_2 · 2 = 4 C_2 ≈ 2.6406
  → sexy primes should appear about TWICE as often as twins
- d = 30: 3, 5 | 30 → C_30 = 2 C_2 · 2 · (4/3) = (16/3) C_2 ≈ 3.5210
  → biggest "popular gap" of d ≤ 30

The "popularity" of d is governed by which small odd primes divide d.
The most "fertile" small d is d = 30 (= 2·3·5), then d = 60, etc.

Polignac's conjecture is OPEN for every d. Zhang (2013) proved bounded
gaps (some d ≤ 7×10⁷ has infinitely many pairs); Maynard-Tao (2014)
shrunk the bound to 246. The d = 2 case (twin primes) remains open.
"""
import numpy as np
from math import log
from sieve_core import sieve


def hl_constant_d(d, C_2=0.6601618158468695):
    """C_d = 2 C_2 · ∏_{q > 2, q | d} (q - 1)/(q - 2) for even d.
    Only ODD prime divisors of d contribute — strip factors of 2 first."""
    if d % 2 != 0:
        return 0.0
    n = d
    while n % 2 == 0:
        n //= 2  # remove all factors of 2
    factor = 1.0
    q = 3
    while q * q <= n:
        if n % q == 0:
            factor *= (q - 1) / (q - 2)
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        factor *= (n - 1) / (n - 2)
    return 2 * C_2 * factor


def odd_prime_divisors(d):
    """Distinct odd prime divisors of d."""
    n = d
    while n % 2 == 0:
        n //= 2
    out = []
    q = 3
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        out.append(n)
    return out


def count_pairs(prime_arr_int32, d, x_max):
    """Count primes p ≤ x_max with p + d also prime, using bitwise AND."""
    # prime_arr_int32 has length x_max + 1 (indexed 0..x_max)
    a = prime_arr_int32[:x_max + 1 - d]
    b = prime_arr_int32[d:x_max + 1]
    return int((a & b).sum())


def main():
    N = 10**8
    print(f"Polignac's conjecture / HL prediction for π_d(N) at N = {N}")
    print("=" * 76)

    print("Building sieve to 10^8...")
    sp = sieve(N)
    primes_arr = np.frombuffer(sp, dtype=np.uint8).astype(np.int32)
    total_primes = int(primes_arr.sum())
    print(f"  total primes: {total_primes}")
    print()

    # Li_2(x) = ∫_2^x dt / log² t (computed via scipy.quad)
    from scipy.integrate import quad
    Li2_N, _ = quad(lambda t: 1.0 / log(t) ** 2, 2, N, limit=200)
    print(f"Li_2({N}) = ∫_2^N dt/log²t = {Li2_N:.2f}")
    print()

    print(f"{'d':>4} {'C_d':>10} {'observed':>12} {'predicted':>12} "
          f"{'ratio':>10} {'note':>20}")
    print("-" * 78)

    even_gaps = list(range(2, 102, 2))  # d = 2, 4, ..., 100
    rows = []
    for d in even_gaps:
        C_d = hl_constant_d(d)
        observed = count_pairs(primes_arr, d, N)
        predicted = C_d * Li2_N
        ratio = observed / predicted if predicted > 0 else 0
        rows.append((d, C_d, observed, predicted, ratio))

        # Highlight notable gaps
        note = ""
        if d == 2:
            note = "twin primes"
        elif d == 4:
            note = "cousin primes"
        elif d == 6:
            note = "sexy primes"
        elif d == 30:
            note = "C_30 = 16/3 · C_2"
        elif d == 60:
            note = ""
        elif d == 100:
            note = ""

        print(f"{d:>4} {C_d:>10.6f} {observed:>12} {predicted:>12.0f} "
              f"{ratio:>10.4f} {note:>20}")

    print()

    # Aggregate analysis
    avg_ratio = np.mean([r[4] for r in rows])
    print(f"Mean ratio over d = 2, 4, ..., 100: {avg_ratio:.4f}")
    print(f"All ratios → 1 as N → ∞ (HL conjecture).")
    print()

    # Show the "popularity" pattern: rank by C_d
    print("Top 10 most 'fertile' even gaps d ≤ 100 (largest C_d):")
    print(f"{'rank':>6} {'d':>6} {'C_d':>12} {'observed':>12} "
          f"{'C_d/C_2':>12} {'odd prime divisors':>22}")
    print("-" * 80)
    sorted_rows = sorted(rows, key=lambda r: -r[1])
    C_2 = 0.6601618158468695
    for rank, (d, C_d, obs, pred, ratio) in enumerate(sorted_rows[:10], 1):
        c_ratio = C_d / (2 * C_2)  # the "extra factor" beyond twin
        odds = odd_prime_divisors(d)
        print(f"{rank:>6} {d:>6} {C_d:>12.6f} {obs:>12} {c_ratio:>12.4f} "
              f"{str(odds):>22}")


if __name__ == '__main__':
    main()
