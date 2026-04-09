"""
TRANSPORT EQUATION FOR THE RATIO R = |H_dev,ωω| / (Δp/3).

If R satisfies DR/Dt < 0 when R → 1: maximum principle → R < 1 forever.

Instead of proving R < 1 from a static bound on the CZ operator,
prove R < 1 DYNAMICALLY by showing the flow keeps it below 1.

Measure: DR/Dt at points where R is LARGEST. If DR/Dt < 0 there,
R can't grow past its current max → bootstrap.
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

def compute_R_field(s, w):
    """Compute R = |H_dev,ωω|/(Δp/3) at every grid point."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    # Δp = source (note: Δp = -A_ijA_ji = |ω|²/2 - |S|²)
    Dp=source  # this IS Δp

    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()

    # H_ωω at every point
    Hww=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):Hww+=wf[i]*H[i,j]*wf[j]
    Hww=Hww/(om_sq+1e-30)

    # H_iso = Δp/3
    Hiso=Dp/3

    # H_dev,ωω = H_ωω - H_iso
    Hdev=Hww-Hiso

    # R = |H_dev,ωω| / |H_iso|  (at points where Δp > 0)
    R=Hdev.abs()/(Hiso.abs()+1e-30)

    return om, R, Dp, Hww, Hiso, Hdev

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
    N=32;dt=1e-4;fd_steps=30
    print("="*70,flush=True)
    print("RATIO TRANSPORT: does R = |H_dev|/|H_iso| satisfy max principle?",flush=True)
    print("="*70,flush=True)
    print("  If DR/Dt < 0 at max-R points: R can't grow → stays < 1\n",flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)
    for _ in range(300):w=s.step(w,dt)  # skip transient

    t=0.03
    R_maxes=[]
    for epoch in range(12):
        # Snapshot 1
        om1,R1,Dp1,Hww1,Hiso1,Hdev1=compute_R_field(s,w)
        om_max1=om1.max().item()

        # High-|ω| mask where Δp > 0
        hi_mask=(om1>0.5*om_max1)&(Dp1>0.1)
        if hi_mask.sum()<10:
            for _ in range(fd_steps):w=s.step(w,dt);t+=dt
            continue

        R1_hi=R1[hi_mask]
        R_max=R1_hi.max().item()
        R_mean=R1_hi.mean().item()
        R_maxes.append(R_max)

        # Evolve for finite difference
        w_save=tuple(wi.clone() for wi in w)
        for _ in range(fd_steps):w=s.step(w,dt);t+=dt

        # Snapshot 2
        om2,R2,Dp2,_,_,_=compute_R_field(s,w)

        # DR/Dt by finite difference (Eulerian, at high-|ω| points of snapshot 1)
        dR=(R2-R1)/(fd_steps*dt)
        dR_hi=dR[hi_mask]

        # At points where R is LARGE (top 10% of R in high-|ω| region)
        R_thr=torch.quantile(R1_hi,0.90).item()
        large_R_mask=hi_mask&(R1>R_thr)
        if large_R_mask.sum()>0:
            dR_large=dR[large_R_mask]
            R_large=R1[large_R_mask]
            frac_neg=(dR_large<0).float().mean().item()*100
            print(f"  t={t:.3f}: R_max={R_max:.3f}  R_mean={R_mean:.3f}  "
                  f"At top-R pts: dR/dt<0: {frac_neg:.0f}%  "
                  f"mean dR={dR_large.mean().item():+.3f}  "
                  f"max R here={R_large.max().item():.3f}",flush=True)
        else:
            print(f"  t={t:.3f}: R_max={R_max:.3f}  R_mean={R_mean:.3f}  (no large-R pts)",flush=True)

    if R_maxes:
        rm=np.array(R_maxes)
        print(f"\n  R_max over time: {rm}",flush=True)
        print(f"  R_max trend: {'DECREASING ✓' if rm[-1]<rm[0] else 'INCREASING or FLAT'}",flush=True)
        print(f"  max(R_max) = {rm.max():.4f}",flush=True)
        print(f"  max(R_max) < 1: {'YES ✓' if rm.max()<1 else 'NO ✗'}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("IF dR/dt < 0 at high-R points: MAXIMUM PRINCIPLE HOLDS",flush=True)
    print("→ R started < 1 and stays < 1 → H_ωω > 0 → regularity",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
