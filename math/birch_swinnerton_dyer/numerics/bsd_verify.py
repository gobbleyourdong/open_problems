#!/usr/bin/env python3
"""
BSD Verification: compute L(E,1) and rank for specific elliptic curves.

For each curve E/Q:
- Compute a_p = p + 1 - #E(F_p) for small primes p
- Compute the partial L-series L(E,s) = Π_p (1 - a_p p^{-s} + p^{1-2s})^{-1}
- Evaluate at s=1: if L(E,1) ≠ 0 → rank 0 (BSD says)
- If L(E,1) = 0: compute L'(E,1) → rank 1 (BSD says)
- For rank ≥ 2: L(E,1) = L'(E,1) = 0 → BSD predicts ord_{s=1} L = rank

Minimal deps: numpy only. No sage, no pari.
"""

import numpy as np
from math import gcd


def curve_points_mod_p(a, b, p):
    """Count points on y² = x³ + ax + b over F_p."""
    count = 1  # point at infinity
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        # Is rhs a quadratic residue mod p?
        if rhs == 0:
            count += 1
        else:
            # Euler criterion: rhs^{(p-1)/2} ≡ 1 mod p iff QR
            if pow(rhs, (p-1)//2, p) == 1:
                count += 2  # two square roots
    return count


def a_p(a_coeff, b_coeff, p):
    """a_p = p + 1 - #E(F_p)."""
    if (4*a_coeff**3 + 27*b_coeff**2) % p == 0:
        return 0  # bad reduction, skip
    return p + 1 - curve_points_mod_p(a_coeff, b_coeff, p)


def primes_up_to(N):
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            for j in range(i*i, N+1, i): sieve[j] = False
    return [i for i in range(2, N+1) if sieve[i]]


def L_value(a_coeff, b_coeff, s, N_primes=500):
    """Partial Euler product for L(E, s)."""
    primes = primes_up_to(N_primes * 10)[:N_primes]
    disc = 4*a_coeff**3 + 27*b_coeff**2

    L = 1.0
    for p in primes:
        ap = a_p(a_coeff, b_coeff, p)
        if disc % p == 0:
            # Bad prime: L_p = (1 - a_p p^{-s})^{-1}
            L *= 1.0 / (1 - ap * p**(-s))
        else:
            # Good prime: L_p = (1 - a_p p^{-s} + p^{1-2s})^{-1}
            L *= 1.0 / (1 - ap * p**(-s) + p**(1-2*s))
    return L


def numerical_rank_estimate(a_coeff, b_coeff, N_primes=200):
    """Estimate the analytic rank from L-series behavior near s=1."""
    L1 = L_value(a_coeff, b_coeff, 1.0, N_primes)
    L1_eps = L_value(a_coeff, b_coeff, 1.01, N_primes)
    L1_2eps = L_value(a_coeff, b_coeff, 1.02, N_primes)

    # Numerical derivative
    Lprime = (L1_eps - L1) / 0.01
    Ldoubleprime = (L1_2eps - 2*L1_eps + L1) / 0.01**2

    if abs(L1) > 0.1:
        return 0, L1, Lprime
    elif abs(Lprime) > 0.1:
        return 1, L1, Lprime
    else:
        return 2, L1, Lprime  # or higher


# Famous elliptic curves
CURVES = {
    # (a, b) for y² = x³ + ax + b, expected rank
    'y²=x³-x (rank 0)': (-1, 0, 0),
    'y²=x³-x+1 (rank 1?)': (-1, 1, 1),
    'y²=x³+1 (rank 0)': (0, 1, 0),
    'y²=x³-4x (rank 0)': (-4, 0, 0),
    'y²=x³+x (rank 0)': (1, 0, 0),
    'y²=x³-x+2 (rank ?)': (-1, 2, None),
    'y²=x³+17 (rank 2?)': (0, 17, 2),
    'y²=x³-2 (rank 1)': (0, -2, 1),
    'y²=x³-7 (rank 1)': (0, -7, 1),
}


def main():
    print("=" * 70)
    print("BSD VERIFICATION — L-values and Rank Estimates")
    print("=" * 70)
    print("BSD: rank(E(Q)) = ord_{s=1} L(E,s)")
    print()

    print(f"{'Curve':>25} | {'L(E,1)':>10} | {'Lprime':>10} | {'est rank':>8} | {'exp rank':>8} | {'BSD?':>5}")
    print("-" * 80)

    for name, params in CURVES.items():
        a, b, expected_rank = params
        # Check discriminant
        disc = 4*a**3 + 27*b**2
        if disc == 0:
            print(f"{name:>25} | {'singular':>10} | {'---':>10} | {'---':>8} | {str(expected_rank):>8} | {'---':>5}")
            continue

        est_rank, L1, Lp = numerical_rank_estimate(a, b, N_primes=100)
        match = "✓" if expected_rank is not None and est_rank == expected_rank else "?" if expected_rank is None else "✗"
        print(f"{name:>25} | {L1:10.4f} | {Lp:10.4f} | {est_rank:>8} | {str(expected_rank):>8} | {match:>5}")

    print()
    print("NOTE: Partial L-series (100 primes) is a ROUGH approximation.")
    print("For rigorous BSD verification, need thousands of primes + functional equation.")
    print()
    print("IRON FORTRESS TARGET: verify BSD for all curves of conductor ≤ 1000.")
    print("This requires: (1) enumerate curves, (2) compute ranks exactly,")
    print("(3) compute L-values with enough precision to determine ord_{s=1}.")
    print("Cremona's tables cover conductor ≤ 500000 — we're building the tools.")


if __name__ == "__main__":
    main()
