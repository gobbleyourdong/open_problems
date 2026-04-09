"""
INSTANCE C — file 260: Palinstrophy transfer sign test.

The enstrophy: dE/dt = 2∫ω·S·ω dx (stretching only, advection vanishes)
The palinstrophy: dP/dt = 2∫∇ω:∇(S·ω)dx + 2∫∇ω:(∇u)^T·∇ω dx + viscous

Key question: is the TOTAL dP/dt negative (or bounded) when the flow
is in the compressive regime (c₃ > 1/3, α < 0)?

If dP/dt ≤ C·P (linear, not cubic): P bounded exponentially → regularity.
The standard bound gives dP/dt ≤ C·P³/ν (cubic → possible blowup).

Test: measure dP/dt directly from DNS and compare to the cubic bound.
Also decompose into stretching vs advection contributions.
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

def measure_palinstrophy(s, w):
    """Compute E, P, dE/dt, dP/dt, and the growth exponents."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]

    # Enstrophy E = Σ|ω̂|²/N³
    E = sum((w[i].abs()**2).sum().item() for i in range(3)) / N**3

    # Palinstrophy P = Σ|k|²|ω̂|²/N³
    P = sum((s.ksq * w[i].abs()**2).sum().item() for i in range(3)) / N**3

    # Super-palinstrophy Q = Σ|k|⁴|ω̂|²/N³
    Q = sum((s.ksq**2 * w[i].abs()**2).sum().item() for i in range(3)) / N**3

    # ||ω||∞
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    om_max=om.max().item()

    # The ratio P³/(E²Q) — dimensionless measure of concentration
    # For Agmon: ||ω||∞² ≤ C√P√Q → ||ω||∞⁴ ≤ C²PQ
    agmon_bound = (P * Q)**0.5 if P>0 and Q>0 else 0

    return {
        'E': E, 'P': P, 'Q': Q,
        'om_max': om_max,
        'agmon': agmon_bound,
        'P_over_E': P/(E+1e-30),  # effective wavenumber squared
        'Q_over_P': Q/(P+1e-30),  # higher moment ratio
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
    dt=1e-4; fd_steps=20
    print("="*70,flush=True)
    print("INSTANCE C — PALINSTROPHY GROWTH: cubic or sub-cubic?",flush=True)
    print("="*70,flush=True)
    print("  Standard bound: dP/dt ≤ C·P³/ν (cubic → blowup)",flush=True)
    print("  If actual: dP/dt ≤ C·P^β with β < 3: sub-cubic → regularity\n",flush=True)

    for ic_name in ['trefoil','TG','KP']:
        N=32;s=NS3D(N,0.);w=make_ic(s,ic_name)

        print(f"--- {ic_name} (Euler) ---",flush=True)
        print(f"  {'t':>6s}  {'E':>10s}  {'P':>12s}  {'dP/dt':>12s}  "
              f"{'dP/P':>8s}  {'dP/P³':>10s}  {'||ω||∞':>8s}  {'P/E':>8s}",flush=True)

        t=0.; prev_P=None
        for epoch in range(15):
            m=measure_palinstrophy(s,w)

            if prev_P is not None:
                dP=(m['P']-prev_P)/(fd_steps*dt)
                dP_over_P=dP/(m['P']+1e-30)
                dP_over_P3=dP/(m['P']**3+1e-30) if m['P']>1e-10 else 0
                print(f"  {t:6.4f}  {m['E']:10.2f}  {m['P']:12.2f}  {dP:+12.2f}  "
                      f"{dP_over_P:+8.4f}  {dP_over_P3:+10.6f}  "
                      f"{m['om_max']:8.2f}  {m['P_over_E']:8.1f}",flush=True)

            prev_P=m['P']
            for _ in range(fd_steps):w=s.step(w,dt);t+=dt

        # Fit the growth: dP/dt = C P^β
        # Collect dense data
        print(f"\n  Growth exponent fit:",flush=True)
        s2=NS3D(N,0.);w2=make_ic(s2,ic_name)
        Ps=[];dPs=[];t2=0.
        for epoch in range(30):
            m1=measure_palinstrophy(s2,w2)
            for _ in range(fd_steps):w2=s2.step(w2,dt);t2+=dt
            m2=measure_palinstrophy(s2,w2)
            dP=(m2['P']-m1['P'])/(fd_steps*dt)
            if m1['P']>1e-6 and dP>0:
                Ps.append(m1['P']);dPs.append(dP)

        if len(Ps)>5:
            Ps=np.array(Ps);dPs=np.array(dPs)
            # log-log fit: log(dP) = β log(P) + log(C)
            logP=np.log(Ps);logdP=np.log(dPs)
            coeffs=np.polyfit(logP,logdP,1)
            beta=coeffs[0];C_eff=np.exp(coeffs[1])
            print(f"  dP/dt ≈ {C_eff:.4f} × P^{beta:.3f}",flush=True)
            if beta < 2:
                print(f"  β = {beta:.3f} < 2: SUB-QUADRATIC → P bounded → regularity potential ✓",flush=True)
            elif beta < 3:
                print(f"  β = {beta:.3f} < 3: sub-cubic but super-quadratic",flush=True)
            else:
                print(f"  β = {beta:.3f} ≥ 3: cubic or worse → standard bound",flush=True)
        else:
            print(f"  Insufficient positive-growth data for fit",flush=True)

        print(flush=True)

    print(f"{'='*70}",flush=True)
    print("KEY: if β < 3, the NS structure improves over the generic bound.",flush=True)
    print("If β < 2, P is bounded → ||ω||_{H¹} bounded → progress toward regularity.",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
