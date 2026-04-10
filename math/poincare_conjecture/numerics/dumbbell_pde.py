#!/usr/bin/env python3
"""
1D PDE Simulation of Ricci Flow on a Dumbbell Manifold

Setup: warped product g = dx² + φ(x,t)² g_S² on (a,b) × S²
This represents a 3-manifold of the form "S² fibered over an interval"
with the fiber radius φ(x) varying along the interval.

The Ricci flow ∂g/∂t = -2 Ric reduces to the 1D PDE:
  ∂φ/∂t = φ'' - (φ'² - 1)/φ

(see Angenent-Knopf for the derivation)

Initial data: dumbbell profile = two bumps connected by a thin neck.
We use φ(x,0) = neck_min + bulb_height * (sin(πx)² + cos(πx)²·decay)
or simply two Gaussians + a constant floor.

Expected behavior under Ricci flow:
- The neck (where φ is small) shrinks faster
- φ(neck) → 0 in finite time → singularity
- The bulbs stay bounded
- Type I marker: R(neck) × (T - t) → const

This is Perelman's Paper 2 scenario: the neck pinches and surgery
must be applied to continue the flow.
"""

import numpy as np


# ===========================================================
# Initial dumbbell profile
# ===========================================================

def dumbbell_initial(x, neck_min=0.3, bulb_height=1.0, bulb_width=1.0):
    """
    Initial dumbbell profile: two Gaussian bulbs connected by a thin neck.
    φ(x) = neck_min + bulb_height * [exp(-(x+L)²/w²) + exp(-(x-L)²/w²)]
    where the bulbs are centered at ±L.
    """
    L = 2.0  # half-distance between bulb centers
    w = bulb_width
    bulbs = np.exp(-(x + L)**2 / w**2) + np.exp(-(x - L)**2 / w**2)
    return neck_min + bulb_height * bulbs


# ===========================================================
# Ricci flow PDE step (semi-implicit / explicit)
# ===========================================================

def ricci_flow_step(phi, dx, dt):
    """
    Take one explicit timestep of ∂φ/∂t = φ'' - (φ'² - 1)/φ.

    Use central differences for φ' and φ''.
    Mirror boundary conditions at the edges (the dumbbell ends).
    """
    n = len(phi)
    phi_new = np.copy(phi)

    # Pad with mirror BCs
    phi_pad = np.empty(n + 2)
    phi_pad[1:-1] = phi
    phi_pad[0] = phi[1]
    phi_pad[-1] = phi[-2]

    # Central differences
    phi_x = (phi_pad[2:] - phi_pad[:-2]) / (2 * dx)
    phi_xx = (phi_pad[2:] - 2 * phi_pad[1:-1] + phi_pad[:-2]) / dx**2

    # Avoid division by zero at neck
    phi_safe = np.maximum(phi, 1e-6)

    # RHS of the PDE
    rhs = phi_xx - (phi_x**2 - 1) / phi_safe

    phi_new = phi + dt * rhs
    # Floor to prevent crash
    phi_new = np.maximum(phi_new, 1e-6)
    return phi_new


def neck_position_and_value(x, phi):
    """Find the position and value of the minimum of phi (the neck)."""
    idx = np.argmin(phi)
    return x[idx], phi[idx]


def scalar_curvature_approx(phi, phi_x, phi_xx):
    """
    Scalar curvature R for the warped product g = dx² + φ² g_S²:
      R = -4 φ''/φ + 2(1 - φ'²)/φ²
    """
    phi_safe = np.maximum(phi, 1e-6)
    R = -4 * phi_xx / phi_safe + 2 * (1 - phi_x**2) / phi_safe**2
    return R


# ===========================================================
# Run the simulation
# ===========================================================

def run_dumbbell_simulation():
    """Simulate Ricci flow on a dumbbell until neck pinch."""
    # Spatial grid
    L = 6.0
    n = 401
    x = np.linspace(-L, L, n)
    dx = x[1] - x[0]

    # Initial dumbbell profile
    phi = dumbbell_initial(x, neck_min=0.3, bulb_height=1.5, bulb_width=1.0)

    # Time stepping
    dt = 0.0005
    t = 0
    max_steps = 10000

    print("=" * 70)
    print("DUMBBELL RICCI FLOW SIMULATION")
    print("=" * 70)
    print(f"Grid: n={n}, dx={dx:.4f}, dt={dt}")
    print(f"Initial: neck_min={phi.min():.4f}, bulb_max={phi.max():.4f}")
    print()
    print(f"{'step':>6} {'t':>9} {'neck min':>11} {'bulb max':>11} "
          f"{'R_neck':>10} {'R(T-t)':>10}")
    print("-" * 70)

    # Find expected singularity time from initial neck
    # T_singular ≈ neck_radius² / 4 for a thin neck
    T_estimate = phi.min()**2 / 4
    print(f"# Estimated singularity time T ≈ neck²/4 = {T_estimate:.5f}")
    print()

    data = []
    for step in range(max_steps):
        phi_min = phi.min()
        if phi_min < 0.005:
            print(f"# Neck pinched at step {step}, t = {t:.5f}")
            break

        # Compute scalar curvature at neck
        idx_neck = np.argmin(phi)
        # Pad for derivatives at neck
        phi_pad = np.empty(n + 2)
        phi_pad[1:-1] = phi
        phi_pad[0] = phi[1]
        phi_pad[-1] = phi[-2]
        phi_x_neck = (phi_pad[idx_neck + 2] - phi_pad[idx_neck]) / (2 * dx)
        phi_xx_neck = (phi_pad[idx_neck + 2] - 2 * phi_pad[idx_neck + 1] + phi_pad[idx_neck]) / dx**2
        R_neck = -4 * phi_xx_neck / max(phi[idx_neck], 1e-6) + \
                 2 * (1 - phi_x_neck**2) / max(phi[idx_neck], 1e-6)**2

        if step % 200 == 0:
            T_current = T_estimate  # rough
            R_times_Tt = R_neck * max(T_current - t, 1e-9)
            print(f"{step:>6} {t:>9.5f} {phi_min:>11.6f} {phi.max():>11.6f} "
                  f"{R_neck:>10.2f} {R_times_Tt:>10.4f}")
            data.append((step, t, phi_min, phi.max(), R_neck))

        phi = ricci_flow_step(phi, dx, dt)
        t += dt

    print()
    print(f"Final: step={step}, t={t:.5f}, neck min={phi.min():.6f}")
    return x, phi, t, data


# ===========================================================
# Volume tracking
# ===========================================================

def volume_of_dumbbell(x, phi):
    """
    The volume of the warped product g = dx² + φ² g_S² is:
      vol = 4π ∫ φ²(x) dx  (since vol(S²) = 4π)
    """
    return 4 * np.pi * np.trapezoid(phi**2, x)


def neck_volume_fraction(x, phi, neck_threshold=0.1):
    """
    Fraction of volume in the "neck region" (where φ < threshold * max).
    """
    threshold = neck_threshold * phi.max()
    mask = phi < threshold
    if not np.any(mask):
        return 0.0
    neck_vol = 4 * np.pi * np.trapezoid((phi[mask])**2, x[mask])
    total_vol = volume_of_dumbbell(x, phi)
    return neck_vol / total_vol if total_vol > 0 else 0.0


def test_volume_evolution():
    """Track how volume changes during dumbbell flow."""
    print("=" * 70)
    print("VOLUME EVOLUTION TEST")
    print("=" * 70)

    L = 6.0
    n = 201
    x = np.linspace(-L, L, n)
    dx = x[1] - x[0]
    phi = dumbbell_initial(x, neck_min=0.3, bulb_height=1.5)

    dt = 0.001
    print(f"{'step':>6} {'t':>9} {'vol':>12} {'neck min':>11} {'neck %':>10}")
    print("-" * 60)

    for step in range(2001):
        if step % 200 == 0:
            v = volume_of_dumbbell(x, phi)
            nm = phi.min()
            nf = neck_volume_fraction(x, phi)
            print(f"{step:>6} {step*dt:>9.4f} {v:>12.4f} {nm:>11.6f} {nf*100:>10.4f}")

        if phi.min() < 0.005:
            print(f"# Neck pinched at t = {step*dt:.4f}")
            break

        phi = ricci_flow_step(phi, dx, dt)

    print()


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Poincaré Conjecture — Numerical Track: Dumbbell PDE Simulation")
    print()

    x, phi_final, t_final, data = run_dumbbell_simulation()

    print()
    test_volume_evolution()

    print()
    print("=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print("""
The 1D Ricci flow PDE on a warped product g = dx² + φ² g_S²:
  ∂φ/∂t = φ'' - (φ'² - 1)/φ

For dumbbell initial data (two bulbs + thin neck):
  - The neck region (small φ) shrinks fastest
  - φ_neck → 0 in finite time → curvature blows up
  - This is the TYPE I singularity Perelman handles via surgery

Surgery procedure (Perelman Paper 2):
  1. Detect neck (R > threshold or φ < threshold)
  2. Cut the manifold along a 2-sphere S² × {x_cut}
  3. Glue in two hemispherical caps
  4. Restart Ricci flow on the (now disconnected) pieces

Each surgery:
  - Reduces the manifold's topology (cuts a handle or disconnects)
  - Preserves κ-noncollapsing (Perelman's key theorem)
  - Preserves all the curvature bounds needed for long-time analysis

Finitely many surgeries are needed because:
  - Topology is finite (bounded by initial Betti numbers)
  - Each surgery strictly reduces complexity
  - Finite extinction time (Paper 3) for simply connected case
""")
