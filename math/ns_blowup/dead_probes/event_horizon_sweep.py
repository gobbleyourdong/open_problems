"""
Event Horizon Sweep — drop near-singular states into NS and see if viscosity dissolves them.

Place a sharp, high-amplitude vortex blob at r=0.10 (peak Biot-Savart sensitivity).
Sweep amplitude A and width σ. For each (A, σ):
  - Initialize with the blob
  - Run 2000 steps
  - Measure: does Γ stay high (blowup) or crash (regularized)?

The critical boundary A_c(σ) separates "viscosity wins" from "blowup wins."
Below this boundary → regularity. Above → blowup.

If A_c doesn't exist (blowup for ALL A at small enough σ) → viscosity can never win.
"""
import sys, os, math, time, json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver

dev = "cuda"
Nr, Nz = 64, 128
nu = 1e-4
L = 1.0 / 6.0
r_target = 0.10

# Sweep parameters
amplitudes = [1000, 5000, 10000]
sigmas = [0.05, 0.03]
n_steps = 2000  # quick screening

results = []
t_total = time.time()

for A in amplitudes:
    for sigma in sigmas:
        print(f"\n--- A={A}, σ={sigma} ---")
        t0 = time.time()

        # Build solver with custom IC via sniper type
        solver = SweepSolver(Nr=Nr, Nz=Nz, L=L, nu=nu, device=dev,
                             ic_type='luo_hou', amplitude=A)  # dummy IC type

        # Override with our custom IC
        r = solver.r
        R, Z = solver.R, solver.Z
        u1 = A * torch.exp(-((R - r_target)**2) / sigma**2) * \
             (1 - R**2) * torch.sin(2 * math.pi * Z / L)
        omega1 = torch.zeros_like(u1)
        u1[0, :] = 0  # wall BC

        t_sim, dt, step = 0.0, 1e-7, 0
        gamma_min = 1.0
        gamma_final = 0.0
        omega_max = 0.0
        omega_history = []
        gamma_history = []
        blowup_step = -1
        spectral_at_gamma_min = 0.0

        for step in range(n_steps):
            if step % 200 == 0:
                psi1 = solver.solve_poisson(omega1)
                du1_dz = solver._ddz(u1)
                S = (omega1 * 2.0 * u1 * du1_dz).sum().item()
                domega1_dr = solver.D_r @ omega1
                domega1_dz = solver._ddz(omega1)
                P = (domega1_dr**2 + domega1_dz**2).sum().item()
                nuP = nu * P
                denom = abs(S) + abs(nuP) + 1e-30
                gamma_val = (S - nuP) / denom

                mid_z = omega1.shape[1] // 2
                omega_slice = omega1[:, mid_z].cpu().numpy()
                coeffs = np.abs(np.fft.rfft(omega_slice))
                n = len(coeffs)
                low = coeffs[:n//4].mean() + 1e-30
                high = coeffs[3*n//4:].mean()
                spec_ratio = high / low

                om1 = omega1.abs().max().item()
                omega_history.append(om1)
                gamma_history.append(gamma_val)

                if gamma_val < gamma_min:
                    gamma_min = gamma_val
                    spectral_at_gamma_min = spec_ratio
                gamma_final = gamma_val
                omega_max = max(omega_max, om1)

                if step % 1000 == 0:
                    status = "OK" if spec_ratio < 0.01 else ("MARG" if spec_ratio < 0.1 else "UNDER")
                    print(f"  step={step:5d} G={gamma_val:+.4f} spec={spec_ratio:.4f} [{status}] "
                          f"|w|={om1:.2e}", flush=True)

            if omega1.abs().max().item() > 1e8:
                blowup_step = step
                break

            u1, omega1, _, _ = solver.step_rk4(u1, omega1, dt)
            t_sim += dt
            u_r_dummy = torch.zeros_like(u1)
            dt = solver.compute_dt(u_r_dummy, u_r_dummy, omega1, dt)

        elapsed = time.time() - t0

        # Classify outcome
        if blowup_step > 0:
            outcome = "BLOWUP"
        elif gamma_min < 0:
            outcome = "REGULARIZED"
        elif gamma_min < 0.05:
            outcome = "NEAR_BALANCE"
        elif gamma_min > 0.3:
            outcome = "STRONG_BLOWUP"
        else:
            outcome = "CONTESTED"

        # Check if omega was growing at the end
        if len(omega_history) > 3:
            omega_trend = omega_history[-1] / (omega_history[-3] + 1e-30)
        else:
            omega_trend = 0

        entry = {
            "A": A, "sigma": sigma,
            "gamma_min": gamma_min,
            "gamma_final": gamma_final,
            "omega_max": omega_max,
            "omega_trend": omega_trend,
            "spectral_at_min": spectral_at_gamma_min,
            "blowup_step": blowup_step,
            "outcome": outcome,
            "elapsed": elapsed,
        }
        results.append(entry)

        print(f"  RESULT: {outcome} | Γ_min={gamma_min:.4f} | |ω|_max={omega_max:.2e} | "
              f"spec@min={spectral_at_gamma_min:.4f} | {elapsed:.0f}s")

# Summary table
print(f"\n{'='*80}")
print(f"EVENT HORIZON SWEEP RESULTS")
print(f"{'='*80}")
print(f"{'A':>8} {'σ':>6} {'Γ_min':>8} {'Γ_final':>8} {'|ω|_max':>10} {'spec@min':>9} {'outcome':>15}")
print(f"{'-'*80}")
for r in results:
    print(f"{r['A']:8d} {r['sigma']:6.2f} {r['gamma_min']:8.4f} {r['gamma_final']:8.4f} "
          f"{r['omega_max']:10.2e} {r['spectral_at_min']:9.4f} {r['outcome']:>15}")

# Find the critical boundary
print(f"\n--- CRITICAL BOUNDARY ---")
for sigma in sigmas:
    sigma_results = [r for r in results if r['sigma'] == sigma]
    strong = [r for r in sigma_results if r['gamma_min'] > 0.2]
    weak = [r for r in sigma_results if r['gamma_min'] < 0.1]
    if strong and weak:
        A_low = max(r['A'] for r in weak)
        A_high = min(r['A'] for r in strong)
        print(f"  σ={sigma:.2f}: A_c ∈ ({A_low}, {A_high})")
    elif strong:
        print(f"  σ={sigma:.2f}: ALL strong blowup (Γ_min > 0.2)")
    elif weak:
        print(f"  σ={sigma:.2f}: ALL regularized (Γ_min < 0.1)")
    else:
        print(f"  σ={sigma:.2f}: mixed")

total = time.time() - t_total
print(f"\nTotal time: {total:.0f}s")

with open(os.path.join(os.path.dirname(__file__), "results", "event_horizon_sweep.json"), "w") as f:
    json.dump(results, f, indent=2)
print("Saved to ns_blowup/results/event_horizon_sweep.json")
