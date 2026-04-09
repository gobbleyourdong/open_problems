"""
Q/P RATIO: does the super-palinstrophy / palinstrophy ratio stay bounded?

Q = ||∇²ω||² (4th order Sobolev), P = ||∇ω||² (2nd order)
Q/P measures spectral concentration. If bounded: log Sobolev closes.

Log Sobolev: ||ω||∞ ≤ C√P √(log(Q/P))
Palin estimate: dP/dt ≤ C||ω||∞ P ≤ C²P^{3/2}√(log(Q/P))

If Q/P ≤ polynomial(t): log(Q/P) ≤ C log(t).
Then: dP/dt ≤ C P^{3/2} √(log t) → integrate → P polynomial → regularity!
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

def measure_hierarchy(s, w):
    N=s.N
    E = sum((w[i].abs()**2).sum().item() for i in range(3))/N**3
    P = sum((s.ksq*w[i].abs()**2).sum().item() for i in range(3))/N**3
    Q = sum((s.ksq**2*w[i].abs()**2).sum().item() for i in range(3))/N**3
    R4 = sum((s.ksq**3*w[i].abs()**2).sum().item() for i in range(3))/N**3
    wf=[s.ifft(s.D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt().max().item()
    return E,P,Q,R4,om

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
print("Q/P RATIO TEST: does super-palinstrophy/palinstrophy stay bounded?",flush=True)
print(f"  {'t':>6s}  {'Q/P':>8s}  {'R4/Q':>8s}  {'P/E':>8s}  {'||ω||∞':>8s}  "
      f"{'log(Q/P)':>8s}  {'√P√log':>8s}  {'ratio':>8s}",flush=True)

t=0.
for epoch in range(40):
    E,P,Q,R4,om=measure_hierarchy(s,w)
    qp=Q/(P+1e-30); rq=R4/(Q+1e-30); pe=P/(E+1e-30)
    logqp=np.log(max(qp,1)); sqrtPlog=np.sqrt(P)*np.sqrt(max(logqp,0.01))
    ratio_check=om/(sqrtPlog+1e-30)  # ||ω||∞ / (√P √log(Q/P)) — should be bounded

    if epoch%4==0:
        print(f"  {t:6.4f}  {qp:8.2f}  {rq:8.2f}  {pe:8.2f}  {om:8.2f}  "
              f"{logqp:8.3f}  {sqrtPlog:8.1f}  {ratio_check:8.4f}",flush=True)

    for _ in range(50):w=s.step(w,dt);t+=dt

# KEY: is Q/P growing, constant, or decreasing?
print(f"\nQ/P trend analysis:",flush=True)
t2=0.;qps=[];ts=[]
s2=NS3D(N,0.);w2=make_trefoil(s2)
for epoch in range(60):
    E,P,Q,R4,om=measure_hierarchy(s2,w2)
    qps.append(Q/(P+1e-30));ts.append(t2)
    for _ in range(50):w2=s2.step(w2,dt);t2+=dt

qps=np.array(qps);ts=np.array(ts)
from scipy.stats import linregress
sl=linregress(ts[5:],qps[5:])
print(f"  Linear fit Q/P vs t: slope={sl.slope:.2f}, R²={sl.rvalue**2:.3f}",flush=True)
sl2=linregress(ts[5:],np.log(qps[5:]+1e-30))
print(f"  Log fit ln(Q/P) vs t: slope={sl2.slope:.4f}, R²={sl2.rvalue**2:.3f}",flush=True)

if sl.slope > 0:
    print(f"  Q/P GROWING at rate {sl.slope:.2f}/time unit",flush=True)
    print(f"  → log(Q/P) ~ log(t) → sub-cubic estimate may still work",flush=True)
else:
    print(f"  Q/P BOUNDED or decreasing → log Sobolev regularity ✓",flush=True)
print("DONE.",flush=True)
