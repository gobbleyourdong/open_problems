"""
Tube Lattice Model — Isolate the cascade geometry.

A finite array of vortex tubes on T³ with controllable orientations.
Each tube: position, direction (θ,φ), circulation Γ, core radius σ.

The Biot-Savart interaction gives mutual strain between tubes.
Single-mode orthogonality: each tube's self-strain has zero projection
on its own axis (built in by construction).

Question: can the adversary choose angles to create an amplifying cascade?
Or does ⊥ force depletion at every step?

Three experiments:
1. Random orientations — generic case
2. Optimized orientations — adversary's best shot
3. Cascade chain — designed to maximize sequential transfer
"""
import torch
import math
import numpy as np
import json
import os
import time

torch.set_default_dtype(torch.float64)


class TubeLattice:
    """A collection of vortex tubes interacting via Biot-Savart."""

    def __init__(self, n_tubes, tube_length=2*math.pi, core_radius=0.3, nu=1e-4):
        self.n = n_tubes
        self.L = tube_length
        self.sigma = core_radius
        self.nu = nu

        # Each tube: position (x,y,z), direction (unit vector), circulation Γ
        self.positions = torch.zeros(n_tubes, 3)
        self.directions = torch.zeros(n_tubes, 3)
        self.circulations = torch.ones(n_tubes)

    def set_random_config(self, seed=0):
        """Random positions and orientations."""
        torch.manual_seed(seed)
        self.positions = torch.rand(self.n, 3) * self.L
        # Random directions on S²
        theta = torch.acos(2*torch.rand(self.n) - 1)
        phi = 2*math.pi*torch.rand(self.n)
        self.directions[:, 0] = torch.sin(theta) * torch.cos(phi)
        self.directions[:, 1] = torch.sin(theta) * torch.sin(phi)
        self.directions[:, 2] = torch.cos(theta)
        self.circulations = torch.ones(self.n) * 10.0

    def set_cascade_config(self, n_stages=5):
        """Cascade chain: each tube feeds the next via perpendicular orientation."""
        self.n = n_stages
        self.positions = torch.zeros(n_stages, 3)
        self.directions = torch.zeros(n_stages, 3)
        self.circulations = torch.ones(n_stages) * 10.0

        for i in range(n_stages):
            self.positions[i] = torch.tensor([i * self.L / n_stages, self.L/2, self.L/2])
            # Each tube perpendicular to the previous (maximum mutual stretching)
            if i % 3 == 0:
                self.directions[i] = torch.tensor([1.0, 0.0, 0.0])
            elif i % 3 == 1:
                self.directions[i] = torch.tensor([0.0, 1.0, 0.0])
            else:
                self.directions[i] = torch.tensor([0.0, 0.0, 1.0])

    def set_optimized_cascade(self, n_stages=5, angle=None):
        """Cascade with a specific inter-tube angle to maximize transfer."""
        self.n = n_stages
        self.positions = torch.zeros(n_stages, 3)
        self.directions = torch.zeros(n_stages, 3)
        self.circulations = torch.ones(n_stages) * 10.0

        if angle is None:
            angle = math.pi / 4  # 45° — maximizes the cross product × projection

        for i in range(n_stages):
            self.positions[i] = torch.tensor([i * 0.5, self.L/2, self.L/2])
            theta = i * angle
            self.directions[i] = torch.tensor([math.cos(theta), math.sin(theta), 0.0])

    def biot_savart_strain(self, i, j):
        """Strain induced by tube j on tube i.

        Returns: α_ij = ê_i · S_j · ê_i (stretching rate on tube i from tube j's strain)

        Key property: α_ii = 0 (single-mode orthogonality — self-strain has zero
        projection on own axis).
        """
        if i == j:
            return 0.0  # SINGLE-MODE ORTHOGONALITY (exact)

        e_i = self.directions[i]
        e_j = self.directions[j]
        r = self.positions[i] - self.positions[j]

        # Periodic distance on T³
        r = r - self.L * torch.round(r / self.L)
        dist = r.norm() + 1e-10

        # Biot-Savart: velocity induced by tube j at tube i's location
        # For a straight tube along e_j with circulation Γ_j:
        # u ~ (Γ_j / 2π) × (e_j × r̂) / dist × regularization
        r_hat = r / dist
        Gamma_j = self.circulations[j].item()

        # Regularized Biot-Savart (Gaussian core)
        reg = 1.0 - math.exp(-dist**2 / (2*self.sigma**2))
        u_induced = Gamma_j / (2*math.pi) * torch.cross(e_j, r_hat) / dist * reg

        # Strain from tube j at tube i: S ~ ∂u/∂x
        # The strain tensor from the Biot-Savart field of tube j
        # Simplified: S_j has eigenvectors along (e_j×r̂, r̂, e_j)
        # with eigenvalues proportional to Γ_j/dist²
        # The stretching rate α_ij = ê_i · S_j · ê_i

        # More careful: the velocity gradient from tube j
        # ∂u_k/∂x_l involves derivatives of the BS kernel
        # For a straight tube: the strain perpendicular to e_j scales as Γ/dist²
        # The projection onto ê_i depends on the angle between ê_i and the strain eigenvectors

        # The strain eigenvectors of tube j's field are perpendicular to e_j
        # (SINGLE-MODE ORTHOGONALITY: strain eigenvectors ⊥ vorticity)
        # So the strain acts in the plane ⊥ e_j.
        # The projection ê_i · S_j · ê_i depends on how much ê_i lies in this plane.

        # Component of ê_i perpendicular to ê_j:
        e_i_perp = e_i - (e_i @ e_j) * e_j
        e_i_perp_mag = e_i_perp.norm()

        # Stretching rate: proportional to Γ_j/dist² × sin²(angle between ê_i and ê_j)
        # × cos(2φ) where φ is the azimuthal angle in the perpendicular plane
        sin2_angle = e_i_perp_mag**2  # sin²(angle between ê_i and ê_j)

        # The cos(2φ) factor depends on the direction of r relative to ê_j
        # For the MAXIMUM stretching: cos(2φ) = 1
        # For average over φ: ⟨cos(2φ)⟩ = 0 (random orientation → zero average)
        # We'll compute the actual cos(2φ)

        if e_i_perp_mag < 1e-10:
            return 0.0  # parallel tubes → no stretching (sin²=0)

        e_i_perp_hat = e_i_perp / e_i_perp_mag

        # The perpendicular component of r relative to ê_j
        r_perp = r - (r @ e_j) * e_j
        r_perp_mag = r_perp.norm()
        if r_perp_mag < 1e-10:
            return 0.0

        r_perp_hat = r_perp / r_perp_mag

        # cos(2φ) where φ is angle between ê_i_perp and r_perp in the ⊥ plane
        cos_phi = (e_i_perp_hat @ r_perp_hat).item()
        cos_2phi = 2*cos_phi**2 - 1

        # Full stretching rate
        strain_mag = Gamma_j / (2*math.pi * dist**2) * reg
        alpha_ij = strain_mag * sin2_angle.item() * cos_2phi

        return alpha_ij

    def compute_transfer_matrix(self):
        """Compute the full interaction matrix α_ij."""
        T = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                T[i, j] = self.biot_savart_strain(i, j)
        return T

    def evolve(self, dt=0.01, n_steps=1000):
        """Evolve the tube amplitudes under mutual stretching + viscous decay.

        dΓ_i/dt = α_total_i × Γ_i - ν/σ² × Γ_i

        where α_total_i = Σ_j α_ij (total stretching on tube i)
        and ν/σ² is the viscous decay rate for a Gaussian core.
        """
        traj = []
        for step in range(n_steps):
            T = self.compute_transfer_matrix()
            alpha_total = T.sum(axis=1)  # total stretching on each tube

            # Viscous decay
            decay = self.nu / self.sigma**2

            # Update circulations
            for i in range(self.n):
                dGamma = (alpha_total[i] - decay) * self.circulations[i].item()
                self.circulations[i] += dt * dGamma

            if step % 100 == 0:
                Gamma_max = self.circulations.abs().max().item()
                alpha_max = max(alpha_total)
                traj.append({
                    'step': step, 'time': step*dt,
                    'Gamma_max': Gamma_max,
                    'alpha_max': float(alpha_max),
                    'alpha_total_mean': float(np.mean(alpha_total)),
                })

        return traj


def run_experiments():
    print("=" * 70)
    print("TUBE LATTICE MODEL — Does ⊥ force depletion at every step?")
    print("=" * 70, flush=True)

    results = {}

    # Experiment 1: Random orientations
    print("\n--- Experiment 1: Random orientations (10 tubes) ---", flush=True)
    lat = TubeLattice(10)
    lat.set_random_config(seed=0)
    T = lat.compute_transfer_matrix()

    print(f"Transfer matrix (diagonal should be 0):")
    print(f"  Diagonal: {[f'{T[i,i]:.4f}' for i in range(min(5,lat.n))]}")
    print(f"  Max |diagonal|: {max(abs(T[i,i]) for i in range(lat.n)):.6e}")
    print(f"  Max |off-diagonal|: {max(abs(T[i,j]) for i in range(lat.n) for j in range(lat.n) if i!=j):.4f}")

    alpha_total = T.sum(axis=1)
    print(f"  Total stretching per tube: {[f'{a:.4f}' for a in alpha_total[:5]]}")
    print(f"  Net stretching (all tubes): {alpha_total.sum():.6f}")
    print(f"  Max α: {alpha_total.max():.4f}, Min α: {alpha_total.min():.4f}")

    traj1 = lat.evolve(dt=0.01, n_steps=2000)
    print(f"  After evolution: Γ_max = {traj1[-1]['Gamma_max']:.6f} (started at 10.0)")
    print(f"  Ratio: {traj1[-1]['Gamma_max']/10.0:.6f}")
    results['random'] = {'T': T.tolist(), 'traj': traj1}

    # Experiment 2: Cascade chain (perpendicular tubes)
    print("\n--- Experiment 2: Perpendicular cascade (5 stages) ---", flush=True)
    lat2 = TubeLattice(5)
    lat2.set_cascade_config(n_stages=5)
    T2 = lat2.compute_transfer_matrix()

    print(f"Transfer matrix:")
    for i in range(5):
        print(f"  Row {i}: {[f'{T2[i,j]:+.4f}' for j in range(5)]}")

    alpha2 = T2.sum(axis=1)
    print(f"  Total stretching per tube: {[f'{a:.4f}' for a in alpha2]}")
    print(f"  Net stretching: {alpha2.sum():.6f}")

    traj2 = lat2.evolve(dt=0.01, n_steps=2000)
    print(f"  After evolution: Γ_max = {traj2[-1]['Gamma_max']:.6f}")
    print(f"  Ratio: {traj2[-1]['Gamma_max']/10.0:.6f}")
    results['cascade'] = {'T': T2.tolist(), 'traj': traj2}

    # Experiment 3: Sweep over inter-tube angle to find maximum amplification
    print("\n--- Experiment 3: Angle sweep (2 tubes, find max amplification) ---", flush=True)
    print(f"{'angle':>8} {'α_12':>10} {'α_21':>10} {'net':>10}")
    best_angle = 0
    best_net = -999
    for angle_deg in range(0, 91, 5):
        angle = math.radians(angle_deg)
        lat3 = TubeLattice(2, core_radius=0.3)
        lat3.positions[0] = torch.tensor([0.0, 0.0, 0.0])
        lat3.positions[1] = torch.tensor([1.0, 0.0, 0.0])
        lat3.directions[0] = torch.tensor([0.0, 0.0, 1.0])
        lat3.directions[1] = torch.tensor([math.sin(angle), 0.0, math.cos(angle)])
        lat3.circulations = torch.tensor([10.0, 10.0])
        T3 = lat3.compute_transfer_matrix()
        net = T3[0,1] + T3[1,0]
        if net > best_net:
            best_net = net
            best_angle = angle_deg
        print(f'{angle_deg:8d} {T3[0,1]:+10.4f} {T3[1,0]:+10.4f} {net:+10.4f}')

    print(f"\n  Best angle for mutual stretching: {best_angle}°, net α = {best_net:.4f}")
    print(f"  Viscous decay rate: ν/σ² = {1e-4/0.09:.4f}")
    print(f"  Net - decay = {best_net - 1e-4/0.09:.4f}")
    can_grow = best_net > 1e-4/0.09
    print(f"  Can tubes grow? {'YES — amplification exceeds decay' if can_grow else 'NO — decay wins'}")

    # Experiment 4: Long chain with optimal angle — does cascade amplify?
    print(f"\n--- Experiment 4: Long cascade (10 stages, angle={best_angle}°) ---", flush=True)
    lat4 = TubeLattice(10)
    lat4.set_optimized_cascade(n_stages=10, angle=math.radians(best_angle))
    T4 = lat4.compute_transfer_matrix()
    alpha4 = T4.sum(axis=1)
    print(f"  Stretching per stage: {[f'{a:.4f}' for a in alpha4]}")
    print(f"  Does stretching DECREASE along chain? ", end="")
    decreasing = all(abs(alpha4[i]) >= abs(alpha4[i+1]) - 0.01 for i in range(len(alpha4)-1))
    print(f"{'YES — depletion!' if decreasing else 'NO — amplification!'}")

    traj4 = lat4.evolve(dt=0.01, n_steps=5000)
    print(f"  After long evolution: Γ_max = {traj4[-1]['Gamma_max']:.6f}")
    ratio = traj4[-1]['Gamma_max'] / 10.0
    print(f"  Ratio: {ratio:.6f}")
    print(f"  {'AMPLIFIED' if ratio > 1.01 else 'DEPLETED' if ratio < 0.99 else 'STABLE'}")

    out = 'ns_blowup/results/tube_lattice.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n{'='*70}")
    print(f"VERDICT: Can the adversary design a cascade that amplifies?")
    print(f"{'='*70}")
    print(f"  Random tubes: {'AMPLIFIED' if traj1[-1]['Gamma_max']>10.01 else 'DEPLETED'}")
    print(f"  Perpendicular cascade: {'AMPLIFIED' if traj2[-1]['Gamma_max']>10.01 else 'DEPLETED'}")
    print(f"  Optimal angle chain: {'AMPLIFIED' if ratio>1.01 else 'DEPLETED'}")
    print(f"\nSaved: {out}", flush=True)


if __name__ == '__main__':
    run_experiments()
