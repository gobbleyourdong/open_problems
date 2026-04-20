"""Cross-validate thin trefoil ratio at N=48."""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N,nu=0.):
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
    def step(s,w,dt):
        D=s.D;u=s.vel(*w);f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]):f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        def add(a,b,c):return tuple(a[i]+c*b[i] for i in range(3))
        k1=tuple(r);k2_r=[];k3_r=[];k4_r=[]
        # Simplified — just do Euler step for speed
        return tuple(s.D*(w[i]+dt*r[i]) for i in range(3))

def measure_ratio(s, w, frac_lo=0.8):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz];u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om_sq=wf[0]**2+wf[1]**2+wf[2]**2;om=om_sq.sqrt()
    om_max=om.max().item()
    if om_max<1e-10:return None
    mask=om>frac_lo*om_max
    idx=mask.nonzero(as_tuple=False)
    n=min(len(idx),500);perm=torch.randperm(len(idx))[:n];pts=idx[perm]
    hiso_list=[];hdev_list=[]
    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12:continue
        eh=wv/wn;Hl=H[:,:,ix,iy,iz]
        trH=Hl.trace().item();hww=(eh@Hl@eh).item()
        hiso_list.append(trH/3);hdev_list.append(hww-trH/3)
    if not hiso_list:return None
    hi=np.abs(np.array(hiso_list)).mean();hd=np.abs(np.array(hdev_list)).mean()
    return {'ratio':hd/(hi+1e-30),'om_max':om_max,'n':len(hiso_list)}

def make_trefoil(s, amp=10., sigma=0.3):
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
    cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
    cz=(-torch.sin(3*tp))*0.5+pi
    tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
    ds=2*pi/200
    for i in range(200):
        g=amp*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*sigma**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    print("="*70,flush=True)
    print("N=48 CROSS-VALIDATION: thin trefoil ratio",flush=True)
    print("="*70,flush=True)

    # Compare N=32 and N=48 for σ=0.15 and σ=0.20
    for sigma in [0.30, 0.20, 0.15]:
        amp = 10. / (sigma/0.3)**2  # scale amplitude to keep circulation constant
        print(f"\n  σ={sigma}, amp={amp:.1f}:",flush=True)
        for N_test in [32, 48]:
            dx = 2*pi/N_test
            s=NS3D(N_test)
            w=make_trefoil(s, amp=amp, sigma=sigma)
            r=measure_ratio(s,w)
            if r:
                print(f"    N={N_test} (dx={dx:.3f}, σ/dx={sigma/dx:.2f}): "
                      f"ratio={r['ratio']:.4f}  |ω|={r['om_max']:.1f}  "
                      f"{'RESOLVED' if sigma/dx>1.0 else 'MARGINAL' if sigma/dx>0.5 else 'UNDER'}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("KEY: if ratio INCREASES with N → real (bad for proof)",flush=True)
    print("     if ratio DECREASES with N → resolution artifact (good)",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
