"""
H_ωω as a function of |ω|: mapping the sign flip precisely.

If H_ωω < 0 at low |ω| and H_ωω > 0 at high |ω|:
→ transport barrier exists
→ particles approaching the max get α reduced

Measure at ALL grid points, binned by |ω|.
Multiple ICs, multiple times.
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

def compute_Hww_field(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
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
    Hww=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):Hww+=wf[i]*H[i,j]*wf[j]
    Hww=Hww/(om_sq+1e-30)
    return om, Hww

def make_ic(s,name):
    X,Y,Z=s.X,s.Y,s.Z
    if name=='TG':
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))
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
    N=32;dt=1e-4
    print("="*70,flush=True)
    print("H_ωω vs |ω|: mapping the sign flip",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)

        print(f"\n--- {ic_name} ---",flush=True)

        for evolve in [500, 2000, 4000]:
            if evolve>500:
                for _ in range(evolve-prev): w=s.step(w,dt)
            else:
                for _ in range(evolve): w=s.step(w,dt)
            prev=evolve
            t=evolve*dt

            om,Hww=compute_Hww_field(s,w)
            om_flat=om.flatten();Hww_flat=Hww.flatten()
            om_max=om_flat.max().item()

            # Bin by |ω|/||ω||∞
            frac=om_flat/om_max
            n_bins=10
            edges=np.linspace(0.05,1.0,n_bins+1)

            print(f"\n  t={t:.3f}, ||ω||∞={om_max:.2f}",flush=True)
            print(f"  {'|ω|/max':>10s}  {'<|ω|>':>7s}  {'<H_ωω>':>8s}  {'H>0%':>6s}  "
                  f"{'med H':>8s}  {'n':>6s}  {'sign':>5s}",flush=True)

            crossover = None
            for i in range(n_bins):
                mask=(frac>=edges[i])&(frac<edges[i+1])&(om_flat>0.1)
                if mask.sum()<10: continue
                h=Hww_flat[mask];o=om_flat[mask]
                mean_h=h.mean().item()
                pct_pos=(h>0).float().mean().item()*100
                sign="+" if mean_h>0 else "-"

                if mean_h > 0 and crossover is None:
                    crossover = edges[i]

                print(f"  [{edges[i]:.2f},{edges[i+1]:.2f})  {o.mean().item():7.2f}  "
                      f"{mean_h:+8.4f}  {pct_pos:5.0f}%  {h.median().item():+8.4f}  "
                      f"{int(mask.sum()):6d}  {sign:>5s}",flush=True)

            if crossover is not None:
                print(f"\n  SIGN FLIP at |ω|/max ≈ {crossover:.2f} "
                      f"(|ω| ≈ {crossover*om_max:.1f})",flush=True)
            else:
                print(f"\n  No sign flip detected (H_ωω same sign throughout)",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
