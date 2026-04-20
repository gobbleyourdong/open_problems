"""
Measure D²α/Dt² vs 2α³ at the max-|ω| point.

From Instance A (files 192, 194): the proof reduces to Q < 0 at the max.
Q = Dα/Dt + α². DQ/Dt < 0 when Q > 0 ⟺ D²α/Dt² < 2α³ - 2αQ.
At the boundary Q = 0: need D²α/Dt² < 2α³.

Measure by triple finite differences: α(t), α(t+h), α(t+2h).
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
    if wn<1e-12:return 0.,0.
    eh=wv/wn;Sl=S[:,:,ix,iy,iz]
    return (eh@Sl@eh).item(), wn.item()

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

N=32;dt=1e-4;h_fd=10  # steps between samples for finite diff
s=NS3D(N,0.);w=make_trefoil(s)
# Skip transient
for _ in range(300):w=s.step(w,dt)

print("D²α/Dt² vs 2α³ at max-|ω| point (trefoil, Euler)",flush=True)
print(f"  {'t':>6s}  {'α':>7s}  {'Dα/Dt':>8s}  {'D²α/Dt²':>9s}  {'2α³':>8s}  "
      f"{'Q=Dα+α²':>8s}  {'DQ/Dt':>8s}  {'D²α<2α³':>8s}  {'DQ<0 if Q>0':>11s}",flush=True)

t=0.03;alphas=[];
# Collect dense α time series
for step_i in range(80):
    a,om=alpha_at_max(s,w)
    alphas.append(a)
    for _ in range(h_fd):w=s.step(w,dt)

dt_fd=h_fd*dt
alphas=np.array(alphas)
# First derivative
Da=np.gradient(alphas, dt_fd)
# Second derivative
D2a=np.gradient(Da, dt_fd)
# Q = Dα/Dt + α²
Q=Da+alphas**2

for i in range(2, len(alphas)-2):
    t_i=t+i*dt_fd
    a=alphas[i]; da=Da[i]; d2a=D2a[i]; q=Q[i]
    two_a3=2*a**3
    dq=D2a[i]+2*a*Da[i]  # DQ/Dt = D²α + 2αDα
    d2_ok="YES ✓" if d2a<two_a3 else "NO ✗"
    dq_ok="YES ✓" if (q<=0 or dq<0) else "NO ✗"

    if i%8==0:
        print(f"  {t_i:6.4f}  {a:+7.3f}  {da:+8.2f}  {d2a:+9.2f}  {two_a3:+8.2f}  "
              f"{q:+8.2f}  {dq:+8.2f}  {d2_ok:>8s}  {dq_ok:>11s}",flush=True)

# Summary
mask_alpha_pos=alphas[2:-2]>0.1
if mask_alpha_pos.sum()>0:
    d2_at_pos=D2a[2:-2][mask_alpha_pos]
    a_at_pos=alphas[2:-2][mask_alpha_pos]
    two_a3_at_pos=2*a_at_pos**3
    frac=np.mean(d2_at_pos<two_a3_at_pos)
    print(f"\n  At α > 0.1: D²α < 2α³ holds {frac*100:.1f}% of the time",flush=True)
    print(f"  Mean D²α = {d2_at_pos.mean():+.2f}, Mean 2α³ = {two_a3_at_pos.mean():+.2f}",flush=True)
    print(f"  Margin: 2α³ - D²α = {(two_a3_at_pos-d2_at_pos).mean():+.2f}",flush=True)

Q_pos=Q[2:-2]>0
DQ_at_Qpos=(D2a[2:-2]+2*alphas[2:-2]*Da[2:-2])[Q_pos]
if Q_pos.sum()>0:
    print(f"\n  When Q > 0: DQ/Dt < 0 holds {(DQ_at_Qpos<0).mean()*100:.1f}%",flush=True)
    print(f"  → Q attractor confirmed: {(DQ_at_Qpos<0).mean()*100:.0f}% compliance",flush=True)

print("\nDONE.",flush=True)
