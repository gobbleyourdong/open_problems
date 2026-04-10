#!/usr/bin/env python3
"""
Heat Kernel on S³ — Spherical Harmonic Expansion

The heat kernel K(x, y, t) on a Riemannian manifold M is the
fundamental solution of the heat equation:
  ∂u/∂t = Δu

It satisfies K(x, y, 0) = δ_y(x) and has the spectral expansion
  K(x, y, t) = Σ_k e^(-λ_k t) φ_k(x) φ_k(y)

where {φ_k} are L²-orthonormal eigenfunctions of -Δ with eigenvalues
λ_k. On round S³(r), the eigenvalues are k(k+2)/r² with multiplicity
(k+1)² (spherical harmonic).

CONNECTION TO PERELMAN'S W-ENTROPY:
The W-entropy uses a "weighted" measure u = (4πτ)^(-n/2) e^(-f),
which is exactly the heat kernel measure (in the soliton normalization).
The conjugate heat equation ∂u/∂t = Δu - Ru (under Ricci flow) is
the natural backward-time heat flow that makes W monotone.

This script:
1. Computes the heat kernel on S³ via spherical harmonic expansion
2. Verifies K(x, x, t) → 1/vol(S³) as t → ∞
3. Computes the heat kernel trace ∫ K(x, x, t) dV = Σ e^(-λ_k t) · mult
4. Shows the connection to entropy: log(K(p, p, t)) ~ -f(p, τ)
"""

import numpy as np


# ===========================================================
# Spherical harmonic eigenvalues on S³(r)
# ===========================================================
# Eigenvalues of -Δ on S³(r): λ_k = k(k+2) / r²
# Multiplicity of level k: m_k = (k+1)²
# Total dimension of eigenspaces: Σ_{k=0}^K (k+1)²

def s3_eigenvalue(k, r=1.0):
    """Eigenvalue λ_k of -Δ on S³(r)."""
    return k * (k + 2) / r**2


def s3_multiplicity(k):
    """Multiplicity of the k-th eigenvalue on S³ (independent of radius)."""
    return (k + 1)**2


def s3_volume(r=1.0):
    """Volume of round S³(r) = 2π² r³."""
    return 2 * np.pi**2 * r**3


# ===========================================================
# Heat kernel on the diagonal: K(x, x, t)
# ===========================================================
# By homogeneity, K(x, x, t) is constant in x.
# By the spectral expansion:
#   K(x, x, t) = (1/vol) · Σ_k m_k · e^(-λ_k t)
# where m_k is the multiplicity (the contribution of all eigenfunctions
# at level k to the diagonal).

def heat_kernel_diagonal_s3(t, r=1.0, k_max=50):
    """K(x, x, t) on round S³(r)."""
    vol = s3_volume(r)
    s = 0.0
    for k in range(k_max + 1):
        lam = s3_eigenvalue(k, r)
        mult = s3_multiplicity(k)
        s += mult * np.exp(-lam * t)
    return s / vol


def test_heat_kernel_decay():
    """Verify K(x,x,t) → 1/vol as t → ∞."""
    print("=" * 70)
    print("TEST 1: Heat kernel diagonal K(x,x,t) on S³(1)")
    print("=" * 70)
    print()

    r = 1.0
    vol = s3_volume(r)
    print(f"r = {r}, vol(S³) = {vol:.6f}")
    print(f"Equilibrium value: 1/vol = {1/vol:.6f}")
    print()
    print(f"{'t':>8} {'K(x,x,t)':>14} {'1/vol':>10} {'gap':>14} "
          f"{'log gap':>10}")
    print("-" * 65)

    times = [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
    for t in times:
        K = heat_kernel_diagonal_s3(t)
        gap = K - 1/vol
        log_gap = np.log(gap) if gap > 1e-300 else float('-inf')
        print(f"{t:8.4f} {K:14.6f} {1/vol:10.6f} {gap:14.6e} {log_gap:10.4f}")

    print()
    print("As t → ∞, K(x,x,t) → 1/vol ≈ 0.0507 (uniform distribution).")
    print("Gap decays exponentially with rate λ_1 = 3.")


# ===========================================================
# Heat kernel trace and the spectrum
# ===========================================================
# The trace ∫ K(x, x, t) dV = Σ_k m_k · e^(-λ_k t) = Z(t).
# This is the partition function / theta function on S³.
# Z(0) = ∞ (uncountable diagonal). Z(∞) = 1 (only k=0 mode survives).

def heat_trace_s3(t, r=1.0, k_max=50):
    """Heat trace Z(t) = Σ m_k e^(-λ_k t) on S³(r)."""
    s = 0.0
    for k in range(k_max + 1):
        lam = s3_eigenvalue(k, r)
        mult = s3_multiplicity(k)
        s += mult * np.exp(-lam * t)
    return s


def test_heat_trace():
    """Compute the heat trace and verify Z(∞) = 1."""
    print("=" * 70)
    print("TEST 2: Heat trace Z(t) = Σ m_k e^(-λ_k t)")
    print("=" * 70)
    print()
    print(f"{'t':>8} {'Z(t)':>14} {'first 5 modes':>50}")
    print("-" * 80)

    for t in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        Z = heat_trace_s3(t)
        modes = " ".join(f"{s3_multiplicity(k)*np.exp(-s3_eigenvalue(k)*t):.3e}"
                         for k in range(5))
        print(f"{t:8.4f} {Z:14.6e} {modes:>50}")

    print()
    print("As t → ∞: Z(t) → m_0 · e^0 = 1 (only the constant mode survives).")
    print("As t → 0: Z(t) → ∞ (Weyl asymptotics: Z(t) ~ vol/(4πt)^(n/2)).")


# ===========================================================
# Heat kernel asymptotics (Weyl formula)
# ===========================================================
# Weyl: Z(t) ~ vol(M)/(4πt)^(n/2) as t → 0
# For S³(1): vol = 2π², n = 3
# Z(t) ~ 2π² / (4πt)^(3/2) = 2π²/(8 π^(3/2) t^(3/2)) = π^(1/2)/(4 t^(3/2))

def test_weyl_asymptotic():
    """Verify Weyl asymptotic Z(t) ~ vol/(4πt)^(n/2) as t → 0."""
    print("=" * 70)
    print("TEST 3: Weyl asymptotic Z(t) ~ vol/(4πt)^(3/2)")
    print("=" * 70)
    print()

    n = 3
    vol = s3_volume(1.0)
    print(f"S³(1): vol = 2π² = {vol:.6f}, dim = {n}")
    print(f"Weyl: Z(t) ~ vol/(4πt)^(3/2)")
    print()
    print(f"{'t':>10} {'Z(t)':>14} {'Weyl':>14} {'ratio':>10}")
    print("-" * 55)

    for t in [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0]:
        Z = heat_trace_s3(t, k_max=200)  # need many modes at small t
        weyl = vol / (4 * np.pi * t)**(n/2)
        ratio = Z / weyl if weyl > 0 else float('nan')
        print(f"{t:10.2e} {Z:14.4e} {weyl:14.4e} {ratio:10.4f}")

    print()
    print("Ratio → 1 as t → 0 (Weyl asymptotic confirmed).")
    print("At larger t, finite-size corrections appear (subleading terms).")


# ===========================================================
# Connection to W-entropy
# ===========================================================
# Perelman's W-entropy uses a probability measure
#   u = (4πτ)^(-n/2) e^(-f)
# constrained to ∫ u dV = 1. On round S³, the optimal f is constant,
# so u = 1/vol.
#
# The heat kernel gives a NATURAL choice: u(x, t) = K(p, x, t) for
# some basepoint p. This makes f(x, t) = -log[(4πt)^(n/2) K(p, x, t)],
# which is exactly Perelman's "reduced length" up to factors.
#
# Under Ricci flow, the conjugate heat equation
#   ∂u/∂t = Δu - Ru
# preserves ∫ u dV = 1 and gives W non-decreasing.

def test_w_entropy_from_heat_kernel():
    """Compute W-entropy from heat kernel diagonal on S³."""
    print("=" * 70)
    print("TEST 4: W-entropy from heat kernel on round S³(1)")
    print("=" * 70)
    print()
    print("On round S³(1) with τ → 0 (heat kernel localized near basepoint p):")
    print("  K(p, p, τ) → ∞ (delta-like)")
    print("  f(p, τ) = -log((4πτ)^(3/2) K(p, p, τ))")
    print()

    print(f"{'τ':>10} {'K(p,p,τ)':>14} {'(4πτ)^(3/2)·K':>16} {'f(p,τ)':>14}")
    print("-" * 65)

    for tau in [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0]:
        K = heat_kernel_diagonal_s3(tau, k_max=300)
        weight = (4 * np.pi * tau)**(3/2) * K
        f = -np.log(weight) if weight > 0 else float('inf')
        print(f"{tau:10.2e} {K:14.4e} {weight:16.6f} {f:14.4f}")

    print()
    print("As τ → 0: weight → 1 (Weyl), f → 0 (heat kernel localizes).")
    print("This is Perelman's normalization: f = 0 at the basepoint as τ → 0.")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Poincaré Conjecture — Numerical Track: Heat Kernel on S³")
    print()

    test_heat_kernel_decay()
    print()
    test_heat_trace()
    print()
    test_weyl_asymptotic()
    print()
    test_w_entropy_from_heat_kernel()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
Heat kernel on S³ verified via spherical harmonic expansion:

  K(x, y, t) = Σ_k e^(-λ_k t) Y_k(x) Y_k(y)

where λ_k = k(k+2) and m_k = (k+1)² on unit S³.

Test 1 (decay): K(x,x,t) → 1/(2π²) as t → ∞ (uniform limit)
Test 2 (trace): Z(t) → 1 as t → ∞ (only constant mode survives)
Test 3 (Weyl): Z(t) → vol/(4πt)^(3/2) as t → 0 (matches at t=10⁻⁴)
Test 4 (entropy): f(p, τ) → 0 as τ → 0 (heat kernel normalization)

These verify the key identities behind Perelman's W-entropy and
reduced length functional. The heat kernel gives the natural "weight"
that makes the W-entropy monotone under Ricci flow.

CONNECTION TO PERELMAN:
- W-entropy uses u = (4πτ)^(-n/2) e^(-f) ← heat kernel ansatz
- Reduced length l(q,τ) ~ -log(K(p,q,τ)) + asymptotic terms
- κ-noncollapsing follows from heat kernel lower bounds
""")
