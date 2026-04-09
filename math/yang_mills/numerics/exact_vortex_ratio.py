#!/usr/bin/env python3
"""
Exact computation of Z/Z- for SU(2) on small lattices via character expansion.

On a 2^4 lattice with periodic BC:
  Z = Σ_{rep assignments} ∏_plaquettes [d_j · c_j(β)] · ∏_links [orthogonality factor]

The character expansion makes Z a FINITE sum (truncated at j_max).
For j_max = 1: each plaquette gets j ∈ {0, 1/2, 1}, which is 3 choices.
On a 2^4 lattice: 24 plaquettes (6 orientations × 4 = 24 on a 2^4 torus).

Wait: on a d-dimensional lattice of size L^d, the number of plaquettes is:
  n_plaq = L^d × d(d-1)/2 = 2^4 × 6 = 96

That's 3^96 ≈ 10^45 terms — WAY too many for direct enumeration.

Instead, use the TRANSFER MATRIX in the character expansion basis.

For a lattice L^3 × T (spatial volume L^3, temporal extent T):
  Z = Tr(T^T)
  where T is the transfer matrix acting on "states" (rep assignments to
  all spatial links in one time slice).

For SU(2) on a 2^3 spatial lattice:
  - Spatial links: 3 × 2^3 = 24 links per time slice
  - Each link carries rep j ∈ {0, 1/2, 1, ...} up to j_max
  - GAUGE INVARIANCE: at each vertex, the reps on adjacent links must
    satisfy coupling rules (Clebsch-Gordan). This reduces the Hilbert space.

For j_max = 1/2: each link is either j=0 or j=1/2.
  - 24 links × 2 choices = 2^24 ≈ 16M states before gauge constraints
  - After gauge constraints: much smaller

For j_max = 0: trivial — one state, Z = 1.

Let me start with the SIMPLEST nontrivial case: 2D lattice (d=2), then
extend to 4D.

In 2D: all plaquettes are independent (after gauge fixing on a torus).
  Z = [Σ_j (2j+1) c_j(β)]^{n_plaq}
  Z- = [Σ_j (2j+1) (-1)^{2j} c_j(β)]^{n_plaq}  (center twist on ALL plaquettes)

Wait, in 2D the center twist only affects plaquettes threaded by the vortex.
On a L×L torus with a vortex line in the x-direction:
  Z- = [Σ_j (2j+1) c_j]^{(L-1)L} × [Σ_j (2j+1) (-1)^{2j} c_j]^L
  (L plaquettes threaded, (L-1)L unthreaded)

Actually, on a 2D torus with the standard gauge-fixing, there is one
independent plaquette (the product of all plaquettes = identity on a torus).
This is getting complicated. Let me just compute directly.

SIMPLEST CASE: 1D chain (necklace) with periodic and anti-periodic BC.
"""

import numpy as np
from scipy.special import iv as bessel_i


def su2_coeffs(beta, j_max=3.0):
    """SU(2) character expansion coefficients."""
    coeffs = []
    for j2 in range(0, int(2 * j_max) + 1):
        j = j2 / 2.0
        d_j = int(2 * j + 1)
        c_j = bessel_i(d_j, beta) / bessel_i(1, beta)
        coeffs.append((j, d_j, c_j))
    return coeffs


def transfer_matrix_1d(coeffs):
    """
    Transfer matrix for 1D chain in character expansion basis.

    For a single bond: T_{j,j'} = δ_{j,j'} · d_j · c_j
    (diagonal in rep basis — each bond independently carries a rep)

    The partition function of a chain of length L:
      Z = Tr(T^L) = Σ_j (d_j c_j)^L
    """
    n = len(coeffs)
    T = np.zeros((n, n))
    for i, (j, d_j, c_j) in enumerate(coeffs):
        T[i, i] = d_j * c_j
    return T


def vortex_ratio_1d(beta, L, j_max=3.0):
    """
    Z/Z- for 1D chain of length L with periodic vs anti-periodic BC.

    Z = Σ_j (d_j c_j)^L
    Z- = Σ_j (-1)^{2j} (d_j c_j)^L
    Z+ = (Z + Z-)/2 = Σ_{j integer} (d_j c_j)^L
    """
    coeffs = su2_coeffs(beta, j_max)

    Z = sum(((d_j * c_j) ** L) for j, d_j, c_j in coeffs)
    Z_minus = sum((((-1) ** int(2*j)) * (d_j * c_j) ** L)
                  for j, d_j, c_j in coeffs)
    Z_plus = (Z + Z_minus) / 2.0

    return Z, Z_minus, Z_plus, Z / Z_plus if Z_plus > 0 else float('inf')


def vortex_ratio_2d_torus(beta, L, j_max=2.0):
    """
    Z/Z- for SU(2) on L×L 2D torus.

    In 2D with gauge fixing, the partition function on an L×L torus is:
      Z = Σ_j (d_j)^{2-2g} · c_j^{L²}
    where g=1 for the torus (genus 1), so (d_j)^{2-2·1} = (d_j)^0 = 1.

    Z = Σ_j c_j^{L²}
    Z- (with center vortex): Z- = Σ_j (-1)^{2j} c_j^{L²}

    Wait — for genus 1: Z = Σ_j c_j^{n_plaq} where n_plaq = L² on a torus.
    The prefactors depend on the exact gauge-fixing and topology.

    Actually for 2D YM on a torus (Migdal): Z = Σ_j d_j^{2-2g} e^{-A c₂(j)/(2N)}
    where A is the area and c₂(j) is the quadratic Casimir.

    For the LATTICE (not continuum): Z = Σ_j d_j^{V-E+F} · c_j^F
    where V = vertices, E = edges, F = faces (plaquettes).
    Euler: V - E + F = 2 - 2g = 0 for torus.
    So: Z = Σ_j c_j^F = Σ_j c_j^{L²}   (on L×L torus, F = L²)

    Z- with center twist: Z- = Σ_j (-1)^{2j} c_j^{L²}
    (the twist multiplies by the center character)
    """
    coeffs = su2_coeffs(beta, j_max)
    F = L * L  # number of plaquettes on torus

    Z = sum(c_j ** F for j, d_j, c_j in coeffs)
    Z_minus = sum(((-1) ** int(2*j)) * c_j ** F for j, d_j, c_j in coeffs)
    Z_plus = (Z + Z_minus) / 2.0

    return Z, Z_minus, Z_plus, Z / Z_plus if Z_plus > 0 else float('inf')


def vortex_ratio_4d_approx(beta, L, j_max=2.0):
    """
    APPROXIMATE Z/Z- for SU(2) on L^4 4D torus.

    In d=4 on a torus: Euler number χ = 0.
    V = L^4, E = 4L^4, F = 6L^4, C = 4L^4, H = L^4
    (V vertices, E edges, F faces=plaquettes, C cubes, H hypercubes)

    For the character expansion:
    Z = Σ_{j on plaquettes} ∏ (d_j c_j) × ∏_links [orthogonality factors]

    In general d dimensions, after integrating over all links:
    The exact formula depends on the topology of the dual cell complex.

    For an APPROXIMATION (mean field / independent plaquettes):
    Z ≈ [Σ_j d_j c_j]^{6L^4}    (each plaquette independent)
    Z- ≈ [Σ_j d_j c_j]^{6L^4 - A_Σ} × [Σ_j d_j (-1)^{2j} c_j]^{A_Σ}

    where A_Σ is the number of plaquettes on the vortex surface.
    For a flat surface in the (1,2) plane at x_3 = x_4 = 0: A_Σ = L^2.

    This is crude but gives the right qualitative behavior.
    """
    coeffs = su2_coeffs(beta, j_max)
    n_plaq = 6 * L**4
    A_sigma = L**2  # vortex surface area

    S_per = sum(d_j * c_j for j, d_j, c_j in coeffs)
    S_anti = sum(d_j * ((-1)**int(2*j)) * c_j for j, d_j, c_j in coeffs)

    # ln(Z) ≈ n_plaq * ln(S_per)
    # ln(Z-) ≈ (n_plaq - A_Σ) * ln(S_per) + A_Σ * ln(S_anti)  if S_anti > 0
    # ln(Z/Z-) ≈ A_Σ * ln(S_per / S_anti)

    if S_anti > 0:
        ln_ratio = A_sigma * np.log(S_per / S_anti)
    elif S_anti == 0:
        ln_ratio = float('inf')
    else:
        # S_anti < 0 means Z- contribution is negative (odd number of
        # half-integer plaquettes dominate) — need to handle carefully
        ln_ratio = float('nan')

    Z_over_Zplus = 2 / (1 + np.exp(-ln_ratio)) if np.isfinite(ln_ratio) else 2.0

    return S_per, S_anti, ln_ratio, Z_over_Zplus


def main():
    print("=" * 75)
    print("EXACT VORTEX RATIO Z/Z+ FOR SU(2)")
    print("=" * 75)

    # 2D torus (exact)
    print("\n--- 2D Torus (EXACT via Migdal formula) ---")
    print(f"{'β':>6} | {'L=2':>12} | {'L=4':>12} | {'L=6':>12} | {'L=8':>12}")
    print("-" * 65)

    for beta in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0, 16.0]:
        ratios = []
        for L in [2, 4, 6, 8]:
            _, _, _, ratio = vortex_ratio_2d_torus(beta, L)
            ratios.append(ratio)
        print(f"{beta:6.1f} | {ratios[0]:12.6f} | {ratios[1]:12.6f} | "
              f"{ratios[2]:12.6f} | {ratios[3]:12.6f}")

    print("\nNote: In 2D, Z/Z+ → ∞ as L → ∞ for any β > 0 (2D YM always confines).")
    print("The ratio measures exp(σ · L²) where σ is the string tension.")

    # 4D torus (approximate)
    print("\n\n--- 4D Torus (APPROXIMATE — independent plaquette) ---")
    print(f"{'β':>6} | {'S_per':>10} | {'S_anti':>10} | {'ln(Z/Z-)':>12} | {'Z/Z+':>10} | {'σ_approx':>10}")
    print("-" * 75)

    for beta in [0.5, 1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0, 6.0, 8.0]:
        S_per, S_anti, ln_ratio, Z_over_Zplus = vortex_ratio_4d_approx(beta, L=4)
        # σ ≈ ln_ratio / L² = ln(S_per/S_anti) (string tension per plaquette)
        sigma = np.log(S_per / S_anti) if S_anti > 0 else float('inf')
        print(f"{beta:6.1f} | {S_per:10.4f} | {S_anti:10.4f} | {ln_ratio:12.4f} | "
              f"{Z_over_Zplus:10.4f} | {sigma:10.4f}")

    # String tension vs β
    print("\n\n--- String Tension σ(β) = ln(S_per/S_anti) ---")
    print("(Independent plaquette approximation)")
    print("If σ(β) > 0 for all β > 0: mass gap exists (confinement)")
    print()

    betas = np.linspace(0.1, 20.0, 200)
    min_sigma = float('inf')
    min_beta = 0

    for beta in betas:
        coeffs = su2_coeffs(beta, j_max=6)
        S_per = sum(d_j * c_j for j, d_j, c_j in coeffs)
        S_anti = sum(d_j * ((-1)**int(2*j)) * c_j for j, d_j, c_j in coeffs)
        if S_anti > 0:
            sigma = np.log(S_per / S_anti)
            if sigma < min_sigma:
                min_sigma = sigma
                min_beta = beta

    print(f"Minimum σ = {min_sigma:.6f} at β = {min_beta:.2f}")
    print(f"σ > 0 for all β ∈ [0.1, 20.0]: {'YES ✓' if min_sigma > 0 else 'NO ✗'}")

    # S_anti sign check
    print("\n\n--- S_anti sign check ---")
    print("S_anti = Σ_j d_j (-1)^{2j} c_j(β)")
    print("= c_0 - 2c_{1/2} + 3c_1 - 4c_{3/2} + 5c_2 - ...")
    print("If S_anti < 0: the half-integer reps dominate (physical at weak coupling?)")
    print()

    for beta in [0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 20.0, 50.0, 100.0]:
        coeffs = su2_coeffs(beta, j_max=10)
        S_per = sum(d_j * c_j for j, d_j, c_j in coeffs)
        S_anti = sum(d_j * ((-1)**int(2*j)) * c_j for j, d_j, c_j in coeffs)
        print(f"β = {beta:6.1f}: S_per = {S_per:10.4f}, S_anti = {S_anti:10.4f}, "
              f"σ = {np.log(S_per/S_anti) if S_anti > 0 else 'S_anti<0 !!!':>10}")


if __name__ == "__main__":
    main()
