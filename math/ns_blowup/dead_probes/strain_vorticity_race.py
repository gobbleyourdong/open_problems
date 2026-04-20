"""
The Strain-Vorticity Race: does |S| catch up to |ω|?

Theory:
  DS/Dt = -S² - Ω² - H,  where -Ω² ~ |ω|²
  Dω/Dt = S·ω,           where |Dω/Dt| ~ |S|·|ω|

When |S| << |ω|:
  d|S|/dt ~ |ω|²  (Ω² dominates strain growth)
  d|ω|/dt ~ |S|·|ω|  (stretching is weak because |S| is small)

So |S| grows FASTER → ratio |ω|/|S| decreases.
Question: does it plateau at |ω|/|S| ~ O(1), or at some other value?

Track ||S||_∞, ||ω||_∞, and their ratio over time for all ICs.
Also track at percentile points (not just max).
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

def compute_norms(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    # |S|² field
    S_sq=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Aij=s.ifft(1j*kd[j]*D*u[i]);Aji=s.ifft(1j*kd[i]*D*u[j])
            S_sq+=0.25*(Aij+Aji)**2
    S_mag=S_sq.sqrt()
    # |ω| field
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    return om, S_mag

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
    N=32; dt=1e-4
    print("="*70,flush=True)
    print("STRAIN-VORTICITY RACE: does |S| catch up to |ω|?",flush=True)
    print("="*70,flush=True)

    for ic_name in ['TG','KP','trefoil']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        print(f"\n--- {ic_name} (Euler, N=32) ---",flush=True)
        print(f"  {'t':>6s}  {'||ω||∞':>8s}  {'||S||∞':>8s}  {'ω/S max':>8s}  "
              f"{'ω/S 99%':>8s}  {'ω/S 95%':>8s}  {'ω/S cond':>9s}  "
              f"{'d|ω|/dt':>8s}  {'d|S|/dt':>8s}",flush=True)

        t=0.; om_prev=None; S_prev=None
        for epoch in range(16):
            om, S_mag = compute_norms(s, w)
            om_max=om.max().item(); S_max=S_mag.max().item()

            # Ratio at different percentiles
            om_flat=om.flatten(); S_flat=S_mag.flatten()
            ratio_flat=om_flat/(S_flat+1e-30)

            # Conditional: ratio at top 5% of |ω|
            thr95=torch.quantile(om_flat,0.95).item()
            mask95=om_flat>thr95
            ratio_cond=ratio_flat[mask95].mean().item() if mask95.sum()>0 else 0

            # Growth rates
            if om_prev is not None:
                dom=(om_max-om_prev)/(250*dt)
                dS=(S_max-S_prev)/(250*dt)
            else:
                dom=0; dS=0

            thr99=torch.quantile(om_flat,0.99).item()
            mask99=om_flat>thr99
            r99=ratio_flat[mask99].mean().item() if mask99.sum()>0 else 0
            r95=ratio_flat[mask95].mean().item() if mask95.sum()>0 else 0

            print(f"  {t:6.3f}  {om_max:8.2f}  {S_max:8.2f}  {om_max/(S_max+1e-30):8.2f}  "
                  f"{r99:8.2f}  {r95:8.2f}  {ratio_cond:9.2f}  "
                  f"{dom:+8.2f}  {dS:+8.2f}",flush=True)

            om_prev=om_max; S_prev=S_max
            for _ in range(250): w=s.step(w,dt); t+=dt

    # LONGER RUN for trefoil to see plateau
    print(f"\n\n{'='*70}",flush=True)
    print("LONG RUN: trefoil to t=1.0 — does the ratio plateau?",flush=True)
    print(f"{'='*70}",flush=True)

    s=NS3D(N,0.);w=make_ic(s,'trefoil')
    t=0.
    print(f"  {'t':>6s}  {'||ω||∞':>8s}  {'||S||∞':>8s}  {'ω/S(max)':>9s}  {'ω/S(99%)':>9s}",flush=True)

    for epoch in range(40):
        om,S_mag=compute_norms(s,w)
        om_flat=om.flatten();S_flat=S_mag.flatten()
        om_max=om.max().item();S_max=S_mag.max().item()
        thr=torch.quantile(om_flat,0.99).item()
        mask=om_flat>thr
        r99=(om_flat[mask]/(S_flat[mask]+1e-30)).mean().item() if mask.sum()>0 else 0

        if epoch%4==0:
            print(f"  {t:6.3f}  {om_max:8.2f}  {S_max:8.2f}  "
                  f"{om_max/(S_max+1e-30):9.2f}  {r99:9.2f}",flush=True)

        for _ in range(250): w=s.step(w,dt); t+=dt

    # Theory check: if d|S|/dt ~ |ω|² and d|ω|/dt ~ |S|·|ω|,
    # what's the predicted ratio evolution?
    print(f"\n\n{'='*70}",flush=True)
    print("THEORY: Predicted ratio evolution",flush=True)
    print(f"{'='*70}",flush=True)
    print("""
From the equations:
  d|S|/dt ~ |ω|²    (from -Ω² term in strain eq)
  d|ω|/dt ~ |S|·|ω| (from vortex stretching)

Let r = |ω|/|S|. Then:
  dr/dt = d|ω|/dt / |S| - |ω| d|S|/dt / |S|²
        ~ |ω| - |ω|·|ω|²/|S|²
        = |ω|(1 - r²)

So: dr/dt ~ |ω|(1 - r²)

Equilibrium: r = 1 (|ω| = |S|)
If r > 1: dr/dt < 0 (ratio decreases toward 1)
If r < 1: dr/dt > 0 (ratio increases toward 1)

The ratio |ω|/|S| → 1 is an ATTRACTOR.

But this is a ROUGH scaling argument. The actual coefficients matter:
  d|S|/dt = C₁|ω|² + C₂|S|² + C₃(pressure)
  d|ω|/dt = C₄|S||ω|

The equilibrium is r = |ω|/|S| = √(C₁/C₄) (depends on coefficients).
If C₁ < C₄: equilibrium at r < 1 (strain exceeds vorticity) — VERY BAD
If C₁ > C₄: equilibrium at r > 1 (vorticity exceeds strain) — SAFE

From data: the trefoil ratio starts at ~4.4 and decreases toward...
Let's extrapolate.
""",flush=True)

    print(f"{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
