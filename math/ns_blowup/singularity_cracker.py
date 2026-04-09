"""
Singularity cracker: brute force pointwise blowup test.

For each random vorticity field:
1. Generate random smooth ω (curl noise, one FFT)
2. Compute real velocity via Biot-Savart (one FFT)
3. Compute strain tensor S and vortex stretching ω·S·ω at every point
4. Compute diffusion ν|∇ω|² at every point
5. Check: does stretching beat diffusion ANYWHERE?

Score = max over all points of (stretching - diffusion) / |ω|²
If score > 0 at ANY point, that's a local growth site.
If score > threshold consistently, that's a blowup candidate.

One sample = 2 FFTs. Can do millions per hour at 32³.
"""
import torch
import math
import time
import json
import os


class SingularityCracker:
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

        # Precompute mask for IC generation
        self.k_mask = (self.ksq <= (N//2)**2).to(torch.float64)
        self.mag = 1.0 / (self.ksq + 1)
        self.mag[0, 0, 0] = 0

    def generate_and_test(self, seed, amp=10.0):
        """
        One complete test: generate ω, compute Biot-Savart, evaluate growth.
        Returns the maximum local growth rate across all points.
        """
        torch.manual_seed(seed)
        N = self.N
        dev = self.device
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz

        # Generate random smooth divergence-free ω via curl of potential
        mag = amp * self.mag * self.k_mask
        Ax = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Ay = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
        Az = mag * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))

        # u = curl(A), ω = curl(u)
        ux_hat = iky*Az - ikz*Ay
        uy_hat = ikz*Ax - ikx*Az
        uz_hat = ikx*Ay - iky*Ax
        wx_hat = D*(iky*uz_hat - ikz*uy_hat)
        wy_hat = D*(ikz*ux_hat - ikx*uz_hat)
        wz_hat = D*(ikx*uy_hat - iky*ux_hat)

        # Biot-Savart: get velocity from vorticity
        px = wx_hat/self.ksq; py = wy_hat/self.ksq; pz = wz_hat/self.ksq
        px[0,0,0]=0; py[0,0,0]=0; pz[0,0,0]=0
        ux_hat = iky*pz - ikz*py
        uy_hat = ikz*px - ikx*pz
        uz_hat = ikx*py - iky*px

        ifft = lambda f: torch.fft.ifftn(f*D).real

        # Physical fields
        wx, wy, wz = ifft(wx_hat), ifft(wy_hat), ifft(wz_hat)

        # Strain tensor S_ij = (∂u_i/∂x_j + ∂u_j/∂x_i) / 2
        dux_dx = ifft(ikx*ux_hat*D); dux_dy = ifft(iky*ux_hat*D); dux_dz = ifft(ikz*ux_hat*D)
        duy_dx = ifft(ikx*uy_hat*D); duy_dy = ifft(iky*uy_hat*D); duy_dz = ifft(ikz*uy_hat*D)
        duz_dx = ifft(ikx*uz_hat*D); duz_dy = ifft(iky*uz_hat*D); duz_dz = ifft(ikz*uz_hat*D)

        # ω·S·ω (vortex stretching rate)
        # S_ij * w_i * w_j = w_i * (∂u_i/∂x_j) * w_j  (symmetric part)
        # Actually: d|ω|²/dt from stretching = 2 * ω_i * S_ij * ω_j
        # where S_ij = (∂u_i/∂x_j + ∂u_j/∂x_i)/2
        # Simpler: stretching = ω_i * ∂u_i/∂x_j * ω_j (full tensor, not just symmetric)
        stretch = (wx * (dux_dx*wx + dux_dy*wy + dux_dz*wz) +
                   wy * (duy_dx*wx + duy_dy*wy + duy_dz*wz) +
                   wz * (duz_dx*wx + duz_dy*wy + duz_dz*wz))

        # |∇ω|² (dissipation)
        dwx_dx = ifft(ikx*wx_hat*D); dwx_dy = ifft(iky*wx_hat*D); dwx_dz = ifft(ikz*wx_hat*D)
        dwy_dx = ifft(ikx*wy_hat*D); dwy_dy = ifft(iky*wy_hat*D); dwy_dz = ifft(ikz*wy_hat*D)
        dwz_dx = ifft(ikx*wz_hat*D); dwz_dy = ifft(iky*wz_hat*D); dwz_dz = ifft(ikz*wz_hat*D)

        grad_w_sq = (dwx_dx**2 + dwx_dy**2 + dwx_dz**2 +
                     dwy_dx**2 + dwy_dy**2 + dwy_dz**2 +
                     dwz_dx**2 + dwz_dy**2 + dwz_dz**2)

        # Local growth rate: d|ω|²/dt = 2*stretch - 2*ν*grad_w_sq
        # Normalized by |ω|² to get relative rate
        w_sq = wx**2 + wy**2 + wz**2
        growth_rate = 2 * (stretch - self.nu * grad_w_sq)

        # Relative growth: where |ω| is significant
        mask = w_sq > w_sq.max() * 0.01  # ignore points with tiny vorticity
        if mask.sum() == 0:
            return 0, 0, 0, 0, 0

        relative_growth = growth_rate[mask] / (w_sq[mask] + 1e-30)

        # Gamma at every point: Γ = (S - νP) / (S + νP)
        S_local = stretch[mask]
        P_local = self.nu * grad_w_sq[mask]
        gamma_local = (S_local - P_local) / (S_local.abs() + P_local.abs() + 1e-30)

        # Stats
        max_growth = relative_growth.max().item()
        mean_growth = relative_growth.mean().item()
        max_gamma = gamma_local.max().item()
        mean_gamma = gamma_local.mean().item()
        frac_positive = (gamma_local > 0).float().mean().item()

        return max_growth, mean_growth, max_gamma, mean_gamma, frac_positive


def main():
    N = 32
    device = 'cuda'
    n_samples = 100000

    for nu in [1e-4, 1e-3, 1e-2]:
        cracker = SingularityCracker(N=N, nu=nu, device=device)

        print(f"\n{'='*60}")
        print(f"SINGULARITY CRACKER: N={N}³, ν={nu:.0e}, {n_samples} samples")
        print(f"{'='*60}", flush=True)

        max_growths = []
        max_gammas = []
        frac_positives = []
        best_seed = -1
        best_score = -1e30
        t0 = time.time()

        for seed in range(n_samples):
            amp = 10.0 * (1 + seed % 5)
            mg, mean_g, max_gam, mean_gam, frac_pos = cracker.generate_and_test(seed, amp)

            max_growths.append(mg)
            max_gammas.append(max_gam)
            frac_positives.append(frac_pos)

            if mg > best_score:
                best_score = mg
                best_seed = seed

            if (seed + 1) % 10000 == 0:
                elapsed = time.time() - t0
                rate = (seed + 1) / elapsed
                mg_arr = torch.tensor(max_growths)
                gam_arr = torch.tensor(max_gammas)
                fp_arr = torch.tensor(frac_positives)

                n_positive = (mg_arr > 0).sum().item()
                print(f"  [{seed+1}/{n_samples}] {rate:.0f}/s | "
                      f"growth>0: {n_positive}/{seed+1} ({100*n_positive/(seed+1):.1f}%) | "
                      f"best: s{best_seed} g={best_score:.4f} | "
                      f"mean_Γ={gam_arr.mean():.4f} frac_Γ>0={fp_arr.mean():.4f} "
                      f"[{elapsed:.0f}s]", flush=True)

        elapsed = time.time() - t0
        mg_arr = torch.tensor(max_growths)
        gam_arr = torch.tensor(max_gammas)
        fp_arr = torch.tensor(frac_positives)

        n_positive = (mg_arr > 0).sum().item()

        print(f"\nRESULTS (ν={nu:.0e}):")
        print(f"  Samples: {n_samples} in {elapsed:.0f}s ({n_samples/elapsed:.0f}/s)")
        print(f"  Local growth > 0: {n_positive}/{n_samples} ({100*n_positive/n_samples:.1f}%)")
        print(f"  Max growth rate: {mg_arr.max():.6f} (seed {best_seed})")
        print(f"  Mean max growth: {mg_arr.mean():.6f}")
        print(f"  Mean Γ_max: {gam_arr.mean():.4f}")
        print(f"  Mean frac(Γ>0): {fp_arr.mean():.4f}")

        if n_positive == 0:
            print(f"\n  *** NO LOCAL GROWTH FOUND IN {n_samples} SAMPLES ***")
            print(f"  Viscosity beats stretching at EVERY point in EVERY configuration.")
            print(f"  This is strong evidence for regularity at ν={nu:.0e}.")
        else:
            print(f"\n  {n_positive} configurations show local growth.")
            print(f"  Best candidate: seed {best_seed}")

        # Save
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        result = {
            'N': N, 'nu': nu, 'n_samples': n_samples,
            'n_positive': n_positive,
            'best_seed': best_seed, 'best_growth': best_score,
            'mean_max_growth': mg_arr.mean().item(),
            'mean_gamma_max': gam_arr.mean().item(),
            'mean_frac_positive': fp_arr.mean().item(),
            'rate_per_sec': n_samples / elapsed,
        }
        out_path = os.path.join(out_dir, f"cracker_N{N}_nu{nu:.0e}.json")
        with open(out_path, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"  Saved: {out_path}", flush=True)


if __name__ == '__main__':
    main()
