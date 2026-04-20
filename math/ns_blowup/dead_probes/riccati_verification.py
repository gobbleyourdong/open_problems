"""
Verify the Riccati bound: dα/dt ≤ -α² + C at high-|ω| points.

Measure dα/dt numerically (finite difference) and compare to -α².
If dα/dt + α² ≤ C for some bounded C, the Riccati mechanism works.

Test on ALL ICs, especially trefoil where α > 0.
"""
import torch, numpy as np, math
DTYPE = torch.float64; pi = math.pi

class NS3D:
    def __init__(s,N=32,nu=0.):
        s.N=N;s.nu=nu;s.Lx=2*pi;dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2;s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def fft(s,f): return torch.fft.fftn(f)
    def ifft(s,f): return torch.fft.ifftn(f).real
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
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)];return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()

def get_alpha_at_max(s, w):
    """Get α = ê·S·ê at the point of max |ω|."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten(); idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return 0.,0.,0.
    eh=wv/wn; Sl=S[:,:,ix,iy,iz]
    alpha=(eh@Sl@eh).item()
    S2ee=(eh@Sl@Sl@eh).item()
    return alpha, S2ee, wn.item()

def make_ic(s,name):
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
        n_pts=200;tp=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
        cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi
        cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
        cz=(-torch.sin(3*tp))*0.5+pi
        tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp)
        tz=-3*torch.cos(3*tp);ds=2*pi/n_pts
        for i in range(n_pts):
            g=10.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
            wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
        return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
    elif name=='rings':
        wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
        for sign in[+1,-1]:
            z0=pi+sign*1.5;rho=((X-pi)**2+(Y-pi)**2).sqrt()
            core=((rho-0.8)**2+(Z-z0)**2).sqrt()
            st=5.*torch.exp(-core**2/(2*0.3**2))
            wx+=sign*st*(-(Y-pi)/(rho+1e-10));wy+=sign*st*((X-pi)/(rho+1e-10))
        return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    N=32;dt=1e-4;dt_fd=50  # 50 steps for finite diff
    print("="*70,flush=True)
    print("RICCATI VERIFICATION: is dα/dt + α² bounded?",flush=True)
    print("="*70,flush=True)
    print(f"\nIf dα/dt + α² ≤ C (bounded), then α ≤ √C (Riccati bound).",flush=True)
    print(f"Measuring at the MAX |ω| point via finite differences.\n",flush=True)

    for ic_name in ['TG','KP','trefoil','rings']:
        s=NS3D(N,0.)
        w=make_ic(s,ic_name)
        print(f"--- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'|ω|':>7s}  {'α':>8s}  {'α²':>8s}  {'dα/dt':>8s}  "
              f"{'dα/dt+α²':>9s}  {'ê·S²·ê':>8s}  {'bounded?':>8s}",flush=True)

        t=0.;alpha_prev=None
        for epoch in range(20):
            alpha,S2ee,om=get_alpha_at_max(s,w)
            if alpha_prev is not None:
                dalpha=(alpha-alpha_prev)/(dt_fd*dt)
                residual=dalpha+alpha**2  # should be ≤ C
                # Also check: dα/dt + ê·S²·ê (should be the pressure+other terms)
                bounded="YES" if abs(residual)<50 else "LARGE"
                print(f"  {t:6.4f}  {om:7.2f}  {alpha:+8.4f}  {alpha**2:8.4f}  "
                      f"{dalpha:+8.4f}  {residual:+9.4f}  {S2ee:8.4f}  {bounded:>8s}",flush=True)
            alpha_prev=alpha
            for _ in range(dt_fd):
                w=s.step(w,dt);t+=dt

    # Summary: what's the max of dα/dt + α² across all ICs?
    print(f"\n{'='*70}",flush=True)
    print("SUMMARY: max(dα/dt + α²) at max-|ω| point",flush=True)
    print(f"{'='*70}",flush=True)
    print(f"\nIf this is bounded, the Riccati mechanism works.",flush=True)
    print(f"The bound C determines the maximum α: α_max = √C.",flush=True)
    print(f"And the maximum |ω| growth: |ω(t)| ≤ |ω(0)|·exp(√C · t).",flush=True)
    print(f"\nFor BKM regularity: exponential growth suffices.\n",flush=True)

    for ic_name in ['TG','KP','trefoil','rings']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        residuals=[];t=0.;ap=None
        for epoch in range(40):
            a,_,_=get_alpha_at_max(s,w)
            if ap is not None: residuals.append((a-ap)/(dt_fd*dt)+a**2)
            ap=a
            for _ in range(dt_fd): w=s.step(w,dt);t+=dt

        res=np.array(residuals)
        print(f"  {ic_name:>8s}: max(dα/dt+α²)={res.max():+.4f}  "
              f"mean={res.mean():+.4f}  min={res.min():+.4f}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
