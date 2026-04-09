"""
WHY is α bounded at ~3 even when H_ωω < 0?

At points with the LARGEST α: is Dα/Dt negative?
Dα/Dt = ê·S²·ê - 2α² - H_ωω

If 2α² > ê·S²·ê + |H_ωω| when α > threshold: α is self-bounding.
The -2α² term grows quadratically and eventually dominates everything.

Test at the HIGH-ALPHA points specifically.
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

def analyze_high_alpha(s, w, alpha_threshold=1.0):
    """At points with α > threshold, measure Dα/Dt components."""
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
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()

    # Compute fields
    alpha_f=torch.zeros(N,N,N,dtype=DTYPE)
    S2ee_f=torch.zeros(N,N,N,dtype=DTYPE)
    Hww_f=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            alpha_f+=wf[i]*S[i,j]*wf[j]
            Hww_f+=wf[i]*H[i,j]*wf[j]
            for k in range(3):
                S2ee_f+=wf[i]*(S[i,k]*S[k,j])*wf[j]/(om_sq+1e-30)  # wrong, need to fix
    # Redo S2ee properly
    S2ee_f=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        Si_w=torch.zeros(N,N,N,dtype=DTYPE)
        for j in range(3): Si_w+=S[i,j]*wf[j]
        S2ee_f+=Si_w**2
    S2ee_f=S2ee_f/(om_sq+1e-30)

    alpha_f=alpha_f/(om_sq+1e-30)
    Hww_f=Hww_f/(om_sq+1e-30)

    Dalpha_f=S2ee_f-2*alpha_f**2-Hww_f

    # Select high-α points
    mask=(alpha_f>alpha_threshold)&(om>1.0)
    if mask.sum()<5: return None

    a=alpha_f[mask].numpy()
    Da=Dalpha_f[mask].numpy()
    S2=S2ee_f[mask].numpy()
    Hw=Hww_f[mask].numpy()
    o=om[mask].numpy()

    return {
        'alpha':a,'Dalpha':Da,'S2ee':S2,'Hww':Hw,'om':o,
        'n':len(a)
    }

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
    print("WHY IS α BOUNDED? Analysis at high-α points",flush=True)
    print("="*70,flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)

    for alpha_thr in [0.5, 1.0, 1.5, 2.0, 2.5]:
        print(f"\n--- α > {alpha_thr} points over time ---",flush=True)
        print(f"  {'t':>5s}  {'n':>5s}  {'<α>':>6s}  {'max α':>6s}  "
              f"{'<Dα>':>7s}  {'Dα<0%':>6s}  {'<S²ê>':>7s}  {'<2α²>':>7s}  "
              f"{'<H_ωω>':>7s}  {'margin':>7s}",flush=True)

        w2=make_trefoil(s)  # fresh
        t=0.
        for epoch in range(12):
            for _ in range(300): w2=s.step(w2,dt); t+=dt
            d=analyze_high_alpha(s,w2,alpha_thr)
            if d is None:
                print(f"  {t:5.3f}  <{alpha_thr} no points",flush=True)
                continue

            margin = 2*np.mean(d['alpha']**2) - np.mean(d['S2ee']) - np.abs(np.mean(d['Hww']))
            print(f"  {t:5.3f}  {d['n']:5d}  {d['alpha'].mean():+6.3f}  "
                  f"{d['alpha'].max():+6.3f}  {d['Dalpha'].mean():+7.2f}  "
                  f"{(d['Dalpha']<0).mean()*100:5.1f}%  "
                  f"{d['S2ee'].mean():7.3f}  {2*np.mean(d['alpha']**2):7.3f}  "
                  f"{d['Hww'].mean():+7.3f}  {margin:+7.3f}",flush=True)

    # THE KEY TEST: at α > 2.5 (the danger zone), is Dα/Dt ALWAYS negative?
    print(f"\n\n{'='*70}",flush=True)
    print("THE KEY: at α > 2.5, is Dα/Dt ALWAYS negative?",flush=True)
    print(f"{'='*70}",flush=True)

    w3=make_trefoil(s)
    all_Da_at_high=[]
    t=0.
    for epoch in range(20):
        for _ in range(200): w3=s.step(w3,dt); t+=dt
        d=analyze_high_alpha(s,w3,2.5)
        if d is not None:
            all_Da_at_high.extend(d['Dalpha'].tolist())
            frac_neg=(d['Dalpha']<0).mean()*100
            print(f"  t={t:.3f}: {d['n']} pts with α>2.5, Dα/Dt<0: {frac_neg:.0f}%  "
                  f"mean Dα={d['Dalpha'].mean():+.2f}  max Dα={d['Dalpha'].max():+.2f}",flush=True)

    if all_Da_at_high:
        arr=np.array(all_Da_at_high)
        print(f"\n  ACROSS ALL TIMES ({len(arr)} total high-α samples):",flush=True)
        print(f"    Dα/Dt < 0: {(arr<0).mean()*100:.1f}%",flush=True)
        print(f"    mean Dα/Dt: {arr.mean():+.3f}",flush=True)
        print(f"    max Dα/Dt: {arr.max():+.3f}",flush=True)
        if (arr<0).mean()>0.95:
            print(f"    → α > 2.5 is SELF-CORRECTING ✓ (Dα/Dt < 0 at {(arr<0).mean()*100:.0f}%)",flush=True)
        elif arr.mean()<0:
            print(f"    → α > 2.5 is MEAN-REVERTING (Dα/Dt < 0 on average)",flush=True)
        else:
            print(f"    → α > 2.5 is NOT self-correcting ✗",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
