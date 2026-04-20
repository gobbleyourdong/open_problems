"""
EIGENVECTOR TILTING: the missing term in the Riccati equation.

From file 154: e₃ rotates toward ω (85-90% of dc₃/dt).
This rotation is driven by the strain-rotation commutator AND the pressure.

The full α evolution at a material point:
  Dα/Dt = ê·S²·ê - 2α² - H_ωω  (from strain equation projected onto ω)

But there's ALSO the eigenvector rotation contribution.
The FULL evolution of the stretching rate including eigenvector motion:

  dα_max/dt = [Dα/Dt at material point]
            + [contribution from max-point migration]
            + [contribution from eigenvector tilting]

The eigenvector tilting: as e₃ rotates toward ω, α = Σλᵢcᵢ changes
because the cᵢ change. This is an ADDITIONAL negative contribution
to dα/dt that we haven't accounted for in the Riccati.

Measure: how much does eigenvector tilting contribute to dα/dt?
Is it enough to close the gap?
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

def full_decomposition_at_max(s, w):
    """
    At the max-|ω| point, decompose dα/dt into ALL contributions:
    1. Eigenvalue change: Σ (dλᵢ/dt) cᵢ  (from strain evolution DS/Dt)
    2. Alignment change: Σ λᵢ (dcᵢ/dt)  (from eigenvector tilting)

    α = Σ λᵢ cᵢ  where cᵢ = (ω̂·eᵢ)²
    dα/dt = Σ (dλᵢ/dt)cᵢ + Σ λᵢ(dcᵢ/dt)

    The eigenvalue part: dλᵢ/dt from the strain equation
    The alignment part: dcᵢ/dt from eigenvector + vorticity rotation
    """
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))

    # Pressure Hessian
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)

    # Omega² term
    Omega=0.5*(A-A.transpose(0,1))
    Omega2=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3):Omega2[i,j]+=Omega[i,k]*Omega[k,j]

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)

    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm().item()
    if wn<1e-12: return None
    eh=wv/wv.norm()

    Sl=S[:,:,ix,iy,iz]
    Hl=H[:,:,ix,iy,iz]
    O2l=Omega2[:,:,ix,iy,iz]

    ev,ec=torch.linalg.eigh(Sl)
    # ev[0]=λ₃ (most compressive), ev[2]=λ₁ (most stretching)
    lam=ev.clone()
    c=torch.tensor([(eh@ec[:,j]).item()**2 for j in range(3)],dtype=DTYPE)
    alpha=(lam*c).sum().item()

    # DS/Dt = -S² - Ω² - H (at material point, ignoring advection at max)
    S2=Sl@Sl
    dSdt = -S2 - O2l - Hl

    # Eigenvalue change rate: dλᵢ/dt = eᵢ · (dS/dt) · eᵢ
    dlam=torch.tensor([(ec[:,j]@dSdt@ec[:,j]).item() for j in range(3)],dtype=DTYPE)

    # Contribution to dα from eigenvalue changes: Σ (dλᵢ/dt) cᵢ
    dalpha_eigenval=(dlam*c).sum().item()

    # The alignment change: Σ λᵢ dcᵢ/dt
    # dcᵢ/dt has two parts:
    #   a) ω̂ rotates (Dω̂/Dt = (S-αI)·ω̂)
    #   b) eᵢ rotates (from dS/dt off-diagonal coupling)
    # Total dcᵢ/dt can be computed as dα/dt - dalpha_eigenval
    # But we need dα/dt from finite differences (done separately)

    # Instead: compute the individual terms of dSdt projected
    # Contribution from -S²:
    dalpha_S2 = -(ec[:,0]@S2@ec[:,0]).item()*c[0].item() + \
                -(ec[:,1]@S2@ec[:,1]).item()*c[1].item() + \
                -(ec[:,2]@S2@ec[:,2]).item()*c[2].item()
    # Wait, this is just dalpha_eigenval from -S² part. Let me do it properly.

    # Split dSdt into three terms
    dSdt_S2 = -S2
    dSdt_O2 = -O2l
    dSdt_H = -Hl

    # Each term's contribution to dα via eigenvalue change
    dalpha_from_S2 = sum((ec[:,j]@dSdt_S2@ec[:,j]).item()*c[j].item() for j in range(3))
    dalpha_from_O2 = sum((ec[:,j]@dSdt_O2@ec[:,j]).item()*c[j].item() for j in range(3))
    dalpha_from_H = sum((ec[:,j]@dSdt_H@ec[:,j]).item()*c[j].item() for j in range(3))

    # H_ωω decomposition
    Hww = (eh@Hl@eh).item()

    # The key identity check:
    # Dα/Dt = ê·S²·ê - 2α² - H_ωω  (from theory)
    # = dalpha_eigenval + dalpha_alignment
    # So dalpha_alignment = Dα/Dt - dalpha_eigenval = (ê·S²·ê - 2α² - H_ωω) - dalpha_eigenval

    S2ee = (eh@S2@eh).item()
    Dalpha_theory = S2ee - 2*alpha**2 - Hww  # Dα/Dt from theory
    dalpha_alignment = Dalpha_theory - dalpha_eigenval  # the tilting part

    return {
        'om': wn, 'alpha': alpha,
        'Hww': Hww, 'Hww_norm': Hww/(wn**2),
        'S2ee': S2ee,
        'Dalpha_theory': Dalpha_theory,
        'dalpha_eigenval': dalpha_eigenval,
        'dalpha_alignment': dalpha_alignment,
        'dalpha_from_S2': dalpha_from_S2,
        'dalpha_from_O2': dalpha_from_O2,
        'dalpha_from_H': dalpha_from_H,
        'lam': lam.numpy(),
        'c': c.numpy(),
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
    print("EIGENVECTOR TILTING: the missing Riccati term",flush=True)
    print("="*70,flush=True)
    print("""
  Dα/Dt = (eigenvalue change) + (alignment change/tilting)

  eigenvalue part: Σ (dλᵢ/dt) cᵢ  — from strain evolution
  alignment part:  Σ λᵢ (dcᵢ/dt)  — from eigenvector + ω rotation

  The alignment part is the TILTING TERM that's missing from the ODE.
  If it's consistently NEGATIVE, it helps prevent blowup.
""",flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.)
        if ic_name=='trefoil':
            w=make_trefoil(s)
        else:
            X,Y,Z=s.X,s.Y,s.Z
            ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))

        print(f"\n--- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'|ω|':>6s}  {'α':>7s}  {'Dα(tot)':>8s}  {'eigenval':>8s}  "
              f"{'TILT':>8s}  {'H_ωω':>8s}  {'-S²':>8s}  {'-Ω²':>8s}  {'-H':>8s}",flush=True)

        t=0.
        for epoch in range(15):
            # Evolve
            for _ in range(200 if epoch>0 else 100): w=s.step(w,dt); t+=dt

            m=full_decomposition_at_max(s,w)
            if m is None: continue

            print(f"  {t:6.4f}  {m['om']:6.1f}  {m['alpha']:+7.3f}  "
                  f"{m['Dalpha_theory']:+8.3f}  {m['dalpha_eigenval']:+8.3f}  "
                  f"{m['dalpha_alignment']:+8.3f}  {m['Hww']:+8.3f}  "
                  f"{m['dalpha_from_S2']:+8.3f}  {m['dalpha_from_O2']:+8.3f}  "
                  f"{m['dalpha_from_H']:+8.3f}",flush=True)

        # Summary
        print(f"\n  Key: if TILT is consistently negative, it's the missing term",flush=True)
        print(f"  that prevents blowup beyond the basic Riccati.",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
