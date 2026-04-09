"""
Newton-Krylov periodic orbit finder for the Leray-frame NS equations.

Algorithm:
  1. Flow map Φ(X₀, T): integrate Leray PDE from state X₀ for Leray-time T
  2. Residual: F(X₀) = Φ(X₀, T) - X₀ = 0  (periodicity condition)
  3. Newton: X₀ ← X₀ - J⁻¹·F  where J = ∂Φ/∂X₀ - I
  4. Krylov: solve J·δX = -F via GMRES, with J·v ≈ (Φ(X₀+εv)-Φ(X₀))/ε

Each GMRES iteration = one forward PDE integration.
At Nr=64: ~30s per integration → ~15 min per Newton step → ~3 hours total.

Usage:
  python orbit_finder.py --nr 64 --nu 1e-4 --period 0.01 --mode scan
  python orbit_finder.py --nr 64 --nu 1e-4 --period 0.01 --mode newton
"""
import sys
import os
import math
import time
import json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from leray_solver import LeraySolver


class OrbitFinder:
    """Newton-Krylov periodic orbit finder for Leray NS."""

    def __init__(self, Nr=64, Nz=128, nu=1e-4, device='cuda',
                 T_period=0.01, dt_init=1e-7,
                 gmres_tol=1e-4, gmres_maxiter=50,
                 newton_tol=1e-6, newton_maxiter=20,
                 fd_eps=1e-7):
        self.Nr = Nr
        self.Nz = Nz
        self.nu = nu
        self.device = device
        self.T_period = T_period
        self.dt_init = dt_init
        self.gmres_tol = gmres_tol
        self.gmres_maxiter = gmres_maxiter
        self.newton_tol = newton_tol
        self.newton_maxiter = newton_maxiter
        self.fd_eps = fd_eps

        # Create solver (reused for all integrations)
        self.solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                                  ic_type='luo_hou', amplitude=1.0)

        # State dimension
        self.n_r = Nr + 1
        self.n_z = Nz + 1
        self.state_dim = 2 * self.n_r * self.n_z  # U₁ + W₁ flattened

        print(f"OrbitFinder: Nr={Nr} Nz={Nz} nu={nu} T={T_period}")
        print(f"State dim: {self.state_dim} ({self.n_r}×{self.n_z} × 2 fields)")

    def state_to_fields(self, x):
        """Flat vector → (U₁, W₁) tensors on device."""
        n = self.n_r * self.n_z
        U1 = x[:n].reshape(self.n_r, self.n_z).to(self.device)
        W1 = x[n:].reshape(self.n_r, self.n_z).to(self.device)
        return U1, W1

    def fields_to_state(self, U1, W1):
        """(U₁, W₁) tensors → flat vector on CPU."""
        return torch.cat([U1.flatten(), W1.flatten()]).cpu()

    def flow_map(self, x0, T, return_trajectory=False):
        """
        Integrate Leray PDE from state x0 for Leray-time T.
        Returns final state as flat vector.
        """
        U1, W1 = self.state_to_fields(x0)
        dt = self.dt_init
        tau = 0.0
        n_steps = 0

        trajectory = []
        if return_trajectory:
            trajectory.append({
                'tau': 0.0, 'U1_max': U1.abs().max().item(),
                'W1_max': W1.abs().max().item(),
            })

        while tau < T:
            # Don't overshoot
            if tau + dt > T:
                dt = T - tau

            U1, W1, _, _ = self.solver.step_rk4(U1, W1, dt)
            tau += dt
            n_steps += 1

            # Adaptive dt
            u_r_dummy = torch.zeros_like(U1)
            dt = self.solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

            # Safety: bail on blowup
            if W1.abs().max().item() > 1e10 or U1.abs().max().item() > 1e10:
                print(f"  BLOWUP during flow_map at tau={tau:.6f}, step={n_steps}")
                break

            if return_trajectory and n_steps % 100 == 0:
                trajectory.append({
                    'tau': tau, 'U1_max': U1.abs().max().item(),
                    'W1_max': W1.abs().max().item(),
                })

        x_final = self.fields_to_state(U1, W1)

        if return_trajectory:
            return x_final, n_steps, trajectory
        return x_final, n_steps

    def residual(self, x0):
        """F(x0) = Φ(x0, T) - x0."""
        x_T, n_steps = self.flow_map(x0, self.T_period)
        return x_T - x0, n_steps

    def jvp(self, x0, x0_T, v):
        """
        Jacobian-vector product: J·v ≈ (Φ(x0+εv) - Φ(x0)) / ε
        x0_T = Φ(x0) is precomputed to save one integration.
        """
        eps = self.fd_eps * max(1.0, x0.norm().item()) / max(1.0, v.norm().item())
        x_pert, _ = self.flow_map(x0 + eps * v, self.T_period)
        # J = dΦ/dx0 - I, so J·v = (Φ(x0+εv) - Φ(x0))/ε - v
        return (x_pert - x0_T) / eps - v

    def gmres(self, x0, x0_T, rhs):
        """
        Solve J·δx = rhs using restarted GMRES (matrix-free).
        J·v computed via jvp (one PDE integration per iteration).
        """
        # Simple GMRES implementation (no restart for now)
        n = len(rhs)
        tol = self.gmres_tol * rhs.norm().item()

        # Arnoldi process
        V = [rhs / rhs.norm()]
        H = torch.zeros(self.gmres_maxiter + 1, self.gmres_maxiter)
        beta = rhs.norm().item()
        e1 = torch.zeros(self.gmres_maxiter + 1)
        e1[0] = beta

        n_jvp = 0
        for j in range(self.gmres_maxiter):
            t0 = time.time()
            w = self.jvp(x0, x0_T, V[j])
            n_jvp += 1
            elapsed = time.time() - t0

            # Gram-Schmidt
            for i in range(j + 1):
                H[i, j] = torch.dot(w, V[i])
                w = w - H[i, j] * V[i]

            H[j + 1, j] = w.norm()

            # Check for breakdown
            if H[j + 1, j].item() < 1e-14:
                print(f"  GMRES breakdown at iter {j}")
                break

            V.append(w / H[j + 1, j])

            # Solve least squares: min |H·y - beta·e1|
            H_sub = H[:j + 2, :j + 1]
            e1_sub = e1[:j + 2]
            y, _ = torch.linalg.lstsq(H_sub, e1_sub)

            # Compute residual norm
            res = (H_sub @ y - e1_sub).norm().item()

            if (j + 1) % 5 == 0 or res < tol:
                print(f"  GMRES iter {j+1}: |res|={res:.2e} "
                      f"(tol={tol:.2e}) [{elapsed:.0f}s/jvp]")

            if res < tol:
                print(f"  GMRES converged at iter {j+1}")
                break

        # Reconstruct solution: x = V·y
        y_final, _ = torch.linalg.lstsq(H[:j + 2, :j + 1], e1[:j + 2])
        x_sol = torch.zeros(n)
        for i in range(len(y_final)):
            x_sol += y_final[i].item() * V[i]

        return x_sol, j + 1, n_jvp

    def newton(self, x0_guess):
        """
        Newton-Krylov iteration to find periodic orbit.
        """
        x = x0_guess.clone()
        history = []

        print(f"\n{'='*60}")
        print(f"NEWTON-KRYLOV ORBIT SEARCH")
        print(f"T_period = {self.T_period}")
        print(f"{'='*60}")

        for k in range(self.newton_maxiter):
            t0 = time.time()

            # Compute residual F = Φ(x, T) - x
            x_T, n_fwd_steps = self.flow_map(x, self.T_period)
            F = x_T - x
            F_norm = F.norm().item()
            x_norm = x.norm().item()
            rel_res = F_norm / (x_norm + 1e-30)

            # Diagnostics
            U1_0, W1_0 = self.state_to_fields(x)
            U1_T, W1_T = self.state_to_fields(x_T)

            print(f"\nNewton step {k}:")
            print(f"  |F| = {F_norm:.6e} (rel: {rel_res:.6e})")
            print(f"  |U₁|₀ = {U1_0.abs().max().item():.4f}, "
                  f"|W₁|₀ = {W1_0.abs().max().item():.4e}")
            print(f"  |U₁|_T = {U1_T.abs().max().item():.4f}, "
                  f"|W₁|_T = {W1_T.abs().max().item():.4e}")
            print(f"  Forward integration: {n_fwd_steps} steps")

            history.append({
                'step': k, 'F_norm': F_norm, 'rel_res': rel_res,
                'U1_max': U1_0.abs().max().item(),
                'W1_max': W1_0.abs().max().item(),
            })

            # Check convergence
            if rel_res < self.newton_tol:
                print(f"\n  CONVERGED at Newton step {k}!")
                print(f"  Periodic orbit found with |F|/|x| = {rel_res:.2e}")
                return x, history, True

            # Solve J·δx = -F via GMRES
            print(f"  Solving GMRES...")
            delta_x, n_gmres, n_jvp = self.gmres(x, x_T, -F)

            # Line search: find α that reduces |F|
            alpha = 1.0
            for ls in range(5):
                x_trial = x + alpha * delta_x
                F_trial, _ = self.residual(x_trial)
                F_trial_norm = F_trial.norm().item()
                if F_trial_norm < F_norm:
                    break
                alpha *= 0.5
                print(f"  Line search: α={alpha:.4f}, |F|={F_trial_norm:.6e}")

            x = x + alpha * delta_x

            elapsed = time.time() - t0
            print(f"  Step {k} complete: α={alpha:.4f}, |δx|={delta_x.norm().item():.4e}, "
                  f"{elapsed:.0f}s ({n_gmres} GMRES, {n_jvp} JVPs)")

        print(f"\nDid not converge in {self.newton_maxiter} Newton steps")
        return x, history, False

    def scan_recurrence(self, x0, T_max, n_checkpoints=100):
        """
        Run Leray solver forward and check for recurrence.
        If the state returns close to x0, we have an approximate period.
        """
        print(f"\n{'='*60}")
        print(f"RECURRENCE SCAN (T_max={T_max})")
        print(f"{'='*60}")

        dt_check = T_max / n_checkpoints
        x_ref = x0.clone()
        x_ref_norm = x_ref.norm().item()

        U1, W1 = self.state_to_fields(x0)
        dt = self.dt_init
        tau = 0.0
        n_steps = 0
        best_dist = float('inf')
        best_tau = 0.0

        results = []

        for checkpoint in range(n_checkpoints):
            tau_target = (checkpoint + 1) * dt_check

            # Integrate to next checkpoint
            while tau < tau_target:
                if tau + dt > tau_target:
                    dt = tau_target - tau
                U1, W1, _, _ = self.solver.step_rk4(U1, W1, dt)
                tau += dt
                n_steps += 1
                u_r_dummy = torch.zeros_like(U1)
                dt = self.solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

                if W1.abs().max().item() > 1e10:
                    print(f"  BLOWUP at τ={tau:.6f}")
                    return results, best_tau

            # Check distance to initial state
            x_current = self.fields_to_state(U1, W1)
            dist = (x_current - x_ref).norm().item()
            rel_dist = dist / (x_ref_norm + 1e-30)

            if dist < best_dist and tau > dt_check:  # skip first checkpoint
                best_dist = dist
                best_tau = tau

            entry = {
                'tau': tau, 'dist': dist, 'rel_dist': rel_dist,
                'U1_max': U1.abs().max().item(),
                'W1_max': W1.abs().max().item(),
            }
            results.append(entry)

            if (checkpoint + 1) % 10 == 0:
                marker = " ← BEST" if tau == best_tau else ""
                print(f"  τ={tau:.6f} dist={dist:.4e} (rel={rel_dist:.4e}) "
                      f"|U₁|={U1.abs().max().item():.4f} "
                      f"|W₁|={W1.abs().max().item():.4e}{marker}")

        print(f"\nBest recurrence: τ={best_tau:.6f}, dist={best_dist:.4e}")
        print(f"  → Use T_period={best_tau:.6f} as initial guess for Newton")

        return results, best_tau


def make_axis_ic(solver, amplitude=50.0, xi_target=0.1, sigma=0.05):
    """Create a smooth axis-concentrated IC for orbit search."""
    XI, ZETA = solver.R, solver.Z
    U1 = amplitude * torch.exp(-((XI - xi_target)**2) / sigma**2) * \
         torch.sin(2 * math.pi * ZETA / solver.Lz)
    W1 = torch.zeros_like(U1)
    U1[0, :] = 0   # far-field BC
    U1[-1, :] = 0   # axis parity
    return U1, W1


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--nu', type=float, default=1e-4)
    parser.add_argument('--period', type=float, default=0.005)
    parser.add_argument('--mode', type=str, default='scan',
                        choices=['scan', 'newton', 'both'])
    parser.add_argument('--amp', type=float, default=50.0)
    parser.add_argument('--device', type=str, default='cuda')
    parser.add_argument('--scan-tmax', type=float, default=0.05)
    args = parser.parse_args()

    finder = OrbitFinder(Nr=args.nr, Nz=args.nz, nu=args.nu,
                         device=args.device, T_period=args.period)

    # Create initial guess
    U1, W1 = make_axis_ic(finder.solver, amplitude=args.amp)
    x0 = finder.fields_to_state(U1, W1)
    print(f"\nIC: axis Gaussian, A={args.amp}, |x₀|={x0.norm().item():.2f}")

    if args.mode in ('scan', 'both'):
        # Scan for recurrence
        results, best_T = finder.scan_recurrence(x0, T_max=args.scan_tmax)

        # Save scan results
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"orbit_scan_nr{args.nr}_nu{args.nu}.json")
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Saved scan to {out_path}")

        if args.mode == 'both' and best_T > 0:
            finder.T_period = best_T

    if args.mode in ('newton', 'both'):
        # Newton-Krylov orbit search
        x_orbit, history, converged = finder.newton(x0)

        if converged:
            print("\n" + "=" * 60)
            print("PERIODIC ORBIT FOUND!")
            print("=" * 60)
            U1_orbit, W1_orbit = finder.state_to_fields(x_orbit)
            print(f"|U₁| = {U1_orbit.abs().max().item():.6f}")
            print(f"|W₁| = {W1_orbit.abs().max().item():.6e}")
            print(f"Period T = {finder.T_period:.8f}")
            print(f"ν = {args.nu}")

            # Save orbit
            out_dir = os.path.join(os.path.dirname(__file__), "results")
            torch.save({
                'U1': U1_orbit.cpu(), 'W1': W1_orbit.cpu(),
                'T_period': finder.T_period, 'nu': args.nu,
                'Nr': args.nr, 'Nz': args.nz,
                'history': history,
            }, os.path.join(out_dir, f"orbit_nr{args.nr}_nu{args.nu}.pt"))

        # Save Newton history
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        out_path = os.path.join(out_dir, f"newton_history_nr{args.nr}_nu{args.nu}.json")
        with open(out_path, "w") as f:
            json.dump(history, f, indent=2)
        print(f"Saved Newton history to {out_path}")


if __name__ == '__main__':
    main()
