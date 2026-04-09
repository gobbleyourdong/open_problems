"""
ENTERING ALPHA: what's α at points about to become the max?

The bootstrap argument: each new max particle enters with α_enter.
Then Dα/Dt < 0 at high |ω| makes it decrease.
If α_enter is bounded: α at the max is bounded → regularity.

Measure α at |ω| in [0.8×||ω||∞, 0.95×||ω||∞] — the "approaching" region.
These are the particles that will soon become the new max.
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

def measure_alpha_profile(s, w):
    """Measure α as a function of |ω|/||ω||∞ (distance from max)."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    om_max=om.max().item()
    if om_max<1e-10: return None

    # α at every point
    alpha_field=torch.zeros(N,N,N,dtype=DTYPE)
    Hww_field=torch.zeros(N,N,N,dtype=DTYPE)

    # Compute S and H
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)

    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    for i in range(3):
        for j in range(3):
            alpha_field+=wf[i]*S[i,j]*wf[j]
            Hww_field+=wf[i]*H[i,j]*wf[j]
    alpha_field=alpha_field/(om_sq+1e-30)
    Hww_field=Hww_field/(om_sq+1e-30)

    # Bin by |ω|/||ω||∞
    frac=om/om_max
    frac_flat=frac.flatten()
    alpha_flat=alpha_field.flatten()
    Hww_flat=Hww_field.flatten()
    om_flat=om.flatten()

    bins=np.array([0.3,0.5,0.7,0.8,0.85,0.9,0.95,0.98,1.001])
    results=[]
    for i in range(len(bins)-1):
        mask=(frac_flat>=bins[i])&(frac_flat<bins[i+1])
        if mask.sum()<5: continue
        a=alpha_flat[mask];h=Hww_flat[mask];o=om_flat[mask]
        results.append({
            'frac_lo':bins[i],'frac_hi':bins[i+1],
            'alpha_mean':a.mean().item(),'alpha_max':a.max().item(),
            'alpha_pos_frac':(a>0).float().mean().item(),
            'Hww_mean':h.mean().item(),
            'om_mean':o.mean().item(),
            'n':int(mask.sum()),
        })
    return results, om_max

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
    N=32;dt=1e-4
    print("="*70,flush=True)
    print("ENTERING ALPHA: α profile as function of |ω|/||ω||∞",flush=True)
    print("="*70,flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)

    for evolve in [200, 500, 1000, 2000, 4000]:
        if evolve>200:
            for _ in range(evolve-prev): w=s.step(w,dt)
        else:
            for _ in range(evolve): w=s.step(w,dt)
        prev=evolve
        t=evolve*dt

        result=measure_alpha_profile(s,w)
        if result is None: continue
        bins,om_max=result

        print(f"\n  t={t:.3f}, ||ω||∞={om_max:.2f}",flush=True)
        print(f"  {'|ω|/max':>10s}  {'<α>':>8s}  {'max α':>8s}  {'α>0':>6s}  "
              f"{'<H_ωω>':>8s}  {'<|ω|>':>7s}  {'n':>5s}",flush=True)

        for b in bins:
            pct=f"[{b['frac_lo']:.2f},{b['frac_hi']:.2f})"
            print(f"  {pct:>10s}  {b['alpha_mean']:+8.4f}  {b['alpha_max']:+8.4f}  "
                  f"{b['alpha_pos_frac']*100:5.1f}%  {b['Hww_mean']:+8.4f}  "
                  f"{b['om_mean']:7.2f}  {b['n']:5d}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("KEY QUESTION: at |ω| > 0.9×||ω||∞ (the 'approaching' zone),",flush=True)
    print("  is α bounded? Is H_ωω positive?",flush=True)
    print("  If YES: particles entering the max have bounded α",flush=True)
    print("  → bootstrap works → α at max bounded → regularity",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
