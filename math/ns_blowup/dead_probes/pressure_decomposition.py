"""
Pressure Hessian decomposition: Yang (local) vs full (non-local).

We know H_ωω_Yang = -|S|²/3 (always compressive).
Question: is H_ωω_full MORE or LESS compressive than Yang?

If H_ωω_full < H_ωω_Yang (more negative): non-local helps → proof easier
If H_ωω_full > H_ωω_Yang (less negative): non-local hurts → proof harder

This experiment computes BOTH from DNS and compares.
"""
import torch
import numpy as np
import math
import time

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
        self.kmag = self.ksq.sqrt()
        self.D = ((self.kx.abs() < N//3) & (self.ky.abs() < N//3) &
                   (self.kz.abs() < N//3)).to(DTYPE)

    def fft(self, f): return torch.fft.fftn(f)
    def ifft(self, fh): return torch.fft.ifftn(fh).real

    def curl(self, a, b, c):
        I = 1j
        return (I*self.ky*c - I*self.kz*b, I*self.kz*a - I*self.kx*c,
                I*self.kx*b - I*self.ky*a)

    def vel(self, a, b, c):
        px = a/self.ksq; py = b/self.ksq; pz = c/self.ksq
        px[0,0,0] = 0; py[0,0,0] = 0; pz[0,0,0] = 0
        I = 1j
        return (I*self.ky*pz - I*self.kz*py, I*self.kz*px - I*self.kx*pz,
                I*self.kx*py - I*self.ky*px)

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
        k1 = self.rhs(w)
        k2 = self.rhs(add(w, k1, .5*dt))
        k3 = self.rhs(add(w, k2, .5*dt))
        k4 = self.rhs(add(w, k3, dt))
        return tuple(self.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))

    def om_max(self, w):
        v = [self.ifft(w[i]) for i in range(3)]
        return (v[0]**2 + v[1]**2 + v[2]**2).sqrt().max().item()


def decompose_pressure_hessian(solver, w, percentile=0.90, n_sample=1000):
    """
    Compute H_ωω (full) and H_ωω_Yang = -|S|²/3 at top |ω| points.
    Returns statistics comparing the two.
    """
    D = solver.D; N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]

    # Velocity and gradients
    u = solver.vel(*w)
    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            A[i,j] = solver.ifft(1j * kd[j] * D * u[i])

    S = 0.5 * (A + A.transpose(0, 1))

    # FULL pressure from Poisson: Δp = |ω|²/2 - |S|²
    # Source: -A_ij A_ji
    source = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            source -= A[i,j] * A[j,i]

    source_h = solver.fft(source)
    p_hat = -source_h / solver.ksq
    p_hat[0,0,0] = 0

    # Full pressure Hessian
    H_full = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H_full[i,j] = solver.ifft(-kd[i] * kd[j] * p_hat)

    # Vorticity
    wf = [solver.ifft(D * w[i]) for i in range(3)]
    om = (wf[0]**2 + wf[1]**2 + wf[2]**2).sqrt()

    thr = torch.quantile(om.flatten(), percentile)
    if thr < 1e-10:
        return None

    mask = om > thr
    idx = mask.nonzero(as_tuple=False)
    n = min(len(idx), n_sample)
    perm = torch.randperm(len(idx))[:n]
    pts = idx[perm]

    results = {
        'H_full': [], 'H_yang': [], 'S_norm_sq': [],
        'c1': [], 'c3': [], 'alpha': [], 'om_local': []
    }

    for pt in pts:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        # ω direction
        wv = torch.tensor([wf[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn = wv.norm()
        if wn < 1e-12:
            continue
        eh = wv / wn

        # Full H_ωω
        Hl = H_full[:,:,ix,iy,iz]
        h_full = (eh @ Hl @ eh).item()

        # Strain norm
        Sl = S[:,:,ix,iy,iz]
        s_norm_sq = (Sl * Sl).sum().item()  # |S|² = tr(S^T S)

        # Yang prediction: -|S|²/3
        h_yang = -s_norm_sq / 3

        # Alignment
        ev, ec = torch.linalg.eigh(Sl)
        c1 = (eh @ ec[:,2]).item()**2
        c3 = (eh @ ec[:,0]).item()**2
        alpha = ev[2].item()*c1 + ev[1].item()*(eh@ec[:,1]).item()**2 + ev[0].item()*c3

        results['H_full'].append(h_full)
        results['H_yang'].append(h_yang)
        results['S_norm_sq'].append(s_norm_sq)
        results['c1'].append(c1)
        results['c3'].append(c3)
        results['alpha'].append(alpha)
        results['om_local'].append(wn.item())

    for k in results:
        results[k] = np.array(results[k])

    return results


def main():
    N = 32
    dt = 2e-4
    n_steps = 1000  # t = 0.2

    print("=" * 70, flush=True)
    print("PRESSURE HESSIAN DECOMPOSITION: Yang (local) vs Full (non-local)", flush=True)
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

        # Evolve and measure at several times
        t = 0.0
        for diag_step in range(6):
            # Evolve 200 steps
            if diag_step > 0:
                for _ in range(200):
                    w = s.step(w, dt)
                    t += dt

            om = s.om_max(w)
            r = decompose_pressure_hessian(s, w)

            if r is None or len(r['H_full']) == 0:
                print(f"  t={t:.3f}: |ω|={om:.3f} — insufficient data", flush=True)
                continue

            hf = r['H_full']
            hy = r['H_yang']
            ratio = hf / (hy + 1e-30)  # H_full / H_yang

            # Key question: is ratio > 1 (non-local helps) or < 1 (non-local hurts)?
            # Since both are negative: ratio > 1 means H_full MORE negative (helps)
            # ratio < 1 means H_full less negative (hurts, but still compressive if >0)

            print(f"\n  t={t:.3f}, |ω|_max={om:.3f}, {len(hf)} pts:", flush=True)
            print(f"    H_ωω (full):  mean={hf.mean():.6f}  std={hf.std():.6f}", flush=True)
            print(f"    H_ωω (Yang):  mean={hy.mean():.6f}  std={hy.std():.6f}", flush=True)
            print(f"    Ratio full/Yang: mean={ratio.mean():.3f}  "
                  f"(>1: non-local helps, <1: hurts)", flush=True)
            print(f"    H_full < H_yang (more compressive): "
                  f"{(hf < hy).sum()}/{len(hf)} ({100*(hf < hy).mean():.0f}%)", flush=True)
            print(f"    H_full < 0 (compressive): "
                  f"{(hf < 0).sum()}/{len(hf)} ({100*(hf < 0).mean():.0f}%)", flush=True)

            # Also report alignment
            print(f"    c₁: mean={r['c1'].mean():.3f}  c₃: mean={r['c3'].mean():.3f}  "
                  f"α: mean={r['alpha'].mean():.4f}", flush=True)

    # Summary
    print(f"\n{'='*70}", flush=True)
    print("INTERPRETATION:", flush=True)
    print("  If ratio > 1: non-local pressure makes H_ωω MORE negative", flush=True)
    print("  → The compression is STRONGER than Yang predicts", flush=True)
    print("  → The non-local term HELPS the proof", flush=True)
    print("  If 0 < ratio < 1: non-local makes H_ωω LESS negative", flush=True)
    print("  → Compression weaker but still present (Yang alone suffices)", flush=True)
    print("  If ratio < 0: non-local REVERSES the sign", flush=True)
    print("  → DANGER: pressure becomes stretching along ω", flush=True)
    print(f"{'='*70}", flush=True)


if __name__ == '__main__':
    main()
