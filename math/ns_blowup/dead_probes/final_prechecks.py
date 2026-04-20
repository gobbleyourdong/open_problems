"""
Final pre-H200 checks:
1. Half-timestep test — method independence
2. Same-seed convergence — |omega|_max(t) curves across N
"""
import torch
import math
import time
import json
import os
import numpy as np


def make_solver(N, nu, device):
    Lx = 2*math.pi; dx = Lx/N
    k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=torch.float64)
    kx,ky,kz = torch.meshgrid(k,k,k,indexing='ij')
    ksq = kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    ikx,iky,ikz = 1j*kx,1j*ky,1j*kz
    kmax = N//3
    D = ((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
    return kx,ky,kz,ksq,ikx,iky,ikz,D,dx


def make_ic(N, seed, kx,ky,kz,ksq,ikx,iky,ikz,D, device):
    torch.manual_seed(seed)
    mag = 10.0/(ksq+1); mag[0,0,0]=0
    ic_mask = ksq <= 64
    Ax=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
    Ay=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
    Az=mag*ic_mask*(torch.randn(N,N,N,device=device)+1j*torch.randn(N,N,N,device=device))
    ux_h=iky*Az-ikz*Ay;uy_h=ikz*Ax-ikx*Az;uz_h=ikx*Ay-iky*Ax
    wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)
    return wx_h,wy_h,wz_h


def ns_rhs(wx_h,wy_h,wz_h, kx,ky,kz,ksq,ikx,iky,ikz,D, nu):
    ifft=lambda f:torch.fft.ifftn(f*D).real
    fft=torch.fft.fftn
    px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
    px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
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
    return(D*fft(sx-ax)-nu*ksq*wx_h,D*fft(sy-ay)-nu*ksq*wy_h,D*fft(sz-az)-nu*ksq*wz_h)


def rk4(wx_h,wy_h,wz_h,dt, kx,ky,kz,ksq,ikx,iky,ikz,D, nu):
    def add(a,b,s):return(a[0]+s*b[0],a[1]+s*b[1],a[2]+s*b[2])
    rhs=lambda *w: ns_rhs(*w, kx,ky,kz,ksq,ikx,iky,ikz,D, nu)
    w=(wx_h,wy_h,wz_h)
    k1=rhs(*w);k2=rhs(*add(w,k1,.5*dt));k3=rhs(*add(w,k2,.5*dt));k4=rhs(*add(w,k3,dt))
    return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
           wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
           wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))


def omega_max(wx_h,wy_h,wz_h):
    wx=torch.fft.ifftn(wx_h).real;wy=torch.fft.ifftn(wy_h).real;wz=torch.fft.ifftn(wz_h).real
    return (wx**2+wy**2+wz**2).sqrt().max().item()


def run_trajectory(N, nu, seed, dt, n_steps, device):
    """Run one trajectory, return list of |omega|_max at each checkpoint."""
    kx,ky,kz,ksq,ikx,iky,ikz,D,dx = make_solver(N, nu, device)
    wx_h,wy_h,wz_h = make_ic(N, seed, kx,ky,kz,ksq,ikx,iky,ikz,D, device)

    traj = []
    times = []
    t = 0.0

    for step in range(n_steps+1):
        if step % 100 == 0:
            om = omega_max(wx_h,wy_h,wz_h)
            traj.append(om)
            times.append(t)
        if step < n_steps:
            wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt, kx,ky,kz,ksq,ikx,iky,ikz,D, nu)
            t += dt

    return times, traj


def main():
    device = 'cuda'
    nu = 1e-4
    seed = 0

    print("=" * 60)
    print("TEST 1: HALF-TIMESTEP METHOD INDEPENDENCE")
    print("N=64, nu=1e-4, seed=0, compare dt=0.005 vs dt=0.0025")
    print("=" * 60, flush=True)

    t0 = time.time()

    times1, traj1 = run_trajectory(64, nu, seed, dt=0.005, n_steps=2000, device=device)
    peak1 = max(traj1)
    ratio1 = peak1 / traj1[0]

    times2, traj2 = run_trajectory(64, nu, seed, dt=0.0025, n_steps=4000, device=device)
    peak2 = max(traj2)
    ratio2 = peak2 / traj2[0]

    elapsed = time.time() - t0
    print(f"  dt=0.005:  peak_ratio = {ratio1:.8f}", flush=True)
    print(f"  dt=0.0025: peak_ratio = {ratio2:.8f}", flush=True)
    print(f"  Difference: {abs(ratio1-ratio2):.2e}", flush=True)

    if abs(ratio1-ratio2) < 0.001:
        print(f"  PASS: Result is dt-INDEPENDENT [{elapsed:.0f}s]", flush=True)
    else:
        print(f"  CONCERN: Result depends on dt [{elapsed:.0f}s]", flush=True)

    print()
    print("=" * 60)
    print("TEST 2: SAME-SEED CONVERGENCE ACROSS RESOLUTIONS")
    print("seed=0, nu=1e-4, dt=0.005, N=16,32,64,128")
    print("=" * 60, flush=True)

    convergence = {}

    for N in [16, 32, 64, 128]:
        t0 = time.time()
        steps = 2000
        if N == 128:
            steps = 1000  # shorter for speed

        times_n, traj_n = run_trajectory(N, nu, seed, dt=0.005, n_steps=steps, device=device)
        peak = max(traj_n)
        ratio = peak / traj_n[0]
        elapsed = time.time() - t0

        convergence[N] = {
            'times': times_n[:11],  # first 11 checkpoints
            'traj': traj_n[:11],
            'peak_ratio': ratio,
            'om0': traj_n[0],
        }

        print(f"  N={N:3d}: om0={traj_n[0]:.6f} peak_ratio={ratio:.8f} [{elapsed:.0f}s]", flush=True)

    print()
    print("CONVERGENCE TABLE:", flush=True)
    print(f"  {'N':>4} {'|ω|_max(0)':>12} {'peak_ratio':>12}", flush=True)
    for N in [16,32,64,128]:
        c = convergence[N]
        print(f"  {N:4d} {c['om0']:12.6f} {c['peak_ratio']:12.8f}", flush=True)

    print()
    # Check: do the trajectories converge?
    # Compare |omega|_max at same physical time across N
    print("TIME SERIES COMPARISON (t=0 to t=5):", flush=True)
    print(f"  {'t':>6} {'N=16':>10} {'N=32':>10} {'N=64':>10} {'N=128':>10}", flush=True)
    for i in range(min(11, len(convergence[16]['traj']))):
        t_val = convergence[16]['times'][i]
        vals = []
        for N in [16,32,64,128]:
            if i < len(convergence[N]['traj']):
                vals.append(f"{convergence[N]['traj'][i]:.6f}")
            else:
                vals.append("--")
        print(f"  {t_val:6.2f} {vals[0]:>10} {vals[1]:>10} {vals[2]:>10} {vals[3]:>10}", flush=True)

    # Save
    results = {
        'test1_dt_independence': {
            'dt_005': ratio1,
            'dt_0025': ratio2,
            'difference': abs(ratio1-ratio2),
            'pass': abs(ratio1-ratio2) < 0.001,
        },
        'test2_convergence': {str(N): {
            'om0': convergence[N]['om0'],
            'peak_ratio': convergence[N]['peak_ratio'],
        } for N in [16,32,64,128]},
    }

    out = 'ns_blowup/results/final_prechecks.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}", flush=True)


if __name__ == '__main__':
    main()
