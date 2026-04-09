"""
Cross-validate |H_dev|/|H_iso| < 1 at high |ω|:
1. Multiple ICs (TG, KP, trefoil)
2. N=32 and N=48
3. Multiple times

Is the ratio a UNIVERSAL constant or IC-dependent?
"""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N=32,nu=0.):
        s.N=N;s.nu=nu;s.Lx=2*pi;dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2;s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def fft(s,f):return torch.fft.fftn(f)
    def ifft(s,f):return torch.fft.ifftn(f).real
    def curl(s,a,b,c):
        I=1j;return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq;p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j;return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D;u=s.vel(*w);f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]):f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c):return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        return tuple(s.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))

def measure_ratio_at_high_omega(s, w, frac_lo=0.8):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()
    om_max=om.max().item()
    if om_max<1e-10:return None

    mask=om>frac_lo*om_max
    idx=mask.nonzero(as_tuple=False)
    n=min(len(idx),1000);perm=torch.randperm(len(idx))[:n];pts=idx[perm]

    hww_list=[];hiso_list=[];hdev_list=[];trH_list=[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm();
        if wn<1e-12:continue
        eh=wv/wn;Hl=H[:,:,ix,iy,iz]
        trH=Hl.trace().item();hww=(eh@Hl@eh).item()
        hiso=trH/3;hdev=hww-hiso
        hww_list.append(hww);hiso_list.append(hiso);hdev_list.append(hdev);trH_list.append(trH)

    if not hww_list:return None
    ha=np.array(hww_list);hi=np.array(hiso_list);hd=np.array(hdev_list)
    ratio=np.abs(hd).mean()/(np.abs(hi).mean()+1e-30)
    return {
        'Hww_mean':ha.mean(),'Hiso_mean':hi.mean(),'Hdev_mean':hd.mean(),
        'ratio':ratio,'Hww_pos':(ha>0).mean(),'om_max':om_max,'n':len(ha),
        'trH_mean':np.mean(trH_list)
    }

def make_ic(s,name):
    X,Y,Z=s.X,s.Y,s.Z
    if name=='TG':
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))
    elif name=='KP':
        ux=torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
        uy=torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
        uz=torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
        return s.curl(s.fft(ux),s.fft(uy),s.fft(uz))
    elif name=='trefoil':
        wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
        tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
        cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
        cz=(-torch.sin(3*tp))*0.5+pi
        tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
        ds=2*pi/200
        for i in range(200):
            g=10.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
            wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
        return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    print("="*70,flush=True)
    print("|H_dev|/|H_iso| CROSS-VALIDATION at |ω| > 80% of max",flush=True)
    print("="*70,flush=True)
    print(f"  Need ratio < 1 for H_ωω > 0 (regularity)\n",flush=True)

    print(f"  {'IC':>10s}  {'N':>3s}  {'t':>5s}  {'||ω||∞':>7s}  {'ratio':>6s}  "
          f"{'<H_ωω>':>8s}  {'<H_iso>':>8s}  {'<H_dev>':>8s}  {'H>0%':>5s}  {'<1?':>4s}",flush=True)
    print("-"*80,flush=True)

    all_ratios=[]
    for ic_name in ['TG','KP','trefoil']:
        for N_test in [32,48]:
            dt=1e-4 if N_test==32 else 5e-5
            s=NS3D(N_test,0.);w=make_ic(s,ic_name)
            t=0.
            for epoch in range(6):
                n_step=500 if N_test==32 else 600
                for _ in range(n_step):w=s.step(w,dt);t+=dt
                r=measure_ratio_at_high_omega(s,w,frac_lo=0.8)
                if r is None:continue
                ok="YES" if r['ratio']<1 else "**NO**"
                all_ratios.append(r['ratio'])
                if epoch%2==0:
                    print(f"  {ic_name:>10s}  {N_test:3d}  {t:5.3f}  {r['om_max']:7.2f}  "
                          f"{r['ratio']:6.3f}  {r['Hww_mean']:+8.3f}  "
                          f"{r['Hiso_mean']:+8.3f}  {r['Hdev_mean']:+8.3f}  "
                          f"{r['Hww_pos']*100:4.0f}%  {ok:>4s}",flush=True)

    all_r=np.array(all_ratios)
    print(f"\n{'='*70}",flush=True)
    print(f"SUMMARY ({len(all_r)} measurements):",flush=True)
    print(f"  Ratio mean: {all_r.mean():.4f}",flush=True)
    print(f"  Ratio max:  {all_r.max():.4f}",flush=True)
    print(f"  Ratio min:  {all_r.min():.4f}",flush=True)
    print(f"  Ratio < 1:  {(all_r<1).sum()}/{len(all_r)} ({100*(all_r<1).mean():.0f}%)",flush=True)
    print(f"  UNIVERSAL: {'YES ✓' if (all_r<1).all() else 'NOT ALWAYS'}",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
