"""
Stress test: measure C at the max-|ω| point for 20 random ICs.

Each IC: random divergence-free field with energy at k=1-4, amplitude
scaled so |ω|₀ ≈ 10-20. Evolve with Euler for 500 steps.
Measure C = (dα/dt + ê·S²·ê) / |ω|² at the max point.

If ALL have C < 1/4: the bound is robust across geometries.
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
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)];return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()

def alpha_at_max(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return 0.,0.,0.
    eh=wv/wn;Sl=S[:,:,ix,iy,iz]
    return (eh@Sl@eh).item(),(eh@Sl@Sl@eh).item(),wn.item()

def random_ic(s, seed, target_om=15.0):
    """Random div-free IC with |ω|_max ≈ target_om."""
    torch.manual_seed(seed); N=s.N
    # Random vector potential at k=1-4
    Ah=[torch.zeros(N,N,N,dtype=torch.complex128) for _ in range(3)]
    for i in range(-4,5):
        for j in range(-4,5):
            for k in range(-4,5):
                q=i*i+j*j+k*k
                if q==0 or q>16: continue
                mag=1.0/q  # 1/k² spectrum
                ii,jj,kk=i%N,j%N,k%N
                for a in Ah: a[ii,jj,kk]=mag*(torch.randn(1)+1j*torch.randn(1)).item()
    I=1j
    ux=I*s.ky*Ah[2]-I*s.kz*Ah[1]; uy=I*s.kz*Ah[0]-I*s.kx*Ah[2]; uz=I*s.kx*Ah[1]-I*s.ky*Ah[0]
    w=s.curl(ux,uy,uz)
    # Scale to target |ω|_max
    om=s.om_max(w)
    if om>1e-10:
        scale=target_om/om
        w=tuple(wi*scale for wi in w)
    return w

def measure_C_series(s, w, dt, n_evolve=300, n_fd=20, n_measurements=10):
    """Evolve and measure C at max point multiple times."""
    # Skip initial transient
    for _ in range(100): w=s.step(w,dt)

    Cs=[]; a_prev=None
    for m in range(n_measurements):
        alpha,S2ee,om=alpha_at_max(s,w)
        if a_prev is not None and om > 1:
            dalpha=(alpha-a_prev)/(n_fd*dt)
            R=dalpha+S2ee
            C=R/(om**2+1e-30)
            Cs.append(C)
        a_prev=alpha
        for _ in range(n_fd): w=s.step(w,dt)
    return np.array(Cs) if Cs else np.array([0.])

def main():
    N=32; dt=1e-4
    print("="*70,flush=True)
    print("C STRESS TEST: 20 random ICs + named ICs",flush=True)
    print("="*70,flush=True)
    print(f"  Threshold: C < 1/4 = 0.25",flush=True)
    print(f"  Measuring C = (dα/dt + ê·S²·ê)/|ω|² at max-|ω| point\n",flush=True)

    print(f"  {'IC':>12s}  {'|ω|₀':>6s}  {'C_mean':>8s}  {'C_med':>8s}  "
          f"{'C_max':>8s}  {'C<¼':>5s}  {'verdict':>8s}",flush=True)
    print("-"*70,flush=True)

    all_C_max = []

    # Named ICs
    for ic_name in ['TG','KP']:
        s=NS3D(N,0.)
        X,Y,Z=s.X,s.Y,s.Z
        if ic_name=='TG':
            ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))
        else:
            ux=torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
            uy=torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
            uz=torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(uz))
        om0=s.om_max(w)
        Cs=measure_C_series(s,w,dt)
        safe="100%" if (Cs<0.25).all() else f"{100*(Cs<0.25).mean():.0f}%"
        v="SAFE ✓" if Cs.max()<0.25 else "SPIKE"
        print(f"  {ic_name:>12s}  {om0:6.1f}  {Cs.mean():+8.5f}  {np.median(Cs):+8.5f}  "
              f"{Cs.max():+8.5f}  {safe:>5s}  {v:>8s}",flush=True)
        all_C_max.append(Cs.max())

    # Trefoil
    s=NS3D(N,0.)
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
    w=(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
    om0=s.om_max(w)
    Cs=measure_C_series(s,w,dt)
    safe="100%" if (Cs<0.25).all() else f"{100*(Cs<0.25).mean():.0f}%"
    v="SAFE ✓" if Cs.max()<0.25 else "SPIKE"
    print(f"  {'trefoil':>12s}  {om0:6.1f}  {Cs.mean():+8.5f}  {np.median(Cs):+8.5f}  "
          f"{Cs.max():+8.5f}  {safe:>5s}  {v:>8s}",flush=True)
    all_C_max.append(Cs.max())

    # 20 random ICs
    for seed in range(20):
        s=NS3D(N,0.)
        w=random_ic(s, seed=seed+1000, target_om=15.0)
        om0=s.om_max(w)
        Cs=measure_C_series(s,w,dt,n_measurements=8)
        safe="100%" if (Cs<0.25).all() else f"{100*(Cs<0.25).mean():.0f}%"
        v="SAFE ✓" if Cs.max()<0.25 else "SPIKE"
        print(f"  {'rand_'+str(seed):>12s}  {om0:6.1f}  {Cs.mean():+8.5f}  {np.median(Cs):+8.5f}  "
              f"{Cs.max():+8.5f}  {safe:>5s}  {v:>8s}",flush=True)
        all_C_max.append(Cs.max())

    # Summary
    all_C_max=np.array(all_C_max)
    print(f"\n{'='*70}",flush=True)
    print(f"SUMMARY: {len(all_C_max)} ICs tested",flush=True)
    print(f"  C_max across all ICs: {all_C_max.max():+.5f}",flush=True)
    print(f"  C_max < 0.25: {(all_C_max<0.25).sum()}/{len(all_C_max)} "
          f"({100*(all_C_max<0.25).mean():.0f}%)",flush=True)
    print(f"  VERDICT: {'C < 1/4 HOLDS for all ICs ✓' if (all_C_max<0.25).all() else 'SOME VIOLATIONS'}",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
