"""Instance C — Long-time palinstrophy for trefoil. What's the asymptotic growth?"""
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

N=32;dt=1e-4
s=NS3D(N,0.);w=make_trefoil(s)
print("INSTANCE C — Trefoil palinstrophy long evolution",flush=True)
print(f"  {'t':>6s}  {'P':>14s}  {'dP/P':>8s}  {'d(lnP)/dt':>10s}  {'||ω||∞':>8s}  {'P/E':>7s}",flush=True)

t=0.;fd=50;prev_P=None
E_vals=[];P_vals=[];t_vals=[];om_vals=[]
for epoch in range(60):
    E=sum((w[i].abs()**2).sum().item() for i in range(3))/N**3
    P=sum((s.ksq*w[i].abs()**2).sum().item() for i in range(3))/N**3
    wf=[s.ifft(s.D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt().max().item()

    E_vals.append(E);P_vals.append(P);t_vals.append(t);om_vals.append(om)

    if prev_P is not None and P>1e-6:
        dP=(P-prev_P)/(fd*dt)
        dP_P=dP/(P+1e-30)
        dlnP=np.log(P/prev_P)/(fd*dt) if prev_P>0 else 0
        if epoch%5==0:
            print(f"  {t:6.4f}  {P:14.2f}  {dP_P:+8.4f}  {dlnP:+10.6f}  "
                  f"{om:8.2f}  {P/E:7.1f}",flush=True)

    prev_P=P
    for _ in range(fd):w=s.step(w,dt);t+=dt

# Fit d(lnP)/dt = growth rate
t_arr=np.array(t_vals[1:]);P_arr=np.array(P_vals[1:])
lnP=np.log(P_arr)
dlnP=np.gradient(lnP,t_arr)

print(f"\n  d(ln P)/dt over time:",flush=True)
for i in range(0,len(t_arr),len(t_arr)//10):
    print(f"    t={t_arr[i]:.3f}: d(lnP)/dt = {dlnP[i]:+.4f}  P={P_arr[i]:.0f}",flush=True)

# Does dlnP/dt grow with t or P?
# If dlnP/dt ∝ t: P ~ exp(ct²) (Gaussian)
# If dlnP/dt ∝ P: P ~ exp(exp(ct)) (doubly exponential → blowup?)
# If dlnP/dt ∝ const: P ~ exp(ct) (exponential → regularity)
from scipy.stats import linregress
# Fit dlnP/dt vs t
sl_t=linregress(t_arr[5:],dlnP[5:])
# Fit dlnP/dt vs lnP
sl_P=linregress(lnP[5:],dlnP[5:])
print(f"\n  Fit: d(lnP)/dt vs t: slope={sl_t.slope:.4f}, R²={sl_t.rvalue**2:.4f}",flush=True)
print(f"  Fit: d(lnP)/dt vs lnP: slope={sl_P.slope:.4f}, R²={sl_P.rvalue**2:.4f}",flush=True)
if sl_t.rvalue**2 > sl_P.rvalue**2:
    print(f"  → d(lnP)/dt ∝ t (better fit) → P ~ exp(ct²) GAUSSIAN ✓",flush=True)
else:
    print(f"  → d(lnP)/dt ∝ lnP (better fit) → SUPER-EXPONENTIAL ✗",flush=True)
print("DONE.",flush=True)
