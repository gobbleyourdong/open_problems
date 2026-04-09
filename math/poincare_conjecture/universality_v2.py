"""
Universality v2: Fix the random IC test.

Previous test failed because:
1. ν=10⁻³ was too dissipative — random fields decayed to zero
2. amp=2 was too weak for nonlinear dynamics to develop
3. Single-mode ICs produce zero self-interaction (no triadic products)

Fix: Use EULER (ν=0), high amplitude (amp=10), and k_max=4-8.
Also: anti-parallel tubes at higher resolution to see 3D instabilities.

KEY QUESTION: Is α ≤ 0 at high |ω| for ALL 3D incompressible flows?
"""
import torch
import numpy as np
import math
import time

DTYPE = torch.float64
pi = math.pi


class NS3D:
    def __init__(self, N=32, nu=0.0):
        self.N = N
        self.nu = nu
        self.Lx = 2 * pi
        dx = self.Lx / N
        x = torch.linspace(0, self.Lx - dx, N, dtype=DTYPE)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')
        k = torch.fft.fftfreq(N, d=dx / (2 * pi)).to(dtype=DTYPE)
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
        fields = {}
        for name, fh in [('ux', ux_h), ('uy', uy_h), ('uz', uz_h),
                          ('wx', wx_h), ('wy', wy_h), ('wz', wz_h)]:
            fields[name] = self.ifft(D * fh)
            for d, kd in [('x', self.kx), ('y', self.ky), ('z', self.kz)]:
                fields[f'd{name}_d{d}'] = self.ifft(1j * kd * D * fh)

        sx = fields['wx']*fields['dux_dx'] + fields['wy']*fields['dux_dy'] + fields['wz']*fields['dux_dz']
        sy = fields['wx']*fields['duy_dx'] + fields['wy']*fields['duy_dy'] + fields['wz']*fields['duy_dz']
        sz = fields['wx']*fields['duz_dx'] + fields['wy']*fields['duz_dy'] + fields['wz']*fields['duz_dz']
        ax = fields['ux']*fields['dwx_dx'] + fields['uy']*fields['dwx_dy'] + fields['uz']*fields['dwx_dz']
        ay = fields['ux']*fields['dwy_dx'] + fields['uy']*fields['dwy_dy'] + fields['uz']*fields['dwy_dz']
        az = fields['ux']*fields['dwz_dx'] + fields['uy']*fields['dwz_dy'] + fields['uz']*fields['dwz_dz']

        return (D * self.fft(sx-ax) - self.nu * self.ksq * wx_h,
                D * self.fft(sy-ay) - self.nu * self.ksq * wy_h,
                D * self.fft(sz-az) - self.nu * self.ksq * wz_h)

    def step_rk4(self, wx_h, wy_h, wz_h, dt):
        def add(s, k, a):
            return (s[0]+a*k[0], s[1]+a*k[1], s[2]+a*k[2])
        w = (wx_h, wy_h, wz_h)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w, k1, 0.5*dt))
        k3 = self.rhs(*add(w, k2, 0.5*dt))
        k4 = self.rhs(*add(w, k3, dt))
        D = self.dealias
        return (D*(wx_h + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])),
                D*(wy_h + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])),
                D*(wz_h + dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])))

    def omega_max(self, wx_h, wy_h, wz_h):
        wx = self.ifft(wx_h); wy = self.ifft(wy_h); wz = self.ifft(wz_h)
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()


def compute_alignment(solver, wx_h, wy_h, wz_h, percentile=0.90, n_max=2000):
    D = solver.dealias
    N = solver.N
    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)
    k_dirs = [solver.kx, solver.ky, solver.kz]
    u_hats = [ux_h, uy_h, uz_h]

    duidxj = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            duidxj[i, j] = solver.ifft(1j * k_dirs[j] * D * u_hats[i])
    S = 0.5 * (duidxj + duidxj.transpose(0, 1))

    wx = solver.ifft(D * wx_h); wy = solver.ifft(D * wy_h); wz = solver.ifft(D * wz_h)
    om = (wx**2 + wy**2 + wz**2).sqrt()
    thr = torch.quantile(om.flatten(), percentile)
    if thr < 1e-10:
        return 0.33, 0.33, 0.33, 0.0, 0.0

    idx = (om > thr).nonzero(as_tuple=False)
    n = min(len(idx), n_max)
    if n == 0:
        return 0.33, 0.33, 0.33, 0.0, 0.0

    perm = torch.randperm(len(idx))[:n]
    pts = idx[perm]
    c1s, c2s, c3s, als = [], [], [], []

    for pt in pts:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()
        Sl = S[:, :, ix, iy, iz].clone()
        wv = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
        wn = wv.norm()
        if wn < 1e-12: continue
        wh = wv / wn
        ev, ec = torch.linalg.eigh(Sl)
        c1 = (wh @ ec[:, 2]).item()**2
        c2 = (wh @ ec[:, 1]).item()**2
        c3 = (wh @ ec[:, 0]).item()**2
        al = ev[2].item()*c1 + ev[1].item()*c2 + ev[0].item()*c3
        c1s.append(c1); c2s.append(c2); c3s.append(c3); als.append(al)

    if not c1s:
        return 0.33, 0.33, 0.33, 0.0, 0.0
    return np.mean(c1s), np.mean(c2s), np.mean(c3s), np.mean(als), thr.item()


def random_ic_strong(solver, k_max=4, amp=10.0, seed=None):
    """Strong random divergence-free IC."""
    if seed is not None:
        torch.manual_seed(seed)
    N = solver.N

    Ax_h = torch.zeros(N, N, N, dtype=torch.complex128)
    Ay_h = torch.zeros_like(Ax_h)
    Az_h = torch.zeros_like(Ax_h)

    for i in range(-k_max, k_max+1):
        for j in range(-k_max, k_max+1):
            for k in range(-k_max, k_max+1):
                ksq = i*i + j*j + k*k
                if ksq == 0 or ksq > k_max**2:
                    continue
                mag = amp / ksq
                ii, jj, kk = i % N, j % N, k % N
                for A_h in [Ax_h, Ay_h, Az_h]:
                    A_h[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()

    I = 1j
    ux_h = I * solver.ky * Az_h - I * solver.kz * Ay_h
    uy_h = I * solver.kz * Ax_h - I * solver.kx * Az_h
    uz_h = I * solver.kx * Ay_h - I * solver.ky * Ax_h
    return solver.curl(ux_h, uy_h, uz_h)


def ic_tg(s):
    X, Y, Z = s.X, s.Y, s.Z
    ux = torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uy = -torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uz = torch.zeros_like(X)
    return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))


def ic_kp(s):
    X, Y, Z = s.X, s.Y, s.Z
    ux = torch.sin(X) * (torch.cos(3*Y) * torch.cos(Z) - torch.cos(Y) * torch.cos(3*Z))
    uy = torch.sin(Y) * (torch.cos(3*Z) * torch.cos(X) - torch.cos(Z) * torch.cos(3*X))
    uz = torch.sin(Z) * (torch.cos(3*X) * torch.cos(Y) - torch.cos(X) * torch.cos(3*Y))
    return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))


def ic_abc(s, A=1.0, B=0.8, C=0.6):
    """Arnold-Beltrami-Childress flow — exact Euler solution (Beltrami)."""
    X, Y, Z = s.X, s.Y, s.Z
    ux = A*torch.sin(Z) + C*torch.cos(Y)
    uy = B*torch.sin(X) + A*torch.cos(Z)
    uz = C*torch.sin(Y) + B*torch.cos(X)
    return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))


def ic_perturbed_abc(s, eps=0.3, seed=42):
    """ABC + random perturbation — breaks Beltrami, triggers dynamics."""
    wx_h, wy_h, wz_h = ic_abc(s)
    torch.manual_seed(seed)
    N = s.N
    # Add random modes at k=2-4
    for _ in range(50):
        i = torch.randint(-4, 5, (1,)).item()
        j = torch.randint(-4, 5, (1,)).item()
        k = torch.randint(-4, 5, (1,)).item()
        ksq = i*i + j*j + k*k
        if ksq < 4 or ksq > 16: continue
        ii, jj, kk = i % N, j % N, k % N
        mag = eps / ksq
        wx_h[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).item()
        wy_h[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).item()
        wz_h[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).item()

    # Re-project to div-free
    kdotw = s.kx*wx_h + s.ky*wy_h + s.kz*wz_h
    wx_h -= s.kx * kdotw / s.ksq
    wy_h -= s.ky * kdotw / s.ksq
    wz_h -= s.kz * kdotw / s.ksq
    wx_h[0,0,0] = 0; wy_h[0,0,0] = 0; wz_h[0,0,0] = 0
    return wx_h, wy_h, wz_h


def main():
    N = 32
    dt = 2e-4  # Smaller for Euler stability
    n_steps = 2000  # Evolve to t=0.4

    print("=" * 70)
    print("UNIVERSALITY v2: Euler (ν=0), strong amplitudes")
    print("=" * 70)

    # =====================================================================
    # Test 1: Named ICs at ν=0
    # =====================================================================
    print("\n--- Test 1: Named ICs, Euler (ν=0) ---")

    named_ics = {
        'TG': ic_tg,
        'KP': ic_kp,
        'ABC(1,0.8,0.6)': ic_abc,
        'Perturbed ABC': ic_perturbed_abc,
    }

    for name, ic_fn in named_ics.items():
        solver = NS3D(N=N, nu=0.0)
        wx_h, wy_h, wz_h = ic_fn(solver)

        om0 = solver.omega_max(wx_h, wy_h, wz_h)
        c1_0, c2_0, c3_0, a0, thr0 = compute_alignment(solver, wx_h, wy_h, wz_h)

        t = 0.0
        for step in range(n_steps):
            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
            t += dt

        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha, thr = compute_alignment(solver, wx_h, wy_h, wz_h)
        mark = "✓" if c3 >= 0.333 else " "
        print(f"  {name:20s}: |ω|₀={om0:.2f}→{om:.2f}  "
              f"c₁={c1:.3f} c₂={c2:.3f} c₃={c3:.3f} α={alpha:.4f} {mark}")
        print(f"    {'':20s}  init: c₁={c1_0:.3f} c₂={c2_0:.3f} c₃={c3_0:.3f}")

    # =====================================================================
    # Test 2: Random ICs, ν=0, amp=10, 20 seeds
    # =====================================================================
    print("\n--- Test 2: Random ICs, Euler (ν=0), amp=10, k_max=4, 20 seeds ---")
    print(f"  {'seed':>4s}  {'|ω|₀':>6s}  {'|ω|_T':>6s}  {'c₁':>6s}  {'c₂':>6s}  "
          f"{'c₃':>6s}  {'α':>8s}  ok?")

    c3_finals = []
    alpha_finals = []
    c3_above = 0
    alpha_neg = 0
    total = 20

    for seed in range(total):
        solver = NS3D(N=N, nu=0.0)
        wx_h, wy_h, wz_h = random_ic_strong(solver, k_max=4, amp=10.0, seed=seed)
        om0 = solver.omega_max(wx_h, wy_h, wz_h)

        t = 0.0
        for step in range(n_steps):
            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
            t += dt

        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha, thr = compute_alignment(solver, wx_h, wy_h, wz_h)

        c3_finals.append(c3)
        alpha_finals.append(alpha)
        if c3 >= 0.333: c3_above += 1
        if alpha <= 0: alpha_neg += 1
        mark = "✓" if c3 >= 0.333 else " "
        a_mark = "≤0" if alpha <= 0 else ">0"
        print(f"  {seed:4d}  {om0:6.2f}  {om:6.2f}  {c1:6.3f}  {c2:6.3f}  "
              f"{c3:6.3f}  {alpha:8.4f}  {mark} {a_mark}")

    print(f"\n  Summary ({total} random ICs):")
    print(f"    c₃ ≥ 1/3:    {c3_above}/{total} ({100*c3_above/total:.0f}%)")
    print(f"    α ≤ 0:        {alpha_neg}/{total} ({100*alpha_neg/total:.0f}%)")
    print(f"    mean c₃:      {np.mean(c3_finals):.4f} ± {np.std(c3_finals):.4f}")
    print(f"    mean α:       {np.mean(alpha_finals):.4f} ± {np.std(alpha_finals):.4f}")

    # =====================================================================
    # Test 3: Higher k_max random ICs (more turbulent)
    # =====================================================================
    print("\n--- Test 3: Random ICs, Euler, amp=10, k_max=8, 10 seeds ---")
    print(f"  {'seed':>4s}  {'|ω|₀':>6s}  {'|ω|_T':>6s}  {'c₁':>6s}  {'c₂':>6s}  "
          f"{'c₃':>6s}  {'α':>8s}  ok?")

    c3_finals2 = []
    for seed in range(10):
        solver = NS3D(N=N, nu=0.0)
        wx_h, wy_h, wz_h = random_ic_strong(solver, k_max=8, amp=10.0, seed=seed+100)
        om0 = solver.omega_max(wx_h, wy_h, wz_h)

        t = 0.0
        for step in range(n_steps):
            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
            t += dt

        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha, thr = compute_alignment(solver, wx_h, wy_h, wz_h)
        c3_finals2.append(c3)
        mark = "✓" if c3 >= 0.333 else " "
        a_mark = "≤0" if alpha <= 0 else ">0"
        print(f"  {seed:4d}  {om0:6.2f}  {om:6.2f}  {c1:6.3f}  {c2:6.3f}  "
              f"{c3:6.3f}  {alpha:8.4f}  {mark} {a_mark}")

    print(f"\n  mean c₃: {np.mean(c3_finals2):.4f} ± {np.std(c3_finals2):.4f}")

    # =====================================================================
    # Test 4: Time evolution for strongest random ICs
    # =====================================================================
    print("\n--- Test 4: Time evolution for 3 strong random ICs ---")
    for seed in [0, 5, 12]:
        solver = NS3D(N=N, nu=0.0)
        wx_h, wy_h, wz_h = random_ic_strong(solver, k_max=4, amp=10.0, seed=seed)

        print(f"\n  seed={seed}:")
        t = 0.0
        for step in range(n_steps + 1):
            if step % 400 == 0:
                om = solver.omega_max(wx_h, wy_h, wz_h)
                c1, c2, c3, alpha, thr = compute_alignment(solver, wx_h, wy_h, wz_h)
                mark = "✓" if c3 >= 0.333 else " "
                print(f"    t={t:.3f}: |ω|={om:6.2f} c₁={c1:.3f} c₂={c2:.3f} "
                      f"c₃={c3:.3f} α={alpha:.4f} {mark}")

            if step < n_steps:
                wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
                t += dt

    # =====================================================================
    # Test 5: Does the stretching rate α scale with |ω|?
    # =====================================================================
    print("\n--- Test 5: α vs |ω| — does compression strengthen at high |ω|? ---")
    print("  Using TG, Euler, measure α at different |ω| thresholds")

    solver = NS3D(N=N, nu=0.0)
    wx_h, wy_h, wz_h = ic_tg(solver)
    t = 0.0
    for step in range(n_steps):
        wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
        t += dt

    om_max = solver.omega_max(wx_h, wy_h, wz_h)
    print(f"\n  t={t:.3f}, |ω|_max={om_max:.3f}")

    for pct in [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]:
        c1, c2, c3, alpha, thr = compute_alignment(solver, wx_h, wy_h, wz_h,
                                                     percentile=pct)
        mark = "✓" if c3 >= 0.333 else " "
        print(f"    top {(1-pct)*100:4.1f}%: |ω|>{thr:.3f}  c₁={c1:.3f} c₃={c3:.3f} "
              f"α={alpha:.4f} {mark}")

    print(f"\n{'='*70}")
    print("DONE.")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
