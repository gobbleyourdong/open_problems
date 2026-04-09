#!/bin/bash
# Nr=128 on H200 — hardware comparison vs Spark Nr=128
# Run AFTER Nr=256 finishes (check: ps aux | grep python)

ssh -o StrictHostKeyChecking=no -p 40957 -i ~/.ssh/id_ed25519 root@103.196.86.19 'nohup python3 -u -c "
import sys, torch, time, json, numpy as np
sys.path.insert(0, \"/root\")
from sweep import SweepSolver

dev = \"cuda\"
Nr, Nz = 128, 256
nu = 1e-4

solver = SweepSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu, device=dev, ic_type=\"luo_hou\", amplitude=100.0)
u1, omega1 = solver.init_ic()
t, dt, step = 0.0, 1e-7, 0
results = []
t0 = time.time()

for step in range(12000):
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
        ratio = high / low
        om1 = omega1.abs().max().item()
        elapsed = time.time() - t0
        status = \"OK\" if ratio < 0.01 else (\"MARG\" if ratio < 0.1 else \"UNDER\")
        results.append({\"step\": step, \"t\": t, \"gamma\": gamma_val, \"spectral\": ratio, \"om1\": om1})
        print(f\"step={step:5d} t={t:.6f} G={gamma_val:+.4f} spec={ratio:.4f} [{status}] |w|={om1:.2e} [{elapsed:.0f}s]\", flush=True)

    if omega1.abs().max().item() > 1e8:
        print(f\"BLOWUP at step={step}\", flush=True)
        break
    u1, omega1, _, _ = solver.step_rk4(u1, omega1, dt)
    t += dt
    u_r_dummy = torch.zeros_like(u1)
    dt = solver.compute_dt(u_r_dummy, u_r_dummy, omega1, dt)

with open(\"/root/gamma_nr128_h200.json\", \"w\") as f:
    json.dump(results, f)
print(\"SAVED\", flush=True)
" > /root/gamma_nr128_h200.log 2>&1 &'
