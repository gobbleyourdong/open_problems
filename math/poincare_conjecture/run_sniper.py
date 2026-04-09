"""
Sniper IC run — Nr=64 first pass, then Nr=256 if promising.
Vorticity at r=0.10 (peak Biot-Savart sensitivity).
ν=1e-4 to match Luo-Hou comparison.
"""
import sys, os, torch, time, json, numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver

dev = "cuda"
Nr, Nz = 64, 128
nu = 1e-4

solver = SweepSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu, device=dev,
                     ic_type="sniper", amplitude=1000.0)
u1, omega1 = solver.init_ic()
t, dt, step = 0.0, 1e-7, 0
results = []
t0 = time.time()
r = solver.r

print(f"Sniper IC: Nr={Nr} Nz={Nz} nu={nu} dev={dev}")
print(f"u1 peak: {u1.abs().max().item():.2f} at r={r[u1.abs().sum(dim=1).argmax()].item():.3f}")

for step in range(15000):
    if step % 100 == 0:
        psi1 = solver.solve_poisson(omega1)
        du1_dz = solver._ddz(u1)
        S = (omega1 * 2.0 * u1 * du1_dz).sum().item()
        domega1_dr = solver.D_r @ omega1
        domega1_dz = solver._ddz(omega1)
        P = (domega1_dr**2 + domega1_dz**2).sum().item()
        nuP = nu * P
        denom = abs(S) + abs(nuP) + 1e-30
        gamma_val = (S - nuP) / denom

        # Core width
        omega_abs = omega1.abs()
        total_weight = omega_abs.sum().item() + 1e-30
        r_expanded = r.unsqueeze(1).expand_as(omega1)
        R_rms = ((r_expanded**2 * omega_abs).sum().item() / total_weight) ** 0.5

        # Strain rate
        dpsi1_dz = solver._ddz(psi1)
        alpha_max = dpsi1_dz.abs().max().item()

        # Spectral check
        mid_z = omega1.shape[1] // 2
        omega_slice = omega1[:, mid_z].cpu().numpy()
        coeffs = np.abs(np.fft.rfft(omega_slice))
        n = len(coeffs)
        low = coeffs[:n//4].mean() + 1e-30
        high = coeffs[3*n//4:].mean()
        ratio = high / low

        om1 = omega1.abs().max().item()
        elapsed = time.time() - t0
        status = "OK" if ratio < 0.01 else ("MARG" if ratio < 0.1 else "UNDER")
        results.append({
            "step": step, "t": t, "gamma": gamma_val,
            "R_rms": R_rms, "alpha": alpha_max,
            "S": S, "nuP": nuP,
            "spectral": ratio, "om1": om1
        })
        print(f"step={step:5d} t={t:.6f} G={gamma_val:+.4f} "
              f"R={R_rms:.4f} a={alpha_max:.2e} "
              f"spec={ratio:.4f} [{status}] "
              f"|w|={om1:.2e} [{elapsed:.0f}s]", flush=True)

    if omega1.abs().max().item() > 1e8:
        print(f"BLOWUP at step={step}", flush=True)
        break
    u1, omega1, _, _ = solver.step_rk4(u1, omega1, dt)
    t += dt
    u_r_dummy = torch.zeros_like(u1)
    dt = solver.compute_dt(u_r_dummy, u_r_dummy, omega1, dt)

out_path = os.path.join(os.path.dirname(__file__), "results", "sniper_nr64.json")
with open(out_path, "w") as f:
    json.dump(results, f)
print(f"SAVED to {out_path}", flush=True)

# Quick summary
gammas = [r["gamma"] for r in results]
if len(gammas) > 10:
    g_min_idx = np.argmin(gammas[1:]) + 1  # skip t=0
    g_min = results[g_min_idx]
    print(f"\nΓ minimum: {g_min['gamma']:.4f} at t={g_min['t']:.6f} step={g_min['step']}")
    print(f"  R_rms={g_min['R_rms']:.4f} alpha={g_min['alpha']:.2e}")
    # Check if rebound happened
    if g_min_idx < len(gammas) - 5:
        rebound = max(gammas[g_min_idx:])
        print(f"  Rebound to: {rebound:.4f}")
