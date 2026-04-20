"""
Measure the effective pressure coefficient C in: dα/dt ≤ -α² + C|ω|²

If C < 1/4: self-depletion wins → regularity.
If C ≥ 1/4: pressure can overwhelm → no bound.

From last session: C ≈ 0.04 at N=32 for the trefoil.
CRITICAL: does C grow with resolution?

Test at N=32 and N=48. If C is resolution-independent, the bound is robust.

Also: measure C at different |ω| thresholds to check if it depends on |ω|.
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

def compute_C_field(s, w):
    """Compute α, ê·S²·ê, |ω| at every point. Then C = (dα/dt + ê·S²·ê) / |ω|²."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    om=om_sq.sqrt()

    # α = ω_i S_ij ω_j / |ω|²
    alpha=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): alpha+=wf[i]*S[i,j]*wf[j]
    alpha=alpha/(om_sq+1e-30)

    # ê·S²·ê
    S2ee=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            tmp=torch.zeros(N,N,N,dtype=DTYPE)
            for k in range(3): tmp+=S[i,k]*S[k,j]
            S2ee+=wf[i]*tmp*wf[j]
    S2ee=S2ee/(om_sq+1e-30)

    return alpha, S2ee, om

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

def make_tg(s):
    X,Y,Z=s.X,s.Y,s.Z
    ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
    return s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))

def measure_C(s, w, dt, n_fd=30, percentiles=[0.90, 0.95, 0.99]):
    """Measure C = R/|ω|² where R = dα/dt + ê·S²·ê at various |ω| thresholds."""
    alpha0, S2ee0, om0 = compute_C_field(s, w)
    w1 = tuple(wi.clone() for wi in w)
    for _ in range(n_fd): w1 = s.step(w1, dt)

    alpha1, _, _ = compute_C_field(s, w1)
    dalpha = (alpha1 - alpha0) / (n_fd * dt)

    # R = dα/dt + ê·S²·ê (the residual after self-depletion)
    # Note: the FULL self-interaction is -ê·S²·ê, so the residual is
    # R = dα/dt + ê·S²·ê = (everything else: -ê·Ω²·ê - ê·H·ê + advection)
    R = dalpha + S2ee0

    # C = R / |ω|² (the effective pressure coefficient)
    C_field = R / (om0**2 + 1e-30)

    results = {}
    om_flat = om0.flatten()
    C_flat = C_field.flatten()
    R_flat = R.flatten()

    for pct in percentiles:
        thr = torch.quantile(om_flat, pct).item()
        mask = om_flat > thr
        if mask.sum() < 10: continue
        C_pts = C_flat[mask]
        R_pts = R_flat[mask]
        om_pts = om_flat[mask]

        results[pct] = {
            'C_mean': C_pts.mean().item(),
            'C_median': C_pts.median().item(),
            'C_max': C_pts.max().item(),
            'R_mean': R_pts.mean().item(),
            'om_mean': om_pts.mean().item(),
            'n': mask.sum().item(),
        }
    return results

def main():
    dt32 = 1e-4; dt48 = 5e-5
    print("="*70, flush=True)
    print("PRESSURE COEFFICIENT C: resolution independence test", flush=True)
    print("="*70, flush=True)
    print(f"  C < 1/4 = 0.25 → self-depletion wins → regularity", flush=True)
    print(f"  C ≥ 1/4 = 0.25 → pressure can overwhelm → danger\n", flush=True)

    # Test trefoil at N=32 and N=48, at multiple evolution times
    for ic_name, make_fn in [('trefoil', make_trefoil), ('TG', make_tg)]:
        for N_test, dt_test in [(32, dt32), (48, dt48)]:
            s = NS3D(N_test, 0.)
            w = make_fn(s)
            print(f"--- {ic_name} N={N_test} ---", flush=True)
            print(f"  {'t':>6s}  {'|ω|_max':>8s}  ", end='', flush=True)
            for pct in [0.90, 0.95, 0.99]:
                print(f"C(top{(1-pct)*100:.0f}%)  ", end='')
            print(flush=True)

            t = 0.
            for epoch in range(10):
                # Evolve
                n_step = 300 if N_test == 32 else 400
                for _ in range(n_step): w = s.step(w, dt_test); t += dt_test

                om_max = max(abs(s.ifft(w[i])).max().item() for i in range(3))  # rough
                # Actually compute properly
                wf = [s.ifft(s.D*w[i]) for i in range(3)]
                om_max = (wf[0]**2+wf[1]**2+wf[2]**2).sqrt().max().item()

                res = measure_C(s, w, dt_test, n_fd=20)

                line = f"  {t:6.3f}  {om_max:8.2f}  "
                for pct in [0.90, 0.95, 0.99]:
                    if pct in res:
                        C_val = res[pct]['C_mean']
                        line += f"{C_val:+8.4f}  "
                    else:
                        line += "     N/A  "
                print(line, flush=True)

    # Summary comparison
    print(f"\n{'='*70}", flush=True)
    print("RESOLUTION COMPARISON: C at t≈0.05 for trefoil", flush=True)
    print(f"{'='*70}", flush=True)

    for N_test, dt_test in [(32, dt32), (48, dt48)]:
        s = NS3D(N_test, 0.)
        w = make_trefoil(s)
        for _ in range(500): w = s.step(w, dt_test)

        res = measure_C(s, w, dt_test, n_fd=20)
        print(f"\n  N={N_test}:", flush=True)
        for pct in [0.90, 0.95, 0.99]:
            if pct in res:
                r = res[pct]
                print(f"    top {(1-pct)*100:.0f}%: C_mean={r['C_mean']:+.5f}  "
                      f"C_median={r['C_median']:+.5f}  C_max={r['C_max']:+.5f}  "
                      f"|ω|_mean={r['om_mean']:.2f}  n={r['n']:.0f}", flush=True)

    # Also check: what's the MAXIMUM C anywhere at high |ω|?
    print(f"\n{'='*70}", flush=True)
    print("WORST-CASE C across all ICs and times", flush=True)
    print(f"{'='*70}", flush=True)

    worst_C = -999
    for ic_name, make_fn in [('trefoil', make_trefoil), ('TG', make_tg)]:
        s = NS3D(32, 0.)
        w = make_fn(s)
        for epoch in range(8):
            for _ in range(250): w = s.step(w, dt32)
            res = measure_C(s, w, dt32, n_fd=20, percentiles=[0.95])
            if 0.95 in res:
                C_max = res[0.95]['C_max']
                if C_max > worst_C:
                    worst_C = C_max
                    worst_info = f"{ic_name} t≈{(epoch+1)*0.025:.3f}"

    print(f"\n  Worst C (top 5%): {worst_C:+.4f} at {worst_info}", flush=True)
    print(f"  Threshold: 1/4 = 0.2500", flush=True)
    print(f"  Margin: {0.25 - worst_C:.4f}", flush=True)
    if worst_C < 0.25:
        print(f"  STATUS: C < 1/4 → self-depletion wins → REGULARITY HOLDS", flush=True)
    else:
        print(f"  STATUS: C ≥ 1/4 → MARGIN VIOLATED — need more analysis", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)

if __name__ == '__main__':
    main()
