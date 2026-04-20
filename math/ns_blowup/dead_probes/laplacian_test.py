"""
THE measurement: |Δω(x*)| / |ω(x*)|² at the vorticity maximum.

From reviewer analysis:
- |∇ξ(x*)| = |∇ω(x*)|/|ω(x*)| at the max (because ∇|ω|=0)
- |∇ω(x*)|² ≤ |ω(x*)| × |Δω(x*)| (from Hessian condition)
- CF condition reduces to: |Δω(x*)|/|ω(x*)|² ≤ C

If this ratio is bounded → regularity follows from published theorems.

Also measure:
- |∇ω(x*)|²/|ω(x*)| — the direct CF quantity
- |Δω(x*)|/|ω(x*)| — the intermediate quantity
- Track during TG evolution where |ω| grows
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_laplacian_test(N_values=None, nu=1e-4, n_steps=2000, dt=0.005,
                       n_seeds=10, device='cuda'):
    if N_values is None:
        N_values = [32, 64, 128]

    all_results = {}

    for N in N_values:
        print(f'\n{"="*70}')
        print(f'N={N}, nu={nu}, {n_seeds} seeds')
        print(f'{"="*70}', flush=True)

        Lx=2*math.pi; dx=Lx/N
        k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device=device,dtype=torch.float64)
        kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
        ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
        ikx,iky,ikz=1j*kx,1j*ky,1j*kz
        kmax=N//3
        D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
        ifft=lambda f:torch.fft.ifftn(f*D).real
        fft=torch.fft.fftn

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

        def measure_at_max(wx_h, wy_h, wz_h):
            """Measure all key quantities at x* where |ω| is max."""
            wx=ifft(wx_h*D);wy=ifft(wy_h*D);wz=ifft(wz_h*D)
            om_mag=(wx**2+wy**2+wz**2).sqrt()
            max_idx=om_mag.argmax().item()
            ix=max_idx//(N*N);iy=(max_idx%(N*N))//N;iz=max_idx%N
            rho=om_mag[ix,iy,iz].item()  # |ω(x*)|
            if rho < 1e-30: return None

            # |∇ω(x*)|² — gradient of vorticity vector
            ik_list=[ikx,iky,ikz]
            w_hats=[wx_h,wy_h,wz_h]
            grad_om_sq = 0.0
            for i in range(3):
                for j in range(3):
                    val = ifft(ik_list[j]*w_hats[i]*D)[ix,iy,iz].item()
                    grad_om_sq += val**2
            grad_om = math.sqrt(grad_om_sq)

            # |Δω(x*)| — Laplacian of vorticity
            # Δω_i = -|k|² ω̂_i in Fourier space
            lap_wx = ifft(-ksq*wx_h*D)[ix,iy,iz].item()
            lap_wy = ifft(-ksq*wy_h*D)[ix,iy,iz].item()
            lap_wz = ifft(-ksq*wz_h*D)[ix,iy,iz].item()
            lap_om = math.sqrt(lap_wx**2 + lap_wy**2 + lap_wz**2)

            # The key ratios
            grad_om_sq_over_rho = grad_om_sq / rho        # |∇ω|²/|ω| — CF quantity
            lap_over_rho = lap_om / rho                    # |Δω|/|ω|
            lap_over_rho_sq = lap_om / (rho**2)            # |Δω|/|ω|² — THE ratio
            grad_xi = grad_om / rho                        # |∇ξ| at x*
            cf_ratio = grad_xi / (rho**0.5)                # |∇ξ|/|ω|^{1/2}

            # Verify Hessian condition: |∇ω|² ≤ |ω| × |Δω|
            hessian_check = grad_om_sq <= rho * lap_om + 1e-20

            return {
                'rho': rho,
                'grad_om': grad_om,
                'lap_om': lap_om,
                'grad_om_sq_over_rho': grad_om_sq_over_rho,
                'lap_over_rho': lap_over_rho,
                'lap_over_rho_sq': lap_over_rho_sq,
                'grad_xi': grad_xi,
                'cf_ratio': cf_ratio,
                'hessian_ok': hessian_check,
            }

        # TEST A: Curl noise at t=0 across resolutions
        print("\n--- Curl noise (t=0) ---", flush=True)
        mag=10.0/(ksq+1); mag[0,0,0]=0; ic_mask=ksq<=64

        seed_results = []
        for seed in range(n_seeds):
            torch.manual_seed(seed)
            Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
            wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

            d = measure_at_max(wx_h,wy_h,wz_h)
            if d:
                d['seed'] = seed
                seed_results.append(d)
                print(f"  seed={seed}: |ω|={d['rho']:.6f} |∇ω|²/|ω|={d['grad_om_sq_over_rho']:.4f} "
                      f"|Δω|/|ω|²={d['lap_over_rho_sq']:.4f} CF={d['cf_ratio']:.4f} "
                      f"Hess={'OK' if d['hessian_ok'] else 'FAIL'}", flush=True)

        curl_summary = {
            'N': N,
            'mean_rho': float(np.mean([d['rho'] for d in seed_results])),
            'mean_grad_sq_over_rho': float(np.mean([d['grad_om_sq_over_rho'] for d in seed_results])),
            'mean_lap_over_rho_sq': float(np.mean([d['lap_over_rho_sq'] for d in seed_results])),
            'max_lap_over_rho_sq': float(np.max([d['lap_over_rho_sq'] for d in seed_results])),
            'mean_cf': float(np.mean([d['cf_ratio'] for d in seed_results])),
            'all_hessian_ok': all(d['hessian_ok'] for d in seed_results),
        }

        # TEST B: TG evolution (|ω| grows dynamically)
        if N <= 128:
            print(f"\n--- TG evolution N={N} ---", flush=True)
            x=torch.linspace(0,2*math.pi-dx,N,device=device,dtype=torch.float64)
            X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
            ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z)
            uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            uz=torch.zeros_like(X)
            ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
            wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

            tg_dt = 0.002  # smaller dt for TG
            tg_steps = 2500  # T=5
            tg_series = []
            t0 = time.time()
            for step in range(tg_steps+1):
                if step % 250 == 0:
                    d = measure_at_max(wx_h,wy_h,wz_h)
                    if d:
                        d['step'] = step
                        d['time'] = step*tg_dt
                        tg_series.append(d)
                        print(f"    t={step*tg_dt:.2f}: |ω|={d['rho']:.4f} "
                              f"|∇ω|²/|ω|={d['grad_om_sq_over_rho']:.4f} "
                              f"|Δω|/|ω|²={d['lap_over_rho_sq']:.6f} "
                              f"CF={d['cf_ratio']:.4f}", flush=True)
                if step < tg_steps:
                    wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,tg_dt)
            print(f"  [{time.time()-t0:.0f}s]", flush=True)
        else:
            tg_series = []

        all_results[str(N)] = {
            'curl_noise': curl_summary,
            'curl_seeds': seed_results,
            'tg_evolution': tg_series,
        }

        print(f"\n  SUMMARY N={N}:")
        print(f"    Curl: |Δω|/|ω|² mean={curl_summary['mean_lap_over_rho_sq']:.4f} "
              f"max={curl_summary['max_lap_over_rho_sq']:.4f}")
        print(f"    Hessian condition: {'ALL OK' if curl_summary['all_hessian_ok'] else 'SOME FAIL'}")

    # Final table
    print('\n' + '=' * 70)
    print('THE TABLE: |Δω(x*)|/|ω(x*)|² across resolutions')
    print('If bounded → regularity follows')
    print('=' * 70)
    print(f'{"N":>6} {"mean |Δω|/|ω|²":>16} {"max |Δω|/|ω|²":>16} {"mean CF":>10} {"Hessian":>10}')
    for n_key in sorted(all_results.keys(), key=int):
        d = all_results[n_key]['curl_noise']
        print(f'{d["N"]:6d} {d["mean_lap_over_rho_sq"]:16.4f} {d["max_lap_over_rho_sq"]:16.4f} '
              f'{d["mean_cf"]:10.4f} {"OK" if d["all_hessian_ok"] else "FAIL":>10}')

    out = 'ns_blowup/results/laplacian_test.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    run_laplacian_test()
