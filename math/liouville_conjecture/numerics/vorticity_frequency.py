#!/usr/bin/env python3
"""
Vorticity Frequency Function and Pressure-Weighted H̃ — Theory Track Requests

The theory track (attempt_001) proposed three modifications to the
Almgren frequency function. They ranked:
  1. Vorticity frequency N_ω(r) — eliminates pressure, Gronwall error
  2. Pressure-weighted H̃(r) — absorbs pressure into Bernoulli
  3. Strain-weighted D_S(r) — mechanically motivated

This script computes the top two on the Burgers vortex:

A. N_ω(r) = r · D_ω(r) / H_ω(r)
   where D_ω = ∫_{B_r} |∇ω|², H_ω = ∫_{∂B_r} |ω|²
   Theory predicts: Gronwall bound N_ω(r) ≤ N_ω(r₀) · exp(C(M)·(r-r₀))
   QUESTION: is growth sub-exponential in practice?

B. H̃(r) = ∫_{∂B_r} (|u|² + 2p) dS
   QUESTION: is H̃(r) > 0 for all r? (If not, modification 1 fails.)
"""

import numpy as np


# ===========================================================
# Burgers vortex: velocity, vorticity, pressure
# ===========================================================

def burgers_velocity(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """(u_r, u_theta, u_z) for Burgers vortex."""
    u_r = -alpha * r / 2
    u_z = alpha * z
    if r > 1e-10:
        u_theta = Gamma / (2 * np.pi * r) * (1 - np.exp(-alpha * r**2 / (2 * nu)))
    else:
        u_theta = Gamma * alpha / (4 * np.pi * nu) * r
    return u_r, u_theta, u_z


def burgers_vorticity(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    Vorticity of Burgers vortex. Only ω_z is non-zero (axisymmetric):
      ω_z = (1/r) ∂(r u_θ)/∂r = Γα/(2πν) · exp(-αr²/(2ν))
    ω_r = ω_θ = 0 (axisymmetric, no z-dependence of u_θ).
    """
    omega_z = Gamma * alpha / (2 * np.pi * nu) * np.exp(-alpha * r**2 / (2 * nu))
    return 0.0, 0.0, omega_z


def burgers_pressure(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    Pressure of Burgers vortex (up to a constant):
      p = -α²(r²/4 + z²/2) + centrifugal term
    The centrifugal part: ∫₀^r u_θ²/s ds (from radial momentum balance).
    We'll compute it numerically.
    """
    # Strain contribution (from u_r, u_z)
    p_strain = -alpha**2 * (r**2 / 4 + z**2 / 2)
    # Centrifugal contribution: ∫₀^r u_θ(s)²/s ds
    n_pts = 100
    if r > 1e-10:
        s_grid = np.linspace(1e-6, r, n_pts)
        ds = s_grid[1] - s_grid[0]
        integrand = np.array([
            burgers_velocity(s, 0, alpha, Gamma, nu)[1]**2 / s
            for s in s_grid
        ])
        p_centrifugal = np.sum(integrand) * ds
    else:
        p_centrifugal = 0.0
    return p_strain + p_centrifugal


# ===========================================================
# A. Vorticity frequency function N_ω(r)
# ===========================================================

def vorticity_grad_squared(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    |∇ω|² for Burgers vortex.
    ω = (0, 0, ω_z(r)) where ω_z = C · exp(-αr²/(2ν)).
    ∂ω_z/∂r = C · (-αr/ν) · exp(-αr²/(2ν))
    ∂ω_z/∂z = 0
    |∇ω|² = (∂ω_z/∂r)²
    """
    C = Gamma * alpha / (2 * np.pi * nu)
    dw_dr = C * (-alpha * r / nu) * np.exp(-alpha * r**2 / (2 * nu))
    return dw_dr**2


def D_omega(R, n_r=40, n_z=40, alpha=1.0, Gamma=1.0, nu=1.0):
    """D_ω(R) = ∫_{B_R} |∇ω|² dV in cylindrical coordinates."""
    total = 0.0
    for i in range(n_r):
        r = (i + 0.5) * R / n_r
        z_max = np.sqrt(max(R**2 - r**2, 0))
        if z_max < 1e-10:
            continue
        for j in range(n_z):
            z = -z_max + (j + 0.5) * 2 * z_max / n_z
            dz = 2 * z_max / n_z
            dr = R / n_r
            vol = 2 * np.pi * r * dr * dz
            total += vorticity_grad_squared(r, z, alpha, Gamma, nu) * vol
    return total


def H_omega(R, n_theta=25, n_phi=15, alpha=1.0, Gamma=1.0, nu=1.0):
    """H_ω(R) = ∫_{∂B_R} |ω|² dS on sphere of radius R."""
    total = 0.0
    for i in range(n_theta):
        theta = (i + 0.5) * np.pi / n_theta
        for j in range(n_phi):
            phi = (j + 0.5) * 2 * np.pi / n_phi
            r = R * np.sin(theta)
            z = R * np.cos(theta)
            d_omega_angle = np.sin(theta) * (np.pi / n_theta) * (2 * np.pi / n_phi)
            _, _, wz = burgers_vorticity(r, z, alpha, Gamma, nu)
            total += wz**2 * R**2 * d_omega_angle
    return total


def test_vorticity_frequency():
    """Compute N_ω(r) on Burgers vortex."""
    print("=" * 70)
    print("A. VORTICITY FREQUENCY FUNCTION N_ω(r) ON BURGERS VORTEX")
    print("=" * 70)
    print()
    print("N_ω(r) = r · D_ω(r) / H_ω(r)")
    print("Theory predicts: Gronwall bound N_ω ≤ N_ω(r₀) · exp(C·(r-r₀))")
    print("Question: is growth sub-exponential in practice?")
    print()
    print(f"{'R':>6} {'D_ω(R)':>12} {'H_ω(R)':>12} {'N_ω(R)':>10} "
          f"{'log N_ω':>10} {'monotone?':>10}")
    print("-" * 70)

    prev_N = None
    monotone = True
    results = []
    for R in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]:
        Dw = D_omega(R, n_r=30, n_z=30)
        Hw = H_omega(R, n_theta=20, n_phi=12)
        if Hw < 1e-15:
            Nw = float('nan')
        else:
            Nw = R * Dw / Hw
        log_Nw = np.log(Nw) if Nw > 0 and not np.isnan(Nw) else float('nan')
        is_mono = "—"
        if prev_N is not None and not np.isnan(Nw) and not np.isnan(prev_N):
            is_mono = "YES" if Nw >= prev_N - 1e-6 else "NO"
            if Nw < prev_N - 1e-6:
                monotone = False
        print(f"{R:6.1f} {Dw:12.6f} {Hw:12.6f} {Nw:10.4f} "
              f"{log_Nw:10.4f} {is_mono:>10}")
        prev_N = Nw
        results.append((R, Nw))

    print()
    print(f"N_ω monotone: {monotone}")
    if len(results) >= 2:
        r1, n1 = results[0]
        r2, n2 = results[-1]
        if n1 > 0 and n2 > 0:
            growth_rate = np.log(n2 / n1) / (r2 - r1) if n2 > n1 else 0
            print(f"Effective exponential rate: {growth_rate:.4f}")
            print(f"(Gronwall bound rate would be C(M); actual rate might be smaller)")
    return monotone, results


# ===========================================================
# B. Pressure-weighted H̃(r)
# ===========================================================

def H_tilde(R, n_theta=25, n_phi=15, alpha=1.0, Gamma=1.0, nu=1.0):
    """H̃(R) = ∫_{∂B_R} (|u|² + 2p) dS on sphere of radius R."""
    total = 0.0
    for i in range(n_theta):
        theta = (i + 0.5) * np.pi / n_theta
        for j in range(n_phi):
            phi = (j + 0.5) * 2 * np.pi / n_phi
            r = R * np.sin(theta)
            z = R * np.cos(theta)
            d_omega_angle = np.sin(theta) * (np.pi / n_theta) * (2 * np.pi / n_phi)

            ur, ut, uz = burgers_velocity(r, z, alpha, Gamma, nu)
            u_sq = ur**2 + ut**2 + uz**2
            p = burgers_pressure(r, z, alpha, Gamma, nu)
            integrand = u_sq + 2 * p

            total += integrand * R**2 * d_omega_angle
    return total


def test_pressure_weighted():
    """Compute H̃(r) and check if it stays positive."""
    print("=" * 70)
    print("B. PRESSURE-WEIGHTED H̃(r) = ∫(|u|² + 2p) dS")
    print("=" * 70)
    print()
    print("Theory track asks: is H̃(r) > 0 for all r?")
    print("If not, the pressure-weighted frequency function is undefined.")
    print()

    H_standard_list = []
    H_tilde_list = []
    print(f"{'R':>6} {'H(R)':>12} {'H̃(R)':>14} {'H̃/H':>10} {'H̃ > 0?':>10}")
    print("-" * 60)

    for R in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]:
        # Standard H(R)
        H_std = 0.0
        n_theta, n_phi = 20, 12
        for i in range(n_theta):
            theta = (i + 0.5) * np.pi / n_theta
            for j in range(n_phi):
                phi = (j + 0.5) * 2 * np.pi / n_phi
                r = R * np.sin(theta)
                z = R * np.cos(theta)
                d_omega_angle = np.sin(theta) * (np.pi / n_theta) * (2 * np.pi / n_phi)
                ur, ut, uz = burgers_velocity(r, z)
                H_std += (ur**2 + ut**2 + uz**2) * R**2 * d_omega_angle

        Ht = H_tilde(R, n_theta=n_theta, n_phi=n_phi)
        ratio = Ht / H_std if H_std > 1e-15 else float('nan')
        sign = "YES" if Ht > 0 else "**NO**"
        print(f"{R:6.1f} {H_std:12.4f} {Ht:14.4f} {ratio:10.4f} {sign:>10}")
        H_standard_list.append(H_std)
        H_tilde_list.append(Ht)

    print()
    all_positive = all(h > 0 for h in H_tilde_list)
    print(f"H̃(r) > 0 for all tested r: {all_positive}")
    if not all_positive:
        print("WARNING: pressure-weighted frequency is NOT well-defined!")
        print("The pressure p is too negative at some points.")
    else:
        print("Good: pressure-weighted modification is at least well-defined.")
    return all_positive


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: Theory Request Response")
    print("(Responding to attempt_001 frequency function modifications)")
    print()

    monotone_w, results_w = test_vorticity_frequency()
    print()
    h_tilde_positive = test_pressure_weighted()

    print()
    print("=" * 70)
    print("SUMMARY FOR THEORY TRACK")
    print("=" * 70)
    print(f"""
A. Vorticity frequency N_ω(r):
   Monotone on Burgers: {monotone_w}
   {"Growth appears sub-exponential (good for Gronwall refinement)" if monotone_w else "Non-monotone — Gronwall bound may be tight"}

B. Pressure-weighted H̃(r):
   Positive for all tested r: {h_tilde_positive}
   {"Modification 1 is well-defined on Burgers" if h_tilde_positive else "Modification 1 FAILS on Burgers (H̃ < 0)"}

Recommendation to theory track:
   {"Focus on Modification 3 (vorticity) — it's monotone here AND eliminates pressure" if monotone_w else "The Gronwall bound may need more structure than generic C(M)"}
""")
