"""
Local Beltramization at x*: does u align with ω as |ω| grows?

If cos(u,ω) → 1 at x* as ρ → ∞:
  → (ω·∇)u has no stretching component (ω × u → 0)
  → α = ξ·S·ξ → 0
  → regularity

Buaria et al. (2020) showed this statistically.
We measure it pointwise at x* during TG evolution.
"""
import torch, math, time, json, os, numpy as np

def run_beltramization(N=64, nu=1e-4, device='cuda'):
    Lx=2*math.pi; dx=Lx/N
    k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device=device,dtype=torch.float64)
    kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
    ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    ikx,iky,ikz=1j*kx,1j*ky,1j*kz
    kmax=N//3; D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
    ifft=lambda f:torch.fft.ifftn(f*D).real; fft=torch.fft.fftn

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

    # TG evolution
    x=torch.linspace(0,2*math.pi-dx,N,device=device,dtype=torch.float64)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    ux_init=torch.cos(X)*torch.sin(Y)*torch.cos(Z)
    uy_init=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
    uz_init=torch.zeros_like(X)
    ux_h=D*fft(ux_init);uy_h=D*fft(uy_init);uz_h=D*fft(uz_init)
    wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

    dt=0.002; n_steps=2500
    print(f'BELTRAMIZATION TEST — TG N={N}')
    print(f't      ρ       |u|@x*  cos(u,ω)  α         |ω×u|/|ω||u|', flush=True)

    series = []
    for step in range(n_steps+1):
        if step % 100 == 0:
            wx=ifft(wx_h*D);wy=ifft(wy_h*D);wz=ifft(wz_h*D)
            om_mag=(wx**2+wy**2+wz**2).sqrt()
            max_idx=om_mag.argmax().item()
            ix=max_idx//(N*N);iy=(max_idx%(N*N))//N;iz=max_idx%N
            rho=om_mag[ix,iy,iz].item()

            # Velocity at x* from Biot-Savart
            px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
            px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
            uxh=iky*pz-ikz*py;uyh=ikz*px-ikx*pz;uzh=ikx*py-iky*px
            ux_phys=ifft(uxh);uy_phys=ifft(uyh);uz_phys=ifft(uzh)

            u_at_x = torch.tensor([ux_phys[ix,iy,iz].item(),
                                   uy_phys[ix,iy,iz].item(),
                                   uz_phys[ix,iy,iz].item()], dtype=torch.float64)
            w_at_x = torch.tensor([wx[ix,iy,iz].item(),
                                   wy[ix,iy,iz].item(),
                                   wz[ix,iy,iz].item()], dtype=torch.float64)

            u_norm = u_at_x.norm().item()
            w_norm = w_at_x.norm().item()

            if u_norm > 1e-30 and w_norm > 1e-30:
                cos_uw = (u_at_x @ w_at_x).item() / (u_norm * w_norm)
                cross = torch.linalg.cross(w_at_x, u_at_x)
                sin_uw = cross.norm().item() / (u_norm * w_norm)
            else:
                cos_uw = 0; sin_uw = 0

            # Stretching
            e_hat = w_at_x / (w_norm + 1e-30)
            ik_list=[ikx,iky,ikz]; u_hats=[uxh,uyh,uzh]
            S=torch.zeros(3,3,dtype=torch.float64)
            for i in range(3):
                for j in range(3):
                    S[i,j]=ifft(ik_list[j]*u_hats[i]*D)[ix,iy,iz].item()
            S=0.5*(S+S.T)
            alpha=(e_hat@S@e_hat).item()

            d = {'time': step*dt, 'rho': rho, 'u_norm': u_norm,
                 'cos_uw': cos_uw, 'sin_uw': sin_uw, 'alpha': alpha}
            series.append(d)

            if step % 250 == 0:
                print(f'{step*dt:5.2f}  {rho:7.4f}  {u_norm:7.4f}  {cos_uw:+8.4f}  {alpha:+9.6f}  {sin_uw:8.4f}',
                      flush=True)

        if step < n_steps:
            wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)

    # Analysis: does cos(u,ω) correlate with ρ?
    rhos = [d['rho'] for d in series if d['rho'] > 1]
    cos_abs = [abs(d['cos_uw']) for d in series if d['rho'] > 1]
    sins = [d['sin_uw'] for d in series if d['rho'] > 1]

    if len(rhos) > 5:
        log_rho = np.log(rhos)
        log_cos = np.log([max(c, 1e-10) for c in cos_abs])
        log_sin = np.log([max(s, 1e-10) for s in sins])
        if np.std(log_rho) > 0.1:
            beta_cos = np.polyfit(log_rho, log_cos, 1)[0]
            beta_sin = np.polyfit(log_rho, log_sin, 1)[0]
        else:
            beta_cos = beta_sin = 0
        print(f'\nSCALING:')
        print(f'  |cos(u,ω)| ~ ρ^{beta_cos:.3f}')
        print(f'  sin(u,ω) ~ ρ^{beta_sin:.3f}')
        print(f'  If beta_cos > 0: Beltramization INCREASES with vorticity')
        print(f'  If beta_sin < 0: misalignment |ω×u| DECREASES with vorticity')

    out = 'ns_blowup/results/beltramization.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(series, f, indent=2)
    print(f'\nSaved: {out}', flush=True)

if __name__ == '__main__':
    run_beltramization()
