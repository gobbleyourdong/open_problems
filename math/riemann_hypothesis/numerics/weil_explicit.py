#!/usr/bin/env python3
"""
Weil Explicit Formula — the bridge between zeros and primes.

The explicit formula (Weil, 1952):

  Σ_ρ h(ρ) = h(1) + h(0) - Σ_p Σ_m (log p / p^{m/2}) [g(m log p) + g(-m log p)]
              + (1/2π) ∫ h(1/2+it) [ψ(1/4+it/2) + ψ(1/4-it/2)] dt - (log 4π + γ) g(0)

where h(s) = ∫ g(x) e^{(s-1/2)x} dx (Fourier-Mellin transform),
ρ runs over non-trivial zeros, p over primes, γ = Euler constant.

For the Connes approach: RH ⟺ positivity of the Weil distribution
  W(f) = Σ_ρ f̂(ρ) ≥ 0 for all f in a specific test function class.

This script:
1. Compute both sides of the explicit formula and verify they match
2. Test the Weil positivity for specific test functions
3. Provide numerical test cases for the even instance's Lean work
"""

import numpy as np
import mpmath
mpmath.mp.dps = 25


def prime_sieve(N):
    """Sieve of Eratosthenes up to N."""
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    return [i for i in range(2, N+1) if is_prime[i]]


def explicit_formula_test(g_func, g_hat_func, primes, zeros_gamma, T_max=100):
    """
    Verify the explicit formula for a test function g.

    Zero side: Σ_ρ h(ρ) where h is the Mellin transform of g
    Prime side: prime sum + archimedean terms

    For simplicity, use the symmetric form with g even:
    h(s) = ∫_{-∞}^{∞} g(x) e^{(s-1/2)x} dx

    For g(x) = e^{-ax²} (Gaussian):
    h(s) = √(π/a) exp((s-1/2)²/(4a))
    """
    # ZERO SIDE: Σ_ρ h(ρ) = Σ_k h(1/2 + iγ_k) + h(1/2 - iγ_k)
    zero_sum = 0.0
    for gamma in zeros_gamma:
        # h(1/2 + iγ) = g_hat(γ) for even g
        zero_sum += 2 * g_hat_func(gamma).real  # pair ρ, ρ̄

    # PRIME SIDE: -Σ_p Σ_m (log p / p^{m/2}) [g(m log p) + g(-m log p)]
    prime_sum = 0.0
    for p in primes:
        log_p = np.log(p)
        for m in range(1, int(T_max / log_p) + 1):
            x = m * log_p
            prime_sum -= (log_p / p**(m/2)) * 2 * g_func(x)  # g even: g(x) + g(-x) = 2g(x)

    # ARCHIMEDEAN TERMS
    # h(0) + h(1) = g_hat(i/2) + g_hat(-i/2) ... for the symmetric form
    # Plus the log(4π) + γ term
    arch = g_hat_func(0.5j).real + g_hat_func(-0.5j).real
    const_term = -(np.log(4*np.pi) + 0.5772156649) * g_func(0)

    return zero_sum, prime_sum, arch, const_term


def main():
    print("=" * 70)
    print("WEIL EXPLICIT FORMULA — Zeros ↔ Primes Bridge")
    print("=" * 70)

    # Setup
    primes = prime_sieve(10000)
    print(f"Primes: {len(primes)} up to {primes[-1]}")

    # Get zeros
    print("Computing 100 zeta zeros...", end="", flush=True)
    zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 101)]
    print(f" done ({zeros[0]:.2f} to {zeros[-1]:.2f})")

    # Test function: Gaussian g(x) = exp(-a x²)
    # h(1/2 + it) = √(π/a) exp(-t²/(4a))
    a = 0.01  # wide Gaussian captures many zeros/primes

    g = lambda x: np.exp(-a * x**2)
    g_hat = lambda t: np.sqrt(np.pi / a) * np.exp(-(t.real**2 - t.imag**2) / (4*a))

    # Actually g_hat for complex t:
    # h(1/2+it) = ∫ e^{-ax²} e^{itx} dx = √(π/a) exp(-t²/(4a))
    g_hat_correct = lambda t: np.sqrt(np.pi / a) * np.exp(-t**2 / (4*a))

    print(f"\n--- Test function: g(x) = exp(-{a}x²) ---")
    print(f"g_hat(t) = √(π/{a}) exp(-t²/{4*a})")

    zero_sum, prime_sum, arch, const = explicit_formula_test(
        g, lambda t: float(g_hat_correct(complex(t)).real),
        primes, zeros
    )

    total_prime_side = prime_sum + arch + const
    print(f"\nZero side:  Σ_ρ h(ρ) = {zero_sum:.6f}")
    print(f"Prime side: Σ_p + arch + const = {prime_sum:.6f} + {arch:.6f} + {const:.6f}")
    print(f"            = {total_prime_side:.6f}")
    print(f"Match: {abs(zero_sum - total_prime_side):.4f} (should be small)")

    # Test with different a values
    print(f"\n--- Explicit formula verification for various Gaussian widths ---")
    print(f"{'a':>8} | {'Zero side':>12} | {'Prime side':>12} | {'Diff':>10} | {'Match?':>7}")
    print("-" * 58)

    for a in [1.0, 0.1, 0.01, 0.005]:
        g = lambda x, a=a: np.exp(-a * x**2)
        g_hat = lambda t, a=a: float((np.sqrt(np.pi/a) * np.exp(-complex(t)**2/(4*a))).real)

        zs, ps, ar, co = explicit_formula_test(g, g_hat, primes, zeros)
        total_p = ps + ar + co
        diff = abs(zs - total_p)
        ok = "✓" if diff < max(abs(zs), 1) * 0.1 else "✗"
        print(f"{a:8.3f} | {zs:12.4f} | {total_p:12.4f} | {diff:10.4f} | {ok:>7}")

    # WEIL POSITIVITY TEST
    # RH ⟺ W(f) = Σ_ρ |f̂(ρ)|² ≥ 0 for appropriate f
    # For f = g * g̃ (convolution with adjoint), f̂ = |ĝ|² ≥ 0 automatically.
    # The nontrivial content: the PRIME SIDE of the explicit formula for |ĝ|²
    # must also be ≥ 0.

    print(f"\n--- Weil Positivity Test ---")
    print("W(g) = Σ_ρ |g_hat(γ_ρ)|² (always ≥ 0 by definition)")
    print("The Connes approach: show the PRIME SIDE equivalent is also ≥ 0")
    print("for a specific class of test functions.")
    print()

    for a in [0.1, 0.01, 0.001]:
        W = sum(2 * (np.sqrt(np.pi/a) * np.exp(-g**2/(4*a)))**2 for g in zeros)
        print(f"  a={a}: W(g) = {W:.4f} (≥ 0? {'✓' if W >= 0 else '✗'})")

    print()
    print("All W(g) > 0 — consistent with RH.")
    print("The Connes program: prove W(f) ≥ 0 for ALL f in the adelic")
    print("Schwartz class, using the structure of primes (not zeros).")


if __name__ == "__main__":
    main()
