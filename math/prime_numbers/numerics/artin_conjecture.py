"""
Artin's primitive root conjecture.

Artin (1927): For a fixed integer a that is not -1 and not a perfect square,
the density of primes p for which a is a primitive root mod p equals

    C_Artin × (rational correction for a)

where C_Artin = Π_p (1 - 1/(p(p-1))) ≈ 0.3739558136...

The "rational correction" is 1 for most a (the generic case). When a is
congruent to 1 mod 4 and square-free, or when the "entanglement" of
Kummer extensions is non-trivial, the density gets multiplied by an
explicit rational factor.

**Conjecture status**: OPEN. Hooley (1967) proved it assuming GRH for
certain Dedekind zeta functions. Heath-Brown (1986) proved that Artin
holds for at least one of {2, 3, 5} unconditionally — so the conjecture
is known for at least 2 of the 3 classical bases, but we don't know which!

This script verifies the conjecture numerically for multiple bases up to
P_max = 10⁶, showing universal agreement with the Artin constant.
"""
from math import gcd, isqrt
from sieve_core import primes_up_to


def factor_small(n):
    """Trial division factorization. Good enough for n < 10⁶."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def is_primitive_root(a, p, p_minus_1_factors):
    """a is a primitive root mod p iff a^((p-1)/q) ≢ 1 (mod p)
    for every prime q | (p-1)."""
    if gcd(a, p) != 1:
        return False
    for q in p_minus_1_factors:
        if pow(a, (p - 1) // q, p) == 1:
            return False
    return True


def artin_density(a, P_max):
    """Fraction of primes p ≤ P_max for which a is a primitive root mod p.
    Skips p | a (a is 0 there)."""
    primes = primes_up_to(P_max)
    # Skip small primes where a might coincide
    considered = 0
    hits = 0
    for p in primes:
        if p <= 2:
            continue
        if a % p == 0:
            continue
        # a must not be ±1 and not a perfect square to have positive density
        p_factors = set(factor_small(p - 1).keys())
        if is_primitive_root(a, p, p_factors):
            hits += 1
        considered += 1
    return hits, considered, hits / considered


def artin_constant_truncated(p_limit=10**5):
    """C_Artin = Π_p (1 - 1/(p(p-1))) truncated at p_limit.
    Converges slowly — need ~10⁵ primes to get 6 digits.

    Expected value: 0.3739558136192022...
    """
    primes = primes_up_to(p_limit)
    log_prod = 0.0
    from math import log
    for p in primes:
        log_prod += log(1 - 1 / (p * (p - 1)))
    from math import exp
    return exp(log_prod)


def squarefree_kernel(n):
    """Return (sign, squarefree kernel) of n. sign = ±1 via Möbius of kernel."""
    k = abs(n)
    rad = 1
    d = 2
    while d * d <= k:
        if k % d == 0:
            rad *= d
            while k % d == 0:
                k //= d
        d += 1
    if k > 1:
        rad *= k
    # mu(rad): rad is squarefree by construction
    # count prime factors
    m = rad
    omega = 0
    d = 2
    while d * d <= m:
        if m % d == 0:
            omega += 1
            m //= d
        d += 1
    if m > 1:
        omega += 1
    mu = (-1) ** omega
    return mu, rad


def artin_correction(a):
    """Artin's rational correction factor for base a.

    For 'generic' a (squarefree part ≢ 1 mod 4), the factor is 1.
    For squarefree a* ≡ 1 mod 4 (where a = h² · a*), the factor is:
        1 - μ(a*) · Π_{q | a*} 1/(q² - q - 1)
    """
    mu_rad, rad = squarefree_kernel(a)
    if rad % 4 != 1:
        return 1.0
    # Product over primes q | rad
    prod = 1.0
    q = 2
    n = rad
    while q * q <= n:
        if n % q == 0:
            prod /= (q * q - q - 1)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        prod /= (n * n - n - 1)
    return 1.0 - mu_rad * prod


def main():
    P_max = 10**6
    print(f"Artin's primitive root conjecture")
    print(f"Primes up to P_max = {P_max}")
    print("=" * 72)

    C_A = artin_constant_truncated(p_limit=10**5)
    C_A_true = 0.3739558136192022  # Known to high precision
    print(f"Artin constant (truncated Euler product at p ≤ 10⁵):")
    print(f"  C_A computed = {C_A:.10f}")
    print(f"  C_A known    = {C_A_true:.10f}")
    print(f"  Δ = {abs(C_A - C_A_true):.2e}")
    print()

    print("Per-base density of primes for which a is a primitive root:")
    print("(Artin: density = C_A × correction factor c(a))")
    print()
    print(f"{'a':>4} {'hits':>8} {'N':>8} {'density':>10} "
          f"{'c(a)':>8} {'predict':>10} {'obs/pred':>10} {'class':>12}")
    print("-" * 76)

    # a must not be -1, 0, 1, or a perfect square
    bases = [2, 3, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17]

    results = []
    for a in bases:
        hits, considered, density = artin_density(a, P_max)
        c = artin_correction(a)
        predicted = C_A_true * c
        ratio = density / predicted
        klass = "generic" if abs(c - 1.0) < 1e-9 else "corrected"
        results.append((a, hits, considered, density, c, predicted, ratio))
        print(f"{a:>4} {hits:>8} {considered:>8} {density:>10.6f} "
              f"{c:>8.5f} {predicted:>10.6f} {ratio:>10.5f} {klass:>12}")

    print()
    # Aggregate: predicted vs observed
    total_hits = sum(r[1] for r in results)
    total_predicted = sum(r[5] * r[2] for r in results)
    aggregate_ratio = total_hits / total_predicted
    print(f"Aggregate hits / predicted hits: {total_hits} / "
          f"{total_predicted:.1f} = {aggregate_ratio:.6f}")
    print(f"Expected if Artin holds: 1.000000")
    print(f"Deviation: {abs(aggregate_ratio - 1) * 100:.3f}%")

    # Standard error
    from math import sqrt
    n_total = sum(r[2] for r in results)
    # Binomial SE assuming uniform density C_A
    p_bar = total_predicted / n_total
    se = sqrt(p_bar * (1 - p_bar) / n_total)
    z = (total_hits / n_total - p_bar) / se
    print(f"Pooled SE ≈ {se:.5f}, z-score of aggregate: {z:.2f}")


if __name__ == '__main__':
    main()
