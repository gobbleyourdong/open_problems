"""N=128 sign flip test — overnight run. Results saved locally."""
import numpy as np, time, json

N=128; L=2*np.pi; dx=L/N; nu=1e-4
k1d=np.fft.fftfreq(N,d=dx/(2*np.pi))
kx,ky,kz=np.meshgrid(k1d,k1d,k1d,indexing='ij')
ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0; kmag=np.sqrt(ksq)
ikx,iky,ikz=1j*kx,1j*ky,1j*kz
kmax=N//3; D=((np.abs(kx)<kmax)&(np.abs(ky)<kmax)&(np.abs(kz)<kmax)).astype(np.float64)
ifft=lambda f:np.fft.ifftn(f*D).real; fft=np.fft.fftn

shells=[]
for j in range(int(np.log2(kmax))+2):
    m=((kmag<2) if j==0 else ((kmag>=2**j)&(kmag<2**(j+1)))).astype(np.float64)*D
    shells.append((m,int(m.sum())))
print(f'N={N}, kmax={kmax}',flush=True)
for j,(m,nm) in enumerate(shells):
    if nm>0: print(f'  j={j}: {nm} modes',flush=True)

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

def measure_sign(wh, target_t):
    wx_h,wy_h,wz_h=wh
    px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq;px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
    ux_h_v=iky*pz-ikz*py;uy_h_v=ikz*px-ikx*pz;uz_h_v=ikx*py-iky*px
    wx_f=ifft(wx_h*D);wy_f=ifft(wy_h*D);wz_f=ifft(wz_h*D)
    gxx=ifft(ikx*ux_h_v*D);gxy=ifft(iky*ux_h_v*D);gxz=ifft(ikz*ux_h_v*D)
    gyx=ifft(ikx*uy_h_v*D);gyy=ifft(iky*uy_h_v*D);gyz=ifft(ikz*uy_h_v*D)
    gzx=ifft(ikx*uz_h_v*D);gzy=ifft(iky*uz_h_v*D);gzz=ifft(ikz*uz_h_v*D)
    stretch_x=wx_f*gxx+wy_f*gyx+wz_f*gzx
    stretch_y=wx_f*gxy+wy_f*gyy+wz_f*gzy
    stretch_z=wx_f*gxz+wy_f*gyz+wz_f*gzz
    omag=np.sqrt(wx_f**2+wy_f**2+wz_f**2).max()
    row = {'t': target_t, 'omega_max': float(omag), 'signs': {}}
    for j in range(1,6):
        mj,nm=shells[j]
        if nm<10: continue
        wj=[ifft(c*mj) for c in [wx_h,wy_h,wz_h]]
        sj=[ifft(D*mj*fft(stretch_x)),ifft(D*mj*fft(stretch_y)),ifft(D*mj*fft(stretch_z))]
        S_field=sum(wj[c]*sj[c] for c in range(3))
        S_total=S_field.sum()*dx**3
        low_mask=(kmag<2**j).astype(np.float64)*D
        u_low=[ifft(c*low_mask) for c in [ux_h_v,uy_h_v,uz_h_v]]
        u_mag=np.sqrt(sum(u_low[c]**2 for c in range(3)))
        U_rms=np.sqrt(np.mean(u_mag**2))
        if U_rms<1e-10: continue
        res=(u_mag<0.5*U_rms)
        S_res=(S_field*res).sum()*dx**3
        sign = '+' if S_res>=0 else '-'
        row['signs'][str(j)] = {'S_res': float(S_res), 'S_total': float(S_total), 'sign': sign}
        print(f'  j={j}: S_res={S_res:+.3e} S_total={S_total:+.3e} [{sign}]', flush=True)
    return row

x=np.linspace(0,L-dx,N);X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
ux0=np.cos(X)*np.sin(Y)*np.cos(Z);uy0=-np.sin(X)*np.cos(Y)*np.cos(Z);uz0=np.zeros_like(X)
ux_h=D*fft(ux0);uy_h=D*fft(uy0);uz_h=D*fft(uz0)
wh=[D*(iky*uz_h-ikz*uy_h),D*(ikz*ux_h-ikx*uz_h),D*(ikx*uy_h-iky*ux_h)]

dt=0.001; results=[]; t0=time.time()
for target_t in [2,3,4,5,6,7,8]:
    prev_t = 0 if target_t==2 else target_t-1
    steps=int((target_t-prev_t)/dt)
    print(f'\nEvolving to t={target_t}...', flush=True)
    for step in range(steps): wh=rk4(wh,dt)
    elapsed=time.time()-t0
    print(f't={target_t}, elapsed={elapsed:.0f}s', flush=True)
    row = measure_sign(wh, target_t)
    results.append(row)
    # Save after each snapshot (in case container dies)
    with open('/workspace/ns_blowup/results/sign_flip_n128.json','w') as f:
        json.dump(results,f,indent=2)
    print(f'Saved {len(results)} snapshots to sign_flip_n128.json', flush=True)

print(f'\nDone in {time.time()-t0:.0f}s', flush=True)
