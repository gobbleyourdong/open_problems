"""
Does the -Ω² term ALONE make Var decrease?

-Ω² = (1/4)(ωω^T - |ω|²I) is EXACT and ALGEBRAIC.
Its contribution to the strain equation DS/Dt involves no pressure.

If the -Ω² contribution to DVar/Dt is ALWAYS NEGATIVE:
then Var decreases from -Ω² alone, regardless of pressure.
Combined with H_ωω > 0 (Fourier lemma): Q = Var - H_ωω eventually < 0.

Compute: the FULL -Ω² contribution (eigenvalue + eigenvector rotation)
to DVar/Dt at the max of |ω|. Is it negative?
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

def omega2_contribution(s, w):
    """
    Compute the -Ω² term's contribution to DVar/Dt at the max of |ω|.

    Method: take the current state. Apply ONLY the -Ω² perturbation to S.
    Compute the resulting change in Var = S²ê - α².
    """
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    Omega=0.5*(A-A.transpose(0,1))

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12:return None
    eh=wv/wn
    Sl=S[:,:,ix,iy,iz]

    # Current Var
    alpha=(eh@Sl@eh).item()
    S2ee=(eh@Sl@Sl@eh).item()
    Var0=S2ee-alpha**2

    # -Ω² contribution to DS/Dt: (1/4)(ωω^T - |ω|²I)
    om_sq=wn.item()**2
    Omega2_contrib=torch.zeros(3,3,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Omega2_contrib[i,j]=(wv[i]*wv[j] - om_sq*(1 if i==j else 0))/4

    # Perturb S by small dt × (-Ω²) and compute new Var
    dt_pert=1e-6
    S_new=Sl+dt_pert*Omega2_contrib
    alpha_new=(eh@S_new@eh).item()
    S2ee_new=(eh@S_new@S_new@eh).item()
    Var_new=S2ee_new-alpha_new**2

    dVar_Omega2=(Var_new-Var0)/dt_pert

    # Also: contributions from -S² and total (for comparison)
    S2_contrib=-(Sl@Sl)  # -S² contribution to DS/Dt
    S_new2=Sl+dt_pert*S2_contrib
    alpha_new2=(eh@S_new2@eh).item()
    Var_new2=(eh@S_new2@S_new2@eh).item()-alpha_new2**2
    dVar_S2=(Var_new2-Var0)/dt_pert

    return {
        'dVar_Omega2':dVar_Omega2, 'dVar_S2':dVar_S2,
        'Var':Var0, 'alpha':alpha, 'om':wn.item(),
        'Omega2_neg': dVar_Omega2 < 0
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
    print("-Ω² CONTRIBUTION TO DVar/Dt: is it always negative?",flush=True)
    print("  -Ω² is ALGEBRAIC (no CZ). If it makes Var decrease: progress!",flush=True)
    print("="*70,flush=True)

    s=NS3D(N);w=make_trefoil(s)

    total=0;neg=0
    print(f"\n  {'t':>6s}  {'α':>7s}  {'Var':>7s}  {'dV(-Ω²)':>10s}  {'dV(-S²)':>10s}  "
          f"{'Ω²<0?':>6s}  {'|ω|':>6s}",flush=True)

    t=0.
    for epoch in range(30):
        for _ in range(200):w=s.step(w,dt);t+=dt
        r=omega2_contribution(s,w)
        if r is None:continue
        if abs(r['alpha'])>0.01:  # only when α is meaningful
            total+=1
            if r['Omega2_neg']:neg+=1
            ok="✓" if r['Omega2_neg'] else "✗"
            if epoch%3==0:
                print(f"  {t:6.4f}  {r['alpha']:+7.3f}  {r['Var']:7.3f}  "
                      f"{r['dVar_Omega2']:+10.2f}  {r['dVar_S2']:+10.2f}  "
                      f"{ok:>6s}  {r['om']:6.1f}",flush=True)

    print(f"\n  -Ω² makes Var decrease: {neg}/{total} ({100*neg/max(total,1):.0f}%)",flush=True)
    if neg==total:
        print(f"  *** -Ω² ALWAYS DECREASES Var! No CZ needed for this part! ***",flush=True)
    elif neg>total*0.8:
        print(f"  -Ω² MOSTLY decreases Var ({100*neg/total:.0f}%). Promising.",flush=True)
    else:
        print(f"  -Ω² doesn't consistently decrease Var. The tilting is more complex.",flush=True)

    print(f"\n{'='*70}",flush=True)

if __name__=='__main__':
    main()
