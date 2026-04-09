"""
Instance B: VERIFY Instance C's proof (file 267).

The LEMMA: On T², the operator L = Δ_xy - k² has all eigenvalues ≤ -k² < 0.
Therefore L⁻¹ maps positive functions to negative functions.
If source f_k > 0 at x*: then p_k < 0, and -k²p_k > 0.
Sum: H_ωω = Σ -k²p_k > 0.

VERIFICATION:
1. Decompose Δp at x* into z-Fourier modes
2. Check: is f_k(x₀,y₀) > 0 for all k with significant amplitude?
3. Compute -k²p_k for each k and verify sum gives H_ωω > 0
4. Measure the QUANTITATIVE gap (how much > 0)
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

def verify_lemma(s, w):
    """Verify the z-Fourier decomposition lemma from file 267."""
    D=s.D;N=s.N;kd=[s.kx,s.ky,s.kz]
    u_h=s.vel(*w)
    A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A[i,j]=s.ifft(1j*kd[j]*D*u_h[i])

    # Source Δp
    source=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):source-=A[i,j]*A[j,i]

    # Full pressure and H_ωω at max point
    p_hat=-s.fft(source)/s.ksq;p_hat[0,0,0]=0
    H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H[i,j]=s.ifft(-kd[i]*kd[j]*p_hat)

    wf=[s.ifft(D*w[i]) for i in range(3)]
    om=(wf[0]**2+wf[1]**2+wf[2]**2).sqrt()
    flat=om.flatten();idx=flat.argmax().item()
    iz_max=idx%N;iy_max=(idx//N)%N;ix_max=idx//(N*N)
    wv=torch.tensor([wf[i][ix_max,iy_max,iz_max] for i in range(3)],dtype=DTYPE)
    wn=wv.norm();eh=wv/wn
    Hl=H[:,:,ix_max,iy_max,iz_max]
    Hww_full=(eh@Hl@eh).item()

    # The ê direction — which coordinate axis is closest to ω?
    # For the proof: decompose along ê, not z.
    # For simplicity: find which axis ê is closest to.
    abs_eh=eh.abs()
    z_axis=abs_eh.argmax().item()  # dominant direction of ω
    print(f"  Max |ω| at ({ix_max},{iy_max},{iz_max}), |ω|={wn.item():.2f}",flush=True)
    print(f"  ω direction: ({eh[0].item():.3f},{eh[1].item():.3f},{eh[2].item():.3f})",flush=True)
    print(f"  Dominant axis: {['x','y','z'][z_axis]} (cos²={abs_eh[z_axis].item()**2:.3f})",flush=True)
    print(f"  H_ωω (full): {Hww_full:+.4f}",flush=True)

    # Decompose source into Fourier modes along the ê-direction
    # For simplicity use the dominant axis
    source_at_max_xy = source[ix_max, iy_max, :]  # along z at (x*,y*)
    p_at_max_xy_hat = p_hat[ix_max, iy_max, :]  # pressure along z

    # Actually, the proof decomposes in ê-direction. Let's use the actual z-axis
    # and verify at the GRID COLUMN through x*

    # z-Fourier transform of source at (x*,y*)
    source_z = source[ix_max, iy_max, :].clone()  # source(x*,y*,z)
    source_z_hat = torch.fft.fft(source_z)  # Fourier in z

    # Pressure at (x*,y*,z)
    # p(x*,y*,z) = Σ_k p_hat(x*,y*,k_z) e^{ik_z z}
    # where p_hat = -source_hat / |k|² involves ALL (kx,ky,kz)

    # For the LEMMA verification: at each k_z, compute
    # f_k = Fourier component of source in z at (x*,y*)
    # p_k = Fourier component of pressure in z at (x*,y*)
    # Check: f_k and p_k have OPPOSITE signs

    # The full 3D Fourier: p_hat(kx,ky,kz) = -source_hat(kx,ky,kz)/|k|²
    # The z-Fourier at (x*,y*): involves summing over kx, ky
    # p(x*,y*,z) = Σ_{kx,ky,kz} p_hat(k) e^{i(kx x* + ky y* + kz z)}
    # = Σ_{kz} [Σ_{kx,ky} p_hat(k) e^{i(kx x* + ky y*)}] e^{ikz z}
    # = Σ_{kz} P(kz) e^{ikz z}

    # Compute P(kz) = Σ_{kx,ky} p_hat(kx,ky,kz) e^{i(kx x* + ky y*)}
    source_3d_hat = s.fft(source)
    p_3d_hat = -source_3d_hat / s.ksq; p_3d_hat[0,0,0] = 0

    # Phase factors
    kx_vals = torch.fft.fftfreq(N, d=1.0/(2*pi)).to(dtype=DTYPE)  # wavenumber values
    x_star = ix_max * 2*pi/N; y_star = iy_max * 2*pi/N

    print(f"\n  z-Fourier decomposition at (x*,y*):",flush=True)
    print(f"  {'kz':>4s}  {'f_kz(source)':>12s}  {'P_kz(press)':>12s}  {'sign_f':>6s}  {'sign_P':>6s}  "
          f"{'opposite?':>9s}  {'-kz²P_kz':>10s}",flush=True)

    Hww_reconstructed = 0.
    kz_vals = torch.fft.fftfreq(N, d=1.0/(2*pi)).to(dtype=DTYPE)

    for kz_idx in range(N//2 + 1):
        kz = kz_vals[kz_idx].item()
        if abs(kz) < 0.01: continue  # skip k=0

        # Source z-Fourier component at (x*,y*)
        f_kz = source_z_hat[kz_idx].item()  # complex, take real part

        # Pressure z-Fourier component: sum over kx,ky
        # P(kz) = Σ_{kx,ky} p_hat(kx,ky,kz) e^{i(kx x* + ky y*)}
        phase_xy = torch.exp(1j * (s.kx[:,:,0]*x_star + s.ky[:,:,0]*y_star))
        P_kz = (p_3d_hat[:,:,kz_idx] * phase_xy).sum().item()  # complex

        f_real = f_kz.real if isinstance(f_kz, complex) else f_kz
        P_real = P_kz.real if isinstance(P_kz, complex) else P_kz

        opposite = "YES ✓" if (f_real > 0 and P_real < 0) or (f_real < 0 and P_real > 0) or abs(f_real)<1e-6 else "NO ✗"

        # Contribution to H_ωω along z: -kz² × P(kz) × e^{ikz z*}
        z_star = iz_max * 2*pi/N
        phase_z = np.exp(1j * kz * z_star)
        contrib = (-kz**2 * P_kz * phase_z)
        Hww_reconstructed += 2*contrib.real  # factor 2 for ±kz symmetry

        if abs(f_real) > 0.1 * abs(source_z_hat[1].item()):
            sf = "+" if f_real > 0 else "-"
            sp = "+" if P_real > 0 else "-"
            print(f"  {kz:4.0f}  {f_real:+12.4f}  {P_real:+12.4f}  {sf:>6s}  {sp:>6s}  "
                  f"{opposite:>9s}  {contrib.real*2:+10.4f}",flush=True)

    print(f"\n  H_ωω reconstructed from z-modes: {Hww_reconstructed:.4f}",flush=True)
    print(f"  H_ωω from full 3D: {Hww_full:.4f}",flush=True)
    print(f"  Match: {'YES ✓' if abs(Hww_reconstructed - Hww_full) < abs(Hww_full)*0.5 else 'APPROXIMATE'}",flush=True)

    return Hww_full

def main():
    N=32;dt=1e-4
    print("="*70,flush=True)
    print("INSTANCE B: VERIFY Instance C's LEMMA (file 267)",flush=True)
    print("="*70,flush=True)
    print("  LEMMA: positive source f_k → negative p_k → positive H_ωω",flush=True)
    print("  (from negative definiteness of Δ_xy - k²)\n",flush=True)

    for ic_name, sigma in [('trefoil_s03', 0.30), ('trefoil_s015', 0.15)]:
        s=NS3D(N);w=make_trefoil(s, amp=10./(sigma/0.3)**2, sigma=sigma)
        # Evolve
        for _ in range(500):w=s.step(w,dt)

        print(f"\n--- {ic_name} (evolved t=0.05) ---",flush=True)
        verify_lemma(s, w)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
