"""
Critical test: how does R = dα/dt + α² scale with |ω|?

If R/|ω|² → 0: α bounded → regularity (GOOD)
If R/|ω|² → C > 0: α ~ |ω| → d|ω|/dt ~ |ω|² → possible blowup (BAD)
If R/|ω|² → ∞: definitely blowup (WORST)

Test by measuring R at points with DIFFERENT |ω| values (not just the max).
Use bins of |ω| and compute mean R in each bin.
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


def compute_alpha_field(s, w):
    """Compute α = ê·S·ê at every grid point."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j]=s.ifft(1j*kd[j]*D*u[i])
    S=0.5*(A+A.transpose(0,1))
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2
    om=om_sq.sqrt()

    # α = ω_i S_ij ω_j / |ω|²
    alpha=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            alpha += wf[i]*S[i,j]*wf[j]
    alpha = alpha / (om_sq + 1e-30)

    # ê·S²·ê = ω_i S_ik S_kj ω_j / |ω|²
    S2ee=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Sij=torch.zeros(N,N,N,dtype=DTYPE)
            for k in range(3): Sij+=S[i,k]*S[k,j]
            S2ee += wf[i]*Sij*wf[j]
    S2ee = S2ee / (om_sq + 1e-30)

    return alpha, S2ee, om


def main():
    N=32;dt=1e-4;dt_fd=20  # 20 steps between snapshots for finite diff
    print("="*70,flush=True)
    print("R SCALING TEST: how does R = dα/dt + α² scale with |ω|?",flush=True)
    print("="*70,flush=True)

    for ic_name in ['TG','KP','trefoil']:
        s=NS3D(N,0.)
        X,Y,Z=s.X,s.Y,s.Z
        if ic_name=='TG':
            ux=torch.cos(X)*torch.sin(Y)*torch.cos(Z);uy=-torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(torch.zeros_like(X)))
        elif ic_name=='KP':
            ux=torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
            uy=torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
            uz=torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
            w=s.curl(s.fft(ux),s.fft(uy),s.fft(uz))
        else:
            wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
            n_pts=200;tp=torch.linspace(0,2*pi,n_pts,dtype=DTYPE)
            cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi
            cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
            cz=(-torch.sin(3*tp))*0.5+pi
            tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp)
            tz=-3*torch.cos(3*tp);ds=2*pi/n_pts
            for i in range(n_pts):
                g=10.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
                wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
            w=(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

        # Evolve to get interesting dynamics
        for _ in range(500): w=s.step(w,dt)

        # Take two snapshots separated by dt_fd steps
        alpha0, S2ee0, om0 = compute_alpha_field(s, w)
        w_save = tuple(wi.clone() for wi in w)

        for _ in range(dt_fd): w=s.step(w,dt)

        alpha1, S2ee1, om1 = compute_alpha_field(s, w)

        # dα/dt by finite difference (Eulerian, at each grid point)
        dalpha = (alpha1 - alpha0) / (dt_fd * dt)

        # R = dα/dt + α²
        R = dalpha + alpha0**2

        # Bin by |ω| and compute mean R, mean α², mean R/|ω|²
        om_flat = om0.flatten().numpy()
        R_flat = R.flatten().numpy()
        alpha_flat = alpha0.flatten().numpy()
        S2ee_flat = S2ee0.flatten().numpy()

        # Only points with significant |ω|
        mask = om_flat > 0.5 * om_flat.max()
        if mask.sum() < 10:
            mask = om_flat > 0.1 * om_flat.max()

        om_m = om_flat[mask]
        R_m = R_flat[mask]
        a_m = alpha_flat[mask]
        S2_m = S2ee_flat[mask]

        # Bin
        n_bins = 8
        pcts = np.linspace(0, 100, n_bins+1)
        edges = np.percentile(om_m, pcts)

        print(f"\n--- {ic_name} (t=0.05, Euler) ---", flush=True)
        print(f"  {'|ω| range':>15s}  {'mean |ω|':>8s}  {'mean α':>8s}  {'mean α²':>8s}  "
              f"{'mean R':>8s}  {'R/|ω|²':>8s}  {'R/α²':>8s}  {'R/S²ê':>8s}", flush=True)

        for i in range(n_bins):
            bin_mask = (om_m >= edges[i]) & (om_m < edges[i+1] + 1e-10)
            if bin_mask.sum() < 5: continue
            om_bin = om_m[bin_mask]
            R_bin = R_m[bin_mask]
            a_bin = a_m[bin_mask]
            S2_bin = S2_m[bin_mask]

            mean_om = om_bin.mean()
            mean_a = a_bin.mean()
            mean_a2 = (a_bin**2).mean()
            mean_R = R_bin.mean()
            mean_S2 = S2_bin.mean()

            R_over_om2 = mean_R / (mean_om**2 + 1e-30)
            R_over_a2 = mean_R / (mean_a2 + 1e-30)
            R_over_S2 = mean_R / (mean_S2 + 1e-30)

            print(f"  [{edges[i]:6.2f},{edges[i+1]:6.2f})  {mean_om:8.2f}  {mean_a:+8.4f}  "
                  f"{mean_a2:8.4f}  {mean_R:+8.4f}  {R_over_om2:+8.5f}  "
                  f"{R_over_a2:+8.3f}  {R_over_S2:+8.3f}", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("KEY: If R/|ω|² → 0 as |ω| increases: REGULARITY (α bounded)", flush=True)
    print("     If R/|ω|² → C > 0: DANGEROUS (α ~ |ω|, possible blowup)", flush=True)
    print("     If R/|ω|² → ∞: BLOWUP", flush=True)
    print(f"{'='*70}", flush=True)


if __name__=='__main__':
    main()
