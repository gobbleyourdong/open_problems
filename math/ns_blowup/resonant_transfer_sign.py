"""
Instance C — Resonant vs non-resonant transfer sign at the PALINSTROPHY level.

Split the triadic transfer into:
  RESONANT: |k₁| ≈ |k₂| ≈ |k₃| (all shells similar)
  NON-RESONANT: |k₁| >> |k₂| or vice versa (scale-separated)

From file 125: the resonant stretching is COMPRESSIVE at high |ω|.
Question: does this hold for the PALINSTROPHY transfer (not just enstrophy)?

Compute: weighted transfer Σ |k₃|² T(k₁,k₂,k₃), split by resonance.
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
        s.kmag=s.ksq.sqrt()
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

def measure_transfer_by_type(s, w):
    """
    Compute the enstrophy and palinstrophy transfer, split by shell interaction type.

    For each shell j receiving transfer T(j):
    Split into: LOCAL (from nearby shells) vs NONLOCAL (from distant shells).
    Local = resonant (|k_source| ≈ |k_target|).
    """
    N=s.N;D=s.D

    # Full RHS
    rhs_w = s.rhs(w)

    # Shell decomposition
    k_max = N//3
    n_shells = min(k_max, 12)

    # For each target shell j, compute transfer from LOCAL and NONLOCAL sources
    results = {'shell':[], 'E_j':[], 'T_total':[], 'T_local':[], 'T_nonlocal':[],
               'P_T_total':[], 'P_T_local':[], 'P_T_nonlocal':[]}

    for j in range(1, n_shells+1):
        target_mask = ((s.kmag >= j-0.5) & (s.kmag < j+0.5)).to(DTYPE)

        # E_j
        E_j = sum((target_mask * w[i].abs()**2).sum().item() for i in range(3)) / N**3

        # Total transfer to shell j (enstrophy)
        T_total = sum(2*(target_mask * (w[i].conj()*rhs_w[i]).real).sum().item()
                      for i in range(3)) / N**3

        # Palinstrophy transfer: weight by |k|²
        P_T_total = sum(2*(s.ksq * target_mask * (w[i].conj()*rhs_w[i]).real).sum().item()
                        for i in range(3)) / N**3

        # To get LOCAL vs NONLOCAL: compute the RHS using only nearby shells as source
        # "Local" = source shells within ±2 of target
        local_mask = torch.zeros(N,N,N,dtype=DTYPE)
        for src_j in range(max(1,j-2), min(n_shells+1, j+3)):
            local_mask += ((s.kmag >= src_j-0.5) & (s.kmag < src_j+0.5)).to(DTYPE)
        local_mask = local_mask.clamp(0,1)

        # Restrict vorticity to local shells
        w_local = tuple(wi * local_mask for wi in w)
        rhs_local = s.rhs(w_local)

        T_local = sum(2*(target_mask * (w[i].conj()*rhs_local[i]).real).sum().item()
                      for i in range(3)) / N**3
        T_nonlocal = T_total - T_local

        P_T_local = sum(2*(s.ksq * target_mask * (w[i].conj()*rhs_local[i]).real).sum().item()
                        for i in range(3)) / N**3
        P_T_nonlocal = P_T_total - P_T_local

        results['shell'].append(j)
        results['E_j'].append(E_j)
        results['T_total'].append(T_total)
        results['T_local'].append(T_local)
        results['T_nonlocal'].append(T_nonlocal)
        results['P_T_total'].append(P_T_total)
        results['P_T_local'].append(P_T_local)
        results['P_T_nonlocal'].append(P_T_nonlocal)

    return {k:np.array(v) for k,v in results.items()}

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
    print("INSTANCE C — RESONANT vs NONLOCAL transfer at palinstrophy level",flush=True)
    print("="*70,flush=True)

    s=NS3D(N,0.);w=make_trefoil(s)
    for _ in range(1000):w=s.step(w,dt)

    r=measure_transfer_by_type(s,w)

    print(f"\n  Trefoil t=0.1:",flush=True)
    print(f"  {'k':>3s}  {'E_j':>10s}  {'T(enst)':>10s}  {'T_loc':>10s}  {'T_nloc':>10s}  "
          f"{'PT(pal)':>10s}  {'PT_loc':>10s}  {'PT_nloc':>10s}",flush=True)

    for i in range(len(r['shell'])):
        if r['E_j'][i] < 1e-10 and abs(r['T_total'][i]) < 1e-10: continue
        print(f"  {r['shell'][i]:3d}  {r['E_j'][i]:10.2f}  "
              f"{r['T_total'][i]:+10.2f}  {r['T_local'][i]:+10.2f}  {r['T_nonlocal'][i]:+10.2f}  "
              f"{r['P_T_total'][i]:+10.0f}  {r['P_T_local'][i]:+10.0f}  {r['P_T_nonlocal'][i]:+10.0f}",flush=True)

    # KEY: is the LOCAL (resonant) transfer NEGATIVE at the palinstrophy level?
    sig = r['E_j'] > 0.01*r['E_j'].max()
    if sig.sum()>0:
        local_pal = r['P_T_local'][sig]
        nonlocal_pal = r['P_T_nonlocal'][sig]
        total_pal = r['P_T_total'][sig]
        print(f"\n  Active shells ({sig.sum()}):",flush=True)
        print(f"    Local (resonant) palinstrophy transfer: {local_pal.sum():+.0f}",flush=True)
        print(f"    Nonlocal palinstrophy transfer: {nonlocal_pal.sum():+.0f}",flush=True)
        print(f"    Total: {total_pal.sum():+.0f}",flush=True)
        print(f"    Local fraction: {abs(local_pal.sum())/(abs(total_pal.sum())+1e-30)*100:.0f}%",flush=True)
        if local_pal.sum() < 0:
            print(f"    → LOCAL TRANSFER IS NEGATIVE (compressive) ✓",flush=True)
        else:
            print(f"    → LOCAL TRANSFER IS POSITIVE (stretching) ✗",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
