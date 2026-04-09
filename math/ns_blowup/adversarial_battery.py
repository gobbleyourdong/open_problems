"""
INSTANCE B: Adversarial IC battery.
Try to push |H_dev,ωω|/(Δp/3) past 1.0 at high |ω|.

Battery:
1. Thin trefoil (σ=0.15) — more localized, more anisotropic
2. Ultra-thin trefoil (σ=0.10) — extreme localization
3. Close perpendicular collision (sep=0.3σ)
4. Linked trefoils (two interlocking knots)
5. Flat pancake (vortex sheet, extreme anisotropy)
6. Point-like vortex blob (3D Gaussian, isotropic baseline)
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

def measure_ratio(s, w, frac_lo=0.8):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()
    om_max=om.max().item()
    if om_max<1e-10:return None
    mask=om>frac_lo*om_max
    idx=mask.nonzero(as_tuple=False)
    n=min(len(idx),500);perm=torch.randperm(len(idx))[:n];pts=idx[perm]
    hiso_list=[];hdev_list=[];hww_list=[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12:continue
        eh=wv/wn;Hl=H[:,:,ix,iy,iz]
        trH=Hl.trace().item();hww=(eh@Hl@eh).item()
        hiso=trH/3;hdev=hww-hiso
        hiso_list.append(hiso);hdev_list.append(hdev);hww_list.append(hww)
    if not hiso_list:return None
    hi=np.abs(np.array(hiso_list)).mean();hd=np.abs(np.array(hdev_list)).mean()
    return {'ratio':hd/(hi+1e-30),'om_max':om_max,
            'Hww_mean':np.mean(hww_list),'Hww_pos':(np.array(hww_list)>0).mean(),
            'fill':(om>0.1*om_max).float().mean().item(),'n':len(hiso_list)}

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

def make_linked_trefoils(s, amp=10., sigma=0.25):
    """Two trefoils offset and linked."""
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    for offset, sign in [((0,0,0), 1), ((0.5,0.5,0), -1)]:
        tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
        cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.4+pi+offset[0]
        cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.4+pi+offset[1]
        cz=(-torch.sin(3*tp))*0.4+pi+offset[2]
        tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
        ds=2*pi/200
        for i in range(200):
            g=sign*amp*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*sigma**2))*ds
            wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def make_pancake(s, amp=15., sigma_r=0.8, sigma_z=0.1):
    """Flat vortex pancake — extreme anisotropy."""
    X,Y,Z=s.X,s.Y,s.Z
    r=((X-pi)**2+(Y-pi)**2).sqrt()
    wz=amp*torch.exp(-r**2/(2*sigma_r**2))*torch.exp(-(Z-pi)**2/(2*sigma_z**2))
    wx=torch.zeros_like(X);wy=torch.zeros_like(X)
    wh=(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
    kdotw=s.kx*wh[0]+s.ky*wh[1]+s.kz*wh[2]
    return(wh[0]-s.kx*kdotw/s.ksq,wh[1]-s.ky*kdotw/s.ksq,wh[2]-s.kz*kdotw/s.ksq)

def make_close_collision(s, amp=15., sep=0.3, sigma=0.2):
    """Two perpendicular tubes at VERY close range."""
    X,Y,Z=s.X,s.Y,s.Z
    r1=((X-pi)**2+(Y-pi-sep/2)**2).sqrt()
    r2=((Y-pi)**2+(Z-pi+sep/2)**2).sqrt()
    wz=amp*torch.exp(-r1**2/(2*sigma**2))
    wx=amp*torch.exp(-r2**2/(2*sigma**2))
    wy=torch.zeros_like(X)
    wh=(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
    kdotw=s.kx*wh[0]+s.ky*wh[1]+s.kz*wh[2]
    return(wh[0]-s.kx*kdotw/s.ksq,wh[1]-s.ky*kdotw/s.ksq,wh[2]-s.kz*kdotw/s.ksq)

def main():
    N=32;dt=1e-4
    print("="*70,flush=True)
    print("INSTANCE B: ADVERSARIAL IC BATTERY",flush=True)
    print("  Target: push ratio past 1.0. Current worst: trefoil 0.84",flush=True)
    print("="*70,flush=True)

    ics = [
        ("trefoil_s03", lambda s: make_trefoil(s, 10., 0.30)),
        ("trefoil_s015", lambda s: make_trefoil(s, 20., 0.15)),
        ("trefoil_s010", lambda s: make_trefoil(s, 30., 0.10)),
        ("linked_trefoils", lambda s: make_linked_trefoils(s)),
        ("pancake", lambda s: make_pancake(s)),
        ("close_coll_03", lambda s: make_close_collision(s, sep=0.3)),
        ("close_coll_015", lambda s: make_close_collision(s, sep=0.15)),
    ]

    print(f"\n  {'IC':>20s}  {'|ω|₀':>6s}  {'fill':>5s}  "
          f"{'ratio(t=0)':>10s}  {'ratio(evol)':>11s}  {'max_ratio':>10s}  {'broke?':>6s}",flush=True)
    print("-"*80,flush=True)

    worst_ratio = 0
    worst_ic = ""

    for name, make_fn in ics:
        s=NS3D(N,0.)
        try:
            w=make_fn(s)
        except Exception as e:
            print(f"  {name:>20s}  ERROR: {e}",flush=True)
            continue

        # Measure at t=0
        r0=measure_ratio(s,w)
        if r0 is None:
            print(f"  {name:>20s}  no data at t=0",flush=True)
            continue
        om0=r0['om_max']

        # Evolve and measure at multiple times
        ratios=[r0['ratio']]
        t=0.
        for epoch in range(6):
            n_step=300
            try:
                for _ in range(n_step):w=s.step(w,dt);t+=dt
            except:
                break
            r=measure_ratio(s,w)
            if r is not None:
                ratios.append(r['ratio'])

        max_r=max(ratios)
        broke="**YES**" if max_r>=1.0 else "no"

        if max_r>worst_ratio:
            worst_ratio=max_r;worst_ic=name

        print(f"  {name:>20s}  {om0:6.1f}  {r0['fill']:5.3f}  "
              f"{ratios[0]:10.4f}  {ratios[-1]:11.4f}  {max_r:10.4f}  {broke:>6s}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print(f"WORST CASE: {worst_ic} with ratio {worst_ratio:.4f}",flush=True)
    if worst_ratio >= 1.0:
        print(f"*** BOUND BROKEN *** — the isotropy proof route is dead",flush=True)
    else:
        print(f"Bound holds. Margin: {1.0 - worst_ratio:.4f} ({(1-worst_ratio)*100:.1f}%)",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
