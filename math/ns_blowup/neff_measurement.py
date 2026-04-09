"""
N_eff measurement at x* — the key diagnostic for the proof.

At the point of maximum |omega|, compute:
1. N_eff = (sum |omega_k(x*)|)^2 / sum |omega_k(x*)|^2  (participation ratio)
2. Angular dispersion of contributing wavevectors
3. cos^2(theta) between omega and principal strain eigenvector
4. Check: does cos^2(theta) * N_eff ~ constant?
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_neff(N_values=None, nu=1e-4, n_steps=2000, dt=0.005,
             n_seeds=10, device='cuda'):
    if N_values is None:
        N_values = [16, 32, 64, 128]

    all_results = {}

    for N in N_values:
        print(f'\n{"="*60}')
        print(f'N={N}, nu={nu}, {n_seeds} seeds')
        print(f'{"="*60}', flush=True)

        Lx = 2*math.pi; dx = Lx/N
        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
        kx,ky,kz = torch.meshgrid(k,k,k,indexing='ij')
        ksq = kx**2+ky**2+kz**2; ksq[0,0,0] = 1.0
        ikx,iky,ikz = 1j*kx, 1j*ky, 1j*kz
        kmax = N//3
        D = ((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)

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

        def compute_neff_and_alignment(wx_h, wy_h, wz_h):
            """At x* where |omega| is max, compute N_eff and cos^2(theta)."""
            # Physical vorticity
            wx = ifft(wx_h*D); wy = ifft(wy_h*D); wz = ifft(wz_h*D)
            om_mag = (wx**2 + wy**2 + wz**2).sqrt()
            max_idx = om_mag.argmax().item()
            ix = max_idx // (N*N); iy = (max_idx % (N*N)) // N; iz = max_idx % N
            om_max_val = om_mag[ix,iy,iz].item()

            # Vorticity direction at x*
            e_vec = torch.tensor([wx[ix,iy,iz].item(), wy[ix,iy,iz].item(),
                                  wz[ix,iy,iz].item()], dtype=torch.float64)
            e_hat = e_vec / (e_vec.norm() + 1e-30)

            # Fourier mode contributions at x*
            # omega_k(x*) = hat{omega}(k) * exp(ik.x*) — complex 3-vector per mode
            # We need |omega_k(x*)| for each k
            x_star = torch.tensor([ix * dx, iy * dx, iz * dx],
                                  dtype=torch.float64, device=device)
            phase = kx * x_star[0] + ky * x_star[1] + kz * x_star[2]
            exp_phase = torch.exp(1j * phase)  # [N,N,N]

            # Mode contributions: omega_k(x*) = hat{omega}(k) * exp(ik.x*)
            owx = wx_h * D * exp_phase  # still complex [N,N,N]
            owy = wy_h * D * exp_phase
            owz = wz_h * D * exp_phase

            # |omega_k(x*)| for each mode
            mode_mag = (owx.abs()**2 + owy.abs()**2 + owz.abs()**2).sqrt()  # [N,N,N]

            # Flatten and compute N_eff
            mm = mode_mag.reshape(-1)
            mm_nonzero = mm[mm > 1e-30]

            sum_mag = mm_nonzero.sum().item()
            sum_mag_sq = (mm_nonzero**2).sum().item()
            N_eff = sum_mag**2 / (sum_mag_sq + 1e-30)

            # Also compute: max mode fraction
            max_mode_mag = mm.max().item()
            max_mode_frac = max_mode_mag / (sum_mag + 1e-30)

            # Angular dispersion of contributing wavevectors
            # Weight each k direction by its mode magnitude
            # Compute the "inertia tensor" of k directions weighted by |omega_k|
            kx_flat = kx.reshape(-1)
            ky_flat = ky.reshape(-1)
            kz_flat = kz.reshape(-1)
            mm_flat = mode_mag.reshape(-1)

            # Only use modes above threshold
            thresh = 0.01 * mm_flat.max()
            mask = mm_flat > thresh
            w = mm_flat[mask]
            kxm = kx_flat[mask]; kym = ky_flat[mask]; kzm = kz_flat[mask]
            kmag = (kxm**2 + kym**2 + kzm**2).sqrt()
            kmag = torch.clamp(kmag, min=1e-10)

            # Unit k directions
            khat_x = kxm / kmag; khat_y = kym / kmag; khat_z = kzm / kmag

            # Weighted direction matrix (3x3)
            w_total = w.sum()
            M = torch.zeros(3, 3, dtype=torch.float64, device=device)
            M[0,0] = (w * khat_x * khat_x).sum() / w_total
            M[0,1] = (w * khat_x * khat_y).sum() / w_total
            M[0,2] = (w * khat_x * khat_z).sum() / w_total
            M[1,0] = M[0,1]; M[1,1] = (w * khat_y * khat_y).sum() / w_total
            M[1,2] = (w * khat_y * khat_z).sum() / w_total
            M[2,0] = M[0,2]; M[2,1] = M[1,2]
            M[2,2] = (w * khat_z * khat_z).sum() / w_total

            # Angular dispersion: if isotropic, M = I/3, eigenvalues all 1/3
            # If concentrated, largest eigenvalue → 1
            ang_eigs = torch.linalg.eigvalsh(M).cpu().tolist()
            angular_dispersion = 1.0 - max(ang_eigs)  # 0 = concentrated, 2/3 = isotropic

            # Strain and cos^2(theta)
            px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px

            dudx = torch.zeros(3, 3, dtype=torch.float64)
            u_hats = [ux_h, uy_h, uz_h]
            ik_list = [ikx, iky, ikz]
            for i in range(3):
                for j in range(3):
                    field = ifft(ik_list[j] * u_hats[i] * D)
                    dudx[i, j] = field[ix, iy, iz].item()

            S = 0.5 * (dudx + dudx.T)
            eigvals, eigvecs = torch.linalg.eigh(S)
            principal = eigvecs[:, -1]
            cos2_theta = (e_hat @ principal).item()**2

            return {
                'N_eff': N_eff,
                'cos2_theta': cos2_theta,
                'product': cos2_theta * N_eff,
                'angular_dispersion': angular_dispersion,
                'ang_eigs': ang_eigs,
                'max_mode_frac': max_mode_frac,
                'om_max': om_max_val,
                'n_active_modes': int(mask.sum().item()),
            }

        # IC setup
        mag = 10.0 / (ksq + 1); mag[0,0,0] = 0
        ic_mask = ksq <= 64

        # Checkpoints: measure at multiple physical times
        check_steps = [0, 400, 1000, 2000]
        check_times = [s * dt for s in check_steps]

        seed_results = []

        for seed in range(n_seeds):
            torch.manual_seed(seed)
            Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
            wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

            t0 = time.time()
            time_series = []
            step = 0
            for cs in check_steps:
                # Advance to checkpoint
                while step < cs:
                    wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)
                    step += 1
                result = compute_neff_and_alignment(wx_h, wy_h, wz_h)
                result['step'] = cs
                result['time'] = cs * dt
                time_series.append(result)

            elapsed = time.time() - t0
            seed_results.append({'seed': seed, 'time_series': time_series})

            # Print one line per seed showing evolution
            neffs_t = [r['N_eff'] for r in time_series]
            cos2s_t = [r['cos2_theta'] for r in time_series]
            prods_t = [r['product'] for r in time_series]
            print(f'  seed={seed}: N_eff=[{",".join(f"{v:.0f}" for v in neffs_t)}] '
                  f'cos2=[{",".join(f"{v:.3f}" for v in cos2s_t)}] '
                  f'prod=[{",".join(f"{v:.1f}" for v in prods_t)}] [{elapsed:.0f}s]', flush=True)

        # Aggregate by time checkpoint
        summaries_by_time = []
        for ti, cs in enumerate(check_steps):
            neffs = [sr['time_series'][ti]['N_eff'] for sr in seed_results]
            cos2s = [sr['time_series'][ti]['cos2_theta'] for sr in seed_results]
            products = [sr['time_series'][ti]['product'] for sr in seed_results]
            ang_disps = [sr['time_series'][ti]['angular_dispersion'] for sr in seed_results]
            summaries_by_time.append({
                'step': cs, 'time': cs * dt,
                'N_eff_mean': float(np.mean(neffs)), 'N_eff_std': float(np.std(neffs)),
                'cos2_mean': float(np.mean(cos2s)), 'cos2_std': float(np.std(cos2s)),
                'product_mean': float(np.mean(products)), 'product_std': float(np.std(products)),
                'ang_disp_mean': float(np.mean(ang_disps)),
            })

        summary = {
            'N': N,
            'by_time': summaries_by_time,
            'per_seed': seed_results,
        }
        all_results[str(N)] = summary

        print(f'\n  SUMMARY N={N}:')
        print(f'  {"t":>6} {"N_eff":>10} {"cos2":>10} {"PRODUCT":>10} {"ang_disp":>10}')
        for s in summaries_by_time:
            print(f'  {s["time"]:6.1f} {s["N_eff_mean"]:10.1f} {s["cos2_mean"]:10.4f} '
                  f'{s["product_mean"]:10.2f} {s["ang_disp_mean"]:10.3f}')
        print(flush=True)

    # Final table — show N_eff evolution over time for each N
    print('\n' + '=' * 70)
    print('N_EFF EVOLUTION TABLE — does N_eff grow with time (energy cascade)?')
    print('=' * 70)
    for n_key in sorted(all_results.keys(), key=int):
        d = all_results[n_key]
        print(f'\nN={d["N"]}:')
        print(f'  {"t":>6} {"N_eff":>10} {"cos2":>10} {"PRODUCT":>10} {"ang_disp":>10}')
        for s in d['by_time']:
            print(f'  {s["time"]:6.1f} {s["N_eff_mean"]:10.1f} {s["cos2_mean"]:10.4f} '
                  f'{s["product_mean"]:10.2f} {s["ang_disp_mean"]:10.3f}')

    # Cross-N comparison at each time
    print('\n' + '=' * 70)
    print('CROSS-N COMPARISON — does cos2 decrease with N at fixed time?')
    print('=' * 70)
    times_to_show = [0.0, 2.0, 5.0, 10.0]
    for t_show in times_to_show:
        print(f'\nt={t_show}:')
        print(f'  {"N":>6} {"N_eff":>10} {"cos2":>10} {"PRODUCT":>10}')
        for n_key in sorted(all_results.keys(), key=int):
            d = all_results[n_key]
            for s in d['by_time']:
                if abs(s['time'] - t_show) < 0.01:
                    print(f'  {d["N"]:6d} {s["N_eff_mean"]:10.1f} {s["cos2_mean"]:10.4f} '
                          f'{s["product_mean"]:10.2f}')

    print('\nKey question: does N_eff GROW with time as energy cascades to small scales?')
    print('If yes → cos2 should shrink → depletion strengthens → proof path viable')

    out = 'ns_blowup/results/neff_scaling.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    run_neff()
