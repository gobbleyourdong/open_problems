"""
CRITICAL TEST: Is the Lagrangian Dα/Dt < 0 at EVERY point where α > 0?

If YES: every material particle's α decreases when positive.
→ α is bounded along every trajectory
→ ||ω||∞ grows at most exponentially
→ BKM → REGULARITY

The Lagrangian formula: Dα/Dt = ê·S²·ê - 2α² - H_ωω

Measure this at ALL high-|ω| points (not just the max).
Check: is Dα/Dt < 0 whenever α > 0?
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

def compute_lagrangian_Dalpha(s, w, n_sample=3000):
    """
    Compute Dα/Dt = ê·S²·ê - 2α² - H_ωω at many grid points.
    Check: when α > 0, is Dα/Dt < 0?
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

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()

    thr=torch.quantile(om.flatten(),0.80)  # top 20%
    if thr<1e-10: return None
    idx=(om>thr).nonzero(as_tuple=False)
    n=min(len(idx),n_sample)
    perm=torch.randperm(len(idx))[:n];pts=idx[perm]

    data={'alpha':[],'Dalpha':[],'S2ee':[],'Hww':[],'om':[],'R_lag':[]}

    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12: continue
        eh=wv/wn
        Sl=S[:,:,ix,iy,iz];Hl=H[:,:,ix,iy,iz]

        alpha=(eh@Sl@eh).item()
        S2ee=(eh@Sl@Sl@eh).item()
        Hww=(eh@Hl@eh).item()
        Dalpha=S2ee-2*alpha**2-Hww
        R_lag=Dalpha+alpha**2  # = S2ee - alpha² - Hww

        data['alpha'].append(alpha)
        data['Dalpha'].append(Dalpha)
        data['S2ee'].append(S2ee)
        data['Hww'].append(Hww)
        data['om'].append(wn.item())
        data['R_lag'].append(R_lag)

    for k in data: data[k]=np.array(data[k])
    return data

def make_ic(s,name):
    X,Y,Z=s.X,s.Y,s.Z
    if name=='TG':
        ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))
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
    print("LAGRANGIAN Dα/Dt: is it negative wherever α > 0?",flush=True)
    print("="*70,flush=True)
    print("  Dα/Dt = ê·S²·ê - 2α² - H_ωω  (at material point)",flush=True)
    print("  If Dα/Dt < 0 when α > 0: α bounded → regularity\n",flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)

        print(f"--- {ic_name} ---",flush=True)

        for evolve_steps in [200, 500, 1000, 2000, 4000]:
            if evolve_steps > 200:
                for _ in range(evolve_steps - prev_steps): w=s.step(w,dt)
            else:
                for _ in range(evolve_steps): w=s.step(w,dt)
            prev_steps = evolve_steps
            t = evolve_steps * dt

            d=compute_lagrangian_Dalpha(s,w)
            if d is None: continue

            # At points where α > 0: what fraction have Dα/Dt < 0?
            pos_alpha = d['alpha'] > 0
            if pos_alpha.sum() > 0:
                Dalpha_at_pos = d['Dalpha'][pos_alpha]
                frac_neg = (Dalpha_at_pos < 0).mean()
                mean_Dalpha = Dalpha_at_pos.mean()
                max_Dalpha = Dalpha_at_pos.max()

                # R_Lagrangian at positive-α points
                R_at_pos = d['R_lag'][pos_alpha]

                print(f"  t={t:.3f}: {pos_alpha.sum()}/{len(d['alpha'])} pts with α>0  "
                      f"Dα/Dt<0: {frac_neg*100:.1f}%  "
                      f"mean Dα/Dt={mean_Dalpha:+.2f}  "
                      f"max Dα/Dt={max_Dalpha:+.2f}  "
                      f"mean R_lag={R_at_pos.mean():+.2f}  "
                      f"R_lag<0: {(R_at_pos<0).mean()*100:.0f}%",flush=True)
            else:
                print(f"  t={t:.3f}: NO points with α>0 (all compressive)",flush=True)

        # Detailed breakdown at the final time
        d=compute_lagrangian_Dalpha(s,w)
        if d is not None:
            alpha=d['alpha']; Dalpha=d['Dalpha']
            pos=alpha>0

            print(f"\n  At t={t:.3f}, detailed breakdown (top 20% |ω|):",flush=True)
            print(f"    Total points: {len(alpha)}",flush=True)
            print(f"    α > 0: {pos.sum()} ({100*pos.mean():.1f}%)",flush=True)
            print(f"    α > 0 AND Dα/Dt < 0: {((alpha>0)&(Dalpha<0)).sum()} "
                  f"({100*((alpha>0)&(Dalpha<0)).mean():.1f}%)",flush=True)
            print(f"    α > 0 AND Dα/Dt > 0: {((alpha>0)&(Dalpha>0)).sum()} "
                  f"({100*((alpha>0)&(Dalpha>0)).mean():.1f}%) ← VIOLATIONS",flush=True)

            # The violations: what do they look like?
            violations = (alpha>0)&(Dalpha>0)
            if violations.sum()>0:
                v_alpha=alpha[violations]
                v_Dalpha=Dalpha[violations]
                v_Hww=d['Hww'][violations]
                v_S2ee=d['S2ee'][violations]
                v_om=d['om'][violations]
                print(f"\n    VIOLATION analysis ({violations.sum()} points):",flush=True)
                print(f"      α: mean={v_alpha.mean():.3f} max={v_alpha.max():.3f}",flush=True)
                print(f"      Dα/Dt: mean={v_Dalpha.mean():.3f} max={v_Dalpha.max():.3f}",flush=True)
                print(f"      H_ωω: mean={v_Hww.mean():.3f} (positive=stretching)",flush=True)
                print(f"      |ω|: mean={v_om.mean():.2f}",flush=True)
                print(f"      ê·S²·ê: mean={v_S2ee.mean():.3f}",flush=True)
                print(f"      2α²: mean={2*v_alpha.mean()**2:.3f}",flush=True)
                print(f"      ê·S²·ê > 2α² + H_ωω at violations",flush=True)
            else:
                print(f"\n    NO VIOLATIONS! Dα/Dt < 0 whenever α > 0! ✓",flush=True)
        print(flush=True)

    print(f"{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
