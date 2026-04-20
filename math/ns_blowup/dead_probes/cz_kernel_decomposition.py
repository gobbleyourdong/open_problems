"""
Calderón-Zygmund kernel decomposition of the pressure Hessian.

H_ij(x) = ∫ K_ij(x-y) source(y) dy  (PV integral)
where source = |ω|²/2 - |S|²

Decompose into shells by distance |x-y|:
H_ij(x) = H_near(δ<r₁) + H_mid(r₁<δ<r₂) + H_far(δ>r₂)

At the max-|ω| point: which shell dominates? What's the sign?

This reveals WHY Yang fails non-locally and WHERE the non-local
contribution comes from.
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

def decompose_pressure_by_distance(s, w, n_shells=8):
    """
    At the max-|ω| point x*, decompose H_ωω into contributions
    from concentric shells at different distances.

    Method: compute the pressure source, apply spatial masks at
    different radii, solve Poisson for each masked source separately,
    and measure H_ωω from each.
    """
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];L=s.Lx

    # Full fields
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()

    # Pressure source: -A_ij A_ji = |ω|²/2 - |S|²
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): source-=A[i,j]*A[j,i]

    # Max-|ω| point
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    xm=ix*L/N;ym=iy*L/N;zm=iz*L/N

    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return None
    eh=wv/wn

    # Distance field from max point (periodic)
    x=torch.linspace(0,L-L/N,N,dtype=DTYPE)
    X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
    dx=torch.min(torch.abs(X-xm),L-torch.abs(X-xm))
    dy=torch.min(torch.abs(Y-ym),L-torch.abs(Y-ym))
    dz=torch.min(torch.abs(Z-zm),L-torch.abs(Z-zm))
    dist=(dx**2+dy**2+dz**2).sqrt()

    # Shell boundaries (log-spaced from grid scale to domain size)
    r_min=L/N  # grid spacing
    r_max=L/2  # half domain
    shell_edges=np.logspace(np.log10(r_min),np.log10(r_max),n_shells+1)

    # Full H_ωω for reference
    source_h=s.fft(source)
    p_hat_full=-source_h/s.ksq; p_hat_full[0,0,0]=0
    H_full=torch.zeros(3,3,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H_full[i,j]=s.ifft(-kd[i]*kd[j]*p_hat_full)[ix,iy,iz]
    H_ww_full=(eh@H_full@eh).item()

    # Decompose by shell
    results=[]
    for shell_idx in range(n_shells):
        r_lo=shell_edges[shell_idx]
        r_hi=shell_edges[shell_idx+1]

        mask=((dist>=r_lo)&(dist<r_hi)).to(DTYPE)
        source_shell=source*mask

        # Solve Poisson for this shell's source
        src_h=s.fft(source_shell)
        p_h=-src_h/s.ksq; p_h[0,0,0]=0

        H_shell=torch.zeros(3,3,dtype=DTYPE)
        for i in range(3):
            for j in range(3):
                H_shell[i,j]=s.ifft(-kd[i]*kd[j]*p_h)[ix,iy,iz]
        H_ww_shell=(eh@H_shell@eh).item()

        # Source statistics in this shell
        src_in=source_shell[mask>0.5]
        src_mean=src_in.mean().item() if len(src_in)>0 else 0
        src_vol=mask.sum().item()*(L/N)**3

        results.append({
            'r_lo': r_lo, 'r_hi': r_hi,
            'H_ww': H_ww_shell,
            'src_mean': src_mean,
            'src_vol': src_vol,
            'n_pts': int(mask.sum().item()),
        })

    return H_ww_full, results, om[ix,iy,iz].item()

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
    print("CZ KERNEL DECOMPOSITION: pressure from near vs far",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        # Evolve to develop dynamics
        for _ in range(500): w=s.step(w,dt)

        print(f"\n--- {ic_name} (t=0.05) ---",flush=True)
        result=decompose_pressure_by_distance(s,w)
        if result is None:
            print("  No data",flush=True)
            continue

        H_full, shells, om_max = result

        print(f"  |omega|_max = {om_max:.2f}",flush=True)
        print(f"  H_ww (full) = {H_full:+.6f}",flush=True)
        print(f"\n  {'r_lo':>6s}  {'r_hi':>6s}  {'H_ww':>10s}  {'% of total':>10s}  "
              f"{'src_mean':>10s}  {'n_pts':>6s}  {'sign':>5s}",flush=True)

        H_sum=0
        for sh in shells:
            pct=sh['H_ww']/(abs(H_full)+1e-30)*100
            sign="+" if sh['H_ww']>0 else "-"
            H_sum+=sh['H_ww']
            print(f"  {sh['r_lo']:6.3f}  {sh['r_hi']:6.3f}  {sh['H_ww']:+10.6f}  "
                  f"{pct:+10.1f}%  {sh['src_mean']:+10.4f}  {sh['n_pts']:6d}  {sign:>5s}",flush=True)

        print(f"  {'SUM':>14s}  {H_sum:+10.6f}  (should ≈ {H_full:+.6f})",flush=True)

        # KEY: at what radius does the sign flip?
        print(f"\n  Cumulative H_ww (from near to far):",flush=True)
        cum=0
        for sh in shells:
            cum+=sh['H_ww']
            print(f"    r < {sh['r_hi']:.3f}: cumulative H_ww = {cum:+.6f}  "
                  f"({'compressive' if cum<0 else 'stretching'})",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("INTERPRETATION:",flush=True)
    print("  If NEAR shells are compressive and FAR shells flip to stretching:",flush=True)
    print("  → Yang (local) is correct locally but non-local tails reverse it",flush=True)
    print("  → This is exactly what Gemini predicted (CZ non-local tails)",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
