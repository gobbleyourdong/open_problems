"""
THE KEY INTEGRAL: ∫|ω|²α cos(kz) dz > 0 at the max-|ω| cross-section?

This is the SINGLE condition that would close the entire proof (file 284).
Measure it directly, for all k, at multiple times, for trefoil and TG.
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

def compute_key_integral(s, w):
    """Compute ∫|ω|²α cos(kz) dz at the max-|ω| cross-section."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w);wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()

    # Strain
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))

    # α field
    alpha_f=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):alpha_f+=wf[i]*S[i,j]*wf[j]
    alpha_f=alpha_f/(om_sq+1e-30)

    # Find max-|ω| point
    flat=om.flatten();idx=flat.argmax().item()
    iz0=idx%N;iy0=(idx//N)%N;ix0=idx//(N*N)

    # The product |ω|²α along the z-line at (ix0, iy0)
    product_z = om_sq[ix0,iy0,:] * alpha_f[ix0,iy0,:]  # shape (N,)
    omega_z = om[ix0,iy0,:]

    # Shift so max is at z=0 (circular shift)
    product_z = torch.roll(product_z, -iz0)
    omega_z = torch.roll(omega_z, -iz0)
    alpha_z = torch.roll(alpha_f[ix0,iy0,:], -iz0)

    # z-coordinates
    dz = 2*pi/N
    z_vals = torch.arange(N, dtype=DTYPE) * dz

    # Compute ∫|ω|²α cos(kz) dz for each k
    integrals = {}
    for k in range(1, N//2):
        cos_kz = torch.cos(k * z_vals)
        integral = (product_z * cos_kz).sum().item() * dz
        integrals[k] = integral

    # Also: the source Df/Dt leading term = |ω|²α
    # Its z-cosine components
    source_integrals = {}
    for k in range(1, min(N//2, 8)):
        cos_kz = torch.cos(k * z_vals)
        si = (product_z * cos_kz).sum().item() * dz
        source_integrals[k] = si

    om_max = om[ix0,iy0,iz0].item()
    alpha_max = alpha_f[ix0,iy0,iz0].item()

    return integrals, source_integrals, om_max, alpha_max, product_z.numpy(), omega_z.numpy(), alpha_z.numpy()

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

N=32;dt=1e-4;s=NS3D(N,0.);w=make_trefoil(s)

print("THE KEY INTEGRAL: ∫|ω|²α cos(kz) dz at the max cross-section",flush=True)
print("If positive for some k: dynamic Fourier lemma → DH/Dt > 0 → proof closes\n",flush=True)

for evolve in [300, 500, 1000, 2000, 3000]:
    if evolve > 300:
        for _ in range(evolve - prev): w=s.step(w,dt)
    else:
        for _ in range(evolve): w=s.step(w,dt)
    prev = evolve
    t = evolve*dt

    integrals, src_int, om_max, alpha_max, prod_z, om_z, alpha_z = compute_key_integral(s, w)

    # Check: for which k is the integral positive?
    pos_k = [k for k,v in src_int.items() if v > 0]
    neg_k = [k for k,v in src_int.items() if v < 0]
    total_pos = sum(v for v in src_int.values() if v > 0)
    total_neg = sum(v for v in src_int.values() if v < 0)

    print(f"t={t:.3f}: ||ω||∞={om_max:.2f}, α={alpha_max:+.3f}",flush=True)
    print(f"  k with ∫>0: {pos_k}  k with ∫<0: {neg_k}",flush=True)
    print(f"  Total positive: {total_pos:+.2f}, Total negative: {total_neg:+.2f}",flush=True)
    print(f"  Net (Σ all k): {total_pos+total_neg:+.2f}",flush=True)

    # Show first few k
    print(f"  {'k':>3s}  {'∫|ω|²α cos(kz)':>16s}  {'sign':>5s}",flush=True)
    for k in range(1, min(8, N//2)):
        v = src_int.get(k, 0)
        sign = "+" if v > 0 else "-"
        print(f"  {k:3d}  {v:+16.4f}  {sign:>5s}",flush=True)

    # Also: is α positive along the z-line near the max?
    n_pos = sum(1 for a in alpha_z[:N//4] if a > 0)  # first quarter (near max)
    print(f"  α > 0 near max (first quarter of z-line): {n_pos}/{N//4}",flush=True)
    print(flush=True)

print("DONE.",flush=True)
