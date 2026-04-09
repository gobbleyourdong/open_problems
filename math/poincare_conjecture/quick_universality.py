"""Quick universality test: 5 random ICs, Euler, short evolution."""
import torch, numpy as np, math, sys
DTYPE = torch.float64; pi = math.pi

class S3D:
    def __init__(s, N=32, nu=0.):
        s.N=N; s.nu=nu; s.Lx=2*pi; dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2; s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def fft(s,f): return torch.fft.fftn(f)
    def ifft(s,f): return torch.fft.ifftn(f).real
    def curl(s,a,b,c):
        I=1j; return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq; p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j; return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D; u=s.vel(*w)
        f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]): f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c): return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        return tuple(s.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)]; return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()

def alignment(s,w,pct=0.9,n=1500):
    D=s.D;N=s.N;u=s.vel(*w);kd=[s.kx,s.ky,s.kz];uh=[*u]
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*uh[i])
    S=.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    thr=torch.quantile(om.flatten(),pct)
    if thr<1e-10: return .33,.33,.33,0.
    idx=(om>thr).nonzero(as_tuple=False)
    m=min(len(idx),n)
    if m==0: return .33,.33,.33,0.
    p=torch.randperm(len(idx))[:m]; pts=idx[p]
    c1s,c2s,c3s,als=[],[],[],[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        Sl=S[:,:,ix,iy,iz].clone()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12: continue
        wh=wv/wn
        ev,ec=torch.linalg.eigh(Sl)
        c1=(wh@ec[:,2]).item()**2;c2=(wh@ec[:,1]).item()**2;c3=(wh@ec[:,0]).item()**2
        al=ev[2].item()*c1+ev[1].item()*c2+ev[0].item()*c3
        c1s.append(c1);c2s.append(c2);c3s.append(c3);als.append(al)
    if not c1s: return .33,.33,.33,0.
    return np.mean(c1s),np.mean(c2s),np.mean(c3s),np.mean(als)

def rand_ic(s,km=4,amp=10.,seed=0):
    torch.manual_seed(seed);N=s.N
    Ah=[torch.zeros(N,N,N,dtype=torch.complex128) for _ in range(3)]
    for i in range(-km,km+1):
        for j in range(-km,km+1):
            for k in range(-km,km+1):
                q=i*i+j*j+k*k
                if q==0 or q>km**2: continue
                m=amp/q; ii,jj,kk=i%N,j%N,k%N
                for a in Ah: a[ii,jj,kk]=m*(torch.randn(1)+1j*torch.randn(1)).item()
    I=1j
    ux=I*s.ky*Ah[2]-I*s.kz*Ah[1];uy=I*s.kz*Ah[0]-I*s.kx*Ah[2];uz=I*s.kx*Ah[1]-I*s.ky*Ah[0]
    return s.curl(ux,uy,uz)

N=32; dt=2e-4; steps=1000  # t=0.2

print("="*60,flush=True)
print("QUICK UNIVERSALITY: Euler, 5 random + 3 named ICs",flush=True)
print("="*60,flush=True)

# Named ICs
for name in ['TG','KP','ABC']:
    s=S3D(N,0.)
    if name=='TG':
        X,Y,Z=s.X,s.Y,s.Z
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z);uz=torch.zeros_like(X)
        w=s.curl(s.fft(ux),s.fft(uy),s.fft(uz))
    elif name=='KP':
        X,Y,Z=s.X,s.Y,s.Z
        ux=torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
        uy=torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
        uz=torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
        w=s.curl(s.fft(ux),s.fft(uy),s.fft(uz))
    else:
        X,Y,Z=s.X,s.Y,s.Z
        ux=torch.sin(Z)+0.6*torch.cos(Y);uy=0.8*torch.sin(X)+torch.cos(Z);uz=0.6*torch.sin(Y)+0.8*torch.cos(X)
        w=s.curl(s.fft(ux),s.fft(uy),s.fft(uz))

    om0=s.om_max(w)
    c1_0,c2_0,c3_0,a0=alignment(s,w)
    t=0.
    for st in range(steps): w=s.step(w,dt); t+=dt
    om=s.om_max(w)
    c1,c2,c3,al=alignment(s,w)
    mk="✓" if c3>=.333 else " "
    am="≤0" if al<=0 else ">0"
    print(f"  {name:8s}: |ω|₀={om0:.1f}→{om:.1f} c₁={c1:.3f} c₃={c3:.3f} α={al:.4f} {mk} {am}",flush=True)
    print(f"           init: c₁={c1_0:.3f} c₃={c3_0:.3f}",flush=True)

# Random ICs
print(f"\nRandom ICs (Euler, amp=10, k_max=4):",flush=True)
c3f=[]; alf=[]
for seed in range(10):
    s=S3D(N,0.)
    w=rand_ic(s,km=4,amp=10.,seed=seed)
    om0=s.om_max(w)
    t=0.
    for st in range(steps): w=s.step(w,dt); t+=dt
    om=s.om_max(w)
    c1,c2,c3,al=alignment(s,w)
    c3f.append(c3); alf.append(al)
    mk="✓" if c3>=.333 else " "
    am="≤0" if al<=0 else ">0"
    print(f"  seed={seed:2d}: |ω|₀={om0:.1f}→{om:.1f} c₁={c1:.3f} c₃={c3:.3f} α={al:.4f} {mk} {am}",flush=True)

c3f=np.array(c3f); alf=np.array(alf)
print(f"\n  c₃ ≥ 1/3: {(c3f>=.333).sum()}/{len(c3f)} ({100*(c3f>=.333).mean():.0f}%)",flush=True)
print(f"  α ≤ 0:    {(alf<=0).sum()}/{len(alf)} ({100*(alf<=0).mean():.0f}%)",flush=True)
print(f"  mean c₃:  {c3f.mean():.4f} ± {c3f.std():.4f}",flush=True)
print(f"  mean α:   {alf.mean():.4f} ± {alf.std():.4f}",flush=True)
print(f"\n{'='*60}",flush=True)
print("DONE.",flush=True)
