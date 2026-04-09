"""
Fluid logic gate: wall geometry that amplifies vorticity.

Gate design: converging nozzle between walls.
- Wide entrance: vortex tube enters at low intensity
- Narrow throat: cross-section shrinks, flow accelerates, vortex stretches
- Wide exit: feeds into next cell (periodic)

If the stretching through the throat > diffusion loss, gain > 1.
Tile this = cascade = blowup.

Gate types:
1. NOZZLE — hourglass walls, vortex tube along axis
2. SPLITTER — one tube enters, two exit (1→2 = gain 2 in topology)
3. COLLISION — two tubes collide head-on at a wall (maximum stagnation strain)
"""
import torch
import math
import time
import json
import os

sys_path = __import__('sys')
sys_path.path.insert(0, os.path.dirname(__file__))
from ns3d_spectral import NS3DSpectral


class FluidGate(NS3DSpectral):
    """3D NS with wall geometry for logic gate experiments."""

    def __init__(self, N=48, nu=0, device='cuda', gate_type='nozzle',
                 wall_eps=0.002, throat_ratio=0.3):
        super().__init__(N=N, nu=nu, device=device)
        self.wall_eps = wall_eps
        self.gate_type = gate_type
        self.throat_ratio = throat_ratio

        # Store ik for derivatives (parent doesn't)
        self.ikx = 1j * self.kx
        self.iky = 1j * self.ky
        self.ikz = 1j * self.kz

        pi = math.pi
        X, Y, Z = self.X, self.Y, self.Z

        # Radial distance from center axis (z-axis through domain center)
        r = torch.sqrt((X - pi)**2 + (Y - pi)**2)

        if gate_type == 'nozzle':
            # Hourglass: wall radius varies with z
            # Wide at z=0,2π (radius = pi*0.9), narrow at z=π (radius = pi*throat_ratio)
            r_wall = pi * (throat_ratio + (1 - throat_ratio) * torch.cos((Z - pi))**2)
            # Wider version: smooth sigmoid transition
            self.fluid_mask = torch.sigmoid((r_wall - r) / (pi * 0.05))

        elif gate_type == 'collision':
            # Two nozzles pointing at each other, meeting at z=π
            # Left half: converging from z=0 to z=π
            # Right half: converging from z=2π to z=π
            dist_to_center = (Z - pi).abs()
            r_wall = pi * (throat_ratio + (1 - throat_ratio) * (dist_to_center / pi).clamp(max=1)**2)
            self.fluid_mask = torch.sigmoid((r_wall - r) / (pi * 0.05))

        elif gate_type == 'splitter':
            # Single channel splits into two: Y-junction
            # Main channel along z, splits at z=π into upper and lower
            r_main = torch.sqrt((X - pi)**2 + (Y - pi)**2)
            split_offset = pi * 0.4 * ((Z - pi) / pi).clamp(min=0)
            r_upper = torch.sqrt((X - pi)**2 + (Y - pi - split_offset)**2)
            r_lower = torch.sqrt((X - pi)**2 + (Y - pi + split_offset)**2)
            r_channel = torch.where(Z < pi, r_main,
                                    torch.min(r_upper, r_lower))
            r_wall_s = pi * throat_ratio * 1.5
            self.fluid_mask = torch.sigmoid((r_wall_s - r_channel) / (pi * 0.05))

        elif gate_type == 'multi_nozzle':
            # Multiple nozzles in series: 3 throats along z
            r_wall = pi * 0.9
            for k in range(3):
                z_throat = pi * (0.5 + k * 0.5)  # at z = π/2, π, 3π/2
                local_squeeze = (1 - throat_ratio) * torch.exp(-((Z - z_throat) / (pi * 0.15))**2)
                r_wall = r_wall - pi * local_squeeze
            self.fluid_mask = torch.sigmoid((r_wall - r) / (pi * 0.05))

        else:
            self.fluid_mask = torch.ones_like(X)

        self.wall_mask = 1.0 - self.fluid_mask
        pct = self.fluid_mask.mean().item() * 100
        print(f"Gate: {gate_type}, throat={throat_ratio}, fluid={pct:.1f}%")

    def rhs_with_wall(self, wx_hat, wy_hat, wz_hat):
        """Standard RHS + velocity penalization via Brinkman."""
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

        # Penalize velocity inside walls BEFORE computing stretching
        # This ensures the velocity field respects the walls
        ux_p = ux * self.fluid_mask
        uy_p = uy * self.fluid_mask
        uz_p = uz * self.fluid_mask

        # Recompute velocity hat with penalized velocity
        ux_p_hat = D * fft(ux_p)
        uy_p_hat = D * fft(uy_p)
        uz_p_hat = D * fft(uz_p)

        # Velocity gradients from penalized velocity
        dux_dx=ifft(ikx*ux_p_hat); dux_dy=ifft(iky*ux_p_hat); dux_dz=ifft(ikz*ux_p_hat)
        duy_dx=ifft(ikx*uy_p_hat); duy_dy=ifft(iky*uy_p_hat); duy_dz=ifft(ikz*uy_p_hat)
        duz_dx=ifft(ikx*uz_p_hat); duz_dy=ifft(iky*uz_p_hat); duz_dz=ifft(ikz*uz_p_hat)

        # Stretching with penalized velocity
        sx = wx*dux_dx+wy*dux_dy+wz*dux_dz
        sy = wx*duy_dx+wy*duy_dy+wz*duy_dz
        sz = wx*duz_dx+wy*duz_dy+wz*duz_dz

        # Advection with penalized velocity
        dwx_dx=ifft(ikx*wx_hat*D); dwx_dy=ifft(iky*wx_hat*D); dwx_dz=ifft(ikz*wx_hat*D)
        dwy_dx=ifft(ikx*wy_hat*D); dwy_dy=ifft(iky*wy_hat*D); dwy_dz=ifft(ikz*wy_hat*D)
        dwz_dx=ifft(ikx*wz_hat*D); dwz_dy=ifft(iky*wz_hat*D); dwz_dz=ifft(ikz*wz_hat*D)

        ax = ux_p*dwx_dx+uy_p*dwx_dy+uz_p*dwx_dz
        ay = ux_p*dwy_dx+uy_p*dwy_dy+uz_p*dwy_dz
        az = ux_p*dwz_dx+uy_p*dwz_dy+uz_p*dwz_dz

        # Direct wall damping on vorticity inside walls (gentle)
        wall_damp_x = -(1.0/self.wall_eps) * self.wall_mask * wx
        wall_damp_y = -(1.0/self.wall_eps) * self.wall_mask * wy
        wall_damp_z = -(1.0/self.wall_eps) * self.wall_mask * wz

        rx = D*fft(sx - ax + wall_damp_x) - self.nu*ksq*wx_hat
        ry = D*fft(sy - ay + wall_damp_y) - self.nu*ksq*wy_hat
        rz = D*fft(sz - az + wall_damp_z) - self.nu*ksq*wz_hat

        return rx, ry, rz

    def step_gate(self, wx, wy, wz, dt):
        """RK4 with wall-aware RHS."""
        def add(a,b,s):
            return (a[0]+s*b[0], a[1]+s*b[1], a[2]+s*b[2])
        w = (wx,wy,wz)
        k1 = self.rhs_with_wall(*w)
        k2 = self.rhs_with_wall(*add(w,k1,0.5*dt))
        k3 = self.rhs_with_wall(*add(w,k2,0.5*dt))
        k4 = self.rhs_with_wall(*add(w,k3,dt))
        return (wx+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
                wy+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),
                wz+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def enstrophy_fluid(self, wx_hat, wy_hat, wz_hat):
        """Enstrophy only in fluid region."""
        wx = torch.fft.ifftn(wx_hat).real * self.fluid_mask
        wy = torch.fft.ifftn(wy_hat).real * self.fluid_mask
        wz = torch.fft.ifftn(wz_hat).real * self.fluid_mask
        return (wx**2 + wy**2 + wz**2).sum().item()


def make_tube_ic(gate, amp=50.0):
    """Vortex tube along z-axis (the gate's flow direction)."""
    X, Y, Z = gate.X, gate.Y, gate.Z
    pi = math.pi

    # Gaussian vortex tube centered on z-axis
    r = torch.sqrt((X - pi)**2 + (Y - pi)**2)
    sigma = pi * 0.15  # tube radius

    # Vorticity along z
    wz = amp * torch.exp(-r**2 / (2*sigma**2)) * gate.fluid_mask
    wx = torch.zeros_like(wz)
    wy = torch.zeros_like(wz)

    return (gate.dealias * torch.fft.fftn(wx),
            gate.dealias * torch.fft.fftn(wy),
            gate.dealias * torch.fft.fftn(wz))


def make_azimuthal_ic(gate, amp=50.0):
    """Azimuthal vorticity — swirl around the z-axis (Luo-Hou style)."""
    X, Y, Z = gate.X, gate.Y, gate.Z
    pi = math.pi

    r = torch.sqrt((X - pi)**2 + (Y - pi)**2)
    r_norm = r / pi

    # Azimuthal velocity: peaks near the wall
    u_theta = amp * torch.exp(-10*(1 - r_norm**2).clamp(min=0)**2) * torch.sin(2*Z)
    u_theta *= gate.fluid_mask

    theta = torch.atan2(Y - pi, X - pi)
    ux = -u_theta * torch.sin(theta)
    uy = u_theta * torch.cos(theta)
    uz = torch.zeros_like(ux)

    ux_hat = gate.dealias * torch.fft.fftn(ux)
    uy_hat = gate.dealias * torch.fft.fftn(uy)
    uz_hat = gate.dealias * torch.fft.fftn(uz)

    return gate.curl(ux_hat, uy_hat, uz_hat)


def run_gate(gate_type, throat_ratio, ic_type, amp, N=48, nu=0,
             n_steps=2000, dt=0.001, device='cuda'):
    """Run one gate experiment and return the score."""
    gate = FluidGate(N=N, nu=nu, device=device, gate_type=gate_type,
                     throat_ratio=throat_ratio)

    if ic_type == 'tube':
        wx,wy,wz = make_tube_ic(gate, amp=amp)
    elif ic_type == 'azimuthal':
        wx,wy,wz = make_azimuthal_ic(gate, amp=amp)
    else:
        return None

    e0 = gate.enstrophy_fluid(wx,wy,wz)
    om0 = gate.omega_max(wx,wy,wz)

    if e0 < 1e-20 or om0 < 1e-10:
        return {'score': 0, 'growth': 0, 'om_peak': 0}

    e_peak = e0
    om_peak = om0
    t = 0
    t0_clock = time.time()

    # Adaptive dt based on max velocity
    dt_use = min(dt, 0.3 * gate.dx / (om0 + 1))

    for step in range(n_steps):
        wx,wy,wz = gate.step_gate(wx,wy,wz, dt_use)
        t += dt_use

        if step % 100 == 0:
            om = gate.omega_max(wx,wy,wz)
            e = gate.enstrophy_fluid(wx,wy,wz)
            e_peak = max(e_peak, e)
            om_peak = max(om_peak, om)

            if om > 1e5:
                break
            if om < om0 * 0.001 and step > 200:
                break

    growth = e_peak / (e0 + 1e-30)
    om_growth = om_peak / (om0 + 1e-30)
    elapsed = time.time() - t0_clock

    # Score: combination of enstrophy growth and vorticity concentration
    score = growth * om_growth

    return {
        'score': score,
        'growth': growth,
        'om_growth': om_growth,
        'om_peak': om_peak,
        'elapsed': elapsed,
    }


def main():
    N = 48
    nu = 0  # Euler first
    device = 'cuda'

    print("=" * 60)
    print("FLUID LOGIC GATE EXPERIMENTS")
    print(f"N={N}³, ν={nu}")
    print("=" * 60)

    configs = []

    # Sweep gate types × throat ratios × IC types × amplitudes
    for gate_type in ['nozzle', 'collision', 'multi_nozzle']:
        for throat in [0.15, 0.25, 0.4]:
            for ic_type in ['tube', 'azimuthal']:
                for amp in [20, 50, 100]:
                    configs.append({
                        'gate': gate_type, 'throat': throat,
                        'ic': ic_type, 'amp': amp,
                    })

    print(f"{len(configs)} configurations\n")

    results = []
    t0 = time.time()

    for i, cfg in enumerate(configs):
        result = run_gate(cfg['gate'], cfg['throat'], cfg['ic'], cfg['amp'],
                          N=N, nu=nu, n_steps=1500, device=device)

        if result:
            result.update(cfg)
            results.append(result)

            marker = ' ***' if result['score'] > 2 else ''
            elapsed = time.time() - t0
            print(f"[{i+1}/{len(configs)}] {cfg['gate']:12s} t={cfg['throat']:.2f} "
                  f"{cfg['ic']:9s} A={cfg['amp']:3d} → "
                  f"score={result['score']:.4f} growth={result['growth']:.4f}× "
                  f"|ω|peak={result['om_peak']:.2f}{marker} [{elapsed:.0f}s]",
                  flush=True)

    # Scoreboard
    results.sort(key=lambda r: r['score'], reverse=True)
    print(f"\n{'='*60}")
    print(f"SCOREBOARD — TOP 10")
    print(f"{'='*60}")
    for i, r in enumerate(results[:10]):
        print(f"  {i+1}. {r['gate']:12s} t={r['throat']:.2f} {r['ic']:9s} A={r['amp']:3d} "
              f"score={r['score']:.4f} growth={r['growth']:.4f}× |ω|={r['om_peak']:.2f}")

    n_amplify = sum(1 for r in results if r['growth'] > 1.5)
    print(f"\nAmplifiers (growth > 1.5×): {n_amplify}/{len(results)}")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"logic_gate_N{N}_nu{nu:.0e}.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
