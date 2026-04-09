"""
Core Width vs Strain Rate Diagnostic — The "Rigged Baseplate" Test

Tests Gemini's prediction: when viscosity spreads the vortex core (R increases),
the Poisson coupling converts wider core into stronger strain (α increases),
which always overpowers dissipation → Γ must rebound.

If α spikes precisely when R is maximum → the Lego mechanism is confirmed.

Nr=64 on Spark, fast prototype. Full version on H200 at Nr=256 later.
"""
import sys, os, torch, time, json, numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver

dev = "cuda"
Nr, Nz = 64, 128
nu = 1e-4

solver = SweepSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu, device=dev,
                     ic_type="luo_hou", amplitude=100.0)
u1, omega1 = solver.init_ic()
t, dt, step = 0.0, 1e-7, 0
results = []
t0 = time.time()

r = solver.r  # Chebyshev points in r, index 0=wall(r=1), Nr=axis(r=0)

for step in range(15000):
    if step % 100 == 0:
        psi1 = solver.solve_poisson(omega1)

        # --- Standard Γ diagnostic ---
        du1_dz = solver._ddz(u1)
        S = (omega1 * 2.0 * u1 * du1_dz).sum().item()
        domega1_dr = solver.D_r @ omega1
        domega1_dz = solver._ddz(omega1)
        P = (domega1_dr**2 + domega1_dz**2).sum().item()
        nuP = nu * P
        denom = abs(S) + abs(nuP) + 1e-30
        gamma_val = (S - nuP) / denom

        # --- Core width R(t): RMS radius of |ω₁| ---
        # Weight by |ω₁| to find where vorticity lives
        omega_abs = omega1.abs()
        total_weight = omega_abs.sum().item() + 1e-30
        # r is shape [Nr+1], broadcast over z
        r_expanded = r.unsqueeze(1).expand_as(omega1)
        R_mean = (r_expanded * omega_abs).sum().item() / total_weight
        R_rms = ((r_expanded**2 * omega_abs).sum().item() / total_weight) ** 0.5

        # --- Core width: half-max radius (more robust) ---
        # Find r where |ω₁| drops to half its max, averaged over z
        omega_z_avg = omega_abs.mean(dim=1)  # average over z → shape [Nr+1]
        omega_max_val = omega_z_avg.max().item()
        if omega_max_val > 1e-10:
            half_max = omega_max_val / 2.0
            # Find first crossing from wall side (index 0 = r=1)
            above = (omega_z_avg > half_max).float()
            # Width = fraction of r domain where |ω₁| > half_max
            R_half = above.mean().item()
        else:
            R_half = 0.0

        # --- Strain rate α(t): max |ψ₁,z| (drives stretching term 2u₁ψ₁,z) ---
        dpsi1_dz = solver._ddz(psi1)
        alpha_max = dpsi1_dz.abs().max().item()

        # --- Strain rate at vorticity peak (more targeted) ---
        # Where is |ω₁| maximum?
        flat_idx = omega_abs.argmax().item()
        peak_r_idx = flat_idx // omega1.shape[1]
        peak_z_idx = flat_idx % omega1.shape[1]
        alpha_at_peak = dpsi1_dz[peak_r_idx, peak_z_idx].abs().item()

        # --- Stretching alignment: u₁ · ψ₁,z at peak ---
        stretch_at_peak = (u1[peak_r_idx, peak_z_idx] *
                          dpsi1_dz[peak_r_idx, peak_z_idx]).item()

        # --- Spectral check ---
        mid_z = omega1.shape[1] // 2
        omega_slice = omega1[:, mid_z].cpu().numpy()
        coeffs = np.abs(np.fft.rfft(omega_slice))
        n = len(coeffs)
        low = coeffs[:n//4].mean() + 1e-30
        high = coeffs[3*n//4:].mean()
        spec_ratio = high / low

        om1 = omega1.abs().max().item()
        elapsed = time.time() - t0

        entry = {
            "step": step, "t": t,
            "gamma": gamma_val,
            "R_rms": R_rms,
            "R_half": R_half,
            "alpha_max": alpha_max,
            "alpha_at_peak": alpha_at_peak,
            "stretch_at_peak": stretch_at_peak,
            "S": S, "nuP": nuP,
            "spectral": spec_ratio,
            "om1": om1,
            "peak_r": r[peak_r_idx].item(),
        }
        results.append(entry)

        status = "OK" if spec_ratio < 0.01 else ("MARG" if spec_ratio < 0.1 else "UNDER")
        print(f"step={step:5d} t={t:.6f} G={gamma_val:+.4f} "
              f"R_rms={R_rms:.4f} R_half={R_half:.3f} "
              f"alpha={alpha_max:.2e} alpha@pk={alpha_at_peak:.2e} "
              f"spec={spec_ratio:.4f} [{status}] "
              f"|w|={om1:.2e} [{elapsed:.0f}s]", flush=True)

    if omega1.abs().max().item() > 1e8:
        print(f"BLOWUP at step={step}", flush=True)
        break
    u1, omega1, _, _ = solver.step_rk4(u1, omega1, dt)
    t += dt
    u_r_dummy = torch.zeros_like(u1)
    dt = solver.compute_dt(u_r_dummy, u_r_dummy, omega1, dt)

out_path = os.path.join(os.path.dirname(__file__),
                        "results", "core_width_nr64.json")
with open(out_path, "w") as f:
    json.dump(results, f)
print(f"SAVED to {out_path}", flush=True)

# --- Quick summary ---
print("\n=== CORE WIDTH vs STRAIN SUMMARY ===")
gammas = [r["gamma"] for r in results]
g_min_idx = np.argmin(gammas)
g_min = results[g_min_idx]
print(f"Γ minimum: {g_min['gamma']:.4f} at t={g_min['t']:.6f}")
print(f"  R_rms={g_min['R_rms']:.4f}  R_half={g_min['R_half']:.3f}")
print(f"  alpha_max={g_min['alpha_max']:.2e}  alpha@peak={g_min['alpha_at_peak']:.2e}")
print(f"  peak_r={g_min['peak_r']:.4f}")

# Find R_rms maximum and check if it correlates with Γ minimum
r_rms_vals = [r["R_rms"] for r in results]
r_max_idx = np.argmax(r_rms_vals)
r_max = results[r_max_idx]
print(f"\nR_rms maximum: {r_max['R_rms']:.4f} at t={r_max['t']:.6f}")
print(f"  Γ at R_max: {r_max['gamma']:.4f}")
print(f"  alpha_max={r_max['alpha_max']:.2e}")

# Check correlation during trough (Γ < 0.5)
trough = [r for r in results if r["gamma"] < 0.5]
if trough:
    print(f"\n--- Trough phase (Γ < 0.5, {len(trough)} points) ---")
    for r in trough[::max(1, len(trough)//10)]:
        print(f"  t={r['t']:.6f} G={r['gamma']:+.4f} R_rms={r['R_rms']:.4f} "
              f"alpha={r['alpha_max']:.2e} S={r['S']:.2e} nuP={r['nuP']:.2e}")
