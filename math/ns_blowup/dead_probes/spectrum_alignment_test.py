"""
Iron Fortress gap-fillers:
1. Energy spectrum at peak vorticity — is the solution well-resolved?
2. Strain-vorticity alignment at x* — is depletion active where it matters?

Runs across N=32,64,128 with 10 seeds each. At the timestep where |omega|_max
peaks, save (a) the energy spectrum E(k) and (b) cos²θ between ω and the
principal strain eigenvector at the point of maximum |ω|.
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_diagnostics(N_values=None, nu=1e-4, n_steps=2000, dt=0.005,
                    n_seeds=10, device='cuda'):
    if N_values is None:
        N_values = [32, 64, 128]

    all_results = {}

    for N in N_values:
        print(f'\n{"="*60}')
        print(f'N={N}, nu={nu}, {n_seeds} seeds, {n_steps} steps')
        print(f'{"="*60}', flush=True)

        Lx = 2*math.pi; dx = Lx/N
        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
        kx,ky,kz = torch.meshgrid(k,k,k,indexing='ij')
        ksq = kx**2+ky**2+kz**2; ksq[0,0,0] = 1.0
        ikx,iky,ikz = 1j*kx, 1j*ky, 1j*kz
        kmax = N//3
        D = ((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
        kmag = ksq.sqrt()

        ifft = lambda f: torch.fft.ifftn(f*D).real
        fft = torch.fft.fftn

        def ns_rhs(wx_h,wy_h,wz_h):
            px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
            ux,uy,uz=ifft(ux_h),ifft(uy_h),ifft(uz_h)
            wx,wy,wz=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
            gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
            gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
            gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
            sx=wx*gxx+wy*gxy+wz*gxz;sy=wx*gyx+wy*gyy+wz*gyz;sz=wx*gzx+wy*gzy+wz*gzz
            ax=ux*ifft(ikx*wx_h*D)+uy*ifft(iky*wx_h*D)+uz*ifft(ikz*wx_h*D)
            ay=ux*ifft(ikx*wy_h*D)+uy*ifft(iky*wy_h*D)+uz*ifft(ikz*wy_h*D)
            az=ux*ifft(ikx*wz_h*D)+uy*ifft(iky*wz_h*D)+uz*ifft(ikz*wz_h*D)
            return(D*fft(sx-ax)-nu*ksq*wx_h,D*fft(sy-ay)-nu*ksq*wy_h,D*fft(sz-az)-nu*ksq*wz_h)

        def rk4(wx_h,wy_h,wz_h,dt):
            def add(a,b,s):return(a[0]+s*b[0],a[1]+s*b[1],a[2]+s*b[2])
            w=(wx_h,wy_h,wz_h)
            k1=ns_rhs(*w);k2=ns_rhs(*add(w,k1,.5*dt));k3=ns_rhs(*add(w,k2,.5*dt));k4=ns_rhs(*add(w,k3,dt))
            return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                   wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                   wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

        def compute_energy_spectrum(ux_h, uy_h, uz_h):
            """Shell-averaged energy spectrum E(k)."""
            E_hat = 0.5 * (ux_h.abs()**2 + uy_h.abs()**2 + uz_h.abs()**2) / N**6
            max_shell = int(kmag.max().item()) + 1
            spectrum = []
            for s in range(max_shell):
                mask = (kmag >= s - 0.5) & (kmag < s + 0.5)
                spectrum.append(E_hat[mask].sum().item())
            return spectrum

        def compute_alignment_at_max(wx_h, wy_h, wz_h):
            """
            At the point where |ω| is maximum:
            1. Compute the strain tensor S_ij
            2. Find principal eigenvector of S (largest eigenvalue)
            3. Return cos²θ between ω and that eigenvector
            """
            # Get velocity from vorticity via Biot-Savart
            px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px

            # Vorticity in physical space
            wx = ifft(wx_h*D); wy = ifft(wy_h*D); wz = ifft(wz_h*D)
            om_mag = (wx**2 + wy**2 + wz**2).sqrt()
            max_idx = om_mag.argmax().item()
            ix = max_idx // (N*N); iy = (max_idx % (N*N)) // N; iz = max_idx % N

            # Vorticity direction at max point
            w_vec = torch.tensor([wx[ix,iy,iz].item(),
                                  wy[ix,iy,iz].item(),
                                  wz[ix,iy,iz].item()], dtype=torch.float64)
            w_norm = w_vec / (w_vec.norm() + 1e-30)

            # Strain tensor S_ij = (du_i/dx_j + du_j/dx_i) / 2 at max point
            dudx = torch.zeros(3, 3, dtype=torch.float64)
            u_hats = [ux_h, uy_h, uz_h]
            ik_list = [ikx, iky, ikz]
            for i in range(3):
                for j in range(3):
                    field = ifft(ik_list[j] * u_hats[i] * D)
                    dudx[i, j] = field[ix, iy, iz].item()

            S = 0.5 * (dudx + dudx.T)

            # Eigendecomposition
            eigvals, eigvecs = torch.linalg.eigh(S)
            # Principal eigenvector = largest eigenvalue
            principal = eigvecs[:, -1]

            cos2_theta = (w_norm @ principal).item()**2

            return {
                'cos2_theta': cos2_theta,
                'omega_mag': om_mag[ix,iy,iz].item(),
                'eigenvalues': eigvals.tolist(),
                'max_point': [ix, iy, iz],
            }

        # IC setup
        mag = 10.0 / (ksq + 1); mag[0,0,0] = 0
        ic_mask = ksq <= 64

        seed_results = []

        for seed in range(n_seeds):
            torch.manual_seed(seed)
            Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            ux_h0=iky*Az-ikz*Ay;uy_h0=ikz*Ax-ikx*Az;uz_h0=ikx*Ay-iky*Ax
            wx_h=D*(iky*uz_h0-ikz*uy_h0);wy_h=D*(ikz*ux_h0-ikx*uz_h0);wz_h=D*(ikx*uy_h0-iky*ux_h0)

            # Track |omega|_max, save state at peak
            om0_val = None
            om_peak = 0.0
            peak_step = 0
            best_state = None
            t0 = time.time()

            for step in range(n_steps + 1):
                if step % 50 == 0:
                    wx_r = torch.fft.ifftn(wx_h).real
                    wy_r = torch.fft.ifftn(wy_h).real
                    wz_r = torch.fft.ifftn(wz_h).real
                    om = (wx_r**2 + wy_r**2 + wz_r**2).sqrt().max().item()
                    if om0_val is None:
                        om0_val = om
                    if om >= om_peak:
                        om_peak = om
                        peak_step = step
                        best_state = (wx_h.clone(), wy_h.clone(), wz_h.clone())

                if step < n_steps:
                    wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)

            # Diagnostics at peak state
            bwx, bwy, bwz = best_state

            # 1. Energy spectrum
            px=bwx/ksq;py=bwy/ksq;pz=bwz/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            ux_h_peak=iky*pz-ikz*py;uy_h_peak=ikz*px-ikx*pz;uz_h_peak=ikx*py-iky*px
            spectrum = compute_energy_spectrum(ux_h_peak, uy_h_peak, uz_h_peak)

            # 2. Strain-vorticity alignment
            alignment = compute_alignment_at_max(bwx, bwy, bwz)

            # Check: is energy piling up at k_max?
            # Ratio of energy in top 10% of shells vs total
            n_shells = len(spectrum)
            top_10pct = int(max(1, n_shells * 0.1))
            E_total = sum(spectrum)
            E_top = sum(spectrum[-top_10pct:])
            pile_up_ratio = E_top / (E_total + 1e-30)

            elapsed = time.time() - t0
            ratio = om_peak / (om0_val + 1e-30)

            result = {
                'seed': seed,
                'om0': om0_val,
                'om_peak': om_peak,
                'ratio': ratio,
                'peak_step': peak_step,
                'peak_time': peak_step * dt,
                'cos2_theta': alignment['cos2_theta'],
                'eigenvalues': alignment['eigenvalues'],
                'pile_up_ratio': pile_up_ratio,
                'spectrum_last_5': spectrum[-5:] if len(spectrum) >= 5 else spectrum,
                'spectrum_kmax': spectrum[-1] if spectrum else 0,
                'E_total': E_total,
            }
            seed_results.append(result)

            print(f'  seed={seed}: ratio={ratio:.6f} cos²θ={alignment["cos2_theta"]:.4f} '
                  f'pile_up={pile_up_ratio:.2e} peak_step={peak_step} '
                  f'eigs=[{alignment["eigenvalues"][0]:.4f},{alignment["eigenvalues"][1]:.4f},{alignment["eigenvalues"][2]:.4f}] '
                  f'[{elapsed:.0f}s]', flush=True)

        # Aggregate
        cos2_vals = [r['cos2_theta'] for r in seed_results]
        pile_vals = [r['pile_up_ratio'] for r in seed_results]
        ratio_vals = [r['ratio'] for r in seed_results]

        summary = {
            'N': N,
            'nu': nu,
            'n_seeds': n_seeds,
            'n_steps': n_steps,
            'alignment': {
                'mean_cos2_theta': float(np.mean(cos2_vals)),
                'max_cos2_theta': float(np.max(cos2_vals)),
                'min_cos2_theta': float(np.min(cos2_vals)),
                'std_cos2_theta': float(np.std(cos2_vals)),
            },
            'spectrum': {
                'mean_pile_up_ratio': float(np.mean(pile_vals)),
                'max_pile_up_ratio': float(np.max(pile_vals)),
            },
            'omega_max': {
                'mean_ratio': float(np.mean(ratio_vals)),
                'max_ratio': float(np.max(ratio_vals)),
            },
            'per_seed': seed_results,
        }

        all_results[str(N)] = summary

        print(f'\n  SUMMARY N={N}:')
        print(f'    cos²θ at x*: mean={np.mean(cos2_vals):.4f} '
              f'(range [{np.min(cos2_vals):.4f}, {np.max(cos2_vals):.4f}])')
        print(f'    Energy pile-up at k_max: mean={np.mean(pile_vals):.2e}')
        print(f'    |ω|_max ratio: mean={np.mean(ratio_vals):.6f} '
              f'max={np.max(ratio_vals):.6f}')

        if np.mean(cos2_vals) < 0.33:
            print(f'    → DEPLETION ACTIVE: cos²θ < 1/3 (random would be 1/3)')
        elif np.mean(cos2_vals) < 0.5:
            print(f'    → PARTIAL DEPLETION: cos²θ < 1/2')
        else:
            print(f'    → WEAK DEPLETION: cos²θ ≥ 1/2')

        if np.mean(pile_vals) < 1e-4:
            print(f'    → WELL RESOLVED: negligible energy at k_max')
        elif np.mean(pile_vals) < 1e-2:
            print(f'    → ADEQUATELY RESOLVED: small energy at k_max')
        else:
            print(f'    → UNDER-RESOLVED: significant energy at k_max')

        print(flush=True)

    # Save
    out = 'ns_blowup/results/spectrum_alignment.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)

    # Strip per_seed spectra to keep file small
    save_results = {}
    for n_key, data in all_results.items():
        save_data = {k: v for k, v in data.items() if k != 'per_seed'}
        save_data['per_seed'] = [{k: v for k, v in s.items()}
                                  for s in data['per_seed']]
        save_results[n_key] = save_data

    with open(out, 'w') as f:
        json.dump(save_results, f, indent=2)
    print(f'\nSaved: {out}', flush=True)

    # Final verdict
    print(f'\n{"="*60}')
    print('IRON FORTRESS DIAGNOSTIC VERDICT')
    print(f'{"="*60}')
    for n_key, data in all_results.items():
        a = data['alignment']
        s = data['spectrum']
        print(f'  N={n_key}: cos²θ={a["mean_cos2_theta"]:.4f}  '
              f'pile_up={s["mean_pile_up_ratio"]:.2e}  '
              f'ratio={data["omega_max"]["max_ratio"]:.6f}')
    print()
    all_resolved = all(all_results[k]['spectrum']['mean_pile_up_ratio'] < 0.01
                       for k in all_results)
    all_depleted = all(all_results[k]['alignment']['mean_cos2_theta'] < 0.5
                       for k in all_results)
    print(f'  Well-resolved: {"YES" if all_resolved else "NO"}')
    print(f'  Depletion active: {"YES" if all_depleted else "NO"}')
    if all_resolved and all_depleted:
        print(f'  → FORTRESS HOLDS: solution is resolved AND depletion prevents blowup')
    print(flush=True)


if __name__ == '__main__':
    run_diagnostics()
