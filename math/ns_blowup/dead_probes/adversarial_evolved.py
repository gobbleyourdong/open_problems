"""
Instance B round 2: Does the ratio GROW during evolution?

The t=0 ratio for thin trefoil is 0.955. But the original trefoil's
ratio was measured at 0.82 AFTER evolution (files 178). Maybe the
thin trefoil's ratio gets WORSE during evolution.

Also try: torus knots T(2,5) — more crossings = more strain interaction.
"""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N,nu=0.):
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
    hiso_list=[];hdev_list=[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12:continue
        eh=wv/wn;Hl=H[:,:,ix,iy,iz]
        trH=Hl.trace().item();hww=(eh@Hl@eh).item()
        hiso_list.append(trH/3);hdev_list.append(hww-trH/3)
    if not hiso_list:return None
    hi=np.abs(np.array(hiso_list)).mean();hd=np.abs(np.array(hdev_list)).mean()
    return hd/(hi+1e-30), om_max

def make_torus_knot(s, p_knot=2, q_knot=5, amp=15., sigma=0.2, R=0.7):
    """Torus knot T(p,q) — winds p times around torus hole, q times around tube."""
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    n_pts=300
    tp=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
    r_minor=0.35
    # Parametric torus knot
    cx=(R+r_minor*torch.cos(q_knot*tp))*torch.cos(p_knot*tp)+pi
    cy=(R+r_minor*torch.cos(q_knot*tp))*torch.sin(p_knot*tp)+pi
    cz=r_minor*torch.sin(q_knot*tp)+pi
    # Tangent
    dcx=torch.gradient(cx,spacing=(tp[1]-tp[0],))[0]
    dcy=torch.gradient(cy,spacing=(tp[1]-tp[0],))[0]
    dcz=torch.gradient(cz,spacing=(tp[1]-tp[0],))[0]
    ds_val=(dcx**2+dcy**2+dcz**2).sqrt()
    tx=dcx/ds_val;ty=dcy/ds_val;tz=dcz/ds_val
    ds=2*pi/n_pts
    for i in range(n_pts):
        g=amp*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*sigma**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

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

def main():
    N=48; dt=5e-5
    print("="*70,flush=True)
    print("INSTANCE B ROUND 2: evolved ratio + torus knots (N=48)",flush=True)
    print("="*70,flush=True)

    # TEST 1: Thin trefoil evolved over time at N=48
    print("\n--- Thin trefoil σ=0.15, N=48: ratio over time ---",flush=True)
    s=NS3D(N);w=make_trefoil(s, amp=40., sigma=0.15)
    t=0.
    print(f"  {'t':>6s}  {'ratio':>6s}  {'|ω|':>7s}",flush=True)
    for epoch in range(10):
        r=measure_ratio(s,w)
        if r:
            ratio,om=r
            print(f"  {t:6.4f}  {ratio:6.4f}  {om:7.1f}",flush=True)
        for _ in range(400):w=s.step(w,dt);t+=dt

    # TEST 2: Torus knots with more crossings
    print(f"\n--- Torus knots at N=48 (t=0, various topologies) ---",flush=True)
    for p,q in [(2,3),(2,5),(2,7),(3,4),(3,5)]:
        s=NS3D(N)
        try:
            w=make_torus_knot(s,p,q,amp=15.,sigma=0.2)
            r=measure_ratio(s,w)
            if r:
                ratio,om=r
                print(f"  T({p},{q}): ratio={ratio:.4f}  |ω|={om:.1f}",flush=True)
        except Exception as e:
            print(f"  T({p},{q}): error {e}",flush=True)

    # TEST 3: Torus knots EVOLVED
    print(f"\n--- Best torus knot evolved ---",flush=True)
    s=NS3D(N);w=make_torus_knot(s,2,5,amp=15.,sigma=0.15)
    t=0.
    max_ratio=0
    for epoch in range(8):
        r=measure_ratio(s,w)
        if r:
            ratio,om=r
            max_ratio=max(max_ratio,ratio)
            if epoch%2==0:
                print(f"  t={t:.4f}: ratio={ratio:.4f}  |ω|={om:.1f}",flush=True)
        for _ in range(400):w=s.step(w,dt);t+=dt
    print(f"  Max ratio during evolution: {max_ratio:.4f}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("SUMMARY: can we break 1.0 with evolved dynamics or complex topology?",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
