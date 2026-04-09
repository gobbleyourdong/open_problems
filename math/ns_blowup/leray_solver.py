"""
Leray-frame solver for axisymmetric NS (Hou-Li variables).

The Leray-rescaled equations are an AUTONOMOUS PDE:

  ∂U₁/∂τ = -(ξ/2 + Uʳ)·U₁,ξ - (ζ/2 + Uᶻ)·U₁,ζ + 2U₁·Ψ₁,ζ - U₁ + ν·Δξ·U₁
  ∂W₁/∂τ = -(ξ/2 + Uʳ)·W₁,ξ - (ζ/2 + Uᶻ)·W₁,ζ + 2U₁·U₁,ζ - (3/2)·W₁ + ν·Δξ·W₁

  where Uʳ = -ξ·Ψ₁,ζ,  Uᶻ = 2Ψ₁ + ξ·Ψ₁,ξ,  -Δξ·Ψ₁ = W₁

Compared to physical frame, only 3 changes:
  1. Radial advection velocity: Uʳ → Uʳ + ξ/2  (Leray drift)
  2. Axial advection velocity:  Uᶻ → Uᶻ + ζ/2  (Leray drift)
  3. Decay terms: -U₁ and -(3/2)·W₁  (Leray penalty)

Poisson, diffusion, stretching all have SAME structure as physical frame.
ν stays constant (does NOT blow up like in Euler self-similar scaling).
"""
import os
import sys
import math
import time
import torch
import numpy as np
import json

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver


class LeraySolver(SweepSolver):
    """
    Leray-frame NS solver.

    Inherits all infrastructure from SweepSolver (Chebyshev grid, Poisson,
    diffusion, RK4, CFL) and overrides compute_rhs() to add Leray terms.

    The grid (ξ, ζ) is the same as the physical (r, z) grid — we're treating
    the bounded domain [0,1] × [0, L/4] as the Leray-frame domain.
    BCs at ξ=1 become far-field decay (same numerical treatment as wall BC).
    """

    def __init__(self, Nr=64, Nz=128, L=1.0/6.0, nu=1e-4, device='cuda',
                 ic_type='luo_hou', amplitude=100.0):
        super().__init__(Nr=Nr, Nz=Nz, L=L, nu=nu, device=device,
                         ic_type=ic_type, amplitude=amplitude)

        # Precompute ξ and ζ grids for drift terms
        # In our convention: self.r = ξ (radial), self.Z = ζ (axial)
        self.xi_r = self.r  # shape (Nr+1,)
        self.xi_z = self.z  # shape (Nz+1,)

        # Expand for broadcasting: xi_r is (Nr+1, 1), xi_z is (1, Nz+1)
        self.xi_r_2d = self.xi_r.unsqueeze(1).expand(Nr+1, Nz+1)
        self.xi_z_2d = self.xi_z.unsqueeze(0).expand(Nr+1, Nz+1)

    def compute_rhs(self, u1, omega1):
        """
        Leray-frame RHS = physical RHS + drift + decay.

        Physical RHS (from parent):
          rhs_u1    = -uʳ·u₁,ξ - uᶻ·u₁,ζ + 2u₁·ψ₁,ζ + ν·Δu₁
          rhs_omega = -uʳ·ω₁,ξ - uᶻ·ω₁,ζ + 2u₁·u₁,ζ + ν·Δω₁

        We add:
          Leray drift: -(ξ/2)·∂f/∂ξ - (ζ/2)·∂f/∂ζ  for both u₁ and ω₁
          Leray decay: -u₁  and  -(3/2)·ω₁
        """
        # Get physical-frame RHS (includes viscosity if nu > 0)
        rhs_u1, rhs_omega1, u_r, u_z = super().compute_rhs(u1, omega1)

        # --- Leray drift terms ---
        # -(ξ/2)·∂U₁/∂ξ
        du1_dxi = self.D_r @ u1
        domega1_dxi = self.D_r @ omega1

        # -(ζ/2)·∂U₁/∂ζ
        du1_dzeta = self._ddz(u1)
        domega1_dzeta = self._ddz(omega1)

        drift_u1 = -0.5 * self.xi_r_2d * du1_dxi - 0.5 * self.xi_z_2d * du1_dzeta
        drift_w1 = -0.5 * self.xi_r_2d * domega1_dxi - 0.5 * self.xi_z_2d * domega1_dzeta

        # --- Leray decay terms ---
        decay_u1 = -1.0 * u1
        decay_w1 = -1.5 * omega1

        # Add to RHS
        rhs_u1 += drift_u1 + decay_u1
        rhs_omega1 += drift_w1 + decay_w1

        # Re-enforce BCs (drift/decay may have polluted boundaries)
        rhs_u1[0, :] = 0       # ξ=1 (far field): U₁ = 0
        rhs_omega1[-1, :] = 0  # ξ=0 (axis parity): W₁ smooth

        return rhs_u1, rhs_omega1, u_r, u_z


def run_leray_forward(Nr=64, Nz=128, nu=1e-4, n_steps=5000, device='cuda',
                      ic_type='luo_hou', amplitude=100.0):
    """
    Run the Leray solver forward from an IC.
    Track diagnostics: |W₁|_max, Γ, spectral ratio.
    """
    solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                         ic_type=ic_type, amplitude=amplitude)
    U1, W1 = solver.init_ic()
    tau, dt, step = 0.0, 1e-7, 0
    results = []
    t0 = time.time()

    print(f"LERAY SOLVER: Nr={Nr} Nz={Nz} nu={nu} ic={ic_type} A={amplitude}")
    print(f"Device: {device}, dtype: {U1.dtype}")

    for step in range(n_steps + 1):
        if step % 100 == 0:
            W1_max = W1.abs().max().item()
            U1_max = U1.abs().max().item()

            # Compute Γ (same formula as physical frame — stretching vs dissipation)
            psi1 = solver.solve_poisson(W1)
            dU1_dz = solver._ddz(U1)
            S = (W1 * 2.0 * U1 * dU1_dz).sum().item()
            dW1_dr = solver.D_r @ W1
            dW1_dz = solver._ddz(W1)
            P = (dW1_dr**2 + dW1_dz**2).sum().item()
            nuP = nu * P
            denom = abs(S) + abs(nuP) + 1e-30
            gamma_val = (S - nuP) / denom

            # Spectral check
            mid_z = W1.shape[1] // 2
            w_slice = W1[:, mid_z].cpu().numpy()
            coeffs = np.abs(np.fft.rfft(w_slice))
            n = len(coeffs)
            low = coeffs[:n//4].mean() + 1e-30
            high = coeffs[3*n//4:].mean()
            spec_ratio = high / low

            elapsed = time.time() - t0
            status = "OK" if spec_ratio < 0.01 else ("MARG" if spec_ratio < 0.1 else "UNDER")

            results.append({
                "step": step, "tau": tau, "gamma": gamma_val,
                "W1_max": W1_max, "U1_max": U1_max,
                "spectral": spec_ratio, "dt": dt,
            })

            if step % 500 == 0:
                print(f"step={step:5d} τ={tau:.4f} Γ={gamma_val:+.4f} "
                      f"|W₁|={W1_max:.2e} |U₁|={U1_max:.2e} "
                      f"spec={spec_ratio:.4f} [{status}] "
                      f"dt={dt:.2e} [{elapsed:.0f}s]", flush=True)

        # Blowup or decay check
        if W1.abs().max().item() > 1e8:
            print(f"BLOWUP at step={step}", flush=True)
            break
        if W1.abs().max().item() < 1e-15 and step > 100:
            print(f"DECAYED to zero at step={step}", flush=True)
            break

        U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
        tau += dt
        u_r_dummy = torch.zeros_like(U1)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

    elapsed = time.time() - t0
    print(f"\nDone. {step} steps in {elapsed:.0f}s")

    # Summary
    if results:
        gammas = [r["gamma"] for r in results if r["step"] > 0]
        W1_maxes = [r["W1_max"] for r in results if r["step"] > 0]
        if gammas:
            print(f"\nΓ range: [{min(gammas):.4f}, {max(gammas):.4f}]")
        if W1_maxes:
            trend = "GROWING" if W1_maxes[-1] > W1_maxes[0] * 1.1 else \
                    "DECAYING" if W1_maxes[-1] < W1_maxes[0] * 0.9 else "STABLE"
            print(f"|W₁| range: [{min(W1_maxes):.2e}, {max(W1_maxes):.2e}] — {trend}")
            if trend == "STABLE":
                print("  → Profile is approximately SELF-SIMILAR in Leray frame")
            elif trend == "DECAYING":
                print("  → Leray penalty wins — solution regularizes")
            else:
                print("  → Stretching beats Leray penalty — potential blowup!")

    return solver, U1, W1, results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--nu', type=float, default=1e-4)
    parser.add_argument('--steps', type=int, default=5000)
    parser.add_argument('--ic', type=str, default='luo_hou')
    parser.add_argument('--amp', type=float, default=100.0)
    parser.add_argument('--device', type=str, default='cuda')
    args = parser.parse_args()

    solver, U1, W1, results = run_leray_forward(
        Nr=args.nr, Nz=args.nz, nu=args.nu, n_steps=args.steps,
        device=args.device, ic_type=args.ic, amplitude=args.amp,
    )

    # Save results
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"leray_{args.ic}_nr{args.nr}.json")
    with open(out_path, "w") as f:
        json.dump(results, f)
    print(f"Saved to {out_path}")
