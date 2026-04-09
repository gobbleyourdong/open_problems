"""
Classic BKM diagnostic: does 1/||ω||∞ extrapolate to zero?

Standard method (Hou-Li 2006, Kerr 2013):
- Plot 1/||ω||∞(t)
- If linear → 1/(T*-t) blowup at T*
- If concave up → sub-blowup (regularity)
- If concave down → super-blowup (faster than 1/(T*-t))

Also fit: ||ω||∞ = A/(T*-t)^γ
- γ = 1: standard BKM blowup
- γ < 1: weaker singularity (BKM still holds)
- γ > 1: stronger singularity

Run on all ICs with dense time sampling.
"""
import torch, numpy as np, math
from scipy.optimize import curve_fit
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
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)];return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()

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

def blowup_fit(t, A, Tstar, gamma):
    """||ω|| = A / (Tstar - t)^gamma"""
    return A / np.maximum(Tstar - t, 1e-10)**gamma

def main():
    dt=1e-4; N=32
    print("="*70,flush=True)
    print("BKM EXTRAPOLATION: does 1/||ω||∞ → 0?",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','TG','KP']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        times=[];oms=[]
        t=0.;n_total=8000 if ic_name=='trefoil' else 4000
        sample=20

        for step in range(n_total+1):
            if step%sample==0:
                om=s.om_max(w)
                times.append(t);oms.append(om)
            if step<n_total: w=s.step(w,dt);t+=dt

        times=np.array(times);oms=np.array(oms)
        inv_om=1.0/oms

        print(f"\n--- {ic_name} (Euler, N={N}, t=[0, {times[-1]:.3f}]) ---",flush=True)
        print(f"  ||ω||∞: {oms[0]:.2f} → {oms[-1]:.2f}",flush=True)
        print(f"  1/||ω||∞: {inv_om[0]:.4f} → {inv_om[-1]:.4f}",flush=True)

        # Linear fit to 1/||ω||: if linear with negative slope, T* = -intercept/slope
        if oms[-1] > oms[0]:  # growing
            # Use second half for fit (more developed dynamics)
            n_half=len(times)//2
            t_fit=times[n_half:]
            inv_fit=inv_om[n_half:]

            coeffs=np.polyfit(t_fit, inv_fit, 1)
            slope, intercept = coeffs
            if slope < 0:
                T_star_linear = -intercept/slope
                print(f"\n  Linear fit to 1/||ω||∞ (second half):",flush=True)
                print(f"    slope = {slope:.6f}, intercept = {intercept:.6f}",flush=True)
                print(f"    Extrapolated T* = {T_star_linear:.4f}",flush=True)
                print(f"    Current t = {times[-1]:.4f}",flush=True)
                if T_star_linear > times[-1]:
                    print(f"    T* > t_final: blowup NOT YET (but predicted at {T_star_linear:.3f})",flush=True)
                else:
                    print(f"    T* < t_final: should have blown up already — fit is WRONG",flush=True)
            else:
                print(f"\n  1/||ω||∞ has POSITIVE slope → ||ω||∞ DECREASING → no blowup",flush=True)

            # Curvature test: second derivative of 1/||ω||
            d2_inv = np.gradient(np.gradient(inv_om, times), times)
            curvature_late = d2_inv[n_half:].mean()
            print(f"\n  Curvature of 1/||ω||∞:",flush=True)
            print(f"    d²(1/||ω||)/dt² (second half): {curvature_late:+.6f}",flush=True)
            if curvature_late > 0:
                print(f"    CONCAVE UP → deceleration → REGULARITY ✓",flush=True)
            elif curvature_late < -1e-6:
                print(f"    CONCAVE DOWN → acceleration → concerning",flush=True)
            else:
                print(f"    APPROXIMATELY LINEAR → marginal",flush=True)

            # Try blowup fit: ||ω|| = A/(T*-t)^γ
            try:
                # Only fit if ||ω|| is growing
                mask = oms > oms[0] * 1.1  # at least 10% growth
                if mask.sum() > 10:
                    t_fit2 = times[mask]
                    om_fit2 = oms[mask]
                    popt, pcov = curve_fit(blowup_fit, t_fit2, om_fit2,
                                           p0=[oms[-1]*0.1, times[-1]*2, 1.0],
                                           bounds=([0, times[-1]*0.5, 0.01],
                                                   [1e6, times[-1]*100, 10.0]),
                                           maxfev=10000)
                    A_fit, Tstar_fit, gamma_fit = popt
                    print(f"\n  Blowup fit: ||ω|| = {A_fit:.2f} / (T*-t)^{gamma_fit:.3f}",flush=True)
                    print(f"    T* = {Tstar_fit:.4f}",flush=True)
                    print(f"    γ = {gamma_fit:.3f}",flush=True)
                    if gamma_fit < 0.5:
                        print(f"    γ < 0.5: very weak growth → REGULARITY ✓",flush=True)
                    elif gamma_fit < 1.0:
                        print(f"    γ < 1: sub-BKM → REGULARITY ✓",flush=True)
                    elif Tstar_fit > 10 * times[-1]:
                        print(f"    T* >> t_final: blowup infinitely far away → REGULARITY ✓",flush=True)
                    else:
                        print(f"    T* = {Tstar_fit:.3f}: fit predicts blowup — CHECK RESOLUTION",flush=True)

                    # Quality of fit
                    om_pred = blowup_fit(t_fit2, *popt)
                    residual = np.sqrt(((om_fit2 - om_pred)**2).mean()) / om_fit2.mean()
                    print(f"    Fit residual: {residual*100:.1f}%",flush=True)
            except Exception as e:
                print(f"\n  Blowup fit failed: {e}",flush=True)

        else:
            print(f"\n  ||ω||∞ is DECREASING → trivially regular ✓",flush=True)

        # Print time series (sparse)
        print(f"\n  Time series:",flush=True)
        print(f"  {'t':>8s}  {'||ω||∞':>8s}  {'1/||ω||':>8s}",flush=True)
        for i in range(0, len(times), max(1,len(times)//12)):
            print(f"  {times[i]:8.4f}  {oms[i]:8.2f}  {inv_om[i]:8.5f}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
