"""
Rare prime classes — Wieferich, Wilson, and Wall-Sun-Sun primes.

These are "primes that pass an extra-strong test" — congruences that
go BEYOND Fermat's little theorem / Wilson's theorem / Lucas sequences
to modulus p² instead of p. Each test "lifts" a known mod-p identity
to mod-p², and only a vanishingly small set of primes satisfy the lift.

WIEFERICH PRIMES (1909):
    p prime such that 2^(p-1) ≡ 1 (mod p²)
By Fermat, 2^(p-1) ≡ 1 (mod p) always; the question is whether the
"lift" to p² holds. Heuristically, prob ≈ 1/p, so expected count up
to N is Σ 1/p ≈ log log N.

Known: ONLY 1093 (Meissner 1913) and 3511 (Beeger 1922).
Searched to 6.7×10^15 with no others found (BOINC project).

FLT connection: Wieferich (1909) proved that if FLT first case fails for
p (i.e., x^p + y^p = z^p with p ∤ xyz), then p is a Wieferich prime.
Mirimanoff (1910) added: 3^(p-1) ≡ 1 mod p² also required.
After Wiles 1995, FLT is proven so the connection is moot, but the
historical motivation is iconic.

WILSON PRIMES (folklore, hunted since the 19th century):
    p prime such that (p-1)! ≡ -1 (mod p²)
By Wilson's theorem, (p-1)! ≡ -1 (mod p) always; the lift to p² is
the question.

Known: ONLY 5, 13, 563. Searched to 2×10^13 with no others found.

WALL-SUN-SUN PRIMES (Fibonacci-Wieferich):
    p prime such that F_{p - (5|p)} ≡ 0 (mod p²)
where (5|p) is the Legendre symbol and F_n is the Fibonacci sequence.
By a Lucas sequence identity, F_{p - (5|p)} ≡ 0 (mod p) always.

Known: NONE. Searched to ~10^17 with no examples found.
Wall-Sun-Sun's nonexistence would imply (relatedly) Catalan-Mihailescu.

This script finds all examples in computationally accessible ranges.
"""
import numpy as np
from math import log
from sieve_core import sieve, primes_up_to


def is_wieferich(p):
    """Wieferich test: 2^(p-1) ≡ 1 mod p²."""
    return pow(2, p - 1, p * p) == 1


def find_wieferich(N):
    """All Wieferich primes ≤ N. Builds prime list, then tests each."""
    primes = primes_up_to(N)
    return [p for p in primes if p > 2 and is_wieferich(p)]


def find_wilson(N):
    """Wilson primes: (p-1)! ≡ -1 mod p²."""
    primes = primes_up_to(N)
    out = []
    for p in primes:
        p2 = p * p
        # Compute (p-1)! mod p²
        f = 1
        for i in range(1, p):
            f = (f * i) % p2
        if f == p2 - 1:  # ≡ -1 mod p²
            out.append(p)
    return out


def fibonacci_pair_mod(n, m):
    """Return (F_n mod m, F_{n+1} mod m) using fast doubling."""
    if n == 0:
        return (0, 1)
    a, b = fibonacci_pair_mod(n // 2, m)
    c = (a * (2 * b - a)) % m
    d = (a * a + b * b) % m
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % m)


def is_wall_sun_sun(p):
    """Wall-Sun-Sun test: F_{p - (5|p)} ≡ 0 mod p²."""
    # Legendre symbol (5|p):
    #   p ≡ ±1 mod 5: +1
    #   p ≡ ±2 mod 5: -1
    #   p = 5: 0 (skip)
    if p == 5:
        return False  # special case
    if p % 5 in (1, 4):
        chi = 1
    else:
        chi = -1
    n = p - chi
    F_n, _ = fibonacci_pair_mod(n, p * p)
    return F_n == 0


def find_wall_sun_sun(N):
    """All Wall-Sun-Sun primes ≤ N."""
    primes = primes_up_to(N)
    return [p for p in primes if p > 5 and is_wall_sun_sun(p)]


def main():
    print("Rare prime classes — Wieferich, Wilson, Wall-Sun-Sun")
    print("=" * 76)

    # ==============================
    # WIEFERICH
    # ==============================
    N_W = 10**7
    print(f"\n[WIEFERICH] 2^(p-1) ≡ 1 mod p², for prime p ≤ {N_W}")
    print("-" * 60)
    print("Searching... (this takes ~2 min for N = 10^7)")
    import time
    t0 = time.time()
    wieferichs = find_wieferich(N_W)
    dt = time.time() - t0
    print(f"  Search time: {dt:.1f}s")
    print(f"  Found: {wieferichs}")
    print(f"  Total: {len(wieferichs)}")
    print()
    print("Heuristic: P(p is Wieferich) ≈ 1/p")
    print(f"  Expected count up to N = Σ 1/p ≈ log log N = {log(log(N_W)):.4f}")
    print(f"  Observed: {len(wieferichs)}")
    print()
    print("Known to 6.7×10^15 (BOINC project, 2015): ONLY 1093 and 3511.")
    print()

    # Verify these are the famous ones
    if wieferichs == [1093, 3511]:
        print("✓ EXACT match: only 1093 (Meissner 1913) and 3511 (Beeger 1922)")
    else:
        print(f"Discrepancy: {wieferichs}")
    print()

    # Compute the "Wieferich quotient" w_p = (2^(p-1) - 1) / p mod p
    print("Wieferich quotient q_p(2) = (2^(p-1) - 1) / p mod p, for first 15 primes:")
    print(f"  p ≡ 0 mod p means p is a Wieferich prime.")
    print(f"{'p':>6} {'q_p(2)':>10}")
    print("-" * 18)
    primes_demo = primes_up_to(50)
    for p in primes_demo:
        if p == 2:
            continue
        q = ((pow(2, p - 1, p * p) - 1) // p) % p
        marker = " ← WIEFERICH" if q == 0 else ""
        print(f"{p:>6} {q:>10}{marker}")
    print()

    # ==============================
    # WILSON
    # ==============================
    N_Wi = 10**4  # bound — (p-1)! is O(p)
    print(f"\n[WILSON] (p-1)! ≡ -1 mod p², for prime p ≤ {N_Wi}")
    print("-" * 60)
    print("Searching...")
    t0 = time.time()
    wilsons = find_wilson(N_Wi)
    dt = time.time() - t0
    print(f"  Search time: {dt:.1f}s")
    print(f"  Found: {wilsons}")
    print()
    print("Known to 2×10^13 (Costa-Gerbicz-Harvey 2013): ONLY 5, 13, 563.")

    if wilsons == [5, 13, 563]:
        print("✓ EXACT match: 5, 13, 563 — only known Wilson primes.")
    print()

    # ==============================
    # WALL-SUN-SUN
    # ==============================
    N_WSS = 10**6
    print(f"\n[WALL-SUN-SUN] F_{{p-(5|p)}} ≡ 0 mod p², for prime p ≤ {N_WSS}")
    print("-" * 60)
    print("Searching... (Fibonacci via fast-doubling, fast)")
    t0 = time.time()
    wss = find_wall_sun_sun(N_WSS)
    dt = time.time() - t0
    print(f"  Search time: {dt:.1f}s")
    print(f"  Found: {wss}")
    print()
    print("Known to 9.7×10^14 (Dorais-Klyve 2010): NONE — no Wall-Sun-Sun")
    print("primes have ever been found.")
    if not wss:
        print("✓ Our search agrees: none in [2, 10^6].")
    print()

    # ==============================
    # SUMMARY
    # ==============================
    print()
    print("=" * 76)
    print("SUMMARY")
    print("=" * 76)
    print()
    print("| Class       | Test                          | Our search | Known total |")
    print("|-------------|-------------------------------|------------|-------------|")
    print(f"| Wieferich   | 2^(p-1) ≡ 1 mod p²            | {len(wieferichs)} ≤ 10^7 | 2 ≤ 6.7×10^15 |")
    print(f"| Wilson      | (p-1)! ≡ -1 mod p²            | {len(wilsons)} ≤ 10^4 | 3 ≤ 2×10^13   |")
    print(f"| Wall-S-S    | F_{{p-(5|p)}} ≡ 0 mod p²       | {len(wss)} ≤ 10^6 | 0 ≤ 10^17     |")
    print()
    print("Each class lifts a mod-p congruence (Fermat, Wilson, Lucas) to mod-p².")
    print("Heuristic: probability ≈ 1/p ⇒ expected count ≈ log log N.")
    print("Wall-Sun-Sun is the most striking — none known anywhere despite searches")
    print("to 10^17 = 6 orders of magnitude past where we'd expect to find one.")


if __name__ == '__main__':
    main()
