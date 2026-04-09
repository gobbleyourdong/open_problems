"""
Pressure Hessian isotropy: is H more isotropic at high |ω|?

tr(H) = Δp = |ω|²/2 - |S|² > 0 at high |ω| (from attractor).
If H ≈ (tr(H)/3)I (isotropic): H_ωω = tr(H)/3 > 0.
If H is anisotropic: H_ωω could be negative despite tr(H) > 0.

Measure the ANISOTROPY ratio: |H_dev|/|H| where H_dev = H - (tr(H)/3)I.
If anisotropy DECREASES with |ω|: explains the sign flip.
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

def measure_isotropy(s, w, n_sample=2000):
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
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
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    om_max=om.max().item()

    idx=(om>0.1*om_max).nonzero(as_tuple=False)
    n=min(len(idx),n_sample);perm=torch.randperm(len(idx))[:n];pts=idx[perm]

    data={'om':[],'Hww':[],'trH':[],'aniso':[],'Hww_iso':[],'Hww_dev':[]}

    for pt in pts:
        ix,iy,iz=pt[0].item(),pt[1].item(),pt[2].item()
        wv=torch.tensor([wf[i][ix,iy,iz] for i in range(3)],dtype=DTYPE)
        wn=wv.norm()
        if wn<1e-12:continue
        eh=wv/wn
        Hl=H[:,:,ix,iy,iz]

        trH=Hl.trace().item()
        Hww=(eh@Hl@eh).item()
        Hww_iso=trH/3  # isotropic prediction
        Hww_dev=Hww-Hww_iso  # deviatoric part

        # Anisotropy: ||H_dev|| / ||H||
        H_dev=Hl-(trH/3)*torch.eye(3,dtype=DTYPE)
        aniso=(H_dev*H_dev).sum().sqrt().item()/((Hl*Hl).sum().sqrt().item()+1e-30)

        data['om'].append(wn.item())
        data['Hww'].append(Hww)
        data['trH'].append(trH)
        data['aniso'].append(aniso)
        data['Hww_iso'].append(Hww_iso)
        data['Hww_dev'].append(Hww_dev)

    for k in data:data[k]=np.array(data[k])
    return data, om_max

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
    print("PRESSURE ISOTROPY: is H more isotropic at high |ω|?",flush=True)
    print("="*70,flush=True)
    print("  H_ωω = H_iso + H_dev = tr(H)/3 + deviatoric",flush=True)
    print("  tr(H) = Δp = |ω|²/2 - |S|² > 0 at high |ω|",flush=True)
    print("  If H becomes isotropic: H_ωω → tr(H)/3 > 0\n",flush=True)

    for ic_name in ['trefoil']:
        s=NS3D(N,0.)
        w=make_trefoil(s)
        for _ in range(2000):w=s.step(w,dt)

        d,om_max=measure_isotropy(s,w)

        # Bin by |ω|/||ω||∞
        frac=d['om']/om_max
        bins=np.array([0.1,0.3,0.5,0.7,0.8,0.9,0.95,1.01])

        print(f"  {ic_name} t=0.2, ||ω||∞={om_max:.2f}",flush=True)
        print(f"  {'|ω|/max':>10s}  {'<H_ωω>':>8s}  {'<tr(H)/3>':>9s}  {'<H_dev>':>8s}  "
              f"{'aniso':>6s}  {'H_iso>0%':>8s}  {'H_ωω=H_iso?':>12s}",flush=True)

        for i in range(len(bins)-1):
            m=(frac>=bins[i])&(frac<bins[i+1])
            if m.sum()<10:continue
            hww=d['Hww'][m]; hiso=d['Hww_iso'][m]; hdev=d['Hww_dev'][m]
            ani=d['aniso'][m]

            # Is H_ωω ≈ H_iso (isotropic prediction)?
            match = np.abs(hww.mean()-hiso.mean()) / (np.abs(hiso.mean())+1e-30)
            match_str = f"{match:.2f}" if np.abs(hiso.mean())>0.01 else "N/A"

            print(f"  [{bins[i]:.1f},{bins[i+1]:.2f})  {hww.mean():+8.3f}  "
                  f"{hiso.mean():+9.3f}  {hdev.mean():+8.3f}  "
                  f"{ani.mean():6.3f}  {(hiso>0).mean()*100:7.0f}%  "
                  f"{'ratio='+match_str:>12s}",flush=True)

        # THE KEY: does H_dev shrink relative to H_iso at high |ω|?
        print(f"\n  KEY: |H_dev_ωω / H_iso_ωω| ratio vs |ω|:",flush=True)
        for i in range(len(bins)-1):
            m=(frac>=bins[i])&(frac<bins[i+1])
            if m.sum()<10:continue
            hiso_mean=np.abs(d['Hww_iso'][m]).mean()
            hdev_mean=np.abs(d['Hww_dev'][m]).mean()
            ratio=hdev_mean/(hiso_mean+1e-30)
            print(f"    |ω|/max [{bins[i]:.1f},{bins[i+1]:.2f}): "
                  f"|H_dev|/|H_iso| = {ratio:.3f}  "
                  f"({'deviatoric dominates' if ratio>1 else 'ISOTROPIC dominates'})",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("IF |H_dev|/|H_iso| → 0 at high |ω|: H becomes isotropic → H_ωω > 0",flush=True)
    print("IF |H_dev|/|H_iso| stays ~1: anisotropy persists → need CZ bound",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
