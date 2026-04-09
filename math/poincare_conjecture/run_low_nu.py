"""
Luo-Hou IC at ν=1e-5 (10× lower than previous runs).
At ν=1e-4, viscosity won at Nr=256.
At ν=1e-5, stretching should dominate much more strongly.
Nr=64 first pass — fast screening.
"""
import sys, os, torch, time, json, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver

dev = "cuda"
Nr, Nz = 64, 128
nu = 1e-5  # 10x lower viscosity

solver = SweepSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu, device=dev,
                     ic_type="luo_hou", amplitude=100.0)
u1, omega1 = solver.init_ic()
t, dt, step = 0.0, 1e-7, 0
results = []
t0 = time.time()
r = solver.r

print(f"Luo-Hou IC: Nr={Nr} Nz={Nz} nu={nu} dev={dev}")

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

        omega_abs = omega1.abs()
        total_weight = omega_abs.sum().item() + 1e-30
        r_expanded = r.unsqueeze(1).expand_as(omega1)
        R_rms = ((r_expanded**2 * omega_abs).sum().item() / total_weight) ** 0.5

        dpsi1_dz = solver._ddz(psi1)
        alpha_max = dpsi1_dz.abs().max().item()

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
        if step % 500 == 0:
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

out_path = os.path.join(os.path.dirname(__file__), "results", "luo_hou_nu1e5_nr64.json")
with open(out_path, "w") as f:
    json.dump(results, f)
print(f"SAVED to {out_path}", flush=True)

# Summary
gammas = [r["gamma"] for r in results if r["step"] > 0]
if gammas:
    g_min = min(gammas)
    print(f"\nΓ_min = {g_min:.4f}")
    print(f"Blowup: {'YES' if any(r['om1'] > 1e7 for r in results) else 'NO'}")
