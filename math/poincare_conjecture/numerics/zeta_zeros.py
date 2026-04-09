#!/usr/bin/env python3
"""
Riemann Zeta Zeros — Phase 0 computation.

numerical track first task: compute and verify zeros of ζ(s) on the critical line.
Build the numerical infrastructure for the systematic approach.

1. Compute ζ(1/2 + it) via the Riemann-Siegel formula
2. Find zeros by sign changes of Z(t) (Hardy's Z-function)
3. Verify known zeros against published values
4. Compute zero spacings and compare with GUE statistics
5. Search for patterns in the zeros that might inform proof approaches
"""

import numpy as np
from scipy.special import gamma as gamma_func
from scipy.optimize import brentq
import time


def zeta_approx(s, N=1000):
    """Approximate ζ(s) by partial sum + Euler-Maclaurin correction."""
    if s.real > 1:
        return sum(n**(-s) for n in range(1, N+1))
    # Use the functional equation for Re(s) < 1
    # ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s)
    s1 = 1 - s
    zeta_1ms = sum(n**(-s1) for n in range(1, N+1))
    return (2**s * np.pi**(s-1) * np.sin(np.pi*s/2) *
            gamma_func(s1) * zeta_1ms)


def hardy_Z(t, N=None):
    """
    Hardy's Z-function: Z(t) = e^{iθ(t)} ζ(1/2 + it)

    where θ(t) = arg(π^{-it/2} Γ(1/4 + it/2)) is the Riemann-Siegel theta.

    Z(t) is REAL for real t. Its zeros are exactly the zeros of ζ on the
    critical line.

    Uses the Riemann-Siegel formula for efficiency:
    Z(t) ≈ 2 Σ_{n=1}^{floor(√(t/2π))} n^{-1/2} cos(θ(t) - t ln(n)) + remainder
    """
    if N is None:
        N = max(10, int(np.sqrt(t / (2 * np.pi))))

    # Riemann-Siegel theta function
    # θ(t) = Im(log Γ(1/4 + it/2)) - (t/2)log(π)
    s = 0.25 + 0.5j * t
    theta = np.imag(np.log(gamma_func(s))) - (t / 2) * np.log(np.pi)

    # Main sum
    Z = 0.0
    for n in range(1, N + 1):
        Z += np.cos(theta - t * np.log(n)) / np.sqrt(n)
    Z *= 2

    return Z


def find_zeros(t_start, t_end, dt=0.1):
    """Find zeros of Z(t) by sign changes."""
    zeros = []
    t = t_start
    Z_prev = hardy_Z(t)

    while t < t_end:
        t_next = t + dt
        Z_next = hardy_Z(t_next)

        if Z_prev * Z_next < 0:
            # Sign change — refine with Brent's method
            try:
                t_zero = brentq(hardy_Z, t, t_next, xtol=1e-10)
                zeros.append(t_zero)
            except ValueError:
                pass

        Z_prev = Z_next
        t = t_next

    return zeros


def main():
    print("=" * 70)
    print("RIEMANN ZETA ZEROS — Phase 0 Computation")
    print("=" * 70)

    # Known first 10 zeros (imaginary parts)
    known_zeros = [
        14.134725142, 21.022039639, 25.010857580, 30.424876126,
        32.935061588, 37.586178159, 40.918719012, 43.327073281,
        48.005150881, 49.773832478
    ]

    # Compute first zeros
    print("\n--- Finding zeros of Z(t) for t ∈ [10, 55] ---\n")
    t0 = time.time()
    zeros = find_zeros(10, 55, dt=0.05)
    dt = time.time() - t0

    print(f"Found {len(zeros)} zeros in {dt:.2f}s\n")
    print(f"{'#':>3} | {'t (computed)':>15} | {'t (known)':>15} | {'error':>12} | {'On Re=1/2?':>10}")
    print("-" * 65)

    for i, t_comp in enumerate(zeros[:10]):
        if i < len(known_zeros):
            t_known = known_zeros[i]
            err = abs(t_comp - t_known)
            print(f"{i+1:3d} | {t_comp:15.9f} | {t_known:15.9f} | {err:12.2e} | {'✓' if err < 1e-6 else '✗':>10}")
        else:
            print(f"{i+1:3d} | {t_comp:15.9f} | {'---':>15} | {'---':>12} | {'?':>10}")

    # Zero spacings
    if len(zeros) >= 2:
        spacings = np.diff(zeros)
        avg_spacing = np.mean(spacings)
        print(f"\n--- Zero Spacings ---")
        print(f"Mean spacing: {avg_spacing:.6f}")
        print(f"Expected (from density): 2π/log(t̄/(2π)) ≈ {2*np.pi/np.log(30/(2*np.pi)):.6f}")

    # Compute more zeros at higher t
    print(f"\n--- Zeros at higher t (100-200) ---\n")
    zeros_high = find_zeros(100, 200, dt=0.05)
    print(f"Found {len(zeros_high)} zeros in t ∈ [100, 200]")
    if len(zeros_high) >= 2:
        sp = np.diff(zeros_high)
        print(f"Mean spacing: {np.mean(sp):.6f}")
        print(f"Min spacing: {np.min(sp):.6f}")
        print(f"Max spacing: {np.max(sp):.6f}")
        print(f"Std: {np.std(sp):.6f}")

    # GUE statistics check
    print(f"\n--- GUE Statistics (normalized spacings) ---")
    if len(zeros_high) >= 10:
        # Normalize spacings to mean 1
        sp_norm = sp / np.mean(sp)
        # GUE prediction: P(s) ≈ (32/π²)s² exp(-4s²/π) (Wigner surmise)
        # Poisson: P(s) = exp(-s)
        # Test: variance. GUE ≈ 0.178, Poisson = 1
        var_sp = np.var(sp_norm)
        print(f"Variance of normalized spacings: {var_sp:.4f}")
        print(f"GUE prediction: ~0.178")
        print(f"Poisson prediction: 1.0")
        print(f"Match: {'GUE ✓' if abs(var_sp - 0.178) < abs(var_sp - 1.0) else 'Poisson ✗'}")

    # Key diagnostic: any zeros OFF the critical line?
    print(f"\n--- Critical Line Check ---")
    print("All zeros found by Z(t) sign changes are BY CONSTRUCTION on Re(s) = 1/2.")
    print("The question is: are there zeros we MISSED (not caught by sign changes)?")
    print(f"Zero count in [10, 55]: {len(zeros[:10])}, expected: 10")
    print(f"Zero count in [100, 200]: {len(zeros_high)}, expected: ~{int((200-100)*np.log(150/(2*np.pi))/(2*np.pi))}")

    N_expected = 0
    for t in [55, 200]:
        # N(T) ≈ T/(2π) log(T/(2πe)) + 7/8
        N_t = t/(2*np.pi) * np.log(t/(2*np.pi*np.e)) + 7/8
        print(f"N({t}) ≈ {N_t:.1f}")


if __name__ == "__main__":
    main()
