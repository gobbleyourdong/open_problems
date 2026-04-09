#!/usr/bin/env python3
"""
Test the interpolation f(t) = ⟨O⟩_t for t ∈ [0, 1].

t = 0: periodic BC (all c_j positive)
t = 1: anti-periodic BC (half-integer c_j flipped on surface Σ)

The interpolated coefficients on Σ plaquettes:
  c_j^(t) = c_j          for integer j
  c_j^(t) = (1-2t) c_j   for half-integer j

If f(t) is monotonically decreasing → f(0) ≥ f(1) → Tomboulis (5.15).

The even instance proved f decreasing for t ∈ [0, 1/2] (spectral positivity).
The gap is t ∈ [1/2, 1] where half-integer coefficients are NEGATIVE.

We test this on the 2D torus (exact computation via character expansion)
and the single-plaquette model to see if f(t) is indeed monotone.
"""

import numpy as np
from scipy.special import iv as bessel_i


def su2_coeffs(beta, j_max=6):
    """Character expansion coefficients c_j(β) for SU(2)."""
    coeffs = {}
    for j2 in range(0, int(2*j_max)+1):
        j = j2 / 2.0
        d = int(2*j+1)
        coeffs[j] = bessel_i(d, beta) / bessel_i(1, beta)
    return coeffs


def interpolated_Z_2d(beta, L, t, j_max=6):
    """
    Partition function on L×L 2D torus with interpolation parameter t.

    On 2D torus (genus 1): Z = Σ_j c_j^{F} where F = L² plaquettes.
    With vortex surface Σ (L plaquettes along one cycle):
      c_j^(t) on Σ: c_j for integer j, (1-2t)c_j for half-integer j
      c_j on non-Σ: c_j (unchanged)

    Z(t) = Σ_j [c_j^{Σ}(t)]^{L} · [c_j]^{L(L-1)}
         = Σ_j [c_j^{Σ}(t)]^L · c_j^{L²-L}

    For integer j: c_j^{Σ}(t) = c_j. So term = c_j^{L²}.
    For half-int j: c_j^{Σ}(t) = (1-2t)c_j. So term = [(1-2t)c_j]^L · c_j^{L²-L}
                                                      = (1-2t)^L · c_j^{L²}
    """
    coeffs = su2_coeffs(beta, j_max)
    Z = 0.0
    for j, c in coeffs.items():
        j2 = int(2*j)
        is_half_int = (j2 % 2 == 1)
        if is_half_int:
            Z += ((1 - 2*t)**L) * c**(L*L)
        else:
            Z += c**(L*L)
    return Z


def observable_expectation_2d(beta, L, t, j_max=6):
    """
    ⟨O⟩_t where O = Σ_P (∂c_j/∂α) χ_j(U_P).

    For simplicity, take O = average plaquette = (1/F) Σ_P (1/2)Tr(U_P).
    In character expansion: ⟨(1/2)Tr(U_P)⟩ = ∂ln Z / ∂β (up to normalization).

    Actually, let's compute f(t) = ln Z(t). If f(t) is concave in t, then
    f(0) ≥ f(1) follows from f'(0) > 0 and f'(1) < 0... no, need monotonicity.

    Let me compute the actual observable:
    ⟨O⟩_t = (1/Z(t)) Σ_j d_j c_j [weight_j(t)]

    For the "coupling response" observable O = ∂S/∂β:
    ⟨∂S/∂β⟩_t = (1/Z(t)) ∂Z(t)/∂β

    This is just the average plaquette. Let me compute Z(t) and ∂Z/∂β(t).
    """
    h = 1e-6
    Z = interpolated_Z_2d(beta, L, t, j_max)
    Z_plus = interpolated_Z_2d(beta + h, L, t, j_max)
    return (np.log(Z_plus) - np.log(Z)) / h  # = ⟨∂S/∂β⟩ = avg plaquette × F


def main():
    print("=" * 70)
    print("INTERPOLATION TEST: f(t) = ⟨O⟩_t for t ∈ [0, 1]")
    print("=" * 70)
    print("t=0: periodic BC. t=1: anti-periodic BC.")
    print("Need: f(0) ≥ f(1) (= Tomboulis 5.15)")
    print("Even instance proved: f decreasing on [0, 1/2]")
    print("Gap: is f also decreasing on [1/2, 1]?")
    print()

    # 2D torus test
    print("--- 2D Torus (exact character expansion) ---\n")

    ts = np.linspace(0, 1, 21)

    for beta in [1.0, 2.0, 3.0, 5.0, 10.0]:
        for L in [4, 6]:
            Zs = [interpolated_Z_2d(beta, L, t) for t in ts]
            lnZs = [np.log(max(abs(Z), 1e-300)) for Z in Zs]

            # Check monotonicity of ln Z(t)
            monotone = all(lnZs[i] >= lnZs[i+1] - 1e-10 for i in range(len(lnZs)-1))
            f0 = lnZs[0]
            f1 = lnZs[-1]

            print(f"β={beta:4.1f}, L={L}: ln Z(0)={f0:8.4f}, ln Z(1)={f1:8.4f}, "
                  f"f(0)≥f(1): {'YES ✓' if f0 >= f1 - 1e-10 else 'NO ✗'}, "
                  f"monotone: {'YES ✓' if monotone else 'NO ✗'}")

    # Detailed profile for β = 2.3, L = 4
    print(f"\n--- Detailed profile: β=2.3, L=4 ---")
    print(f"{'t':>6} | {'ln Z(t)':>12} | {'Z(t)':>12} | {'Δ(ln Z)':>10}")
    print("-" * 50)
    beta, L = 2.3, 4
    prev_lnZ = None
    for t in np.linspace(0, 1, 21):
        Z = interpolated_Z_2d(beta, L, t)
        lnZ = np.log(max(abs(Z), 1e-300))
        delta = f"{lnZ - prev_lnZ:+10.6f}" if prev_lnZ is not None else "    ---   "
        # Mark the t=0.5 boundary
        marker = " ← t=1/2" if abs(t - 0.5) < 0.01 else ""
        print(f"{t:6.2f} | {lnZ:12.6f} | {Z:12.4e} | {delta}{marker}")
        prev_lnZ = lnZ

    # Single-plaquette test (1D, simplest case)
    print(f"\n--- Single plaquette (1D chain, L=8) ---")
    print("Z(t) = Σ_j [(1-2t)^{half-int flag}]^L · [d_j c_j]^L")
    print()

    L = 8
    for beta in [1.0, 2.0, 4.0, 8.0]:
        coeffs = su2_coeffs(beta, j_max=6)
        Zs = []
        for t in ts:
            Z = 0.0
            for j, c in coeffs.items():
                j2 = int(2*j)
                d_j = 2*j + 1
                is_half = (j2 % 2 == 1)
                if is_half:
                    Z += ((1-2*t) * d_j * c) ** L
                else:
                    Z += (d_j * c) ** L
            Zs.append(Z)

        lnZs = [np.log(max(abs(Z), 1e-300)) for Z in Zs]
        f0, f1 = lnZs[0], lnZs[-1]
        monotone = all(lnZs[i] >= lnZs[i+1] - 1e-10 for i in range(len(lnZs)-1))
        print(f"β={beta:4.1f}: f(0)={f0:8.4f}, f(1)={f1:8.4f}, "
              f"f(0)≥f(1): {'YES ✓' if f0 >= f1 - 1e-10 else 'NO ✗'}, "
              f"monotone: {'YES ✓' if monotone else 'NO ✗'}")

    # The critical test: does f(t) have a MINIMUM in (1/2, 1)?
    print(f"\n--- Critical: where is min of f(t) on [0,1]? ---")
    for beta in [1.0, 2.0, 2.3, 3.0, 5.0, 10.0]:
        L = 4
        ts_fine = np.linspace(0, 1, 101)
        Zs = [interpolated_Z_2d(beta, L, t) for t in ts_fine]
        lnZs = np.array([np.log(max(abs(Z), 1e-300)) for Z in Zs])
        min_idx = np.argmin(lnZs)
        min_t = ts_fine[min_idx]
        print(f"β={beta:4.1f}, L={L}: min at t={min_t:.2f}, "
              f"f(0)-f(min)={lnZs[0]-lnZs[min_idx]:+.6f}, "
              f"f(1)-f(min)={lnZs[-1]-lnZs[min_idx]:+.6f}")


if __name__ == "__main__":
    main()
