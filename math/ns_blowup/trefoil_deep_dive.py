"""
Deep dive into the trefoil knot: c₃ = 0.25, α = +0.051 (STRETCHING).

Questions:
1. Is this transient or persistent?
2. Does α eventually turn negative?
3. What's happening at the highest |ω| points specifically?
4. How does c₃ evolve over longer time?
5. Is this a resolution issue (trefoil needs more modes)?
6. What do rings look like over time?
"""
import torch
import numpy as np
import math
import sys

DTYPE = torch.float64
pi = math.pi


class NS3D:
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
    def spectral_ratio(s,w):
        spec = sum(wi.abs() for wi in w)
        N=s.N; lo=spec[:N//4,:N//4,:N//4].mean().item()
        hi=spec[N//4:N//2,N//4:N//2,N//4:N//2].mean().item()
        return hi/(lo+1e-30)


def alignment(s, w, percentile=0.90, n_max=2000):
    D=s.D; N=s.N; u=s.vel(*w); kd=[s.kx,s.ky,s.kz]
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    thr=torch.quantile(om.flatten(),percentile)
    if thr<1e-10: return dict(c1=.33,c2=.33,c3=.33,alpha=0,n=0,om_thr=0,om_max=0)
    idx=(om>thr).nonzero(as_tuple=False)
    n=min(len(idx),n_max)
    if n==0: return dict(c1=.33,c2=.33,c3=.33,alpha=0,n=0,om_thr=0,om_max=0)
    perm=torch.randperm(len(idx))[:n]; pts=idx[perm]
    c1s,c2s,c3s,als=[],[],[],[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        Sl=S[:,:,ix,iy,iz]; wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12: continue
        eh=wv/wn; ev,ec=torch.linalg.eigh(Sl)
        c1=(eh@ec[:,2]).item()**2; c2=(eh@ec[:,1]).item()**2; c3=(eh@ec[:,0]).item()**2
        al=ev[2].item()*c1+ev[1].item()*c2+ev[0].item()*c3
        c1s.append(c1);c2s.append(c2);c3s.append(c3);als.append(al)
    if not c1s: return dict(c1=.33,c2=.33,c3=.33,alpha=0,n=0,om_thr=0,om_max=0)
    return dict(c1=np.mean(c1s),c2=np.mean(c2s),c3=np.mean(c3s),
                alpha=np.mean(als),n=len(c1s),om_thr=thr.item(),
                om_max=om.max().item())


def make_trefoil(s, amp=10.0, sigma=0.3):
    X,Y,Z = s.X, s.Y, s.Z
    wx=torch.zeros_like(X); wy=torch.zeros_like(X); wz=torch.zeros_like(X)
    n_pts=200
    t_param=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
    cx=(torch.sin(t_param)+2*torch.sin(2*t_param))*0.5+pi
    cy=(torch.cos(t_param)-2*torch.cos(2*t_param))*0.5+pi
    cz=(-torch.sin(3*t_param))*0.5+pi
    tx=torch.cos(t_param)+4*torch.cos(2*t_param)
    ty=-torch.sin(t_param)+4*torch.sin(2*t_param)
    tz=-3*torch.cos(3*t_param)
    ds=2*pi/n_pts
    for i in range(n_pts):
        dist_sq=(X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2
        g=amp*torch.exp(-dist_sq/(2*sigma**2))*ds
        wx+=g*tx[i]; wy+=g*ty[i]; wz+=g*tz[i]
    return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))


def make_rings(s, amp=5.0, sep=1.5, sigma=0.3):
    X,Y,Z = s.X, s.Y, s.Z
    wx=torch.zeros_like(X); wy=torch.zeros_like(X); wz=torch.zeros_like(X)
    R=0.8
    for sign in [+1,-1]:
        z0=pi+sign*sep
        rho=((X-pi)**2+(Y-pi)**2).sqrt()
        core_dist=((rho-R)**2+(Z-z0)**2).sqrt()
        strength=amp*torch.exp(-core_dist**2/(2*sigma**2))
        theta_x=-(Y-pi)/(rho+1e-10)
        theta_y=(X-pi)/(rho+1e-10)
        wx+=sign*strength*theta_x; wy+=sign*strength*theta_y
    return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))


def main():
    N = 32; dt = 1e-4  # smaller dt for trefoil (higher |ω|)

    print("="*70, flush=True)
    print("TREFOIL + RINGS DEEP DIVE", flush=True)
    print("="*70, flush=True)

    # =================================================================
    # TREFOIL: long evolution
    # =================================================================
    print("\n--- TREFOIL (Euler, N=32, amp=10, σ=0.3) ---", flush=True)
    print(f"  {'t':>6s}  {'|ω|':>7s}  {'spec':>8s}  {'c₁':>5s}  {'c₂':>5s}  {'c₃':>5s}  "
          f"{'α':>8s}  {'c₃≥⅓':>5s}  {'α≤0':>4s}", flush=True)

    s = NS3D(N, 0.0)
    w = make_trefoil(s)
    t = 0.0

    for epoch in range(20):
        om = s.om_max(w)
        spec = s.spectral_ratio(w)
        r = alignment(s, w)
        c3m = "✓" if r['c3']>=0.333 else " "
        am = "✓" if r['alpha']<=0 else "✗"
        print(f"  {t:6.4f}  {om:7.2f}  {spec:8.2e}  {r['c1']:5.3f}  {r['c2']:5.3f}  "
              f"{r['c3']:5.3f}  {r['alpha']:+8.4f}  {c3m:>5s}  {am:>4s}", flush=True)

        if spec > 0.1:
            print(f"  *** UNDER-RESOLVED (spec={spec:.2e}) — results unreliable ***", flush=True)

        if om > 1e4:
            print(f"  *** BLOWUP DETECTED ***", flush=True)
            break

        for _ in range(200):
            w = s.step(w, dt)
            t += dt

    # Also measure at different percentiles
    print(f"\n  Percentile scan at final time t={t:.4f}:", flush=True)
    for pct in [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]:
        r = alignment(s, w, percentile=pct)
        c3m = "✓" if r['c3']>=0.333 else " "
        am = "✓" if r['alpha']<=0 else "✗"
        print(f"    top {(1-pct)*100:5.1f}%: |ω|>{r['om_thr']:7.2f}  "
              f"c₁={r['c1']:.3f}  c₃={r['c3']:.3f}  α={r['alpha']:+.4f}  {c3m} {am}", flush=True)

    # =================================================================
    # TREFOIL at higher resolution (N=48) to check convergence
    # =================================================================
    print(f"\n--- TREFOIL at N=48 (resolution check) ---", flush=True)
    s48 = NS3D(48, 0.0)
    w48 = make_trefoil(s48)
    t48 = 0.0
    dt48 = 5e-5

    print(f"  {'t':>6s}  {'|ω|':>7s}  {'spec':>8s}  {'c₁':>5s}  {'c₃':>5s}  {'α':>8s}", flush=True)
    for epoch in range(10):
        om = s48.om_max(w48)
        spec = s48.spectral_ratio(w48)
        r = alignment(s48, w48)
        print(f"  {t48:6.4f}  {om:7.2f}  {spec:8.2e}  {r['c1']:5.3f}  {r['c3']:5.3f}  "
              f"{r['alpha']:+8.4f}", flush=True)

        if spec > 0.1:
            print(f"  *** UNDER-RESOLVED ***", flush=True)
        if om > 1e4: break

        for _ in range(200):
            w48 = s48.step(w48, dt48)
            t48 += dt48

    # =================================================================
    # RINGS: long evolution
    # =================================================================
    print(f"\n--- RINGS (Euler, N=32) ---", flush=True)
    print(f"  {'t':>6s}  {'|ω|':>7s}  {'c₁':>5s}  {'c₂':>5s}  {'c₃':>5s}  "
          f"{'α':>8s}  c₃≥⅓  α≤0", flush=True)

    s = NS3D(N, 0.0)
    w = make_rings(s)
    t = 0.0

    for epoch in range(15):
        om = s.om_max(w)
        r = alignment(s, w)
        c3m = "✓" if r['c3']>=0.333 else " "
        am = "✓" if r['alpha']<=0 else "✗"
        print(f"  {t:6.4f}  {om:7.2f}  {r['c1']:5.3f}  {r['c2']:5.3f}  "
              f"{r['c3']:5.3f}  {r['alpha']:+8.4f}  {c3m:>5s}  {am:>4s}", flush=True)

        for _ in range(200):
            w = s.step(w, dt)
            t += dt

    # =================================================================
    # ABC: α > 0 case
    # =================================================================
    print(f"\n--- ABC (Euler, N=32) ---", flush=True)
    print(f"  {'t':>6s}  {'|ω|':>7s}  {'c₁':>5s}  {'c₂':>5s}  {'c₃':>5s}  "
          f"{'α':>8s}  c₃≥⅓  α≤0", flush=True)

    s = NS3D(N, 0.0)
    X,Y,Z = s.X,s.Y,s.Z
    ux=torch.sin(Z)+0.6*torch.cos(Y); uy=0.8*torch.sin(X)+torch.cos(Z)
    uz=0.6*torch.sin(Y)+0.8*torch.cos(X)
    w = s.curl(s.fft(ux), s.fft(uy), s.fft(uz))
    t = 0.0

    for epoch in range(15):
        om = s.om_max(w)
        r = alignment(s, w)
        c3m = "✓" if r['c3']>=0.333 else " "
        am = "✓" if r['alpha']<=0 else "✗"
        print(f"  {t:6.4f}  {om:7.2f}  {r['c1']:5.3f}  {r['c2']:5.3f}  "
              f"{r['c3']:5.3f}  {r['alpha']:+8.4f}  {c3m:>5s}  {am:>4s}", flush=True)

        for _ in range(200):
            w = s.step(w, dt)
            t += dt

    # =================================================================
    # What does BKM ACTUALLY need?
    # =================================================================
    print(f"\n\n{'='*70}", flush=True)
    print("WHAT DOES BKM ACTUALLY NEED?", flush=True)
    print(f"{'='*70}", flush=True)
    print("""
BKM: blowup at T* iff ∫₀^T* ||ω||_∞ dt = ∞.

For regularity: need ||ω||_∞ to NOT blow up.
The vorticity equation: d|ω|/dt ≤ α|ω| + viscous.

If α ≤ C (bounded), then |ω| grows at most exponentially:
|ω(t)| ≤ |ω(0)| exp(Ct)

Exponential growth gives ∫||ω||_∞ dt < ∞ on finite intervals.
So BKM regularity holds if α is BOUNDED (doesn't need to be negative!).

The question isn't "is α ≤ 0?" but "is α bounded?"

For BKM: even α = +0.05 (trefoil) is fine as long as it stays bounded.
The dangerous scenario is α → +∞ (which would give super-exponential growth).

The self-depletion ê·S²·ê ≥ α² prevents this:
dα/dt ≤ -α² + (pressure terms)
If α gets large positive, the -α² kills it (Riccati).
""", flush=True)

    print(f"{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
