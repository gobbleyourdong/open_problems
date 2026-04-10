#!/usr/bin/env python3
"""
Known Ancient Solutions to 3D Navier-Stokes — Phase 1 Exploration

The Liouville conjecture says: every bounded ancient solution to NS on R³
is trivially u ≡ 0. Before attacking the conjecture, we compute all KNOWN
explicit (or semi-explicit) ancient/eternal solutions and verify they
satisfy Liouville (bounded ones are constant).

KNOWN ANCIENT/ETERNAL NS SOLUTIONS:

1. TRIVIAL: u ≡ 0 (the target of Liouville)
2. LAMB-OSEEN VORTEX: u_θ = Γ/(2πr) (1 - e^(-r²/(4νt)))
   - 2D, axisymmetric, ancient as t → -∞ (diffusing vortex)
   - UNBOUNDED at t → -∞ (vortex core concentrates)
   - Satisfies Liouville vacuously (not bounded)
3. BURGERS VORTEX: u_θ = Γ/(2πr) (1 - e^(-αr²/(2ν))), u_z = αz, u_r = -αr/2
   - 3D axisymmetric WITH strain
   - Eternal (steady state of vortex + strain)
   - UNBOUNDED (u_z = αz grows linearly)
   - Satisfies Liouville vacuously
4. OSEEN VORTEX (2D): similar to Lamb-Oseen
5. BELTRAMI FLOWS: curl u = λu (parallel velocity and vorticity)
   - Exact NS solutions: ∂u/∂t = -νλ²u (exponential decay)
   - Ancient if we take t → -∞: u grows exponentially backward!
   - UNBOUNDED ancient → satisfies Liouville vacuously
6. POISEUILLE/COUETTE: steady channel/pipe flows
   - Defined on domains with boundaries, not R³
   - Not relevant for the R³ Liouville problem
7. CONSTANT FLOW: u = c (constant vector)
   - Ancient, bounded, but ∇·u = 0 requires c arbitrary on R³
   - Liouville says this is the ONLY bounded ancient solution

OBSERVATION: Every known non-trivial ancient NS solution is UNBOUNDED.
No non-trivial BOUNDED ancient solution is known. This is strong
numerical evidence FOR the Liouville conjecture.

This script computes key quantities for each known solution.
"""

import numpy as np


# ===========================================================
# 1. Lamb-Oseen vortex (2D, embedded in 3D)
# ===========================================================
# u_θ(r, t) = Γ/(2πr) · (1 - exp(-r²/(4νt)))
# Only makes sense for t > 0; as t → 0⁺, approaches a point vortex.
# For ancient solutions, set t → -∞: the exponential exp(-r²/(4νt)) → ∞ for t < 0,
# so the solution BLOWS UP backward. NOT a bounded ancient solution.

def lamb_oseen_u_theta(r, t, Gamma=1.0, nu=1.0):
    """Azimuthal velocity of Lamb-Oseen vortex at radius r and time t > 0."""
    if t <= 0:
        return float('nan')  # Not defined for t ≤ 0
    return Gamma / (2 * np.pi * r) * (1 - np.exp(-r**2 / (4 * nu * t)))


def lamb_oseen_vorticity(r, t, Gamma=1.0, nu=1.0):
    """Vorticity ω_z of Lamb-Oseen vortex."""
    if t <= 0:
        return float('nan')
    return Gamma / (4 * np.pi * nu * t) * np.exp(-r**2 / (4 * nu * t))


def test_lamb_oseen():
    """Compute Lamb-Oseen and show it's unbounded as t → 0⁺."""
    print("=" * 70)
    print("1. LAMB-OSEEN VORTEX (2D)")
    print("=" * 70)
    print()
    print("u_θ(r,t) = Γ/(2πr) · (1 - e^(-r²/(4νt)))")
    print("Vorticity concentrates at r = 0 as t → 0⁺")
    print()
    print(f"{'t':>10} {'max |u_θ|':>12} {'max |ω|':>14} {'bounded?':>10}")
    print("-" * 55)

    r = np.linspace(0.01, 5, 200)
    for t in [10.0, 1.0, 0.1, 0.01, 0.001]:
        u = np.array([lamb_oseen_u_theta(ri, t) for ri in r])
        w = np.array([lamb_oseen_vorticity(ri, t) for ri in r])
        print(f"{t:10.4f} {np.max(np.abs(u)):12.4f} {np.max(np.abs(w)):14.4f} "
              f"{'YES' if np.max(np.abs(u)) < 100 else 'NO':>10}")

    print()
    print("As t → 0⁺: vorticity → δ(0), velocity → Γ/(2πr) (point vortex)")
    print("UNBOUNDED — NOT a bounded ancient solution.")
    print("Liouville is satisfied VACUOUSLY (hypothesis not met).")


# ===========================================================
# 2. Burgers vortex (3D, axisymmetric + axial strain)
# ===========================================================
# u_r = -αr/2, u_z = αz, u_θ = Γ/(2πr) · (1 - exp(-αr²/(2ν)))
# This is a STEADY (eternal) solution balancing strain and diffusion.
# UNBOUNDED: u_z = αz grows linearly in z.

def burgers_vortex(r, z, alpha=1.0, Gamma=1.0, nu=1.0):
    """Velocity field of Burgers vortex at (r, z)."""
    u_r = -alpha * r / 2
    u_z = alpha * z
    u_theta = Gamma / (2 * np.pi * r) * (1 - np.exp(-alpha * r**2 / (2 * nu)))
    return u_r, u_theta, u_z


def test_burgers_vortex():
    """Compute Burgers vortex and show it's unbounded."""
    print("=" * 70)
    print("2. BURGERS VORTEX (3D, steady)")
    print("=" * 70)
    print()
    print("u_r = -αr/2, u_θ = Γ/(2πr)(1-e^(-αr²/2ν)), u_z = αz")
    print()
    print(f"{'r':>6} {'z':>6} {'u_r':>10} {'u_θ':>10} {'u_z':>10} {'|u|':>10}")
    print("-" * 60)

    for r, z in [(0.5, 0), (1, 0), (2, 0), (1, 1), (1, 10), (1, 100)]:
        ur, ut, uz = burgers_vortex(r, z)
        mag = np.sqrt(ur**2 + ut**2 + uz**2)
        print(f"{r:6.1f} {z:6.1f} {ur:10.4f} {ut:10.4f} {uz:10.4f} {mag:10.4f}")

    print()
    print("|u| → ∞ as z → ∞ (because u_z = αz)")
    print("UNBOUNDED — NOT a bounded ancient solution.")
    print("Liouville satisfied vacuously.")


# ===========================================================
# 3. Beltrami flows (curl u = λu)
# ===========================================================
# If curl u = λu, then:
#   ∂u/∂t = νΔu - (u·∇)u - ∇p
# But for Beltrami: (u·∇)u = ½∇|u|² - u × (curl u) = ½∇|u|² - λ(u × u) = ½∇|u|²
# So ∇p = -½∇|u|², and ∂u/∂t = νΔu = -νλ²u.
# Solution: u(x,t) = e^(-νλ²t) u₀(x).
# Ancient (t → -∞): u grows as e^{νλ²|t|} → UNBOUNDED.

def test_beltrami():
    """Beltrami flow: exact but unbounded ancient."""
    print("=" * 70)
    print("3. BELTRAMI FLOWS (curl u = λu)")
    print("=" * 70)
    print()
    print("Solution: u(x,t) = e^(-νλ²t) u₀(x)")
    print("Forward: exponential decay (great!)")
    print("Ancient (t → -∞): exponential GROWTH (unbounded!)")
    print()

    nu = 1.0
    lam = 1.0
    u0_max = 1.0
    print(f"{'t':>10} {'|u|_max':>14} {'bounded?':>10}")
    print("-" * 40)
    for t in [0, -1, -5, -10, -20]:
        u_max = u0_max * np.exp(-nu * lam**2 * t)
        print(f"{t:10.1f} {u_max:14.4e} {'YES' if u_max < 100 else 'NO':>10}")

    print()
    print("At t = -20: |u|_max ≈ 4.9e+08 — vastly unbounded backward.")
    print("UNBOUNDED ancient — Liouville satisfied vacuously.")


# ===========================================================
# 4. The critical observation: ALL known ancient are unbounded
# ===========================================================

def critical_observation():
    """Summarize: every known non-trivial ancient NS solution is unbounded."""
    print("=" * 70)
    print("CRITICAL OBSERVATION")
    print("=" * 70)
    print()

    solutions = [
        ("u ≡ 0 (trivial)", "bounded", "ancient", "constant ✓"),
        ("u ≡ c (constant)", "bounded", "ancient", "constant ✓"),
        ("Lamb-Oseen vortex", "UNBOUNDED (t→0)", "NOT ancient", "vacuous"),
        ("Burgers vortex", "UNBOUNDED (z→∞)", "eternal", "vacuous"),
        ("Beltrami flow", "UNBOUNDED (t→-∞)", "ancient", "vacuous"),
        ("Arnold-Beltrami-Childress", "UNBOUNDED (t→-∞)", "ancient", "vacuous"),
        ("Poiseuille/Couette", "not on R³", "steady", "not applicable"),
    ]

    print(f"{'Solution':<30} {'Bounded?':<20} {'Ancient?':<15} {'Liouville':>12}")
    print("-" * 80)
    for name, bdd, anc, liou in solutions:
        print(f"{name:<30} {bdd:<20} {anc:<15} {liou:>12}")

    print()
    print("CONCLUSION: No known non-trivial BOUNDED ancient NS solution exists.")
    print("Every known ancient solution is either trivial (u = 0) or unbounded.")
    print()
    print("This is strong empirical evidence FOR the Liouville conjecture.")
    print("It's also the reason the conjecture is hard: we can't study bounded")
    print("ancient solutions because we can't find any (besides the trivial one).")


# ===========================================================
# 5. Key quantities for future comparison
# ===========================================================

def compute_key_quantities():
    """Compute the quantities gap.md says to track."""
    print("=" * 70)
    print("KEY QUANTITIES FOR THE GAP ANALYSIS")
    print("=" * 70)
    print()
    print("For each ancient/eternal solution, compute:")
    print()

    # Burgers vortex (the richest 3D example)
    print("--- BURGERS VORTEX (α = 1, Γ = 1, ν = 1) ---")
    r_grid = np.linspace(0.1, 5, 50)

    # Vortex stretching: |ω · ∇u| at z = 0 (where the stretching is cleanest)
    # For Burgers: ω = ω_z ê_z, ∇u has component ∂u_z/∂z = α in the z direction
    # So ω · ∇u = α · ω_z ê_z in the z direction
    alpha = 1.0
    Gamma = 1.0
    nu = 1.0
    omega_z = Gamma / (4 * np.pi * nu / alpha) * np.exp(-alpha * r_grid**2 / (2 * nu))
    stretching = alpha * omega_z  # ω · ∇u (z-component)
    diffusion = np.gradient(np.gradient(omega_z, r_grid), r_grid) + \
                np.gradient(omega_z, r_grid) / r_grid  # approximate Δω_z

    # Stretching/diffusion ratio
    ratio = np.abs(stretching) / (np.abs(diffusion) + 1e-12)

    print(f"  Max |vortex stretching|: {np.max(np.abs(stretching)):.6f}")
    print(f"  Max |diffusion Δω|:      {np.max(np.abs(diffusion)):.6f}")
    print(f"  Max stretching/diffusion ratio: {np.max(ratio):.4f}")
    print()

    # Frequency function N(r) = r · ∫_{B_r} |∇u|² / ∫_{∂B_r} |u|²
    # This is hard to compute for Burgers; approximate
    print("  Frequency function: requires integration (see attempt_001)")
    print()

    # Dirichlet integral growth
    # ∫_{B_R} |∇u|² for Burgers vortex: diverges (because u_z = αz)
    print("  Dirichlet integral: DIVERGES (u_z = αz, so |∇u|² ~ α²)")
    print("  This confirms: Burgers is unbounded → Galdi's Liouville")
    print("  (finite Dirichlet integral → constant) is consistent.")
    print()

    # Pressure
    # For Burgers: p = -α²(r²/4 + z²/2) + ... (from the strain field)
    print("  Pressure: p = -α²(r²/4 + z²/2) + centrifugal term")
    print("  ∇p is unbounded (∝ r, z) — consistent with bounded u ↛ bounded ∇p")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: Known Ancient Solutions")
    print("Phase 1 Exploration")
    print()

    test_lamb_oseen()
    print()
    test_burgers_vortex()
    print()
    test_beltrami()
    print()
    critical_observation()
    print()
    compute_key_quantities()

    print()
    print("=" * 70)
    print("PHASE 1 VERDICT")
    print("=" * 70)
    print("""
Every known non-trivial ancient NS solution is UNBOUNDED.
No bounded non-constant ancient solution has ever been found.

This means:
1. Liouville has no known counterexample (strong evidence FOR)
2. We cannot study the object we're trying to prove doesn't exist
3. Any numerical attack must work INDIRECTLY — via monotone
   quantities, inequalities, and contradictions

The Poincaré parallel: Perelman didn't find ancient Ricci flows
by construction either. He proved they must be solitons via five
monotone invariants. The Liouville problem needs the NS analog:
a monotone invariant that detects u ≡ 0 as the unique bounded
ancient solution.

NEXT: frequency function exploration (attempt_001 in theory track,
frequency_function.py in numerical track).
""")
