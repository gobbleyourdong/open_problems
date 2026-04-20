"""
Verify: the c₃ increase is driven by ROTATION of ω toward e₃.

Compute dc₃/dt numerically by finite differences at high-|ω| points.
Decompose: is c₃ increasing because ω rotates, or because S eigenvectors rotate?

At a point with ω and S:
  c₃ = cos²(ω, e₃) = (ω̂ · e₃)²

dc₃/dt = 2(ω̂ · e₃)(dω̂/dt · e₃ + ω̂ · de₃/dt)

So c₃ changes from two effects:
1. ω̂ rotates (dω̂/dt ≠ 0) — the vorticity direction changes
2. e₃ rotates (de₃/dt ≠ 0) — the strain eigenvectors change

Which one dominates?
"""
import torch
import numpy as np
import math
import sys

DTYPE = torch.float64
pi = math.pi


class NS3D:
    def __init__(self, N=32, nu=0.0):
        self.N = N; self.nu = nu; self.Lx = 2*pi
        dx = self.Lx/N
        x = torch.linspace(0, self.Lx-dx, N, dtype=DTYPE)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')
        k = torch.fft.fftfreq(N, d=dx/(2*pi)).to(dtype=DTYPE)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2; self.ksq[0,0,0] = 1
        self.D = ((self.kx.abs() < N//3) & (self.ky.abs() < N//3) &
                   (self.kz.abs() < N//3)).to(DTYPE)

    def fft(self, f): return torch.fft.fftn(f)
    def ifft(self, fh): return torch.fft.ifftn(fh).real
    def curl(self, a, b, c):
        I = 1j
        return (I*self.ky*c-I*self.kz*b, I*self.kz*a-I*self.kx*c, I*self.kx*b-I*self.ky*a)
    def vel(self, a, b, c):
        px=a/self.ksq;py=b/self.ksq;pz=c/self.ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        I=1j
        return (I*self.ky*pz-I*self.kz*py, I*self.kz*px-I*self.kx*pz, I*self.kx*py-I*self.ky*px)
    def rhs(self, w):
        D = self.D; u = self.vel(*w)
        f = {}
        for n, h in zip(['ux','uy','uz','wx','wy','wz'], [*u, *w]):
            f[n] = self.ifft(D*h)
            for d, kd in zip('xyz', [self.kx, self.ky, self.kz]):
                f[f'd{n}_d{d}'] = self.ifft(1j*kd*D*h)
        r = []
        for c in 'xyz':
            st = f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad = f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*self.fft(st-ad) - self.nu*self.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(self, w, dt):
        def add(a, b, c): return tuple(a[i]+c*b[i] for i in range(3))
        k1 = self.rhs(w); k2 = self.rhs(add(w,k1,.5*dt))
        k3 = self.rhs(add(w,k2,.5*dt)); k4 = self.rhs(add(w,k3,dt))
        return tuple(self.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
    def om_max(self, w):
        v = [self.ifft(w[i]) for i in range(3)]
        return (v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()


def get_fields(solver, w):
    """Extract physical-space fields and strain."""
    D = solver.D; N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]
    u = solver.vel(*w)

    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            A[i,j] = solver.ifft(1j * kd[j] * D * u[i])

    S = 0.5 * (A + A.transpose(0, 1))
    wf = [solver.ifft(D * w[i]) for i in range(3)]
    om = (wf[0]**2 + wf[1]**2 + wf[2]**2).sqrt()
    return wf, S, om


def measure_rotation(solver, w0, w1, dt_total, percentile=0.90, n_sample=500):
    """
    At top-|ω| points of w0, measure:
    - c₃ at time t (from w0)
    - c₃ at time t+dt (from w1)
    - dc₃/dt by finite difference
    - Decompose into ω-rotation and e₃-rotation contributions
    """
    wf0, S0, om0 = get_fields(solver, w0)
    wf1, S1, om1 = get_fields(solver, w1)

    thr = torch.quantile(om0.flatten(), percentile)
    if thr < 1e-10:
        return None

    N = solver.N
    mask = om0 > thr
    idx = mask.nonzero(as_tuple=False)
    n = min(len(idx), n_sample)
    perm = torch.randperm(len(idx))[:n]
    pts = idx[perm]

    results = {'dc3_dt': [], 'dc3_omega_rot': [], 'dc3_e3_rot': [],
               'c3_0': [], 'c1_0': [], 'alpha_0': []}

    for pt in pts:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        # Time 0
        wv0 = torch.tensor([wf0[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn0 = wv0.norm()
        if wn0 < 1e-12: continue
        eh0 = wv0 / wn0

        Sl0 = S0[:,:,ix,iy,iz].clone()
        ev0, ec0 = torch.linalg.eigh(Sl0)
        e3_0 = ec0[:, 0]  # most compressive
        e1_0 = ec0[:, 2]  # most stretching

        c3_0 = (eh0 @ e3_0).item()**2
        c1_0 = (eh0 @ e1_0).item()**2
        alpha_0 = sum(ev0[j].item() * (eh0 @ ec0[:,j]).item()**2 for j in range(3))

        # Time 1
        wv1 = torch.tensor([wf1[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn1 = wv1.norm()
        if wn1 < 1e-12: continue
        eh1 = wv1 / wn1

        Sl1 = S1[:,:,ix,iy,iz].clone()
        ev1, ec1 = torch.linalg.eigh(Sl1)
        e3_1 = ec1[:, 0]

        # Fix sign ambiguity: e3_1 should be close to e3_0
        if (e3_1 @ e3_0).item() < 0:
            e3_1 = -e3_1

        c3_1 = (eh1 @ e3_1).item()**2

        # dc₃/dt by finite difference
        dc3 = (c3_1 - c3_0) / dt_total

        # Decompose: c₃ = (ω̂ · e₃)²
        # dc₃ ≈ 2(ω̂·e₃)(dω̂/dt·e₃ + ω̂·de₃/dt) · dt
        #
        # Component from ω rotation: fix e₃ at t=0, use ω̂ at t=1
        c3_omega_rot = (eh1 @ e3_0).item()**2  # ω rotated, e₃ fixed
        dc3_omega = (c3_omega_rot - c3_0) / dt_total

        # Component from e₃ rotation: fix ω̂ at t=0, use e₃ at t=1
        c3_e3_rot = (eh0 @ e3_1).item()**2  # ω fixed, e₃ rotated
        dc3_e3 = (c3_e3_rot - c3_0) / dt_total

        results['dc3_dt'].append(dc3)
        results['dc3_omega_rot'].append(dc3_omega)
        results['dc3_e3_rot'].append(dc3_e3)
        results['c3_0'].append(c3_0)
        results['c1_0'].append(c1_0)
        results['alpha_0'].append(alpha_0)

    for k in results:
        results[k] = np.array(results[k])
    return results


def main():
    N = 32
    dt = 2e-4
    dt_diag = 50  # steps between measurements

    print("=" * 70, flush=True)
    print("c₃ ROTATION DECOMPOSITION: ω rotation vs e₃ rotation", flush=True)
    print("=" * 70, flush=True)

    for ic_name in ['TG', 'KP']:
        s = NS3D(N, nu=0.0)
        X, Y, Z = s.X, s.Y, s.Z

        if ic_name == 'TG':
            ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
            uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            uz = torch.zeros_like(X)
        else:
            ux = torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
            uy = torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
            uz = torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))

        w = s.curl(s.fft(ux), s.fft(uy), s.fft(uz))
        print(f"\n--- {ic_name}, Euler, N={N} ---", flush=True)

        t = 0.0
        for epoch in range(10):
            # Save state
            w_prev = tuple(wi.clone() for wi in w)
            t_prev = t

            # Evolve
            for _ in range(dt_diag):
                w = s.step(w, dt)
                t += dt

            if epoch == 0:
                continue  # skip first (need two snapshots)

            dt_total = t - t_prev
            r = measure_rotation(s, w_prev, w, dt_total)

            if r is None or len(r['dc3_dt']) == 0:
                print(f"  t={t:.4f}: insufficient data", flush=True)
                continue

            # Analyze
            dc3 = r['dc3_dt']
            dc3_w = r['dc3_omega_rot']
            dc3_e = r['dc3_e3_rot']

            print(f"\n  t={t:.4f}, |ω|={s.om_max(w):.3f}:", flush=True)
            print(f"    c₃: mean={r['c3_0'].mean():.3f}  "
                  f"c₁: mean={r['c1_0'].mean():.3f}  "
                  f"α: mean={r['alpha_0'].mean():.4f}", flush=True)
            print(f"    dc₃/dt (total):     mean={dc3.mean():.4f}", flush=True)
            print(f"    dc₃/dt (ω rotates): mean={dc3_w.mean():.4f}  "
                  f"({100*abs(dc3_w.mean())/(abs(dc3_w.mean())+abs(dc3_e.mean())+1e-30):.0f}%)", flush=True)
            print(f"    dc₃/dt (e₃ rotates):mean={dc3_e.mean():.4f}  "
                  f"({100*abs(dc3_e.mean())/(abs(dc3_w.mean())+abs(dc3_e.mean())+1e-30):.0f}%)", flush=True)
            print(f"    ω rotation HELPS c₃: {(dc3_w > 0).mean()*100:.0f}%", flush=True)
            print(f"    e₃ rotation HELPS c₃: {(dc3_e > 0).mean()*100:.0f}%", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
