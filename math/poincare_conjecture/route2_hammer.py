"""
ROUTE 2 DEEP DIVE: The enstrophy route.

The key quantity: <α> = ∫|ω|²α dx / ∫|ω|² dx (enstrophy-weighted mean α)

This controls enstrophy growth: d/dt∫|ω|² = 2∫|ω|²α = 2<α>∫|ω|²

If <α> ≤ C: enstrophy ≤ E₀ exp(2Ct) → bounded on finite intervals.
Then: ||ω||∞ ≤ C' ||ω||_{H^s} ≤ C'' (enstrophy)^p → bounded.

TESTS:
1. Long-run <α> for trefoil (hardest IC) — does it stay bounded?
2. Analytical bound on <α> from the trace-free constraint
3. The connection: <α> = <Σ λ_i c_i> = <λ₁c₁ + λ₂c₂ + λ₃c₃>
   With trace-free λ₁+λ₂+λ₃=0 and c₁+c₂+c₃=1:
   <α> = <λ₁(c₁-1/3) + λ₂(c₂-1/3) + λ₃(c₃-1/3)>
   If c_i ≈ 1/3 (isotropic): <α> = 0 exactly!
4. Cross-validate on ALL ICs
5. Test with viscosity (NS, not just Euler)
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

def enstrophy_budget(s, w):
    """Compute enstrophy, stretching, and weighted <α>."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];L=s.Lx
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2

    u_h=s.vel(*w)
    # ω·Sω = Σ ω_i S_ij ω_j
    wSw=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Sij=0.5*(s.ifft(1j*kd[j]*D*u_h[i])+s.ifft(1j*kd[i]*D*u_h[j]))
            wSw+=wf[i]*Sij*wf[j]

    enstrophy=om_sq.mean().item()*L**3
    stretching=wSw.mean().item()*L**3
    # Weighted average: <α> = ∫ω·Sω / ∫|ω|²
    alpha_weighted=(wSw.sum()/(om_sq.sum()+1e-30)).item()
    # Also: simple volume average of α (at points where |ω|>0)
    alpha_field=wSw/(om_sq+1e-30)
    alpha_vol=alpha_field.mean().item()

    # Palinstrophy (for Sobolev bound)
    # ∫|∇ω|² = Σ |k|² |ω_hat|²
    palinstrophy=0.
    for i in range(3):
        palinstrophy+=(s.ksq*(w[i].abs()**2)).sum().item()
    palinstrophy/=N**3  # normalize

    return {
        'enstrophy': enstrophy,
        'stretching': stretching,
        'alpha_w': alpha_weighted,
        'alpha_vol': alpha_vol,
        'palinstrophy': palinstrophy,
        'om_max': (om_sq.sqrt()).max().item(),
    }

def make_ic(s, name):
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
    dt=1e-4; N=32

    print("="*70,flush=True)
    print("ROUTE 2 HAMMER: enstrophy budget, long runs, all ICs",flush=True)
    print("="*70,flush=True)

    # =====================================================================
    # TEST 1: Long run for trefoil
    # =====================================================================
    print(f"\n--- TEST 1: Trefoil long run (Euler, t=0 to 0.8) ---",flush=True)
    print(f"  {'t':>6s}  {'E':>10s}  {'∫ωSω':>10s}  {'<α>_w':>9s}  {'<α>_v':>9s}  "
          f"{'|ω|∞':>7s}  {'P':>10s}  {'P/E':>7s}",flush=True)

    s=NS3D(N,0.);w=make_ic(s,'trefoil')
    t=0.; alpha_ws=[]
    for epoch in range(40):
        b=enstrophy_budget(s,w)
        alpha_ws.append(b['alpha_w'])
        if epoch%4==0:
            print(f"  {t:6.4f}  {b['enstrophy']:10.2f}  {b['stretching']:+10.2f}  "
                  f"{b['alpha_w']:+9.5f}  {b['alpha_vol']:+9.5f}  "
                  f"{b['om_max']:7.2f}  {b['palinstrophy']:10.2f}  "
                  f"{b['palinstrophy']/(b['enstrophy']+1e-30):7.2f}",flush=True)
        for _ in range(200): w=s.step(w,dt); t+=dt

    alpha_ws=np.array(alpha_ws)
    print(f"\n  <α>_weighted: mean={alpha_ws.mean():.5f}  max={alpha_ws.max():.5f}  "
          f"min={alpha_ws.min():.5f}",flush=True)
    print(f"  BOUNDED: {'YES ✓' if alpha_ws.max()<0.5 else 'MARGINAL'}",flush=True)

    # =====================================================================
    # TEST 2: All ICs comparison
    # =====================================================================
    print(f"\n\n--- TEST 2: All ICs at t=0.3 ---",flush=True)
    print(f"  {'IC':>10s}  {'E':>10s}  {'<α>_w':>9s}  {'<α>_vol':>9s}  "
          f"{'|ω|∞':>7s}  {'P/E':>7s}",flush=True)

    for ic_name in ['TG','KP','trefoil']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        for _ in range(3000): w=s.step(w,dt)
        b=enstrophy_budget(s,w)
        print(f"  {ic_name:>10s}  {b['enstrophy']:10.2f}  {b['alpha_w']:+9.5f}  "
              f"{b['alpha_vol']:+9.5f}  {b['om_max']:7.2f}  "
              f"{b['palinstrophy']/(b['enstrophy']+1e-30):7.2f}",flush=True)

    # =====================================================================
    # TEST 3: Analytical bound on <α>
    # =====================================================================
    print(f"\n\n--- TEST 3: Analytical bound ---",flush=True)
    print("""
  <α> = ∫ω·Sω / ∫|ω|² = ∫Σ λ_i c_i |ω|² / ∫|ω|²

  With trace-free λ₁+λ₂+λ₃=0:
    α = λ₁c₁ + λ₂c₂ + λ₃c₃
      = λ₁(c₁-1/3) + λ₂(c₂-1/3) + λ₃(c₃-1/3)

  So α = 0 when c_i = 1/3 (isotropic alignment).

  |α| ≤ |λ₁||c₁-1/3| + |λ₂||c₂-1/3| + |λ₃||c₃-1/3|
       ≤ max|λ_i| × Σ|c_i-1/3|
       ≤ |S| × 2  (since |c_i-1/3| ≤ 2/3 and sum ≤ 2)

  So |α| ≤ 2|S|.

  For the enstrophy-weighted average:
  |<α>| ≤ 2 <|S|> where <|S|> = ∫|S||ω|² / ∫|ω|²

  By Cauchy-Schwarz on the Biot-Savart law:
    |S(x)| ≤ C ∫ |ω(y)| / |x-y|² dy  (in 3D)

  This gives ||S||∞ ≤ C ||ω||_{L³} (by Hardy-Littlewood-Sobolev).
  And ||ω||_{L³} ≤ ||ω||_{L²}^{1/2} ||ω||_{L∞}^{1/2}.

  So the bound:
  |<α>| ≤ 2 ||S||∞ ≤ C ||ω||_{L³} ≤ C √(E) √(||ω||∞)

  This GROWS with ||ω||∞ — not useful for proving bounded <α>.
""",flush=True)

    # But: the NUMERICAL data shows <α> stays bounded even as ||ω||∞ grows.
    # This suggests a CANCELLATION that the worst-case bound misses.

    # =====================================================================
    # TEST 4: Does <α> grow with ||ω||∞?
    # =====================================================================
    print(f"--- TEST 4: <α> vs ||ω||∞ scaling ---",flush=True)
    print(f"  If <α> ~ ||ω||∞^0: bounded (GOOD, proof works)",flush=True)
    print(f"  If <α> ~ ||ω||∞^p with p>0: unbounded (BAD)\n",flush=True)

    s=NS3D(N,0.);w=make_ic(s,'trefoil')
    t=0.; data_aw=[]; data_om=[]
    for epoch in range(50):
        b=enstrophy_budget(s,w)
        data_aw.append(b['alpha_w']); data_om.append(b['om_max'])
        for _ in range(200): w=s.step(w,dt); t+=dt

    data_aw=np.array(data_aw); data_om=np.array(data_om)
    # Linear regression: log|<α>| vs log||ω||∞
    mask=data_aw>0
    if mask.sum()>5:
        log_aw=np.log(data_aw[mask])
        log_om=np.log(data_om[mask])
        coeffs=np.polyfit(log_om,log_aw,1)
        p=coeffs[0]
        print(f"  Power law fit: <α> ~ ||ω||∞^{p:.3f}",flush=True)
        if p<0.5:
            print(f"  p < 0.5: <α> grows SLOWER than √||ω||∞ → manageable",flush=True)
        elif p<1:
            print(f"  p < 1: <α> grows sub-linearly → may still work",flush=True)
        else:
            print(f"  p ≥ 1: <α> grows at least linearly → DANGEROUS",flush=True)
    else:
        print(f"  <α> is mostly negative — no positive growth to fit",flush=True)
        print(f"  <α> range: [{data_aw.min():.5f}, {data_aw.max():.5f}]",flush=True)

    # Scatter: <α> vs ||ω||∞
    print(f"\n  {'||ω||∞':>8s}  {'<α>':>10s}",flush=True)
    for i in range(0,len(data_aw),5):
        print(f"  {data_om[i]:8.2f}  {data_aw[i]:+10.5f}",flush=True)

    # =====================================================================
    # TEST 5: Viscous NS — does viscosity help?
    # =====================================================================
    print(f"\n\n--- TEST 5: NS with viscosity (trefoil) ---",flush=True)
    for nu in [0., 1e-3, 1e-2]:
        s=NS3D(N,nu);w=make_ic(s,'trefoil')
        t=0.; aw_max=-999
        for epoch in range(20):
            b=enstrophy_budget(s,w)
            if b['alpha_w']>aw_max: aw_max=b['alpha_w']
            for _ in range(200): w=s.step(w,dt); t+=dt
        print(f"  ν={nu:.0e}: max <α> over t=[0,{t:.2f}] = {aw_max:+.5f}  "
              f"|ω|∞(final)={s.om_max(w):.2f}",flush=True)

    # =====================================================================
    # TEST 6: The EXACT identity
    # =====================================================================
    print(f"\n\n--- TEST 6: Exact identity ∫ω·Sω = -(1/4)∫|ω|⁴/(something)? ---",flush=True)
    print("  Actually: ∫ω·Sω = (1/2)∫ω_i ω_j (∂u_i/∂x_j + ∂u_j/∂x_i)",flush=True)
    print("  = ∫ω_i ω_j ∂u_i/∂x_j (by symmetry of ω_i ω_j)",flush=True)
    print("  = ∫ω_i ω_j A_ij",flush=True)
    print("  = ∫ω · (A·ω)  where A = ∇u",flush=True)
    print("  = ∫ω · (Dω/Dt)  (since Dω/Dt = A·ω for Euler)",flush=True)
    print("  = (1/2) D/Dt ∫|ω|²  (chain rule)",flush=True)
    print("  ✓ Consistent: d/dt∫|ω|² = 2∫ω·Sω\n",flush=True)

    # The bound on ∫ω·Sω:
    # |∫ω·Sω| = |∫ω·(Dω/Dt)| = |(1/2)d/dt∫|ω|²|
    # This is just saying the enstrophy growth rate IS 2∫ω·Sω.
    # Not independently useful.

    # But: ∫ω·Sω = ∫ω_i ω_j S_ij = ∫ω_i ω_j (∂u_i/∂x_j)
    # Integrate by parts: = -∫u_i ∂(ω_i ω_j)/∂x_j (periodic BC)
    # = -∫u_i (ω_j ∂ω_i/∂x_j + ω_i ∂ω_j/∂x_j)
    # = -∫u_i ω_j ∂ω_i/∂x_j  (since ∂ω_j/∂x_j = ∇·ω = 0)
    # = -∫(u·∇ω)·ω ... wait, this isn't new either.

    # Actually there IS a useful identity:
    # ∫ω·Sω = -(1/4)d/dt∫|A|²  ... no, that's not right.

    # The key bound from the literature:
    # |∫ω·Sω| ≤ ||S||_∞ ∫|ω|² = ||S||_∞ × enstrophy
    # And ||S||_∞ ≤ C ||ω||_{BMO} (Calderon-Zygmund)
    # So |<α>| ≤ ||S||_∞ ≤ C ||ω||_{BMO}

    # The BMO norm of ω: ||ω||_{BMO} ≤ C log(||∇ω||_2 / ||ω||_2) × ||ω||_∞
    # (by the logarithmic Sobolev inequality)

    # So |<α>| ≤ C ||ω||_∞ log(P/E) where P = palinstrophy, E = enstrophy.

    print("  Literature bound: |<α>| ≤ C ||S||∞ ≤ C' ||ω||_∞ log(P/E)",flush=True)
    print("  Verify numerically:\n",flush=True)

    s=NS3D(N,0.);w=make_ic(s,'trefoil')
    t=0.
    print(f"  {'t':>6s}  {'<α>':>9s}  {'||ω||∞':>8s}  {'P/E':>8s}  "
          f"{'log(P/E)':>8s}  {'||ω||∞·log':>10s}  {'ratio':>8s}",flush=True)
    for epoch in range(20):
        b=enstrophy_budget(s,w)
        pe=b['palinstrophy']/(b['enstrophy']+1e-30)
        log_pe=np.log(max(pe,1))
        bound=b['om_max']*log_pe
        ratio=abs(b['alpha_w'])/(bound+1e-30)
        print(f"  {t:6.4f}  {b['alpha_w']:+9.5f}  {b['om_max']:8.2f}  "
              f"{pe:8.2f}  {log_pe:8.3f}  {bound:10.4f}  {ratio:8.5f}",flush=True)
        for _ in range(200): w=s.step(w,dt); t+=dt

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
