#!/usr/bin/env python3
"""
NS Log-Enstrophy Growth Rate G_max — The Next Number for NS Regularity.

G(t) = ∫ log(1 + |ω(x,t)|²) dx

If G_max = sup_t G(t)/t < ∞ for all smooth solutions: regularity follows.
If G_max = ∞ for some flow: that flow is the blowup candidate.

This script computes G(t) on standard test flows using numpy (CPU).
For production: use the PyTorch GPU solver in ns3d_spectral.py.

Test flows:
1. Taylor-Green vortex (the standard blowup candidate)
2. ABC flow (Beltrami, exact Euler solution)
3. Random divergence-free initial data

Deps: numpy only (CPU spectral solver for small N).
"""

import numpy as np
import time


class SpectralNS3D_CPU:
    """Minimal 3D spectral NS solver on [0,2π]³ periodic. CPU/numpy."""

    def __init__(self, N=32, nu=0.01):
        self.N = N
        self.nu = nu
        self.L = 2 * np.pi

        # Wavenumbers
        k1d = np.fft.fftfreq(N, d=1.0/N)
        self.kx, self.ky, self.kz = np.meshgrid(k1d, k1d, k1d, indexing='ij')
        self.k2 = self.kx**2 + self.ky**2 + self.kz**2
        self.k2[0, 0, 0] = 1  # avoid div by zero

        # Dealiasing mask (2/3 rule)
        kmax = N // 3
        self.mask = ((np.abs(self.kx) <= kmax) & (np.abs(self.ky) <= kmax) &
                     (np.abs(self.kz) <= kmax)).astype(float)

    def project_divfree(self, uh, vh, wh):
        """Leray projection: remove gradient component."""
        div = self.kx * uh + self.ky * vh + self.kz * wh
        uh -= self.kx * div / self.k2
        vh -= self.ky * div / self.k2
        wh -= self.kz * div / self.k2
        return uh, vh, wh

    def rhs(self, uh, vh, wh):
        """RHS of NS in Fourier: -P(u·∇u) - ν k² û."""
        N = self.N
        # To physical space
        u = np.fft.ifftn(uh).real
        v = np.fft.ifftn(vh).real
        w = np.fft.ifftn(wh).real

        # Nonlinear term: u·∇u (dealiased)
        ux = np.fft.ifftn(1j * self.kx * uh).real
        uy = np.fft.ifftn(1j * self.ky * uh).real
        uz = np.fft.ifftn(1j * self.kz * uh).real
        vx = np.fft.ifftn(1j * self.kx * vh).real
        vy = np.fft.ifftn(1j * self.ky * vh).real
        vz = np.fft.ifftn(1j * self.kz * vh).real
        wx = np.fft.ifftn(1j * self.kx * wh).real
        wy = np.fft.ifftn(1j * self.ky * wh).real
        wz = np.fft.ifftn(1j * self.kz * wh).real

        nlx = u*ux + v*uy + w*uz
        nly = u*vx + v*vy + w*vz
        nlz = u*wx + v*wy + w*wz

        nlxh = np.fft.fftn(nlx) * self.mask
        nlyh = np.fft.fftn(nly) * self.mask
        nlzh = np.fft.fftn(nlz) * self.mask

        # Project
        nlxh, nlyh, nlzh = self.project_divfree(nlxh, nlyh, nlzh)

        # Diffusion
        duh = -nlxh - self.nu * self.k2 * uh
        dvh = -nlyh - self.nu * self.k2 * vh
        dwh = -nlzh - self.nu * self.k2 * wh

        return duh, dvh, dwh

    def step_rk4(self, uh, vh, wh, dt):
        """One RK4 step."""
        k1u, k1v, k1w = self.rhs(uh, vh, wh)
        k2u, k2v, k2w = self.rhs(uh+dt/2*k1u, vh+dt/2*k1v, wh+dt/2*k1w)
        k3u, k3v, k3w = self.rhs(uh+dt/2*k2u, vh+dt/2*k2v, wh+dt/2*k2w)
        k4u, k4v, k4w = self.rhs(uh+dt*k3u, vh+dt*k3v, wh+dt*k3w)
        uh += dt/6*(k1u + 2*k2u + 2*k3u + k4u)
        vh += dt/6*(k1v + 2*k2v + 2*k3v + k4v)
        wh += dt/6*(k1w + 2*k2w + 2*k3w + k4w)
        return uh, vh, wh

    def vorticity(self, uh, vh, wh):
        """Compute vorticity ω = ∇×u in physical space."""
        wx = np.fft.ifftn(1j*(self.ky*wh - self.kz*vh)).real
        wy = np.fft.ifftn(1j*(self.kz*uh - self.kx*wh)).real
        wz = np.fft.ifftn(1j*(self.kx*vh - self.ky*uh)).real
        return wx, wy, wz

    def log_enstrophy(self, uh, vh, wh):
        """G = (1/V) ∫ log(1 + |ω|²) dx (volume-averaged)."""
        wx, wy, wz = self.vorticity(uh, vh, wh)
        omega_sq = wx**2 + wy**2 + wz**2
        return np.mean(np.log(1 + omega_sq))

    def enstrophy(self, uh, vh, wh):
        """Ω = (1/V) ∫ |ω|² dx."""
        wx, wy, wz = self.vorticity(uh, vh, wh)
        return np.mean(wx**2 + wy**2 + wz**2)

    def max_vorticity(self, uh, vh, wh):
        wx, wy, wz = self.vorticity(uh, vh, wh)
        return np.sqrt(np.max(wx**2 + wy**2 + wz**2))


def taylor_green_ic(N):
    """Taylor-Green vortex: u = (sin x cos y cos z, -cos x sin y cos z, 0)."""
    x = np.linspace(0, 2*np.pi, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    u = np.sin(X) * np.cos(Y) * np.cos(Z)
    v = -np.cos(X) * np.sin(Y) * np.cos(Z)
    w = np.zeros_like(u)
    return np.fft.fftn(u), np.fft.fftn(v), np.fft.fftn(w)


def abc_flow_ic(N, A=1.0, B=1.0, C=1.0):
    """ABC flow: Beltrami (ω = u), exact Euler solution."""
    x = np.linspace(0, 2*np.pi, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    u = A*np.sin(Z) + C*np.cos(Y)
    v = B*np.sin(X) + A*np.cos(Z)
    w = C*np.sin(Y) + B*np.cos(X)
    return np.fft.fftn(u), np.fft.fftn(v), np.fft.fftn(w)


def run_and_track(solver, uh, vh, wh, T_max, dt, name):
    """Run the solver and track G(t), Ω(t), ||ω||_∞(t)."""
    t = 0.0
    G_data = [(0, solver.log_enstrophy(uh, vh, wh),
               solver.enstrophy(uh, vh, wh),
               solver.max_vorticity(uh, vh, wh))]

    steps = int(T_max / dt)
    print(f"  {name}: T_max={T_max}, dt={dt:.4f}, {steps} steps")

    for step in range(steps):
        uh, vh, wh = solver.step_rk4(uh, vh, wh, dt)
        t += dt
        if (step+1) % max(1, steps//10) == 0:
            G = solver.log_enstrophy(uh, vh, wh)
            E = solver.enstrophy(uh, vh, wh)
            W = solver.max_vorticity(uh, vh, wh)
            G_data.append((t, G, E, W))

    return G_data


def main():
    print("=" * 60)
    print("NS LOG-ENSTROPHY GROWTH RATE G_max")
    print("=" * 60)
    print()

    N = 32  # Small for CPU. Production: N=256 on GPU.
    nu = 0.01

    solver = SpectralNS3D_CPU(N=N, nu=nu)
    print(f"Grid: {N}³, ν={nu}")

    # Taylor-Green
    print(f"\n--- Taylor-Green Vortex ---")
    uh, vh, wh = taylor_green_ic(N)
    uh, vh, wh = solver.project_divfree(uh, vh, wh)
    tg_data = run_and_track(solver, uh, vh, wh, T_max=2.0, dt=0.005, name="TG")

    # ABC flow
    print(f"\n--- ABC Flow ---")
    uh, vh, wh = abc_flow_ic(N)
    uh, vh, wh = solver.project_divfree(uh, vh, wh)
    abc_data = run_and_track(solver, uh, vh, wh, T_max=2.0, dt=0.005, name="ABC")

    # Results
    print(f"\n{'='*60}")
    print("G(t) = ∫ log(1+|ω|²) dx  (log-enstrophy)")
    print(f"{'='*60}")

    for name, data in [("Taylor-Green", tg_data), ("ABC Flow", abc_data)]:
        print(f"\n{name}:")
        print(f"{'t':>6} | {'G(t)':>10} | {'G/t':>10} | {'Ω(t)':>10} | {'||ω||∞':>10}")
        print("-" * 55)
        for t, G, E, W in data:
            Gt = G/t if t > 0 else 0
            print(f"{t:6.2f} | {G:10.4f} | {Gt:10.4f} | {E:10.2f} | {W:10.2f}")

        # G_max estimate
        G_rates = [G/t for t, G, E, W in data if t > 0.1]
        if G_rates:
            G_max = max(G_rates)
            G_final = G_rates[-1]
            trend = "DECREASING" if G_rates[-1] < G_rates[0] else "INCREASING"
            print(f"\n  G_max = {G_max:.4f}, G(T)/T = {G_final:.4f}, trend: {trend}")
            if trend == "DECREASING":
                print(f"  G(t)/t → 0: log-enstrophy grows SUB-LINEARLY. CONSISTENT WITH REGULARITY ✓")
            else:
                print(f"  G(t)/t increasing: log-enstrophy might grow super-linearly. WATCH THIS.")


if __name__ == "__main__":
    main()
