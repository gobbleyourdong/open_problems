"""
Dynamic Tube Lattice — WITH back-reaction.

The tubes now RESPOND to the strain they experience:
1. Circulation evolves: dΓ/dt = α×Γ - ν/σ²×Γ (stretching vs decay)
2. Direction evolves: dê/dt = (I-ê⊗ê)·S·ê (strain rotates the direction)
3. Core radius evolves: dσ/dt = -α×σ/2 (stretching thins the tube, det=1)

The back-reaction: stretching rotates directions (anti-twist),
which CHANGES the mutual strain, which REDUCES amplification.

Does the amplification survive the dynamics?
"""
import torch
import math
import numpy as np
import time

torch.set_default_dtype(torch.float64)


def run_dynamic_lattice():
    print("=" * 70)
    print("DYNAMIC TUBE LATTICE — WITH BACK-REACTION")
    print("Does amplification survive when tubes respond to strain?")
    print("=" * 70, flush=True)

    nu = 1e-4
    L = 2 * math.pi

    for config_name, n_tubes, setup_fn in [
        ("2 tubes at 85°", 2, "two_tubes"),
        ("5 perpendicular cascade", 5, "cascade"),
        ("10 optimal chain", 10, "optimal"),
    ]:
        print(f"\n--- {config_name} ---", flush=True)

        # Initialize
        positions = torch.zeros(n_tubes, 3)
        directions = torch.zeros(n_tubes, 3)
        circulations = torch.ones(n_tubes) * 10.0
        sigmas = torch.ones(n_tubes) * 0.3  # core radii

        if setup_fn == "two_tubes":
            positions[0] = torch.tensor([0.0, 0.0, 0.0])
            positions[1] = torch.tensor([1.0, 0.0, 0.0])
            angle = math.radians(85)
            directions[0] = torch.tensor([0.0, 0.0, 1.0])
            directions[1] = torch.tensor([math.sin(angle), 0.0, math.cos(angle)])

        elif setup_fn == "cascade":
            for i in range(n_tubes):
                positions[i] = torch.tensor([i * L / n_tubes, L/2, L/2])
                if i % 3 == 0:
                    directions[i] = torch.tensor([1.0, 0.0, 0.0])
                elif i % 3 == 1:
                    directions[i] = torch.tensor([0.0, 1.0, 0.0])
                else:
                    directions[i] = torch.tensor([0.0, 0.0, 1.0])

        elif setup_fn == "optimal":
            angle = math.radians(85)
            for i in range(n_tubes):
                positions[i] = torch.tensor([i * 0.5, L/2, L/2])
                theta = i * angle
                directions[i] = torch.tensor([math.cos(theta), math.sin(theta), 0.0])

        # Normalize directions
        for i in range(n_tubes):
            directions[i] = directions[i] / directions[i].norm()

        def compute_strain_on_tube(i):
            """Compute the strain tensor S at tube i from all other tubes."""
            e_i = directions[i]
            alpha_total = 0.0
            S_perp = torch.zeros(3)  # perpendicular strain component for direction rotation

            for j in range(n_tubes):
                if i == j:
                    continue  # SINGLE-MODE ORTHOGONALITY

                e_j = directions[j]
                r = positions[i] - positions[j]
                r = r - L * torch.round(r / L)  # periodic
                dist = r.norm().item() + 1e-10
                Gamma_j = circulations[j].item()
                sigma_j = sigmas[j].item()

                reg = 1.0 - math.exp(-dist**2 / (2*sigma_j**2))
                strain_mag = Gamma_j / (2*math.pi * dist**2) * reg

                # Component of ê_i perpendicular to ê_j
                e_i_par = (e_i @ e_j) * e_j
                e_i_perp = e_i - e_i_par
                sin2 = (e_i_perp @ e_i_perp).item()

                if sin2 < 1e-20:
                    continue

                # Perpendicular distance direction
                r_perp = r - (r @ e_j) * e_j
                r_perp_mag = r_perp.norm().item()
                if r_perp_mag < 1e-10:
                    continue

                r_perp_hat = r_perp / r_perp_mag
                e_i_perp_hat = e_i_perp / math.sqrt(sin2)
                cos_phi = (e_i_perp_hat @ r_perp_hat).item()
                cos_2phi = 2*cos_phi**2 - 1

                alpha_ij = strain_mag * sin2 * cos_2phi
                alpha_total += alpha_ij

                # Direction rotation: (I - ê⊗ê)·S·ê
                # The strain from tube j rotates ê_i in the perpendicular plane
                # dê_i/dt contribution from tube j: proportional to strain_mag × sin × cos
                # Direction: toward the stretching eigenvector of S_j
                rotation_mag = strain_mag * math.sqrt(sin2) * cos_phi
                S_perp += rotation_mag * e_i_perp_hat

            return alpha_total, S_perp

        # Evolution
        dt = 0.001
        n_steps = 10000
        Gamma_max_init = circulations.abs().max().item()

        print(f"  {'t':>6} {'Γ_max':>10} {'ratio':>8} {'σ_min':>8} {'max_angle_change':>16}", flush=True)

        initial_directions = directions.clone()
        blew_up = False
        final_ratio = 0

        for step in range(n_steps):
            if step % 1000 == 0:
                Gamma_max = circulations.abs().max().item()
                sigma_min = sigmas.min().item()
                # Angle change from initial
                max_angle_change = 0.0
                for i in range(n_tubes):
                    cos_angle = (directions[i] @ initial_directions[i]).item()
                    cos_angle = max(-1, min(1, cos_angle))
                    angle_change = math.degrees(math.acos(cos_angle))
                    max_angle_change = max(max_angle_change, angle_change)

                ratio = Gamma_max / Gamma_max_init
                print(f"  {step*dt:6.2f} {Gamma_max:10.4f} {ratio:8.4f} {sigma_min:8.4f} {max_angle_change:16.2f}°",
                      flush=True)

                if Gamma_max > 1e10 or math.isnan(Gamma_max):
                    blew_up = True
                    print(f"  → BLOWUP at t={step*dt:.2f}")
                    break

                if Gamma_max < 0.01:
                    print(f"  → FULLY DEPLETED at t={step*dt:.2f}")
                    break

                final_ratio = ratio

            # Compute strains
            alphas = []
            S_perps = []
            for i in range(n_tubes):
                alpha_i, S_perp_i = compute_strain_on_tube(i)
                alphas.append(alpha_i)
                S_perps.append(S_perp_i)

            # Update all tubes
            for i in range(n_tubes):
                # 1. Circulation: dΓ/dt = α×Γ - ν/σ²×Γ
                decay = nu / (sigmas[i].item()**2)
                dGamma = (alphas[i] - decay) * circulations[i].item()
                circulations[i] += dt * dGamma

                # 2. Direction: dê/dt = S_perp (the perpendicular strain rotates ê)
                de = S_perps[i] * dt
                directions[i] += de
                # Re-normalize
                norm = directions[i].norm()
                if norm > 1e-10:
                    directions[i] /= norm

                # 3. Core radius: dσ/dt = -α×σ/2 (stretching thins, compression fattens)
                dsigma = -alphas[i] * sigmas[i].item() / 2 * dt
                sigmas[i] += dsigma
                sigmas[i] = max(sigmas[i].item(), 0.01)  # minimum core radius
                sigmas[i] = torch.tensor(sigmas[i]) if isinstance(sigmas[i], float) else sigmas[i]

        if not blew_up:
            Gamma_max = circulations.abs().max().item()
            final_ratio = Gamma_max / Gamma_max_init
            max_angle_change = 0.0
            for i in range(n_tubes):
                cos_a = max(-1, min(1, (directions[i] @ initial_directions[i]).item()))
                max_angle_change = max(max_angle_change, math.degrees(math.acos(cos_a)))

            print(f"\n  FINAL: ratio={final_ratio:.6f}, max direction change={max_angle_change:.1f}°")
            if final_ratio > 1.01:
                print(f"  → AMPLIFICATION SURVIVES BACK-REACTION")
            elif final_ratio < 0.99:
                print(f"  → DEPLETION WINS — back-reaction kills amplification")
            else:
                print(f"  → MARGINAL — approximately stable")

    print(f"\n{'='*70}")
    print(f"THE QUESTION: Does the anti-twist (direction rotation)")
    print(f"destroy the amplification that the static model predicted?")
    print(f"{'='*70}", flush=True)


if __name__ == '__main__':
    run_dynamic_lattice()
