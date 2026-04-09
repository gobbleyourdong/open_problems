"""
Measure D(Δp)/Dt decomposed into |ω|²α and D|S|²/Dt at the max.
Instance A (V_complete_assessment) showed Step 5 is broken because
D(Δp)/Dt ≠ |ω|²α. The D|S|²/Dt term was dropped.

Measure: what fraction is |ω|²α vs D|S|²/Dt?
If |ω|²α dominates: Step 5 might be salvageable.
If D|S|²/Dt is comparable: Step 5 is truly broken.
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

def measure_source_derivative(s, w):
    """Compute D(Δp)/Dt = D(|ω|²/2)/Dt - D|S|²/Dt at the max by finite diff."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]

    # Source = Δp = |ω|²/2 - |S|²
    u_h=s.vel(*w)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    om=om_sq.sqrt()

    # |S|² field
    S_sq=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Aij=s.ifft(1j*kd[j]*D*u_h[i]);Aji=s.ifft(1j*kd[i]*D*u_h[j])
            Sij=0.5*(Aij+Aji)
            S_sq+=Sij**2

    source = om_sq/2 - S_sq  # Δp

    # α at the max
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    alpha_f=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):alpha_f+=wf[i]*S[i,j]*wf[j]
    alpha_f=alpha_f/(om_sq+1e-30)

    # Find max
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)

    return {
        'om_sq': om_sq[ix,iy,iz].item(),
        'S_sq': S_sq[ix,iy,iz].item(),
        'source': source[ix,iy,iz].item(),
        'alpha': alpha_f[ix,iy,iz].item(),
        'om_max': om[ix,iy,iz].item(),
        'source_field': source,
        'om_sq_alpha': (om_sq * alpha_f),  # |ω|²α field
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

N=32;dt=1e-4;fd=30;s=NS3D(N,0.);w=make_trefoil(s)
for _ in range(500):w=s.step(w,dt)

print("D(Δp)/Dt DECOMPOSITION at the max-|ω| point",flush=True)
print(f"  D(Δp)/Dt = D(|ω|²/2)/Dt - D|S|²/Dt = |ω|²α - D|S|²/Dt\n",flush=True)
print(f"  {'t':>6s}  {'|ω|²α':>8s}  {'D(source)':>10s}  {'D|S|²/Dt':>10s}  "
      f"{'|ω|²α frac':>11s}  {'same sign?':>10s}",flush=True)

t=0.05
for epoch in range(10):
    m1 = measure_source_derivative(s, w)
    w_save=tuple(wi.clone() for wi in w)
    for _ in range(fd):w=s.step(w,dt)
    m2 = measure_source_derivative(s, w)
    t+=fd*dt

    # D(source)/Dt by finite diff
    Dsource = (m2['source'] - m1['source'])/(fd*dt)
    # |ω|²α at the max
    om2_alpha = m1['om_sq'] * m1['alpha']
    # D|S|²/Dt = |ω|²α - D(source)
    DS2 = om2_alpha - Dsource

    frac = om2_alpha / (abs(om2_alpha) + abs(DS2) + 1e-30)
    same = "YES" if (om2_alpha > 0 and Dsource > 0) or (om2_alpha < 0 and Dsource < 0) else "NO"

    print(f"  {t:6.4f}  {om2_alpha:+8.0f}  {Dsource:+10.0f}  {DS2:+10.0f}  "
          f"{frac*100:10.1f}%  {same:>10s}",flush=True)

print(f"\nKEY: if |ω|²α dominates D(source) and has same sign: Step 5 salvageable",flush=True)
print(f"     if D|S|²/Dt is large and opposite sign: Step 5 truly broken",flush=True)
print("DONE.",flush=True)
