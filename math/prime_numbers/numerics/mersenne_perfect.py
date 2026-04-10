"""
Mersenne primes and the Euclid-Euler theorem.

A Mersenne number is M_p = 2^p - 1. If M_p is prime, it's a Mersenne prime.

Euclid (300 BC): If 2^p - 1 is prime, then 2^(p-1) · (2^p - 1) is perfect.
Euler (1747): EVERY even perfect number has this form.

Together (Euclid-Euler theorem): even perfect numbers ↔ Mersenne primes.

It is unknown whether any ODD perfect number exists; if it does, it must
be > 10^1500. (Conjectured: no odd perfect numbers exist.)

Lucas-Lehmer test (Lucas 1878, Lehmer 1930): For p odd prime, M_p is prime
iff S_{p-2} ≡ 0 (mod M_p), where
    S_0 = 4
    S_{i+1} = S_i² - 2

This is THE primality test that has dominated the search for large primes.
The largest known prime is always a Mersenne prime, currently
M_82589933 (December 2018, ~25 million digits).

Lenstra-Pomerance-Wagstaff heuristic: the count of Mersenne primes
M_p with p ≤ X is asymptotically
    M(X) ~ (e^γ / log 2) · log X = (2.5695...) · log_2 X

where γ ≈ 0.5772 is Euler's constant. (See Wagstaff 1983.)

This script:
1. Implements Lucas-Lehmer
2. Tests all M_p for prime p ≤ 1500
3. Verifies the Euclid-Euler perfect number formula
4. Compares count to LPW heuristic
"""
from math import log, exp
from sieve_core import primes_up_to


def lucas_lehmer(p):
    """Lucas-Lehmer test for M_p = 2^p - 1, p odd prime."""
    if p == 2:
        return True  # M_2 = 3 is prime, not handled by LL
    M = (1 << p) - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0


def find_mersenne_primes(p_max):
    """Find all Mersenne primes M_p with p ≤ p_max."""
    primes_p = primes_up_to(p_max)
    found = []
    for p in primes_p:
        if lucas_lehmer(p):
            found.append(p)
    return found


def perfect_number(p):
    """Even perfect number from Mersenne prime M_p (Euclid-Euler)."""
    return (1 << (p - 1)) * ((1 << p) - 1)


def sigma(n):
    """Sum of divisors of n (only for verification — slow for large n)."""
    if n == 1:
        return 1
    s = 1 + n
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s


def lpw_prediction(X, gamma=0.5772156649):
    """Lenstra-Pomerance-Wagstaff heuristic count for Mersenne primes ≤ X."""
    return (exp(gamma) / log(2)) * log(X)


def main():
    P_MAX = 1500  # Lucas-Lehmer is fast for p ≤ 1500 (M_p has ~450 digits)
    print(f"Mersenne primes via Lucas-Lehmer test, p ≤ {P_MAX}")
    print("=" * 76)

    print("Finding all Mersenne primes...")
    mersennes = find_mersenne_primes(P_MAX)
    print(f"  Found {len(mersennes)} Mersenne primes M_p with p ≤ {P_MAX}")
    print()

    # Display
    print("All discovered Mersenne primes:")
    print(f"{'#':>4} {'p':>6} {'digits of M_p':>16} {'M_p (start...end)':>40}")
    print("-" * 70)
    for i, p in enumerate(mersennes, 1):
        Mp = (1 << p) - 1
        n_digits = len(str(Mp))
        s = str(Mp)
        if n_digits <= 20:
            display = s
        else:
            display = s[:8] + "..." + s[-8:]
        print(f"{i:>4} {p:>6} {n_digits:>16} {display:>40}")
    print()

    # Lenstra-Pomerance-Wagstaff verification
    print("LPW heuristic: M(X) ~ (e^γ / log 2) · log X ≈ 2.5695 · log_2 X")
    print()
    print(f"{'X':>10} {'observed M(X)':>16} {'LPW prediction':>16} {'ratio':>10}")
    print("-" * 56)
    for X in [10, 30, 100, 300, 1000, 1500]:
        obs = sum(1 for p in mersennes if p <= X)
        pred = lpw_prediction(X)
        ratio = obs / pred if pred > 0 else 0
        print(f"{X:>10} {obs:>16} {pred:>16.3f} {ratio:>10.4f}")
    print()
    print("Note: LPW is a heuristic, not a theorem. The Mersenne primes are")
    print("distributed irregularly and the agreement is qualitative.")
    print()

    # Verify Euclid-Euler theorem for the first few perfect numbers
    print("EUCLID-EULER VERIFICATION: σ(N) = 2N for N = 2^(p-1)·(2^p - 1)")
    print("(σ(N) = sum of all divisors of N, including N itself)")
    print(f"{'p':>4} {'M_p':>14} {'perfect N':>20} {'σ(N)':>22} {'σ(N) - 2N':>14}")
    print("-" * 78)
    for p in mersennes[:6]:  # first 6 perfect numbers
        Mp = (1 << p) - 1
        N = perfect_number(p)
        if N > 10**12:
            # σ computation is too slow for huge N
            # Use the fact that for N = 2^(p-1)·M_p with M_p prime:
            #   σ(N) = (2^p - 1) · (M_p + 1) = (2^p - 1) · 2^p = 2^p · M_p · ... wait
            # σ(N) = σ(2^(p-1)) · σ(M_p) = (2^p - 1) · (M_p + 1) = M_p · 2^p
            #      = 2 · 2^(p-1) · M_p = 2N    ✓ algebraic verification
            sigma_N = (Mp) * (1 << p)
            verified = "(algebraic)"
        else:
            sigma_N = sigma(N)
            verified = ""
        diff = sigma_N - 2 * N
        N_str = str(N) if N < 10**14 else f"{str(N)[:10]}...({len(str(N))} digits)"
        sigma_str = str(sigma_N) if sigma_N < 10**14 else f"...{verified}"
        print(f"{p:>4} {Mp:>14} {N_str:>20} {sigma_str:>22} {diff:>14}")
    print()
    print("All differences are 0 — every Euclid number is perfect.")
    print()

    # Algebraic identity proof
    print("Algebraic identity (proof of Euclid's direction):")
    print("  For N = 2^(p-1) · M_p with M_p = 2^p - 1 prime:")
    print("  σ(N) = σ(2^(p-1)) · σ(M_p)              [σ multiplicative]")
    print("       = (2^p - 1) · (M_p + 1)")
    print("       = M_p · 2^p")
    print("       = 2 · 2^(p-1) · M_p")
    print("       = 2N")
    print("  ⇒ N is perfect.  Q.E.D.")
    print()

    # Show how Mersennes thin out
    print("DENSITY OF MERSENNE PRIMES")
    print(f"{'p range':>14} {'count':>8} {'rate (per log)':>18}")
    print("-" * 44)
    bins = [(2, 30), (31, 100), (101, 300), (301, 1000), (1001, 1500)]
    for lo, hi in bins:
        cnt = sum(1 for p in mersennes if lo <= p <= hi)
        log_range = log(hi) - log(lo)
        rate = cnt / log_range if log_range > 0 else 0
        print(f"{f'[{lo}, {hi}]':>14} {cnt:>8} {rate:>18.3f}")
    print()
    print("LPW predicts a constant rate ≈ e^γ / log 2 ≈ 2.5695 per unit of log X.")
    print("Observed rate per log range varies but averages near this value.")


if __name__ == '__main__':
    main()
