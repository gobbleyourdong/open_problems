import torch, math, time, json, os

N = 512
nu = 1e-4
dev = 'cuda'
n_seeds = 20
n_generations = 50
steps_per_gen = 10
dt = 0.005

Lx=2*math.pi; dx=Lx/N
k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device=dev,dtype=torch.float64)
kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
ikx,iky,ikz=1j*kx,1j*ky,1j*kz
kmax=N//3
D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)

ifft=lambda f:torch.fft.ifftn(f*D).real
fft=torch.fft.fftn

def compute_growth(wx_h,wy_h,wz_h):
    px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
    px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
    ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
    wx,wy,wz=ifft(wx_h),ifft(wy_h),ifft(wz_h)
    gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
    gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
    gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
    stretch=wx*(gxx*wx+gxy*wy+gxz*wz)+wy*(gyx*wx+gyy*wy+gyz*wz)+wz*(gzx*wx+gzy*wy+gzz*wz)
    dwx_dx=ifft(ikx*wx_h*D);dwx_dy=ifft(iky*wx_h*D);dwx_dz=ifft(ikz*wx_h*D)
    dwy_dx=ifft(ikx*wy_h*D);dwy_dy=ifft(iky*wy_h*D);dwy_dz=ifft(ikz*wy_h*D)
    dwz_dx=ifft(ikx*wz_h*D);dwz_dy=ifft(iky*wz_h*D);dwz_dz=ifft(ikz*wz_h*D)
    grad_w_sq=dwx_dx**2+dwx_dy**2+dwx_dz**2+dwy_dx**2+dwy_dy**2+dwy_dz**2+dwz_dx**2+dwz_dy**2+dwz_dz**2
    w_sq=wx**2+wy**2+wz**2
    growth=stretch-nu*grad_w_sq
    return growth, w_sq

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

print(f'Taylor-Green N={N} on H100: {n_seeds} seeds, {n_generations} gens', flush=True)
gen_fracs=[[] for _ in range(n_generations)]
gen_net=[[] for _ in range(n_generations)]
t0=time.time()

for seed in range(n_seeds):
    torch.manual_seed(seed)
    x=torch.linspace(0,Lx-dx,N,device=dev,dtype=torch.float64)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    amp=5.0*(1+seed%3)
    ux=amp*torch.cos(X)*torch.sin(Y)*torch.cos(Z)+0.1*amp*torch.randn_like(X)
    uy=-amp*torch.sin(X)*torch.cos(Y)*torch.cos(Z)+0.1*amp*torch.randn_like(X)
    uz=0.1*amp*torch.randn_like(X)
    ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
    wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)
    del X,Y,Z,ux,uy,uz,ux_h,uy_h,uz_h

    for gen in range(n_generations):
        growth,w_sq=compute_growth(wx_h,wy_h,wz_h)
        sig=w_sq>w_sq.max()*0.01
        n_g=((growth>0)&sig).sum().item()
        n_s=sig.sum().item()
        gen_fracs[gen].append(n_g/(n_s+1))
        # Also track net growth
        net=growth[sig].sum().item()
        total_wsq=w_sq[sig].sum().item()
        gen_net[gen].append(net/(total_wsq+1e-30))
        del growth, w_sq
        for _ in range(steps_per_gen):
            wx_h,wy_h,wz_h=rk4(wx_h,wy_h,wz_h,dt)

    if(seed+1)%5==0:
        elapsed=time.time()-t0
        frac_traj=' '.join(f'{torch.tensor(gen_fracs[g]).mean():.4f}' for g in [0,9,19,29,39,49])
        net_traj=' '.join(f'{torch.tensor(gen_net[g]).mean():.4f}' for g in [0,9,49])
        print(f'  [{seed+1}/{n_seeds}] frac: {frac_traj} | net: {net_traj} [{elapsed:.0f}s]',flush=True)

    del wx_h,wy_h,wz_h
    torch.cuda.empty_cache()

trajectory=[torch.tensor(gen_fracs[g]).mean().item() for g in range(n_generations)]
net_trajectory=[torch.tensor(gen_net[g]).mean().item() for g in range(n_generations)]
fg0=trajectory[0]; fg49=trajectory[-1]
net0=net_trajectory[0]; net49=net_trajectory[-1]

print(f'\nTaylor-Green N={N}:')
print(f'  frac: gen0={fg0:.6f} gen49={fg49:.6f}')
print(f'  net:  gen0={net0:.6f} gen49={net49:.6f}')
print(f'  net negative = regularity regardless of frac')

with open('ns_blowup/results/tg_n512.json','w') as f:
    json.dump({'N':N,'ic':'taylor_green','n_seeds':n_seeds,'n_generations':n_generations,
               'frac_gen0':fg0,'frac_gen49':fg49,'net_gen0':net0,'net_gen49':net49,
               'frac_trajectory':trajectory,'net_trajectory':net_trajectory},f,indent=2)
print('Saved ns_blowup/results/tg_n512.json',flush=True)
