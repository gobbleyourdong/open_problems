"""
Cross-check the -Ω² dominance on ALL available ICs.
Also validate perturbation theory against finite-difference dc₃.

ICs to test:
1. Taylor-Green (done, repeat for validation)
2. Kida-Pelz (done, repeat)
3. ABC flow (A=1, B=0.8, C=0.6)
4. Perturbed ABC (breaks Beltrami)
5. Colliding vortex rings
6. Curl noise (random, broadband)
7. Trefoil knot

Also: sanity check that perturbation theory matches finite differences.
"""
import torch
import numpy as np
import math
import sys

DTYPE = torch.float64
pi = math.pi


class NS3D:
    def __init__(s, N=32, nu=0.):
        s.N=N; s.nu=nu; s.Lx=2*pi; dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2; s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def fft(s,f): return torch.fft.fftn(f)
    def ifft(s,f): return torch.fft.ifftn(f).real
    def curl(s,a,b,c):
        I=1j; return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq; p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j; return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D; u=s.vel(*w)
        f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]): f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c): return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        return tuple(s.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)]; return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()


def make_ic(solver, name):
    s = solver
    X, Y, Z = s.X, s.Y, s.Z

    if name == 'TG':
        ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
        uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        uz = torch.zeros_like(X)
        return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))

    elif name == 'KP':
        ux = torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
        uy = torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
        uz = torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))
        return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))

    elif name == 'ABC':
        A, B, C = 1.0, 0.8, 0.6
        ux = A*torch.sin(Z) + C*torch.cos(Y)
        uy = B*torch.sin(X) + A*torch.cos(Z)
        uz = C*torch.sin(Y) + B*torch.cos(X)
        return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))

    elif name == 'ABC_pert':
        # ABC + random perturbation to break Beltrami
        w = list(make_ic(s, 'ABC'))
        torch.manual_seed(42)
        N = s.N
        for comp in range(3):
            noise = torch.randn(N, N, N, dtype=DTYPE) * 0.3
            noise_h = s.fft(noise) * s.D
            # Keep only k=2-4
            mask = ((s.ksq.sqrt() >= 2) & (s.ksq.sqrt() <= 4)).to(DTYPE)
            w[comp] = w[comp] + noise_h * mask
        # Project to div-free
        wh = tuple(w)
        kdotw = s.kx*wh[0] + s.ky*wh[1] + s.kz*wh[2]
        w = list(wh)
        w[0] = w[0] - s.kx*kdotw/s.ksq
        w[1] = w[1] - s.ky*kdotw/s.ksq
        w[2] = w[2] - s.kz*kdotw/s.ksq
        w[0][0,0,0]=0; w[1][0,0,0]=0; w[2][0,0,0]=0
        return tuple(w)

    elif name == 'rings':
        # Colliding vortex rings
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        R, sep, amp, sigma = 0.8, 1.5, 5.0, 0.3
        for sign in [+1, -1]:
            z0 = pi + sign * sep
            rho = ((X - pi)**2 + (Y - pi)**2).sqrt()
            core_dist = ((rho - R)**2 + (Z - z0)**2).sqrt()
            strength = amp * torch.exp(-core_dist**2 / (2*sigma**2))
            theta_x = -(Y - pi) / (rho + 1e-10)
            theta_y = (X - pi) / (rho + 1e-10)
            wx += sign * strength * theta_x
            wy += sign * strength * theta_y
        wh = (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))
        return wh

    elif name == 'curl_noise':
        torch.manual_seed(123)
        N = s.N
        Ah = [torch.zeros(N,N,N,dtype=torch.complex128) for _ in range(3)]
        for oct in range(3):
            freq = 2**oct; amp_oct = 5.0 / (2**oct)
            klo, khi = max(1, freq-1), freq*2
            for i in range(-khi,khi+1):
                for j in range(-khi,khi+1):
                    for k in range(-khi,khi+1):
                        q=i*i+j*j+k*k
                        if q<klo**2 or q>khi**2: continue
                        mag = amp_oct/(q+1)
                        ii,jj,kk = i%N,j%N,k%N
                        for a in Ah:
                            a[ii,jj,kk] += mag*(torch.randn(1)+1j*torch.randn(1)).item()
        I=1j
        ux=I*s.ky*Ah[2]-I*s.kz*Ah[1]; uy=I*s.kz*Ah[0]-I*s.kx*Ah[2]; uz=I*s.kx*Ah[1]-I*s.ky*Ah[0]
        return s.curl(ux, uy, uz)

    elif name == 'trefoil':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        amp, sigma = 10.0, 0.3
        n_pts = 200
        t_param = torch.linspace(0, 2*pi, n_pts, dtype=DTYPE)
        cx = (torch.sin(t_param) + 2*torch.sin(2*t_param)) * 0.5 + pi
        cy = (torch.cos(t_param) - 2*torch.cos(2*t_param)) * 0.5 + pi
        cz = (-torch.sin(3*t_param)) * 0.5 + pi
        tx = torch.cos(t_param) + 4*torch.cos(2*t_param)
        ty = -torch.sin(t_param) + 4*torch.sin(2*t_param)
        tz = -3*torch.cos(3*t_param)
        ds = 2*pi/n_pts
        for i in range(n_pts):
            dist_sq = (X-cx[i])**2 + (Y-cy[i])**2 + (Z-cz[i])**2
            g = amp * torch.exp(-dist_sq/(2*sigma**2)) * ds
            wx += g * tx[i]; wy += g * ty[i]; wz += g * tz[i]
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    else:
        raise ValueError(f"Unknown IC: {name}")


def analyze_decomp(solver, w, percentile=0.90, n_sample=500):
    """Compute dc₃ decomposition from -S², -Ω², -H."""
    D = solver.D; N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]

    u = solver.vel(*w)
    A = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): A[i,j] = solver.ifft(1j*kd[j]*D*u[i])
    S = 0.5*(A+A.transpose(0,1))
    Omega = 0.5*(A-A.transpose(0,1))

    wf = [solver.ifft(D*w[i]) for i in range(3)]
    om = (wf[0]**2+wf[1]**2+wf[2]**2).sqrt()

    # -S²
    nS2 = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3): nS2[i,j] -= S[i,k]*S[k,j]

    # -Ω²
    nO2 = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3): nO2[i,j] -= Omega[i,k]*Omega[k,j]

    # -H (full pressure)
    source = torch.zeros(N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): source -= A[i,j]*A[j,i]
    p_hat = -solver.fft(source)/solver.ksq; p_hat[0,0,0]=0
    nH = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    for i in range(3):
        for j in range(3): nH[i,j] = -solver.ifft(-kd[i]*kd[j]*p_hat)  # note: -H

    thr = torch.quantile(om.flatten(), percentile)
    if thr < 1e-10: return None

    idx = (om > thr).nonzero(as_tuple=False)
    n = min(len(idx), n_sample)
    perm = torch.randperm(len(idx))[:n]; pts = idx[perm]

    res = {'dc3_S2':[], 'dc3_O2':[], 'dc3_H':[], 'c3':[], 'c1':[], 'alpha':[]}

    for pt in pts:
        ix,iy,iz = pt[0].item(), pt[1].item(), pt[2].item()
        Sl = S[:,:,ix,iy,iz]; ev,ec = torch.linalg.eigh(Sl)
        e3,e2,e1 = ec[:,0],ec[:,1],ec[:,2]

        wv = torch.tensor([wf[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn = wv.norm()
        if wn < 1e-12: continue
        eh = wv/wn

        c3 = (eh@e3).item()**2; c1 = (eh@e1).item()**2
        alpha = sum(ev[j].item()*(eh@ec[:,j]).item()**2 for j in range(3))

        for name, dS_tensor in [('S2', nS2), ('O2', nO2), ('H', nH)]:
            dS = dS_tensor[:,:,ix,iy,iz]
            dc3 = 0.0
            for i_idx, (e_i, lam_i) in enumerate([(e1, ev[2]), (e2, ev[1])]):
                lam_diff = ev[0].item() - lam_i.item()
                if abs(lam_diff) < 1e-12: continue
                coupling = (e_i @ dS @ e3).item()
                dc3 += 2*(eh@e3).item()*(eh@e_i).item()*coupling/lam_diff
            res[f'dc3_{name}'].append(dc3)

        res['c3'].append(c3); res['c1'].append(c1); res['alpha'].append(alpha)

    for k in res: res[k] = np.array(res[k])
    return res


def main():
    N = 32; dt = 2e-4

    print("="*70, flush=True)
    print("CROSS-CHECK: -Ω² dominance across ALL IC types", flush=True)
    print("="*70, flush=True)

    ics = ['TG', 'KP', 'ABC', 'ABC_pert', 'rings', 'curl_noise', 'trefoil']
    evolve_steps = {
        'TG': 500, 'KP': 500, 'ABC': 500, 'ABC_pert': 500,
        'rings': 500, 'curl_noise': 300, 'trefoil': 300
    }

    print(f"\n{'IC':>12s}  {'|ω|₀':>6s}  {'|ω|_T':>6s}  {'c₃':>5s}  {'c₁':>5s}  "
          f"{'α':>7s}  {'dc₃(-Ω²)':>10s}  {'dc₃(-H)':>10s}  {'dc₃(-S²)':>10s}  "
          f"{'Ω²/H':>5s}  {'Ω²>0':>5s}", flush=True)
    print("-"*110, flush=True)

    for ic_name in ics:
        s = NS3D(N, 0.0)
        try:
            w = make_ic(s, ic_name)
        except Exception as e:
            print(f"  {ic_name:>12s}: ERROR creating IC: {e}", flush=True)
            continue

        om0 = s.om_max(w)

        # Evolve
        n_steps = evolve_steps.get(ic_name, 500)
        t = 0.0
        for step in range(n_steps):
            w = s.step(w, dt)
            t += dt

        om = s.om_max(w)
        r = analyze_decomp(s, w)

        if r is None or len(r['c3']) == 0:
            print(f"  {ic_name:>12s}: |ω|₀={om0:.1f}→{om:.1f}  INSUFFICIENT DATA", flush=True)
            continue

        dc_o = r['dc3_O2']
        dc_h = r['dc3_H']
        dc_s = r['dc3_S2']

        ratio = abs(dc_o.mean()) / (abs(dc_h.mean()) + 1e-30)
        pct_pos = (dc_o > 0).mean() * 100

        print(f"  {ic_name:>12s}  {om0:6.1f}  {om:6.1f}  {r['c3'].mean():5.3f}  "
              f"{r['c1'].mean():5.3f}  {r['alpha'].mean():7.4f}  "
              f"{dc_o.mean():+10.4f}  {dc_h.mean():+10.4f}  {dc_s.mean():+10.4f}  "
              f"{ratio:5.2f}  {pct_pos:5.0f}%", flush=True)

    # Now do time series for a couple of ICs to show it holds throughout evolution
    print(f"\n\n{'='*70}", flush=True)
    print("TIME SERIES: does -Ω² dominance persist throughout evolution?", flush=True)
    print(f"{'='*70}", flush=True)

    for ic_name in ['TG', 'KP', 'ABC_pert', 'curl_noise']:
        s = NS3D(N, 0.0)
        w = make_ic(s, ic_name)
        print(f"\n--- {ic_name} ---", flush=True)
        print(f"  {'t':>6s}  {'|ω|':>6s}  {'c₃':>5s}  {'dc₃(-Ω²)':>10s}  {'dc₃(-H)':>10s}  "
              f"{'ratio':>5s}  {'-Ω²>0':>6s}", flush=True)

        t = 0.0
        for epoch in range(8):
            for _ in range(100):
                w = s.step(w, dt)
                t += dt

            om = s.om_max(w)
            r = analyze_decomp(s, w)
            if r is None or len(r['c3']) == 0: continue

            dc_o = r['dc3_O2']; dc_h = r['dc3_H']
            ratio = abs(dc_o.mean())/(abs(dc_h.mean())+1e-30)
            pct = (dc_o > 0).mean()*100

            print(f"  {t:6.3f}  {om:6.2f}  {r['c3'].mean():5.3f}  "
                  f"{dc_o.mean():+10.4f}  {dc_h.mean():+10.4f}  "
                  f"{ratio:5.2f}  {pct:5.0f}%", flush=True)

    # SANITY CHECK: validate perturbation theory against finite differences
    print(f"\n\n{'='*70}", flush=True)
    print("SANITY CHECK: perturbation theory vs finite-difference dc₃", flush=True)
    print(f"{'='*70}", flush=True)

    s = NS3D(N, 0.0)
    w = make_ic(s, 'TG')
    # Evolve to t=0.05
    for _ in range(250): w = s.step(w, dt)

    # Save state
    w0 = tuple(wi.clone() for wi in w)

    # Get perturbation theory prediction
    r0 = analyze_decomp(s, w0, n_sample=200)
    pert_total = r0['dc3_S2'] + r0['dc3_O2'] + r0['dc3_H']

    # Evolve one more small step for finite difference
    dt_fd = 50 * dt  # 50 steps
    w1 = tuple(wi.clone() for wi in w0)
    for _ in range(50): w1 = s.step(w1, dt)

    # Compute c₃ at both times using the SAME grid points
    D = s.D
    wf0 = [s.ifft(D*w0[i]) for i in range(3)]
    S0 = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    u0 = s.vel(*w0)
    kd = [s.kx, s.ky, s.kz]
    for i in range(3):
        for j in range(3):
            A_ij = s.ifft(1j*kd[j]*D*u0[i])
            S0[i,j] = 0.5*(A_ij + s.ifft(1j*kd[i]*D*u0[j]))

    wf1 = [s.ifft(D*w1[i]) for i in range(3)]
    S1 = torch.zeros(3,3,N,N,N,dtype=DTYPE)
    u1 = s.vel(*w1)
    for i in range(3):
        for j in range(3):
            A_ij = s.ifft(1j*kd[j]*D*u1[i])
            S1[i,j] = 0.5*(A_ij + s.ifft(1j*kd[i]*D*u1[j]))

    om0_field = (wf0[0]**2+wf0[1]**2+wf0[2]**2).sqrt()
    thr = torch.quantile(om0_field.flatten(), 0.90)
    idx = (om0_field > thr).nonzero(as_tuple=False)
    n = min(200, len(idx))
    perm = torch.randperm(len(idx))[:n]; pts = idx[perm]

    fd_dc3 = []
    pt_dc3 = []
    for pi_idx, pt in enumerate(pts):
        ix,iy,iz = pt[0].item(), pt[1].item(), pt[2].item()

        wv0 = torch.tensor([wf0[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn0 = wv0.norm()
        if wn0 < 1e-12: continue
        eh0 = wv0/wn0

        ev0, ec0 = torch.linalg.eigh(S0[:,:,ix,iy,iz])
        c3_0 = (eh0 @ ec0[:,0]).item()**2

        wv1 = torch.tensor([wf1[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn1 = wv1.norm()
        if wn1 < 1e-12: continue
        eh1 = wv1/wn1

        ev1, ec1 = torch.linalg.eigh(S1[:,:,ix,iy,iz])
        e3_1 = ec1[:,0]
        if (e3_1 @ ec0[:,0]).item() < 0: e3_1 = -e3_1
        c3_1 = (eh1 @ e3_1).item()**2

        fd = (c3_1 - c3_0) / dt_fd
        fd_dc3.append(fd)

        if pi_idx < len(pert_total):
            pt_dc3.append(pert_total[pi_idx])

    fd_dc3 = np.array(fd_dc3)
    pt_dc3 = np.array(pt_dc3[:len(fd_dc3)])

    print(f"\n  Finite difference dc₃/dt: mean={fd_dc3.mean():.4f} std={fd_dc3.std():.4f}", flush=True)
    print(f"  Perturbation theory:      mean={pt_dc3.mean():.4f} std={pt_dc3.std():.4f}", flush=True)
    corr = np.corrcoef(fd_dc3[:len(pt_dc3)], pt_dc3)[0,1] if len(pt_dc3) > 1 else 0
    print(f"  Correlation: {corr:.4f}", flush=True)
    print(f"  Sign agreement: {(np.sign(fd_dc3[:len(pt_dc3)]) == np.sign(pt_dc3)).mean()*100:.0f}%", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
