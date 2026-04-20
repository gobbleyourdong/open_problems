"""
Filament curvature at x* and stretching event duration.

Two measurements that could unlock the proof:
1. κ(x*) vs ρ — does curvature grow with vorticity? If κ ~ ρ^β, β > 0 → Path B works
2. Duration of α > 0 events — does it scale as 1/|S|? If yes → anti-twist is quantifiable

Run during TG evolution where ρ grows dynamically (the real test).
"""
import torch
import math
import time
import json
import os
import numpy as np


def run_curvature_events(N_values=None, nu=1e-4, device='cuda'):
    if N_values is None:
        N_values = [32, 64, 128]

    all_results = {}

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

        def measure_full(wx_h, wy_h, wz_h):
            wx=ifft(wx_h*D);wy=ifft(wy_h*D);wz=ifft(wz_h*D)
            om_mag=(wx**2+wy**2+wz**2).sqrt()
            max_idx=om_mag.argmax().item()
            ix=max_idx//(N*N);iy=(max_idx%(N*N))//N;iz=max_idx%N
            rho=om_mag[ix,iy,iz].item()
            if rho < 1e-30: return None

            w_hats=[wx_h,wy_h,wz_h]
            e_hat=torch.tensor([wx[ix,iy,iz].item(),wy[ix,iy,iz].item(),
                                wz[ix,iy,iz].item()],dtype=torch.float64)
            e_hat=e_hat/(e_hat.norm()+1e-30)

            # ∇ω at x*
            grad_om=torch.zeros(3,3,dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    grad_om[i,j]=ifft(ik_list[j]*w_hats[i]*D)[ix,iy,iz].item()

            # |∇ω|²
            grad_om_sq=(grad_om**2).sum().item()

            # ∇ξ = ∇ω/ρ at x*
            grad_xi=grad_om/rho
            grad_xi_sq=(grad_xi**2).sum().item()

            # Curvature of vortex line κ = |dξ/ds| where s is arc length along ξ
            # dξ/ds = (ξ·∇)ξ = projected directional derivative of ξ along ξ
            # κ² = |dξ/ds|² = Σᵢ (Σⱼ ξⱼ ∂ξᵢ/∂xⱼ)²
            dxi_ds = torch.zeros(3, dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    dxi_ds[i] += e_hat[j].item() * grad_xi[i,j].item()
            # Project out component along ξ (κ is perpendicular to ξ)
            dxi_ds_parallel = (dxi_ds @ e_hat) * e_hat
            dxi_ds_perp = dxi_ds - dxi_ds_parallel
            kappa = dxi_ds_perp.norm().item()

            # Strain and stretching
            px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
            u_hats=[ux_h,uy_h,uz_h]
            S=torch.zeros(3,3,dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    S[i,j]=ifft(ik_list[j]*u_hats[i]*D)[ix,iy,iz].item()
            S=0.5*(S+S.T)
            eigvals,eigvecs=torch.linalg.eigh(S)
            alpha=(e_hat@S@e_hat).item()
            S_norm=eigvals[-1].item()

            # Bending cost
            bending_cost = nu * grad_xi_sq

            # Anti-twist fraction c = bending_cost / alpha (when alpha > 0)
            c_fraction = bending_cost / (alpha + 1e-30) if alpha > 0 else 0.0

            return {
                'rho': rho,
                'kappa': kappa,
                'alpha': alpha,
                'S_norm': S_norm,
                'grad_xi_sq': grad_xi_sq,
                'bending_cost': bending_cost,
                'c_fraction': c_fraction,
                'grad_om_sq': grad_om_sq,
            }

        # TG evolution — the real test where ρ grows
        print(f'\n{"="*70}')
        print(f'TG EVOLUTION N={N} — curvature and event tracking')
        print(f'{"="*70}', flush=True)

        x=torch.linspace(0,2*math.pi-dx,N,device=device,dtype=torch.float64)
        X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z)
        uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        uz=torch.zeros_like(X)
        ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
        wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

        dt=0.002; n_steps=2500  # T=5
        sample_every=5  # fine sampling for event detection

        series=[]
        t0=time.time()
        for step in range(n_steps+1):
            if step % sample_every == 0:
                d=measure_full(wx_h,wy_h,wz_h)
                if d:
                    d['step']=step; d['time']=step*dt
                    series.append(d)
            if step < n_steps:
                wx_h,wy_h,wz_h=rk4(wx_h,wy_h,wz_h,dt)

        elapsed=time.time()-t0

        # Analyze stretching events
        alphas=[d['alpha'] for d in series]
        rhos=[d['rho'] for d in series]
        kappas=[d['kappa'] for d in series]
        times_arr=[d['time'] for d in series]

        # Find stretching events (contiguous periods where alpha > 0)
        events=[]
        in_event=False
        event_start=0
        event_alpha_sum=0
        for i,a in enumerate(alphas):
            if a > 0 and not in_event:
                in_event=True
                event_start=i
                event_alpha_sum=a*sample_every*dt
            elif a > 0 and in_event:
                event_alpha_sum+=a*sample_every*dt
            elif a <= 0 and in_event:
                in_event=False
                duration=times_arr[i]-times_arr[event_start]
                peak_alpha=max(alphas[event_start:i])
                mean_rho=np.mean(rhos[event_start:i])
                mean_kappa=np.mean(kappas[event_start:i])
                events.append({
                    'start': times_arr[event_start],
                    'duration': duration,
                    'peak_alpha': peak_alpha,
                    'integral': event_alpha_sum,
                    'mean_rho': mean_rho,
                    'mean_kappa': mean_kappa,
                })
                event_alpha_sum=0

        # Print results
        print(f'\n  Time series (sampled every {sample_every} steps):')
        print(f'  {"t":>6} {"ρ":>8} {"κ":>8} {"α":>10} {"|S|":>8} {"ν|∇ξ|²":>10} {"c":>6}')
        for d in series[::50]:  # print every 50th sample
            print(f'  {d["time"]:6.2f} {d["rho"]:8.4f} {d["kappa"]:8.4f} '
                  f'{d["alpha"]:10.6f} {d["S_norm"]:8.4f} {d["bending_cost"]:10.6f} '
                  f'{d["c_fraction"]:6.2f}', flush=True)

        # κ vs ρ scaling
        valid=[(d['rho'],d['kappa']) for d in series if d['rho']>0.5 and d['kappa']>1e-10]
        if len(valid)>5:
            log_rho=np.log([v[0] for v in valid])
            log_kappa=np.log([v[1] for v in valid])
            if np.std(log_rho)>0.1:
                beta=np.polyfit(log_rho,log_kappa,1)[0]
            else:
                beta=0
        else:
            beta=0

        print(f'\n  CURVATURE SCALING: κ ~ ρ^β with β = {beta:.3f}')
        if beta > 0:
            print(f'  → Curvature GROWS with vorticity (good for proof)')
        elif beta < -0.1:
            print(f'  → Curvature SHRINKS with vorticity (bad)')
        else:
            print(f'  → Curvature approximately constant')

        # Event analysis
        print(f'\n  STRETCHING EVENTS (α > 0 episodes):')
        print(f'  Found {len(events)} events in T={n_steps*dt}')
        if events:
            print(f'  {"start":>6} {"dur":>8} {"peak_α":>10} {"∫α":>10} {"ρ_mean":>8} {"κ_mean":>8}')
            for e in events:
                print(f'  {e["start"]:6.2f} {e["duration"]:8.4f} {e["peak_alpha"]:10.6f} '
                      f'{e["integral"]:10.6f} {e["mean_rho"]:8.4f} {e["mean_kappa"]:8.4f}', flush=True)

            durations=[e['duration'] for e in events]
            peak_alphas=[e['peak_alpha'] for e in events]
            integrals=[e['integral'] for e in events]

            print(f'\n  Duration: mean={np.mean(durations):.4f} max={np.max(durations):.4f}')
            print(f'  Peak α:  mean={np.mean(peak_alphas):.6f} max={np.max(peak_alphas):.6f}')
            print(f'  ∫α per event: mean={np.mean(integrals):.6f} total={np.sum(integrals):.6f}')

            # Does duration scale as 1/|S|?
            if len(events)>3:
                dur_arr=np.array(durations)
                S_arr=np.array([e['mean_rho'] for e in events])  # proxy for |S|
                if np.std(np.log(S_arr+1e-10))>0.1:
                    dur_scaling=np.polyfit(np.log(S_arr+1e-10),np.log(dur_arr+1e-10),1)[0]
                    print(f'  Duration scaling: τ ~ ρ^{dur_scaling:.2f} (want: -1 for τ~1/|S|)')

        all_results[str(N)]={
            'beta': float(beta),
            'n_events': len(events),
            'events': events,
            'total_stretch_pos': float(np.sum(integrals)) if events else 0,
            'series_summary': {
                'rho_max': float(max(rhos)),
                'kappa_max': float(max(kappas)),
                'alpha_max': float(max(alphas)),
                'alpha_min': float(min(alphas)),
            },
        }
        print(f'  [{elapsed:.0f}s]', flush=True)

    # Cross-resolution summary
    print(f'\n{"="*70}')
    print('CROSS-RESOLUTION SUMMARY')
    print(f'{"="*70}')
    print(f'{"N":>6} {"β(κ~ρ^β)":>10} {"events":>8} {"Σ∫α₊":>10} {"ρ_max":>8} {"κ_max":>8}')
    for n_key in sorted(all_results.keys(),key=int):
        d=all_results[n_key]
        s=d['series_summary']
        print(f'{int(n_key):6d} {d["beta"]:10.3f} {d["n_events"]:8d} '
              f'{d["total_stretch_pos"]:10.6f} {s["rho_max"]:8.4f} {s["kappa_max"]:8.4f}')

    out='ns_blowup/results/curvature_events.json'
    os.makedirs(os.path.dirname(out),exist_ok=True)
    with open(out,'w') as f:
        json.dump(all_results,f,indent=2)
    print(f'\nSaved: {out}',flush=True)


if __name__=='__main__':
    run_curvature_events()
