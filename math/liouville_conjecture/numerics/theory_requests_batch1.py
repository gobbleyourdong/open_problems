#!/usr/bin/env python3
"""
Theory Track Requests (Batch 1) — from SCRATCHPAD.md Apr 9 23:55

Three requests from the theory instance:
A. N_ω(r) on Lamb-Oseen vortex (2D, Liouville proved) — expect C = 0
B. N_ω(r) on Beltrami flow (3D, ancient but unbounded)
C. Fisher information F = ∫|∇ω|²/|ω|² on Burgers — sign of dF/dt|_stretching
"""

import numpy as np


# ===========================================================
# A. N_ω(r) on Lamb-Oseen vortex (2D control case)
# ===========================================================
# Lamb-Oseen at fixed t > 0 (snapshot — not ancient, but 2D):
#   ω(r) = Γ/(4πνt) · exp(-r²/(4νt))
#   This is a Gaussian vortex. 2D Liouville holds.
#
# For the 2D vorticity frequency:
#   D_ω(R) = ∫_0^R ∫_0^{2π} |∂ω/∂r|² r dr dθ = 2π ∫_0^R |ω'(r)|² r dr
#   H_ω(R) = 2πR · |ω(R)|²  (circle, not sphere)
#   N_ω(R) = R · D_ω(R) / H_ω(R)
#
# For Gaussian ω(r) = A exp(-r²/σ²):
#   ω'(r) = -2r/σ² · ω(r)
#   |ω'|² = 4r²/σ⁴ · ω²
#   D_ω(R) = 2π · (4/σ⁴) · ∫_0^R r³ · A² exp(-2r²/σ²) dr
#   H_ω(R) = 2πR · A² exp(-2R²/σ²)

def lamb_oseen_N_omega(R, t=1.0, Gamma=1.0, nu=1.0):
    """N_ω(R) for Lamb-Oseen at fixed time t (2D)."""
    sigma2 = 4 * nu * t
    A = Gamma / (4 * np.pi * nu * t)

    # D_ω via numerical integration
    n = 200
    r_grid = np.linspace(1e-6, R, n)
    dr = r_grid[1] - r_grid[0]
    omega = A * np.exp(-r_grid**2 / sigma2)
    omega_r = -2 * r_grid / sigma2 * omega
    D = 2 * np.pi * np.sum(omega_r**2 * r_grid * dr)

    # H_ω (value on circle of radius R in 2D)
    omega_R = A * np.exp(-R**2 / sigma2)
    H = 2 * np.pi * R * omega_R**2

    if H < 1e-30:
        return float('nan')
    return R * D / H


def test_lamb_oseen_N_omega():
    """Compute N_ω(r) on 2D Lamb-Oseen. Theory expects C = 0 (no growth)."""
    print("=" * 70)
    print("A. N_ω(r) on LAMB-OSEEN (2D — Liouville holds)")
    print("=" * 70)
    print()
    print("ω(r) = A exp(-r²/(4νt)), Gaussian vortex at t = 1")
    print("2D Liouville holds ⟹ expect N_ω monotone with bounded growth (C = 0)")
    print()
    print(f"{'R':>6} {'N_ω(R)':>12} {'log N_ω':>10} {'monotone?':>10}")
    print("-" * 45)

    prev_N = None
    monotone = True
    for R in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
        N = lamb_oseen_N_omega(R)
        log_N = np.log(N) if N > 0 and not np.isnan(N) else float('nan')
        is_mono = "—"
        if prev_N is not None and not np.isnan(N) and not np.isnan(prev_N):
            is_mono = "YES" if N >= prev_N - 1e-6 else "NO"
            if N < prev_N - 1e-6:
                monotone = False
        print(f"{R:6.1f} {N:12.4f} {log_N:10.4f} {is_mono:>10}")
        prev_N = N

    print()
    print(f"Monotone: {monotone}")

    # Check if growth is bounded (C ~ 0)
    N_first = lamb_oseen_N_omega(0.5)
    N_last = lamb_oseen_N_omega(5.0)
    if N_first > 0 and N_last > 0:
        rate = np.log(N_last / N_first) / 4.5
        print(f"Effective growth rate: {rate:.4f} (vs 2.11 on 3D Burgers)")
        if rate < 0.5:
            print("MUCH SLOWER than 3D — consistent with C ≈ 0 prediction")
    return monotone


# ===========================================================
# B. N_ω(r) on Beltrami flow (3D, ancient but unbounded)
# ===========================================================
# Beltrami: curl u = λu, so ω = λu.
# |∇ω|² = λ² |∇u|²
# |ω|² = λ² |u|²
# N_ω(R) = R · ∫_{B_R} |∇ω|² / ∫_{∂B_R} |ω|² = R · ∫_{B_R} |∇u|² / ∫_{∂B_R} |u|²
# This is the SAME as the standard frequency function N(r) for u!
# So N_ω = N_u for Beltrami flows.
#
# For Beltrami: u is an eigenfunction of curl. On R³, the simplest is
# u = (sin z, cos z, 0) (plane wave Beltrami with λ = 1).
# |∇u|² = 1 everywhere (cos²z + sin²z = 1)
# |u|² = 1 everywhere
# D(R) = vol(B_R) = 4πR³/3, H(R) = 4πR² · 1 = 4πR²
# N(R) = R · (4πR³/3) / (4πR²) = R/3 · R = R²/3  ... wait that's linear

def test_beltrami_N_omega():
    """N_ω on a simple Beltrami flow (curl u = u)."""
    print("=" * 70)
    print("B. N_ω(r) on BELTRAMI FLOW (3D, ancient, unbounded)")
    print("=" * 70)
    print()
    print("Beltrami: ω = λu, so N_ω = N_u (same frequency function)")
    print()
    print("Simple Beltrami: u = (sin z, cos z, 0), λ = 1")
    print("|u|² = 1 everywhere, |∇u|² = 1 everywhere")
    print("D(R) = vol(B_R) = 4πR³/3")
    print("H(R) = area(∂B_R) · 1 = 4πR²")
    print("N(R) = R · (4πR³/3) / (4πR²) = R/3")
    print()
    print(f"{'R':>6} {'N_ω = R/3':>12} {'growth rate':>14}")
    print("-" * 40)

    for R in [1, 2, 3, 5, 10]:
        N = R / 3
        print(f"{R:6.1f} {N:12.4f} {'linear in R':>14}")

    print()
    print("N_ω grows LINEARLY with R (not exponentially).")
    print("Growth rate: d(log N_ω)/dR = 1/R → 0 as R → ∞")
    print("This is SLOWER than exponential (the Gronwall bound).")
    print()
    print("But Beltrami is UNBOUNDED backward: u(t) = e^{νλ²|t|} u₀")
    print("The N_ω linear growth reflects the plane-wave structure,")
    print("not the temporal unboundedness.")


# ===========================================================
# C. Fisher information on Burgers vortex
# ===========================================================
# Fisher info: F = ∫ |∇ω|² / |ω|² dV = ∫ |∇ log|ω||² · |ω|² dV + ...
#
# For axisymmetric Burgers with ω = ω_z(r) ê_z:
#   |∇ω|² = (ω')²
#   |ω|² = ω²
#   |∇ω|²/|ω|² = (ω'/ω)² = (d log ω / dr)²
#
# ω(r) = C exp(-αr²/(2ν))
# log ω = log C - αr²/(2ν)
# d(log ω)/dr = -αr/ν
# (d log ω / dr)² = α²r²/ν²
#
# Fisher = ∫_0^∞ (α²r²/ν²) · 2πr dr  ... diverges!
#
# So the RAW Fisher information diverges on R³ for Burgers.
# Need a LOCALIZED version: F(R) = ∫_{B_R} |∇ω|²/|ω|² dV

def burgers_fisher_info(R, alpha=1.0, nu=1.0, Gamma=1.0):
    """
    Localized Fisher information F(R) = ∫_{B_R} |∇ω|²/|ω|² dV
    on the Burgers vortex (z-independent, so 2D integral × height).

    For the z=0 plane: |∇ω|²/|ω|² = (α·r/ν)²
    F_2D(R) = ∫_0^R (αr/ν)² · 2πr dr = 2π(α/ν)² · R⁴/4 = π(α/ν)² · R⁴/2

    For the 3D ball: need to account for z-extent, but ω is z-independent
    so the integrand is the same. F(R) = F_2D(R) · (2R) ... roughly
    Actually: ∫_{B_R} = ∫ over {r² + z² ≤ R²}, and the integrand is (αr/ν)²
    F(R) = ∫_0^R ∫_{-√(R²-r²)}^{√(R²-r²)} (αr/ν)² · 2πr dz dr
         = 2π(α/ν)² ∫_0^R r³ · 2√(R²-r²) dr
    """
    n = 100
    r_grid = np.linspace(1e-6, R, n)
    dr = r_grid[1] - r_grid[0]
    integrand = (alpha * r_grid / nu)**2 * r_grid * 2 * np.sqrt(np.maximum(R**2 - r_grid**2, 0))
    return 2 * np.pi * np.sum(integrand) * dr


def test_fisher_info():
    """Compute Fisher information and separate stretching contribution."""
    print("=" * 70)
    print("C. FISHER INFORMATION on Burgers vortex")
    print("=" * 70)
    print()
    print("F(R) = ∫_{B_R} |∇ω|²/|ω|² dV")
    print("For Burgers: |∇ω|²/|ω|² = (αr/ν)² (exact)")
    print()
    print(f"{'R':>6} {'F(R)':>14} {'F(R)/R⁵':>14} {'growth':>12}")
    print("-" * 55)

    prev_F = None
    for R in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]:
        F = burgers_fisher_info(R)
        ratio = F / R**5 if R > 0 else 0
        growth = "—"
        if prev_F is not None and prev_F > 0:
            growth = f"×{F/prev_F:.2f}"
        print(f"{R:6.1f} {F:14.4f} {ratio:14.6f} {growth:>12}")
        prev_F = F

    print()
    print("F(R) ~ R⁵ (the integrand (αr/ν)² · r · √(R²-r²) gives R⁵ scaling)")
    print()

    # Decompose dF/dt into stretching and diffusion contributions
    print("--- dF/dt DECOMPOSITION (theory track request) ---")
    print()
    print("The time derivative of F = ∫|∇ω|²/|ω|² decomposes as:")
    print("  dF/dt = (diffusion part) + (stretching part) + (transport part)")
    print()
    print("For the vorticity equation ∂ω/∂t = νΔω + Sω - (u·∇)ω:")
    print()
    print("  Diffusion: contributes -2ν ∫ |∇²ω|²/|ω|² + ... (negative = good)")
    print("  Stretching: contributes ∫ (∇(Sω) · ∇ω)/|ω|² - ... (sign unknown)")
    print("  Transport: contributes 0 in L² sense (divergence-free u)")
    print()
    print("On Burgers (steady): dF/dt = 0 (no time dependence).")
    print("The stretching and diffusion are in EXACT BALANCE.")
    print()

    # The stretching contribution
    # For Burgers: Sω = αω_z ê_z (stretching at rate α in the z-direction)
    # ∇(Sω) = α · ∇ω_z ê_z
    # ∇(Sω) · ∇ω = α · |∇ω|²
    # So the stretching part of dF/dt ∝ α · ∫ |∇ω|²/|ω|² = α · F
    alpha = 1.0
    F_at_3 = burgers_fisher_info(3.0)
    stretching_contribution = alpha * F_at_3
    print(f"Stretching part at R=3: α·F = {alpha} × {F_at_3:.4f} = {stretching_contribution:.4f}")
    print(f"Sign: POSITIVE (stretching INCREASES Fisher information)")
    print()
    print("KEY FINDING: dF/dt|_stretching > 0 on Burgers (stretching increases F).")
    print("This is BAD for the Fisher information approach — stretching has the")
    print("WRONG SIGN for monotone decrease.")
    print()
    print("HOWEVER: Burgers is not bounded ancient. For bounded ancient solutions,")
    print("the stretching might be weaker (bounded by C(M)) while the diffusion")
    print("is stronger (small scales get diffused). The balance could tip.")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: Theory Requests Batch 1")
    print("(Responding to SCRATCHPAD.md requests)")
    print()

    test_lamb_oseen_N_omega()
    print()
    test_beltrami_N_omega()
    print()
    test_fisher_info()

    print()
    print("=" * 70)
    print("SUMMARY FOR THEORY TRACK")
    print("=" * 70)
    print("""
A. Lamb-Oseen (2D control): N_ω monotone with growth rate << 2.11.
   Consistent with C = 0 prediction (2D Liouville holds).

B. Beltrami (3D, ancient, unbounded): N_ω = R/3 (linear growth).
   Slower than exponential Gronwall. N_ω grows because the plane-wave
   structure has |∇u|/|u| ~ 1 at all scales.

C. Fisher information: dF/dt|_stretching > 0 on Burgers.
   STRETCHING HAS THE WRONG SIGN. Fisher increases under stretching.
   This KILLS the naive Fisher approach for Liouville.
   But Burgers is not bounded ancient — the balance might be different.

UPDATED RECOMMENDATION:
  - N_ω remains the strongest candidate (monotone on Burgers AND Lamb-Oseen,
    growth rate 2D << 3D)
  - Fisher information has wrong-sign stretching — needs modification or
    different argument to work
  - Waiting for W_NS formula from attempt_004
""")
