"""
Multi-generation infection test: does R0 sustain across iterations?

Generation 0: Find growing points in random field
Generation 1: Boost growing points, recompute, find NEW growing points
Generation 2: Boost the new growing points, recompute again
...
Generation N: Does the infection still spread?

If R0 > 1 at every generation → sustained cascade → blowup
If R0 drops below 1 → burnout → regularity
"""
import torch
import math
import time
import json
import os


class GenerationalInfection:
    def __init__(self, N=32, nu=1e-4, device='cuda'):
        self.N = N
        self.nu = nu
        self.device = device

        Lx = 2 * math.pi
        dx = Lx / N
        self.dx = dx

        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0
        self.ikx = 1j * self.kx
        self.iky = 1j * self.ky
        self.ikz = 1j * self.kz

        kmax = N // 3
        self.dealias = ((self.kx.abs() < kmax) &
                        (self.ky.abs() < kmax) &
                        (self.kz.abs() < kmax)).to(torch.float64)
        self.k_mask = (self.ksq <= (N//2)**2).to(torch.float64)
        self.mag_template = 1.0 / (self.ksq + 1)
        self.mag_template[0, 0, 0] = 0

    def generate_field(self, seed, amp=10.0):
        torch.manual_seed(seed)
        N, dev, D = self.N, self.device, self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz
        mag = amp * self.mag_template * self.k_mask
        Ax = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Ay = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Az = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        ux_hat = iky*Az - ikz*Ay
        uy_hat = ikz*Ax - ikx*Az
        uz_hat = ikx*Ay - iky*Ax
        wx_hat = D*(iky*uz_hat - ikz*uy_hat)
        wy_hat = D*(ikz*ux_hat - ikx*uz_hat)
        wz_hat = D*(ikx*uy_hat - iky*ux_hat)
        return wx_hat, wy_hat, wz_hat

    def compute_growth_field(self, wx_hat, wy_hat, wz_hat):
        """Returns per-point growth rate: stretching - nu*dissipation."""
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz

        px = wx_hat/self.ksq; py = wy_hat/self.ksq; pz = wz_hat/self.ksq
        px[0,0,0]=0; py[0,0,0]=0; pz[0,0,0]=0
        ux_hat = iky*pz - ikz*py
        uy_hat = ikz*px - ikx*pz
        uz_hat = ikx*py - iky*px

        ifft = lambda f: torch.fft.ifftn(f*D).real
        wx, wy, wz = ifft(wx_hat), ifft(wy_hat), ifft(wz_hat)

        dux_dx=ifft(ikx*ux_hat*D); dux_dy=ifft(iky*ux_hat*D); dux_dz=ifft(ikz*ux_hat*D)
        duy_dx=ifft(ikx*uy_hat*D); duy_dy=ifft(iky*uy_hat*D); duy_dz=ifft(ikz*uy_hat*D)
        duz_dx=ifft(ikx*uz_hat*D); duz_dy=ifft(iky*uz_hat*D); duz_dz=ifft(ikz*uz_hat*D)

        stretch = (wx*(dux_dx*wx + dux_dy*wy + dux_dz*wz) +
                   wy*(duy_dx*wx + duy_dy*wy + duy_dz*wz) +
                   wz*(duz_dx*wx + duz_dy*wy + duz_dz*wz))

        dwx_dx=ifft(ikx*wx_hat*D); dwx_dy=ifft(iky*wx_hat*D); dwx_dz=ifft(ikz*wx_hat*D)
        dwy_dx=ifft(ikx*wy_hat*D); dwy_dy=ifft(iky*wy_hat*D); dwy_dz=ifft(ikz*wy_hat*D)
        dwz_dx=ifft(ikx*wz_hat*D); dwz_dy=ifft(iky*wz_hat*D); dwz_dz=ifft(ikz*wz_hat*D)

        grad_w_sq = (dwx_dx**2 + dwx_dy**2 + dwx_dz**2 +
                     dwy_dx**2 + dwy_dy**2 + dwy_dz**2 +
                     dwz_dx**2 + dwz_dy**2 + dwz_dz**2)

        w_sq = wx**2 + wy**2 + wz**2
        growth = stretch - self.nu * grad_w_sq

        return growth, w_sq

    def run_generations(self, seed, amp=10.0, n_generations=20, boost=1.5):
        """
        Run the infection across multiple generations.
        Each generation: boost growing points, recompute, count new growth.
        """
        wx_hat, wy_hat, wz_hat = self.generate_field(seed, amp)
        N = self.N

        gen_data = []

        for gen in range(n_generations):
            growth, w_sq = self.compute_growth_field(wx_hat, wy_hat, wz_hat)

            # Threshold: significant vorticity
            w_threshold = w_sq.max() * 0.01
            significant = w_sq > w_threshold

            # Count growing points
            growing = (growth > 0) & significant
            n_growing = growing.sum().item()
            n_significant = significant.sum().item()
            frac_growing = n_growing / (n_significant + 1)

            # Max growth rate
            growth_masked = growth.clone()
            growth_masked[~significant] = -1e30
            max_growth = growth_masked.max().item()

            # Total enstrophy and its rate
            total_enstrophy = w_sq[significant].sum().item()
            total_growth = growth[significant].sum().item()
            net_rate = total_growth / (total_enstrophy + 1e-30)

            gen_data.append({
                'gen': gen,
                'n_growing': n_growing,
                'n_significant': n_significant,
                'frac_growing': frac_growing,
                'max_growth': max_growth,
                'total_enstrophy': total_enstrophy,
                'net_rate': net_rate,
            })

            # Boost growing points for next generation
            wx = torch.fft.ifftn(wx_hat).real
            wy = torch.fft.ifftn(wy_hat).real
            wz = torch.fft.ifftn(wz_hat).real

            boost_mask = growing.float()
            # Smooth the boost slightly to keep spectral clean
            boost_hat = torch.fft.fftn(boost_mask)
            boost_smooth = torch.fft.ifftn(boost_hat * self.dealias).real.clamp(min=0)
            boost_smooth = boost_smooth / (boost_smooth.max() + 1e-30)

            factor = 1.0 + (boost - 1.0) * boost_smooth
            wx = wx * factor
            wy = wy * factor
            wz = wz * factor

            wx_hat = self.dealias * torch.fft.fftn(wx)
            wy_hat = self.dealias * torch.fft.fftn(wy)
            wz_hat = self.dealias * torch.fft.fftn(wz)

        return gen_data


def main():
    N = 32
    device = 'cuda'
    n_seeds = 1000
    n_generations = 20

    for nu in [1e-4, 1e-3]:
        tester = GenerationalInfection(N=N, nu=nu, device=device)

        print(f"\n{'='*60}")
        print(f"GENERATIONAL INFECTION: N={N}³, ν={nu:.0e}")
        print(f"{n_seeds} fields × {n_generations} generations")
        print(f"{'='*60}", flush=True)

        # Track R0 per generation across all seeds
        gen_frac_growing = [[] for _ in range(n_generations)]
        gen_net_rate = [[] for _ in range(n_generations)]
        gen_max_growth = [[] for _ in range(n_generations)]

        t0 = time.time()

        for seed in range(n_seeds):
            amp = 10.0 * (1 + seed % 5)
            data = tester.run_generations(seed, amp, n_generations, boost=1.5)

            for g in range(n_generations):
                gen_frac_growing[g].append(data[g]['frac_growing'])
                gen_net_rate[g].append(data[g]['net_rate'])
                gen_max_growth[g].append(data[g]['max_growth'])

            if (seed + 1) % 200 == 0:
                elapsed = time.time() - t0
                # Show generation trajectory for latest batch
                traj = ' '.join(f'{data[g]["frac_growing"]:.2f}' for g in [0, 4, 9, 14, 19])
                print(f'  [{seed+1}/{n_seeds}] {(seed+1)/elapsed:.0f}/s | '
                      f'frac_growing @gen 0,4,9,14,19: {traj} [{elapsed:.0f}s]', flush=True)

        elapsed = time.time() - t0

        print(f'\nGENERATION TRAJECTORY (mean over {n_seeds} seeds):')
        print(f'{"gen":>4} {"frac_growing":>14} {"net_rate":>12} {"max_growth":>12} {"trend":>8}')

        prev_frac = None
        for g in range(n_generations):
            fg = torch.tensor(gen_frac_growing[g]).mean().item()
            nr = torch.tensor(gen_net_rate[g]).mean().item()
            mg = torch.tensor(gen_max_growth[g]).mean().item()
            trend = ''
            if prev_frac is not None:
                if fg > prev_frac * 1.01:
                    trend = '↑'
                elif fg < prev_frac * 0.99:
                    trend = '↓'
                else:
                    trend = '→'
            prev_frac = fg
            print(f'{g:4d} {fg:14.4f} {nr:12.6f} {mg:12.6f} {trend:>8}')

        # Key metric: does frac_growing increase or decrease across generations?
        fg_first = torch.tensor(gen_frac_growing[0]).mean().item()
        fg_last = torch.tensor(gen_frac_growing[-1]).mean().item()

        print(f'\nfrac_growing: gen 0 = {fg_first:.4f} → gen {n_generations-1} = {fg_last:.4f}')
        if fg_last > fg_first:
            print(f'*** GROWTH SPREADS across generations! Infection SUSTAINS. ***')
            print(f'*** This is CASCADE behavior → evidence for BLOWUP ***')
        elif fg_last > fg_first * 0.5:
            print(f'*** Growth persists but doesn\'t accelerate. MARGINAL. ***')
        else:
            print(f'*** Growth decays across generations. Infection BURNS OUT. ***')
            print(f'*** This is QUARANTINE behavior → evidence for REGULARITY ***')

        # Save
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        summary = {
            'N': N, 'nu': nu, 'n_seeds': n_seeds, 'n_generations': n_generations,
            'frac_growing_gen0': fg_first,
            'frac_growing_final': fg_last,
            'trajectory': [torch.tensor(gen_frac_growing[g]).mean().item()
                          for g in range(n_generations)],
        }
        with open(os.path.join(out_dir, f'infection_gen_N{N}_nu{nu:.0e}.json'), 'w') as f:
            json.dump(summary, f, indent=2)
        print(f'Saved: infection_gen_N{N}_nu{nu:.0e}.json', flush=True)


if __name__ == '__main__':
    main()
