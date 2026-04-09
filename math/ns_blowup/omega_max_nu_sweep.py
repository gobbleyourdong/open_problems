"""
|omega|_max vs viscosity sweep.

THE critical test: does |omega|_max stay bounded as nu → 0?

If YES → geometric mechanism, not viscous damping → supports regularity
If NO → just viscous damping → expected, doesn't address the problem

Fix IC (seed 0, k≤8), fix N=64, vary nu.
Track |omega|_max(t) / |omega|_max(0) through T=10.
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_nu_sweep(N=64, nu_values=None, n_steps=2000, dt=0.005,
                 n_seeds=20, device='cuda'):
    if nu_values is None:
        nu_values = [1e-2, 1e-3, 1e-4, 1e-5, 0]  # 0 = Euler

    Lx = 2*math.pi
    dx = Lx/N
    k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
    kx,ky,kz = torch.meshgrid(k,k,k,indexing='ij')
    ksq = kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    ikx,iky,ikz = 1j*kx,1j*ky,1j*kz
    kmax = N//3
    D = ((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)

    ifft = lambda f: torch.fft.ifftn(f*D).real
    fft = torch.fft.fftn

    def make_rhs(nu):
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
        return ns_rhs

    def rk4(ns_rhs, wx_h,wy_h,wz_h,dt):
        def add(a,b,s):return(a[0]+s*b[0],a[1]+s*b[1],a[2]+s*b[2])
        w=(wx_h,wy_h,wz_h)
        k1=ns_rhs(*w);k2=ns_rhs(*add(w,k1,.5*dt));k3=ns_rhs(*add(w,k2,.5*dt));k4=ns_rhs(*add(w,k3,dt))
        return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def omega_max(wx_h,wy_h,wz_h):
        wx=torch.fft.ifftn(wx_h).real;wy=torch.fft.ifftn(wy_h).real;wz=torch.fft.ifftn(wz_h).real
        return (wx**2+wy**2+wz**2).sqrt().max().item()

    # Fixed IC: low modes only
    mag = 10.0/(ksq+1); mag[0,0,0]=0
    ic_mask = ksq <= 64  # k <= 8

    print(f'|omega|_max vs VISCOSITY SWEEP')
    print(f'N={N}, {n_seeds} seeds, {n_steps} steps (T={n_steps*dt})')
    print(f'IC: curl noise k<=8, amp=10')
    print(f'nu values: {nu_values}')
    print('='*60, flush=True)

    results = {}

    for nu in nu_values:
        ns_rhs = make_rhs(nu)
        nu_str = f'{nu:.0e}' if nu > 0 else 'Euler'

        all_ratios = []
        all_peaks = []
        all_trajectories = []
        t0 = time.time()

        for seed in range(n_seeds):
            torch.manual_seed(seed)
            Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
            ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
            wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

            om0 = omega_max(wx_h,wy_h,wz_h)
            traj = [om0]
            om_peak = om0

            # Adaptive dt for low viscosity
            dt_use = min(dt, 0.3*dx/(om0+1e-10))
            if nu > 0:
                dt_use = min(dt_use, 0.5*dx**2/nu)
            actual_steps = max(int(n_steps * dt / dt_use), n_steps)

            for step in range(actual_steps):
                wx_h,wy_h,wz_h = rk4(ns_rhs, wx_h,wy_h,wz_h, dt_use)
                if step % max(1, actual_steps//20) == 0:
                    om = omega_max(wx_h,wy_h,wz_h)
                    traj.append(om)
                    om_peak = max(om_peak, om)
                    if om > 1e6:
                        print(f'  BLOWUP at nu={nu_str} seed={seed} step={step}', flush=True)
                        break

            ratio = om_peak / (om0 + 1e-30)
            all_ratios.append(ratio)
            all_peaks.append(om_peak)
            all_trajectories.append(traj)

        elapsed = time.time() - t0
        mean_ratio = np.mean(all_ratios)
        max_ratio = np.max(all_ratios)

        results[nu_str] = {
            'nu': nu,
            'mean_ratio': float(mean_ratio),
            'max_ratio': float(max_ratio),
            'mean_peak': float(np.mean(all_peaks)),
        }

        print(f'nu={nu_str:>8s}: mean_ratio={mean_ratio:.6f} max_ratio={max_ratio:.6f} '
              f'[{elapsed:.0f}s]', flush=True)

    print(f'\n{"="*60}')
    print('VISCOSITY SWEEP RESULTS')
    print(f'{"="*60}')
    print(f'{"nu":>10} {"mean_ratio":>12} {"max_ratio":>12}')
    for nu_str, r in results.items():
        print(f'{nu_str:>10} {r["mean_ratio"]:12.6f} {r["max_ratio"]:12.6f}')

    print()
    ratios = [r['max_ratio'] for r in results.values()]
    if all(r <= 1.01 for r in ratios):
        print('ALL RATIOS ≤ 1.01: |omega|_max bounded INDEPENDENT of viscosity')
        print('→ This is NOT viscous damping — it is GEOMETRIC')
        print('→ Strong evidence for regularity')
    elif ratios[-1] > ratios[0] * 1.5:
        print('RATIO GROWS with decreasing nu')
        print('→ Viscous damping is the mechanism, not geometry')
        print('→ Does not address the regularity question')
    else:
        print('MIXED — some growth but bounded')

    out = 'ns_blowup/results/omega_max_nu_sweep.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    run_nu_sweep()
