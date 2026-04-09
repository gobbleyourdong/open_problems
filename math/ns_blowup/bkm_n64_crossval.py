"""
N=64 cross-validation of the BKM curvature diagnostic for trefoil.

If 1/||ω||∞ is still concave up at N=64, the result is resolution-converged.
"""
import torch, numpy as np, math, time
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N=64,nu=0.):
        s.N=N;s.nu=nu;s.Lx=2*pi;dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2;s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
        print(f"NS3D: N={N}, {N**3:,} pts, dealias modes: {int(s.D.sum()):,}",flush=True)
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
    def spectral_ratio(s,w):
        spec=sum(wi.abs() for wi in w);N=s.N
        lo=spec[:N//4,:N//4,:N//4].mean().item()
        hi=spec[N//4:N//2,N//4:N//2,N//4:N//2].mean().item()
        return hi/(lo+1e-30)

def make_trefoil(s, amp=10., sigma=0.3):
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
    cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
    cz=(-torch.sin(3*tp))*0.5+pi
    tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
    ds=2*pi/200
    for i in range(200):
        g=amp*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*sigma**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    print("="*70,flush=True)
    print("N=64 CROSS-VALIDATION: BKM curvature for trefoil",flush=True)
    print("="*70,flush=True)

    # Run at N=32, N=48, N=64 with same IC
    for N_test in [32, 48, 64]:
        dt = {32: 1e-4, 48: 5e-5, 64: 3e-5}[N_test]
        n_total = {32: 8000, 48: 6000, 64: 4000}[N_test]
        sample = {32: 40, 48: 30, 64: 20}[N_test]

        s=NS3D(N_test,0.)
        w=make_trefoil(s)

        times=[];oms=[];specs=[]
        t=0.; t0=time.time()

        for step in range(n_total+1):
            if step%sample==0:
                om=s.om_max(w)
                sp=s.spectral_ratio(w) if step%(sample*5)==0 else -1
                times.append(t);oms.append(om);specs.append(sp)
                if step%(sample*10)==0:
                    elapsed=time.time()-t0
                    print(f"  N={N_test} step={step}/{n_total} t={t:.4f} "
                          f"|ω|={om:.2f} [{elapsed:.0f}s]",flush=True)
            if step<n_total: w=s.step(w,dt);t+=dt

        times=np.array(times);oms=np.array(oms)
        inv_om=1.0/oms

        # Curvature in second half
        n_half=len(times)//2
        t2=times[n_half:];inv2=inv_om[n_half:]
        d2_inv=np.gradient(np.gradient(inv2,t2),t2)
        curv=d2_inv.mean()

        # Linear fit for T*
        coeffs=np.polyfit(t2,inv2,1)
        slope=coeffs[0]
        T_star=-coeffs[1]/slope if slope<0 else float('inf')

        elapsed=time.time()-t0
        print(f"\n  N={N_test} RESULT [{elapsed:.0f}s]:",flush=True)
        print(f"    t: [0, {times[-1]:.4f}], ||ω||∞: {oms[0]:.2f} → {oms[-1]:.2f}",flush=True)
        print(f"    1/||ω||∞: {inv_om[0]:.5f} → {inv_om[-1]:.5f}",flush=True)
        print(f"    Curvature d²(1/||ω||)/dt²: {curv:+.6f}",flush=True)
        print(f"    Sign: {'CONCAVE UP (regularity) ✓' if curv>0 else 'CONCAVE DOWN (danger) ✗' if curv<-1e-6 else 'FLAT'}",flush=True)
        print(f"    Linear T*: {T_star:.3f}",flush=True)

        # Resolution check
        valid_specs=[sp for sp in specs if sp>0]
        if valid_specs:
            max_spec=max(valid_specs)
            print(f"    Max spectral ratio: {max_spec:.2e} "
                  f"({'RESOLVED' if max_spec<0.01 else 'MARGINAL' if max_spec<0.1 else 'UNDER-RESOLVED'})",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("CROSS-VALIDATION TABLE:",flush=True)
    print("  If curvature sign is SAME at all N: result is converged.",flush=True)
    print("  If curvature changes sign: resolution-dependent — need higher N.",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
