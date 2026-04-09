"""
Warm-start orbit search: run Leray forward to build self-consistent state,
then scan for recurrence from the warmed state.

Also try: take physical-frame checkpoint, transform to Leray variables,
use that as IC (already has U₁ and W₁ in approximate balance).
"""
import sys, os, math, time, json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from leray_solver import LeraySolver
from orbit_finder import OrbitFinder, make_axis_ic


def warmstart_scan(Nr=64, Nz=128, nu=1e-4, device='cuda',
                   warmup_tau=0.005, scan_tau=0.02, n_checkpoints=50):
    """
    Phase 1: Run Leray forward for warmup_tau to build self-consistent state.
    Phase 2: From warmed state, scan for recurrence over scan_tau.
    """
    print("=" * 60)
    print("WARM-START ORBIT SEARCH")
    print(f"Nr={Nr} Nz={Nz} nu={nu}")
    print(f"Warmup: {warmup_tau}, Scan: {scan_tau}")
    print("=" * 60)

    solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                         ic_type='luo_hou', amplitude=1.0)

    # Create axis-concentrated IC
    XI, ZETA = solver.R, solver.Z
    xi_target = 0.15
    sigma = 0.08
    amp = 100.0

    U1 = amp * torch.exp(-((XI - xi_target)**2) / sigma**2) * \
         torch.sin(2 * math.pi * ZETA / solver.Lz)
    W1 = torch.zeros_like(U1)
    U1[0, :] = 0
    U1[-1, :] = 0

    print(f"\nIC: Gaussian at ξ={xi_target}, σ={sigma}, A={amp}")
    print(f"|U₁|₀ = {U1.abs().max().item():.2f}")

    # Phase 1: Warmup
    print(f"\n--- PHASE 1: WARMUP (τ={warmup_tau}) ---")
    dt = 1e-7
    tau = 0.0
    t0 = time.time()

    for step in range(100000):
        if step % 500 == 0:
            u_max = U1.abs().max().item()
            w_max = W1.abs().max().item()
            spec = 0
            if w_max > 0:
                mid_z = W1.shape[1] // 2
                w_slice = W1[:, mid_z].cpu().numpy()
                coeffs = np.abs(np.fft.rfft(w_slice))
                n = len(coeffs)
                low = coeffs[:n//4].mean() + 1e-30
                high = coeffs[3*n//4:].mean()
                spec = high / low
            status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
            elapsed = time.time() - t0
            print(f"  step={step:5d} τ={tau:.6f} |U₁|={u_max:.4f} |W₁|={w_max:.4e} "
                  f"spec={spec:.4f} [{status}] dt={dt:.2e} [{elapsed:.0f}s]")

            if status == "UNDER":
                print("  SPECTRAL UNDER-RESOLVED — stopping warmup")
                break

        if tau >= warmup_tau:
            break

        U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
        tau += dt
        u_r_dummy = torch.zeros_like(U1)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

        if U1.abs().max().item() > 1e8:
            print("  BLOWUP during warmup")
            return

    print(f"\nWarmup complete at τ={tau:.6f}")
    print(f"|U₁| = {U1.abs().max().item():.4f}")
    print(f"|W₁| = {W1.abs().max().item():.4e}")

    # Phase 2: Recurrence scan from warmed state
    print(f"\n--- PHASE 2: RECURRENCE SCAN (Δτ={scan_tau}) ---")

    x_ref = torch.cat([U1.flatten(), W1.flatten()]).cpu()
    x_ref_norm = x_ref.norm().item()

    dt_check = scan_tau / n_checkpoints
    best_dist = float('inf')
    best_tau_offset = 0.0
    results = []

    for cp in range(n_checkpoints):
        tau_target = tau + (cp + 1) * dt_check

        while tau < tau_target:
            if tau + dt > tau_target:
                dt = tau_target - tau
            U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
            tau += dt
            u_r_dummy = torch.zeros_like(U1)
            dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

            if U1.abs().max().item() > 1e8:
                print("  BLOWUP during scan")
                break

        x_current = torch.cat([U1.flatten(), W1.flatten()]).cpu()
        dist = (x_current - x_ref).norm().item()
        rel_dist = dist / (x_ref_norm + 1e-30)
        tau_offset = (cp + 1) * dt_check

        if dist < best_dist:
            best_dist = dist
            best_tau_offset = tau_offset

        # Also track field-level metrics
        u_max = U1.abs().max().item()
        w_max = W1.abs().max().item()

        # Spectral
        mid_z = W1.shape[1] // 2
        w_slice = W1[:, mid_z].cpu().numpy()
        coeffs = np.abs(np.fft.rfft(w_slice))
        n = len(coeffs)
        low = coeffs[:n//4].mean() + 1e-30
        high = coeffs[3*n//4:].mean()
        spec = high / low

        results.append({
            'tau_offset': tau_offset, 'dist': dist, 'rel_dist': rel_dist,
            'U1_max': u_max, 'W1_max': w_max, 'spectral': spec,
        })

        if (cp + 1) % 5 == 0:
            status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
            marker = " ← BEST" if tau_offset == best_tau_offset else ""
            print(f"  Δτ={tau_offset:.6f} dist={dist:.4e} (rel={rel_dist:.4e}) "
                  f"|U₁|={u_max:.4f} |W₁|={w_max:.4e} [{status}]{marker}")

            if status == "UNDER":
                print("  SPECTRAL UNDER-RESOLVED — stopping scan")
                break

    print(f"\nBest recurrence: Δτ={best_tau_offset:.6f}, dist={best_dist:.4e} "
          f"(rel={best_dist/x_ref_norm:.4e})")

    # Is the best distance decreasing? Check if there's a dip
    dists = [r['dist'] for r in results]
    if len(dists) > 5:
        # Look for local minima
        for i in range(2, len(dists)-2):
            if dists[i] < dists[i-1] and dists[i] < dists[i+1] and dists[i] < dists[i-2]:
                print(f"  LOCAL MINIMUM at Δτ={results[i]['tau_offset']:.6f}, "
                      f"dist={dists[i]:.4e}")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"warmstart_scan_nr{Nr}.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved to {out_path}")

    return results


def checkpoint_ic(Nr=64, Nz=128, nu=1e-4, device='cuda'):
    """
    Load physical-frame checkpoint and transform to Leray variables.
    Use as IC for orbit search.
    """
    print("=" * 60)
    print("CHECKPOINT IC — Transform physical data to Leray frame")
    print("=" * 60)

    # Load Nr=256 checkpoint
    ckpt_dir = os.path.join(os.path.dirname(__file__), "results", "h200_sync")
    ckpt_files = sorted([f for f in os.listdir(ckpt_dir) if f.startswith("checkpoint_nr256")])

    if not ckpt_files:
        print("No checkpoints found!")
        return None

    # Use the checkpoint nearest the Γ minimum (step 20000-25000)
    best_ckpt = None
    for f in ckpt_files:
        step = int(f.split("step")[1].split(".")[0])
        if step >= 20000:
            best_ckpt = f
            break
    if best_ckpt is None:
        best_ckpt = ckpt_files[-1]

    ckpt_path = os.path.join(ckpt_dir, best_ckpt)
    print(f"Loading: {best_ckpt}")

    data = torch.load(ckpt_path, map_location='cpu', weights_only=False)
    print(f"Checkpoint keys: {list(data.keys())}")

    if 'u1' in data and 'omega1' in data:
        u1_phys = data['u1']
        w1_phys = data['omega1']
        t_phys = data.get('t', 0)

        print(f"Physical frame: t={t_phys:.6f}")
        print(f"  |u₁| = {u1_phys.abs().max().item():.4f}")
        print(f"  |ω₁| = {w1_phys.abs().max().item():.4e}")
        print(f"  Shape: {u1_phys.shape}")

        # Leray transform:
        # U₁ = λ² · u₁,  W₁ = λ³ · ω₁
        # where λ = √(T*-t), T* = 0.0284 (from our fit)
        T_star = 0.0284
        lam = math.sqrt(T_star - t_phys)
        print(f"  T* = {T_star}, λ = {lam:.6f}")

        U1_leray = lam**2 * u1_phys
        W1_leray = lam**3 * w1_phys

        print(f"Leray frame:")
        print(f"  |U₁| = {U1_leray.abs().max().item():.4f}")
        print(f"  |W₁| = {W1_leray.abs().max().item():.4e}")

        # If checkpoint is Nr=256 but we want Nr=64, need to interpolate
        if u1_phys.shape[0] != Nr + 1:
            print(f"\nCheckpoint is {u1_phys.shape[0]-1}×{u1_phys.shape[1]-1}, "
                  f"need {Nr}×{Nz}. Interpolation needed.")
            print("Skipping — use matching resolution or add interpolation.")
            return None

        return U1_leray, W1_leray
    else:
        print(f"Unexpected checkpoint format: {list(data.keys())}")
        return None


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--nu', type=float, default=1e-4)
    parser.add_argument('--warmup', type=float, default=0.003)
    parser.add_argument('--scan', type=float, default=0.01)
    parser.add_argument('--device', type=str, default='cuda')
    args = parser.parse_args()

    # Try checkpoint IC first
    result = checkpoint_ic(Nr=args.nr, Nz=args.nz, nu=args.nu, device=args.device)

    # Run warm-start scan
    warmstart_scan(Nr=args.nr, Nz=args.nz, nu=args.nu, device=args.device,
                   warmup_tau=args.warmup, scan_tau=args.scan)
