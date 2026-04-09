"""
Miller's Eigenfunction Distance Criterion (Theorem 1.12):
Regularity if ∫₀ᵀ inf_ρ ||-ρΔS - S||^p_{L^q} dt < ∞

Miller's formula (Proposition 6.2):
inf_ρ ||-ρΔS - S||²_{L²} = (1 - ||S||⁴_{H¹}/(||S||²_{L²}×||-ΔS||²_{L²})) × ||S||²_{L²}

The factor (1 - ||S||⁴_{H¹}/(||S||²_{L²}||-ΔS||²_{L²})) ∈ [0,1]:
= 0 iff S is an eigenfunction of -Δ
= 1 iff S has maximum spread across scales

If this factor → 0 at high ρ (single mode dominates) → eigenfunction distance → 0
→ time integral converges → regularity.
"""
import torch
import math
import time
import json
import os
import numpy as np

torch.set_default_dtype(torch.float64)


def run_eigenfunction_test(N=64, nu=1e-4, device='cuda'):
    Lx=2*math.pi; dx=Lx/N
    k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device)
    kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
    ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    ikx,iky,ikz=1j*kx,1j*ky,1j*kz
    kmax=N//3; D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
    ifft=lambda f:torch.fft.ifftn(f*D).real; fft=torch.fft.fftn
    ik_list=[ikx,iky,ikz]

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

    def compute_strain_norms(wx_h, wy_h, wz_h):
        """Compute ||S||_{L²}, ||S||_{H¹}, ||-ΔS||_{L²} from vorticity."""
        # Velocity from Biot-Savart
        px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
        u_hats=[ux_h,uy_h,uz_h]

        # Strain S_ij = (∂u_i/∂x_j + ∂u_j/∂x_i)/2 in Fourier
        # ||S||²_{H^α} = Σ_{i,j} ||Ŝ_ij||²_{H^α} = Σ |k|^{2α} |Ŝ_ij(k)|²
        S_L2_sq = 0.0    # ||S||²_{L²}
        S_H1_sq = 0.0    # ||S||²_{H¹} = Σ(1+|k|²)|Ŝ|²
        S_H2_sq = 0.0    # ||-ΔS||²_{L²} = Σ|k|⁴|Ŝ|²

        for i in range(3):
            for j in range(i, 3):
                S_ij_h = 0.5 * (ik_list[j]*u_hats[i] + ik_list[i]*u_hats[j]) * D
                S_ij_sq = (S_ij_h.abs()**2).sum().item() / N**6
                S_ij_k2 = (ksq * S_ij_h.abs()**2).sum().item() / N**6
                S_ij_k4 = (ksq**2 * S_ij_h.abs()**2).sum().item() / N**6

                factor = 1 if i == j else 2  # off-diagonal counted twice
                S_L2_sq += factor * S_ij_sq
                S_H1_sq += factor * (S_ij_sq + S_ij_k2)
                S_H2_sq += factor * S_ij_k4

        return math.sqrt(S_L2_sq), math.sqrt(S_H1_sq), math.sqrt(S_H2_sq)

    # TG evolution
    print(f'EIGENFUNCTION DISTANCE — TG N={N}', flush=True)
    print(f'Miller factor = 1 - ||S||⁴_{{H¹}}/(||S||²_{{L²}}||-ΔS||²_{{L²}})')
    print(f'= 0 → S is eigenfunction of -Δ (GOOD for regularity)')
    print(f'= 1 → S has max spectral spread (BAD)')
    print(f'')

    x=torch.linspace(0,2*math.pi-dx,N,device=device,dtype=torch.float64)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z)
    uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
    uz=torch.zeros_like(X)
    ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
    wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

    dt=0.002; n_steps=2500
    print(f'{"t":>5} {"||S||_L2":>10} {"||S||_H1":>10} {"||-ΔS||":>10} {"factor":>8} {"ρ_max":>8}')

    series = []
    for step in range(n_steps+1):
        if step % 250 == 0:
            S_L2, S_H1, DeltaS = compute_strain_norms(wx_h, wy_h, wz_h)
            # Miller factor
            if S_L2 > 1e-30 and DeltaS > 1e-30:
                factor = 1.0 - S_H1**4 / (S_L2**2 * DeltaS**2)
            else:
                factor = 0.0

            # Also compute ρ_max
            wx=ifft(wx_h*D);wy=ifft(wy_h*D);wz=ifft(wz_h*D)
            rho = (wx**2+wy**2+wz**2).sqrt().max().item()

            d = {'time': step*dt, 'S_L2': S_L2, 'S_H1': S_H1,
                 'DeltaS': DeltaS, 'factor': factor, 'rho': rho}
            series.append(d)

            print(f'{step*dt:5.2f} {S_L2:10.6f} {S_H1:10.6f} {DeltaS:10.6f} '
                  f'{factor:8.4f} {rho:8.4f}', flush=True)

        if step < n_steps:
            wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)

    # Analysis
    factors = [d['factor'] for d in series]
    rhos = [d['rho'] for d in series]

    print(f'\nSUMMARY:')
    print(f'  Factor range: [{min(factors):.6f}, {max(factors):.6f}]')
    print(f'  Factor at max ρ ({max(rhos):.2f}): {series[rhos.index(max(rhos))]["factor"]:.6f}')
    print(f'  Does factor → 0 at high ρ? {"YES" if series[rhos.index(max(rhos))]["factor"] < 0.5 else "NO"}')

    # Time integral of factor^p (for regularity: needs to be finite)
    integral = sum(d['factor'] * dt * 250 for d in series)  # crude Riemann sum
    print(f'  ∫ factor dt ≈ {integral:.4f} (finite = good)')

    out = f'ns_blowup/results/eigenfunction_distance_N{N}.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(series, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    run_eigenfunction_test()
