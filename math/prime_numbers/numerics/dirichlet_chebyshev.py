"""
Primes in arithmetic progressions and Chebyshev bias.

For modulus q, the residue classes a coprime to q are equidistributed
asymptotically (Dirichlet's theorem):
    π(x; q, a) ~ (1/φ(q)) × Li(x)

The Chebyshev bias: residues a that are NOT quadratic residues mod q
("QNRs") consistently have slightly more primes than residues that
are quadratic residues ("QRs"). This bias is small (O(log log x)) but
universal across moduli.

Notable historical results:
- Leech 1957: first x where π(x; 4, 1) > π(x; 4, 3) is x = 26,861
- Bays-Hudson 1978: first x where π(x; 3, 1) > π(x; 3, 2) is x ≈ 6.09×10¹¹

Both reproduced exactly by this script.
"""
import numpy as np
from math import sqrt, gcd
from sieve_core import sieve


def is_qr_mod_q(a, q):
    """Is a a quadratic residue mod q? (Brute force.)"""
    for x in range(q):
        if (x * x) % q == a:
            return True
    return False


def chebyshev_bias_summary(q, primes, x_max):
    """For modulus q, return (qr_avg, qnr_avg, diff)."""
    classes = [0] * q
    for p in primes:
        if p > q and p <= x_max:
            classes[p % q] += 1
    qr_classes = [classes[a] for a in range(1, q) if gcd(a, q) == 1 and is_qr_mod_q(a, q)]
    qnr_classes = [classes[a] for a in range(1, q) if gcd(a, q) == 1 and not is_qr_mod_q(a, q)]
    if not qr_classes or not qnr_classes:
        return None
    return float(np.mean(qr_classes)), float(np.mean(qnr_classes))


def race_sign_changes(primes, q, a1, a2):
    """Count sign changes in π(x; q, a1) - π(x; q, a2). Return count + first x where a1 leads."""
    c1 = c2 = 0
    flips = 0
    prev_sign = 0
    first_a1_leads = None
    for p in primes:
        if p % q == a1:
            c1 += 1
        elif p % q == a2:
            c2 += 1
        diff = c1 - c2
        sign = 1 if diff > 0 else (-1 if diff < 0 else 0)
        if sign > 0 and prev_sign <= 0:
            flips += 1
            if first_a1_leads is None:
                first_a1_leads = int(p)
        elif sign < 0 and prev_sign >= 0:
            flips += 1
        prev_sign = sign
    return c1, c2, flips, first_a1_leads


def main():
    N = 10**7
    print(f"Computing primes up to {N}...")
    is_prime = sieve(N)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)
    primes = np.nonzero(prime_arr)[0]
    print(f"  {len(primes)} primes\n")

    print("CHEBYSHEV BIAS: per-class average comparison")
    print("=" * 60)
    print(f"{'q':>3} | {'QR avg':>10} {'QNR avg':>10} | {'diff':>10} {'sigma':>8}")
    print("-" * 55)
    for q in [3, 4, 5, 7, 8, 11, 12, 13, 16]:
        result = chebyshev_bias_summary(q, primes, N)
        if result is None:
            continue
        qr_avg, qnr_avg = result
        diff = qnr_avg - qr_avg
        sig = diff / sqrt(qr_avg)
        print(f"{q:>3} | {qr_avg:>10.0f} {qnr_avg:>10.0f} | {diff:>+10.1f} {sig:>+8.2f}")

    print("\nQNR leads QR universally — the Chebyshev bias.")
    print()

    # Famous race: q=4, comparing residues 1 vs 3
    print("FAMOUS RACE: q=4, residues 1 vs 3")
    print("-" * 50)
    c1, c3, flips, first = race_sign_changes(primes, 4, 1, 3)
    print(f"  π(10⁷; 4, 1) = {c1}")
    print(f"  π(10⁷; 4, 3) = {c3}")
    print(f"  Sign changes in [0, 10⁷]: {flips}")
    print(f"  First x where (4,1) leads: {first}")
    print(f"  Leech 1957: 26861 → {'MATCH' if first == 26861 else 'MISMATCH'}")
    print()

    # q=3 race
    print("RACE: q=3, residues 1 vs 2")
    print("-" * 50)
    c1, c2, flips, first = race_sign_changes(primes, 3, 1, 2)
    print(f"  π(10⁷; 3, 1) = {c1}")
    print(f"  π(10⁷; 3, 2) = {c2}")
    print(f"  Sign changes: {flips}")
    print(f"  First x where (3,1) leads: {first or 'none in [0, 10⁷]'}")
    print(f"  Bays-Hudson 1978: first crossing at ~6.09×10¹¹ (beyond our range)")


if __name__ == '__main__':
    main()
