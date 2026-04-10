#!/usr/bin/env python3
"""
Almgren Frequency Function on NS Solutions — Priority 2

The Almgren frequency function:
  N(r) = r · D(r) / H(r)
where:
  D(r) = ∫_{B_r} |∇u|² dV  (Dirichlet integral on ball of radius r)
  H(r) = ∫_{∂B_r} |u|² dS  (L² norm on sphere of radius r)

For HARMONIC functions on R^n: N(r) is monotone non-decreasing (Almgren 1979).
This implies polynomial growth ⟹ Liouville for bounded harmonic functions.

For NS solutions: the nonlinear term (u · ∇)u and the pressure ∇p add
error terms to dN/dr. The question: is N(r) "almost monotone" in practice?

Mountain 1 in gap.md says: the NS error term is O(M · r² · D(r)) while
the good term is O(r · D'(r)). For large M the error dominates.

This script computes N(r) on the Burgers vortex (the richest explicit 3D
NS solution) and on simpler flows, to see the frequency function profile
and understand where monotonicity breaks.

NOTE: Burgers vortex is UNBOUNDED (u_z = αz), so N(r) will grow with r.
For bounded solutions, we'd expect N(r) to be bounded. The Burgers case
shows the STRUCTURE of N(r) without the boundedness constraint.
"""

import numpy as np
from scipy import integrate


# ===========================================================
# Burgers vortex velocity and gradients
# ===========================================================
# u_r = -αr/2, u_θ = Γ/(2πr)(1 - e^{-αr²/(2ν)}), u_z = αz
# In Cartesian (for gradient computation):
#   u_x = u_r cos θ - u_θ sin θ
#   u_y = u_r sin θ + u_θ cos θ
#   u_z = αz

def burgers_velocity_cyl(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """Burgers vortex in cylindrical (r, θ, z) — θ-independent."""
    u_r = -alpha * r / 2
    if r > 1e-10:
        u_theta = Gamma / (2 * np.pi * r) * (1 - np.exp(-alpha * r**2 / (2 * nu)))
    else:
        u_theta = Gamma * alpha / (4 * np.pi * nu) * r  # Taylor expansion at r=0
    u_z = alpha * z
    return u_r, u_theta, u_z


def burgers_speed_squared(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """Speed squared |u|² at (r, z)."""
    ur, ut, uz = burgers_velocity_cyl(r, z, alpha, Gamma, nu)
    return ur**2 + ut**2 + uz**2


def burgers_grad_squared(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    |∇u|² at (r, z) for Burgers vortex.
    Approximate by finite differences in r and z.
    """
    dr = 1e-4
    dz = 1e-4

    # Compute all 3 components at nearby points
    def u_vec(ri, zi):
        ur, ut, uz = burgers_velocity_cyl(ri, zi, alpha, Gamma, nu)
        return np.array([ur, ut, uz])

    u0 = u_vec(r, z)
    # ∂u/∂r, ∂u/∂z
    du_dr = (u_vec(r + dr, z) - u_vec(r - dr, z)) / (2 * dr)
    du_dz = (u_vec(r, z + dz) - u_vec(r, z - dz)) / (2 * dz)
    # ∂u/∂θ = 0 (axisymmetric), but there's a 1/r term from cylindrical coords
    # |∇u|² in cylindrical = |∂u/∂r|² + (1/r²)|∂u/∂θ - rotational terms|² + |∂u/∂z|²
    # For axisymmetric: simplifies, but let's just use the cartesian-like ||
    grad_sq = np.sum(du_dr**2) + np.sum(du_dz**2)
    # Add the 1/r² terms from u_theta/r contribution
    if r > 1e-10:
        ur, ut, uz = burgers_velocity_cyl(r, z, alpha, Gamma, nu)
        grad_sq += (ut / r)**2 + (ur / r)**2  # approximate extra cylindrical terms
    return grad_sq


# ===========================================================
# Frequency function computation
# ===========================================================

def dirichlet_integral(R_max, n_r=50, n_z=50, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    D(R) = ∫_{B_R} |∇u|² dV for Burgers vortex.
    Integrate in cylindrical coordinates over {r² + z² ≤ R²}.
    """
    total = 0.0
    # Use (r, z) grid inside the ball r² + z² ≤ R²
    for i in range(n_r):
        r = (i + 0.5) * R_max / n_r
        z_max_at_r = np.sqrt(max(R_max**2 - r**2, 0))
        if z_max_at_r < 1e-10:
            continue
        for j in range(n_z):
            z = -z_max_at_r + (j + 0.5) * 2 * z_max_at_r / n_z
            dz = 2 * z_max_at_r / n_z
            dr = R_max / n_r
            vol_element = 2 * np.pi * r * dr * dz  # cylindrical volume element
            grad2 = burgers_grad_squared(r, z, alpha, Gamma, nu)
            total += grad2 * vol_element
    return total


def sphere_l2_integral(R, n_theta=30, n_phi=20, alpha=1.0, Gamma=1.0, nu=1.0):
    """
    H(R) = ∫_{∂B_R} |u|² dS for Burgers vortex.
    Integrate over the sphere of radius R.
    """
    total = 0.0
    for i in range(n_theta):
        theta = (i + 0.5) * np.pi / n_theta
        for j in range(n_phi):
            phi = (j + 0.5) * 2 * np.pi / n_phi
            # Spherical to cylindrical
            r = R * np.sin(theta)
            z = R * np.cos(theta)
            d_omega = np.sin(theta) * (np.pi / n_theta) * (2 * np.pi / n_phi)
            u2 = burgers_speed_squared(r, z, alpha, Gamma, nu)
            total += u2 * R**2 * d_omega
    return total


def frequency_function(R, alpha=1.0, Gamma=1.0, nu=1.0):
    """N(R) = R · D(R) / H(R) for the Burgers vortex."""
    D = dirichlet_integral(R, alpha=alpha, Gamma=Gamma, nu=nu)
    H = sphere_l2_integral(R, alpha=alpha, Gamma=Gamma, nu=nu)
    if H < 1e-15:
        return float('nan')
    return R * D / H


def test_frequency_function():
    """Compute N(r) for the Burgers vortex at various radii."""
    print("=" * 70)
    print("FREQUENCY FUNCTION N(r) ON BURGERS VORTEX")
    print("=" * 70)
    print()
    print("N(r) = r · D(r) / H(r)")
    print("D(r) = ∫_{B_r} |∇u|², H(r) = ∫_{∂B_r} |u|²")
    print()
    print("For harmonic functions: N(r) is monotone non-decreasing (Almgren).")
    print("For NS: monotonicity is broken by nonlinear terms.")
    print()
    print(f"{'R':>6} {'D(R)':>12} {'H(R)':>12} {'N(R)':>10} {'monotone?':>10}")
    print("-" * 60)

    prev_N = None
    monotone = True
    radii = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
    for R in radii:
        D = dirichlet_integral(R, n_r=30, n_z=30)
        H = sphere_l2_integral(R, n_theta=20, n_phi=15)
        N = R * D / H if H > 1e-15 else float('nan')
        is_mono = "—"
        if prev_N is not None and not np.isnan(N) and not np.isnan(prev_N):
            if N >= prev_N - 1e-6:
                is_mono = "YES"
            else:
                is_mono = "NO"
                monotone = False
        print(f"{R:6.1f} {D:12.4f} {H:12.4f} {N:10.4f} {is_mono:>10}")
        prev_N = N

    print()
    print(f"N(r) monotone non-decreasing: {monotone}")
    print()
    if monotone:
        print("INTERESTING: N(r) appears monotone even for this NS solution!")
        print("(But Burgers is unbounded, so this doesn't prove Liouville.)")
    else:
        print("N(r) is NOT monotone — the NS nonlinearity breaks Almgren.")
    return monotone


# ===========================================================
# Comparison: frequency function on a harmonic function
# ===========================================================

def test_frequency_harmonic():
    """N(r) for a harmonic function (should be exactly monotone)."""
    print("=" * 70)
    print("COMPARISON: N(r) for harmonic function u(x) = x₁ (linear)")
    print("=" * 70)
    print()
    print("For u = x₁: |∇u|² = 1, |u|² = x₁² = r² sin²θ cos²φ")
    print("D(r) = vol(B_r) = 4πr³/3")
    print("H(r) = ∫ r² sin²θ cos²φ · r² dΩ = r⁴ · 4π/3")
    print("N(r) = r · (4πr³/3) / (r⁴ · 4π/3) = 1 (constant)")
    print()
    print("For a degree-k homogeneous harmonic polynomial: N(r) = k (constant).")
    print("This is the Almgren result: N(r) ≡ k for harmonic degree-k functions.")
    print()
    print("For BOUNDED harmonic functions on R³: N(r) ≤ 0 (degree 0 = constant)")
    print("⟹ u = const. This is the classical Liouville theorem.")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: Frequency Function")
    print()

    test_frequency_harmonic()
    print()
    monotone = test_frequency_function()

    print()
    print("=" * 70)
    print("WHAT THIS TELLS US")
    print("=" * 70)
    print("""
The frequency function N(r) = r · D(r) / H(r) is the tool from Mountain 1.
On harmonic functions: N(r) is constant (= degree of the polynomial).
On NS solutions: N(r) picks up error from (u·∇)u and ∇p.

For the BOUNDED Liouville case, we'd need:
  N(r) bounded ⟹ u has at most polynomial growth ⟹ bounded ⟹ u = const

But the NS nonlinearity means N(r) might not be monotone or bounded.
The frequency function approach needs either:
  (a) A modified N(r) that absorbs the nonlinear error, or
  (b) A separate argument that bounded ancient solutions have bounded N(r)

The Burgers vortex test shows the STRUCTURE of N(r) on a real 3D NS
solution. Even though Burgers is unbounded, the profile of N(r) reveals
how the nonlinear terms affect the frequency.
""")
