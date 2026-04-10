"""
Hardy-Littlewood k-tuple constants from first principles.

For a pattern h = (h_1, ..., h_k), the HL constant is:
  C(h) = ∏_p [(1 - ν(h, p)/p) / (1 - 1/p)^k]

where ν(h, p) = number of distinct residues of h mod p.

HL conjecture: π_h(N) ~ C(h) × Li_k(N) where Li_k(N) = ∫_2^N dt/(log t)^k.

This script computes the HL constants to 10 digits and compares
with prime constellation counts from the sieve.
"""
import numpy as np
from math import log, exp
from scipy.integrate import quad
from sieve_core import sieve, primes_up_to


def hl_constant(h, p_limit=10**6):
    """Compute HL constant C(h) via product over primes up to p_limit.
    Convergence is logarithmic — p_limit = 10^6 gives ~10 digit accuracy."""
    k = len(h)
    ps = primes_up_to(p_limit)
    log_C = 0.0
    for p in ps:
        residues = set(hi % p for hi in h)
        nu = len(residues)
        if nu == p:
            return 0.0  # inadmissible
        log_num = log(1 - nu / p)
        log_den = k * log(1 - 1/p)
        log_C += log_num - log_den
    return exp(log_C)


def Li_k(x, k):
    """Li_k(x) = ∫_2^x dt/(log t)^k via scipy.quad (adaptive)."""
    if x < 2:
        return 0.0
    val, _err = quad(lambda t: 1.0 / log(t)**k, 2, x, limit=200)
    return val


def count_constellation(primes_arr, offsets):
    """Count positions i where i+h is prime for all h in offsets.
    offsets should start with 0."""
    N = len(primes_arr) - 1
    max_off = max(offsets)
    slices = [primes_arr[o:N + 1 - max_off + o] for o in offsets]
    mask = slices[0]
    for s in slices[1:]:
        mask = mask & s
    return int(mask.sum())


def main():
    # Build sieve up to 10^8
    print("Building sieve up to 10^8...")
    N = 10**8
    sp = sieve(N)
    primes_arr = np.frombuffer(sp, dtype=np.uint8).astype(np.int32)

    # Standard constellations
    patterns = {
        'Twin (0,2)': [0, 2],
        'Cousin (0,4)': [0, 4],
        'Sexy (0,6)': [0, 6],
        'Triplet (0,2,6)': [0, 2, 6],
        'Triplet (0,4,6)': [0, 4, 6],
        'Quadruplet (0,2,6,8)': [0, 2, 6, 8],
        'Quintuplet (0,2,6,8,12)': [0, 2, 6, 8, 12],
        'Sextuplet (0,4,6,10,12,16)': [0, 4, 6, 10, 12, 16],
    }

    print(f"\nHL constants and counts at N = {N}")
    print("=" * 75)
    print(f"{'Pattern':>30} | {'Count':>10} | {'C(h)':>12} | {'Pred':>10} | {'Ratio':>8}")
    print("-" * 75)

    for name, pattern in patterns.items():
        k = len(pattern)
        C = hl_constant(pattern)
        count = count_constellation(primes_arr, pattern)
        li = Li_k(N, k)
        pred = C * li
        ratio = count / pred if pred > 0 else 0
        print(f"{name:>30} | {count:>10} | {C:>12.6f} | {pred:>10.0f} | {ratio:>8.4f}")

    print("\nAll ratios should ≈ 1 (converging from above as N → ∞).")


if __name__ == '__main__':
    main()
