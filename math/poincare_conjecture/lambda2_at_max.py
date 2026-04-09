"""
Is λ₂ > 0 at the max of |ω|?

If λ₂ > 0 at the max: the restricted Euler dynamics ALONE push c₂ > 1/3.
The chain: λ₂ > 0 → c₂ increases above 1/3 → V/|ω|² < 1/12 → regularity.

Also measure: what fraction of time is λ₂ > 0 at the max?
And: what's the typical λ₁:λ₂:λ₃ ratio at the max?
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

def measure_at_max(s, w):
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
    ev,ec=torch.linalg.eigh(Sl)
    # ev sorted ascending: λ₃, λ₂, λ₁
    lam3,lam2,lam1=ev[0].item(),ev[1].item(),ev[2].item()
    c1=(eh@ec[:,2]).item()**2
    c2=(eh@ec[:,1]).item()**2
    c3=(eh@ec[:,0]).item()**2
    alpha=lam1*c1+lam2*c2+lam3*c3
    V=(lam1**2*c1+lam2**2*c2+lam3**2*c3)-alpha**2
    return {'lam1':lam1,'lam2':lam2,'lam3':lam3,
            'c1':c1,'c2':c2,'c3':c3,'alpha':alpha,'V':V,
            'om':wn.item(),'V_norm':V/(wn.item()**2+1e-30)}

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
    print("λ₂ AND c₂ AT THE MAX OF |ω|",flush=True)
    print("  Need: c₂ > 1/3 for the proof (file 235)",flush=True)
    print("  If λ₂ > 0: restricted Euler pushes c₂ up",flush=True)
    print("="*70,flush=True)

    total=0;c2_above=0;lam2_pos=0

    for ic_name in ['TG','KP','trefoil']:
        s=NS3D(N);w=make_ic(s,ic_name)
        print(f"\n  --- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'λ₁':>6s}  {'λ₂':>6s}  {'λ₃':>6s}  {'c₁':>5s}  {'c₂':>5s}  {'c₃':>5s}  "
              f"{'V/ω²':>7s}  {'λ₂>0':>5s}  {'c₂>⅓':>5s}",flush=True)

        t=0.
        for epoch in range(25):
            for _ in range(200):w=s.step(w,dt);t+=dt
            m=measure_at_max(s,w)
            if m is None:continue
            total+=1
            if m['c2']>0.333:c2_above+=1
            if m['lam2']>0:lam2_pos+=1
            l2ok="✓" if m['lam2']>0 else "✗"
            c2ok="✓" if m['c2']>0.333 else "✗"
            if epoch%4==0:
                print(f"  {t:6.4f}  {m['lam1']:+6.3f}  {m['lam2']:+6.3f}  {m['lam3']:+6.3f}  "
                      f"{m['c1']:5.3f}  {m['c2']:5.3f}  {m['c3']:5.3f}  "
                      f"{m['V_norm']:7.5f}  {l2ok:>5s}  {c2ok:>5s}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print(f"SUMMARY ({total} measurements):",flush=True)
    print(f"  λ₂ > 0: {lam2_pos}/{total} ({100*lam2_pos/max(total,1):.1f}%)",flush=True)
    print(f"  c₂ > 1/3: {c2_above}/{total} ({100*c2_above/max(total,1):.1f}%)",flush=True)
    print(f"  V/|ω|² < 1/12: check the V_norm column (need < 0.0833)",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
