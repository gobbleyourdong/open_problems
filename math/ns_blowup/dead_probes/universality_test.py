"""
Universality test: does c₃ ≥ 1/3 appear for RANDOM initial conditions?

The TG test showed the (2,2,0) modes are critical. But TG has special symmetry.
Is the c₃ ≥ 1/3 mechanism universal or geometry-dependent?

Test:
1. Random large-scale IC (random phases at |k|≤4)
2. Random multi-scale IC (k_max=8)
3. Single vortex tube (anti-parallel pair)
4. Many random seeds to get statistics

Also: analytical test of WHY the (2,2,0) modes create c₃ alignment.
"""
import torch
import numpy as np
import math
import time

DTYPE = torch.float64


class NS3D:
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
        return 0.33, 0.33, 0.33, 0.0

    idx = (om > thr).nonzero(as_tuple=False)
    n = min(len(idx), n_max)
    if n == 0:
        return 0.33, 0.33, 0.33, 0.0

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
        return 0.33, 0.33, 0.33, 0.0
    return np.mean(c1s), np.mean(c2s), np.mean(c3s), np.mean(als)


def random_ic(solver, k_max=4, amp=2.0, seed=None):
    """Random divergence-free IC with modes at |k| ≤ k_max."""
    if seed is not None:
        torch.manual_seed(seed)
    N = solver.N

    # Random potential field A in Fourier space
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

    # u = curl(A) → divergence-free
    I = 1j
    ux_h = I * solver.ky * Az_h - I * solver.kz * Ay_h
    uy_h = I * solver.kz * Ax_h - I * solver.kx * Az_h
    uz_h = I * solver.kx * Ay_h - I * solver.ky * Ax_h

    # ω = curl(u)
    return solver.curl(ux_h, uy_h, uz_h)


def anti_parallel_tubes(solver, amp=5.0, sep=math.pi/2, sigma=0.5):
    """Two anti-parallel vortex tubes — simplest interaction geometry."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    # Tube 1: +z direction at y = π - sep/2
    # Tube 2: -z direction at y = π + sep/2
    r1 = ((X - pi)**2 + (Y - pi + sep/2)**2).sqrt()
    r2 = ((X - pi)**2 + (Y - pi - sep/2)**2).sqrt()

    wz = amp * (torch.exp(-r1**2 / (2*sigma**2)) - torch.exp(-r2**2 / (2*sigma**2)))
    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)

    wx_h = solver.dealias * solver.fft(wx)
    wy_h = solver.dealias * solver.fft(wy)
    wz_h = solver.dealias * solver.fft(wz)

    # Project to div-free
    kdotw = solver.kx*wx_h + solver.ky*wy_h + solver.kz*wz_h
    wx_h -= solver.kx * kdotw / solver.ksq
    wy_h -= solver.ky * kdotw / solver.ksq
    wz_h -= solver.kz * kdotw / solver.ksq
    wx_h[0,0,0] = 0; wy_h[0,0,0] = 0; wz_h[0,0,0] = 0

    return wx_h, wy_h, wz_h


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


def evolve(solver, wx_h, wy_h, wz_h, t_final=0.4, dt=5e-4):
    t = 0.0
    while t < t_final - 1e-10:
        wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
        t += dt
    return wx_h, wy_h, wz_h, t


def main():
    N = 32
    nu = 1e-3
    dt = 5e-4

    print("=" * 70)
    print("UNIVERSALITY TEST: is c₃ ≥ 1/3 universal or IC-specific?")
    print("=" * 70)

    # =====================================================================
    # Test 1: 20 random ICs
    # =====================================================================
    print("\n--- Test 1: Random ICs (k_max=4, 20 seeds) ---")
    print(f"  {'seed':>4s}  {'c₁(t=0)':>8s}  {'c₃(t=0)':>8s}  {'c₁(t=T)':>8s}  "
          f"{'c₃(t=T)':>8s}  {'α':>8s}  {'|ω|':>6s}  c₃≥1/3?")

    c3_initial = []
    c3_final = []
    c3_above = 0
    total = 20

    for seed in range(total):
        solver = NS3D(N=N, nu=nu)
        wx_h, wy_h, wz_h = random_ic(solver, k_max=4, amp=2.0, seed=seed)

        c1_0, c2_0, c3_0, a_0 = compute_alignment(solver, wx_h, wy_h, wz_h)

        wx_h, wy_h, wz_h, t = evolve(solver, wx_h, wy_h, wz_h, t_final=0.4, dt=dt)
        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha = compute_alignment(solver, wx_h, wy_h, wz_h)

        c3_initial.append(c3_0)
        c3_final.append(c3)
        mark = "✓" if c3 >= 0.333 else " "
        if c3 >= 0.333:
            c3_above += 1

        print(f"  {seed:4d}  {c1_0:8.3f}  {c3_0:8.3f}  {c1:8.3f}  {c3:8.3f}  "
              f"{alpha:8.4f}  {om:6.2f}  {mark}")

    print(f"\n  Summary: c₃ ≥ 1/3 in {c3_above}/{total} cases ({100*c3_above/total:.0f}%)")
    print(f"  c₃ initial: mean={np.mean(c3_initial):.3f}, std={np.std(c3_initial):.3f}")
    print(f"  c₃ final:   mean={np.mean(c3_final):.3f}, std={np.std(c3_final):.3f}")
    print(f"  c₃ shift:   {np.mean(c3_final) - np.mean(c3_initial):+.3f}")

    # =====================================================================
    # Test 2: Anti-parallel tubes
    # =====================================================================
    print("\n--- Test 2: Anti-parallel vortex tubes ---")

    for sep in [0.5, 1.0, 1.5, 2.0, 3.0]:
        solver = NS3D(N=N, nu=nu)
        wx_h, wy_h, wz_h = anti_parallel_tubes(solver, amp=5.0, sep=sep)
        c1_0, c2_0, c3_0, _ = compute_alignment(solver, wx_h, wy_h, wz_h)

        wx_h, wy_h, wz_h, t = evolve(solver, wx_h, wy_h, wz_h, t_final=0.4, dt=dt)
        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha = compute_alignment(solver, wx_h, wy_h, wz_h)
        mark = "✓" if c3 >= 0.333 else " "
        print(f"  sep={sep:.1f}: c₁={c1:.3f} c₂={c2:.3f} c₃={c3:.3f} "
              f"α={alpha:.4f} |ω|={om:.2f} {mark}  (init c₃={c3_0:.3f})")

    # =====================================================================
    # Test 3: Single-mode IC (just one Fourier mode)
    # =====================================================================
    print("\n--- Test 3: Single-mode IC (one Fourier mode ω_hat(k₀)) ---")
    print("  The simplest possible IC. Does c₃ shift after evolution?")

    for k0 in [(1,0,0), (1,1,0), (1,1,1), (2,1,0), (2,1,1)]:
        solver = NS3D(N=N, nu=nu)
        N_ = solver.N
        wx_h = torch.zeros(N_, N_, N_, dtype=torch.complex128)
        wy_h = torch.zeros_like(wx_h)
        wz_h = torch.zeros_like(wx_h)

        # Set a single mode with random amplitude
        torch.manual_seed(42)
        i, j, k = k0
        amp = 3.0

        # Must make field real: f(-k) = conj(f(k))
        for sg in [1, -1]:
            ii = (sg*i) % N_
            jj = (sg*j) % N_
            kk = (sg*k) % N_
            phase = torch.randn(3) + 1j * torch.randn(3)
            if sg == -1:
                phase = phase.conj()
            wx_h[ii,jj,kk] = amp * phase[0].item()
            wy_h[ii,jj,kk] = amp * phase[1].item()
            wz_h[ii,jj,kk] = amp * phase[2].item()

        # Project to div-free: k · ω_hat = 0
        kv = torch.tensor([i, j, k], dtype=DTYPE)
        for sg in [1, -1]:
            ii = (sg*i) % N_
            jj = (sg*j) % N_
            kk = (sg*k) % N_
            w_vec = torch.tensor([wx_h[ii,jj,kk], wy_h[ii,jj,kk], wz_h[ii,jj,kk]])
            k_hat = kv / (kv.norm() + 1e-30)
            proj = (k_hat @ w_vec.real + 1j * (k_hat @ w_vec.imag))
            wx_h[ii,jj,kk] -= proj * k_hat[0]
            wy_h[ii,jj,kk] -= proj * k_hat[1]
            wz_h[ii,jj,kk] -= proj * k_hat[2]

        c1_0, c2_0, c3_0, _ = compute_alignment(solver, wx_h, wy_h, wz_h)

        wx_h, wy_h, wz_h, t = evolve(solver, wx_h, wy_h, wz_h, t_final=0.4, dt=dt)
        om = solver.omega_max(wx_h, wy_h, wz_h)
        c1, c2, c3, alpha = compute_alignment(solver, wx_h, wy_h, wz_h)
        mark = "✓" if c3 >= 0.333 else " "
        print(f"  k₀={str(k0):>10s}: c₃: {c3_0:.3f} → {c3:.3f} "
              f"(Δ={c3-c3_0:+.3f}) α={alpha:.4f} |ω|={om:.2f} {mark}")

    # =====================================================================
    # Test 4: Longer evolution for random ICs — does c₃ persist?
    # =====================================================================
    print("\n--- Test 4: Long evolution (t=0 → 2.0) for 5 random ICs ---")
    print("  Does c₃ ≥ 1/3 persist or is it transient?")

    for seed in [0, 3, 7, 11, 15]:
        solver = NS3D(N=N, nu=nu)
        wx_h, wy_h, wz_h = random_ic(solver, k_max=4, amp=2.0, seed=seed)

        t = 0.0
        t_final = 2.0
        diag_times = [0.0, 0.2, 0.5, 1.0, 1.5, 2.0]
        diag_idx = 0

        print(f"\n  seed={seed}:")
        while t < t_final - 1e-10:
            if diag_idx < len(diag_times) and t >= diag_times[diag_idx] - 1e-10:
                c1, c2, c3, alpha = compute_alignment(solver, wx_h, wy_h, wz_h)
                om = solver.omega_max(wx_h, wy_h, wz_h)
                mark = "✓" if c3 >= 0.333 else " "
                print(f"    t={t:.2f}: c₁={c1:.3f} c₂={c2:.3f} c₃={c3:.3f} "
                      f"α={alpha:.4f} |ω|={om:.2f} {mark}")
                diag_idx += 1

            wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
            t += dt

        # Final
        c1, c2, c3, alpha = compute_alignment(solver, wx_h, wy_h, wz_h)
        om = solver.omega_max(wx_h, wy_h, wz_h)
        mark = "✓" if c3 >= 0.333 else " "
        print(f"    t={t:.2f}: c₁={c1:.3f} c₂={c2:.3f} c₃={c3:.3f} "
              f"α={alpha:.4f} |ω|={om:.2f} {mark}")

    # =====================================================================
    # Test 5: The analytical question — trace-free + Biot-Savart
    # =====================================================================
    print("\n\n--- Test 5: Analytical — is self-interaction always compressive? ---")
    print("  For a SINGLE Fourier mode ω_hat(k), the strain from Biot-Savart is:")
    print("  S(x) depends on the phase structure of ω_hat.")
    print("  Computing for TG-like modes...")

    solver = NS3D(N=N, nu=nu)
    N_ = solver.N

    # TG-like: modes at (1,1,1) with specific phase structure
    # What's the strain and alignment at the point of maximum |ω|?

    # Set up TG IC explicitly
    wx_h, wy_h, wz_h = ic_tg(solver)

    D = solver.dealias
    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)

    # At the point of max |ω|
    wx = solver.ifft(D * wx_h)
    wy = solver.ifft(D * wy_h)
    wz = solver.ifft(D * wz_h)
    om = (wx**2 + wy**2 + wz**2).sqrt()

    # Find max point
    flat_idx = om.flatten().argmax().item()
    iz = flat_idx % N_
    iy = (flat_idx // N_) % N_
    ix = flat_idx // (N_ * N_)

    print(f"\n  Max |ω| at ({ix},{iy},{iz}), |ω|={om[ix,iy,iz].item():.4f}")
    print(f"  Position: x={solver.X[ix,iy,iz].item():.3f}, "
          f"y={solver.Y[ix,iy,iz].item():.3f}, z={solver.Z[ix,iy,iz].item():.3f}")

    # Strain at max point
    k_dirs = [solver.kx, solver.ky, solver.kz]
    u_hats = [ux_h, uy_h, uz_h]
    Smat = torch.zeros(3, 3, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            duidxj = solver.ifft(1j * k_dirs[j] * D * u_hats[i])
            Smat[i, j] += duidxj[ix, iy, iz]
    Smat = 0.5 * (Smat + Smat.T)

    eigvals, eigvecs = torch.linalg.eigh(Smat)
    w_vec = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
    wh = w_vec / w_vec.norm()

    print(f"\n  Strain eigenvalues: λ₁={eigvals[2].item():.4f}, "
          f"λ₂={eigvals[1].item():.4f}, λ₃={eigvals[0].item():.4f}")
    print(f"  Trace: {eigvals.sum().item():.6f} (should be 0)")

    for i, name in [(2, 'e₁(stretch)'), (1, 'e₂(inter)'), (0, 'e₃(compress)')]:
        cos2 = (wh @ eigvecs[:, i]).item()**2
        print(f"  cos²(ω, {name}) = {cos2:.4f}  "
              f"eigvec = ({eigvecs[0,i].item():.3f}, {eigvecs[1,i].item():.3f}, "
              f"{eigvecs[2,i].item():.3f})")

    print(f"  ω direction: ({wh[0].item():.3f}, {wh[1].item():.3f}, {wh[2].item():.3f})")

    # Now evolve 1 step and see what changes
    print("\n  After 200 steps (t=0.1):")
    wx_h2, wy_h2, wz_h2 = ic_tg(solver)
    for step in range(200):
        wx_h2, wy_h2, wz_h2 = solver.step_rk4(wx_h2, wy_h2, wz_h2, dt)

    wx2 = solver.ifft(D * wx_h2)
    wy2 = solver.ifft(D * wy_h2)
    wz2 = solver.ifft(D * wz_h2)
    om2 = (wx2**2 + wy2**2 + wz2**2).sqrt()
    flat_idx2 = om2.flatten().argmax().item()
    iz2 = flat_idx2 % N_
    iy2 = (flat_idx2 // N_) % N_
    ix2 = flat_idx2 // (N_ * N_)

    ux_h2, uy_h2, uz_h2 = solver.vel_from_vort(wx_h2, wy_h2, wz_h2)
    Smat2 = torch.zeros(3, 3, dtype=DTYPE)
    u_hats2 = [ux_h2, uy_h2, uz_h2]
    for i in range(3):
        for j in range(3):
            duidxj = solver.ifft(1j * k_dirs[j] * D * u_hats2[i])
            Smat2[i, j] += duidxj[ix2, iy2, iz2]
    Smat2 = 0.5 * (Smat2 + Smat2.T)

    eigvals2, eigvecs2 = torch.linalg.eigh(Smat2)
    w_vec2 = torch.tensor([wx2[ix2,iy2,iz2], wy2[ix2,iy2,iz2], wz2[ix2,iy2,iz2]], dtype=DTYPE)
    wh2 = w_vec2 / w_vec2.norm()

    print(f"  Max |ω| at ({ix2},{iy2},{iz2}), |ω|={om2[ix2,iy2,iz2].item():.4f}")
    print(f"  Strain eigenvalues: λ₁={eigvals2[2].item():.4f}, "
          f"λ₂={eigvals2[1].item():.4f}, λ₃={eigvals2[0].item():.4f}")

    for i, name in [(2, 'e₁'), (1, 'e₂'), (0, 'e₃')]:
        cos2 = (wh2 @ eigvecs2[:, i]).item()**2
        print(f"  cos²(ω, {name}) = {cos2:.4f}")

    print(f"\n{'='*70}")
    print("DONE.")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
