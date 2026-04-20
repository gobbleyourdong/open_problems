"""
Validation run: Nr=256 on Spark (Docker) to compare against H200 results.
Run 5000 steps — enough to check if early trajectory matches H200.
"""
import sys, os, torch, time, numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver

dev = "cuda"
Nr, Nz = 256, 512
nu = 1e-4

solver = SweepSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu, device=dev,
                     ic_type="luo_hou", amplitude=100.0)
u1, omega1 = solver.init_ic()
t, dt, step = 0.0, 1e-7, 0
t0 = time.time()
r = solver.r

print(f"VALIDATE: Nr={Nr} Nz={Nz} nu={nu} dev={dev} dtype={u1.dtype}")
print(f"GPU: {torch.cuda.get_device_name()}")

for step in range(5001):
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

print(f"\nDone. Total time: {time.time()-t0:.0f}s")

# Compare against H200 reference values at key steps
print("\n--- COMPARISON vs H200 ---")
h200_ref = {
    200:  (0.9819, 75.06, 0.0044),
    1000: (0.9717, 377.3, 0.0009),
    2000: (0.9613, 784.4, 0.0007),
    3000: (0.9556, 1506.4, 0.0008),
    4000: (0.9115, 3725.9, 0.0008),
    5000: (0.5618, 7413.3, 0.0008),
}
print(f"{'step':>6} {'H200_G':>8} {'Spark_G':>8} {'diff':>8} | "
      f"{'H200_w':>10} {'Spark_w':>10}")
