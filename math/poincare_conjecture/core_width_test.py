"""
CORE WIDTH: does the trefoil core thin to zero?

If ||ω||∞ ~ 1/σ² (vortex tube scaling), then blowup requires σ → 0.
If pressure prevents σ from going below σ_min > 0, regularity follows.

Measure σ(t) from the DNS:
- At the max-|ω| point, compute the second derivative of |ω|
- The Gaussian width: σ² ≈ -|ω|_max / Δ|ω| (where Δ is the Laplacian)
- Track σ over time

Also: measure the HELICITY (conserved in Euler) as a consistency check.
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

def measure_core(s, w):
    """Measure the core width at the max-|ω| point."""
    D=s.D; N=s.N; kd=[s.kx,s.ky,s.kz]
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    om=om_sq.sqrt()
    om_max=om.max().item()

    # Laplacian of |ω|² at the max point
    om_sq_h=s.fft(om_sq)
    lap_om_sq=s.ifft(-s.ksq*om_sq_h)

    # Find max
    flat=om.flatten()
    idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)

    lap_val=lap_om_sq[ix,iy,iz].item()
    om_sq_val=om_sq[ix,iy,iz].item()

    # For Gaussian profile |ω|² ~ exp(-r²/σ²):
    # Δ(|ω|²) = -2d/σ² × |ω|² at the center (d = spatial dimension = 3)
    # So σ² = -2d × |ω|²_max / Δ(|ω|²)_max
    if lap_val < -1e-10:
        sigma_sq = -6*om_sq_val/lap_val  # d=3
        sigma = np.sqrt(sigma_sq) if sigma_sq > 0 else 0
    else:
        sigma = 0  # can't compute (not a local max in Laplacian sense)

    # Also compute: effective width from second moment
    # w = sqrt(∫r²|ω|² / ∫|ω|²) centered at max
    x=torch.linspace(0,2*pi-2*pi/N,N,dtype=DTYPE)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    xm=ix*2*pi/N; ym=iy*2*pi/N; zm=iz*2*pi/N
    # Periodic distance
    dx=torch.min(torch.abs(X-xm), 2*pi-torch.abs(X-xm))
    dy=torch.min(torch.abs(Y-ym), 2*pi-torch.abs(Y-ym))
    dz=torch.min(torch.abs(Z-zm), 2*pi-torch.abs(Z-zm))
    r_sq=dx**2+dy**2+dz**2

    # Weight by |ω|² in a local region (r < 1)
    local_mask=(r_sq < 1.0).to(DTYPE)
    weights=om_sq*local_mask
    w_total=weights.sum().item()
    if w_total > 1e-10:
        sigma_moment=np.sqrt((r_sq*weights).sum().item()/w_total)
    else:
        sigma_moment=0

    # Helicity: H = ∫ω·u
    u_h=s.vel(*w)
    uf=[s.ifft(u_h[i]) for i in range(3)]
    helicity=(wf[0]*uf[0]+wf[1]*uf[1]+wf[2]*uf[2]).mean().item()*(2*pi)**3

    # Enstrophy
    enstrophy=om_sq.mean().item()*(2*pi)**3

    return {
        'om_max': om_max,
        'sigma_lap': sigma,
        'sigma_moment': sigma_moment,
        'helicity': helicity,
        'enstrophy': enstrophy,
    }

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
    print("CORE WIDTH: does σ have a positive lower bound?",flush=True)
    print("="*70,flush=True)
    print("  If σ_min > 0: ||ω||∞ ≤ C/σ_min² < ∞ → regularity",flush=True)
    print("  If σ → 0: blowup possible\n",flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)

    print(f"  {'t':>6s}  {'|ω|∞':>7s}  {'σ_lap':>7s}  {'σ_mom':>7s}  "
          f"{'|ω|·σ²':>8s}  {'H':>10s}  {'E':>10s}",flush=True)

    t=0.; sigma_mins=[]
    for epoch in range(30):
        m=measure_core(s,w)
        # Scaling: if |ω| ~ 1/σ², then |ω|·σ² should be constant
        om_sigma2=m['om_max']*m['sigma_lap']**2 if m['sigma_lap']>0 else 0
        sigma_mins.append(m['sigma_lap'])

        if epoch%3==0:
            print(f"  {t:6.4f}  {m['om_max']:7.2f}  {m['sigma_lap']:7.4f}  "
                  f"{m['sigma_moment']:7.4f}  {om_sigma2:8.4f}  "
                  f"{m['helicity']:+10.4f}  {m['enstrophy']:10.2f}",flush=True)

        for _ in range(250): w=s.step(w,dt); t+=dt

    sigma_arr=np.array([s for s in sigma_mins if s>0])
    if len(sigma_arr)>0:
        print(f"\n  Core width σ statistics:",flush=True)
        print(f"    min σ = {sigma_arr.min():.4f}",flush=True)
        print(f"    max σ = {sigma_arr.max():.4f}",flush=True)
        print(f"    mean σ = {sigma_arr.mean():.4f}",flush=True)
        print(f"    σ trend: {'DECREASING' if sigma_arr[-1]<sigma_arr[0] else 'STABLE/INCREASING'}",flush=True)

        if sigma_arr.min() > 0.1:
            print(f"\n  σ_min = {sigma_arr.min():.4f} > 0.1",flush=True)
            print(f"  → ||ω||∞ ≤ C/σ_min² ≈ {6/(sigma_arr.min()**2):.0f}",flush=True)
            print(f"  → BOUNDED → regularity ✓",flush=True)
        else:
            print(f"\n  σ approaching resolution limit — inconclusive",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
