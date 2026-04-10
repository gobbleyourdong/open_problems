"""
Core sieve infrastructure for the prime_numbers campaign.

Provides:
  - sieve(N) — Sieve of Eratosthenes, returns boolean array up to N
  - primes_up_to(N) — list of primes ≤ N
  - pi(x, primes) — prime counting function (vectorized via bisect)
  - Li(x) — logarithmic integral, Gauss's approximation

Target: handle N up to ~10^9 on a single CPU with bytearray storage.
Dependencies: numpy only.
"""
import numpy as np
from math import log, isqrt
from bisect import bisect_right


def sieve(N):
    """Sieve of Eratosthenes up to N (inclusive).
    Returns a bytearray where arr[i] = 1 if i is prime, 0 otherwise."""
    if N < 2:
        return bytearray(N + 1)
    is_prime = bytearray([1]) * (N + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, isqrt(N) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return is_prime


def primes_up_to(N):
    """List of primes ≤ N via sieve."""
    s = sieve(N)
    return [i for i in range(N + 1) if s[i]]


def pi(x, primes_sorted):
    """π(x) via bisect on a sorted primes list."""
    return bisect_right(primes_sorted, x)


def Li(x):
    """Logarithmic integral Li(x) = ∫_2^x dt/log(t).
    Gauss's approximation to π(x).
    Uses trapezoidal rule with O(log x) subdivisions (exponential spacing)."""
    if x < 2:
        return 0.0
    # Simpson's rule on log-spaced intervals for accuracy
    n = 10000
    ts = np.linspace(2, x, n)
    vals = 1.0 / np.log(ts)
    return np.trapezoid(vals, ts)


if __name__ == '__main__':
    import time
    print("Sieve core — smoke test")
    print("=" * 50)
    for N in [10**4, 10**5, 10**6, 10**7]:
        t0 = time.time()
        ps = primes_up_to(N)
        dt = time.time() - t0
        print(f"  π({N}) = {len(ps)}, Li({N}) = {Li(N):.1f}, "
              f"deficit = {Li(N) - len(ps):+.1f}, {dt:.2f}s")
