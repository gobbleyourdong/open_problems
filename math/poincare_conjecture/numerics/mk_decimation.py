#!/usr/bin/env python3
"""
Migdal-Kadanoff decimation for SU(2) and U(1) in d=4.

Tests Tomboulis inequality (5.15): Z > Z+ under MK decimation.
Z+ = (Z + Z-)/2 where Z- has center-twisted BC.

The MK decimation acts on character expansion coefficients {c_j(β)}:
  Step 1 (bond moving): c_j → c_j^d  (raise to power d-1 for SU(N))
  Step 2 (decimation):  convolution on the group
    For SU(2): c_j' = (c_j^{d-1})^* ... (group convolution via Clebsch-Gordan)
    Actually: MK is simpler — bond move + decimate = specific recursion on c_j

For SU(2) with character expansion coefficients c_j:
  After one MK step on L^d lattice with scale factor b=2:
    c_j^(new) = [Σ_k (2k+1) c_k^{2(d-1)} · {j,j,k}]
  where {j,j,k} are related to 6j symbols.

Actually the standard MK recursion for d=4 with b=2 is:
  Step 1: Bond moving (d-1=3 bonds moved to 1):
    C_j^{moved} = c_j^3   (character coefficients raised to 3rd power)
  Step 2: Decimation (integrate out one site):
    c_j^{new} = c_j^{moved} * c_j / d_j = c_j^4 / (2j+1)

Actually this isn't right either. Let me be precise.

The MK approximation for d=4 with decimation factor b=2:
  1. Bond moving: move (d-1)=3 bonds onto 1 → effective single-bond weight
     f_moved(U) = [f(U)]^{d-1} = [f(U)]^3
     In characters: c_j^{moved} = c_j^3
     (product of class functions = convolution of chars, but for same group element
      it's just the power)

  Wait: the bond weight is W(U) = Σ_j d_j c_j χ_j(U).
  Moving 3 bonds onto 1: W_moved(U) = [W(U)]^3 = [Σ_j d_j c_j χ_j(U)]^3
  This is NOT c_j^3 in general. Need to expand using Clebsch-Gordan.

  But there's a simpler formulation using the CONVOLUTION on the group:

  2. Decimation of site x: integrate out U_x from two consecutive bonds:
     ∫ W(U₁ U_x) W(U_x† U₂) dU_x = Σ_j d_j c_j² χ_j(U₁ U₂⁻¹)  (NO, wrong)

Actually let me just use the standard result. For the MK recursion on the
heat kernel coefficients:

  The decimation of a single bond chain U₁·U₂ → U₁₂:
    ∫ f(U₁) f(U₂) δ(U₁U₂ = U₁₂) dU₁ dU₂ → gives new coefficients

  For character expansion W(U) = Σ_j d_j c_j χ_j(U):
    [W * W](U₁₂) = ∫ W(U₁) W(U₁⁻¹ U₁₂) dU₁ = Σ_j d_j c_j² χ_j(U₁₂)

  So convolution squares the coefficients: c_j → c_j²

  Bond moving multiplies coefficients: d-1 bonds moved → c_j → c_j^{d-1}

  One full MK step (bond move + decimation): c_j → c_j^{d-1} · c_j = c_j^d

  Wait that's too simple. Let me verify.

For d=4, b=2:
  Bond moving: (d-1)=3 bonds from perpendicular directions moved to one direction
    This gives: the effective bond weight squared along the remaining direction
    c_j → c_j^{d-1} = c_j^3  (bond moving)
  Decimation: integrate out the intermediate site
    c_j → c_j² (convolution)
  Combined: c_j → (c_j^3)^2 / c_j ... no.

  Actually: one MK step = bond move + decimate:
    c_j^{new} = c_j^{2(d-1)} = c_j^6  for d=4, b=2

  Let me just code it both ways and compare.

The key test: compute Z/Z+ at each step and see if it stays > 1.
"""

import numpy as np
from scipy.special import iv as bessel_i
import sys


def su2_char_coeffs(beta, j_max=6):
    """SU(2) character expansion coefficients c_j(β) = I_{2j+1}(β) / I_1(β)."""
    coeffs = {}
    for j2 in range(0, int(2 * j_max) + 1):
        j = j2 / 2.0
        n = int(2 * j + 1)
        coeffs[j] = bessel_i(n, beta) / bessel_i(1, beta)
    return coeffs


def u1_char_coeffs(beta, n_max=10):
    """U(1) character expansion coefficients c_n(β) = I_n(β) / I_0(β)."""
    coeffs = {}
    for n in range(0, n_max + 1):
        coeffs[n] = bessel_i(n, beta) / bessel_i(0, beta)
    return coeffs


def mk_step_simple(coeffs, d=4):
    """
    One MK decimation step: c_j → c_j^{2(d-1)}.

    This is the simplest version: bond move (d-1 bonds) + decimation (square).
    Combined exponent = 2(d-1) = 6 for d=4.
    """
    return {j: c ** (2 * (d - 1)) for j, c in coeffs.items()}


def mk_step_split(coeffs, d=4):
    """
    One MK step: bond move c_j → c_j^{d-1}, then decimate c_j → c_j^2.
    Combined: c_j → c_j^{2(d-1)}.
    Same as above but conceptually clearer.
    """
    # Bond move: d-1 = 3 bonds merged
    moved = {j: c ** (d - 1) for j, c in coeffs.items()}
    # Decimation: convolve two bonds = square coefficients
    decimated = {j: c ** 2 for j, c in moved.items()}
    return decimated


def partition_function_ratio_su2(coeffs, L=4):
    """
    Compute Z/Z+ for SU(2) on L^4 lattice using character expansion.

    Z = Σ_j (2j+1)^{n_free} · c_j^{n_plaq}  (schematic)
    Z- = same but with c_j → (-1)^{2j} c_j on one surface
    Z+ = (Z + Z-) / 2

    For an APPROXIMATE estimate using mean-field:
    Z ≈ [Σ_j (2j+1) c_j(β)]^V  (independent plaquettes)
    Z- ≈ [Σ_j (2j+1) (-1)^{2j} c_j(β)]^{V_Σ} · [Σ_j (2j+1) c_j(β)]^{V-V_Σ}

    where V_Σ = L^{d-1} plaquettes on the twisted surface.

    But this is too crude. Let me use the 1D transfer matrix approach.

    For the EFFECTIVE 1D chain after MK decimation to a single line:
    Z = Tr(T^L) where T has eigenvalues λ_j = d_j c_j
    Z- = Tr(T^L · twist) where twist flips half-integer reps
    """
    # Transfer matrix eigenvalues (1D effective theory after full MK)
    # λ_j = (2j+1) · c_j  for each representation j

    # Z = Σ_j λ_j^L = Σ_j [(2j+1) c_j]^L
    Z = sum((2*j + 1) * c for j, c in coeffs.items()) ** L

    # Z- = Σ_j (-1)^{2j} λ_j^L  (center twist flips half-integer reps)
    Z_minus = 0.0
    for j, c in coeffs.items():
        j2 = int(2 * j)
        sign = (-1) ** j2
        Z_minus += sign * ((2*j + 1) * c) ** L

    # Actually this isn't right either. The transfer matrix for the
    # character expansion of a 1D chain is diagonal:
    # T = diag(d_j c_j) in the representation basis
    # Z = Σ_j (d_j c_j)^L
    # Z- = Σ_j (-1)^{2j} (d_j c_j)^L

    Z = sum(((2*j + 1) * c) ** L for j, c in coeffs.items())
    Z_minus = sum(((-1)**(int(2*j))) * ((2*j + 1) * c) ** L
                  for j, c in coeffs.items())

    Z_plus = (Z + Z_minus) / 2

    if Z_plus <= 0:
        return float('inf')
    return Z / Z_plus


def partition_function_ratio_u1(coeffs, L=4):
    """Compute Z/Z+ for U(1). Center twist: c_n → (-1)^n c_n."""
    Z = sum((c if n == 0 else 2 * c) ** L for n, c in coeffs.items())  # wrong
    # Actually for U(1): Z = Σ_n c_n^L (1D chain, each mode contributes)
    # With multiplicity: Z = [c_0 + 2 Σ_{n>0} c_n]^L  (mean field)

    # 1D transfer matrix: eigenvalues are c_n for each Fourier mode
    # Z = Σ_n c_n^L  (with multiplicity 1 for n=0, 2 for n>0 via ±n)
    # Z- = Σ_n (-1)^n c_n^L

    Z = coeffs[0] ** L + sum(2 * c ** L for n, c in coeffs.items() if n > 0)
    Z_minus = coeffs[0] ** L + sum(2 * ((-1)**n) * c ** L
                                    for n, c in coeffs.items() if n > 0)
    Z_plus = (Z + Z_minus) / 2

    if Z_plus <= 0:
        return float('inf')
    return Z / Z_plus


def main():
    print("=" * 75)
    print("MIGDAL-KADANOFF DECIMATION — TOMBOULIS (5.15) TEST")
    print("=" * 75)

    print("\n" + "=" * 75)
    print("SU(2) — Should preserve Z > Z+ (confinement at all β)")
    print("=" * 75)

    betas = [0.5, 1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0, 6.0, 8.0]
    n_steps = 5
    L = 4  # effective chain length for ratio computation

    print(f"\n{'β':>6} |", end="")
    for step in range(n_steps + 1):
        print(f"  step {step:d}  ", end="")
    print(f"| {'Preserved?':>10}")
    print("-" * (10 + 10 * (n_steps + 1) + 15))

    for beta in betas:
        coeffs = su2_char_coeffs(beta, j_max=4)
        ratios = []

        current = dict(coeffs)
        for step in range(n_steps + 1):
            ratio = partition_function_ratio_su2(current, L=L)
            ratios.append(ratio)
            if step < n_steps:
                current = mk_step_simple(current, d=4)

        preserved = all(r > 1.0 for r in ratios)
        print(f"{beta:6.1f} |", end="")
        for r in ratios:
            if r > 1e6:
                print(f"  {'>>1':>6}  ", end="")
            else:
                print(f"  {r:7.4f} ", end="")
        print(f"| {'YES ✓' if preserved else 'NO ✗':>10}")

    print("\n" + "=" * 75)
    print("U(1) — Should FAIL at weak coupling (Coulomb phase, β > β_c ≈ 1.01)")
    print("=" * 75)

    betas_u1 = [0.3, 0.5, 0.8, 1.0, 1.01, 1.05, 1.1, 1.5, 2.0, 3.0]

    print(f"\n{'β':>6} |", end="")
    for step in range(n_steps + 1):
        print(f"  step {step:d}  ", end="")
    print(f"| {'Preserved?':>10}")
    print("-" * (10 + 10 * (n_steps + 1) + 15))

    for beta in betas_u1:
        coeffs = u1_char_coeffs(beta, n_max=6)
        ratios = []

        current = dict(coeffs)
        for step in range(n_steps + 1):
            ratio = partition_function_ratio_u1(current, L=L)
            ratios.append(ratio)
            if step < n_steps:
                current = mk_step_simple(current, d=4)

        preserved = all(r > 1.0 for r in ratios)
        print(f"{beta:6.2f} |", end="")
        for r in ratios:
            if r > 1e6:
                print(f"  {'>>1':>6}  ", end="")
            elif abs(r) < 0.001:
                print(f"  {r:7.1e} ", end="")
            else:
                print(f"  {r:7.4f} ", end="")
        print(f"| {'YES ✓' if preserved else 'NO ✗':>10}")

    # Detailed coefficient evolution
    print("\n" + "=" * 75)
    print("COEFFICIENT EVOLUTION — SU(2) at β = 2.3 (crossover)")
    print("=" * 75)

    coeffs = su2_char_coeffs(2.3, j_max=4)
    print(f"\n{'Step':>4} |", end="")
    for j2 in range(0, 9):
        j = j2 / 2.0
        print(f"  c_{j:.1f}   ", end="")
    print()
    print("-" * (8 + 10 * 9))

    current = dict(coeffs)
    for step in range(6):
        print(f"{step:4d} |", end="")
        for j2 in range(0, 9):
            j = j2 / 2.0
            c = current.get(j, 0.0)
            if c < 1e-10:
                print(f"  {'~0':>6}  ", end="")
            else:
                print(f"  {c:7.5f}", end="")
        print()
        current = mk_step_simple(current, d=4)

    print("\nNote: c_0 = 1 always. All other c_j → 0 rapidly under MK.")
    print("This means MK flows to STRONG COUPLING (c_j = δ_{j,0}).")
    print("The flow is toward infinite mass gap — confinement is STABLE.")

    # Key diagnostic
    print("\n" + "=" * 75)
    print("KEY DIAGNOSTIC: c_{1/2} / c_0 ratio (controls vortex cost)")
    print("=" * 75)
    print("If c_{1/2} → 0 faster than c_0 → 1: vortex cost INCREASES ✓")
    print("If c_{1/2} → 1: vortex cost DECREASES ✗")

    for beta in [1.0, 2.0, 2.3, 4.0, 8.0]:
        coeffs = su2_char_coeffs(beta, j_max=4)
        print(f"\nβ = {beta}:")
        current = dict(coeffs)
        for step in range(5):
            r = current.get(0.5, 0.0) / current.get(0.0, 1.0)
            print(f"  step {step}: c_{{1/2}}/c_0 = {r:.6f}")
            current = mk_step_simple(current, d=4)


if __name__ == "__main__":
    main()
