"""
Twin primes, prime gaps, and Cramér's conjecture.

Questions:
1. How many twin primes ≤ N? Compare with Hardy-Littlewood prediction
     π_2(N) ~ 2 C_2 N / (log N)²  where C_2 = 0.660161... (twin prime constant)
2. What is the maximum gap g(p) for p ≤ N? Cramér: g(p) ~ (log p)²
3. Distribution of gaps — is it consistent with random-prime heuristic?
"""
import numpy as np
import time
from sieve_core import sieve


def analyze_twins_and_gaps(N):
    is_prime = sieve(N)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)
    primes = np.nonzero(prime_arr)[0]

    # Twin primes: p such that p and p+2 are both prime
    # Generate pairs
    twin_mask = np.zeros_like(prime_arr)
    twin_mask[:-2] = prime_arr[:-2] & prime_arr[2:]
    n_twins = int(twin_mask.sum())

    # Gaps between consecutive primes
    gaps = np.diff(primes)
    max_gap = int(gaps.max())
    max_gap_idx = int(gaps.argmax())
    max_gap_at = int(primes[max_gap_idx])

    # Distribution of gap sizes
    gap_hist = np.bincount(gaps)

    return {
        'N': N,
        'n_primes': len(primes),
        'n_twins': n_twins,
        'max_gap': max_gap,
        'max_gap_at_prime': max_gap_at,
        'gap_hist': gap_hist,
        'gaps': gaps,
    }


def main():
    print("TWIN PRIMES AND PRIME GAPS", flush=True)
    print("=" * 60, flush=True)

    C_2 = 0.6601618158

    for N in [10**5, 10**6, 10**7, 10**8]:
        t0 = time.time()
        r = analyze_twins_and_gaps(N)
        dt = time.time() - t0

        print(f"\nN = {N}:", flush=True)
        print(f"  π(N) = {r['n_primes']}", flush=True)
        print(f"  π_2(N) = {r['n_twins']} (twin primes)", flush=True)

        # Hardy-Littlewood twin prime prediction
        hl_twin = 2 * C_2 * N / (np.log(N) ** 2)
        ratio = r['n_twins'] / hl_twin
        print(f"  HL prediction: {hl_twin:.0f}, ratio = {ratio:.4f}", flush=True)

        print(f"  max gap: {r['max_gap']} (at prime {r['max_gap_at_prime']})", flush=True)

        # Cramér: max gap ~ (log p)²
        log_p = np.log(r['max_gap_at_prime'])
        cramer_pred = log_p ** 2
        cramer_ratio = r['max_gap'] / cramer_pred
        print(f"  Cramér (log p)² = {cramer_pred:.1f}, ratio = {cramer_ratio:.2f}", flush=True)

        # Common gap sizes
        hist = r['gap_hist']
        top_gaps = np.argsort(hist)[::-1][:5]
        print(f"  Most common gaps:", flush=True)
        for g in top_gaps:
            if hist[g] > 0:
                print(f"    gap={g}: {hist[g]} occurrences ({hist[g]/(r['n_primes']-1)*100:.1f}%)", flush=True)

        print(f"  Time: {dt:.1f}s", flush=True)

    # Now: look for SIGN CHANGES in prime race π(x;4,3) - π(x;4,1)
    # (Chebyshev bias: primes ≡ 3 mod 4 usually exceed primes ≡ 1 mod 4)
    print("\nPRIME RACE: π(x;4,1) vs π(x;4,3)", flush=True)
    print("-" * 50, flush=True)
    N_race = 10**6
    is_prime = sieve(N_race)
    prime_arr = np.frombuffer(is_prime, dtype=np.uint8)

    # Cumulative counts
    residue_4_1 = np.zeros(N_race + 1, dtype=np.int64)
    residue_4_3 = np.zeros(N_race + 1, dtype=np.int64)
    count_1 = count_3 = 0
    first_flip = None
    for p in range(3, N_race + 1):
        if prime_arr[p]:
            if p % 4 == 1:
                count_1 += 1
            elif p % 4 == 3:
                count_3 += 1
        residue_4_1[p] = count_1
        residue_4_3[p] = count_3

    # Find sign changes of (π(x;4,1) - π(x;4,3))
    diff = residue_4_1.astype(np.int64) - residue_4_3.astype(np.int64)
    # Sign flips where diff crosses 0
    flips = []
    prev_sign = 0
    for x in range(5, N_race + 1):
        curr = diff[x]
        if curr > 0 and prev_sign <= 0:
            flips.append(('4,1 leads', x))
            prev_sign = 1
        elif curr < 0 and prev_sign >= 0:
            flips.append(('4,3 leads', x))
            prev_sign = -1
        elif curr == 0 and prev_sign != 0:
            pass  # tie

    print(f"  π(x;4,1) vs π(x;4,3) up to {N_race}:", flush=True)
    print(f"  Final: π({N_race};4,1) = {count_1}, π({N_race};4,3) = {count_3}", flush=True)
    print(f"  Difference: {count_1 - count_3} ({'4,1 leads' if count_1 > count_3 else '4,3 leads'})", flush=True)
    print(f"  Number of sign flips: {len(flips)}", flush=True)
    if flips:
        print(f"  First flip: {flips[0][0]} at x = {flips[0][1]}", flush=True)
        if len(flips) > 1:
            print(f"  Second flip: {flips[1][0]} at x = {flips[1][1]}", flush=True)
    print(f"  (Known: first x where π(x;4,1) > π(x;4,3) is x = 26861, Leech 1957)", flush=True)


if __name__ == '__main__':
    main()
