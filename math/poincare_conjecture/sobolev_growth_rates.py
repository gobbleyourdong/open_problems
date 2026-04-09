"""
Instance C — Does d/dt||ω||²_{H^s} scale LINEARLY with ||ω||²_{H^s}?

If YES for s > 3/2: ||ω||_{H^s} grows exponentially → Sobolev → ||ω||∞ bounded → REGULARITY.

Standard bound: d/dt||ω||²_{H^s} ≤ C||ω||³_{H^s} (cubic → blowup).
If actual: d/dt||ω||²_{H^s} ≤ C||ω||²_{H^s} (linear → exponential → regularity).

Measure for s = 0 (enstrophy), 1 (palinstrophy), 2 (H² norm), 2.5 (H^{5/2}).
s > 3/2 = 1.5 embeds into L^∞ in 3D.
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

def sobolev_norms(s, w, exponents=[0, 1, 1.5, 2, 2.5]):
    """Compute ||ω||²_{H^s} = Σ (1+|k|²)^s |ω̂|² for various s."""
    N=s.N
    norms = {}
    for exp in exponents:
        weight = (1 + s.ksq)**exp
        val = sum((weight * w[i].abs()**2).sum().item() for i in range(3)) / N**3
        norms[exp] = val
    return norms

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
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    N=32;dt=1e-4;fd=30
    exponents=[0, 1, 1.5, 2, 2.5]
    print("="*70,flush=True)
    print("INSTANCE C — Sobolev norm growth rates: linear or cubic?",flush=True)
    print("="*70,flush=True)
    print(f"  s > 1.5 embeds into L^∞. If d/dt||ω||²_{{H^s}} ~ ||ω||²_{{H^s}}:",flush=True)
    print(f"  → exponential growth → bounded → REGULARITY\n",flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)
    t=0.

    # Headers
    hdr = f"  {'t':>6s}"
    for exp in exponents:
        hdr += f"  {'d/H'+str(exp):>10s}"
    hdr += f"  {'||ω||∞':>8s}"
    print(hdr, flush=True)

    prev_norms = None
    growth_rates = {exp: [] for exp in exponents}
    norm_vals = {exp: [] for exp in exponents}

    for epoch in range(40):
        norms = sobolev_norms(s, w, exponents)

        if prev_norms is not None:
            line = f"  {t:6.4f}"
            for exp in exponents:
                dn = (norms[exp] - prev_norms[exp]) / (fd * dt)
                rate = dn / (norms[exp] + 1e-30)  # d/dt(ln||ω||²_{H^s})
                growth_rates[exp].append(rate)
                norm_vals[exp].append(norms[exp])
                line += f"  {rate:+10.4f}"
            wf=[s.ifft(s.D*w[i]) for i in range(3)]
            om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt().max().item()
            line += f"  {om:8.2f}"
            if epoch % 4 == 0:
                print(line, flush=True)

        prev_norms = norms
        for _ in range(fd): w=s.step(w,dt); t+=dt

    # Analysis: for each s, fit d(ln||ω||²)/dt vs t and vs ln||ω||²
    print(f"\n  SCALING ANALYSIS:", flush=True)
    print(f"  {'s':>4s}  {'d(ln)/dt saturation':>20s}  {'fit vs t (R²)':>14s}  "
          f"{'fit vs lnN (R²)':>16s}  {'verdict':>10s}", flush=True)

    from scipy.stats import linregress
    for exp in exponents:
        gr = np.array(growth_rates[exp])
        nv = np.array(norm_vals[exp])
        ts = np.arange(len(gr)) * fd * dt + fd*dt

        if len(gr) < 5: continue

        # Does d(ln)/dt saturate?
        late_rate = gr[-5:].mean()

        # Fit vs t
        sl_t = linregress(ts[3:], gr[3:])
        # Fit vs ln(norm)
        sl_n = linregress(np.log(nv[3:]+1e-30), gr[3:])

        if sl_t.rvalue**2 > sl_n.rvalue**2:
            verdict = "~t"
        else:
            if sl_n.slope > 0.5:
                verdict = "~N^p BAD"
            else:
                verdict = "~const OK"

        print(f"  {exp:4.1f}  {late_rate:+20.4f}  {sl_t.rvalue**2:14.4f}  "
              f"{sl_n.rvalue**2:16.4f}  {verdict:>10s}", flush=True)

    # THE KEY: does the growth rate d(ln||ω||²_{H^s})/dt SATURATE for s > 1.5?
    print(f"\n  CRITICAL: growth rate saturation for s = 2.0 and 2.5:", flush=True)
    for exp in [2.0, 2.5]:
        gr = np.array(growth_rates[exp])
        if len(gr) < 5: continue
        early = gr[2:5].mean()
        late = gr[-5:].mean()
        print(f"    s={exp}: early rate={early:.4f}, late rate={late:.4f}, "
              f"ratio={late/early:.3f}", flush=True)
        if late < 2 * early:
            print(f"    → Rate NOT accelerating → BOUNDED growth → regularity potential ✓", flush=True)
        else:
            print(f"    → Rate ACCELERATING → possible cubic regime ✗", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)

if __name__=='__main__':
    main()
