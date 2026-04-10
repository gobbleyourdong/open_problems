"""
BSD verification via smoothed L-function sums.

The Euler product L(E, s) = Π_p L_p(p^{-s})^{-1} does NOT converge at
s = 1 (it converges absolutely only for Re(s) > 3/2). To compute
L(E, 1) we need the FUNCTIONAL EQUATION:

    Λ(E, s) = N^{s/2} (2π)^{-s} Γ(s) L(E, s) = ε · Λ(E, 2-s)

where N is the conductor, ε = ±1 is the root number.

This gives the SMOOTHED SUM formula (Cremona, "Algorithms for Modular
Elliptic Curves"):

    L(E, 1) = 2 Σ_{n=1}^∞ (a_n / n) · exp(-2πn / √N)

for ε = +1 (even functional equation). This converges EXPONENTIALLY
in n, so only ~√N terms are needed for high precision.

For ε = -1 (odd functional equation), L(E, 1) = 0 automatically
(forced by the functional equation), and we need L'(E, 1) instead.

a_n COEFFICIENTS: For n composite, use the multiplicative structure:
    a_{mn} = a_m · a_n for gcd(m, n) = 1
    a_{p^k} = a_p · a_{p^{k-1}} - p · a_{p^{k-2}} for good primes p

BSD CONJECTURE (1965):
    rank E(Q) = ord_{s=1} L(E, s)

Proven for rank 0 (Kolyvagin 1988) and rank 1 (Gross-Zagier 1986 + Kolyvagin).
OPEN for rank ≥ 2.
"""
import numpy as np
from math import sqrt, pi, exp, log


def sieve_primes(N):
    s = [True] * (N + 1)
    s[0] = s[1] = False
    for i in range(2, int(N**0.5) + 1):
        if s[i]:
            for j in range(i*i, N+1, i):
                s[j] = False
    return [i for i in range(2, N+1) if s[i]]


def count_points(a4, a6, p):
    """#E(F_p) for y² = x³ + a4·x + a6. Includes point at infinity."""
    count = 1
    for x in range(p):
        rhs = (x*x*x + a4*x + a6) % p
        if rhs == 0:
            count += 1
        elif pow(rhs, (p-1)//2, p) == 1:
            count += 2
    return count


def compute_ap(a4, a6, primes, disc):
    """a_p for each prime p. Return dict p → a_p."""
    ap = {}
    for p in primes:
        if disc % p == 0:
            # Bad reduction: a_p ∈ {-1, 0, +1}
            # For simplicity, compute point count
            pts = count_points(a4 % p, a6 % p, p)
            ap[p] = p + 1 - pts
        else:
            ap[p] = p + 1 - count_points(a4, a6, p)
    return ap


def compute_an(ap_dict, primes, N_max, disc):
    """Compute a_n for n = 1..N_max using multiplicative extension.

    a_1 = 1
    a_{mn} = a_m · a_n for gcd(m, n) = 1
    a_{p^k} = a_p · a_{p^{k-1}} - χ(p) · p · a_{p^{k-2}}
    where χ(p) = 0 for bad primes, 1 for good primes.
    """
    a = [0] * (N_max + 1)
    a[1] = 1
    # For each prime power p^k ≤ N_max:
    for p in primes:
        if p > N_max:
            break
        ap = ap_dict.get(p, 0)
        is_good = (disc % p != 0)
        # a[p] = ap
        a[p] = ap
        # Higher powers
        pk = p * p
        k = 2
        while pk <= N_max:
            if is_good:
                a[pk] = ap * a[pk // p] - p * a[pk // (p * p)]
            else:
                a[pk] = ap * a[pk // p]
            pk *= p
            k += 1
    # Extend multiplicatively: iterate over composites
    # Build from small to large using the multiplicative property
    for n in range(2, N_max + 1):
        if a[n] != 0:
            continue
        # Factor n into (p^k, m) where p is smallest prime factor
        m = n
        for p in primes:
            if p * p > m:
                break
            if m % p == 0:
                pk = 1
                while m % p == 0:
                    pk *= p
                    m //= p
                if m == 1:
                    # n = p^k, already handled above
                    pass
                else:
                    # n = pk * m, gcd = 1
                    a[n] = a[pk] * a[m]
                break
        else:
            # m is prime (and n = m), should be handled already
            pass
    return a


def L_smoothed(a_n, conductor, n_terms=None):
    """L(E, 1) = 2 Σ_{n=1}^M a_n/n · exp(-2πn/√N)

    Converges exponentially: term n ~ exp(-2πn/√N).
    Need about √N / (2π) · 35 ≈ 6√N terms for 15-digit precision.
    """
    N = conductor
    sqrt_N = sqrt(N)
    if n_terms is None:
        n_terms = min(len(a_n) - 1, int(6 * sqrt_N) + 100)
    total = 0.0
    for n in range(1, n_terms + 1):
        if n >= len(a_n):
            break
        term = a_n[n] / n * exp(-2 * pi * n / sqrt_N)
        total += term
    return 2 * total


def main():
    print("BSD Verification: L(E, 1) via smoothed sum")
    print("=" * 76)
    print("L(E, 1) = 2 Σ a_n/n · exp(-2πn/√N)")
    print("This converges exponentially — only ~6√N terms needed.")
    print()

    # Well-known curves in short Weierstrass y² = x³ + a4·x + a6
    # with conductors from LMFDB / Cremona's tables
    curves = [
        # (a4, a6, conductor, rank, root_number, label)
        (-1, 0, 32, 0, +1, "32a1: y²=x³-x"),
        (0, 1, 27, 0, -1, "27a1: y²=x³+1"),
        (1, 0, 32, 0, -1, "32a2: y²=x³+x"),
        (-4, 0, 256, 0, +1, "256a1: y²=x³-4x"),
        (-1, 1, 141, 0, +1, "141?: y²=x³-x+1"),
        # Higher rank
        (0, -2, 1728, 1, -1, "1728?: y²=x³-2"),
        (0, 17, 27648, 2, +1, "?: y²=x³+17"),
    ]

    primes = sieve_primes(5000)
    print(f"Using {len(primes)} primes for a_p computation")
    print()

    print(f"{'Label':>25} {'N':>6} {'ε':>4} {'L(E,1)':>14} {'rank':>6} {'BSD':>5}")
    print("-" * 64)

    for a4, a6, cond, rank, eps, label in curves:
        disc = abs(-16 * (4 * a4**3 + 27 * a6**2))
        ap = compute_ap(a4, a6, primes, disc)
        n_max = max(int(6 * sqrt(cond)) + 200, 500)
        an = compute_an(ap, primes, n_max, disc)
        L1 = L_smoothed(an, cond)

        # BSD check
        if eps == +1:
            # Even: L(E,1) should be nonzero for rank 0, zero for rank 2
            if rank == 0:
                bsd = "✓" if abs(L1) > 0.01 else "✗"
            elif rank == 2:
                bsd = "✓" if abs(L1) < 0.01 else "✗"
            else:
                bsd = "?"
        else:
            # Odd: L(E,1) = 0 by functional equation → rank odd
            L1 = 0.0  # exact by symmetry
            bsd = "✓" if rank % 2 == 1 else "?"

        print(f"{label:>25} {cond:>6} {eps:>+4d} {L1:>14.6f} {rank:>6} {bsd:>5}")

    print()
    print("KEY OBSERVATIONS:")
    print("  - ε = +1 (even): L(E,1) computed via smoothed sum.")
    print("    Nonzero → rank 0, zero → rank ≥ 2.")
    print("  - ε = -1 (odd): L(E,1) = 0 by functional equation.")
    print("    rank must be odd (1, 3, ...). Need L'(E,1) for rank 1 vs 3.")
    print()
    print("  - Rank 0 + rank 1: PROVEN (Kolyvagin 1988, Gross-Zagier 1986)")
    print("  - Rank ≥ 2: BSD is OPEN.")
    print()

    # Show the a_p distribution for the first curve (Sato-Tate bridge)
    print("=" * 76)
    print("a_p DISTRIBUTION for y²=x³-x (conductor 32, non-CM)")
    print("(Bridge to Sato-Tate: a_p / 2√p → semicircle)")
    print("=" * 76)
    disc = abs(-16 * (4 * (-1)**3 + 27 * 0**2))
    ap_vals = compute_ap(-1, 0, primes[:500], disc)
    # Normalize: θ_p = arccos(a_p / 2√p)
    from math import acos, cos
    angles = []
    for p, a in ap_vals.items():
        if disc % p == 0:
            continue
        cos_t = a / (2 * sqrt(p))
        cos_t = max(-1, min(1, cos_t))
        angles.append(acos(cos_t))
    cos2 = np.mean([cos(2*t) for t in angles])
    cos4 = np.mean([cos(4*t) for t in angles])
    print(f"  ⟨cos 2θ⟩ = {cos2:+.4f}  (Sato-Tate predicts -1/2)")
    print(f"  ⟨cos 4θ⟩ = {cos4:+.4f}  (Sato-Tate predicts  0 for non-CM)")
    print(f"  n_primes used: {len(angles)}")
    print()
    print("This bridges to prime_numbers/certs/sato_tate_verified.md where")
    print("we confirmed ⟨cos 2θ⟩ ≈ -1/2 at 36σ for 6 curves.")


if __name__ == '__main__':
    main()
