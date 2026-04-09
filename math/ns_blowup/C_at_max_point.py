"""
DEFINITIVE TEST: C at the SINGLE max-|ω| point.

BKM only cares about ||ω||_∞. So only C at the max-|ω| point matters.
The outlier C>0.25 at other top-1% points are irrelevant for BKM.

Measure C = R/|ω|² at the max-|ω| point via finite differences.
Cross-validate N=32 vs N=48. Multiple ICs. Many timesteps.
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

def alpha_at_max(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return 0.,0.,0.
    eh=wv/wn;Sl=S[:,:,ix,iy,iz]
    return (eh@Sl@eh).item(), (eh@Sl@Sl@eh).item(), wn.item()

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
    print("="*70,flush=True)
    print("C AT THE SINGLE MAX-|ω| POINT (the only point BKM cares about)",flush=True)
    print("="*70,flush=True)

    n_fd = 20  # steps for finite difference

    for ic_name in ['trefoil','TG','KP']:
        for N_test in [32, 48]:
            dt = 1e-4 if N_test==32 else 5e-5
            s=NS3D(N_test,0.);w=make_ic(s,ic_name)

            print(f"\n--- {ic_name} N={N_test} ---",flush=True)
            print(f"  {'t':>6s}  {'|ω|':>7s}  {'α':>8s}  {'S²ê':>8s}  "
                  f"{'dα/dt':>8s}  {'R':>8s}  {'C=R/ω²':>8s}  {'C<¼?':>5s}",flush=True)

            t=0.;a_prev=None;C_all=[]

            # Skip initial transient
            for _ in range(100): w=s.step(w,dt); t+=dt

            for epoch in range(30):
                alpha,S2ee,om=alpha_at_max(s,w)

                if a_prev is not None:
                    dalpha=(alpha-a_prev)/(n_fd*dt)
                    R=dalpha+S2ee  # residual after self-depletion
                    C=R/(om**2+1e-30)
                    C_all.append(C)
                    safe="YES" if C<0.25 else "**NO**"
                    print(f"  {t:6.4f}  {om:7.2f}  {alpha:+8.4f}  {S2ee:8.4f}  "
                          f"{dalpha:+8.2f}  {R:+8.4f}  {C:+8.5f}  {safe:>5s}",flush=True)

                a_prev=alpha
                for _ in range(n_fd): w=s.step(w,dt); t+=dt

            if C_all:
                C_arr=np.array(C_all)
                print(f"\n  SUMMARY (N={N_test}):",flush=True)
                print(f"    C mean:   {C_arr.mean():+.5f}",flush=True)
                print(f"    C median: {np.median(C_arr):+.5f}",flush=True)
                print(f"    C max:    {C_arr.max():+.5f}",flush=True)
                print(f"    C min:    {C_arr.min():+.5f}",flush=True)
                print(f"    C < 0.25: {(C_arr<0.25).sum()}/{len(C_arr)} "
                      f"({100*(C_arr<0.25).mean():.0f}%)",flush=True)
                print(f"    VERDICT:  {'SAFE — C < 1/4 at max point' if C_arr.max()<0.25 else 'VIOLATIONS EXIST'}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
