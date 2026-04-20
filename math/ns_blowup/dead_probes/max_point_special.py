"""
Is the Fourier cancellation SPECIFIC to the max-|ω| point?

Hypothesis: the constraint ∇|ω|² = 0 at the max forces the phases
of the Fourier shells to cancel, making H_ωω small there.

Test: compare |H_ωω| at:
1. The max-|ω| point (where ∇|ω|²=0)
2. Other high-|ω| points (where ∇|ω|²≠0)
3. Random points

If |H_ωω| is systematically SMALLER at the max → gradient constraint is key.
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

def compute_Hww_and_grad(s, w):
    """Compute H_ωω AND |∇|ω|²| at every grid point."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
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

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    om=om_sq.sqrt()

    # H_ωω at every point
    Hww=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Hww+=wf[i]*H[i,j]*wf[j]
    Hww=Hww/(om_sq+1e-30)

    # |∇|ω|²| at every point
    om_sq_h=s.fft(om_sq)
    grad_om_sq=torch.zeros(N,N,N,dtype=DTYPE)
    for j in range(3):
        g=s.ifft(1j*kd[j]*D*om_sq_h)
        grad_om_sq+=g**2
    grad_om_sq=grad_om_sq.sqrt()

    # Normalize: |∇|ω|²| / |ω|² (dimensionless gradient)
    grad_norm=grad_om_sq/(om_sq+1e-30)

    return om, Hww, grad_norm

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
    print("MAX-POINT SPECIAL: is H_ωω small specifically at the max?",flush=True)
    print("="*70,flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)
    for _ in range(500): w=s.step(w,dt)

    om,Hww,grad_norm=compute_Hww_and_grad(s,w)
    om_flat=om.flatten();Hww_flat=Hww.flatten();grad_flat=grad_norm.flatten()

    # Bin by |ω| AND by gradient magnitude
    thr=torch.quantile(om_flat,0.90).item()
    mask_hi=om_flat>thr

    # At the max: grad should be ~0
    # At other high-|ω|: grad > 0

    om_hi=om_flat[mask_hi];Hww_hi=Hww_flat[mask_hi];grad_hi=grad_flat[mask_hi]

    # Bin by gradient
    n_bins=5
    pcts=np.linspace(0,100,n_bins+1)
    edges=np.percentile(grad_hi.numpy(),pcts)

    print(f"\n  High-|ω| points (top 10%), binned by |∇|ω|²|/|ω|²:",flush=True)
    print(f"  {'grad range':>20s}  {'mean grad':>10s}  {'mean |H_ww|':>12s}  "
          f"{'mean H_ww':>10s}  {'mean |ω|':>8s}  {'n':>5s}",flush=True)

    for i in range(n_bins):
        m=(grad_hi>=edges[i])&(grad_hi<edges[i+1]+1e-10)
        if m.sum()<5: continue
        print(f"  [{edges[i]:8.3f},{edges[i+1]:8.3f})  "
              f"{grad_hi[m].mean().item():10.4f}  "
              f"{Hww_hi[m].abs().mean().item():12.4f}  "
              f"{Hww_hi[m].mean().item():+10.4f}  "
              f"{om_hi[m].mean().item():8.2f}  "
              f"{int(m.sum()):5d}",flush=True)

    # The MAX point specifically
    max_idx=om_flat.argmax()
    print(f"\n  AT THE MAX POINT:",flush=True)
    print(f"    |ω| = {om_flat[max_idx].item():.2f}",flush=True)
    print(f"    H_ωω = {Hww_flat[max_idx].item():+.6f}",flush=True)
    print(f"    |∇|ω|²|/|ω|² = {grad_flat[max_idx].item():.6f}",flush=True)
    print(f"    |H_ωω| = {abs(Hww_flat[max_idx].item()):.6f}",flush=True)

    # Compare: |H_ωω| at the max vs at the MEDIAN high-|ω| point
    median_Hww = Hww_hi.abs().median().item()
    max_Hww = abs(Hww_flat[max_idx].item())
    print(f"\n  |H_ωω| at max point: {max_Hww:.4f}",flush=True)
    print(f"  |H_ωω| median of top 10%: {median_Hww:.4f}",flush=True)
    print(f"  Ratio: {max_Hww/median_Hww:.3f}",flush=True)

    if max_Hww < median_Hww:
        print(f"  MAX POINT HAS SMALLER |H_ωω| ← gradient constraint helps ✓",flush=True)
    else:
        print(f"  MAX POINT HAS LARGER |H_ωω| ← gradient constraint doesn't help ✗",flush=True)

    # CORRELATION: |H_ωω| vs gradient at high-|ω| points
    corr=np.corrcoef(Hww_hi.abs().numpy(), grad_hi.numpy())[0,1]
    print(f"\n  Correlation(|H_ωω|, grad) at high |ω|: {corr:+.4f}",flush=True)
    if corr > 0.3:
        print(f"  POSITIVE correlation: small grad → small |H_ωω| ✓",flush=True)
    elif corr < -0.3:
        print(f"  NEGATIVE: small grad → LARGE |H_ωω| ✗",flush=True)
    else:
        print(f"  WEAK correlation: grad doesn't strongly predict |H_ωω|",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
