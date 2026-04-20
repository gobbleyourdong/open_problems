"""
ALGEBRAIC tilting formula: dcᵢ/dt = (|ω|²/2) cᵢ Σⱼ≠ᵢ cⱼ/(λᵢ-λⱼ)

This is the -Ω² eigenvector rotation contribution. EXACT. NO PRESSURE.

Compute dVar/dt from this formula at the max of |ω|.
Also: check if the -S² and -H tilting contributions change the sign.
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

def algebraic_analysis(s, w):
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
    wn=wv.norm().item();om_sq=wn**2
    if wn<1e-12:return None
    eh=wv/wv.norm()
    Sl=S[:,:,ix,iy,iz]
    ev,ec=torch.linalg.eigh(Sl)
    lam=ev.numpy()  # λ₃, λ₂, λ₁ (ascending)
    c=np.array([(eh@ec[:,j]).item()**2 for j in range(3)])
    alpha=sum(lam[j]*c[j] for j in range(3))

    # The algebraic tilting formula: dcᵢ/dt = (|ω|²/2) cᵢ Σⱼ≠ᵢ cⱼ/(λᵢ-λⱼ)
    dc = np.zeros(3)
    for i in range(3):
        for j in range(3):
            if i==j: continue
            gap = lam[i]-lam[j]
            if abs(gap) < 1e-10: continue
            dc[i] += c[j]/(gap)
        dc[i] *= om_sq/2 * c[i]

    # dVar/dt from tilting: Σ(λᵢ² - 2αλᵢ) dcᵢ
    dVar_tilt = sum((lam[i]**2 - 2*alpha*lam[i]) * dc[i] for i in range(3))

    # For comparison: the vorticity rotation contribution
    # Dω̂/Dt = (S-αI)·ω̂. This gives dcᵢ/dt = 2cᵢ(λᵢ-α) (restricted Euler part)
    dc_re = np.array([2*c[i]*(lam[i]-alpha) for i in range(3)])
    dVar_re = sum((lam[i]**2 - 2*alpha*lam[i]) * dc_re[i] for i in range(3))

    Var = sum(lam[i]**2*c[i] for i in range(3)) - alpha**2

    return {
        'lam': lam, 'c': c, 'alpha': alpha, 'Var': Var, 'om': wn,
        'dc_tilt': dc, 'dc_re': dc_re,
        'dVar_tilt': dVar_tilt, 'dVar_re': dVar_re,
        'dVar_total_approx': dVar_tilt + dVar_re,
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
    print("ALGEBRAIC TILTING: exact formula for dcᵢ/dt from -Ω²",flush=True)
    print("  dcᵢ/dt = (|ω|²/2) cᵢ Σⱼ≠ᵢ cⱼ/(λᵢ-λⱼ)",flush=True)
    print("="*70,flush=True)

    s=NS3D(N);w=make_trefoil(s)
    print(f"\n  {'t':>6s}  {'λ₁':>6s}  {'λ₂':>6s}  {'λ₃':>6s}  {'c₁':>5s}  {'c₂':>5s}  "
          f"{'Var':>6s}  {'dV(tilt)':>9s}  {'dV(RE)':>9s}  {'dV(sum)':>9s}  {'sum<0':>5s}",flush=True)

    t=0.; neg_count=0; total=0
    for epoch in range(25):
        for _ in range(200):w=s.step(w,dt);t+=dt
        r=algebraic_analysis(s,w)
        if r is None or abs(r['alpha'])<0.01:continue
        total+=1
        neg = r['dVar_total_approx'] < 0
        if neg: neg_count+=1

        if epoch%3==0:
            print(f"  {t:6.4f}  {r['lam'][2]:+6.3f}  {r['lam'][1]:+6.3f}  {r['lam'][0]:+6.3f}  "
                  f"{r['c'][2]:5.3f}  {r['c'][1]:5.3f}  {r['Var']:6.3f}  "
                  f"{r['dVar_tilt']:+9.2f}  {r['dVar_re']:+9.2f}  "
                  f"{r['dVar_total_approx']:+9.2f}  {'✓' if neg else '✗':>5s}",flush=True)

    print(f"\n  dV(tilt+RE) < 0: {neg_count}/{total} ({100*neg_count/max(total,1):.0f}%)",flush=True)
    print(f"\n  NOTE: This is only -Ω² and restricted Euler (no -S², no -H).",flush=True)
    print(f"  The -H (pressure) contribution is the MISSING part.",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
