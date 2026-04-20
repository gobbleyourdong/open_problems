"""
Domino search WITH WALLS — penalization method.

Add soft cylindrical walls inside periodic cells to trap vorticity.
Sweep curl noise ICs + wall configurations.
Score by enstrophy growth rate.

The wall is the missing ingredient — every proven Euler blowup uses one.
"""
import torch
import math
import time
import json
import os


class NS3DWalled:
    """3D NS with penalized wall boundaries."""

    def __init__(self, N=32, nu=0, device='cuda', wall_r=0.8, wall_eps=0.01, wall_width=0.1):
        self.N = N
        self.nu = nu
        self.device = device
        self.dtype = torch.float64
        self.wall_eps = wall_eps  # penalization strength (smaller = harder wall)

        Lx = 2 * math.pi
        self.Lx = Lx
        dx = Lx / N
        self.dx = dx

        k = torch.fft.fftfreq(N, d=dx/(2*math.pi)).to(device=device, dtype=self.dtype)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0

        kmax = N // 3
        self.dealias = ((self.kx.abs() < kmax) &
                        (self.ky.abs() < kmax) &
                        (self.kz.abs() < kmax)).to(self.dtype)

        self.ikx = 1j * self.kx
        self.iky = 1j * self.ky
        self.ikz = 1j * self.kz

        x = torch.linspace(0, Lx - dx, N, device=device, dtype=self.dtype)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')

        # Cylindrical wall centered at (pi, pi), axis along z
        pi = math.pi
        r = torch.sqrt((self.X - pi)**2 + (self.Y - pi)**2)
        # Smooth wall: 1 inside fluid (r < wall_r), 0 inside solid
        self.fluid_mask = torch.sigmoid((wall_r * pi - r) / (wall_width * pi))
        # Wall mask is complement
        self.wall_mask = 1.0 - self.fluid_mask

        pct_fluid = self.fluid_mask.mean().item() * 100
        print(f"NS3D Walled: N={N}³, ν={nu:.1e}, wall_r={wall_r}, eps={wall_eps}")
        print(f"  Fluid fraction: {pct_fluid:.1f}%")

    def rhs(self, wx_hat, wy_hat, wz_hat):
        D = self.dealias
        ikx, iky, ikz = self.ikx, self.iky, self.ikz
        ksq = self.ksq

        # Biot-Savart
        px = wx_hat/ksq; py = wy_hat/ksq; pz = wz_hat/ksq
        px[0,0,0]=0; py[0,0,0]=0; pz[0,0,0]=0

        ux_hat = iky*pz - ikz*py
        uy_hat = ikz*px - ikx*pz
        uz_hat = ikx*py - iky*px

        ifft = lambda f: torch.fft.ifftn(f*D).real
        fft = torch.fft.fftn

        ux,uy,uz = ifft(ux_hat), ifft(uy_hat), ifft(uz_hat)
        wx,wy,wz = ifft(wx_hat*D), ifft(wy_hat*D), ifft(wz_hat*D)

        # Velocity gradients
        dux_dx=ifft(ikx*ux_hat*D); dux_dy=ifft(iky*ux_hat*D); dux_dz=ifft(ikz*ux_hat*D)
        duy_dx=ifft(ikx*uy_hat*D); duy_dy=ifft(iky*uy_hat*D); duy_dz=ifft(ikz*uy_hat*D)
        duz_dx=ifft(ikx*uz_hat*D); duz_dy=ifft(iky*uz_hat*D); duz_dz=ifft(ikz*uz_hat*D)

        # Stretching - advection
        nl_x = (wx*dux_dx+wy*dux_dy+wz*dux_dz) - (ux*ifft(ikx*wx_hat*D)+uy*ifft(iky*wx_hat*D)+uz*ifft(ikz*wx_hat*D))
        nl_y = (wx*duy_dx+wy*duy_dy+wz*duy_dz) - (ux*ifft(ikx*wy_hat*D)+uy*ifft(iky*wy_hat*D)+uz*ifft(ikz*wy_hat*D))
        nl_z = (wx*duz_dx+wy*duz_dy+wz*duz_dz) - (ux*ifft(ikx*wz_hat*D)+uy*ifft(iky*wz_hat*D)+uz*ifft(ikz*wz_hat*D))

        # Wall penalization: drive VELOCITY to zero inside wall
        # Vorticity is FREE — it's generated at the wall surface naturally
        # The Brinkman penalization acts on the momentum equation
        vel_pen_x = -(1.0/self.wall_eps) * self.wall_mask * ux
        vel_pen_y = -(1.0/self.wall_eps) * self.wall_mask * uy
        vel_pen_z = -(1.0/self.wall_eps) * self.wall_mask * uz

        # Convert velocity penalty to vorticity penalty via curl
        # curl(penalty) adds to dω/dt
        vp_x_hat = D * fft(vel_pen_x)
        vp_y_hat = D * fft(vel_pen_y)
        vp_z_hat = D * fft(vel_pen_z)
        curl_pen_x = iky*vp_z_hat - ikz*vp_y_hat
        curl_pen_y = ikz*vp_x_hat - ikx*vp_z_hat
        curl_pen_z = ikx*vp_y_hat - iky*vp_x_hat

        rx = D*fft(nl_x) + curl_pen_x - self.nu*ksq*wx_hat
        ry = D*fft(nl_y) + curl_pen_y - self.nu*ksq*wy_hat
        rz = D*fft(nl_z) + curl_pen_z - self.nu*ksq*wz_hat

        return rx, ry, rz

    def step_rk4(self, wx, wy, wz, dt):
        def add(a,b,s):
            return (a[0]+s*b[0], a[1]+s*b[1], a[2]+s*b[2])
        w = (wx,wy,wz)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w,k1,0.5*dt))
        k3 = self.rhs(*add(w,k2,0.5*dt))
        k4 = self.rhs(*add(w,k3,dt))
        return (wx+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                wy+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                wz+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def enstrophy(self, wx_hat, wy_hat, wz_hat):
        wx = torch.fft.ifftn(wx_hat).real * self.fluid_mask
        wy = torch.fft.ifftn(wy_hat).real * self.fluid_mask
        wz = torch.fft.ifftn(wz_hat).real * self.fluid_mask
        return (wx**2 + wy**2 + wz**2).mean().item()

    def omega_max(self, wx_hat, wy_hat, wz_hat):
        wx = torch.fft.ifftn(wx_hat).real * self.fluid_mask
        wy = torch.fft.ifftn(wy_hat).real * self.fluid_mask
        wz = torch.fft.ifftn(wz_hat).real * self.fluid_mask
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()


def make_walled_ic(solver, seed, amp=20.0):
    """Curl noise IC masked to fluid region."""
    torch.manual_seed(seed)
    N = solver.N
    dev = solver.device

    kmax = N // 2
    mask_k = solver.ksq <= kmax**2
    mag = amp / (solver.ksq + 1)
    mag[0,0,0] = 0

    Ax = mag * mask_k * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
    Ay = mag * mask_k * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))
    Az = mag * mask_k * (torch.randn(N,N,N,device=dev) + 1j*torch.randn(N,N,N,device=dev))

    ikx,iky,ikz = solver.ikx, solver.iky, solver.ikz
    ux_hat = iky*Az - ikz*Ay
    uy_hat = ikz*Ax - ikx*Az
    uz_hat = ikx*Ay - iky*Ax

    wx_hat = iky*uz_hat - ikz*uy_hat
    wy_hat = ikz*ux_hat - ikx*uz_hat
    wz_hat = ikx*uy_hat - iky*ux_hat

    # Mask to fluid region in physical space, then back to Fourier
    wx = torch.fft.ifftn(wx_hat).real * solver.fluid_mask
    wy = torch.fft.ifftn(wy_hat).real * solver.fluid_mask
    wz = torch.fft.ifftn(wz_hat).real * solver.fluid_mask

    return (solver.dealias*torch.fft.fftn(wx),
            solver.dealias*torch.fft.fftn(wy),
            solver.dealias*torch.fft.fftn(wz))


def make_luo_hou_3d(solver, amp=100.0):
    """Luo-Hou style IC: azimuthal velocity concentrated near the wall."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    r = torch.sqrt((X - pi)**2 + (Y - pi)**2)
    r_norm = r / (solver.Lx / 2)  # normalize

    u_theta = amp * torch.exp(-30*(1 - r_norm**2).clamp(min=0)**4) * torch.sin(2*Z)
    u_theta *= solver.fluid_mask

    theta = torch.atan2(Y - pi, X - pi)
    ux = -u_theta * torch.sin(theta)
    uy = u_theta * torch.cos(theta)
    uz = torch.zeros_like(ux)

    ux_hat = solver.dealias * torch.fft.fftn(ux)
    uy_hat = solver.dealias * torch.fft.fftn(uy)
    uz_hat = solver.dealias * torch.fft.fftn(uz)

    wx_hat = solver.iky*uz_hat - solver.ikz*uy_hat
    wy_hat = solver.ikz*ux_hat - solver.ikx*uz_hat
    wz_hat = solver.ikx*uy_hat - solver.iky*ux_hat

    return wx_hat, wy_hat, wz_hat


def run_experiment(N=32, nu=0, n_seeds=200, n_steps=500, device='cuda',
                   wall_r=0.8, wall_eps=0.01):
    """Run the walled domino search."""
    solver = NS3DWalled(N=N, nu=nu, device=device, wall_r=wall_r, wall_eps=wall_eps)

    print(f"\n--- Euler (ν={nu}) with wall (r={wall_r}) ---")

    # First: test Luo-Hou IC
    print(f"\nLuo-Hou 3D walled IC:")
    wx,wy,wz = make_luo_hou_3d(solver, amp=100.0)
    e0 = solver.enstrophy(wx,wy,wz)
    om0 = solver.omega_max(wx,wy,wz)
    print(f"  IC: |ω|={om0:.2f}, enst={e0:.0f}")

    dt = min(0.3 * solver.dx / (om0 + 1), wall_eps * 0.5, 0.005)
    t = 0; t0 = time.time()
    e_peak = e0; om_peak = om0

    for step in range(n_steps):
        wx,wy,wz = solver.step_rk4(wx,wy,wz, dt)
        t += dt
        if step % 100 == 0:
            om = solver.omega_max(wx,wy,wz)
            e = solver.enstrophy(wx,wy,wz)
            e_peak = max(e_peak, e)
            om_peak = max(om_peak, om)
            elapsed = time.time() - t0
            print(f"  step={step:4d} t={t:.4f} |ω|={om:.2f} enst={e:.0f} "
                  f"[{elapsed:.0f}s]", flush=True)
            if om > 1e5:
                print(f"  BLOWUP!")
                break

    growth = e_peak / (e0 + 1e-30)
    print(f"  Luo-Hou growth: {growth:.4f}×, |ω| peak: {om_peak:.2f}")

    # Then: sweep curl noise ICs
    print(f"\nCurl noise sweep ({n_seeds} seeds):")
    results = []
    t0 = time.time()

    for seed in range(n_seeds):
        amp = 20.0 * (1 + seed % 5)
        wx,wy,wz = make_walled_ic(solver, seed, amp=amp)
        e0 = solver.enstrophy(wx,wy,wz)
        if e0 < 1e-20:
            continue

        e_peak = e0
        om_peak = solver.omega_max(wx,wy,wz)

        dt_ic = min(0.3 * solver.dx / (om_peak + 1), wall_eps * 0.5, 0.005)
        for step in range(n_steps):
            wx,wy,wz = solver.step_rk4(wx,wy,wz, dt_ic)
            if step % 50 == 0:
                e = solver.enstrophy(wx,wy,wz)
                om = solver.omega_max(wx,wy,wz)
                e_peak = max(e_peak, e)
                om_peak = max(om_peak, om)
                if om > 1e5:
                    break

        growth = e_peak / (e0 + 1e-30)
        results.append({'seed': seed, 'amp': amp, 'growth': growth, 'om_peak': om_peak})

        if (seed+1) % 50 == 0:
            elapsed = time.time() - t0
            tops = sorted(results, key=lambda r:r['growth'], reverse=True)[:3]
            top_str = ' '.join(f"s{r['seed']}:{r['growth']:.2f}×" for r in tops)
            print(f"  [{seed+1}/{n_seeds}] {elapsed:.0f}s | top: {top_str}", flush=True)

    results.sort(key=lambda r: r['growth'], reverse=True)
    n_amp = sum(1 for r in results if r['growth'] > 1.5)

    print(f"\nTOP 10:")
    for i,r in enumerate(results[:10]):
        print(f"  {i+1}. seed={r['seed']} amp={r['amp']:.0f} growth={r['growth']:.4f}× |ω|peak={r['om_peak']:.2f}")
    print(f"Growth > 1.5: {n_amp}/{len(results)}")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"domino_walled_N{N}_nu{nu:.0e}.json")
    with open(out_path, "w") as f:
        json.dump(results[:50], f, indent=2)
    print(f"Saved: {out_path}")

    return results


if __name__ == '__main__':
    # Euler first (ν=0) — can we blow up?
    run_experiment(N=32, nu=0, n_seeds=200, n_steps=500, device='cuda')

    # Then NS (ν=1e-4) — does viscosity kill the best candidates?
    run_experiment(N=32, nu=1e-4, n_seeds=200, n_steps=500, device='cuda')
