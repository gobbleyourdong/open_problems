"""
MIGRATION EFFECT: the mechanism that saves the PDE from the ODE blowup.

ODE predicts: d|ω|_max/dt = α_max × |ω|_max (if max is a material point)
PDE actual:   d||ω||∞/dt = α_max × ||ω||∞ + M  (M = migration correction)

If M < 0: migration HELPS (max moves to less-stretched region)
If M = 0: no migration (ODE is correct → blowup)
If M > 0: migration HURTS (shouldn't happen)

Measure M directly from DNS. This is the QUANTIFIED missing mechanism.
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

def get_max_info(s, w):
    """Get |ω|_max, α at max, position of max."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return 0.,0.,np.array([0.,0.,0.])
    eh=wv/wn;Sl=S[:,:,ix,iy,iz]
    alpha=(eh@Sl@eh).item()
    pos=np.array([ix*2*pi/N, iy*2*pi/N, iz*2*pi/N])
    return wn.item(), alpha, pos

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
    N=32; dt=1e-4; fd_steps=5  # very fine finite differences
    print("="*70,flush=True)
    print("MIGRATION EFFECT: what saves the PDE from ODE blowup?",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.)
        if ic_name=='trefoil':
            w=make_trefoil(s)
        else:
            X,Y,Z=s.X,s.Y,s.Z
            ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))

        print(f"\n--- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'|ω|∞':>7s}  {'α_max':>8s}  {'α·|ω|':>8s}  {'d|ω|/dt':>8s}  "
              f"{'M(migr)':>8s}  {'M/α|ω|':>8s}  {'pos_x':>6s}  {'Δpos':>6s}",flush=True)

        t=0.; om_prev=None; pos_prev=None
        migration_fracs=[]

        for epoch in range(80):
            om, alpha, pos = get_max_info(s, w)

            if om_prev is not None:
                domdt = (om - om_prev) / (fd_steps * dt)
                alpha_om = alpha * om  # ODE prediction
                M = domdt - alpha_om  # migration effect

                # Position change
                dpos = np.linalg.norm(pos - pos_prev) if pos_prev is not None else 0
                # Handle periodic wrapping
                dp = pos - pos_prev if pos_prev is not None else np.zeros(3)
                dp = np.minimum(np.abs(dp), 2*pi - np.abs(dp))
                dpos = np.linalg.norm(dp)

                migration_frac = M / (abs(alpha_om) + 1e-30)
                migration_fracs.append(migration_frac)

                if epoch % 8 == 0:
                    print(f"  {t:6.4f}  {om:7.2f}  {alpha:+8.4f}  {alpha_om:+8.2f}  "
                          f"{domdt:+8.2f}  {M:+8.2f}  {migration_frac:+8.3f}  "
                          f"{pos[0]:6.2f}  {dpos:6.3f}",flush=True)

            om_prev = om; pos_prev = pos.copy()
            for _ in range(fd_steps): w=s.step(w,dt); t+=dt

        mf = np.array(migration_fracs)
        print(f"\n  Migration effect M / (α·|ω|):",flush=True)
        print(f"    mean = {mf.mean():+.4f}",flush=True)
        print(f"    median = {np.median(mf):+.4f}",flush=True)
        print(f"    M < 0 (helps): {(mf<0).sum()}/{len(mf)} ({100*(mf<0).mean():.0f}%)",flush=True)

        if (mf<0).mean() > 0.5:
            eff_reduction = -mf[mf<0].mean()
            print(f"    Effective α reduction from migration: {eff_reduction*100:.0f}%",flush=True)
            print(f"    → Effective α = α_max × (1 - {eff_reduction:.2f})",flush=True)
            # If migration reduces α by fraction f, effective growth:
            # d|ω|/dt = (1-f)α|ω| instead of α|ω|
            # Blowup only if (1-f)√C > some threshold
            print(f"    → With C=0.03: effective √C reduced from {np.sqrt(0.03):.3f} to "
                  f"{np.sqrt(0.03)*(1-eff_reduction):.3f}",flush=True)

    # Compare: ODE prediction vs actual for trefoil
    print(f"\n\n{'='*70}",flush=True)
    print("ODE vs PDE: predicted vs actual ||ω||∞(t)",flush=True)
    print(f"{'='*70}",flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)

    # Collect dense trajectory
    times=[]; oms=[]; alphas=[]
    t=0.
    for step in range(8000):
        if step%10==0:
            om,alpha,_=get_max_info(s,w)
            times.append(t);oms.append(om);alphas.append(alpha)
        w=s.step(w,dt);t+=dt

    times=np.array(times);oms=np.array(oms);alphas=np.array(alphas)

    # ODE prediction: integrate d|ω|/dt = α(t)·|ω| using MEASURED α
    om_ode=[oms[0]]
    for i in range(1,len(times)):
        dt_i=times[i]-times[i-1]
        om_ode.append(om_ode[-1]*np.exp(alphas[i-1]*dt_i))
    om_ode=np.array(om_ode)

    print(f"\n  {'t':>6s}  {'|ω| PDE':>9s}  {'|ω| ODE':>9s}  {'ratio':>7s}  {'α':>8s}",flush=True)
    for i in range(0,len(times),len(times)//12):
        ratio=oms[i]/(om_ode[i]+1e-30)
        print(f"  {times[i]:6.3f}  {oms[i]:9.2f}  {om_ode[i]:9.2f}  {ratio:7.4f}  {alphas[i]:+8.4f}",flush=True)

    print(f"\n  Final: PDE |ω|={oms[-1]:.2f}, ODE |ω|={om_ode[-1]:.2f}",flush=True)
    print(f"  Ratio PDE/ODE = {oms[-1]/om_ode[-1]:.4f}",flush=True)
    print(f"  Migration slowed growth by factor {om_ode[-1]/oms[-1]:.1f}×",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
