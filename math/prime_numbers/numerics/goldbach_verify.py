"""
Goldbach verification: every even n > 2 is p + q for primes p, q.

For each even n ∈ [4, N], count the number of representations r(n):
  r(n) = |{(p, q) : p ≤ q, p+q = n, p and q both prime}|

Key questions:
1. r(n) ≥ 1 for all tested n? (If not, Goldbach fails)
2. What is min r(n) in the range? (Hardy-Littlewood predicts r(n) ~ n/(log n)²)
3. Which n have the SMALLEST r(n)? (Likely odd-powered-of-2 multiples, deep structure)
"""
import numpy as np
import time
from sieve_core import sieve, primes_up_to


def goldbach_rep_count(N):
    """For each even n ∈ [4, N], compute r(n) = # of Goldbach representations.
    Returns (r_array, min_r, min_n).

    Method: convolve the prime indicator with itself.
    r(n) = (1/2) × |{(p,q) : p+q = n, p,q prime}| (unordered pairs)
    """
    is_prime = sieve(N)
    is_prime_arr = np.frombuffer(is_prime, dtype=np.uint8).astype(np.int32)

    # Convolution: count of (p, q) with p + q = n
    # conv[i] = sum_{p+q=i} is_prime[p] × is_prime[q]
    # Using FFT via numpy.convolve
    print(f"  Convolving prime indicator (N={N})...", flush=True)
    t0 = time.time()
    # For large N, use scipy.signal.fftconvolve
    from scipy.signal import fftconvolve
    conv = fftconvolve(is_prime_arr, is_prime_arr, mode='full')
    # Round to nearest integer (FFT precision)
    conv_int = np.round(conv).astype(np.int64)
    print(f"  Convolution: {time.time()-t0:.1f}s", flush=True)

    # Unordered count: r(n) = (conv[n] + is_prime[n/2]) / 2
    # The +is_prime[n/2] handles p = q = n/2 case
    # Ordered pairs: conv[n] = (unordered × 2) - (1 if p=q=n/2 else 0)
    # So unordered = (conv[n] + is_prime[n/2]) // 2

    # Extract even n from 4 to N
    even_ns = np.arange(4, N + 1, 2)
    r_values = np.zeros(len(even_ns), dtype=np.int64)
    for idx, n in enumerate(even_ns):
        half = n // 2
        half_prime = 1 if (half < len(is_prime_arr) and is_prime_arr[half]) else 0
        r_values[idx] = (conv_int[n] + half_prime) // 2

    return even_ns, r_values


def main():
    print("GOLDBACH VERIFICATION", flush=True)
    print("=" * 60, flush=True)

    for N in [10**5, 10**6, 10**7]:
        print(f"\nN = {N}:", flush=True)
        t0 = time.time()
        even_ns, r = goldbach_rep_count(N)
        dt = time.time() - t0

        # Check Goldbach
        violations = np.sum(r == 0)
        # Ignore n=2 which has no rep (only even prime, 1 is not prime)
        # Our range starts at 4, which has rep 2+2

        min_r = r.min()
        min_idx = r.argmin()
        min_n = even_ns[min_idx]

        # Where does r(n) reach small values?
        small_indices = np.argsort(r)[:10]

        max_r = r.max()
        max_idx = r.argmax()
        max_n = even_ns[max_idx]

        print(f"  {len(even_ns)} even numbers checked", flush=True)
        print(f"  Goldbach violations: {violations}", flush=True)
        print(f"  min r(n) = {min_r} at n = {min_n}", flush=True)
        print(f"  max r(n) = {max_r} at n = {max_n}", flush=True)
        print(f"  Smallest 10 r(n) values:", flush=True)
        for i in small_indices:
            print(f"    r({even_ns[i]}) = {r[i]}", flush=True)
        print(f"  Time: {dt:.1f}s", flush=True)

        # Hardy-Littlewood prediction: r(n) ~ 2 C_2 n / (log n)²
        # where C_2 = twin prime constant ≈ 0.660161
        # For comparison, compute HL prediction for n = N
        C_2 = 0.6601618158
        hl_pred = 2 * C_2 * N / (np.log(N) ** 2)
        print(f"  Hardy-Littlewood r({N}) ≈ {hl_pred:.0f} (observed: {r[-1]})", flush=True)


if __name__ == '__main__':
    main()
