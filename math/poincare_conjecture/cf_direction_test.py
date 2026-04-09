"""
Constantin-Fefferman direction criterion: is |∇ξ| bounded at high |ω|?

Theorem (CF 1993): If |∇(ω/|ω|)| ≤ C/|ω|^{1/2} in the region where |ω| > M,
then regularity.

Weaker version: if |∇ξ|·|ω|^{1/2} is bounded, regularity follows.

Test: measure |∇ξ| at high-|ω| points and check the scaling with |ω|.
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

def measure_direction_gradient(s, w):
    """Compute |∇ξ| where ξ = ω/|ω|, binned by |ω|."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()

    # ξ_i = ω_i/|ω|
    xi=[wf[i]/(om+1e-30) for i in range(3)]

    # ∇ξ_i: gradient of each component
    grad_xi_sq=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        xi_h=s.fft(xi[i])
        for j in range(3):
            dxi=s.ifft(1j*kd[j]*D*xi_h)
            grad_xi_sq+=dxi**2

    grad_xi=grad_xi_sq.sqrt()  # |∇ξ|

    return om, grad_xi

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
    print("CONSTANTIN-FEFFERMAN: |nabla xi| at high |omega|",flush=True)
    print("="*70,flush=True)
    print("  CF criterion: |nabla(omega/|omega|)| <= C/|omega|^{1/2} => regularity",flush=True)
    print("  Test: |nabla xi| * |omega|^{1/2} bounded? (= CF number)\n",flush=True)

    for ic_name in ['trefoil','TG']:
        s=NS3D(N,0.);w=make_ic(s,ic_name)

        print(f"--- {ic_name} ---",flush=True)
        print(f"  {'t':>6s}  {'|om|_max':>8s}  ",end='',flush=True)
        for pct in [0.90,0.95,0.99]:
            print(f"CF({(1-pct)*100:.0f}%)  ",end='')
        print("  |nabla_xi|(99%)  scaling_p",flush=True)

        t=0.
        for epoch in range(15):
            om,gxi=measure_direction_gradient(s,w)
            om_flat=om.flatten();gxi_flat=gxi.flatten()
            om_max=om_flat.max().item()

            line=f"  {t:6.4f}  {om_max:8.2f}  "
            for pct in [0.90,0.95,0.99]:
                thr=torch.quantile(om_flat,pct).item()
                mask=om_flat>thr
                if mask.sum()>0:
                    cf=gxi_flat[mask]*om_flat[mask].sqrt()
                    line+=f"{cf.mean().item():7.3f}  "
                else:
                    line+="    N/A  "

            # At 99th percentile: measure |nabla xi| and the scaling
            thr99=torch.quantile(om_flat,0.99).item()
            mask99=om_flat>thr99
            if mask99.sum()>0:
                gxi_99=gxi_flat[mask99].mean().item()
                # Scaling: |nabla xi| ~ |omega|^p → log fit
                line+=f"  {gxi_99:10.4f}  "
            else:
                line+="       N/A  "

            # Power law: bin |nabla xi| vs |omega|
            mask_hi=om_flat>0.5*om_max
            if mask_hi.sum()>100:
                log_om=torch.log(om_flat[mask_hi])
                log_gxi=torch.log(gxi_flat[mask_hi]+1e-30)
                valid=(log_gxi>-20)&(log_om>0)
                if valid.sum()>10:
                    coeffs=np.polyfit(log_om[valid].numpy(),log_gxi[valid].numpy(),1)
                    p=coeffs[0]
                    line+=f"  {p:+.3f}"
                else:
                    line+="    N/A"
            else:
                line+="    N/A"

            print(line,flush=True)
            for _ in range(500): w=s.step(w,dt); t+=dt

    print(f"\n{'='*70}",flush=True)
    print("CF CRITERION INTERPRETATION:",flush=True)
    print("  CF number = |nabla xi| * |omega|^{1/2}",flush=True)
    print("  If CF bounded: REGULARITY (by Constantin-Fefferman 1993)",flush=True)
    print("  If CF grows: direction becomes singular → no conclusion",flush=True)
    print(f"\n  Scaling: |nabla xi| ~ |omega|^p",flush=True)
    print(f"  p < -1/2: CF number DECREASES with |omega| → strong regularity",flush=True)
    print(f"  p = -1/2: CF number constant → marginal regularity",flush=True)
    print(f"  p > -1/2: CF number grows → CF criterion fails",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
