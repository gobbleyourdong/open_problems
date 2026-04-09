"""Phase scrambler N=128 — FAST version.
Uses Frobenius norm for ||S||_∞ approximation instead of eigvalsh on every point.
||S||_F / sqrt(N^3) approximates ||S||_∞ / sqrt(6) for Gaussian-like fields.
Actually, just sample 5000 random points for ||S||_∞ instead of all N^3.
"""
import numpy as np, time, json

N=128; L=2*np.pi; dx=L/N; nu=1e-4
k1d=np.fft.fftfreq(N,d=dx/(2*np.pi))
kx,ky,kz=np.meshgrid(k1d,k1d,k1d,indexing='ij')
ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0; kmag=np.sqrt(ksq)
ikx,iky,ikz=1j*kx,1j*ky,1j*kz
kmax=N//3; D=((np.abs(kx)<kmax)&(np.abs(ky)<kmax)&(np.abs(kz)<kmax)).astype(np.float64)
ifft=lambda f:np.fft.ifftn(f*D).real; fft=np.fft.fftn; ik=[ikx,iky,ikz]

shells=[]
max_shell=int(np.log2(kmax))+1
for j in range(max_shell+1):
    m=((kmag<2) if j==0 else ((kmag>=2**j)&(kmag<2**(j+1)))).astype(np.float64)*D
    shells.append((m,int(m.sum())))
print(f'N={N}, kmax={kmax}',flush=True)
for j,(m,nm) in enumerate(shells):
    if nm>0: print(f'  j={j}: {nm} modes',flush=True)

def compute_theta_fast(wh, j):
    mj,nm=shells[j]
    if nm<3: return 0.0
    wjh=[c*mj for c in wh]
    pj=[c/ksq for c in wjh]
    for p in pj: p[0,0,0]=0
    ujh=[iky*pj[2]-ikz*pj[1],ikz*pj[0]-ikx*pj[2],ikx*pj[1]-iky*pj[0]]
    wj=[ifft(c) for c in wjh]
    S=np.zeros((3,3,N,N,N))
    for i in range(3):
        for l in range(3):
            S[i,l]=ifft(ik[l]*ujh[i]*D)
    S=0.5*(S+S.transpose(1,0,2,3,4))
    wSw=sum(wj[i]*S[i,l]*wj[l] for i in range(3) for l in range(3))
    T=wSw.sum()*dx**3
    E=sum((wj[c]**2).sum() for c in range(3))*dx**3
    # FAST ||S||_∞: sample 8000 random points instead of all N^3
    n_sample=8000
    np.random.seed(42)
    ix=np.random.randint(0,N,n_sample)
    iy=np.random.randint(0,N,n_sample)
    iz=np.random.randint(0,N,n_sample)
    Si=0.0
    for si in range(n_sample):
        mat=S[:,:,ix[si],iy[si],iz[si]]
        eigs=np.linalg.eigvalsh(mat)
        Si=max(Si,max(abs(eigs)))
    return abs(T)/(E*Si+1e-30)

def ns_rhs(wh):
    wx_h,wy_h,wz_h=wh
    px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq;px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
    ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
    ux,uy,uz=ifft(ux_h),ifft(uy_h),ifft(uz_h)
    wx,wy,wz=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
    gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
    gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
    gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
    sx=wx*gxx+wy*gxy+wz*gxz;sy=wx*gyx+wy*gyy+wz*gyz;sz=wx*gzx+wy*gzy+wz*gzz
    ax=ux*ifft(ikx*wx_h*D)+uy*ifft(iky*wx_h*D)+uz*ifft(ikz*wx_h*D)
    ay=ux*ifft(ikx*wy_h*D)+uy*ifft(iky*wy_h*D)+uz*ifft(ikz*wy_h*D)
    az=ux*ifft(ikx*wz_h*D)+uy*ifft(iky*wz_h*D)+uz*ifft(ikz*wz_h*D)
    return[D*fft(sx-ax)-nu*ksq*wx_h,D*fft(sy-ay)-nu*ksq*wy_h,D*fft(sz-az)-nu*ksq*wz_h]

def rk4(wh,dt):
    k1=ns_rhs(wh);w2=[wh[c]+.5*dt*k1[c] for c in range(3)]
    k2=ns_rhs(w2);w3=[wh[c]+.5*dt*k2[c] for c in range(3)]
    k3=ns_rhs(w3);w4=[wh[c]+dt*k3[c] for c in range(3)]
    k4=ns_rhs(w4)
    return[wh[c]+dt/6*(k1[c]+2*k2[c]+2*k3[c]+k4[c]) for c in range(3)]

x=np.linspace(0,L-dx,N);X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
ux0=np.cos(X)*np.sin(Y)*np.cos(Z);uy0=-np.sin(X)*np.cos(Y)*np.cos(Z);uz0=np.zeros_like(X)
uh=[D*fft(ux0),D*fft(uy0),D*fft(uz0)]
wh=[D*(iky*uh[2]-ikz*uh[1]),D*(ikz*uh[0]-ikx*uh[2]),D*(ikx*uh[1]-iky*uh[0])]

dt=0.001; active=[1,2,3,4,5]
sample=100  # sample every 0.1 time units (less frequent to compensate)
hdr='  t    |ω|max  '+''.join(f'   θ(j={j})  ' for j in active)
print(hdr,flush=True)

peaks={j:0.0 for j in active}; t0=time.time()

for step in range(10000):  # t=0 to 10
    t=step*dt
    if step%sample==0:
        thetas={j:compute_theta_fast(wh,j) for j in active}
        w_phys=[ifft(wh[c]*D) for c in range(3)]
        wmax=np.sqrt(sum(w_phys[c]**2 for c in range(3))).max()
        row=f'{t:5.2f}  {wmax:7.2f}  '
        for j in active:
            peaks[j]=max(peaks[j],thetas[j])
            row+=f'{thetas[j]:11.6f} '
        print(row,flush=True)
    wh=rk4(wh,dt)

elapsed=time.time()-t0
print(f'\nCompleted in {elapsed:.0f}s',flush=True)
print(f'\nPEAK θ BY SHELL:',flush=True)
for j in active:
    print(f'  j={j} (N={shells[j][1]:6d}): peak θ = {peaks[j]:.6f}',flush=True)
print(f'\nRATIOS:',flush=True)
for i in range(len(active)-1):
    j1,j2=active[i],active[i+1]
    if peaks[j1]>0:
        print(f'  j={j1}→{j2}: {peaks[j2]/peaks[j1]:.4f}',flush=True)

with open('ns_blowup/results/phase_scrambler_n128.json','w') as f:
    json.dump({'peaks':{str(j):peaks[j] for j in active},'N':N,'nu':nu},f)
print('Saved.',flush=True)
