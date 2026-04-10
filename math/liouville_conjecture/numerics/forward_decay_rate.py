#!/usr/bin/env python3
"""
Forward Decay Rate — Does ||w(t)|| Decrease for Forward NS?

The gap: backward entry into the ε₀ ball. Equivalent question:
if we run NS FORWARD from large data, does ||w(t)|| eventually
drop below ε₀ = ν/(8C)?

For an ancient solution at time t₀, looking backward is the same as
looking at a forward solution that has been running since t₀ - T for
T → ∞. So forward decay at large time IS backward decay viewed
from the perspective of a later time.

This script:
1. Spectral 2D NS on torus (where Liouville holds) — measure decay rate
2. Compare to the ε₀ threshold
3. Estimate how long a bounded 3D flow needs to run to enter ε₀ ball
"""

import numpy as np


# ===========================================================
# 2D spectral NS on torus (forward)
# ===========================================================

def test_2d_forward_decay():
    """Run 2D NS forward and measure ||ω(t)||_∞ decay."""
    print("=" * 70)
    print("2D FORWARD NS — decay rate to zero")
    print("=" * 70)
    print()

    N = 64
    nu = 0.1
    dt = 0.001
    L = 2 * np.pi

    x = np.linspace(0, L, N, endpoint=False)
    dx = x[1] - x[0]
    kx = np.fft.fftfreq(N, d=dx) * 2 * np.pi
    KX, KY = np.meshgrid(kx, kx)
    K2 = KX**2 + KY**2
    K2_safe = K2.copy()
    K2_safe[0, 0] = 1

    # Initial condition: strong vortex
    X, Y = np.meshgrid(x, x)
    omega = 5.0 * np.sin(X) * np.cos(2*Y) + 3.0 * np.cos(3*X)
    initial_max = np.max(np.abs(omega))

    print(f"Grid: {N}×{N}, ν = {nu}, initial max|ω| = {initial_max:.4f}")
    print()
    print(f"{'t':>8} {'max|ω|':>12} {'max|ω|/initial':>16} {'< ε₀?':>8}")
    print("-" * 50)

    eps_0 = 0.443  # our estimate
    entered_ball = False
    entry_time = None

    for step in range(20001):
        if step % 1000 == 0:
            max_omega = np.max(np.abs(omega))
            ratio = max_omega / initial_max
            in_ball = "YES" if max_omega < eps_0 else "no"
            if max_omega < eps_0 and not entered_ball:
                entered_ball = True
                entry_time = step * dt
            print(f"{step*dt:8.2f} {max_omega:12.6f} {ratio:16.6f} {in_ball:>8}")

        # Spectral step (semi-implicit: diffusion implicit, advection explicit)
        omega_hat = np.fft.fft2(omega)

        # Velocity from stream function: ψ_hat = -ω_hat / K²
        psi_hat = -omega_hat / K2_safe
        psi_hat[0, 0] = 0

        # u = (∂ψ/∂y, -∂ψ/∂x)
        ux_hat = 1j * KY * psi_hat
        uy_hat = -1j * KX * psi_hat
        ux = np.real(np.fft.ifft2(ux_hat))
        uy = np.real(np.fft.ifft2(uy_hat))

        # ∂ω/∂x, ∂ω/∂y
        domega_dx = np.real(np.fft.ifft2(1j * KX * omega_hat))
        domega_dy = np.real(np.fft.ifft2(1j * KY * omega_hat))

        # Advection: u · ∇ω
        advection = ux * domega_dx + uy * domega_dy

        # Semi-implicit: new_omega_hat = (omega_hat - dt * adv_hat) / (1 + nu*K2*dt)
        adv_hat = np.fft.fft2(advection)
        omega_hat = (omega_hat - dt * adv_hat) / (1 + nu * K2 * dt)

        # Dealias (2/3 rule)
        mask = (np.abs(KX) < N//3 * kx[1]) & (np.abs(KY) < N//3 * kx[1])
        omega_hat *= mask

        omega = np.real(np.fft.ifft2(omega_hat))

    print()
    if entered_ball:
        print(f"ENTERED ε₀ ball at t ≈ {entry_time:.2f}")
    else:
        print(f"Did NOT enter ε₀ ball in {20000*dt:.1f} time units")
        print(f"Final max|ω| = {np.max(np.abs(omega)):.6f}, ε₀ = {eps_0:.4f}")

    print()
    print("2D NS: vorticity decays exponentially (no stretching).")
    print("The decay rate is set by the lowest active Fourier mode: ~ νk²_min.")
    print(f"For ν = {nu}, k_min = 1: decay rate ~ {nu:.2f}, half-life ~ {np.log(2)/nu:.2f}")
    return entered_ball, entry_time


# ===========================================================
# 3D decay estimate (analytical, from energy inequality)
# ===========================================================

def test_3d_decay_estimate():
    """Estimate the 3D decay time to enter the ε₀ ball."""
    print("=" * 70)
    print("3D DECAY ESTIMATE (energy inequality)")
    print("=" * 70)
    print()
    print("For 3D NS on R³ with initial data ||u₀||_∞ = M:")
    print("  The energy ||u(t)||₂² decays: d/dt ||u||₂² = -2ν||∇u||₂²")
    print("  By Poincaré (on bounded domain): ||∇u||₂² ≥ λ₁ ||u||₂²")
    print("  So ||u||₂² ≤ ||u₀||₂² · e^{-2νλ₁t}")
    print()
    print("On R³: no Poincaré inequality (λ₁ = 0). Energy can persist.")
    print("BUT: for BOUNDED solutions, Sobolev interpolation gives:")
    print("  ||u||_∞ ≤ C · ||u||₂^{1/2} · ||∇u||₂^{1/2} (Gagliardo-Nirenberg)")
    print("  So ||u||_∞ decays IF ||u||₂ and ||∇u||₂ both decay.")
    print()

    nu = 1.0
    eps_0 = nu / (8 * 2 / np.sqrt(np.pi))  # ν/(8·C_O)

    print(f"ε₀ = ν/(8·C_Oseen) = {eps_0:.4f}")
    print()
    print("For the ancient solution framework:")
    print("  An ancient solution at time 0 was the 'end state' of a flow")
    print("  that started at t = -T for T → ∞.")
    print("  If the flow decays, then at time 0 the solution has had")
    print("  infinite time to decay → should be in the ε₀ ball → Liouville.")
    print()
    print("THE SUBTLETY: on R³, decay is NOT guaranteed.")
    print("  Energy can spread to infinity (not decay, just diffuse).")
    print("  The sup-norm ||u(t)||_∞ might persist even as L² norm decays")
    print("  (the energy spreads spatially while maintaining amplitude).")
    print()
    print("This is EXACTLY the gap: the stretching term can MAINTAIN the")
    print("amplitude at small scales even as the large-scale energy diffuses.")
    print("An ancient solution on R³ has had infinite time to reach this")
    print("balance — the question is whether such balance is sustainable.")


# ===========================================================
# The key obstruction: R³ vs torus
# ===========================================================

def test_r3_vs_torus():
    """Why the decay works on torus but not (obviously) on R³."""
    print("=" * 70)
    print("R³ VS TORUS — why decay is harder on R³")
    print("=" * 70)
    print()
    print("On torus T³(L):")
    print("  Poincaré inequality: ||∇u||₂ ≥ (2π/L) · ||u||₂")
    print("  Energy decays: ||u||₂² ≤ ||u₀||₂² · e^{-2ν(2π/L)²t}")
    print("  Everything decays to zero exponentially → Liouville on torus EASY")
    print()
    print("On R³:")
    print("  NO Poincaré inequality (λ₁ = 0, continuous spectrum)")
    print("  Energy can persist: u(x,t) could maintain ||u||₂ = const")
    print("  The solution can 'run away' spatially without losing amplitude")
    print()

    L_values = [1, 10, 100, 1000]
    nu = 1.0
    eps_0 = 0.111  # ν/(8C)

    print("Decay times on T³(L) to reach ||u||_∞ < ε₀:")
    print(f"{'L':>8} {'λ₁ = (2π/L)²':>14} {'decay rate':>12} {'time to ε₀':>14}")
    print("-" * 55)

    M = 10.0  # initial ||u||_∞
    for L in L_values:
        lam1 = (2*np.pi/L)**2
        rate = 2*nu*lam1
        if rate > 0:
            t_eps = np.log(M / eps_0) / rate
        else:
            t_eps = float('inf')
        print(f"{L:8d} {lam1:14.6f} {rate:12.6f} {t_eps:14.4f}")

    print()
    print("As L → ∞ (approaching R³): decay time → ∞.")
    print("The 'time to enter ε₀ ball' diverges as L → ∞.")
    print("On R³ (L = ∞): no guaranteed entry time → the gap is real.")


# ===========================================================
# Main
# ===========================================================
if __name__ == "__main__":
    print("Liouville Conjecture — Numerical Track: Forward Decay Rate")
    print()

    entered, t_entry = test_2d_forward_decay()
    print()
    test_3d_decay_estimate()
    print()
    test_r3_vs_torus()

    print()
    print("=" * 70)
    print("SYNTHESIS")
    print("=" * 70)
    print(f"""
Forward decay tests:

2D torus (N=64, ν=0.1): {"entered ε₀ ball at t=" + f"{t_entry:.2f}" if entered else "decay ongoing, approaching ε₀"}
  Decay rate ~ νk²_min = ν·1 = 0.1 (exponential)

3D R³ (analytical): NO guaranteed decay time.
  The Poincaré inequality fails on R³ (λ₁ = 0).
  Energy can diffuse spatially without losing sup-norm amplitude.

Torus T³(L) as L → ∞: decay time diverges as L².
  This is consistent: R³ is the limit of large tori,
  and the decay time becomes infinite in the limit.

THE GAP (restated): on R³, the sup-norm of a bounded ancient solution
might NEVER enter the ε₀ ball because the energy has infinite space
to spread into. The stretching can maintain small-scale structure
while the large-scale energy diffuses to infinity.

The ancient condition (infinite backward time) should prevent this:
if the solution has been running "forever," it has already had infinite
time to spread — so it should have spread as far as it can.
But "as far as it can" on R³ is ∞, which doesn't force decay.

THIS IS WHY R³ MATTERS: on any bounded domain, Liouville is easy
(Poincaré inequality). The R³ case is special because energy has
infinite room to escape without decaying.
""")
