"""Verify: straight Lamb-Oseen tube has ratio = 1.0 exactly."""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

N=32; L=2*pi; dx=L/N
x=torch.linspace(0,L-dx,N,dtype=DTYPE)
X,Y,Z=torch.meshgrid(x,x,x,indexing='ij')
k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
ksq=kx**2+ky**2+kz**2;ksq[0,0,0]=1
D=((kx.abs()<N//3)&(ky.abs()<N//3)&(kz.abs()<N//3)).to(DTYPE)
F=torch.fft.fftn;iF=lambda f:torch.fft.ifftn(f).real

# Straight tube along z
sigma=0.4; omega0=10.0
r_sq=(X-pi)**2+(Y-pi)**2
wz=omega0*torch.exp(-r_sq/(2*sigma**2))
wx=torch.zeros_like(X);wy=torch.zeros_like(X)
wh=(D*F(wx),D*F(wy),D*F(wz))

# Velocity via Biot-Savart
def vel(wh):
    p=[wh[i]/ksq for i in range(3)]
    for i in range(3):p[i][0,0,0]=0
    I=1j
    return(I*ky*p[2]-I*kz*p[1],I*kz*p[0]-I*kx*p[2],I*kx*p[1]-I*ky*p[0])

uh=vel(wh)
kd=[kx,ky,kz]

# Pressure Hessian
A=torch.zeros(3,3,N,N,N,dtype=DTYPE)
for i in range(3):
    for j in range(3):A[i,j]=iF(1j*kd[j]*D*[uh[0],uh[1],uh[2]][i])
source=torch.zeros(N,N,N,dtype=DTYPE)
for i in range(3):
    for j in range(3):source-=A[i,j]*A[j,i]
p_hat=-F(source)/ksq;p_hat[0,0,0]=0
H=torch.zeros(3,3,N,N,N,dtype=DTYPE)
for i in range(3):
    for j in range(3):H[i,j]=iF(-kd[i]*kd[j]*p_hat)

# At the center (pi,pi,pi) = grid point (N//2, N//2, N//2)
ix=iy=N//2; iz=N//2
om_at=wz[ix,iy,iz].item()
Hl=H[:,:,ix,iy,iz]
trH=Hl.trace().item()
Hzz=Hl[2,2].item()
Hxx=Hl[0,0].item()

eh=torch.tensor([0.,0.,1.],dtype=DTYPE)
Hww=(eh@Hl@eh).item()
Hiso=trH/3
Hdev=Hww-Hiso
ratio=abs(Hdev)/(abs(Hiso)+1e-30)

print(f"Straight Lamb-Oseen tube: sigma={sigma}, omega0={omega0}",flush=True)
print(f"  |omega| at center = {om_at:.4f}",flush=True)
print(f"  Dp = source at center = {source[ix,iy,iz].item():.4f}",flush=True)
print(f"  H_xx = {Hxx:.6f}",flush=True)
print(f"  H_zz = H_ww = {Hzz:.6f}",flush=True)
print(f"  tr(H) = {trH:.6f}",flush=True)
print(f"  H_iso = Dp/3 = {Hiso:.6f}",flush=True)
print(f"  H_dev,ww = {Hdev:.6f}",flush=True)
print(f"  Ratio |H_dev|/|H_iso| = {ratio:.6f}",flush=True)
print(f"  PREDICTED: 1.000000",flush=True)
print(f"  MATCH: {'YES' if abs(ratio-1.0)<0.05 else 'NO'} (diff={abs(ratio-1):.6f})",flush=True)

# Now add slight curvature (sinusoidal perturbation in z)
print(f"\n--- With z-perturbation (curvature) ---",flush=True)
for eps in [0.0, 0.01, 0.05, 0.1, 0.3]:
    wz_p = omega0*torch.exp(-r_sq/(2*sigma**2)) * (1 + eps*torch.cos(Z))
    wh_p=(D*F(wx),D*F(wy),D*F(wz_p))
    uh_p=vel(wh_p)
    A_p=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):A_p[i,j]=iF(1j*kd[j]*D*[uh_p[0],uh_p[1],uh_p[2]][i])
    src_p=torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):src_p-=A_p[i,j]*A_p[j,i]
    ph_p=-F(src_p)/ksq;ph_p[0,0,0]=0
    H_p=torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):H_p[i,j]=iF(-kd[i]*kd[j]*ph_p)
    Hl_p=H_p[:,:,ix,iy,iz]
    trHp=Hl_p.trace().item();Hwwp=(eh@Hl_p@eh).item()
    Hiso_p=trHp/3;Hdev_p=Hwwp-Hiso_p
    ratio_p=abs(Hdev_p)/(abs(Hiso_p)+1e-30)
    print(f"  eps={eps:.2f}: H_zz={Hl_p[2,2].item():+.4f}  ratio={ratio_p:.4f}  "
          f"{'<1 ✓' if ratio_p<1 else '=1'}",flush=True)
