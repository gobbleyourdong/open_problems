"""
Does viscosity rescue the trefoil?

The trefoil at ν=0 (Euler) has persistent α > 0 and c₃ < 1/3.
Hypothesis: at ν > 0 (NS), the tube diffuses, fill fraction increases,
and the compression mechanism activates.

Test at multiple ν values: 0, 10⁻⁴, 10⁻³, 10⁻², 10⁻¹.
Track: fill fraction, c₃, α, |ω|_max over time.

Also test: does the trefoil's stretching SATURATE even at ν=0?
The self-depletion dα/dt ≤ -α² should eventually bound α.
"""
import torch
import numpy as np
import math

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


def alignment(s, w, pct=0.90, n_max=1500):
    D=s.D; N=s.N; u=s.vel(*w); kd=[s.kx,s.ky,s.kz]
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    thr=torch.quantile(om.flatten(),pct)
    if thr<1e-10: return .33,.33,.33,0.
    idx=(om>thr).nonzero(as_tuple=False)
    n=min(len(idx),n_max)
    if n==0: return .33,.33,.33,0.
    perm=torch.randperm(len(idx))[:n]; pts=idx[perm]
    c1s,c2s,c3s,als=[],[],[],[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        Sl=S[:,:,ix,iy,iz]; wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12: continue
        eh=wv/wn; ev,ec=torch.linalg.eigh(Sl)
        c1=(eh@ec[:,2]).item()**2; c3=(eh@ec[:,0]).item()**2
        al=sum(ev[j].item()*(eh@ec[:,j]).item()**2 for j in range(3))
        c1s.append(c1);c3s.append(c3);als.append(al)
    if not c1s: return .33,.33,.33,0.
    return np.mean(c1s),0,np.mean(c3s),np.mean(als)


def fill_fraction(s, w, threshold=0.1):
    D=s.D
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    return (om > threshold*om.max()).float().mean().item()


def make_trefoil(s, amp=10.0, sigma=0.3):
    X,Y,Z = s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    n_pts=200; t_p=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
    cx=(torch.sin(t_p)+2*torch.sin(2*t_p))*0.5+pi
    cy=(torch.cos(t_p)-2*torch.cos(2*t_p))*0.5+pi
    cz=(-torch.sin(3*t_p))*0.5+pi
    tx=torch.cos(t_p)+4*torch.cos(2*t_p); ty=-torch.sin(t_p)+4*torch.sin(2*t_p)
    tz=-3*torch.cos(3*t_p); ds=2*pi/n_pts
    for i in range(n_pts):
        g=amp*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*sigma**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))


def main():
    N = 32; dt = 1e-4

    print("="*70, flush=True)
    print("VISCOSITY RESCUE TEST: Does ν > 0 save the trefoil?", flush=True)
    print("="*70, flush=True)

    nu_values = [0.0, 1e-4, 1e-3, 5e-3, 1e-2, 5e-2]

    for nu in nu_values:
        s = NS3D(N, nu)
        w = make_trefoil(s)
        print(f"\n--- ν = {nu:.0e} ---", flush=True)
        print(f"  {'t':>6s}  {'|ω|':>7s}  {'fill':>5s}  {'c₁':>5s}  {'c₃':>5s}  "
              f"{'α':>8s}  c₃≥⅓  α≤0", flush=True)

        t = 0.0
        for epoch in range(16):
            om = s.om_max(w)
            ff = fill_fraction(s, w)
            c1, _, c3, alpha = alignment(s, w)
            c3m = "✓" if c3 >= 0.333 else " "
            am = "✓" if alpha <= 0 else "✗"
            print(f"  {t:6.4f}  {om:7.2f}  {ff:5.3f}  {c1:5.3f}  {c3:5.3f}  "
                  f"{alpha:+8.4f}  {c3m:>5s}  {am:>4s}", flush=True)

            if om < 1e-6:
                print(f"  *** DECAYED ***", flush=True)
                break
            if om > 1e5:
                print(f"  *** BLOWUP ***", flush=True)
                break

            for _ in range(250):
                w = s.step(w, dt)
                t += dt

    # Also check: BKM integral ∫||ω||_∞ dt
    print(f"\n\n{'='*70}", flush=True)
    print("BKM INTEGRAL: ∫||ω||_∞ dt for trefoil at various ν", flush=True)
    print(f"{'='*70}", flush=True)

    for nu in [0.0, 1e-3, 1e-2]:
        s = NS3D(N, nu)
        w = make_trefoil(s)
        t = 0.0
        bkm = 0.0
        om_history = []

        for step in range(4000):
            om = s.om_max(w)
            bkm += om * dt
            if step % 500 == 0:
                om_history.append((t, om, bkm))
            w = s.step(w, dt)
            t += dt
            if om > 1e5: break

        print(f"\n  ν={nu:.0e}: t_final={t:.4f}, |ω|_final={om:.2f}, BKM={bkm:.4f}", flush=True)
        for t_h, om_h, bkm_h in om_history:
            print(f"    t={t_h:.3f}: |ω|={om_h:.2f}, ∫|ω|dt={bkm_h:.4f}", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
