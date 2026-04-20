"""
Chebyshev(r) × Fourier-sine(z) spectral solver
Axisymmetric Euler equations in Hou-Li variables
Luo-Hou 2014: boundary blowup at (r,z)=(1,0), T*=0.0035056

Variables: u₁=uθ/r  ω₁=ωθ/r  ψ₁=ψθ/r
Equations (ν=0 Euler):
  ∂ₜu₁ + uʳ∂ᵣu₁ + uᶻ∂zu₁ = 2u₁ψ₁,z
  ∂ₜω₁ + uʳ∂ᵣω₁ + uᶻ∂zω₁ = 2u₁u₁,z
  −(∂ᵣᵣ + 3/r·∂ᵣ + ∂zz)ψ₁ = ω₁
  uʳ = −r·ψ₁,z   uᶻ = 2ψ₁ + r·ψ₁,r
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve
import time
import json
import os


def cheb_diff(N):
    """Chebyshev differentiation matrix on [-1,1], N+1 points."""
    i = np.arange(N + 1)
    x = np.cos(np.pi * i / N)

    c = np.ones(N + 1)
    c[0] = c[N] = 2.0
    c *= (-1.0) ** i

    X = x[:, None] - x[None, :]
    D = (c[:, None] / c[None, :]) / (X + np.eye(N + 1))
    D[np.diag_indices(N + 1)] = 0.0
    D[np.diag_indices(N + 1)] = -D.sum(axis=1)

    return D, x


class LuoHouSolver:
    """
    Spectral solver for axisymmetric Euler blowup (Luo-Hou 2014).

    r ∈ [0,1]: Chebyshev collocation, Nr+1 points
    z ∈ [0,L/4]: Fourier sine, Nz modes

    u₁ z-basis: sin((2k-1)πz/(2Lz))  — odd at z=0, even at z=Lz
    ω₁,ψ₁ z-basis: sin(kπz/Lz)       — odd at z=0, odd at z=Lz
    """

    def __init__(self, Nr=32, Nz=32, L=1/6, nu=0.0):
        self.Nr = Nr
        self.Nz = Nz
        self.L = L
        self.Lz = L / 4
        self.nu = nu

        self._setup_grids()
        self._setup_poisson()

    def _setup_grids(self):
        Nr, Nz = self.Nr, self.Nz
        Lz = self.Lz

        # --- Chebyshev in r on [0,1] ---
        D, x = cheb_diff(Nr)
        self.r_nodes = (1.0 + x) / 2.0       # r[0]=1 (wall), r[Nr]=0 (axis)
        self.D1r = 2.0 * D                    # d/dr on [0,1]
        self.D2r = self.D1r @ self.D1r

        self.r_col = self.r_nodes[:, None]     # (Nr+1, 1) for broadcasting

        # --- Fourier sine in z on [0, Lz] ---
        j = np.arange(1, Nz + 1)
        self.z_nodes = Lz * j / (Nz + 1)      # interior collocation points

        # Wavenumbers
        k = np.arange(1, Nz + 1)
        self.kz_u = (2 * k - 1) * np.pi / (2 * Lz)   # u₁ odd-even modes
        self.kz_w = k * np.pi / Lz                     # ω₁,ψ₁ odd-odd modes

        # Forward transform matrices: physical → spectral via S⁻¹
        self.Su = np.sin(self.kz_u[None, :] * self.z_nodes[:, None])
        self.Sw = np.sin(self.kz_w[None, :] * self.z_nodes[:, None])
        self.Su_inv = np.linalg.inv(self.Su)
        self.Sw_inv = np.linalg.inv(self.Sw)

        # z-derivative matrices in physical space
        # ∂z[sin(kz·z)] = kz·cos(kz·z), so D_z = C·diag(kz)·S⁻¹
        Cu = np.cos(self.kz_u[None, :] * self.z_nodes[:, None])
        Cw = np.cos(self.kz_w[None, :] * self.z_nodes[:, None])
        self.Dz_u = Cu @ np.diag(self.kz_u) @ self.Su_inv    # (Nz, Nz)
        self.Dz_w = Cw @ np.diag(self.kz_w) @ self.Sw_inv

        # z second derivative: ∂zz[sin(kz·z)] = -kz²·sin(kz·z)
        # Dzz = S·diag(-kz²)·S⁻¹ — stays in same basis
        self.Dzz_u = self.Su @ np.diag(-self.kz_u**2) @ self.Su_inv
        self.Dzz_w = self.Sw @ np.diag(-self.kz_w**2) @ self.Sw_inv

        # 2D grid
        self.R, self.Z = np.meshgrid(self.r_nodes, self.z_nodes, indexing='ij')

    def _setup_poisson(self):
        """
        Precompute LU factors for Poisson: −Δ₃ψ₁ = ω₁
        In spectral-z: −(D²ᵣ + 3/r·Dᵣ − kz²)ψ̂ₖ = ω̂ₖ for each mode k

        BCs: ψ₁(r=1)=0 [index 0], ∂ᵣψ₁(r=0)=0 [index Nr]
        """
        Nr = self.Nr
        D1 = self.D1r
        D2 = self.D2r

        # 3/r diagonal — skip r=0 (will be overwritten by BC row)
        r = self.r_nodes
        diag_3r = np.zeros(Nr + 1)
        for i in range(Nr + 1):
            if r[i] > 1e-14:
                diag_3r[i] = 3.0 / r[i]
            else:
                # r=0: L'Hôpital → 3/r·∂ᵣ → 3·∂ᵣᵣ, but BC row overrides
                diag_3r[i] = 0.0

        Lr = D2 + np.diag(diag_3r) @ D1  # radial part of Δ₃

        self.poisson_lu = []
        for k in range(self.Nz):
            A = -(Lr - self.kz_w[k]**2 * np.eye(Nr + 1))

            # BC: ψ₁(r=1) = 0  [row 0]
            A[0, :] = 0.0
            A[0, 0] = 1.0

            # BC: ∂ᵣψ₁(r=0) = 0  [row Nr]
            A[Nr, :] = D1[Nr, :]

            self.poisson_lu.append(lu_factor(A))

    def solve_poisson(self, omega1):
        """Solve −Δ₃ψ₁ = ω₁. Input/output: (Nr+1, Nz) physical space."""
        Nr = self.Nr

        # To spectral in z
        omega_hat = omega1 @ self.Sw_inv.T

        psi_hat = np.zeros_like(omega_hat)
        for k in range(self.Nz):
            rhs = omega_hat[:, k].copy()
            rhs[0] = 0.0       # ψ₁(r=1) = 0
            rhs[Nr] = 0.0      # ∂ᵣψ₁(r=0) = 0
            psi_hat[:, k] = lu_solve(self.poisson_lu[k], rhs)

        # Back to physical
        return psi_hat @ self.Sw.T

    def compute_velocity(self, psi1):
        """uʳ = −r·ψ₁,z   uᶻ = 2ψ₁ + r·ψ₁,r"""
        r = self.r_col
        psi1_z = psi1 @ self.Dz_w.T
        psi1_r = self.D1r @ psi1
        ur = -r * psi1_z
        uz = 2.0 * psi1 + r * psi1_r
        return ur, uz, psi1_z, psi1_r

    def rhs(self, u1, omega1):
        """
        RHS of evolution equations (inviscid or viscous).
        Returns (du1_dt, domega1_dt), shape (Nr+1, Nz).
        """
        Nr = self.Nr

        # Poisson solve
        psi1 = self.solve_poisson(omega1)

        # Velocity field
        ur, uz, psi1_z, _ = self.compute_velocity(psi1)

        # Spatial derivatives
        u1_r = self.D1r @ u1
        u1_z = u1 @ self.Dz_u.T
        omega1_r = self.D1r @ omega1
        omega1_z = omega1 @ self.Dz_w.T

        # Advection + stretching
        rhs_u = -ur * u1_r - uz * u1_z + 2.0 * u1 * psi1_z
        rhs_w = -ur * omega1_r - uz * omega1_z + 2.0 * u1 * u1_z

        # Viscous diffusion
        if self.nu > 0:
            r = self.r_col
            diag_3r = np.where(r > 1e-14, 3.0 / r, 0.0)

            u1_rr = self.D2r @ u1
            u1_zz = u1 @ self.Dzz_u.T
            diff_u = u1_rr + diag_3r * u1_r + u1_zz

            omega1_rr = self.D2r @ omega1
            omega1_zz = omega1 @ self.Dzz_w.T
            diff_w = omega1_rr + diag_3r * omega1_r + omega1_zz

            rhs_u += self.nu * diff_u
            rhs_w += self.nu * diff_w

        # --- Boundary conditions ---
        # r=1 (index 0): no-flow wall, u₁ and ω₁ evolved freely
        #   (Luo-Hou uses 7th-order extrapolation — TODO upgrade)
        #   For now: evaluate PDE at wall (no singularity at r=1)

        # r=0 (index Nr): symmetry ∂ᵣu₁=∂ᵣω₁=0
        # Enforce by not zeroing RHS — the PDE is regular at r=0
        # because uʳ = -r·ψ₁,z → 0 as r→0, so advection vanishes.
        # Stretching and z-advection are smooth at r=0.

        return rhs_u, rhs_w

    def step_rk4(self, u1, omega1, dt):
        """Classic RK4."""
        k1u, k1w = self.rhs(u1, omega1)
        k2u, k2w = self.rhs(u1 + 0.5 * dt * k1u, omega1 + 0.5 * dt * k1w)
        k3u, k3w = self.rhs(u1 + 0.5 * dt * k2u, omega1 + 0.5 * dt * k2w)
        k4u, k4w = self.rhs(u1 + dt * k3u, omega1 + dt * k3w)

        u1_new = u1 + (dt / 6.0) * (k1u + 2 * k2u + 2 * k3u + k4u)
        w1_new = omega1 + (dt / 6.0) * (k1w + 2 * k2w + 2 * k3w + k4w)

        return u1_new, w1_new

    def initial_conditions(self):
        """Luo-Hou 2014 IC: u₁(0)=100·exp(−30(1−r²)⁴)·sin(12πz), ω₁(0)=0"""
        R, Z = self.R, self.Z
        u1 = 100.0 * np.exp(-30.0 * (1.0 - R**2)**4) * np.sin(12.0 * np.pi * Z)
        omega1 = np.zeros_like(u1)
        return u1, omega1

    def diagnostics(self, u1, omega1, psi1, t):
        """Key blowup diagnostics."""
        omega_max = np.max(np.abs(omega1))
        u1_max = np.max(np.abs(u1))

        idx_w = np.unravel_index(np.argmax(np.abs(omega1)), omega1.shape)
        idx_u = np.unravel_index(np.argmax(np.abs(u1)), u1.shape)

        return {
            't': float(t),
            'omega_max': float(omega_max),
            'u1_max': float(u1_max),
            'omega_loc': (float(self.r_nodes[idx_w[0]]), float(self.z_nodes[idx_w[1]])),
            'u1_loc': (float(self.r_nodes[idx_u[0]]), float(self.z_nodes[idx_u[1]])),
        }

    def spectral_coeffs(self, u1, omega1):
        """Check spectral decay — convergence diagnostic."""
        u_hat = u1 @ self.Su_inv.T   # (Nr+1, Nz) spectral in z
        w_hat = omega1 @ self.Sw_inv.T

        # Max spectral coeff magnitude per z-mode
        u_spec = np.max(np.abs(u_hat), axis=0)
        w_spec = np.max(np.abs(w_hat), axis=0)

        return u_spec, w_spec


def run(Nr=32, Nz=32, nu=0.0, T_end=0.0035, dt0=1e-5,
        cfl_safety=0.5, log_every=10, save_dir='ns_blowup/results'):
    """
    Main driver. Adaptive time stepping with CFL.
    """
    os.makedirs(save_dir, exist_ok=True)

    print(f"=== Luo-Hou 2014 Euler Blowup ===")
    print(f"Nr={Nr} Nz={Nz} ν={nu} T_end={T_end}")
    print(f"Domain: r∈[0,1] z∈[0,{1/24:.6f}]")
    print(f"Expected blowup: T*=0.0035056 at (r,z)=(1,0)")
    print()

    solver = LuoHouSolver(Nr=Nr, Nz=Nz, L=1/6, nu=nu)
    u1, omega1 = solver.initial_conditions()

    t = 0.0
    dt = dt0
    step = 0
    history = []

    t_start = time.time()

    while t < T_end:
        # Adaptive dt: CFL based on max velocity
        psi1 = solver.solve_poisson(omega1)
        ur, uz, psi1_z, _ = solver.compute_velocity(psi1)

        u_max = max(np.max(np.abs(ur)), np.max(np.abs(uz)), 1e-10)
        dr_min = np.min(np.diff(np.sort(solver.r_nodes)))
        dz_min = np.min(np.diff(solver.z_nodes))
        dx_min = min(dr_min, dz_min)

        dt_cfl = cfl_safety * dx_min / u_max
        dt = min(dt_cfl, T_end - t, dt0)

        # Diagnostics
        if step % log_every == 0:
            diag = solver.diagnostics(u1, omega1, psi1, t)
            diag['dt'] = float(dt)
            diag['step'] = step
            history.append(diag)

            # Blowup scaling check
            T_star = 0.0035056
            dt_blow = T_star - t
            if dt_blow > 0 and diag['omega_max'] > 1:
                gamma_est = -np.log(diag['omega_max']) / np.log(dt_blow)
            else:
                gamma_est = 0

            elapsed = time.time() - t_start
            print(f"[{step:6d}] t={t:.8f}  dt={dt:.2e}  "
                  f"|ω₁|={diag['omega_max']:.6e}  |u₁|={diag['u1_max']:.6e}  "
                  f"ω@({diag['omega_loc'][0]:.3f},{diag['omega_loc'][1]:.6f})  "
                  f"γ≈{gamma_est:.2f}  [{elapsed:.1f}s]")

        # RK4 step
        u1, omega1 = solver.step_rk4(u1, omega1, dt)
        t += dt
        step += 1

        # Blowup detection
        if np.max(np.abs(omega1)) > 1e20 or np.any(np.isnan(omega1)):
            print(f"\n*** BLOWUP DETECTED at t={t:.10f} step={step} ***")
            print(f"    |ω₁|_max = {np.max(np.abs(omega1)):.6e}")
            break

    # Final diagnostics
    elapsed = time.time() - t_start
    psi1 = solver.solve_poisson(omega1)
    diag = solver.diagnostics(u1, omega1, psi1, t)
    print(f"\n=== FINAL t={t:.10f}  |ω₁|={diag['omega_max']:.6e}  [{elapsed:.1f}s] ===")

    # Save
    np.savez(f"{save_dir}/state_Nr{Nr}_Nz{Nz}.npz",
             u1=u1, omega1=omega1, r=solver.r_nodes, z=solver.z_nodes,
             t=t, Nr=Nr, Nz=Nz, nu=nu)

    with open(f"{save_dir}/history_Nr{Nr}_Nz{Nz}.json", 'w') as f:
        json.dump(history, f, indent=2)

    # Spectral decay check
    u_spec, w_spec = solver.spectral_coeffs(u1, omega1)
    print(f"\nSpectral decay (last 4 z-modes):")
    print(f"  u₁: {u_spec[-4:]}")
    print(f"  ω₁: {w_spec[-4:]}")

    return solver, u1, omega1, history


if __name__ == '__main__':
    run(Nr=32, Nz=32, nu=0.0, T_end=0.0035, dt0=1e-5, log_every=10)
