"""
DEFINITIVE H_ωω measurement at the max-|ω| point.

H_ωω = ê · H · ê  where H_ij = ∂²p/∂x_i∂x_j (pressure Hessian)
ê = ω/|ω| (vorticity direction)

From Poisson: Δp = |ω|²/2 - |S|² (exact for incompressible Euler)

Key numbers:
  H_ωω itself (raw)
  H_ωω / |ω|² (normalized — the C coefficient)
  Compare to self-depletion α² and ê·S²·ê

All ICs. Both resolutions. Multiple times. Dense sampling.
"""
import torch, numpy as np, math, time
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

def measure_Hww(s, w):
    """Complete measurement at the max-|ω| point."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))

    # Source and pressure
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0

    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)

    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm().item()
    if wn<1e-12: return None
    eh=wv/wv.norm()

    Sl=S[:,:,ix,iy,iz]; Hl=H[:,:,ix,iy,iz]
    alpha=(eh@Sl@eh).item()
    S2ee=(eh@Sl@Sl@eh).item()
    Hww=(eh@Hl@eh).item()
    Snorm=(Sl*Sl).sum().item()

    return {
        'om': wn,
        'alpha': alpha,
        'S2ee': S2ee,
        'Hww': Hww,
        'Hww_norm': Hww/(wn**2+1e-30),  # H_ωω / |ω|²
        'Snorm': Snorm,
        'ratio_om_S': wn**2/(Snorm+1e-30),
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
    dt=1e-4
    print("="*70,flush=True)
    print("H_ωω DEFINITIVE: at the max-|ω| point, all ICs, all times",flush=True)
    print("="*70,flush=True)
    print(f"\n  H_ωω > 0: pressure STRETCHES along ω (fights compression)",flush=True)
    print(f"  H_ωω < 0: pressure COMPRESSES along ω (helps)\n",flush=True)

    for N_test in [32, 48]:
        dt_use = dt if N_test==32 else 5e-5
        print(f"\n{'='*70}",flush=True)
        print(f"  N = {N_test}",flush=True)
        print(f"{'='*70}",flush=True)

        for ic_name in ['TG','KP','trefoil']:
            s=NS3D(N_test,0.);w=make_ic(s,ic_name)

            print(f"\n  --- {ic_name} ---",flush=True)
            print(f"  {'t':>6s}  {'|ω|':>7s}  {'H_ωω':>10s}  {'H/|ω|²':>9s}  "
                  f"{'α':>8s}  {'α²':>8s}  {'ê·S²·ê':>8s}  {'|ω|²/|S|²':>9s}",flush=True)

            t=0.; Hww_list=[]
            n_steps = 400 if N_test==32 else 300
            n_epochs = 15

            for epoch in range(n_epochs):
                m=measure_Hww(s,w)
                if m is None: continue
                Hww_list.append(m['Hww_norm'])

                print(f"  {t:6.4f}  {m['om']:7.2f}  {m['Hww']:+10.4f}  "
                      f"{m['Hww_norm']:+9.5f}  {m['alpha']:+8.4f}  "
                      f"{m['alpha']**2:8.4f}  {m['S2ee']:8.4f}  "
                      f"{m['ratio_om_S']:9.2f}",flush=True)

                for _ in range(n_steps): w=s.step(w,dt_use); t+=dt_use

            if Hww_list:
                ha=np.array(Hww_list)
                print(f"\n  H_ωω/|ω|² summary:",flush=True)
                print(f"    mean = {ha.mean():+.6f}",flush=True)
                print(f"    |mean| = {abs(ha.mean()):.6f}",flush=True)
                print(f"    std = {ha.std():.6f}",flush=True)
                print(f"    max = {ha.max():+.6f}",flush=True)
                print(f"    min = {ha.min():+.6f}",flush=True)
                print(f"    threshold 1/4 = 0.250000",flush=True)
                print(f"    |H/ω²| < 1/4: {'YES ✓' if abs(ha).max()<0.25 else 'NO'}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("WHAT H_ωω IS:",flush=True)
    print("""
  H_ωω = ê · (∂²p/∂x_i∂x_j) · ê

  The second derivative of PRESSURE in the VORTICITY direction.

  Pressure solves: Δp = |ω|²/2 - |S|²  (Poisson equation)

  H_ωω enters the stretching rate evolution:
    Dα/Dt = ê·S²·ê - 2α² - H_ωω  (at a material point)

  For regularity: need H_ωω to not overwhelm the self-depletion α².
  The ratio H_ωω/|ω|² is the normalized coefficient.
  If |H_ωω/|ω|²| < 1/4: the self-depletion wins (from our analysis).
""",flush=True)

if __name__=='__main__':
    main()
