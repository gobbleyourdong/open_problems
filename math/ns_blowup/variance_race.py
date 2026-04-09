"""
Instance B: The variance race — does Var/α² drop below 2 over time?

Blowup requires: Var ≥ 2α² (file 273).
Tilting reduces Var (file 173).
If Var/α² → below 2: blowup impossible.

Measure Var = ê·S²·ê - α² and α² at the max point over long times.
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

def measure_variance(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12:return None
    eh=wv/wn;Sl=S[:,:,ix,iy,iz]
    alpha=(eh@Sl@eh).item()
    S2ee=(eh@Sl@Sl@eh).item()
    var=S2ee-alpha**2
    return {'var':var,'alpha':alpha,'alpha2':alpha**2,'ratio':var/(alpha**2+1e-30),
            'om':wn.item(),'blowup_ok':var>=2*alpha**2}

def make_ic(s,name):
    X,Y,Z=s.X,s.Y,s.Z
    if name=='trefoil':
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
    elif name=='thin_trefoil':
        wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
        tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
        cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
        cz=(-torch.sin(3*tp))*0.5+pi
        tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
        ds=2*pi/200
        for i in range(200):
            g=40.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.15**2))*ds
            wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
        return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
    elif name=='TG':
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))

def main():
    N=32;dt=1e-4
    print("="*70,flush=True)
    print("VARIANCE RACE: does Var/α² drop below 2?",flush=True)
    print("  Blowup requires Var ≥ 2α² (file 273)",flush=True)
    print("  If Var/α² < 2: blowup impossible",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','thin_trefoil','TG']:
        s=NS3D(N);w=make_ic(s,ic_name)
        print(f"\n  --- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'Var':>8s}  {'α²':>8s}  {'Var/α²':>8s}  {'|ω|':>6s}  "
              f"{'Var≥2α²':>7s}  {'trend':>8s}",flush=True)

        t=0.; prev_ratio=None
        for epoch in range(25):
            for _ in range(200):w=s.step(w,dt);t+=dt
            m=measure_variance(s,w)
            if m is None or abs(m['alpha'])<1e-6: continue
            ratio=m['ratio']
            trend="↓" if prev_ratio and ratio<prev_ratio else "↑" if prev_ratio and ratio>prev_ratio else " "
            blowup="YES" if m['blowup_ok'] else "NO ✓"
            if epoch%3==0:
                print(f"  {t:6.4f}  {m['var']:8.3f}  {m['alpha2']:8.4f}  "
                      f"{ratio:8.2f}  {m['om']:6.1f}  {blowup:>7s}  {trend:>8s}",flush=True)
            prev_ratio=ratio

    print(f"\n{'='*70}",flush=True)
    print("IF Var/α² drops below 2 and stays there: blowup impossible.",flush=True)
    print("IF Var/α² stays above 2: blowup condition satisfied (but not sufficient).",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
