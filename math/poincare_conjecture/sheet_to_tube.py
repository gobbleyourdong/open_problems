"""
Instance B: Does a vortex sheet EVOLVE into tubes with R < 1?

Static sheet: R = 2 (breaks the bound).
After Euler evolution: does R drop below 1 as sheets roll up into tubes?

This tests: is the R < 1 property DYNAMIC (created by evolution)?
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

def measure_ratio_at_max(s, w):
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
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12:return None
    eh=wv/wn;Hl=H[:,:,ix,iy,iz]
    trH=Hl.trace().item();hww=(eh@Hl@eh).item()
    hiso=trH/3;hdev=hww-hiso
    R=abs(hdev)/(abs(hiso)+1e-30)
    return R, wn.item(), hww

def main():
    N=32;dt=2e-4
    print("="*70,flush=True)
    print("SHEET → TUBE: does evolution push R from 2 toward < 1?",flush=True)
    print("="*70,flush=True)

    s=NS3D(N)
    X,Y,Z=s.X,s.Y,s.Z

    # Perturbed vortex sheet: ω = ω₀(z) ŷ with sinusoidal perturbation
    # ω_y = A exp(-z²/2σ²) (1 + ε sin(x) sin(y))
    # The perturbation triggers Kelvin-Helmholtz rollup into tubes
    sigma=0.3; A=5.0; eps=0.3
    wy = A * torch.exp(-(Z-pi)**2/(2*sigma**2)) * (1 + eps*torch.sin(X)*torch.sin(Y))
    wx = torch.zeros_like(X)
    wz = torch.zeros_like(X)
    wh = (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))
    # Project div-free
    kdotw = s.kx*wh[0]+s.ky*wh[1]+s.kz*wh[2]
    w = (wh[0]-s.kx*kdotw/s.ksq, wh[1]-s.ky*kdotw/s.ksq, wh[2]-s.kz*kdotw/s.ksq)

    print(f"\n  Perturbed vortex sheet (ε={eps}):",flush=True)
    print(f"  {'t':>6s}  {'R':>6s}  {'|ω|':>7s}  {'H_ωω':>8s}  {'R<1':>4s}",flush=True)

    t=0.
    for epoch in range(20):
        r = measure_ratio_at_max(s, w)
        if r:
            R, om, hww = r
            ok = "✓" if R < 1.0 else "✗"
            print(f"  {t:6.4f}  {R:6.4f}  {om:7.2f}  {hww:+8.3f}  {ok:>4s}",flush=True)
        for _ in range(200): w=s.step(w,dt); t+=dt

    # Also try a pure sheet (no perturbation) — it shouldn't evolve (steady state)
    print(f"\n  Pure vortex sheet (no perturbation):",flush=True)
    wy2 = A * torch.exp(-(Z-pi)**2/(2*sigma**2))
    wh2 = (s.D*s.fft(torch.zeros_like(X)), s.D*s.fft(wy2), s.D*s.fft(torch.zeros_like(X)))
    kdotw2 = s.kx*wh2[0]+s.ky*wh2[1]+s.kz*wh2[2]
    w2 = (wh2[0]-s.kx*kdotw2/s.ksq, wh2[1]-s.ky*kdotw2/s.ksq, wh2[2]-s.kz*kdotw2/s.ksq)

    r = measure_ratio_at_max(s, w2)
    if r:
        R, om, hww = r
        print(f"  t=0: R={R:.4f}  |ω|={om:.2f}  H_ωω={hww:+.3f}  "
              f"{'R<1 ✓' if R<1 else 'R≥1 ✗'}",flush=True)

    # Evolve the pure sheet
    t2=0.
    for epoch in range(10):
        for _ in range(200): w2=s.step(w2,dt); t2+=dt
        r = measure_ratio_at_max(s, w2)
        if r:
            R, om, hww = r
            ok = "✓" if R < 1 else "✗"
            if epoch%3==0:
                print(f"  t={t2:.4f}: R={R:.4f}  |ω|={om:.2f}  H_ωω={hww:+.3f}  {ok}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("IF perturbed sheet: R starts high, drops to < 1 as tubes form",flush=True)
    print("IF pure sheet: R stays high (no instability to create tubes)",flush=True)
    print("This shows R < 1 is DYNAMIC, created by nonlinear evolution",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
