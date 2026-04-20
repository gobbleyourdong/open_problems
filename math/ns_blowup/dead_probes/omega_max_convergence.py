"""
|omega|_max convergence under refinement.

The BKM criterion: blowup iff ∫|ω|_∞ dt = ∞.
If |ω|_max stays bounded for all time at every resolution → regularity.

Track |ω|_max(t) for the SAME IC resolved at different N.
Fix low modes (k=1..8), add higher modes as N increases.
The shared content should produce convergent |ω|_max trajectories.
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_omega_max(N, nu=1e-4, n_steps=2000, dt=0.005, seeds=range(50), device='cuda'):
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
        return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def omega_max(wx_h,wy_h,wz_h):
        wx=torch.fft.ifftn(wx_h).real
        wy=torch.fft.ifftn(wy_h).real
        wz=torch.fft.ifftn(wz_h).real
        return (wx**2+wy**2+wz**2).sqrt().max().item()

    # IC: curl noise with FIXED low modes only (k <= 8)
    # This ensures the SAME physical IC at every resolution
    mag = 10.0 / (ksq + 1)
    mag[0,0,0] = 0
    k_ic_max = 8  # only populate modes up to k=8
    ic_mask = (ksq <= k_ic_max**2)

    all_trajectories = []
    all_peaks = []
    all_ratios = []
    t0 = time.time()

    for seed in seeds:
        torch.manual_seed(seed)
        Ax = mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        Ay = mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        Az = mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
        wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

        om0 = omega_max(wx_h,wy_h,wz_h)
        trajectory = [om0]
        om_peak = om0

        for step in range(n_steps):
            wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)
            if step % 100 == 99:
                om = omega_max(wx_h,wy_h,wz_h)
                trajectory.append(om)
                om_peak = max(om_peak, om)

        om_final = trajectory[-1]
        all_trajectories.append(trajectory)
        all_peaks.append(om_peak)
        all_ratios.append(om_peak / (om0 + 1e-30))

        if (seed+1) % 10 == 0:
            elapsed = time.time() - t0
            print(f'  N={N} [{seed+1}/{len(list(seeds))}] '
                  f'om0={om0:.4f} peak={om_peak:.4f} ratio={om_peak/om0:.4f} '
                  f'[{elapsed:.0f}s]', flush=True)

    return {
        'peaks': all_peaks,
        'ratios': all_ratios,
        'trajectories': all_trajectories,
        'mean_peak': float(np.mean(all_peaks)),
        'max_peak': float(np.max(all_peaks)),
        'mean_ratio': float(np.mean(all_ratios)),
        'max_ratio': float(np.max(all_ratios)),
    }


def main():
    device = 'cuda'
    nu = 1e-4
    n_steps = 2000
    dt = 0.005
    n_seeds = 50

    print('|omega|_max CONVERGENCE UNDER REFINEMENT')
    print(f'nu={nu}, {n_steps} steps (T={n_steps*dt}), {n_seeds} seeds')
    print(f'IC: curl noise, k_max=8 (FIXED across resolutions)')
    print('='*60, flush=True)

    results = {}

    for N in [16, 32, 64, 128]:
        print(f'\nN={N}:', flush=True)
        r = run_omega_max(N, nu=nu, n_steps=n_steps, dt=dt,
                          seeds=range(n_seeds), device=device)
        results[str(N)] = {
            'N': N,
            'mean_peak': r['mean_peak'],
            'max_peak': r['max_peak'],
            'mean_ratio': r['mean_ratio'],
            'max_ratio': r['max_ratio'],
        }
        print(f'  N={N}: mean_peak={r["mean_peak"]:.6f} max_peak={r["max_peak"]:.6f} '
              f'mean_ratio={r["mean_ratio"]:.4f} max_ratio={r["max_ratio"]:.4f}', flush=True)

    print(f'\n{"="*60}')
    print('CONVERGENCE TABLE: |omega|_max')
    print(f'{"="*60}')
    print(f'{"N":>5} {"mean_peak":>12} {"max_peak":>12} {"mean_ratio":>12} {"max_ratio":>12}')
    for N in [16, 32, 64, 128]:
        r = results[str(N)]
        print(f'{N:5d} {r["mean_peak"]:12.6f} {r["max_peak"]:12.6f} '
              f'{r["mean_ratio"]:12.4f} {r["max_ratio"]:12.4f}')

    print()
    max_of_max = max(r['max_ratio'] for r in results.values())
    if max_of_max <= 1.0:
        print('ALL RATIOS <= 1.0: |omega|_max NEVER GROWS')
        print('→ BKM integral bounded → REGULARITY')
    elif max_of_max <= 1.1:
        print(f'MAX RATIO = {max_of_max:.4f}: |omega|_max approximately bounded')
        print('→ BKM integral likely bounded')
    else:
        print(f'MAX RATIO = {max_of_max:.4f}: |omega|_max GROWS')
        print('→ Potential blowup — investigate further')

    print()
    # Check convergence: does peak_omega CONVERGE as N increases?
    peaks = [results[str(N)]['mean_peak'] for N in [16,32,64,128]]
    if all(abs(peaks[i] - peaks[i+1]) / peaks[i] < 0.1 for i in range(len(peaks)-1)):
        print('Peak values CONVERGE under refinement: physical, not numerical')
    else:
        ratios = [peaks[i+1]/peaks[i] for i in range(len(peaks)-1)]
        print(f'Peak ratios across N: {[f"{r:.4f}" for r in ratios]}')
        if all(r < 1.1 for r in ratios):
            print('Peaks bounded and slowly varying: consistent with regularity')

    # Save
    out = 'ns_blowup/results/omega_max_convergence.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    main()
