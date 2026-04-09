#!/usr/bin/env python3
"""
Monte Carlo measurement of vortex free energy F_v = -ln(Z⁻/Z) for SU(2) d=4.

F_v > 0 ↔ confinement ↔ mass gap.

Method: Z⁻/Z = ⟨(-1)^{vortex_flux}⟩_Z where vortex_flux counts half-integer
representations threading the surface Σ.

For SU(2): the center element is detected by the sign of (1/2)Tr(U_P).
A center vortex through Σ flips the sign of Tr(U) for links crossing Σ.

Operationally: Z⁻/Z = ⟨∏_{P∈Σ} sign(Tr(U_P))⟩ ... no, that's not right.

Actually: Z⁻/Z = ⟨exp(-ΔS)⟩_periodic where ΔS is the change in action
from inserting the center twist. For SU(2) with Wilson action:
  ΔS = β Σ_{P∈Σ} [(1 - (1/2)Tr(-U_P)) - (1 - (1/2)Tr(U_P))]
     = β Σ_{P∈Σ} (1/2)[Tr(U_P) - Tr(-U_P)]
     = β Σ_{P∈Σ} Tr(U_P)  [since Tr(-U) = -Tr(U) for SU(2)]

So: Z⁻/Z = ⟨exp(-β Σ_{P∈Σ} Tr(U_P))⟩_periodic

And: F_v = -ln⟨exp(-β Σ_{P∈Σ} Tr(U_P))⟩

This is a standard Monte Carlo observable (though exponentially noisy for
large Area(Σ) — the "overlap problem").

For small lattices: direct computation is feasible.
"""

import numpy as np
import time

# SU(2) quaternion ops (reused)
def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0],axis=-1)

def qconj(a): return a*np.array([1,-1,-1,-1])

class Lattice4D:
    def __init__(self, L):
        self.L = L
        a = np.random.randn(L,L,L,L,4,4)
        self.links = a / np.linalg.norm(a, axis=-1, keepdims=True)

    def plaquette_trace(self, mu, nu):
        """(1/2)Tr(U_P) for all plaquettes in (mu,nu) plane."""
        U_mu = self.links[..., mu, :]
        U_nu = self.links[..., nu, :]
        U_mu_s = np.roll(U_mu, -1, axis=nu)
        U_nu_s = np.roll(U_nu, -1, axis=mu)
        P = qmul(qmul(U_mu, U_nu_s), qmul(qconj(U_mu_s), qconj(U_nu)))
        return P[..., 0]  # (1/2)Tr = a_0

    def avg_plaquette(self):
        total = 0.0
        count = 0
        for mu in range(4):
            for nu in range(mu+1, 4):
                total += np.mean(self.plaquette_trace(mu, nu))
                count += 1
        return total / count

    def staple(self, x, mu):
        L = self.L
        S = np.zeros(4)
        for nu in range(4):
            if nu == mu: continue
            xm = list(x); xm[mu]=(xm[mu]+1)%L
            xn = list(x); xn[nu]=(xn[nu]+1)%L
            xmn=list(x); xmn[mu]=(xmn[mu]+1)%L; xmn[nu]=(xmn[nu]-1)%L
            xbn=list(x); xbn[nu]=(xbn[nu]-1)%L
            S += qmul(qmul(self.links[tuple(xm)+(nu,)],qconj(self.links[tuple(xn)+(mu,)])),qconj(self.links[tuple(x)+(nu,)]))
            S += qmul(qmul(qconj(self.links[tuple(xmn)+(nu,)]),qconj(self.links[tuple(xbn)+(mu,)])),self.links[tuple(xbn)+(nu,)])
        return S

    def heatbath(self, beta):
        L = self.L
        for mu in range(4):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x=(x0,x1,x2,x3)
                            A = self.staple(x, mu)
                            k = np.sqrt(np.sum(A**2))
                            if k < 1e-10: continue
                            ab = beta*k
                            for _ in range(50):
                                r=np.random.uniform()
                                a0=1+np.log(r+(1-r)*np.exp(-2*ab))/ab
                                if np.random.uniform()<np.sqrt(max(0,1-a0*a0)):
                                    break
                            rv=np.random.randn(3)
                            norm=np.linalg.norm(rv)
                            if norm>0:
                                rv*=np.sqrt(max(0,1-a0**2))/norm
                            self.links[x+(mu,)]=qmul(np.array([a0,rv[0],rv[1],rv[2]]),qconj(A/k))

    def vortex_observable(self, beta):
        """
        Compute exp(-β Σ_{P∈Σ} Tr(U_P)) where Σ is the (0,1) plane at x2=x3=0.

        F_v = -ln⟨this⟩. If F_v > 0: confinement.
        """
        # Σ = plaquettes in (0,1) plane at x2=0, x3=0 for all x0, x1
        # Actually: Σ should be a CLOSED surface. On a 4D torus, take
        # the surface at x2=0, all x0,x1,x3. Area = L³.
        # But that's too large — the overlap problem will kill us.
        #
        # Instead: take a SMALLER surface. The vortex flux through a
        # surface of area A gives Z⁻/Z ~ exp(-σA). For σ ~ 1 and A ~ L²,
        # this is already exponentially small.
        #
        # Use the 't Hooft loop: Σ = (0,1) plaquettes at x2=0, x3=0.
        # Area = L × L = L². For L=4: A=16.
        # Z⁻/Z ~ exp(-σ·16) ~ exp(-16) ~ 10⁻⁷. Very small signal.
        #
        # For a meaningful measurement, use small Σ: just ONE plaquette.
        # Then ΔS = β · Tr(U_P) for that plaquette.
        # F_v(1 plaq) = -ln⟨exp(-β Tr(U_P))⟩

        # Single plaquette vortex cost
        P_01 = self.plaquette_trace(0, 1)  # all (0,1) plaquettes
        # Pick plaquette at x=(0,0,0,0)
        tr_P = P_01[0, 0, 0, 0] * 2  # Tr(U_P) = 2 * (1/2)Tr

        # For area = 1: exp(-β · Tr(U_P))
        return np.exp(-beta * tr_P)

    def vortex_observable_line(self, beta):
        """
        Vortex cost for a line of plaquettes: Σ = (0,1) plaq at x2=0, x3=0, all x0.
        Area = L (a 1D slice).
        """
        P_01 = self.plaquette_trace(0, 1)  # shape (L,L,L,L)
        tr_sum = 2 * np.sum(P_01[:, 0, 0, 0])  # Σ Tr(U_P) for x1=0,x2=0,x3=0, all x0
        return np.exp(-beta * tr_sum)


def main():
    print("=" * 70)
    print("VORTEX FREE ENERGY — Monte Carlo on 4⁴ SU(2)")
    print("=" * 70)
    print("F_v = -ln⟨exp(-β Σ_{P∈Σ} Tr(U_P))⟩")
    print("F_v > 0 ↔ confinement ↔ mass gap")
    print()

    L = 4
    n_therm = 80
    n_meas = 100
    n_skip = 3

    betas = [1.5, 2.0, 2.3, 3.0, 4.0]

    for beta in betas:
        print(f"\nβ = {beta}, L = {L}")
        lat = Lattice4D(L)

        print(f"  Thermalizing ({n_therm})...", end="", flush=True)
        for _ in range(n_therm):
            lat.heatbath(beta)
        print(" done.")

        # Measure
        obs_1plaq = []
        obs_line = []
        plaq_avg = []

        print(f"  Measuring ({n_meas})...", end="", flush=True)
        for i in range(n_meas):
            for _ in range(n_skip):
                lat.heatbath(beta)
            obs_1plaq.append(lat.vortex_observable(beta))
            obs_line.append(lat.vortex_observable_line(beta))
            plaq_avg.append(lat.avg_plaquette())
            if (i+1) % 20 == 0:
                print(f" {i+1}", end="", flush=True)
        print(" done.")

        avg_P = np.mean(plaq_avg)
        # 1-plaquette vortex
        v1 = np.mean(obs_1plaq)
        Fv1 = -np.log(v1) if v1 > 0 else float('inf')
        # Line vortex (L plaquettes)
        vL = np.mean(obs_line)
        FvL = -np.log(vL) if vL > 0 else float('inf')

        sigma_1 = Fv1  # F_v per plaquette
        sigma_L = FvL / L if FvL < float('inf') else float('inf')

        print(f"  ⟨P⟩ = {avg_P:.4f}")
        print(f"  1-plaq: ⟨exp(-βTr)⟩ = {v1:.6f}, F_v = {Fv1:.4f}")
        print(f"  L-line: ⟨exp(-βΣTr)⟩ = {vL:.2e}, F_v = {FvL:.4f}, σ = F_v/L = {sigma_L:.4f}")
        print(f"  F_v > 0? {'YES ✓' if Fv1 > 0 and FvL > 0 else 'NO ✗'}")

    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print("""
F_v(1 plaq) measures the cost of inserting a minimal vortex.
F_v(L line) measures the cost of a vortex line of length L.

If σ = F_v/Area > 0 for all β → area law → confinement → mass gap.

The σ values should match the independent-plaquette prediction
σ_indep = ln(S_per/S_anti) from attempt_011 (within MC errors).
""")


if __name__ == "__main__":
    main()
