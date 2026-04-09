"""
Fourier shell decomposition of the pressure Hessian.

The CORRECT decomposition: by wavenumber, not by distance.
In Fourier space: H_ij(k) = k_i k_j / |k|² × source(k)
This is EXACT (no aliasing) for each k-shell.
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

def fourier_pressure_decomp(s, w):
    """Decompose H_ωω by Fourier shell (exact, no aliasing)."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)

    # Velocity gradient and source
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    source_h=s.fft(source)

    # Vorticity direction at max
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
    wn=wv.norm()
    if wn<1e-12: return None
    eh=wv/wn

    # Full H_ωω
    p_hat_full=-source_h/s.ksq; p_hat_full[0,0,0]=0
    H_full=torch.zeros(3,3,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H_full[i,j]=s.ifft(-kd[i]*kd[j]*p_hat_full)[ix,iy,iz]
    H_ww_full=(eh@H_full@eh).item()

    # Shell decomposition: |k| in [k_lo, k_hi)
    k_edges=np.arange(0.5, N//2+0.5, 1.0)  # integer shells

    results=[]
    for si in range(len(k_edges)-1):
        klo=k_edges[si]; khi=k_edges[si+1]
        mask=((s.kmag>=klo)&(s.kmag<khi))

        # Pressure in this shell: p_hat = -source_hat/|k|² (only for k in shell)
        p_shell=-source_h*mask/s.ksq
        p_shell[0,0,0]=0

        # H_ωω from this shell
        H_shell=torch.zeros(3,3,dtype=DTYPE)
        for i in range(3):
            for j in range(3):
                H_shell[i,j]=s.ifft(-kd[i]*kd[j]*p_shell)[ix,iy,iz]
        H_ww_shell=(eh@H_shell@eh).item()

        # Source energy in this shell
        src_energy=(source_h.abs()**2 * mask).sum().item()

        results.append({
            'k_lo':klo,'k_hi':khi,
            'H_ww':H_ww_shell,
            'src_E':src_energy,
            'n_modes':int(mask.sum().item()),
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
    print("FOURIER SHELL PRESSURE: H_ww by wavenumber (EXACT)",flush=True)
    print("="*70,flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)
        for _ in range(500): w=s.step(w,dt)

        result=fourier_pressure_decomp(s,w)
        if result is None: continue
        H_full,shells,om_max=result

        print(f"\n--- {ic_name} (t=0.05) ---",flush=True)
        print(f"  |ω|_max={om_max:.2f}, H_ww(full)={H_full:+.6f}",flush=True)
        print(f"\n  {'|k|':>5s}  {'H_ww':>10s}  {'% total':>8s}  {'cumul':>10s}  "
              f"{'src_E':>10s}  {'modes':>6s}",flush=True)

        cum=0
        for sh in shells:
            if abs(sh['H_ww'])<1e-12 and sh['src_E']<1e-6: continue
            cum+=sh['H_ww']
            pct=sh['H_ww']/(abs(H_full)+1e-30)*100
            k_mid=(sh['k_lo']+sh['k_hi'])/2
            print(f"  {k_mid:5.1f}  {sh['H_ww']:+10.6f}  {pct:+8.1f}%  "
                  f"{cum:+10.6f}  {sh['src_E']:10.2f}  {sh['n_modes']:6d}",flush=True)

        print(f"  {'SUM':>5s}  {cum:+10.6f}  (full: {H_full:+.6f})",flush=True)

        # KEY: which wavenumbers contribute stretching vs compression?
        stretch_k=[]
        compress_k=[]
        for sh in shells:
            if sh['H_ww']>1e-8: stretch_k.append((sh['k_lo']+sh['k_hi'])/2)
            elif sh['H_ww']<-1e-8: compress_k.append((sh['k_lo']+sh['k_hi'])/2)
        print(f"\n  Stretching modes (H_ww>0): k = {[f'{k:.0f}' for k in stretch_k[:10]]}",flush=True)
        print(f"  Compressive modes (H_ww<0): k = {[f'{k:.0f}' for k in compress_k[:10]]}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
