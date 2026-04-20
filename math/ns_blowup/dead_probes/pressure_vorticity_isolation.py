"""
Pressure-Vorticity Isolation Study

Goal: understand WHEN and WHY pressure helps or hurts the c₃ alignment.

Key question from the cross-check:
- TG/KP: pressure OPPOSES c₃ but -Ω² wins (c₃ > 1/3)
- ABC: pressure HELPS c₃ (both terms positive)
- Rings: pressure BEATS -Ω² (c₃ < 1/3, but α ≈ 0)
- Trefoil: α > 0 and GROWING

What determines the pressure's role?

Hypothesis: it depends on the SPATIAL STRUCTURE of ω.
- Volume-filling ω (many modes, isotropic): pressure is local-ish, -Ω² wins
- Localized ω (tube/filament): pressure is non-local (Biot-Savart of line), dominates

Test: compute the NON-LOCAL fraction of the pressure Hessian.
Decompose H = H_local (Yang) + H_nonlocal (remainder).
Measure: when does ||H_nonlocal|| > ||H_local||?

Also: compute the RATIO |ω|²/|S|² — this tells us if the flow is
vorticity-dominated (high ratio) or strain-dominated (low ratio).
Yang's formula is better when |ω| >> |S|.
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


def make_ic(solver, name):
    s = solver; X, Y, Z = s.X, s.Y, s.Z
    if name == 'TG':
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z); uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux), s.fft(uy), s.fft(torch.zeros_like(X)))
    elif name == 'KP':
        ux=torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
        uy=torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
        uz=torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
        return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))
    elif name == 'trefoil':
        wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
        n_pts=200; t_p=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
        cx=(torch.sin(t_p)+2*torch.sin(2*t_p))*0.5+pi
        cy=(torch.cos(t_p)-2*torch.cos(2*t_p))*0.5+pi
        cz=(-torch.sin(3*t_p))*0.5+pi
        tx=torch.cos(t_p)+4*torch.cos(2*t_p); ty=-torch.sin(t_p)+4*torch.sin(2*t_p)
        tz=-3*torch.cos(3*t_p); ds=2*pi/n_pts
        for i in range(n_pts):
            g=10.0*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
            wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))
    elif name == 'rings':
        wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
        for sign in [+1,-1]:
            z0=pi+sign*1.5; rho=((X-pi)**2+(Y-pi)**2).sqrt()
            core=((rho-0.8)**2+(Z-z0)**2).sqrt()
            st=5.0*torch.exp(-core**2/(2*0.3**2))
            wx+=sign*st*(-(Y-pi)/(rho+1e-10)); wy+=sign*st*((X-pi)/(rho+1e-10))
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))
    elif name == 'single_tube':
        # Single straight vortex tube — simplest localized structure
        rho = ((X-pi)**2 + (Y-pi)**2).sqrt()
        wz = 8.0 * torch.exp(-rho**2 / (2*0.4**2))
        return (s.D*s.fft(torch.zeros_like(X)), s.D*s.fft(torch.zeros_like(X)), s.D*s.fft(wz))
    elif name == 'two_tubes_perp':
        # Two perpendicular tubes — creates 3D interaction
        r1 = ((X-pi)**2 + (Y-pi)**2).sqrt()
        r2 = ((Y-pi)**2 + (Z-pi)**2).sqrt()
        wz = 8.0*torch.exp(-r1**2/(2*0.4**2))
        wx = 8.0*torch.exp(-r2**2/(2*0.4**2))
        wh = (s.D*s.fft(wx), s.D*s.fft(torch.zeros_like(X)), s.D*s.fft(wz))
        # Project div-free
        kdotw = s.kx*wh[0]+s.ky*wh[1]+s.kz*wh[2]
        return (wh[0]-s.kx*kdotw/s.ksq, wh[1]-s.ky*kdotw/s.ksq, wh[2]-s.kz*kdotw/s.ksq)
    else:
        raise ValueError(name)


def analyze_pressure_vorticity(solver, w, percentile=0.90, n_sample=500):
    """
    At high-|ω| points, measure:
    1. |ω|²/|S|² ratio (vorticity vs strain dominance)
    2. H_local (Yang) vs H_nonlocal (remainder) norms
    3. The spatial locality of ω (participation ratio / filling fraction)
    4. c₁, c₂, c₃, α as usual
    """
    D=solver.D; N=solver.N; kd=[solver.kx,solver.ky,solver.kz]
    u=solver.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=solver.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))

    wf=[solver.ifft(D*w[i]) for i in range(3)]
    om_sq = wf[0]**2+wf[1]**2+wf[2]**2
    om = om_sq.sqrt()

    # Full pressure Hessian
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): source-=A[i,j]*A[j,i]
    p_hat=-solver.fft(source)/solver.ksq; p_hat[0,0,0]=0
    H_full=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): H_full[i,j]=solver.ifft(-kd[i]*kd[j]*p_hat)

    # Yang local approximation: H_yang = -(1/4)(ω⊗ω - |ω|²I/3) + (Δp/3)I
    # Actually, let's compute the DEVIATORIC part of Yang:
    # H_dev_yang = -(1/4)(ω_i ω_j - |ω|²δ_ij/3)
    H_yang = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H_yang[i,j] = -0.25*(wf[i]*wf[j])
            if i == j:
                H_yang[i,j] += 0.25*om_sq/3
    # Add isotropic part: (Δp/3)I = (|ω|²/2 - |S|²)I/3
    S_sq_trace = sum((S[i,j]**2).clone() for i in range(3) for j in range(3))
    iso = (om_sq/2 - S_sq_trace)/3
    for i in range(3):
        H_yang[i,i] += iso

    # Non-local = H_full - H_yang
    H_nonlocal = H_full - H_yang

    thr = torch.quantile(om.flatten(), percentile)
    if thr < 1e-10: return None

    idx = (om > thr).nonzero(as_tuple=False)
    n = min(len(idx), n_sample)
    perm = torch.randperm(len(idx))[:n]; pts = idx[perm]

    res = {'om_sq_over_S_sq':[], 'H_local_norm':[], 'H_nonlocal_norm':[],
           'H_full_omega':[], 'H_yang_omega':[], 'H_nonlocal_omega':[],
           'c1':[], 'c2':[], 'c3':[], 'alpha':[]}

    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12: continue
        eh=wv/wn

        Sl=S[:,:,ix,iy,iz]
        ev,ec=torch.linalg.eigh(Sl)
        c1=(eh@ec[:,2]).item()**2; c2=(eh@ec[:,1]).item()**2; c3=(eh@ec[:,0]).item()**2
        al=sum(ev[j].item()*(eh@ec[:,j]).item()**2 for j in range(3))

        om_sq_local = om_sq[ix,iy,iz].item()
        S_sq_local = S_sq_trace[ix,iy,iz].item()
        ratio = om_sq_local / (S_sq_local + 1e-30)

        Hfl = H_full[:,:,ix,iy,iz]
        Hyl = H_yang[:,:,ix,iy,iz]
        Hnl = H_nonlocal[:,:,ix,iy,iz]

        res['om_sq_over_S_sq'].append(ratio)
        res['H_local_norm'].append(Hyl.norm().item())
        res['H_nonlocal_norm'].append(Hnl.norm().item())
        res['H_full_omega'].append((eh@Hfl@eh).item())
        res['H_yang_omega'].append((eh@Hyl@eh).item())
        res['H_nonlocal_omega'].append((eh@Hnl@eh).item())
        res['c1'].append(c1); res['c2'].append(c2); res['c3'].append(c3); res['alpha'].append(al)

    for k in res: res[k]=np.array(res[k])

    # Spatial filling fraction: what fraction of the domain has |ω| > 0.1*|ω|_max
    fill = (om > 0.1*om.max()).float().mean().item()

    res['fill_fraction'] = fill
    return res


def main():
    N=32; dt=1e-4

    print("="*70, flush=True)
    print("PRESSURE-VORTICITY ISOLATION STUDY", flush=True)
    print("="*70, flush=True)

    ics = ['TG', 'KP', 'trefoil', 'rings', 'single_tube', 'two_tubes_perp']
    evolve = {'TG':500, 'KP':500, 'trefoil':500, 'rings':500,
              'single_tube':500, 'two_tubes_perp':500}

    print(f"\n{'IC':>15s}  {'fill':>5s}  {'|ω|²/|S|²':>10s}  "
          f"{'||H_nl||/||H_y||':>16s}  {'H_ω(full)':>10s}  {'H_ω(yang)':>10s}  {'H_ω(nl)':>10s}  "
          f"{'c₃':>5s}  {'α':>8s}", flush=True)
    print("-"*110, flush=True)

    for ic_name in ics:
        s = NS3D(N, 0.0)
        try:
            w = make_ic(s, ic_name)
        except Exception as e:
            print(f"  {ic_name:>15s}: ERROR: {e}", flush=True)
            continue

        # Evolve
        t = 0.0
        for _ in range(evolve.get(ic_name, 500)):
            w = s.step(w, dt)
            t += dt

        r = analyze_pressure_vorticity(s, w)
        if r is None:
            print(f"  {ic_name:>15s}: insufficient data", flush=True)
            continue

        nl_ratio = np.mean(r['H_nonlocal_norm']) / (np.mean(r['H_local_norm']) + 1e-30)

        print(f"  {ic_name:>15s}  {r['fill_fraction']:5.3f}  {np.mean(r['om_sq_over_S_sq']):10.2f}  "
              f"{nl_ratio:16.3f}  {np.mean(r['H_full_omega']):+10.4f}  "
              f"{np.mean(r['H_yang_omega']):+10.4f}  {np.mean(r['H_nonlocal_omega']):+10.4f}  "
              f"{np.mean(r['c3']):5.3f}  {np.mean(r['alpha']):+8.4f}", flush=True)

    # Detailed time series for trefoil vs TG (the contrast case)
    print(f"\n\n{'='*70}", flush=True)
    print("TIME SERIES: TG vs trefoil — how does the pressure relationship evolve?", flush=True)
    print(f"{'='*70}", flush=True)

    for ic_name in ['TG', 'trefoil']:
        s = NS3D(N, 0.0)
        w = make_ic(s, ic_name)
        print(f"\n--- {ic_name} ---", flush=True)
        print(f"  {'t':>6s}  {'fill':>5s}  {'|ω|²/|S|²':>10s}  {'||Hnl||/||Hy||':>14s}  "
              f"{'Hω(full)':>9s}  {'Hω(yang)':>9s}  {'Hω(nl)':>9s}  "
              f"{'c₃':>5s}  {'α':>7s}", flush=True)

        t = 0.0
        for epoch in range(10):
            for _ in range(200):
                w = s.step(w, dt)
                t += dt

            r = analyze_pressure_vorticity(s, w, n_sample=300)
            if r is None: continue

            nl_ratio = np.mean(r['H_nonlocal_norm'])/(np.mean(r['H_local_norm'])+1e-30)
            print(f"  {t:6.3f}  {r['fill_fraction']:5.3f}  {np.mean(r['om_sq_over_S_sq']):10.2f}  "
                  f"{nl_ratio:14.3f}  {np.mean(r['H_full_omega']):+9.4f}  "
                  f"{np.mean(r['H_yang_omega']):+9.4f}  {np.mean(r['H_nonlocal_omega']):+9.4f}  "
                  f"{np.mean(r['c3']):5.3f}  {np.mean(r['alpha']):+7.4f}", flush=True)

    # KEY: what is the SIGN of the non-local pressure along ω?
    print(f"\n\n{'='*70}", flush=True)
    print("KEY QUESTION: Sign of non-local pressure H_ω for each IC", flush=True)
    print("  Positive = stretching along ω (bad)", flush=True)
    print("  Negative = compression along ω (good)", flush=True)
    print(f"{'='*70}", flush=True)

    for ic_name in ics:
        s = NS3D(N, 0.0)
        w = make_ic(s, ic_name)
        for _ in range(500): w = s.step(w, dt)

        r = analyze_pressure_vorticity(s, w)
        if r is None: continue

        h_nl = r['H_nonlocal_omega']
        pct_pos = (h_nl > 0).mean() * 100
        print(f"  {ic_name:>15s}: H_ω(nonlocal) mean={h_nl.mean():+.4f}  "
              f"positive at {pct_pos:.0f}% of points  "
              f"fill={r['fill_fraction']:.3f}", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
