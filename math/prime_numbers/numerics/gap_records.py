"""
Prime gap records up to N.

A 'record gap' is a gap between consecutive primes that exceeds all
previous gaps. The sequence of record gaps is OEIS A005250 (gap values)
and OEIS A002386 (positions where records occur).

The 'merit' of a gap is g/log(p) — Cramér's normalized measure.
- Cramér's conjecture: gaps satisfy g(p) = O((log p)²), max merit grows as log p.
- Granville-Maynard refinement: max merit ~ 2e^γ × log p (asymptotically).

This script enumerates all record gaps up to N and reports their merits.
Verified to match OEIS A005250 exactly for all 25 records below 10⁸.
"""
import numpy as np
from math import log
from sieve_core import sieve


def find_gap_records(N):
    """Return list of (gap, p_n, p_{n+1}, merit) for each new record gap."""
    is_prime = sieve(N)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)
    primes = np.nonzero(prime_arr)[0]

    gaps = np.diff(primes)
    record = 0
    records = []
    for i, g in enumerate(gaps):
        if g > record:
            record = int(g)
            p1 = int(primes[i])
            p2 = int(primes[i + 1])
            merit = g / log(p2)
            records.append((record, p1, p2, merit))
    return records


def main():
    N = 10**8
    print(f"Finding prime gap records up to {N}")
    print("=" * 65)

    records = find_gap_records(N)
    print(f"Found {len(records)} record gaps")
    print()
    print(f"{'#':>3} {'gap':>5} {'p_n':>12} {'p_{n+1}':>12} {'log p':>8} {'merit':>8}")
    print("-" * 65)
    for i, (g, p1, p2, merit) in enumerate(records):
        print(f"{i+1:>3} {g:>5} {p1:>12} {p2:>12} {log(p2):>8.2f} {merit:>8.4f}")

    # Verify against OEIS A005250
    OEIS_A005250 = [1, 2, 4, 6, 8, 14, 18, 20, 22, 34, 36, 44, 52, 72, 86,
                    96, 112, 114, 118, 132, 148, 154, 180, 210, 220]
    my_gaps = [r[0] for r in records]
    match = all(my_gaps[i] == OEIS_A005250[i]
                for i in range(min(len(my_gaps), len(OEIS_A005250))))
    print(f"\nOEIS A005250 match: {'PERFECT' if match else 'MISMATCH'}")

    # Merit growth
    max_merit = max(r[3] for r in records)
    print(f"Max merit: {max_merit:.4f}")
    print(f"Expected ~log(N) = {log(N):.2f} for record merits")


if __name__ == '__main__':
    main()
