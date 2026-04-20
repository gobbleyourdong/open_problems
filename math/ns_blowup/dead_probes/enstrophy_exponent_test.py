"""
Measure the enstrophy growth exponent: does max E(T)/E(0) scale as E₀^{3/2} or E₀^{1.49}?

Kang-Protas (2020): max enstrophy amplification ~ 0.224 × E₀^{1.490 ± 0.004}
If exponent < 3/2 at resolved scales → the gap is real → regularity via Miller.

Strategy:
- Generate ICs with varying E₀ (enstrophy) by scaling amplitude
- For each E₀: evolve NS and track max E(t)/E₀
- Fit the power law: max E(T)/E₀ vs E₀
- Report the exponent across N=32, 64, 128
"""
import torch
import math
import time
import json
import numpy as np

torch.set_default_dtype(torch.float64)


def run_enstrophy_exponent(N=64, nu=1e-4, device='cpu'):
    Lx = 2*math.pi; dx = Lx/N
    k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device)
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
        w=(wx_h,wy_h,wz_h);k1=ns_rhs(*w);k2=ns_rhs(*add(w,k1,.5*dt));k3=ns_rhs(*add(w,k2,.5*dt));k4=ns_rhs(*add(w,k3,dt))
        return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
               wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
               wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def enstrophy(wx_h,wy_h,wz_h):
        """E = (1/2) ∫|ω|² dx = (1/2) Σ|ω̂(k)|²"""
        return 0.5 * ((wx_h*D).abs()**2 + (wy_h*D).abs()**2 + (wz_h*D).abs()**2).sum().item() / N**3

    # Base IC (seed=0, k≤8)
    mag_base = 1.0/(ksq+1); mag_base[0,0,0] = 0
    ic_mask = ksq <= 64

    # Vary amplitude to get different E₀
    # E₀ scales as amp² (enstrophy is quadratic in ω)
    amplitudes = [1, 2, 5, 10, 20, 50, 100, 200, 500]

    print(f'ENSTROPHY GROWTH EXPONENT — N={N}, ν={nu}')
    print(f'{"amp":>6} {"E₀":>12} {"max_E":>12} {"ratio":>10} {"log_E0":>8} {"log_ratio":>10}')

    results = []

    for amp in amplitudes:
        torch.manual_seed(0)
        mag = amp * mag_base
        Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
        ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
        wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

        E0 = enstrophy(wx_h,wy_h,wz_h)

        # Adaptive dt for CFL
        dt = min(0.005, 0.5 / (amp + 1))
        n_steps = max(500, int(5.0 / dt))

        max_E = E0
        t0 = time.time()
        for step in range(n_steps):
            wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)
            if step % max(1, n_steps//20) == 0:
                E = enstrophy(wx_h,wy_h,wz_h)
                max_E = max(max_E, E)

        elapsed = time.time() - t0
        ratio = max_E / E0
        log_E0 = math.log10(E0) if E0 > 0 else 0
        log_ratio = math.log10(ratio) if ratio > 1 else 0

        results.append({'amp': amp, 'E0': E0, 'max_E': max_E, 'ratio': ratio,
                       'log_E0': log_E0, 'log_ratio': log_ratio})

        print(f'{amp:6d} {E0:12.4f} {max_E:12.4f} {ratio:10.6f} {log_E0:8.3f} {log_ratio:10.6f} [{elapsed:.0f}s]',
              flush=True)

    # Fit power law: max_E/E0 = C × E0^(β-1)  → log(ratio) = log(C) + (β-1)log(E0)
    # Only use points where ratio > 1 (actual growth)
    growing = [(r['log_E0'], r['log_ratio']) for r in results if r['ratio'] > 1.001]

    if len(growing) >= 3:
        x = np.array([g[0] for g in growing])
        y = np.array([g[1] for g in growing])
        slope, intercept = np.polyfit(x, y, 1)
        beta = slope + 1  # ratio ~ E0^(β-1), so log(ratio) slope = β-1

        print(f'\nFIT: log(ratio) = {slope:.4f} × log(E₀) + {intercept:.4f}')
        print(f'EXPONENT β = {beta:.4f} (ratio ~ E₀^{{β-1}} = E₀^{{{slope:.4f}}})')
        print(f'')
        print(f'CRITICAL: β = 3/2 = 1.5000 is the blowup threshold')
        print(f'Kang-Protas: β = 1.490 ± 0.004')
        print(f'Our measurement: β = {beta:.4f}')
        print(f'Gap from 3/2: {1.5 - beta:.4f}')
        if beta < 1.5:
            print(f'→ BELOW THRESHOLD — supports regularity!')
        else:
            print(f'→ AT OR ABOVE THRESHOLD')
    else:
        print(f'\nNot enough growing cases for fit (need ratio > 1)')
        beta = None

    out = f'ns_blowup/results/enstrophy_exponent_N{N}.json'
    import os; os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'N': N, 'nu': nu, 'beta': beta, 'results': results}, f, indent=2)
    print(f'\nSaved: {out}', flush=True)

    return beta


if __name__ == '__main__':
    for N in [32, 64]:
        print(f'\n{"="*70}')
        run_enstrophy_exponent(N=N)
        print()
