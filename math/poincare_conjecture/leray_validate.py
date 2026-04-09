"""
Leray solver validation.

Test 1: Small-amplitude IC → should decay exponentially due to Leray penalty.
         Linearized equation: ∂U₁/∂τ ≈ -(ξ/2)·U₁,ξ - U₁ + ν·ΔU₁
         Dominant: -U₁ → decay rate e^{-τ}

Test 2: Run BOTH physical and Leray solvers from same IC, compare early steps.
         With drift/decay ON, Leray should show faster decay of |W₁|.

Test 3: Axis-concentrated IC — Gaussian blob at ξ=0.1, designed for Leray frame.
         This is what the orbit finder will use.
"""
import sys, os, torch, time, math, numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver
from leray_solver import LeraySolver

dev = "cuda"
Nr, Nz = 64, 128
nu = 1e-4

print("=" * 70)
print("TEST 1: Small amplitude — verify Leray decay")
print("=" * 70)

solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=dev,
                     ic_type='luo_hou', amplitude=1.0)  # tiny amplitude
U1, W1 = solver.init_ic()
tau, dt = 0.0, 1e-6

print(f"|U₁|₀ = {U1.abs().max().item():.4f}")

u_maxes = []
w_maxes = []
taus = []

for step in range(2001):
    if step % 200 == 0:
        u_max = U1.abs().max().item()
        w_max = W1.abs().max().item()
        u_maxes.append(u_max)
        w_maxes.append(w_max)
        taus.append(tau)

        # Expected decay: |U₁| ~ e^{-τ}, |W₁| ~ e^{-1.5τ}
        expected_u = u_maxes[0] * math.exp(-tau) if tau > 0 else u_maxes[0]
        expected_w = w_maxes[0] * math.exp(-1.5 * tau) if w_maxes[0] > 0 and tau > 0 else 0

        print(f"  step={step:4d} τ={tau:.6f} "
              f"|U₁|={u_max:.6f} (expect {expected_u:.6f}) "
              f"|W₁|={w_max:.4e} (expect {expected_w:.4e})")

    U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
    tau += dt

# Check decay rate
if len(u_maxes) > 5 and u_maxes[1] > 0:
    # Fit log(|U₁|) vs τ → slope should be ≈ -1
    taus_arr = np.array(taus[1:])
    log_u = np.log(np.array(u_maxes[1:]) + 1e-30)
    if len(taus_arr) > 2:
        slope_u = np.polyfit(taus_arr, log_u, 1)[0]
        print(f"\n  U₁ decay rate: {slope_u:.4f} (expected: -1.0)")
        print(f"  {'PASS ✓' if abs(slope_u + 1.0) < 0.5 else 'FAIL ✗'}")


print("\n" + "=" * 70)
print("TEST 2: Physical vs Leray comparison")
print("=" * 70)

amp = 10.0  # moderate amplitude
phys = SweepSolver(Nr=Nr, Nz=Nz, nu=nu, device=dev,
                   ic_type='luo_hou', amplitude=amp)
leray = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=dev,
                    ic_type='luo_hou', amplitude=amp)

u1_p, w1_p = phys.init_ic()
u1_l, w1_l = leray.init_ic()
dt = 1e-6

print(f"{'step':>5} {'|u₁|_phys':>12} {'|u₁|_leray':>12} {'ratio':>8} | "
      f"{'|w₁|_phys':>12} {'|w₁|_leray':>12} {'ratio':>8}")

for step in range(1001):
    if step % 100 == 0:
        up = u1_p.abs().max().item()
        ul = u1_l.abs().max().item()
        wp = w1_p.abs().max().item()
        wl = w1_l.abs().max().item()
        r_u = ul / (up + 1e-30)
        r_w = wl / (wp + 1e-30) if wp > 0 else 0
        print(f"{step:5d} {up:12.4f} {ul:12.4f} {r_u:8.4f} | "
              f"{wp:12.4e} {wl:12.4e} {r_w:8.4f}")

    u1_p, w1_p, _, _ = phys.step_rk4(u1_p, w1_p, dt)
    u1_l, w1_l, _, _ = leray.step_rk4(u1_l, w1_l, dt)

print("\nExpected: Leray |U₁| < Physical |u₁| (decay term)")
print("Expected: Leray |W₁| < Physical |ω₁| (stronger decay term)")


print("\n" + "=" * 70)
print("TEST 3: Axis-concentrated IC for orbit search")
print("=" * 70)

solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=dev,
                     ic_type='luo_hou', amplitude=1.0)  # dummy, we override

# Gaussian at ξ=0.1, width σ=0.05 — concentrated near axis
xi = solver.r  # (Nr+1,)
zeta = solver.z  # (Nz+1,)
XI, ZETA = solver.R, solver.Z

xi_target = 0.1
sigma_xi = 0.05
amp_test = 50.0

U1 = amp_test * torch.exp(-((XI - xi_target)**2) / sigma_xi**2) * \
     torch.sin(2 * math.pi * ZETA / solver.Lz)
W1 = torch.zeros_like(U1)
U1[0, :] = 0  # far-field BC
U1[-1, :] = 0  # axis BC (smooth)

tau, dt = 0.0, 1e-7

print(f"IC: Gaussian at ξ={xi_target}, σ={sigma_xi}, A={amp_test}")
print(f"|U₁|₀ = {U1.abs().max().item():.2f}")

for step in range(3001):
    if step % 300 == 0:
        u_max = U1.abs().max().item()
        w_max = W1.abs().max().item()

        # Spectral check
        mid_z = W1.shape[1] // 2
        if w_max > 0:
            w_slice = W1[:, mid_z].cpu().numpy()
            coeffs = np.abs(np.fft.rfft(w_slice))
            n = len(coeffs)
            low = coeffs[:n//4].mean() + 1e-30
            high = coeffs[3*n//4:].mean()
            spec = high / low
        else:
            spec = 0

        status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
        print(f"  step={step:4d} τ={tau:.6f} |U₁|={u_max:.4f} |W₁|={w_max:.4e} "
              f"spec={spec:.4f} [{status}]")

        if u_max < 1e-10 and step > 100:
            print("  → DECAYED (Leray penalty dominates)")
            break
        if u_max > 1e6:
            print("  → BLOWUP (stretching dominates)")
            break

    U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
    tau += dt
    u_r_dummy = torch.zeros_like(U1)
    dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

print("\nDone.")
