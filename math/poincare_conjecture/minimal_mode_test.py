"""
Minimal mode experiment: find the EXACT threshold for c₃ ≥ 1/3.

We know k≤2 fails and k≤4 works. Let's find the precise boundary.
Also: identify WHICH specific triadic interactions produce the c₃ shift.

For TG on T³:
  ω has modes at k = (±1, ±1, ±1) (8 modes per component, |k|=√3)

Triadic products k₁ + k₂ for TG:
  (1,1,1) + (-1,-1,1) = (0,0,2)     |k| = 2.00      <-- face modes
  (1,1,1) + (-1,1,-1) = (0,2,0)     |k| = 2.00
  (1,1,1) + (1,-1,-1) = (2,0,0)     |k| = 2.00
  (1,1,1) + (-1,1,1)  = (0,2,2)     |k| = 2√2 = 2.83
  (1,1,1) + (1,-1,1)  = (2,0,2)     |k| = 2√2 = 2.83
  (1,1,1) + (1,1,-1)  = (2,2,0)     |k| = 2√2 = 2.83
  (1,1,1) + (1,1,1)   = (2,2,2)     |k| = 2√3 = 3.46  <-- corner modes

So the products are at |k| = 0, 2, 2√2, 2√3.
At k≤2: we get (0,0,2) family but LOSE (0,2,2) and (2,2,2).
At k≤3: we get (0,2,2) family but LOSE (2,2,2).
At k≤4: we get EVERYTHING.

Question: is k≤3 enough? Which products matter?
"""
import torch
import numpy as np
import math
import time

DEVICE = 'cpu'
DTYPE = torch.float64


class NS3DMini:
    """Minimal 3D NS for mode-counting experiments."""

    def __init__(self, N=32, nu=1e-3):
        self.N = N
        self.nu = nu
        self.Lx = 2 * math.pi
        dx = self.Lx / N

        x = torch.linspace(0, self.Lx - dx, N, dtype=DTYPE)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')

        k = torch.fft.fftfreq(N, d=dx / (2 * math.pi)).to(dtype=DTYPE)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0
        self.kmag = self.ksq.sqrt()
        self.dealias = ((self.kx.abs() < N//3) & (self.ky.abs() < N//3) &
                        (self.kz.abs() < N//3)).to(DTYPE)

    def fft(self, f): return torch.fft.fftn(f)
    def ifft(self, fh): return torch.fft.ifftn(fh).real

    def curl(self, ux_h, uy_h, uz_h):
        I = 1j
        return (I*self.ky*uz_h - I*self.kz*uy_h,
                I*self.kz*ux_h - I*self.kx*uz_h,
                I*self.kx*uy_h - I*self.ky*ux_h)

    def vel_from_vort(self, wx_h, wy_h, wz_h):
        px = wx_h / self.ksq; py = wy_h / self.ksq; pz = wz_h / self.ksq
        px[0,0,0] = 0; py[0,0,0] = 0; pz[0,0,0] = 0
        I = 1j
        return (I*self.ky*pz - I*self.kz*py,
                I*self.kz*px - I*self.kx*pz,
                I*self.kx*py - I*self.ky*px)

    def rhs(self, wx_h, wy_h, wz_h):
        D = self.dealias
        ux_h, uy_h, uz_h = self.vel_from_vort(wx_h, wy_h, wz_h)
        ux = self.ifft(D*ux_h); uy = self.ifft(D*uy_h); uz = self.ifft(D*uz_h)
        wx = self.ifft(D*wx_h); wy = self.ifft(D*wy_h); wz = self.ifft(D*wz_h)

        grads = {}
        for name, fh in [('ux', ux_h), ('uy', uy_h), ('uz', uz_h)]:
            for d, kd in [('x', self.kx), ('y', self.ky), ('z', self.kz)]:
                grads[f'd{name}_d{d}'] = self.ifft(1j * kd * D * fh)
        sx = wx*grads['dux_dx'] + wy*grads['dux_dy'] + wz*grads['dux_dz']
        sy = wx*grads['duy_dx'] + wy*grads['duy_dy'] + wz*grads['duy_dz']
        sz = wx*grads['duz_dx'] + wy*grads['duz_dy'] + wz*grads['duz_dz']

        wgrads = {}
        for name, fh in [('wx', wx_h), ('wy', wy_h), ('wz', wz_h)]:
            for d, kd in [('x', self.kx), ('y', self.ky), ('z', self.kz)]:
                wgrads[f'd{name}_d{d}'] = self.ifft(1j * kd * D * fh)
        ax = ux*wgrads['dwx_dx'] + uy*wgrads['dwx_dy'] + uz*wgrads['dwx_dz']
        ay = ux*wgrads['dwy_dx'] + uy*wgrads['dwy_dy'] + uz*wgrads['dwy_dz']
        az = ux*wgrads['dwz_dx'] + uy*wgrads['dwz_dy'] + uz*wgrads['dwz_dz']

        rhs_x = D * self.fft(sx - ax) - self.nu * self.ksq * wx_h
        rhs_y = D * self.fft(sy - ay) - self.nu * self.ksq * wy_h
        rhs_z = D * self.fft(sz - az) - self.nu * self.ksq * wz_h
        return rhs_x, rhs_y, rhs_z

    def step_rk4(self, wx_h, wy_h, wz_h, dt):
        def add(s1, s2, a):
            return (s1[0]+a*s2[0], s1[1]+a*s2[1], s1[2]+a*s2[2])
        w = (wx_h, wy_h, wz_h)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w, k1, 0.5*dt))
        k3 = self.rhs(*add(w, k2, 0.5*dt))
        k4 = self.rhs(*add(w, k3, dt))
        D = self.dealias
        return (D*(wx_h + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])),
                D*(wy_h + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])),
                D*(wz_h + dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])))

    def trunc(self, fh, kr):
        return fh * (self.kmag <= kr + 0.5).to(DTYPE)

    def omega_max(self, wx_h, wy_h, wz_h):
        wx = self.ifft(wx_h); wy = self.ifft(wy_h); wz = self.ifft(wz_h)
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()

    def custom_mask(self, fh, allowed_kmags):
        """Keep only modes at specific |k| values (with tolerance 0.1)."""
        mask = torch.zeros_like(self.kmag)
        for km in allowed_kmags:
            mask += ((self.kmag - km).abs() < 0.1).to(DTYPE)
        mask = mask.clamp(0, 1)
        return fh * mask


def compute_c3(solver, wx_h, wy_h, wz_h, percentile=0.90, n_sample=2000):
    """Compute mean c₃ at top |ω| points."""
    D = solver.dealias
    N = solver.N

    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)
    duidxj = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    k_dirs = [solver.kx, solver.ky, solver.kz]
    u_hats = [ux_h, uy_h, uz_h]
    for i in range(3):
        for j in range(3):
            duidxj[i, j] = solver.ifft(1j * k_dirs[j] * D * u_hats[i])

    S = 0.5 * (duidxj + duidxj.transpose(0, 1))

    wx = solver.ifft(D * wx_h)
    wy = solver.ifft(D * wy_h)
    wz = solver.ifft(D * wz_h)
    om_mag = (wx**2 + wy**2 + wz**2).sqrt()

    threshold = torch.quantile(om_mag.flatten(), percentile)
    if threshold < 1e-10:
        return 0.33, 0.33, 0.33, 0.0

    mask = om_mag > threshold
    idx = mask.nonzero(as_tuple=False)
    n_pts = min(len(idx), n_sample)
    if n_pts == 0:
        return 0.33, 0.33, 0.33, 0.0

    perm = torch.randperm(len(idx))[:n_pts]
    sampled = idx[perm]

    c1s, c2s, c3s, alphas = [], [], [], []
    for pt in sampled:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()
        Sl = S[:, :, ix, iy, iz].clone()
        w = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
        wn = w.norm()
        if wn < 1e-12: continue
        wh = w / wn
        eigvals, eigvecs = torch.linalg.eigh(Sl)
        c1 = (wh @ eigvecs[:, 2]).item()**2
        c2 = (wh @ eigvecs[:, 1]).item()**2
        c3 = (wh @ eigvecs[:, 0]).item()**2
        alpha = eigvals[2].item()*c1 + eigvals[1].item()*c2 + eigvals[0].item()*c3
        c1s.append(c1); c2s.append(c2); c3s.append(c3); alphas.append(alpha)

    if not c1s:
        return 0.33, 0.33, 0.33, 0.0
    return np.mean(c1s), np.mean(c2s), np.mean(c3s), np.mean(alphas)


def ic_tg(s):
    X, Y, Z = s.X, s.Y, s.Z
    ux = torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uy = -torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uz = torch.zeros_like(X)
    return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))


def evolve_and_measure(solver, wx_h, wy_h, wz_h, n_steps=800, dt=5e-4,
                       k_trunc=None, custom_kmags=None):
    """Evolve with optional truncation, return c₃ time series."""
    results = []
    t = 0.0
    for step in range(n_steps + 1):
        if step % 200 == 0:
            c1, c2, c3, alpha = compute_c3(solver, wx_h, wy_h, wz_h)
            om = solver.omega_max(wx_h, wy_h, wz_h)
            results.append((t, c1, c2, c3, alpha, om))

        if step < n_steps:
            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
            if k_trunc is not None:
                wx_h = solver.trunc(wx_h, k_trunc)
                wy_h = solver.trunc(wy_h, k_trunc)
                wz_h = solver.trunc(wz_h, k_trunc)
            if custom_kmags is not None:
                wx_h = solver.custom_mask(wx_h, custom_kmags)
                wy_h = solver.custom_mask(wy_h, custom_kmags)
                wz_h = solver.custom_mask(wz_h, custom_kmags)
            t += dt

    return results


def main():
    print("=" * 70)
    print("MINIMAL MODE EXPERIMENT: which modes drive c₃ ≥ 1/3?")
    print("=" * 70)

    N = 32
    nu = 1e-3
    dt = 5e-4
    n_steps = 800

    # TG modes and their triadic products:
    # IC:     |k| = √3 ≈ 1.73
    # Gen 1:  |k| = 0, 2, 2√2, 2√3
    #         0      2.00  2.83  3.46

    sqrt3 = math.sqrt(3)
    sqrt2 = math.sqrt(2)

    # Test 1: Fine-grained k_retain values
    print("\n--- Test 1: Fine-grained k_retain for TG ---")
    k_values = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 10.0]

    for kr in k_values:
        solver = NS3DMini(N=N, nu=nu)
        wx_h, wy_h, wz_h = ic_tg(solver)
        # Truncate IC
        wx_h = solver.trunc(wx_h, kr)
        wy_h = solver.trunc(wy_h, kr)
        wz_h = solver.trunc(wz_h, kr)

        results = evolve_and_measure(solver, wx_h, wy_h, wz_h, n_steps, dt, k_trunc=kr)

        # Print final state
        t, c1, c2, c3, alpha, om = results[-1]
        c3_check = "✓" if c3 >= 0.333 else " "
        print(f"  k≤{kr:4.1f}: t={t:.3f} c₁={c1:.3f} c₂={c2:.3f} c₃={c3:.3f} "
              f"α={alpha:.4f} |ω|={om:.3f} {c3_check}")

    # Test 2: Specific mode families
    print("\n--- Test 2: Specific mode families ---")
    print("  TG IC at |k|=√3. Products at |k|={0, 2, 2√2, 2√3}")

    families = {
        'IC only (√3)': [sqrt3],
        'IC + face (√3, 2)': [sqrt3, 2.0],
        'IC + face + edge (√3, 2, 2√2)': [sqrt3, 2.0, 2*sqrt2],
        'IC + ALL products (√3, 2, 2√2, 2√3)': [sqrt3, 2.0, 2*sqrt2, 2*sqrt3],
        'IC + products + gen2': [sqrt3, 2.0, 2*sqrt2, 2*sqrt3, 3.0, math.sqrt(8), math.sqrt(12)],
    }

    # Actually, custom_mask with specific |k| values won't work cleanly for evolution
    # because the nonlinear terms generate modes at ALL |k|.
    # A better test: evolve full, then POST-HOC truncate for measurement.

    print("\n--- Test 3: POST-HOC truncation at t=0.4 ---")
    print("  Evolve FULL NS, then measure c₃ with fields truncated to specific |k| ranges")

    solver = NS3DMini(N=N, nu=nu)
    wx_h, wy_h, wz_h = ic_tg(solver)

    # Evolve to t=0.4
    t = 0.0
    for step in range(n_steps):
        wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
        t += dt

    print(f"\n  Evolved to t={t:.4f}, |ω|_max = {solver.omega_max(wx_h, wy_h, wz_h):.3f}")

    # Now measure c₃ with fine-grained truncation
    for kr in [1.0, 1.5, 1.8, 2.0, 2.5, 2.9, 3.0, 3.5, 4.0, 5.0, 6.0, 10.0]:
        c1, c2, c3, alpha = compute_c3(solver,
                                        solver.trunc(wx_h, kr),
                                        solver.trunc(wy_h, kr),
                                        solver.trunc(wz_h, kr))
        c3_check = "✓" if c3 >= 0.333 else " "

        # Count modes at this truncation
        n_modes = int(((solver.kmag <= kr + 0.5) & (solver.kmag > 0.5)).sum().item())
        print(f"  k≤{kr:4.1f} ({n_modes:4d} modes): c₁={c1:.3f} c₂={c2:.3f} "
              f"c₃={c3:.3f} α={alpha:.4f} {c3_check}")

    # Test 4: Track which modes GROW during evolution
    print("\n--- Test 4: Mode energy growth ---")
    print("  Which |k| shells gain the most energy during evolution?")

    solver2 = NS3DMini(N=N, nu=nu)
    wx_h0, wy_h0, wz_h0 = ic_tg(solver2)

    # Evolve
    wx_h1, wy_h1, wz_h1 = wx_h0.clone(), wy_h0.clone(), wz_h0.clone()
    for step in range(n_steps):
        wx_h1, wy_h1, wz_h1 = solver2.step_rk4(wx_h1, wy_h1, wz_h1, dt)

    # Shell energies
    k_shells = np.arange(0.5, 11.5, 0.5)
    print(f"\n  {'|k| range':>12s}  {'E(t=0)':>10s}  {'E(t=0.4)':>10s}  {'ratio':>8s}  {'growth':>8s}")
    for i in range(len(k_shells) - 1):
        klo, khi = k_shells[i], k_shells[i+1]
        mask = ((solver2.kmag >= klo) & (solver2.kmag < khi)).to(DTYPE)

        E0 = (mask * (wx_h0.abs()**2 + wy_h0.abs()**2 + wz_h0.abs()**2)).sum().item()
        E1 = (mask * (wx_h1.abs()**2 + wy_h1.abs()**2 + wz_h1.abs()**2)).sum().item()

        if E0 > 1e-20 or E1 > 1e-20:
            ratio = E1 / max(E0, 1e-30)
            growth = "GROW" if ratio > 2 else ("decay" if ratio < 0.5 else "~same")
            print(f"  [{klo:4.1f}, {khi:4.1f}): {E0:10.4e}  {E1:10.4e}  {ratio:8.2f}  {growth}")

    # Test 5: The CRITICAL MODES — evolve with ONLY face modes removed
    print("\n\n--- Test 5: Surgical mode removal ---")
    print("  Remove specific mode families and check if c₃ drops")

    # Full evolution baseline
    solver = NS3DMini(N=N, nu=nu)
    wx_h, wy_h, wz_h = ic_tg(solver)
    for step in range(n_steps):
        wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
    c1_full, c2_full, c3_full, a_full = compute_c3(solver, wx_h, wy_h, wz_h)
    print(f"  Full NS:     c₁={c1_full:.3f} c₂={c2_full:.3f} c₃={c3_full:.3f} α={a_full:.4f}")

    # Remove modes and remeasure (post-hoc)
    removals = {
        'Remove |k|≈2 (face)': lambda km: (km - 2.0).abs() > 0.1,
        'Remove |k|≈2√2 (edge)': lambda km: (km - 2*sqrt2).abs() > 0.1,
        'Remove |k|≈2√3 (corner)': lambda km: (km - 2*sqrt3).abs() > 0.1,
        'Remove |k|>2 (all products)': lambda km: km <= 2.1,
        'Remove |k|>√3 (IC only)': lambda km: km <= sqrt3 + 0.1,
        'Keep |k|≤3 only': lambda km: km <= 3.1,
        'Keep |k|≤2√2 only': lambda km: km <= 2*sqrt2 + 0.1,
    }

    for name, keep_fn in removals.items():
        mask = keep_fn(solver.kmag).to(DTYPE)
        c1, c2, c3, alpha = compute_c3(solver,
                                         wx_h * mask, wy_h * mask, wz_h * mask)
        c3_check = "✓" if c3 >= 0.333 else " "
        delta = c3 - c3_full
        print(f"  {name:40s}: c₃={c3:.3f} (Δ={delta:+.3f}) {c3_check}")

    # Test 6: Viscosity independence — is this inviscid?
    print("\n\n--- Test 6: Viscosity dependence ---")
    print("  Run at different ν, check if c₃ is robust")

    for nu_test in [0.0, 1e-4, 1e-3, 5e-3, 1e-2]:
        solver = NS3DMini(N=N, nu=nu_test)
        wx_h, wy_h, wz_h = ic_tg(solver)
        for step in range(n_steps):
            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
        c1, c2, c3, alpha = compute_c3(solver, wx_h, wy_h, wz_h)
        om = solver.omega_max(wx_h, wy_h, wz_h)
        c3_check = "✓" if c3 >= 0.333 else " "
        print(f"  ν={nu_test:.0e}: c₃={c3:.3f} α={alpha:.4f} |ω|={om:.3f} {c3_check}")

    print(f"\n{'='*70}")
    print("DONE.")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
