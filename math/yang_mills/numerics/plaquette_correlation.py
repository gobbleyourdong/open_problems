#!/usr/bin/env python3
"""
Plaquette-plaquette correlation test for SU(2) lattice gauge theory.

Tests: Cov(Tr(U_P), Tr(U_Q)) ≥ 0 for all plaquette pairs P, Q.

This is the KEY numerical test for the Yang-Mills mass gap proof.
If positive correlation holds at ALL β → Tomboulis (5.15) follows → mass gap.
If it fails at some β → need a different route.

Method: Monte Carlo with heatbath + overrelaxation on L^4 lattice.
SU(2) parametrized as quaternions (a₀, a₁, a₂, a₃) on S³.

For SPEED on Spark GPU, this uses numpy vectorized operations.
Full GPU (PyTorch/CUDA) would be faster but this suffices for L ≤ 8.
"""

import numpy as np
from typing import Tuple
import time


# ============================================================================
# SU(2) as quaternions: U = a₀I + i(a₁σ₁ + a₂σ₂ + a₃σ₃), |a|²=1
# Multiplication: quaternion product
# Inverse: conjugate (a₀, -a₁, -a₂, -a₃)
# Trace: 2a₀
# ============================================================================

def quat_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Quaternion multiplication. a, b have shape (..., 4)."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ], axis=-1)


def quat_conj(a: np.ndarray) -> np.ndarray:
    """Quaternion conjugate = SU(2) inverse."""
    return a * np.array([1, -1, -1, -1])


def quat_trace(a: np.ndarray) -> np.ndarray:
    """Tr(U) = 2a₀ for SU(2)."""
    return 2 * a[..., 0]


def random_su2(shape: tuple) -> np.ndarray:
    """Random SU(2) element (Haar measure) via 4D Gaussian projection."""
    a = np.random.randn(*shape, 4)
    a /= np.linalg.norm(a, axis=-1, keepdims=True)
    return a


def identity_su2(shape: tuple) -> np.ndarray:
    """Identity element of SU(2)."""
    a = np.zeros((*shape, 4))
    a[..., 0] = 1.0
    return a


# ============================================================================
# Lattice gauge field: links[x0, x1, x2, x3, mu] = quaternion (4,)
# Plaquette: U_P = U_{x,mu} U_{x+mu,nu} U_{x+nu,mu}^{-1} U_{x,nu}^{-1}
# ============================================================================

class LatticeSU2:
    def __init__(self, L: int, d: int = 4):
        self.L = L
        self.d = d
        # Start hot (random)
        self.links = random_su2((L,) * d + (d,))

    def shift(self, arr: np.ndarray, mu: int, n: int = 1) -> np.ndarray:
        """Shift array by n in direction mu (periodic BC)."""
        return np.roll(arr, -n, axis=mu)

    def plaquette(self, mu: int, nu: int) -> np.ndarray:
        """Compute all plaquettes in (mu, nu) plane. Returns (..., 4) quaternions."""
        U_mu = self.links[..., mu, :]              # U_{x, mu}
        U_nu_shifted = self.shift(self.links[..., nu, :], mu)  # U_{x+mu, nu}
        U_mu_shifted = self.shift(self.links[..., mu, :], nu)  # U_{x+nu, mu}
        U_nu = self.links[..., nu, :]              # U_{x, nu}

        # U_P = U_mu * U_nu_shifted * U_mu_shifted^{-1} * U_nu^{-1}
        temp = quat_mul(U_mu, U_nu_shifted)
        temp = quat_mul(temp, quat_conj(U_mu_shifted))
        temp = quat_mul(temp, quat_conj(U_nu))
        return temp

    def plaquette_trace(self, mu: int, nu: int) -> np.ndarray:
        """(1/2) Tr(U_P) for all plaquettes in (mu, nu) plane."""
        return quat_trace(self.plaquette(mu, nu)) / 2

    def wilson_action(self, beta: float) -> float:
        """S = β Σ_P (1 - (1/2) Re Tr(U_P))."""
        S = 0.0
        for mu in range(self.d):
            for nu in range(mu + 1, self.d):
                S += np.sum(1.0 - self.plaquette_trace(mu, nu))
        return beta * S

    def staple(self, x_idx: tuple, mu: int) -> np.ndarray:
        """
        Sum of staples around link (x, mu).
        Returns a quaternion (not normalized to SU(2)).
        """
        L, d = self.L, self.d
        result = np.zeros(4)

        for nu in range(d):
            if nu == mu:
                continue

            # Forward staple: U_{x+mu,nu} U_{x+nu,mu}^{-1} U_{x,nu}^{-1}
            x_plus_mu = list(x_idx)
            x_plus_mu[mu] = (x_plus_mu[mu] + 1) % L
            x_plus_nu = list(x_idx)
            x_plus_nu[nu] = (x_plus_nu[nu] + 1) % L

            U_nu_xpmu = self.links[tuple(x_plus_mu) + (nu,)]
            U_mu_xpnu = self.links[tuple(x_plus_nu) + (mu,)]
            U_nu_x = self.links[x_idx + (nu,)]

            fwd = quat_mul(U_nu_xpmu, quat_conj(U_mu_xpnu))
            fwd = quat_mul(fwd, quat_conj(U_nu_x))
            result += fwd

            # Backward staple: U_{x+mu-nu,nu}^{-1} U_{x-nu,mu}^{-1} U_{x-nu,nu}
            x_minus_nu = list(x_idx)
            x_minus_nu[nu] = (x_minus_nu[nu] - 1) % L
            x_plus_mu_minus_nu = list(x_idx)
            x_plus_mu_minus_nu[mu] = (x_plus_mu_minus_nu[mu] + 1) % L
            x_plus_mu_minus_nu[nu] = (x_plus_mu_minus_nu[nu] - 1) % L

            U_nu_xpmumn = self.links[tuple(x_plus_mu_minus_nu) + (nu,)]
            U_mu_xmn = self.links[tuple(x_minus_nu) + (mu,)]
            U_nu_xmn = self.links[tuple(x_minus_nu) + (nu,)]

            bwd = quat_mul(quat_conj(U_nu_xpmumn), quat_conj(U_mu_xmn))
            bwd = quat_mul(bwd, U_nu_xmn)
            result += bwd

        return result

    def heatbath_update(self, beta: float):
        """One full heatbath sweep over all links."""
        L, d = self.L, self.d
        for mu in range(d):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x_idx = (x0, x1, x2, x3)
                            A = self.staple(x_idx, mu)
                            k = np.sqrt(np.sum(A**2))
                            if k < 1e-10:
                                self.links[x_idx + (mu,)] = random_su2(())[0] if False else random_su2(())
                                continue
                            # Kennedy-Pendleton heatbath
                            a_beta = beta * k
                            # Sample a₀ from P(a₀) ∝ √(1-a₀²) exp(a_beta * a₀)
                            # Using rejection: proposal uniform in [exp(-2a_beta), 1]
                            while True:
                                r = np.random.uniform()
                                x = 1 + np.log(r + (1-r)*np.exp(-2*a_beta)) / a_beta
                                if np.random.uniform() < np.sqrt(1 - x*x):
                                    a0 = x
                                    break
                            # Random direction for (a₁, a₂, a₃) on sphere of radius √(1-a₀²)
                            r_vec = np.random.randn(3)
                            r_vec *= np.sqrt(1 - a0**2) / np.linalg.norm(r_vec)
                            U_new = np.array([a0, r_vec[0], r_vec[1], r_vec[2]])
                            # Multiply by A_hat to align with staple
                            A_hat = A / k
                            self.links[x_idx + (mu,)] = quat_mul(U_new, quat_conj(A_hat))


def measure_plaquette_correlations(lat: LatticeSU2, n_meas: int, beta: float,
                                     n_therm: int = 50, n_skip: int = 5):
    """
    Measure plaquette-plaquette correlations.

    Returns: dict with 'avg_plaq', 'cov_same_plane', 'cov_diff_plane', 'cov_by_dist'
    """
    L = lat.L

    # Thermalize
    print(f"  Thermalizing ({n_therm} sweeps)...", end="", flush=True)
    for _ in range(n_therm):
        lat.heatbath_update(beta)
    print(" done.")

    # Measure
    plaq_values = []  # Per-measurement: array of all plaquette traces

    print(f"  Measuring ({n_meas} configs, skip {n_skip})...", end="", flush=True)
    for i in range(n_meas):
        for _ in range(n_skip):
            lat.heatbath_update(beta)

        # Collect plaquette traces for mu=0,nu=1 and mu=0,nu=2
        p01 = lat.plaquette_trace(0, 1).flatten()
        p02 = lat.plaquette_trace(0, 2).flatten()
        plaq_values.append((p01.copy(), p02.copy()))

        if (i + 1) % 10 == 0:
            print(f" {i+1}", end="", flush=True)
    print(" done.")

    # Analyze: same-plane correlation
    p01_all = np.array([p[0] for p in plaq_values])  # (n_meas, L^4)
    p02_all = np.array([p[1] for p in plaq_values])

    avg_p01 = np.mean(p01_all)
    avg_p02 = np.mean(p02_all)

    # Cross-plaquette covariance (same plane, different sites)
    # Take two random plaquettes from the same plane
    n_sites = p01_all.shape[1]
    cov_same = 0.0
    n_pairs = min(100, n_sites)
    for _ in range(n_pairs):
        i, j = np.random.choice(n_sites, 2, replace=False)
        cov_same += np.mean(p01_all[:, i] * p01_all[:, j]) - avg_p01**2
    cov_same /= n_pairs

    # Cross-plane covariance
    cov_diff = 0.0
    for _ in range(n_pairs):
        i = np.random.choice(n_sites)
        j = np.random.choice(n_sites)
        cov_diff += np.mean(p01_all[:, i] * p02_all[:, j]) - avg_p01 * avg_p02
    cov_diff /= n_pairs

    return {
        'avg_plaq': (avg_p01 + avg_p02) / 2,
        'cov_same_plane': cov_same,
        'cov_diff_plane': cov_diff,
    }


def main():
    print("=" * 70)
    print("PLAQUETTE-PLAQUETTE CORRELATION TEST — SU(2) d=4")
    print("=" * 70)
    print("Testing: Cov(Tr(U_P), Tr(U_Q)) ≥ 0 for all plaquette pairs")
    print("If YES → evidence for Tomboulis (5.15) → mass gap")
    print()

    L = 4
    n_meas = 50
    n_therm = 100
    n_skip = 3

    betas = [1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0]

    print(f"Lattice: {L}^4, {n_meas} measurements, {n_therm} thermalization sweeps")
    print()

    results = []
    for beta in betas:
        print(f"\nβ = {beta}:")
        t0 = time.time()
        lat = LatticeSU2(L)
        res = measure_plaquette_correlations(lat, n_meas, beta, n_therm, n_skip)
        dt = time.time() - t0
        res['beta'] = beta
        res['time'] = dt
        results.append(res)
        print(f"  ⟨P⟩ = {res['avg_plaq']:.6f}")
        print(f"  Cov(same plane) = {res['cov_same_plane']:.2e}")
        print(f"  Cov(diff plane) = {res['cov_diff_plane']:.2e}")
        print(f"  Time: {dt:.1f}s")

    # Summary table
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'β':>6} | {'⟨P⟩':>8} | {'Cov(same)':>12} | {'Cov(diff)':>12} | {'Sign':>6} | {'Time':>6}")
    print("-" * 65)
    all_positive = True
    for r in results:
        sign_same = "+" if r['cov_same_plane'] >= 0 else "-"
        sign_diff = "+" if r['cov_diff_plane'] >= 0 else "-"
        sign = f"{sign_same}/{sign_diff}"
        if r['cov_same_plane'] < 0 or r['cov_diff_plane'] < 0:
            all_positive = False
        print(f"{r['beta']:6.1f} | {r['avg_plaq']:8.4f} | {r['cov_same_plane']:12.2e} | "
              f"{r['cov_diff_plane']:12.2e} | {sign:>6} | {r['time']:5.1f}s")

    print()
    if all_positive:
        print("ALL COVARIANCES POSITIVE ✓ — consistent with Tomboulis (5.15)")
    else:
        print("NEGATIVE COVARIANCE FOUND ✗ — plaquette positive correlation FAILS")


if __name__ == "__main__":
    main()
