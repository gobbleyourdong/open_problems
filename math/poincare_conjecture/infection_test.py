"""
Infection test: Can a growing pixel infect its neighbors through Biot-Savart?

For each high-growth pixel found by the cracker:
1. Identify the growing point (max Γ location)
2. Perturb: amplify vorticity at that point
3. One Poisson solve: compute the NEW velocity field
4. Evaluate Γ at ALL neighboring points
5. Count: how many neighbors flipped from decaying to growing?

If infection ratio > 1 (each growing point creates >1 new growing points) → cascade
If infection ratio < 1 → quarantine → regularity

This is the R0 of the singularity. R0 > 1 = pandemic = blowup. R0 < 1 = dies out.
"""
import torch
import math
import time
import json
import os


class InfectionTest:
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
        """Generate random smooth div-free vorticity field."""
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

    def compute_gamma_field(self, wx_hat, wy_hat, wz_hat):
        """Compute Γ at every point. Returns Γ field and component fields."""
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz

        # Biot-Savart
        px = wx_hat/self.ksq; py = wy_hat/self.ksq; pz = wz_hat/self.ksq
        px[0,0,0]=0; py[0,0,0]=0; pz[0,0,0]=0
        ux_hat = iky*pz - ikz*py
        uy_hat = ikz*px - ikx*pz
        uz_hat = ikx*py - iky*px

        ifft = lambda f: torch.fft.ifftn(f*D).real

        wx, wy, wz = ifft(wx_hat), ifft(wy_hat), ifft(wz_hat)

        # Strain: ω_i * ∂u_i/∂x_j * ω_j
        dux_dx=ifft(ikx*ux_hat*D); dux_dy=ifft(iky*ux_hat*D); dux_dz=ifft(ikz*ux_hat*D)
        duy_dx=ifft(ikx*uy_hat*D); duy_dy=ifft(iky*uy_hat*D); duy_dz=ifft(ikz*uy_hat*D)
        duz_dx=ifft(ikx*uz_hat*D); duz_dy=ifft(iky*uz_hat*D); duz_dz=ifft(ikz*uz_hat*D)

        stretch = (wx*(dux_dx*wx + dux_dy*wy + dux_dz*wz) +
                   wy*(duy_dx*wx + duy_dy*wy + duy_dz*wz) +
                   wz*(duz_dx*wx + duz_dy*wy + duz_dz*wz))

        # Dissipation
        dwx_dx=ifft(ikx*wx_hat*D); dwx_dy=ifft(iky*wx_hat*D); dwx_dz=ifft(ikz*wx_hat*D)
        dwy_dx=ifft(ikx*wy_hat*D); dwy_dy=ifft(iky*wy_hat*D); dwy_dz=ifft(ikz*wy_hat*D)
        dwz_dx=ifft(ikx*wz_hat*D); dwz_dy=ifft(iky*wz_hat*D); dwz_dz=ifft(ikz*wz_hat*D)

        grad_w_sq = (dwx_dx**2 + dwx_dy**2 + dwx_dz**2 +
                     dwy_dx**2 + dwy_dy**2 + dwy_dz**2 +
                     dwz_dx**2 + dwz_dy**2 + dwz_dz**2)

        S = stretch
        P = self.nu * grad_w_sq
        gamma = (S - P) / (S.abs() + P.abs() + 1e-30)
        w_sq = wx**2 + wy**2 + wz**2

        return gamma, w_sq, S, P

    def test_infection(self, seed, amp=10.0, boost_factor=2.0):
        """
        The core test:
        1. Generate field, find max-Γ point
        2. Boost vorticity at that point
        3. Recompute Γ everywhere
        4. Count new growing points in the neighborhood
        """
        wx_hat, wy_hat, wz_hat = self.generate_field(seed, amp)

        # Baseline Γ field
        gamma0, w_sq0, S0, P0 = self.compute_gamma_field(wx_hat, wy_hat, wz_hat)

        # Find max-Γ point (where stretching most dominates)
        # Only consider points with significant vorticity
        mask = w_sq0 > w_sq0.max() * 0.01
        gamma_masked = gamma0.clone()
        gamma_masked[~mask] = -1e10
        peak_idx = gamma_masked.argmax()
        pi, pj, pk = (peak_idx // (self.N*self.N),
                       (peak_idx % (self.N*self.N)) // self.N,
                       peak_idx % self.N)

        gamma_at_peak = gamma0[pi, pj, pk].item()

        # Count growing neighbors BEFORE boost
        # Neighborhood: 3x3x3 cube around peak (26 neighbors)
        neighbors_before = 0
        neighbors_total = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    if di == 0 and dj == 0 and dk == 0:
                        continue
                    ni = (pi + di) % self.N
                    nj = (pj + dj) % self.N
                    nk = (pk + dk) % self.N
                    neighbors_total += 1
                    if gamma0[ni, nj, nk] > 0:
                        neighbors_before += 1

        # Boost vorticity at peak point
        wx = torch.fft.ifftn(wx_hat).real
        wy = torch.fft.ifftn(wy_hat).real
        wz = torch.fft.ifftn(wz_hat).real

        # Gaussian boost centered at peak
        N = self.N
        x = torch.arange(N, device=self.device, dtype=torch.float64)
        X, Y, Z = torch.meshgrid(x, x, x, indexing='ij')

        # Periodic distance
        dx = (X - pi.float()).remainder(N)
        dx = torch.min(dx, N - dx)
        dy = (Y - pj.float()).remainder(N)
        dy = torch.min(dy, N - dy)
        dz = (Z - pk.float()).remainder(N)
        dz = torch.min(dz, N - dz)
        dist_sq = dx**2 + dy**2 + dz**2

        boost = (boost_factor - 1) * torch.exp(-dist_sq / 2.0)  # sigma = 1 grid cell

        wx_boosted = wx * (1 + boost)
        wy_boosted = wy * (1 + boost)
        wz_boosted = wz * (1 + boost)

        wx_hat_b = self.dealias * torch.fft.fftn(wx_boosted)
        wy_hat_b = self.dealias * torch.fft.fftn(wy_boosted)
        wz_hat_b = self.dealias * torch.fft.fftn(wz_boosted)

        # Recompute Γ with boosted field
        gamma1, w_sq1, S1, P1 = self.compute_gamma_field(wx_hat_b, wy_hat_b, wz_hat_b)

        # Count growing neighbors AFTER boost
        neighbors_after = 0
        flipped_positive = 0
        flipped_negative = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    if di == 0 and dj == 0 and dk == 0:
                        continue
                    ni = (pi + di) % self.N
                    nj = (pj + dj) % self.N
                    nk = (pk + dk) % self.N
                    if gamma1[ni, nj, nk] > 0:
                        neighbors_after += 1
                    # Track flips
                    was_positive = gamma0[ni, nj, nk] > 0
                    now_positive = gamma1[ni, nj, nk] > 0
                    if not was_positive and now_positive:
                        flipped_positive += 1
                    if was_positive and not now_positive:
                        flipped_negative += 1

        # Extended neighborhood: 5x5x5 (124 neighbors)
        ext_before = 0
        ext_after = 0
        ext_flipped_pos = 0
        ext_total = 0
        for di in range(-2, 3):
            for dj in range(-2, 3):
                for dk in range(-2, 3):
                    if di == 0 and dj == 0 and dk == 0:
                        continue
                    ni = (pi + di) % self.N
                    nj = (pj + dj) % self.N
                    nk = (pk + dk) % self.N
                    ext_total += 1
                    if gamma0[ni, nj, nk] > 0:
                        ext_before += 1
                    if gamma1[ni, nj, nk] > 0:
                        ext_after += 1
                    if gamma0[ni, nj, nk] <= 0 and gamma1[ni, nj, nk] > 0:
                        ext_flipped_pos += 1

        # R0: infection ratio
        # How many NEW growing points did the boost create?
        R0_near = flipped_positive  # out of 26 neighbors
        R0_ext = ext_flipped_pos   # out of 124 neighbors

        return {
            'seed': seed,
            'gamma_peak': gamma_at_peak,
            'peak_loc': (int(pi), int(pj), int(pk)),
            'neighbors_before': neighbors_before,
            'neighbors_after': neighbors_after,
            'flipped_positive': flipped_positive,
            'flipped_negative': flipped_negative,
            'R0_near': R0_near,
            'R0_ext': R0_ext,
            'ext_before': ext_before,
            'ext_after': ext_after,
        }


def main():
    N = 32
    nu = 1e-4
    device = 'cuda'
    n_samples = 10000

    tester = InfectionTest(N=N, nu=nu, device=device)

    print(f"INFECTION TEST: N={N}³, ν={nu:.0e}, {n_samples} samples")
    print(f"Question: does boosting a growing point infect its neighbors?")
    print(f"R0 > 1 = cascade. R0 < 1 = quarantine.")
    print(flush=True)

    results = []
    R0_near_list = []
    R0_ext_list = []
    t0 = time.time()

    for i in range(n_samples):
        seed = i
        amp = 10.0 * (1 + i % 5)

        result = tester.test_infection(seed, amp, boost_factor=2.0)
        results.append(result)
        R0_near_list.append(result['R0_near'])
        R0_ext_list.append(result['R0_ext'])

        if (i + 1) % 1000 == 0:
            elapsed = time.time() - t0
            R0n = torch.tensor(R0_near_list, dtype=torch.float64)
            R0e = torch.tensor(R0_ext_list, dtype=torch.float64)
            print(f"  [{i+1}/{n_samples}] {(i+1)/elapsed:.0f}/s | "
                  f"R0_near: mean={R0n.mean():.2f} max={R0n.max():.0f} | "
                  f"R0_ext: mean={R0e.mean():.2f} max={R0e.max():.0f} | "
                  f"[{elapsed:.0f}s]", flush=True)

    elapsed = time.time() - t0
    R0n = torch.tensor(R0_near_list, dtype=torch.float64)
    R0e = torch.tensor(R0_ext_list, dtype=torch.float64)

    print(f"\n{'='*60}")
    print(f"INFECTION RESULTS (ν={nu:.0e})")
    print(f"{'='*60}")
    print(f"Samples: {n_samples} in {elapsed:.0f}s ({n_samples/elapsed:.0f}/s)")
    print(f"\nNear neighborhood (26 neighbors):")
    print(f"  R0 mean: {R0n.mean():.4f}")
    print(f"  R0 max:  {R0n.max():.0f}")
    print(f"  R0 > 0:  {(R0n > 0).sum().item()}/{n_samples} ({100*(R0n>0).float().mean():.1f}%)")
    print(f"  R0 > 1:  {(R0n > 1).sum().item()}/{n_samples} ({100*(R0n>1).float().mean():.1f}%)")

    print(f"\nExtended neighborhood (124 neighbors):")
    print(f"  R0 mean: {R0e.mean():.4f}")
    print(f"  R0 max:  {R0e.max():.0f}")
    print(f"  R0 > 0:  {(R0e > 0).sum().item()}/{n_samples} ({100*(R0e>0).float().mean():.1f}%)")
    print(f"  R0 > 5:  {(R0e > 5).sum().item()}/{n_samples} ({100*(R0e>5).float().mean():.1f}%)")

    # Net infection: did the total number of growing neighbors increase?
    net_infections = []
    for r in results:
        net = r['neighbors_after'] - r['neighbors_before']
        net_infections.append(net)
    net = torch.tensor(net_infections, dtype=torch.float64)

    print(f"\nNet infection (near, after - before):")
    print(f"  Mean: {net.mean():.4f}")
    print(f"  Positive (growth spreads): {(net > 0).sum().item()}/{n_samples} ({100*(net>0).float().mean():.1f}%)")
    print(f"  Negative (growth contained): {(net < 0).sum().item()}/{n_samples} ({100*(net<0).float().mean():.1f}%)")
    print(f"  Zero (unchanged): {(net == 0).sum().item()}/{n_samples}")

    if R0n.mean() < 1:
        print(f"\n*** R0 < 1: QUARANTINE. Growth cannot sustain cascade. ***")
        print(f"*** The Biot-Savart coupling DEFOCUSES stretching. ***")
        print(f"*** This is regularity evidence. ***")
    else:
        print(f"\n*** R0 >= 1: CASCADE POSSIBLE. Growth can spread. ***")
        print(f"*** Blowup candidates exist. ***")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    summary = {
        'N': N, 'nu': nu, 'n_samples': n_samples,
        'R0_near_mean': R0n.mean().item(),
        'R0_near_max': R0n.max().item(),
        'R0_ext_mean': R0e.mean().item(),
        'R0_ext_max': R0e.max().item(),
        'net_infection_mean': net.mean().item(),
        'frac_net_positive': (net > 0).float().mean().item(),
    }
    with open(os.path.join(out_dir, f'infection_N{N}_nu{nu:.0e}.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved: infection_N{N}_nu{nu:.0e}.json", flush=True)


if __name__ == '__main__':
    main()
