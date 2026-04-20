"""Lean N=64 BKM curvature test. Only tracks ||ω||∞. No extras."""
import torch, numpy as np, math, time, gc
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N,nu=0.):
        s.N=N;s.nu=nu;L=2*pi;dx=L/N
        x=torch.linspace(0,L-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2;s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def curl(s,a,b,c):
        I=1j;return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq;p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j;return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D;F=torch.fft.fftn;iF=lambda x:torch.fft.ifftn(x).real
        u=s.vel(*w);f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=iF(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]):f[f'd{n}_d{d}']=iF(1j*kd*D*h)
        del u  # free memory
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*F(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        del f  # free memory
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c):return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        D=s.D
        r=tuple(D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
        del k1,k2,k3,k4
        return r
    def om_max(s,w):
        iF=lambda x:torch.fft.ifftn(x).real
        v=[iF(w[i]) for i in range(3)]
        r=(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()
        del v
        return r

def make_trefoil(s):
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
    cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
    cz=(-torch.sin(3*tp))*0.5+pi
    tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
    ds=2*pi/200
    for i in range(200):
        g=10.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    del X,Y,Z
    return(s.D*torch.fft.fftn(wx),s.D*torch.fft.fftn(wy),s.D*torch.fft.fftn(wz))

N=64; dt=3e-5; n_total=12000; sample=60  # t_final ≈ 0.36
print(f"N={N}, dt={dt}, {n_total} steps, t_final≈{n_total*dt:.3f}",flush=True)

gc.collect()
s=NS3D(N)
print(f"Solver created. Memory per complex field: {N**3*16/1e6:.1f} MB",flush=True)
w=make_trefoil(s)
del s.X, s.Y, s.Z  # free IC grid
gc.collect()

times=[];oms=[]
t=0.;t0=time.time()

for step in range(n_total+1):
    if step%sample==0:
        om=s.om_max(w)
        times.append(t);oms.append(om)
        if step%(sample*5)==0:
            el=time.time()-t0
            eta=(el/(step+1))*(n_total-step) if step>0 else 0
            print(f"  step={step:>5d}/{n_total} t={t:.4f} |ω|={om:.2f} "
                  f"[{el:.0f}s, eta {eta:.0f}s]",flush=True)
    if step<n_total:
        w=s.step(w,dt);t+=dt

times=np.array(times);oms=np.array(oms);inv=1.0/oms

# Curvature in second half
nh=len(times)//2
d2=np.gradient(np.gradient(inv[nh:],times[nh:]),times[nh:])
curv=d2.mean()

# Linear T*
c=np.polyfit(times[nh:],inv[nh:],1)
Ts=-c[1]/c[0] if c[0]<0 else float('inf')

el=time.time()-t0
print(f"\n{'='*60}",flush=True)
print(f"N=64 RESULT [{el:.0f}s]:",flush=True)
print(f"  t: [0, {times[-1]:.4f}]",flush=True)
print(f"  ||ω||∞: {oms[0]:.2f} → {oms[-1]:.2f}",flush=True)
print(f"  1/||ω||∞: {inv[0]:.5f} → {inv[-1]:.5f}",flush=True)
print(f"  Curvature d²(1/||ω||)/dt²: {curv:+.6f}",flush=True)
print(f"  Sign: {'CONCAVE UP → REGULARITY ✓' if curv>0 else 'CONCAVE DOWN → DANGER ✗'}",flush=True)
print(f"  Linear T*: {Ts:.3f}",flush=True)
print(f"\n  Compare N=32: curvature = +0.157 (concave up)",flush=True)
print(f"  N=64 {'AGREES' if curv>0 else 'DISAGREES'} with N=32",flush=True)

# Time series
print(f"\n  Time series:",flush=True)
for i in range(0,len(times),max(1,len(times)//15)):
    print(f"    t={times[i]:.4f}  |ω|={oms[i]:.2f}  1/|ω|={inv[i]:.5f}",flush=True)
print(f"{'='*60}",flush=True)
