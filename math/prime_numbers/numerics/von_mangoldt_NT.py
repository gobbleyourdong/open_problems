"""
Riemann-von Mangoldt formula for N(T): the count of nontrivial zeros
ρ = β + iγ of ζ(s) with 0 < γ ≤ T.

The exact formula is:
    N(T) = θ(T)/π + 1 + S(T)
where θ(T) is the Riemann-Siegel theta function:
    θ(T) = arg Γ(1/4 + iT/2) - (T/2) log π
and S(T) = (1/π) arg ζ(1/2 + iT) is the small remainder term.

Asymptotic form (Riemann-von Mangoldt 1859/1905):
    N(T) = (T/(2π)) log(T/(2π)) - T/(2π) + 7/8 + S(T) + O(1/T)
         = (T/(2π)) log(T/(2πe)) + 7/8 + S(T) + O(1/T)

Properties of S(T):
- S(T) = O(log T) under RH (Backlund 1918, Selberg 1944)
- S(T) is "usually small": ⟨|S(T)|²⟩ = (1/(2π²)) log log T + O(1)
- The OSCILLATION of S(T) around zero is the analytic content of RH
- Each zero contributes a sudden jump of +1 in S(T) at T = γ_n

This script verifies the formula by directly counting cached/computed
zeros against the smooth approximation.
"""
import mpmath
import json
import os
from math import log, pi


def load_or_compute_zeros(n_zeros=1000, cache_path='/tmp/rh_zeros_NT.json'):
    """Load cached zeros or compute fresh ones via mpmath.zetazero."""
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            data = json.load(f)
        if len(data) >= n_zeros:
            return [float(g) for g in data[:n_zeros]]
    print(f"Computing first {n_zeros} Riemann zeros (this takes ~30s)...")
    mpmath.mp.dps = 25
    gammas = []
    for k in range(1, n_zeros + 1):
        g = float(mpmath.zetazero(k).imag)
        gammas.append(g)
        if k % 100 == 0:
            print(f"  computed {k}/{n_zeros}, γ_{k} = {g:.4f}")
    with open(cache_path, 'w') as f:
        json.dump(gammas, f)
    print(f"  cached at {cache_path}")
    return gammas


def N_smooth(T):
    """Smooth (non-S(T)) part of Riemann-von Mangoldt: (T/2π) log(T/2πe) + 7/8."""
    return (T / (2 * pi)) * log(T / (2 * pi)) - T / (2 * pi) + 7 / 8


def N_smooth_exact(T):
    """Exact smooth formula: θ(T)/π + 1 where θ is Riemann-Siegel theta.

    mpmath.siegeltheta gives the analytically-continued (unwrapped) theta,
    NOT the principal argument — that's essential for the formula to work."""
    return float(mpmath.siegeltheta(T)) / pi + 1


def N_actual(T, gammas):
    """Count gammas ≤ T."""
    # Binary search would be faster but gammas is short
    return sum(1 for g in gammas if g <= T)


def main():
    print("Riemann-von Mangoldt formula for N(T)")
    print("=" * 76)

    n_zeros = 500
    gammas = load_or_compute_zeros(n_zeros=n_zeros)
    print(f"Loaded {len(gammas)} zeros, γ_1 = {gammas[0]:.6f}, "
          f"γ_{n_zeros} = {gammas[-1]:.6f}")
    print()

    # Verify N(T) at various heights
    print("N(T) verification:")
    print(f"{'T':>10} {'N(T)':>8} {'smooth':>12} {'exact-θ':>12} "
          f"{'S(T)':>10} {'|S|/log T':>10}")
    print("-" * 72)
    test_Ts = [10, 25, 50, 100, 150, 200, 300, 500, 700, 1000]
    for T in test_Ts:
        if T > gammas[-1]:
            break
        N = N_actual(T, gammas)
        smooth = N_smooth(T)
        exact_smooth = N_smooth_exact(T)
        S = N - exact_smooth
        s_norm = abs(S) / log(T) if T > 1 else 0
        print(f"{T:>10.2f} {N:>8} {smooth:>12.4f} {exact_smooth:>12.4f} "
              f"{S:>+10.4f} {s_norm:>10.4f}")
    print()

    # Test at exact zero heights (just before the zero, S(T) should be near 0)
    print("S(T) just BEFORE each γ_n (T = γ_n - ε):")
    print(f"{'n':>4} {'γ_n':>12} {'N(T-ε)':>8} {'smooth':>12} {'S(T-ε)':>12}")
    print("-" * 56)
    for n in [10, 50, 100, 200, 300, 400, 500]:
        if n > len(gammas):
            break
        T = gammas[n - 1] - 1e-6
        N = N_actual(T, gammas)
        sm = N_smooth_exact(T)
        S = N - sm
        print(f"{n:>4} {gammas[n-1]:>12.6f} {N:>8} {sm:>12.4f} {S:>+12.4f}")
    print()

    # The smooth formula should predict ~the n at T = γ_n - ε
    print("S(T) just AFTER each γ_n (T = γ_n + ε): jumps by +1")
    print(f"{'n':>4} {'γ_n':>12} {'N(T+ε)':>8} {'smooth':>12} {'S(T+ε)':>12}")
    print("-" * 56)
    for n in [10, 50, 100, 200, 300, 400, 500]:
        if n > len(gammas):
            break
        T = gammas[n - 1] + 1e-6
        N = N_actual(T, gammas)
        sm = N_smooth_exact(T)
        S = N - sm
        print(f"{n:>4} {gammas[n-1]:>12.6f} {N:>8} {sm:>12.4f} {S:>+12.4f}")
    print()

    # Average |S(T)| over a grid: should grow like √(log log T)
    print("⟨S(T)²⟩ growth (Selberg's central limit):")
    print(f"{'T_max':>10} {'mean S':>12} {'std S':>12} "
          f"{'predict √(log log T_max / 2π²)':>30}")
    print("-" * 76)
    import numpy as np
    np.random.seed(42)
    for T_max in [50, 100, 200, 500, 1000]:
        if T_max > gammas[-1]:
            break
        # Sample 200 random T in [10, T_max]
        T_samples = np.random.uniform(10, T_max, 200)
        S_vals = []
        for T in T_samples:
            N = N_actual(T, gammas)
            sm = N_smooth_exact(T)
            S_vals.append(N - sm)
        S_arr = np.array(S_vals)
        mean_s = float(S_arr.mean())
        std_s = float(S_arr.std())
        predict = (log(max(log(T_max), 2)) / (2 * pi ** 2)) ** 0.5
        print(f"{T_max:>10} {mean_s:>+12.4f} {std_s:>12.4f} {predict:>30.4f}")
    print()
    print("Selberg (1944): S(T) is approximately Gaussian with")
    print("    Var S(T) ~ (1/(2π²)) log log T")
    print("So std(S) should grow VERY slowly with T (log log scale).")


if __name__ == '__main__':
    main()
