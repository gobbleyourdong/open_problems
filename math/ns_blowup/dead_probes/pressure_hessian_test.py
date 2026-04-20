"""
Pressure Hessian at x* — does it oppose stretching?

If ê·H·ê > 0 at the vorticity maximum when α > 0,
the strain equation gives dα/dt ≤ -|S|² - ê·H·ê + viscous ≤ -α²
which is SELF-LIMITING and closes the proof.

Also measure ê·S²·ê (the self-depletion term).
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_pressure_test(N_values=None, nu=1e-4, device='cuda'):
    if N_values is None:
        N_values = [64]  # Start with N=64 TG for speed

    for N in N_values:
        Lx=2*math.pi; dx=Lx/N
        k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device=device,dtype=torch.float64)
        kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
        ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
        ikx,iky,ikz=1j*kx,1j*ky,1j*kz
        kmax=N//3
        D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
        ifft=lambda f:torch.fft.ifftn(f*D).real
        fft=torch.fft.fftn
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
            w=(wx_h,wy_h,wz_h)
            k1=ns_rhs(*w);k2=ns_rhs(*add(w,k1,.5*dt));k3=ns_rhs(*add(w,k2,.5*dt));k4=ns_rhs(*add(w,k3,dt))
            return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                   wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                   wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

        def measure_strain_dynamics(wx_h, wy_h, wz_h):
            """Measure all terms in the strain evolution at x*."""
            # Vorticity
            wx=ifft(wx_h*D);wy=ifft(wy_h*D);wz=ifft(wz_h*D)
            om_mag=(wx**2+wy**2+wz**2).sqrt()
            max_idx=om_mag.argmax().item()
            ix=max_idx//(N*N);iy=(max_idx%(N*N))//N;iz=max_idx%N
            rho=om_mag[ix,iy,iz].item()
            if rho<1e-30: return None

            e_hat=torch.tensor([wx[ix,iy,iz].item(),wy[ix,iy,iz].item(),
                                wz[ix,iy,iz].item()],dtype=torch.float64)
            e_hat=e_hat/(e_hat.norm()+1e-30)

            # Velocity from Biot-Savart
            px_h=wx_h/ksq;py_h=wy_h/ksq;pz_h=wz_h/ksq
            px_h[0,0,0]=0;py_h[0,0,0]=0;pz_h[0,0,0]=0
            ux_h=iky*pz_h-ikz*py_h;uy_h=ikz*px_h-ikx*pz_h;uz_h=ikx*py_h-iky*px_h
            u_hats=[ux_h,uy_h,uz_h]

            # Velocity gradient A_ij = ∂u_i/∂x_j at x*
            A=torch.zeros(3,3,dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    A[i,j]=ifft(ik_list[j]*u_hats[i]*D)[ix,iy,iz].item()

            # Strain S and rotation Ω
            S=0.5*(A+A.T)
            Omega=0.5*(A-A.T)

            # α = ê·S·ê
            alpha=(e_hat@S@e_hat).item()

            # ê·S²·ê (self-depletion, should be ≥ 0)
            S2=S@S
            eS2e=(e_hat@S2@e_hat).item()

            # Pressure: Δp = |ω|²/2 - |S|² (from the Poisson equation)
            S_norm_sq=(S**2).sum().item()
            omega_sq=rho**2
            laplacian_p=omega_sq/2-S_norm_sq

            # Pressure Hessian H_ij = ∂²p/∂x_i∂x_j
            # Compute p in Fourier: p̂ = -(k_ik_j/|k|²) (û_iû_j)^  [convolution]
            # Simpler: use Δp = |ω|²/2 - |S|²  to get p, then differentiate
            # Actually compute directly: p = -u_iu_j δ_ij from Poisson
            # In Fourier: p̂(k) = -(1/|k|²) Σ kᵢkⱼ FT(uᵢuⱼ)(k)
            ux=ifft(ux_h);uy=ifft(uy_h);uz=ifft(uz_h)
            u_phys=[ux,uy,uz]

            # Compute FT(u_i u_j) for each pair, then contract with k_i k_j
            p_hat=torch.zeros(N,N,N,dtype=torch.complex128,device=device)
            k_list_real=[kx,ky,kz]
            for i in range(3):
                for j in range(3):
                    uiuj_hat=fft(u_phys[i]*u_phys[j])
                    p_hat-=k_list_real[i]*k_list_real[j]*uiuj_hat/ksq
            p_hat[0,0,0]=0  # zero mean pressure

            # Pressure Hessian: H_ij = ∂²p/∂x_i∂x_j = IFFT(-k_i k_j p̂)
            H=torch.zeros(3,3,dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    H[i,j]=ifft(-k_list_real[i]*k_list_real[j]*p_hat*D)[ix,iy,iz].item()

            # ê·H·ê (pressure Hessian projected onto vorticity direction)
            eHe=(e_hat@H@e_hat).item()

            # Isotropic part of H
            H_iso=H.trace().item()/3  # = Δp/3

            # dα/dt ≈ -ê·S²·ê - ê·H·ê + ν·(ê·ΔS·ê)
            # The strain self-depletion + pressure opposition
            dalpha_self=-eS2e
            dalpha_pressure=-eHe
            dalpha_estimate=dalpha_self+dalpha_pressure  # ignoring viscous

            return {
                'rho': rho,
                'alpha': alpha,
                'eS2e': eS2e,
                'eHe': eHe,
                'H_iso': H_iso,
                'laplacian_p': laplacian_p,
                'S_norm_sq': S_norm_sq,
                'dalpha_self': dalpha_self,
                'dalpha_pressure': dalpha_pressure,
                'dalpha_estimate': dalpha_estimate,
                'self_depletion_ratio': -eS2e/(alpha+1e-30) if alpha>0 else 0,
                'pressure_opposes': eHe > 0 and alpha > 0,
            }

        # TG evolution
        print(f'\n{"="*70}')
        print(f'PRESSURE HESSIAN TEST — TG N={N}')
        print(f'Does ê·H·ê > 0 when α > 0? (pressure opposes stretching)')
        print(f'{"="*70}', flush=True)

        x=torch.linspace(0,2*math.pi-dx,N,device=device,dtype=torch.float64)
        X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z)
        uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        uz=torch.zeros_like(X)
        ux_h_init=D*fft(ux);uy_h_init=D*fft(uy);uz_h_init=D*fft(uz)
        wx_h=D*(iky*uz_h_init-ikz*uy_h_init)
        wy_h=D*(ikz*ux_h_init-ikx*uz_h_init)
        wz_h=D*(ikx*uy_h_init-iky*ux_h_init)

        dt=0.002; n_steps=2500
        series=[]
        t0=time.time()

        print(f'  {"t":>5} {"ρ":>8} {"α":>10} {"-ê·S²·ê":>10} {"-ê·H·ê":>10} {"Δp":>10} {"opposes?":>8}')

        for step in range(n_steps+1):
            if step%50==0:
                d=measure_strain_dynamics(wx_h,wy_h,wz_h)
                if d:
                    d['step']=step; d['time']=step*dt
                    series.append(d)
                    if step%250==0:
                        opp="YES" if d['pressure_opposes'] else "no"
                        print(f'  {d["time"]:5.2f} {d["rho"]:8.4f} {d["alpha"]:10.6f} '
                              f'{d["dalpha_self"]:10.6f} {d["dalpha_pressure"]:10.6f} '
                              f'{d["laplacian_p"]:10.4f} {opp:>8}', flush=True)
            if step<n_steps:
                wx_h,wy_h,wz_h=rk4(wx_h,wy_h,wz_h,dt)

        elapsed=time.time()-t0
        print(f'  [{elapsed:.0f}s]', flush=True)

        # Analysis
        pos_stretch=[d for d in series if d['alpha']>0]
        if pos_stretch:
            opposes_count=sum(1 for d in pos_stretch if d['pressure_opposes'])
            print(f'\n  When α > 0 ({len(pos_stretch)} samples):')
            print(f'    Pressure opposes stretching: {opposes_count}/{len(pos_stretch)} '
                  f'({100*opposes_count/len(pos_stretch):.0f}%)')
            print(f'    Mean -ê·S²·ê: {np.mean([d["dalpha_self"] for d in pos_stretch]):.6f} (want: < 0)')
            print(f'    Mean -ê·H·ê:  {np.mean([d["dalpha_pressure"] for d in pos_stretch]):.6f} (want: < 0)')
            print(f'    Mean dα/dt estimate: {np.mean([d["dalpha_estimate"] for d in pos_stretch]):.6f}')

            # The key ratio: does self-depletion exceed α?
            ratios=[d['self_depletion_ratio'] for d in pos_stretch if d['alpha']>0.01]
            if ratios:
                print(f'    ê·S²·ê / α (when α>0.01): mean={np.mean(ratios):.4f} '
                      f'(>1 means self-depletion exceeds stretching)')

        out=f'ns_blowup/results/pressure_hessian_N{N}.json'
        os.makedirs(os.path.dirname(out),exist_ok=True)
        with open(out,'w') as f:
            json.dump(series,f,indent=2)
        print(f'\n  Saved: {out}', flush=True)


if __name__=='__main__':
    run_pressure_test()
