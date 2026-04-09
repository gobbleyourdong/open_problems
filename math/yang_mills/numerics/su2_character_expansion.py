"""
SU(2) Character Expansion — Exact Mass Gap on Small Lattices

The partition function for SU(2) lattice gauge theory can be EXACTLY
expanded using representation theory:

  exp(β/2 · Tr(U)) = Σ_j (2j+1) · a_j(β) · χ_j(U)

where j = 0, 1/2, 1, 3/2, ... and a_j(β) = I_{2j+1}(β) / I_1(β).

On small lattices (2^d, 3^d), the full transfer matrix can be constructed
in the representation basis and diagonalized exactly.

This script computes:
1. The Bessel function coefficients a_j(β)
2. The mass gap Δ(β) = -ln(λ₁/λ₀) for 1D (trivial) and 2D lattices
3. Scaling of Δ(β) across the full coupling range

Author: Even Instance (for Odd Instance to extend)
Date: 2026-04-07
"""

import numpy as np
from scipy.special import iv as bessel_i  # Modified Bessel function I_n(x)
import sys


def character_coefficients(beta: float, j_max: int = 20) -> np.ndarray:
    """Compute a_j(β) = I_{2j+1}(β) / I_1(β) for j = 0, 1/2, 1, ..., j_max/2.

    These are the expansion coefficients of exp(β/2 · Tr(U)) in SU(2) characters.

    For SU(2), j labels spin-j representation, dim = 2j+1.
    We use half-integer indexing: j_idx = 0 means j=0, j_idx=1 means j=1/2, etc.
    """
    I1 = bessel_i(1, beta)
    if I1 == 0:
        return np.zeros(j_max + 1)

    coeffs = np.zeros(j_max + 1)
    for j_idx in range(j_max + 1):
        j = j_idx / 2  # actual spin
        n = int(2 * j + 1)  # Bessel order = dimension of irrep
        coeffs[j_idx] = bessel_i(n, beta) / I1
    return coeffs


def mass_gap_1d(beta: float, j_max: int = 20) -> float:
    """Mass gap for 1D SU(2) gauge theory (trivial but instructive).

    In 1D, there are no plaquettes. The transfer matrix is just
    the Haar-measure-weighted identity. The 'mass gap' comes from
    the ratio of character coefficients:

    Δ = -ln(a_{1/2}(β) / a_0(β))

    This is the gap between the trivial and fundamental representations.
    """
    coeffs = character_coefficients(beta, j_max)
    if coeffs[0] <= 0 or coeffs[1] <= 0:
        return float('inf')
    return -np.log(coeffs[1] / coeffs[0])


def mass_gap_strong_coupling(beta: float) -> float:
    """Analytic strong-coupling prediction for mass gap.

    At small β: a_{1/2}(β)/a_0(β) ≈ β/4 + O(β³)
    So Δ ≈ -ln(β/4) = ln(4/β)
    """
    if beta <= 0:
        return float('inf')
    return np.log(4 / beta)


def mass_gap_scan(beta_min: float = 0.1, beta_max: float = 20.0,
                  n_points: int = 200) -> tuple:
    """Scan mass gap across coupling range.

    Returns (betas, gaps_1d, gaps_strong_coupling).
    """
    betas = np.linspace(beta_min, beta_max, n_points)
    gaps_1d = np.array([mass_gap_1d(b) for b in betas])
    gaps_sc = np.array([mass_gap_strong_coupling(b) for b in betas])
    return betas, gaps_1d, gaps_sc


def transfer_matrix_2d_su2(L: int, beta: float, j_max: int = 5) -> np.ndarray:
    """Construct transfer matrix for 2D SU(2) lattice gauge theory.

    On a 2D lattice with L spatial sites and periodic BC:
    - L spatial links, each carrying an SU(2) element
    - L plaquettes per time slice
    - Transfer matrix acts on functions of L link variables

    In the character expansion basis, label states by (j₁, j₂, ..., j_L)
    where j_i is the representation on the i-th spatial link.

    For 2D, the transfer matrix in this basis is DIAGONAL (no spatial plaquettes
    coupling different representations). The eigenvalues are products of
    a_{j_i}(β) ratios.

    Actually in 2D: T_{j₁...j_L, j'₁...j'_L} factorizes by plaquette.
    Each plaquette couples one spatial and one temporal link.

    This is a warmup — 3D and 4D have spatial plaquettes that mix representations.
    """
    # In 2D, number of representations to keep per link
    n_reps = 2 * j_max + 1  # j = 0, 1/2, 1, ..., j_max

    coeffs = character_coefficients(beta, 2 * j_max)

    # In 2D, the transfer matrix for a single plaquette gives
    # eigenvalue a_j(β) for the j-th representation.
    # For L plaquettes: eigenvalue = ∏_{i=1}^L a_{j_i}(β)

    # State space: (j₁, ..., j_L) ∈ {0, 1/2, 1, ..., j_max}^L
    # This has n_reps^L states.

    n_states = n_reps ** L
    eigenvalues = np.zeros(n_states)

    for state_idx in range(n_states):
        # Decode state index into representation labels
        ev = 1.0
        idx = state_idx
        for _ in range(L):
            j_idx = idx % n_reps
            idx //= n_reps
            ev *= coeffs[j_idx]
        eigenvalues[state_idx] = ev

    # Sort eigenvalues descending
    eigenvalues = np.sort(eigenvalues)[::-1]
    return eigenvalues


def main():
    print("=" * 60)
    print("SU(2) Yang-Mills — Character Expansion Mass Gap")
    print("=" * 60)

    # 1. Character coefficients at various couplings
    print("\n--- Character Coefficients a_j(β) ---")
    for beta in [0.5, 1.0, 2.0, 5.0, 10.0]:
        coeffs = character_coefficients(beta, 6)
        print(f"β={beta:5.1f}: a_0={coeffs[0]:.6f}  a_½={coeffs[1]:.6f}  "
              f"a_1={coeffs[2]:.6f}  a_{3/2}={coeffs[3]:.6f}")

    # 2. 1D mass gap scan
    print("\n--- 1D Mass Gap Δ(β) ---")
    print(f"{'β':>8} {'Δ (exact)':>12} {'Δ (strong)':>12} {'ratio':>8}")
    for beta in [0.1, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 15.0, 20.0]:
        gap = mass_gap_1d(beta)
        gap_sc = mass_gap_strong_coupling(beta)
        ratio = gap / gap_sc if gap_sc > 0 and gap < 100 else float('nan')
        print(f"{beta:8.1f} {gap:12.6f} {gap_sc:12.6f} {ratio:8.4f}")

    # 3. 2D transfer matrix eigenvalues
    print("\n--- 2D Transfer Matrix (L=2, SU(2)) ---")
    for beta in [1.0, 2.0, 4.0, 8.0]:
        evals = transfer_matrix_2d_su2(L=2, beta=beta, j_max=3)
        gap = -np.log(evals[1] / evals[0]) if evals[0] > 0 and evals[1] > 0 else float('inf')
        print(f"β={beta:4.1f}: λ₀={evals[0]:.6f}  λ₁={evals[1]:.6f}  "
              f"Δ={gap:.6f}  (top 5: {evals[:5].round(6)})")

    print("\n--- 2D Transfer Matrix (L=3, SU(2)) ---")
    for beta in [1.0, 2.0, 4.0, 8.0]:
        evals = transfer_matrix_2d_su2(L=3, beta=beta, j_max=3)
        gap = -np.log(evals[1] / evals[0]) if evals[0] > 0 and evals[1] > 0 else float('inf')
        print(f"β={beta:4.1f}: λ₀={evals[0]:.6f}  λ₁={evals[1]:.6f}  "
              f"Δ={gap:.6f}")

    # 4. Physical mass gap scaling test
    print("\n--- Physical Mass Gap m = Δ/a (SU(2), 2D, L=2) ---")
    print("In 2D, YM is solvable. Mass gap should scale correctly.")
    print(f"{'β':>8} {'Δ (lattice)':>12} {'a (asympt.)':>12} {'m = Δ/a':>12}")
    b0_su2 = 22 / (48 * np.pi**2)  # one-loop beta function coeff for SU(2)
    for beta in [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 16.0, 20.0]:
        evals = transfer_matrix_2d_su2(L=2, beta=beta, j_max=5)
        gap = -np.log(evals[1] / evals[0]) if evals[1] > 0 else float('inf')
        # Asymptotic freedom: a ~ exp(-β/(4 b₀ N)) with N=2
        a_lattice = np.exp(-beta / (8 * b0_su2)) if beta > 0 else 1.0
        m_phys = gap / a_lattice if a_lattice > 0 and gap < 100 else float('nan')
        print(f"{beta:8.1f} {gap:12.6f} {a_lattice:12.6e} {m_phys:12.6e}")

    print("\n" + "=" * 60)
    print("NOTE: 2D YM has no propagating DOF — mass gap is 'trivial'.")
    print("The real test is 3D and 4D, which need Monte Carlo or")
    print("explicit transfer matrix construction in higher-dim rep basis.")
    print("=" * 60)


if __name__ == "__main__":
    main()
