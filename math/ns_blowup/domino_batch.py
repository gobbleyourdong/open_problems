"""
Batched domino search: run MANY ICs simultaneously on GPU.
16³ per IC × batch_size ICs = one big tensor operation.
GPU does them all in parallel.
"""
import torch
import math
import time
import json
import os


class NS3DBatched:
    """Batched 3D NS — B ICs running simultaneously."""

    def __init__(self, N=16, nu=1e-4, batch=128, device='cuda'):
        self.N = N
        self.nu = nu
        self.B = batch
        self.device = device

        Lx = 2 * math.pi
        dx = Lx / N
        self.dx = dx

        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
        kx, ky, kz = torch.meshgrid(k, k, k, indexing='ij')

        # Expand for batch dimension: (1, N, N, N)
        self.kx = kx.unsqueeze(0)
        self.ky = ky.unsqueeze(0)
        self.kz = kz.unsqueeze(0)
        self.ksq = (kx**2 + ky**2 + kz**2).unsqueeze(0)
        self.ksq[:, 0, 0, 0] = 1.0

        kmax = N // 3
        self.dealias = ((kx.abs() < kmax) & (ky.abs() < kmax) & (kz.abs() < kmax)).to(torch.float64).unsqueeze(0)

        self.ikx = 1j * self.kx
        self.iky = 1j * self.ky
        self.ikz = 1j * self.kz

        mem_mb = batch * N**3 * 8 * 6 / 1e6  # 6 fields (wx,wy,wz + intermediates)
        print(f"NS3D Batched: N={N}³, batch={batch}, ν={nu:.1e}")
        print(f"  Total points: {batch * N**3:,}")
        print(f"  Est. memory: {mem_mb:.0f} MB")

    def rhs(self, wx, wy, wz):
        """Batched RHS. All tensors are (B, N, N, N)."""
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz
        ksq = self.ksq

        # Biot-Savart
        px = wx / ksq; py = wy / ksq; pz = wz / ksq
        px[:, 0, 0, 0] = 0; py[:, 0, 0, 0] = 0; pz[:, 0, 0, 0] = 0

        ux_h = iky*pz - ikz*py
        uy_h = ikz*px - ikx*pz
        uz_h = ikx*py - iky*px

        ifft = lambda f: torch.fft.ifftn(f * D, dim=(-3,-2,-1)).real
        fft = lambda f: torch.fft.fftn(f, dim=(-3,-2,-1))

        ux, uy, uz = ifft(ux_h), ifft(uy_h), ifft(uz_h)
        Wx, Wy, Wz = ifft(wx*D), ifft(wy*D), ifft(wz*D)

        # Velocity gradients (9 terms)
        dux_dx=ifft(ikx*ux_h*D); dux_dy=ifft(iky*ux_h*D); dux_dz=ifft(ikz*ux_h*D)
        duy_dx=ifft(ikx*uy_h*D); duy_dy=ifft(iky*uy_h*D); duy_dz=ifft(ikz*uy_h*D)
        duz_dx=ifft(ikx*uz_h*D); duz_dy=ifft(iky*uz_h*D); duz_dz=ifft(ikz*uz_h*D)

        # Stretching - advection
        nl_x = (Wx*dux_dx+Wy*dux_dy+Wz*dux_dz) - (ux*ifft(ikx*wx*D)+uy*ifft(iky*wx*D)+uz*ifft(ikz*wx*D))
        nl_y = (Wx*duy_dx+Wy*duy_dy+Wz*duy_dz) - (ux*ifft(ikx*wy*D)+uy*ifft(iky*wy*D)+uz*ifft(ikz*wy*D))
        nl_z = (Wx*duz_dx+Wy*duz_dy+Wz*duz_dz) - (ux*ifft(ikx*wz*D)+uy*ifft(iky*wz*D)+uz*ifft(ikz*wz*D))

        return (D*fft(nl_x) - self.nu*ksq*wx,
                D*fft(nl_y) - self.nu*ksq*wy,
                D*fft(nl_z) - self.nu*ksq*wz)

    def step(self, wx, wy, wz, dt):
        """RK4 on batch."""
        def add(a, b, s):
            return (a[0]+s*b[0], a[1]+s*b[1], a[2]+s*b[2])
        w = (wx, wy, wz)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w, k1, 0.5*dt))
        k3 = self.rhs(*add(w, k2, 0.5*dt))
        k4 = self.rhs(*add(w, k3, dt))
        return (wx+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                wy+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                wz+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def enstrophy_batch(self, wx, wy, wz):
        """Per-IC enstrophy. Returns (B,) tensor."""
        Wx = torch.fft.ifftn(wx, dim=(-3,-2,-1)).real
        Wy = torch.fft.ifftn(wy, dim=(-3,-2,-1)).real
        Wz = torch.fft.ifftn(wz, dim=(-3,-2,-1)).real
        return (Wx**2 + Wy**2 + Wz**2).mean(dim=(-3,-2,-1))

    def omega_max_batch(self, wx, wy, wz):
        """Per-IC max vorticity. Returns (B,) tensor."""
        Wx = torch.fft.ifftn(wx, dim=(-3,-2,-1)).real
        Wy = torch.fft.ifftn(wy, dim=(-3,-2,-1)).real
        Wz = torch.fft.ifftn(wz, dim=(-3,-2,-1)).real
        om = (Wx**2 + Wy**2 + Wz**2).sqrt()
        return om.reshape(self.B, -1).max(dim=1).values


def make_batch_ic(solver, start_seed, amp_base=5.0):
    """Generate a batch of random curl noise ICs."""
    B, N, dev = solver.B, solver.N, solver.device

    wx_all = torch.zeros(B, N, N, N, device=dev, dtype=torch.complex128)
    wy_all = torch.zeros_like(wx_all)
    wz_all = torch.zeros_like(wx_all)

    kmax = N // 2
    mask = (solver.ksq <= kmax**2)  # (1, N, N, N)

    for b in range(B):
        torch.manual_seed(start_seed + b)
        amp = amp_base * (1 + (start_seed + b) % 10)
        mag = amp / (solver.ksq[0] + 1)
        mag[0, 0, 0] = 0

        Ax = mag * mask[0] * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Ay = mag * mask[0] * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Az = mag * mask[0] * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))

        ikx, iky, ikz = solver.ikx[0], solver.iky[0], solver.ikz[0]
        ux = iky*Az - ikz*Ay
        uy = ikz*Ax - ikx*Az
        uz = ikx*Ay - iky*Ax
        wx_all[b] = iky*uz - ikz*uy
        wy_all[b] = ikz*ux - ikx*uz
        wz_all[b] = ikx*uy - iky*ux

    return wx_all * solver.dealias, wy_all * solver.dealias, wz_all * solver.dealias


def main():
    N = 16
    batch = 128  # 128 ICs simultaneously
    n_steps = 200
    dt = 0.005
    device = 'cuda'
    total_seeds = 1024  # 8 batches of 128

    for nu in [1e-3, 1e-4, 1e-5, 0]:
        solver = NS3DBatched(N=N, nu=nu, batch=batch, device=device)

        print(f"\n{'='*60}")
        print(f"ν={nu:.0e} — {total_seeds} ICs in batches of {batch}")
        print(f"{'='*60}", flush=True)

        all_results = []
        t0 = time.time()

        for batch_idx in range(total_seeds // batch):
            start_seed = batch_idx * batch

            # Generate batch
            wx, wy, wz = make_batch_ic(solver, start_seed)
            e0 = solver.enstrophy_batch(wx, wy, wz)

            # Track peak
            e_peak = e0.clone()
            om_peak = solver.omega_max_batch(wx, wy, wz)

            # Run
            for step in range(n_steps):
                wx, wy, wz = solver.step(wx, wy, wz, dt)
                if step % 20 == 0:
                    e = solver.enstrophy_batch(wx, wy, wz)
                    om = solver.omega_max_batch(wx, wy, wz)
                    e_peak = torch.max(e_peak, e)
                    om_peak = torch.max(om_peak, om)

            # Compute growth ratios
            growth = (e_peak / (e0 + 1e-30)).cpu().numpy()
            om_peaks = om_peak.cpu().numpy()

            for b in range(batch):
                all_results.append({
                    'seed': start_seed + b,
                    'growth': float(growth[b]),
                    'om_peak': float(om_peaks[b]),
                })

            elapsed = time.time() - t0
            batch_top = sorted(all_results, key=lambda r: r['growth'], reverse=True)[:3]
            top_str = ' '.join(f"s{r['seed']}:{r['growth']:.2f}×" for r in batch_top)
            print(f"  batch {batch_idx+1}/{total_seeds//batch} [{elapsed:.0f}s] top: {top_str}", flush=True)

        elapsed = time.time() - t0

        # Sort and report
        all_results.sort(key=lambda r: r['growth'], reverse=True)
        n_amp = sum(1 for r in all_results if r['growth'] > 1.0)
        n_strong = sum(1 for r in all_results if r['growth'] > 2.0)

        print(f"\nDone: {total_seeds} ICs in {elapsed:.0f}s ({elapsed/total_seeds*1000:.0f}ms/IC)")
        print(f"\nTOP 10:")
        for i, r in enumerate(all_results[:10]):
            print(f"  {i+1}. seed={r['seed']} growth={r['growth']:.4f}× |ω|peak={r['om_peak']:.2f}")
        print(f"\nGrowth > 1.0: {n_amp}/{total_seeds} ({100*n_amp/total_seeds:.1f}%)")
        print(f"Growth > 2.0: {n_strong}/{total_seeds} ({100*n_strong/total_seeds:.1f}%)")

        # Save
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"domino_batch_N{N}_nu{nu:.0e}.json")
        with open(out_path, "w") as f:
            json.dump(all_results[:100], f, indent=2)
        print(f"Saved: {out_path}", flush=True)


if __name__ == '__main__':
    main()
