"""
Carmichael numbers — the composites that fool Fermat's little theorem for
EVERY base coprime to them.

A Carmichael number is a composite n such that
    a^(n-1) ≡ 1 (mod n)    for all integers a with gcd(a, n) = 1.

Smallest: 561 = 3 × 11 × 17.

KORSELT'S CRITERION (1899): n is a Carmichael number if and only if
  1. n is composite
  2. n is squarefree
  3. (p - 1) | (n - 1) for every prime p dividing n

Korselt published the criterion 11 years before Carmichael actually found
the first example. The criterion is straightforward to verify but finding
n satisfying it requires building the right factorization.

Historical note:
- 1910: Carmichael publishes the smallest examples
- 1939: Chernick gives the formula (6k+1)(12k+1)(18k+1) for some k
- 1956: Erdős conjectures C(x) > x^(1-ε)
- 1994: Alford-Granville-Pomerance prove infinitely many Carmichael numbers
- Best lower bound: C(x) > x^(2/7) (Harman 2008)
- Best upper bound: C(x) < x · exp(-c log x log log log x / log log x)
                                                       (Pomerance 1981)

Carmichael numbers are the reason **Fermat's primality test alone is not
sufficient**. The Miller-Rabin test (which adds the strong primality
condition) handles them by introducing witnesses for compositeness.

This script:
1. Builds the smallest-prime-factor (SPF) sieve to 10^7
2. Tests each composite via Korselt's criterion
3. Lists all Carmichael numbers found and their factorizations
4. Verifies a few via brute Fermat tests with random bases
5. Compares the count to Pomerance's heuristic
"""
import numpy as np
from math import log, exp
from sieve_core import sieve


def spf_sieve(N):
    """Smallest prime factor for each n ≤ N."""
    spf = np.zeros(N + 1, dtype=np.int32)
    for p in range(2, N + 1):
        if spf[p] == 0:  # p is prime
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


def factor(n, spf):
    """Return list of (prime, exponent) pairs via SPF lookup."""
    out = []
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def is_carmichael(n, spf):
    """Korselt's criterion check."""
    if n < 4:
        return False
    facs = factor(n, spf)
    if len(facs) < 3:
        return False  # Carmichael needs ≥ 3 distinct primes
    for _p, e in facs:
        if e > 1:
            return False  # not squarefree
    for p, _e in facs:
        if (n - 1) % (p - 1) != 0:
            return False
    return True


def find_carmichael_numbers(N):
    """All Carmichael numbers ≤ N."""
    print(f"Building SPF sieve up to {N}...")
    spf = spf_sieve(N)
    print(f"  done, scanning composites for Korselt...")
    out = []
    # Carmichael numbers are odd (Korselt forces it: if 2 | n then (2-1) = 1 | (n-1) trivially,
    # but n - 1 odd ⇒ n even ⇒ n ≥ 6 needs another prime, etc. Easier: just skip n even.)
    for n in range(9, N + 1, 2):
        if spf[n] == n:
            continue  # n is prime
        if is_carmichael(n, spf):
            out.append(n)
    return out


def fermat_witness_count(n, n_bases=20, rng_seed=42):
    """For composite n, return how many of n_bases random bases a satisfy
    a^(n-1) ≡ 1 (mod n) (i.e., FAIL to detect compositeness). Should be
    n_bases for Carmichael numbers (modulo gcd(a, n) > 1)."""
    rng = np.random.default_rng(rng_seed)
    fooled = 0
    for _ in range(n_bases):
        a = int(rng.integers(2, n - 1))
        if pow(a, n - 1, n) == 1:
            fooled += 1
    return fooled


def pomerance_upper(x):
    """Pomerance 1981 upper bound: C(x) < x · exp(-c log x log log log x / log log x).
    Use c = 1 for the leading constant; this gives an upper-bound shape."""
    if x < 100:
        return float(x)
    log_x = log(x)
    log_log_x = log(log_x)
    log_log_log_x = log(log_log_x) if log_log_x > 1 else 0.5
    return x * exp(-log_x * log_log_log_x / log_log_x)


def main():
    N = 10**7
    print("Carmichael numbers via Korselt's criterion")
    print("=" * 76)

    cs = find_carmichael_numbers(N)
    print(f"Found {len(cs)} Carmichael numbers ≤ {N}")
    print()

    # Reference counts (OEIS A055553 — count of Carmichael ≤ 10^k):
    ref = {3: 1, 4: 7, 5: 16, 6: 43, 7: 105, 8: 255, 9: 646}
    print("Verification against OEIS A055553:")
    print(f"{'X':>10} {'observed':>10} {'OEIS':>10} {'match':>8}")
    print("-" * 46)
    for k in range(3, 8):
        X = 10 ** k
        obs = sum(1 for c in cs if c <= X)
        if k in ref and X <= N:
            oeis = ref[k]
            match = "✓" if obs == oeis else "✗"
            print(f"{X:>10} {obs:>10} {oeis:>10} {match:>8}")
    print()

    # Show first 20 Carmichael numbers with factorizations
    print("First 20 Carmichael numbers with factorizations:")
    spf = spf_sieve(N)
    for c in cs[:20]:
        facs = factor(c, spf)
        fac_str = " × ".join(str(p) for p, _ in facs)
        print(f"  {c:>12} = {fac_str}")
    print()

    # The famous (6k+1)(12k+1)(18k+1) Chernick triples in our list
    print("Chernick-style Carmichael numbers (6k+1)(12k+1)(18k+1) found:")
    chernicks = []
    for k in range(1, 200):
        a = 6 * k + 1
        b = 12 * k + 1
        c = 18 * k + 1
        n = a * b * c
        if n > N:
            break
        # Need a, b, c all prime
        from sympy import isprime
        if isprime(a) and isprime(b) and isprime(c):
            chernicks.append((k, a, b, c, n))
            print(f"  k={k:>4}: ({a}, {b}, {c}) → n = {n:>12}  "
                  f"(in our list: {'✓' if n in set(cs) else '✗'})")
    print(f"Total Chernick Carmichaels in [4, 10^7]: {len(chernicks)}")
    print()

    # Verify a few via brute Fermat tests
    print("FERMAT FAILURE verification — testing 20 random bases per number:")
    print("(For a Carmichael number, ALL coprime bases satisfy a^(n-1) ≡ 1 mod n)")
    print(f"{'n':>10} {'fooled / 20':>12} {'spf':>6}")
    print("-" * 32)
    for c in cs[:10]:
        f = fermat_witness_count(c)
        print(f"{c:>10} {f:>12} {int(spf[c]):>6}")
    print()

    # Pomerance heuristic
    print("Pomerance heuristic (1981 upper bound, conjecturally tight):")
    print(f"{'X':>10} {'C(X) obs':>12} {'Pomerance UB':>16} {'ratio':>10}")
    print("-" * 52)
    for k in range(3, 8):
        X = 10 ** k
        obs = sum(1 for c in cs if c <= X)
        ub = pomerance_upper(X)
        ratio = obs / ub if ub > 0 else 0
        print(f"{X:>10} {obs:>12} {ub:>16.2f} {ratio:>10.6f}")
    print()
    print("The Pomerance bound is C(X) < X exp(-log X log log log X / log log X).")
    print("Observed C(X) is much smaller than X but grows polynomially-ish.")
    print()

    # Empirical growth rate
    print("Empirical growth: C(X) ~ X^α for some α between 1/3 and 1?")
    print(f"{'k':>4} {'C(10^k)':>10} {'log_10 C':>10} {'α est':>10}")
    print("-" * 38)
    last_log_C = None
    for k in range(3, 8):
        X = 10 ** k
        obs = sum(1 for c in cs if c <= X)
        if obs == 0:
            continue
        log_C = log(obs) / log(10)
        alpha = log_C / k
        print(f"{k:>4} {obs:>10} {log_C:>10.4f} {alpha:>10.4f}")
        last_log_C = log_C


if __name__ == '__main__':
    main()
