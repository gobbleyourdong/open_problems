"""
Full 3D Navier-Stokes solver — pseudospectral on periodic domain.

No axisymmetric restriction. Full 3D. Spectral accuracy via FFT.
Designed for the Spark GB10 (128GB unified memory).

Method:
  - Velocity-vorticity formulation
  - FFT-based Poisson solver (3 lines)
  - Dealiased pseudospectral for nonlinear terms (2/3 rule)
  - RK4 time stepping
  - Adaptive CFL

Grid: N³ periodic domain [0, 2π]³
At N=256: 16.7M points, ~1.3GB for all fields. Trivial for Spark.
"""
import torch
import numpy as np
import math
import time
import json
import os


class NS3DSpectral:
    """Full 3D incompressible Navier-Stokes, pseudospectral."""

    def __init__(self, N=128, nu=1e-4, Lx=2*math.pi, device='cuda', dtype=torch.float64):
        self.N = N
        self.nu = nu
        self.Lx = Lx
        self.device = device
        self.dtype = dtype

        # Physical grid
        dx = Lx / N
        x = torch.linspace(0, Lx - dx, N, device=device, dtype=dtype)
        self.x = x
        self.dx = dx
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')

        # Wavenumbers
        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=dtype)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')

        # |k|² for Poisson (avoid division by zero at k=0)
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0  # prevent div by zero; k=0 mode set to 0 anyway

        # Dealiasing mask (2/3 rule)
        kmax = N // 3
        self.dealias = ((self.kx.abs() < kmax) &
                        (self.ky.abs() < kmax) &
                        (self.kz.abs() < kmax)).to(dtype)

        # Viscous integrating factor for each mode: exp(-nu*|k|²*dt)
        # Precomputed per timestep in step()

        print(f"NS3D: N={N}, nu={nu}, L={Lx:.4f}, device={device}")
        print(f"  Grid: {N}³ = {N**3:,} points")
        print(f"  Memory per field: {N**3 * 8 / 1e6:.1f} MB")
        print(f"  Dealiased modes: {int(self.dealias.sum()):,} / {N**3:,}")

    def fft(self, f):
        return torch.fft.fftn(f)

    def ifft(self, f_hat):
        return torch.fft.ifftn(f_hat).real

    def dealias_field(self, f_hat):
        return f_hat * self.dealias

    def curl(self, ux_hat, uy_hat, uz_hat):
        """Compute curl in Fourier space: ω = ∇ × u"""
        # ω_x = ∂u_z/∂y - ∂u_y/∂z
        # ω_y = ∂u_x/∂z - ∂u_z/∂x
        # ω_z = ∂u_y/∂x - ∂u_x/∂y
        I = 1j
        wx_hat = I * self.ky * uz_hat - I * self.kz * uy_hat
        wy_hat = I * self.kz * ux_hat - I * self.kx * uz_hat
        wz_hat = I * self.kx * uy_hat - I * self.ky * ux_hat
        return wx_hat, wy_hat, wz_hat

    def velocity_from_vorticity(self, wx_hat, wy_hat, wz_hat):
        """
        Biot-Savart in Fourier space.
        u = curl(ψ), where -Δψ = ω → ψ_hat = ω_hat / |k|²
        Then u_hat = ik × ψ_hat
        """
        # Stream function (vector)
        psi_x_hat = wx_hat / self.ksq
        psi_y_hat = wy_hat / self.ksq
        psi_z_hat = wz_hat / self.ksq

        # Zero the mean (k=0)
        psi_x_hat[0, 0, 0] = 0
        psi_y_hat[0, 0, 0] = 0
        psi_z_hat[0, 0, 0] = 0

        # u = curl(psi)
        I = 1j
        ux_hat = I * self.ky * psi_z_hat - I * self.kz * psi_y_hat
        uy_hat = I * self.kz * psi_x_hat - I * self.kx * psi_z_hat
        uz_hat = I * self.kx * psi_y_hat - I * self.ky * psi_x_hat

        return ux_hat, uy_hat, uz_hat

    def rhs_vorticity(self, wx_hat, wy_hat, wz_hat):
        """
        Compute dω/dt = (ω·∇)u - (u·∇)ω + ν·Δω

        In Fourier: viscous term is just -ν|k|²ω_hat
        Nonlinear terms computed in physical space (dealiased).
        """
        # Get velocity from vorticity (Biot-Savart)
        ux_hat, uy_hat, uz_hat = self.velocity_from_vorticity(wx_hat, wy_hat, wz_hat)

        # To physical space (dealiased)
        ux = self.ifft(self.dealias_field(ux_hat))
        uy = self.ifft(self.dealias_field(uy_hat))
        uz = self.ifft(self.dealias_field(uz_hat))
        wx = self.ifft(self.dealias_field(wx_hat))
        wy = self.ifft(self.dealias_field(wy_hat))
        wz = self.ifft(self.dealias_field(wz_hat))

        # Velocity gradients for stretching term (ω·∇)u
        dux_dx = self.ifft(1j * self.kx * self.dealias_field(ux_hat))
        dux_dy = self.ifft(1j * self.ky * self.dealias_field(ux_hat))
        dux_dz = self.ifft(1j * self.kz * self.dealias_field(ux_hat))
        duy_dx = self.ifft(1j * self.kx * self.dealias_field(uy_hat))
        duy_dy = self.ifft(1j * self.ky * self.dealias_field(uy_hat))
        duy_dz = self.ifft(1j * self.kz * self.dealias_field(uy_hat))
        duz_dx = self.ifft(1j * self.kx * self.dealias_field(uz_hat))
        duz_dy = self.ifft(1j * self.ky * self.dealias_field(uz_hat))
        duz_dz = self.ifft(1j * self.kz * self.dealias_field(uz_hat))

        # Stretching: (ω·∇)u
        stretch_x = wx * dux_dx + wy * dux_dy + wz * dux_dz
        stretch_y = wx * duy_dx + wy * duy_dy + wz * duy_dz
        stretch_z = wx * duz_dx + wy * duz_dy + wz * duz_dz

        # Advection: (u·∇)ω
        dwx_dx = self.ifft(1j * self.kx * self.dealias_field(wx_hat))
        dwx_dy = self.ifft(1j * self.ky * self.dealias_field(wx_hat))
        dwx_dz = self.ifft(1j * self.kz * self.dealias_field(wx_hat))
        dwy_dx = self.ifft(1j * self.kx * self.dealias_field(wy_hat))
        dwy_dy = self.ifft(1j * self.ky * self.dealias_field(wy_hat))
        dwy_dz = self.ifft(1j * self.kz * self.dealias_field(wy_hat))
        dwz_dx = self.ifft(1j * self.kx * self.dealias_field(wz_hat))
        dwz_dy = self.ifft(1j * self.ky * self.dealias_field(wz_hat))
        dwz_dz = self.ifft(1j * self.kz * self.dealias_field(wz_hat))

        advect_x = ux * dwx_dx + uy * dwx_dy + uz * dwx_dz
        advect_y = ux * dwy_dx + uy * dwy_dy + uz * dwy_dz
        advect_z = ux * dwz_dx + uy * dwz_dy + uz * dwz_dz

        # Nonlinear RHS in physical space
        nl_x = stretch_x - advect_x
        nl_y = stretch_y - advect_y
        nl_z = stretch_z - advect_z

        # Back to Fourier and add viscous term
        rhs_x = self.dealias_field(self.fft(nl_x)) - self.nu * self.ksq * wx_hat
        rhs_y = self.dealias_field(self.fft(nl_y)) - self.nu * self.ksq * wy_hat
        rhs_z = self.dealias_field(self.fft(nl_z)) - self.nu * self.ksq * wz_hat

        return rhs_x, rhs_y, rhs_z

    def step_rk4(self, wx_hat, wy_hat, wz_hat, dt):
        """RK4 timestep in Fourier space."""
        def pack(a, b, c):
            return (a, b, c)
        def add(s1, s2, alpha):
            return (s1[0] + alpha*s2[0], s1[1] + alpha*s2[1], s1[2] + alpha*s2[2])

        w = pack(wx_hat, wy_hat, wz_hat)

        k1 = self.rhs_vorticity(*w)
        k2 = self.rhs_vorticity(*add(w, k1, 0.5*dt))
        k3 = self.rhs_vorticity(*add(w, k2, 0.5*dt))
        k4 = self.rhs_vorticity(*add(w, k3, dt))

        wx_hat = wx_hat + (dt/6) * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        wy_hat = wy_hat + (dt/6) * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        wz_hat = wz_hat + (dt/6) * (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])

        # Dealias
        wx_hat = self.dealias_field(wx_hat)
        wy_hat = self.dealias_field(wy_hat)
        wz_hat = self.dealias_field(wz_hat)

        return wx_hat, wy_hat, wz_hat

    def compute_dt(self, wx_hat, wy_hat, wz_hat):
        """Adaptive CFL timestep."""
        ux_hat, uy_hat, uz_hat = self.velocity_from_vorticity(wx_hat, wy_hat, wz_hat)
        ux = self.ifft(ux_hat)
        uy = self.ifft(uy_hat)
        uz = self.ifft(uz_hat)

        u_max = max(ux.abs().max().item(), uy.abs().max().item(), uz.abs().max().item())
        if u_max < 1e-10:
            return 1e-3

        dt_adv = 0.5 * self.dx / u_max
        dt_visc = 0.5 * self.dx**2 / (self.nu + 1e-30)
        return min(dt_adv, dt_visc, 0.01)

    def enstrophy(self, wx_hat, wy_hat, wz_hat):
        """Total enstrophy: ∫|ω|²dx"""
        wx = self.ifft(wx_hat)
        wy = self.ifft(wy_hat)
        wz = self.ifft(wz_hat)
        return (wx**2 + wy**2 + wz**2).mean().item() * self.Lx**3

    def omega_max(self, wx_hat, wy_hat, wz_hat):
        """Maximum vorticity magnitude."""
        wx = self.ifft(wx_hat)
        wy = self.ifft(wy_hat)
        wz = self.ifft(wz_hat)
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()

    def spectral_ratio(self, wx_hat):
        """Check spectral resolution: ratio of high to low modes."""
        spectrum = wx_hat.abs()
        N = self.N
        # Average over shells
        low = spectrum[:N//4, :N//4, :N//4].mean().item()
        high = spectrum[N//4:N//2, N//4:N//2, N//4:N//2].mean().item()
        return high / (low + 1e-30)


# ============================================================
# Initial conditions
# ============================================================

def ic_taylor_green(solver):
    """Taylor-Green vortex — exact decaying solution, good for validation."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uy = -torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uz = torch.zeros_like(X)

    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)

    wx_hat, wy_hat, wz_hat = solver.curl(ux_hat, uy_hat, uz_hat)
    return wx_hat, wy_hat, wz_hat


def ic_kida_pelz(solver):
    """Kida-Pelz high-symmetry IC — historically tested for blowup."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.sin(X) * (torch.cos(3*Y) * torch.cos(Z) - torch.cos(Y) * torch.cos(3*Z))
    uy = torch.sin(Y) * (torch.cos(3*Z) * torch.cos(X) - torch.cos(Z) * torch.cos(3*X))
    uz = torch.sin(Z) * (torch.cos(3*X) * torch.cos(Y) - torch.cos(X) * torch.cos(3*Y))

    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)

    wx_hat, wy_hat, wz_hat = solver.curl(ux_hat, uy_hat, uz_hat)
    return wx_hat, wy_hat, wz_hat


def ic_colliding_rings(solver, R=0.8, sep=1.5, amp=5.0):
    """Two vortex rings approaching each other — classic blowup candidate."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)
    wz = torch.zeros_like(X)

    for sign in [+1, -1]:
        # Ring center
        z0 = pi + sign * sep
        # Distance from ring axis (z-axis) in the (x,y) plane
        rho = torch.sqrt((X - pi)**2 + (Y - pi)**2)
        # Distance from ring core
        core_dist = torch.sqrt((rho - R)**2 + (Z - z0)**2)
        # Gaussian vortex core
        sigma = 0.2
        strength = amp * torch.exp(-core_dist**2 / (2*sigma**2))

        # Vorticity direction: tangent to ring (azimuthal)
        theta_x = -(Y - pi) / (rho + 1e-10)
        theta_y = (X - pi) / (rho + 1e-10)

        wx += sign * strength * theta_x
        wy += sign * strength * theta_y

    wx_hat = solver.dealias_field(solver.fft(wx))
    wy_hat = solver.dealias_field(solver.fft(wy))
    wz_hat = solver.dealias_field(solver.fft(wz))

    return wx_hat, wy_hat, wz_hat


def ic_curl_noise(solver, amp=5.0, octaves=3, seed=None):
    """
    Curl noise IC — divergence-free by construction.
    Smooth potential field → curl → velocity → curl → vorticity.
    Each octave doubles the frequency and halves the amplitude (VFX convention).
    """
    if seed is not None:
        torch.manual_seed(seed)

    N = solver.N
    device = solver.device

    # Build a smooth random potential field A (vector) in Fourier space
    # Then u = curl(A) is automatically divergence-free
    Ax_hat = torch.zeros(N, N, N, device=device, dtype=torch.complex128)
    Ay_hat = torch.zeros_like(Ax_hat)
    Az_hat = torch.zeros_like(Ax_hat)

    for octave in range(octaves):
        freq = 2 ** octave  # 1, 2, 4, ...
        amplitude = amp / (2 ** octave)  # halve each octave
        k_lo = max(1, freq - 1)
        k_hi = freq * 2

        for i in range(-k_hi, k_hi + 1):
            for j in range(-k_hi, k_hi + 1):
                for k in range(-k_hi, k_hi + 1):
                    ksq = i*i + j*j + k*k
                    if ksq < k_lo**2 or ksq > k_hi**2:
                        continue
                    mag = amplitude / (ksq + 1)
                    ii, jj, kk = i % N, j % N, k % N
                    Ax_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(device).item()
                    Ay_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(device).item()
                    Az_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(device).item()

    # u = curl(A) — divergence-free by vector identity
    I = 1j
    ux_hat = I * solver.ky * Az_hat - I * solver.kz * Ay_hat
    uy_hat = I * solver.kz * Ax_hat - I * solver.kx * Az_hat
    uz_hat = I * solver.kx * Ay_hat - I * solver.ky * Ax_hat

    # ω = curl(u)
    wx_hat, wy_hat, wz_hat = solver.curl(ux_hat, uy_hat, uz_hat)
    wx_hat = solver.dealias_field(wx_hat)
    wy_hat = solver.dealias_field(wy_hat)
    wz_hat = solver.dealias_field(wz_hat)

    return wx_hat, wy_hat, wz_hat


def ic_trefoil_knot(solver, amp=10.0, core_width=0.3):
    """
    Trefoil knotted vortex tube — topologically nontrivial.
    A knotted vortex line can't untie without reconnection,
    which concentrates vorticity at the reconnection point.
    """
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)
    wz = torch.zeros_like(X)

    # Trefoil knot parametrized on [0, 2π]
    n_pts = 200
    s = torch.linspace(0, 2*pi, n_pts, device=solver.device, dtype=solver.dtype)

    # Trefoil: x = sin(s) + 2sin(2s), y = cos(s) - 2cos(2s), z = -sin(3s)
    cx = (torch.sin(s) + 2*torch.sin(2*s)) * 0.5 + pi
    cy = (torch.cos(s) - 2*torch.cos(2*s)) * 0.5 + pi
    cz = (-torch.sin(3*s)) * 0.5 + pi

    # Tangent vectors (unnormalized = vorticity direction × strength)
    ds = 2*pi / n_pts
    tx = torch.cos(s) + 4*torch.cos(2*s)
    ty = -torch.sin(s) + 4*torch.sin(2*s)
    tz = -3*torch.cos(3*s)

    # Deposit vorticity as Gaussian tubes along the knot
    sigma = core_width
    for i in range(n_pts):
        dist_sq = (X - cx[i])**2 + (Y - cy[i])**2 + (Z - cz[i])**2
        gaussian = amp * torch.exp(-dist_sq / (2*sigma**2)) * ds
        wx += gaussian * tx[i]
        wy += gaussian * ty[i]
        wz += gaussian * tz[i]

    wx_hat = solver.dealias_field(solver.fft(wx))
    wy_hat = solver.dealias_field(solver.fft(wy))
    wz_hat = solver.dealias_field(solver.fft(wz))

    return wx_hat, wy_hat, wz_hat


def ic_random_large_scale(solver, amp=2.0, k_max=4):
    """Random large-scale vorticity field."""
    torch.manual_seed(42)
    N = solver.N

    wx_hat = torch.zeros(N, N, N, device=solver.device, dtype=torch.complex128)
    wy_hat = torch.zeros_like(wx_hat)
    wz_hat = torch.zeros_like(wx_hat)

    # Random phases for low wavenumber modes
    for i in range(-k_max, k_max+1):
        for j in range(-k_max, k_max+1):
            for k in range(-k_max, k_max+1):
                if i == 0 and j == 0 and k == 0:
                    continue
                ksq = i*i + j*j + k*k
                if ksq > k_max**2:
                    continue
                mag = amp / ksq
                ii, jj, kk = i % N, j % N, k % N
                wx_hat[ii, jj, kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                wy_hat[ii, jj, kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                wz_hat[ii, jj, kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()

    # Project to divergence-free: ω_hat → ω_hat - k(k·ω_hat)/|k|²
    kdotw = solver.kx*wx_hat + solver.ky*wy_hat + solver.kz*wz_hat
    wx_hat -= solver.kx * kdotw / solver.ksq
    wy_hat -= solver.ky * kdotw / solver.ksq
    wz_hat -= solver.kz * kdotw / solver.ksq
    wx_hat[0,0,0] = 0; wy_hat[0,0,0] = 0; wz_hat[0,0,0] = 0

    return wx_hat, wy_hat, wz_hat


# ============================================================
# Main runner
# ============================================================

def run(N=128, nu=1e-4, ic_name='taylor_green', n_steps=10000, device='cuda'):
    solver = NS3DSpectral(N=N, nu=nu, device=device)

    ic_funcs = {
        'taylor_green': ic_taylor_green,
        'kida_pelz': ic_kida_pelz,
        'colliding_rings': ic_colliding_rings,
        'random': ic_random_large_scale,
        'curl_noise': ic_curl_noise,
        'trefoil': ic_trefoil_knot,
    }

    if ic_name not in ic_funcs:
        print(f"Unknown IC: {ic_name}. Available: {list(ic_funcs.keys())}")
        return

    wx_hat, wy_hat, wz_hat = ic_funcs[ic_name](solver)

    print(f"\nIC: {ic_name}")
    print(f"|ω|_max = {solver.omega_max(wx_hat, wy_hat, wz_hat):.4f}")
    print(f"Enstrophy = {solver.enstrophy(wx_hat, wy_hat, wz_hat):.4f}")

    dt = solver.compute_dt(wx_hat, wy_hat, wz_hat)
    t = 0.0
    t0 = time.time()
    results = []

    for step in range(n_steps + 1):
        if step % 200 == 0:
            om_max = solver.omega_max(wx_hat, wy_hat, wz_hat)
            enst = solver.enstrophy(wx_hat, wy_hat, wz_hat)
            spec = solver.spectral_ratio(wx_hat)
            elapsed = time.time() - t0
            status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")

            results.append({
                'step': step, 't': t, 'omega_max': om_max,
                'enstrophy': enst, 'spectral': spec, 'dt': dt,
            })

            if step % 1000 == 0:
                print(f"step={step:6d} t={t:.6f} |ω|={om_max:.4f} "
                      f"enst={enst:.4f} spec={spec:.4e} [{status}] "
                      f"dt={dt:.2e} [{elapsed:.0f}s]", flush=True)

            if om_max > 1e6:
                print(f"BLOWUP at step {step}")
                break
            if status == "UNDER":
                print(f"UNDER-RESOLVED at step {step}")
                break

        wx_hat, wy_hat, wz_hat = solver.step_rk4(wx_hat, wy_hat, wz_hat, dt)
        t += dt
        dt = solver.compute_dt(wx_hat, wy_hat, wz_hat)

    elapsed = time.time() - t0
    print(f"\nDone: {step} steps in {elapsed:.0f}s ({elapsed/max(step,1):.2f}s/step)")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"ns3d_{ic_name}_N{N}.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {out_path}")

    return solver, wx_hat, wy_hat, wz_hat, results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, default=128)
    parser.add_argument('--nu', type=float, default=1e-4)
    parser.add_argument('--ic', type=str, default='taylor_green')
    parser.add_argument('--steps', type=int, default=10000)
    parser.add_argument('--device', type=str, default='cuda')
    args = parser.parse_args()

    run(N=args.N, nu=args.nu, ic_name=args.ic, n_steps=args.steps, device=args.device)
