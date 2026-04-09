"""
Domino search: 16³ grid, thousands of ICs, measure enstrophy growth.

The test: does energy amplify across one periodic cell?
Growth ratio > 1 = the domino flips two = blowup candidate.
Growth ratio < 1 = viscosity wins = regularity.

Sweep random curl noise seeds at various parameters.
Rank by peak enstrophy growth rate.
"""
import torch
import math
import time
import json
import os


class NS3DFast:
    """Minimal 3D NS solver optimized for speed at small N."""

    def __init__(self, N=16, nu=1e-4, device='cuda'):
        self.N = N
        self.nu = nu
        self.device = device
        self.dtype = torch.float64

        Lx = 2 * math.pi
        self.Lx = Lx
        dx = Lx / N
        self.dx = dx

        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=self.dtype)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0

        kmax = N // 3
        self.dealias = ((self.kx.abs() < kmax) &
                        (self.ky.abs() < kmax) &
                        (self.kz.abs() < kmax)).to(self.dtype)

        # Precompute 1j * k for derivatives
        self.ikx = 1j * self.kx
        self.iky = 1j * self.ky
        self.ikz = 1j * self.kz

        # Grid for IC construction
        x = torch.linspace(0, Lx - dx, N, device=device, dtype=self.dtype)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')

    def rhs(self, wx_hat, wy_hat, wz_hat):
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz

        # Biot-Savart: psi = w / |k|², u = curl(psi)
        px = wx_hat / self.ksq
        py = wy_hat / self.ksq
        pz = wz_hat / self.ksq
        px[0,0,0] = 0; py[0,0,0] = 0; pz[0,0,0] = 0

        ux_hat = iky*pz - ikz*py
        uy_hat = ikz*px - ikx*pz
        uz_hat = ikx*py - iky*px

        # To physical (dealiased)
        ifft = lambda f: torch.fft.ifftn(f * D).real
        ux, uy, uz = ifft(ux_hat), ifft(uy_hat), ifft(uz_hat)
        wx, wy, wz = ifft(wx_hat*D), ifft(wy_hat*D), ifft(wz_hat*D)

        # Velocity gradients
        dux_dx = ifft(ikx*ux_hat*D); dux_dy = ifft(iky*ux_hat*D); dux_dz = ifft(ikz*ux_hat*D)
        duy_dx = ifft(ikx*uy_hat*D); duy_dy = ifft(iky*uy_hat*D); duy_dz = ifft(ikz*uy_hat*D)
        duz_dx = ifft(ikx*uz_hat*D); duz_dy = ifft(iky*uz_hat*D); duz_dz = ifft(ikz*uz_hat*D)

        # Stretching (w·∇)u
        sx = wx*dux_dx + wy*dux_dy + wz*dux_dz
        sy = wx*duy_dx + wy*duy_dy + wz*duy_dz
        sz = wx*duz_dx + wy*duz_dy + wz*duz_dz

        # Advection (u·∇)w
        dwx_dx = ifft(ikx*wx_hat*D); dwx_dy = ifft(iky*wx_hat*D); dwx_dz = ifft(ikz*wx_hat*D)
        dwy_dx = ifft(ikx*wy_hat*D); dwy_dy = ifft(iky*wy_hat*D); dwy_dz = ifft(ikz*wy_hat*D)
        dwz_dx = ifft(ikx*wz_hat*D); dwz_dy = ifft(iky*wz_hat*D); dwz_dz = ifft(ikz*wz_hat*D)

        ax = ux*dwx_dx + uy*dwx_dy + uz*dwx_dz
        ay = ux*dwy_dx + uy*dwy_dy + uz*dwy_dz
        az = ux*dwz_dx + uy*dwz_dy + uz*dwz_dz

        # RHS = stretching - advection + viscous
        fft = torch.fft.fftn
        rx = D*fft(sx - ax) - self.nu*self.ksq*wx_hat
        ry = D*fft(sy - ay) - self.nu*self.ksq*wy_hat
        rz = D*fft(sz - az) - self.nu*self.ksq*wz_hat

        return rx, ry, rz

    def step(self, wx, wy, wz, dt):
        """RK4."""
        def add(a, b, s):
            return (a[0]+s*b[0], a[1]+s*b[1], a[2]+s*b[2])
        w = (wx, wy, wz)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w, k1, 0.5*dt))
        k3 = self.rhs(*add(w, k2, 0.5*dt))
        k4 = self.rhs(*add(w, k3, dt))
        return (wx + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                wy + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                wz + dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def enstrophy(self, wx_hat, wy_hat, wz_hat):
        wx = torch.fft.ifftn(wx_hat).real
        wy = torch.fft.ifftn(wy_hat).real
        wz = torch.fft.ifftn(wz_hat).real
        return (wx**2 + wy**2 + wz**2).mean().item()

    def omega_max(self, wx_hat, wy_hat, wz_hat):
        wx = torch.fft.ifftn(wx_hat).real
        wy = torch.fft.ifftn(wy_hat).real
        wz = torch.fft.ifftn(wz_hat).real
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()


def make_curl_noise_ic(solver, seed, amp=5.0, k_modes=None):
    """Vectorized curl noise IC from seed."""
    torch.manual_seed(seed)
    N = solver.N
    dev = solver.device

    # Random potential field — all modes at once
    mag = amp / (solver.ksq + 1)  # amplitude per mode
    mag[0,0,0] = 0

    # Mask to low modes only
    kmax = N // 2
    mask = solver.ksq <= kmax**2

    Ax = mag * mask * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
    Ay = mag * mask * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
    Az = mag * mask * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))

    # u = curl(A)
    ikx, iky, ikz = solver.ikx, solver.iky, solver.ikz
    ux_hat = iky*Az - ikz*Ay
    uy_hat = ikz*Ax - ikx*Az
    uz_hat = ikx*Ay - iky*Ax

    # w = curl(u)
    wx_hat = iky*uz_hat - ikz*uy_hat
    wy_hat = ikz*ux_hat - ikx*uz_hat
    wz_hat = ikx*uy_hat - iky*ux_hat

    return (solver.dealias*wx_hat, solver.dealias*wy_hat, solver.dealias*wz_hat)


def test_ic(solver, wx, wy, wz, n_steps=500, dt=0.005):
    """Run IC, return peak enstrophy growth ratio."""
    e0 = solver.enstrophy(wx, wy, wz)
    if e0 < 1e-20:
        return 0.0, 0.0, 0.0

    e_max = e0
    om_max = solver.omega_max(wx, wy, wz)

    for step in range(n_steps):
        wx, wy, wz = solver.step(wx, wy, wz, dt)
        if step % 50 == 0:
            e = solver.enstrophy(wx, wy, wz)
            om = solver.omega_max(wx, wy, wz)
            e_max = max(e_max, e)
            om_max = max(om_max, om)
            if om > 1e6:
                return e_max / e0, om_max, e_max

    e_final = solver.enstrophy(wx, wy, wz)
    return e_max / e0, om_max, e_final / e0


def main():
    N = 16
    device = 'cuda'
    n_seeds = 1000
    n_steps = 500
    dt = 0.005

    # Sweep over nu values
    nu_values = [1e-3, 1e-4, 1e-5, 0]

    for nu in nu_values:
        solver = NS3DFast(N=N, nu=nu, device=device)

        print(f"\n{'='*60}")
        print(f"DOMINO SEARCH: N={N}³, ν={nu:.1e}, {n_seeds} seeds")
        print(f"{'='*60}")

        results = []
        t0 = time.time()

        for seed in range(n_seeds):
            # Vary amplitude too
            amp = 5.0 * (1 + (seed % 10))  # 5 to 50

            wx, wy, wz = make_curl_noise_ic(solver, seed, amp=amp)
            growth, om_peak, e_ratio = test_ic(solver, wx, wy, wz, n_steps, dt)

            results.append({
                'seed': seed, 'amp': amp,
                'growth': growth, 'om_peak': om_peak, 'e_ratio': e_ratio,
            })

            if (seed + 1) % 100 == 0:
                elapsed = time.time() - t0
                tops = sorted(results, key=lambda r: r['growth'], reverse=True)[:3]
                top_str = ', '.join(f"s{r['seed']}:{r['growth']:.2f}×" for r in tops)
                print(f"  [{seed+1}/{n_seeds}] {elapsed:.0f}s | top: {top_str}", flush=True)

        elapsed = time.time() - t0

        # Sort by growth
        results.sort(key=lambda r: r['growth'], reverse=True)

        print(f"\nDone in {elapsed:.0f}s ({elapsed/n_seeds:.3f}s per IC)")
        print(f"\nTOP 20 ENSTROPHY AMPLIFIERS:")
        print(f"{'rank':>4} {'seed':>6} {'amp':>6} {'growth':>10} {'|ω|_peak':>10}")
        for i, r in enumerate(results[:20]):
            marker = ' ← BLOWUP?' if r['growth'] > 2.0 else ''
            print(f"{i+1:4d} {r['seed']:6d} {r['amp']:6.0f} {r['growth']:10.4f}× {r['om_peak']:10.2f}{marker}")

        # Count amplifiers
        n_amp = sum(1 for r in results if r['growth'] > 1.0)
        n_strong = sum(1 for r in results if r['growth'] > 2.0)
        print(f"\nGrowth > 1.0: {n_amp}/{n_seeds} ({100*n_amp/n_seeds:.1f}%)")
        print(f"Growth > 2.0: {n_strong}/{n_seeds} ({100*n_strong/n_seeds:.1f}%)")

        if n_strong > 0:
            print(f"\n*** STRONG AMPLIFIERS FOUND ***")
            print(f"These ICs show enstrophy MORE THAN DOUBLING.")
            print(f"Run at higher resolution to check if growth persists.")

        # Save
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"domino_N{N}_nu{nu:.0e}.json")
        with open(out_path, "w") as f:
            json.dump(results[:100], f, indent=2)  # save top 100
        print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
