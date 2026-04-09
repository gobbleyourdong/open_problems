"""
Multi-IC family infection test.
7 IC families x 3 resolutions x 50 seeds = bulletproof variety.
"""
import torch, math, time, json, os

dev = 'cuda'
nu = 1e-4
n_generations = 20
steps_per_gen = 10
dt = 0.005
n_seeds = 50

def run_infection(N, ic_func, ic_name, seeds):
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
        return stretch-nu*grad_w_sq, w_sq

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

    gen_fracs=[[] for _ in range(n_generations)]
    ctx = {'kx':kx,'ky':ky,'kz':kz,'ksq':ksq,'ikx':ikx,'iky':iky,'ikz':ikz,'D':D}

    for seed in seeds:
        wx_h,wy_h,wz_h = ic_func(N, seed, ctx)
        for gen in range(n_generations):
            growth,w_sq=compute_growth(wx_h,wy_h,wz_h)
            sig=w_sq>w_sq.max()*0.01
            n_g=((growth>0)&sig).sum().item()
            n_s=sig.sum().item()
            gen_fracs[gen].append(n_g/(n_s+1))
            for _ in range(steps_per_gen):
                wx_h,wy_h,wz_h=rk4(wx_h,wy_h,wz_h,dt)

    fg0=torch.tensor(gen_fracs[0]).mean().item()
    fg19=torch.tensor(gen_fracs[-1]).mean().item()
    return fg0, fg19


def ic_curl_noise(N, seed, ctx):
    torch.manual_seed(seed)
    mag = 10.0 / (ctx['ksq'] + 1); mag[0,0,0] = 0
    mask = ctx['ksq'] <= (N//2)**2
    Ax=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Ay=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Az=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_steep(N, seed, ctx):
    torch.manual_seed(seed)
    mag = 10.0 / (ctx['ksq']**2 + 1); mag[0,0,0] = 0
    mask = ctx['ksq'] <= (N//2)**2
    Ax=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Ay=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Az=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_flat(N, seed, ctx):
    torch.manual_seed(seed)
    mag = 10.0 / (ctx['ksq'].sqrt() + 1); mag[0,0,0] = 0
    mask = ctx['ksq'] <= (N//2)**2
    Ax=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Ay=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Az=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_low_mode(N, seed, ctx):
    torch.manual_seed(seed)
    mag = 50.0 * (ctx['ksq'] <= 5).to(torch.float64); mag[0,0,0] = 0
    Ax=mag*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Ay=mag*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Az=mag*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_taylor_green(N, seed, ctx):
    torch.manual_seed(seed)
    Lx=2*math.pi; dx=Lx/N
    x=torch.linspace(0,Lx-dx,N,device=dev,dtype=torch.float64)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    amp=5.0*(1+seed%3)
    ux=amp*torch.cos(X)*torch.sin(Y)*torch.cos(Z)+0.1*amp*torch.randn_like(X)
    uy=-amp*torch.sin(X)*torch.cos(Y)*torch.cos(Z)+0.1*amp*torch.randn_like(X)
    uz=0.1*amp*torch.randn_like(X)
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=D*torch.fft.fftn(ux);uy_h=D*torch.fft.fftn(uy);uz_h=D*torch.fft.fftn(uz)
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_kida_pelz(N, seed, ctx):
    torch.manual_seed(seed)
    Lx=2*math.pi; dx=Lx/N
    x=torch.linspace(0,Lx-dx,N,device=dev,dtype=torch.float64)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    amp=5.0*(1+seed%3)
    ux=amp*torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))+0.1*amp*torch.randn_like(X)
    uy=amp*torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))+0.1*amp*torch.randn_like(X)
    uz=amp*torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))+0.1*amp*torch.randn_like(X)
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=D*torch.fft.fftn(ux);uy_h=D*torch.fft.fftn(uy);uz_h=D*torch.fft.fftn(uz)
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)

def ic_high_amp(N, seed, ctx):
    torch.manual_seed(seed)
    mag = 100.0 / (ctx['ksq'] + 1); mag[0,0,0] = 0
    mask = ctx['ksq'] <= (N//2)**2
    Ax=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Ay=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    Az=mag*mask*(torch.randn(N,N,N,device=dev)+1j*torch.randn(N,N,N,device=dev))
    ikx,iky,ikz,D=ctx['ikx'],ctx['iky'],ctx['ikz'],ctx['D']
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    return D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)


ic_families = {
    'curl_noise': ic_curl_noise,
    'steep_k4': ic_steep,
    'flat_k1': ic_flat,
    'low_mode': ic_low_mode,
    'taylor_green': ic_taylor_green,
    'kida_pelz': ic_kida_pelz,
    'high_amp': ic_high_amp,
}

results = {}
t0 = time.time()

for N in [32, 64, 128]:
    for ic_name, ic_func in ic_families.items():
        seeds = list(range(n_seeds))
        t1 = time.time()
        fg0, fg19 = run_infection(N, ic_func, ic_name, seeds)
        elapsed = time.time() - t1
        results[f'N{N}_{ic_name}'] = {'N': N, 'ic': ic_name, 'frac_gen0': fg0, 'frac_gen19': fg19}
        print(f'N={N:3d} {ic_name:15s}: gen0={fg0:.6f} gen19={fg19:.6f} [{elapsed:.0f}s]', flush=True)

print(f'\n{"="*65}')
print(f'MULTI-IC CONVERGENCE TABLE')
print(f'{"="*65}')
print(f'{"IC family":>15} {"N=32":>12} {"N=64":>12} {"N=128":>12}')
for ic_name in ic_families:
    vals = []
    for N in [32, 64, 128]:
        key = f'N{N}_{ic_name}'
        if key in results:
            vals.append(f'{results[key]["frac_gen0"]:.6f}')
        else:
            vals.append('--')
    print(f'{ic_name:>15} {vals[0]:>12} {vals[1]:>12} {vals[2]:>12}')

total_elapsed = time.time() - t0
print(f'\nTotal: {total_elapsed:.0f}s')

with open('/root/multi_ic_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print('Saved /root/multi_ic_results.json', flush=True)
