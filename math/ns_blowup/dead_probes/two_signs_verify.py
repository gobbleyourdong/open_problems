"""
Verify the TWO-SIGN proof (file 283):
  DVar/Dt < 0 AND DH_ωω/Dt > 0 at the max when α > 0.

If both hold: DQ/Dt = DVar/Dt - DH_ωω/Dt < 0 automatically.
No magnitude comparison needed — just signs!

Measure via finite differences at the max point.
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

def measure_VH(s, w):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
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
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12:return None
    eh=wv/wn;Sl=S[:,:,ix,iy,iz];Hl=H[:,:,ix,iy,iz]
    alpha=(eh@Sl@eh).item()
    S2ee=(eh@Sl@Sl@eh).item()
    Hww=(eh@Hl@eh).item()
    V=S2ee-alpha**2
    return V, Hww, alpha, wn.item()

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
    N=32;dt=1e-4;fd=20
    print("="*70,flush=True)
    print("TWO-SIGN VERIFICATION: DVar/Dt < 0 AND DH/Dt > 0 when α > 0?",flush=True)
    print("="*70,flush=True)

    s=NS3D(N);w=make_trefoil(s)
    for _ in range(200):w=s.step(w,dt)  # skip transient

    t=0.02; total_alpha_pos=0; both_signs=0; dvar_neg=0; dh_pos=0
    print(f"  {'t':>6s}  {'α':>7s}  {'V':>7s}  {'H_ωω':>7s}  {'DV/Dt':>8s}  {'DH/Dt':>8s}  "
          f"{'DV<0':>5s}  {'DH>0':>5s}  {'BOTH':>5s}",flush=True)

    V_prev=None; H_prev=None
    for epoch in range(30):
        r=measure_VH(s,w)
        if r is None:
            for _ in range(fd):w=s.step(w,dt);t+=dt
            continue
        V,Hww,alpha,om=r

        if V_prev is not None and alpha > 0.1:
            dV=(V-V_prev)/(fd*dt)
            dH=(Hww-H_prev)/(fd*dt)
            total_alpha_pos+=1
            dv_ok=dV<0; dh_ok=dH>0; both=dv_ok and dh_ok
            if dv_ok:dvar_neg+=1
            if dh_ok:dh_pos+=1
            if both:both_signs+=1

            if epoch%3==0:
                print(f"  {t:6.4f}  {alpha:+7.3f}  {V:7.3f}  {Hww:+7.3f}  "
                      f"{dV:+8.2f}  {dH:+8.2f}  "
                      f"{'✓' if dv_ok else '✗':>5s}  {'✓' if dh_ok else '✗':>5s}  "
                      f"{'✓✓' if both else '✗':>5s}",flush=True)

        V_prev=V; H_prev=Hww
        for _ in range(fd):w=s.step(w,dt);t+=dt

    print(f"\n  When α > 0 ({total_alpha_pos} measurements):",flush=True)
    print(f"    DVar/Dt < 0: {dvar_neg}/{total_alpha_pos} ({100*dvar_neg/max(total_alpha_pos,1):.0f}%)",flush=True)
    print(f"    DH_ωω/Dt > 0: {dh_pos}/{total_alpha_pos} ({100*dh_pos/max(total_alpha_pos,1):.0f}%)",flush=True)
    print(f"    BOTH signs: {both_signs}/{total_alpha_pos} ({100*both_signs/max(total_alpha_pos,1):.0f}%)",flush=True)

    if both_signs == total_alpha_pos:
        print(f"\n  *** BOTH SIGNS HOLD AT 100% → DQ/Dt < 0 AUTOMATIC ***",flush=True)
    elif both_signs > 0.8*total_alpha_pos:
        print(f"\n  Both signs hold at {100*both_signs/total_alpha_pos:.0f}% — STRONG but not 100%",flush=True)

    print(f"\n{'='*70}",flush=True)

if __name__=='__main__':
    main()
