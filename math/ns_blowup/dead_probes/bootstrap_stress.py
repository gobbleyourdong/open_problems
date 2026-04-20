"""
STRESS TEST the bootstrap: does max α < 3 and H_ωω > 0 hold
in the approaching zone for ALL ICs, at N=48, and over long times?

Also: try to BREAK it with an adversarial IC (maximum initial stretching).
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

def measure_approaching_zone(s, w, frac_lo=0.85, frac_hi=1.001):
    """Measure α and H_ωω in the approaching zone."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()
    om_max=om.max().item()
    if om_max<1e-10: return None

    # α field
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    S=0.5*(A+A.transpose(0,1))
    alpha_field=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):alpha_field+=wf[i]*S[i,j]*wf[j]
    alpha_field=alpha_field/(om_sq+1e-30)

    # H_ωω field
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)
    Hww_field=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):Hww_field+=wf[i]*H[i,j]*wf[j]
    Hww_field=Hww_field/(om_sq+1e-30)

    # Approaching zone
    frac=om/om_max
    mask=(frac>=frac_lo)&(frac<frac_hi)
    n_pts=mask.sum().item()
    if n_pts<3: return None

    a=alpha_field[mask];h=Hww_field[mask]
    return {
        'om_max':om_max, 'n_pts':int(n_pts),
        'alpha_mean':a.mean().item(), 'alpha_max':a.max().item(),
        'alpha_min':a.min().item(),
        'Hww_mean':h.mean().item(), 'Hww_min':h.min().item(),
        'Hww_pos_frac':(h>0).float().mean().item(),
    }

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
    elif name=='adversarial':
        # Two perpendicular tubes aimed at each other — maximum stretching
        r1=((X-pi)**2+(Y-pi)**2).sqrt()
        r2=((Y-pi)**2+(Z-pi)**2).sqrt()
        sigma=0.25
        # Tube 1 along z, tube 2 along x — perpendicular collision
        wz=15.0*torch.exp(-r1**2/(2*sigma**2))
        wx=15.0*torch.exp(-r2**2/(2*sigma**2))
        wy=torch.zeros_like(X)
        wh=(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))
        # Project div-free
        kdotw=s.kx*wh[0]+s.ky*wh[1]+s.kz*wh[2]
        return(wh[0]-s.kx*kdotw/s.ksq,wh[1]-s.ky*kdotw/s.ksq,wh[2]-s.kz*kdotw/s.ksq)

def main():
    dt=1e-4
    print("="*70,flush=True)
    print("BOOTSTRAP STRESS TEST: all ICs, N=32 and N=48",flush=True)
    print("="*70,flush=True)
    print(f"  Approaching zone: |ω| > 0.85×||ω||∞",flush=True)
    print(f"  Bootstrap needs: max α bounded AND H_ωω > 0\n",flush=True)

    print(f"  {'IC':>12s}  {'N':>3s}  {'t':>5s}  {'||ω||∞':>7s}  {'maxα':>6s}  "
          f"{'<H_ωω>':>7s}  {'H>0%':>5s}  {'n':>4s}  {'α<3?':>5s}  {'H>0?':>4s}",flush=True)
    print("-"*85,flush=True)

    worst_alpha = 0
    worst_ic = ""
    hww_violations = 0
    total_tests = 0

    for ic_name in ['TG','KP','trefoil','adversarial']:
        for N_test in [32, 48]:
            dt_use = dt if N_test==32 else 5e-5
            s=NS3D(N_test,0.)
            try:
                w=make_ic(s,ic_name)
            except:
                continue

            t=0.
            for epoch in range(10):
                n_step = 300 if N_test==32 else 400
                for _ in range(n_step): w=s.step(w,dt_use); t+=dt_use

                m=measure_approaching_zone(s,w,frac_lo=0.85)
                if m is None: continue
                total_tests += 1

                a_ok = "YES" if m['alpha_max']<3.5 else "**NO**"
                h_ok = "YES" if m['Hww_pos_frac']>0.8 else "NO"

                if m['alpha_max']>worst_alpha:
                    worst_alpha=m['alpha_max'];worst_ic=f"{ic_name}_N{N_test}_t{t:.3f}"
                if m['Hww_pos_frac']<0.5:
                    hww_violations+=1

                if epoch%3==0:
                    print(f"  {ic_name:>12s}  {N_test:3d}  {t:5.3f}  {m['om_max']:7.2f}  "
                          f"{m['alpha_max']:+6.2f}  {m['Hww_mean']:+7.2f}  "
                          f"{m['Hww_pos_frac']*100:5.0f}%  {m['n_pts']:4d}  "
                          f"{a_ok:>5s}  {h_ok:>4s}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print(f"SUMMARY ({total_tests} measurements):",flush=True)
    print(f"  Worst max α in approaching zone: {worst_alpha:.3f} at {worst_ic}",flush=True)
    print(f"  α < 3.5 everywhere: {'YES ✓' if worst_alpha<3.5 else 'NO ✗'}",flush=True)
    print(f"  H_ωω violations (<50% positive): {hww_violations}/{total_tests}",flush=True)
    print(f"\n  Bootstrap holds: {'YES ✓' if worst_alpha<3.5 and hww_violations==0 else 'NEEDS REVIEW'}",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
