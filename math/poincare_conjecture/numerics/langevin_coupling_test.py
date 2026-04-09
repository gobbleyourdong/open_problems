#!/usr/bin/env python3
"""
Coupled MC test: periodic vs anti-periodic with SAME random numbers.

Track Δ(t) = ⟨O⟩_per(t) - ⟨O⟩_anti(t) over MC time.
If Δ(t) ≥ 0 at all times → evidence for Option D (Langevin coupling).

Method: Run two lattices in lockstep with identical random seeds.
Lattice 1: periodic BC (standard Wilson action)
Lattice 2: anti-periodic BC (center twist on surface Σ)
Same heatbath proposals → noise cancels → Δ evolution is smooth.
"""

import numpy as np

def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0],axis=-1)
def qconj(a): return a*np.array([1,-1,-1,-1])


class CoupledLattice:
    """Two SU(2) lattices with shared random numbers."""
    def __init__(self, L):
        self.L = L
        # Start BOTH from the same hot config
        a = np.random.randn(L,L,L,L,4,4)
        links_init = a / np.linalg.norm(a, axis=-1, keepdims=True)
        self.links_per = links_init.copy()
        self.links_anti = links_init.copy()

    def staple(self, links, x, mu, twist=False):
        """Compute staple sum. If twist=True, flip links crossing Σ."""
        L = self.L
        S = np.zeros(4)
        for nu in range(4):
            if nu == mu: continue
            xm=list(x);xm[mu]=(xm[mu]+1)%L
            xn=list(x);xn[nu]=(xn[nu]+1)%L
            xmn=list(x);xmn[mu]=(xmn[mu]+1)%L;xmn[nu]=(xmn[nu]-1)%L
            xbn=list(x);xbn[nu]=(xbn[nu]-1)%L

            # Get link values, applying twist if needed
            def get_link(ll, pos, d):
                v = ll[tuple(pos)+(d,)]
                if twist and self._is_twisted(pos, d):
                    return -v  # center twist: U → -U
                return v

            fwd = qmul(qmul(get_link(links,xm,nu), qconj(get_link(links,xn,mu))),
                        qconj(get_link(links,x,nu)))
            bwd = qmul(qmul(qconj(get_link(links,xmn,nu)), qconj(get_link(links,xbn,mu))),
                        get_link(links,xbn,nu))
            S += fwd + bwd
        return S

    def _is_twisted(self, pos, mu):
        """Is link (pos, mu) on the twisted surface?
        Twist: links in direction 0 at x1=0, x2=0, x3=0."""
        return mu == 0 and pos[1] == 0 and pos[2] == 0 and pos[3] == 0

    def coupled_heatbath_sweep(self, beta):
        """One coupled sweep: same random numbers, different staples."""
        L = self.L
        for mu in range(4):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x = (x0,x1,x2,x3)
                            # SAME random numbers for both
                            seed_state = np.random.get_state()

                            # Periodic lattice
                            A_per = self.staple(self.links_per, x, mu, twist=False)
                            k_per = np.sqrt(np.sum(A_per**2))
                            if k_per > 1e-10:
                                np.random.set_state(seed_state)  # reset RNG
                                ab = beta * k_per
                                for _ in range(50):
                                    r=np.random.uniform()
                                    a0=1+np.log(r+(1-r)*np.exp(-2*ab))/ab
                                    if np.random.uniform()<np.sqrt(max(0,1-a0*a0)):
                                        break
                                rv=np.random.randn(3)
                                norm=np.linalg.norm(rv)
                                if norm>0: rv*=np.sqrt(max(0,1-a0**2))/norm
                                U_per=qmul(np.array([a0,rv[0],rv[1],rv[2]]),qconj(A_per/k_per))
                                self.links_per[x+(mu,)] = U_per

                            # Anti-periodic lattice (same seed!)
                            # The twist changes the staple for links near Σ
                            np.random.set_state(seed_state)  # SAME random numbers

                            A_anti = self.staple(self.links_anti, x, mu, twist=True)
                            k_anti = np.sqrt(np.sum(A_anti**2))
                            if k_anti > 1e-10:
                                ab = beta * k_anti
                                for _ in range(50):
                                    r=np.random.uniform()
                                    a0=1+np.log(r+(1-r)*np.exp(-2*ab))/ab
                                    if np.random.uniform()<np.sqrt(max(0,1-a0*a0)):
                                        break
                                rv=np.random.randn(3)
                                norm=np.linalg.norm(rv)
                                if norm>0: rv*=np.sqrt(max(0,1-a0**2))/norm
                                U_anti=qmul(np.array([a0,rv[0],rv[1],rv[2]]),qconj(A_anti/k_anti))
                                self.links_anti[x+(mu,)] = U_anti

    def avg_plaquette(self, links):
        """Average (1/2)Tr(U_P) over all plaquettes."""
        L = self.L
        total = 0.0
        count = 0
        for mu in range(4):
            for nu in range(mu+1, 4):
                U_mu = links[...,mu,:]
                U_nu = links[...,nu,:]
                P = qmul(qmul(U_mu, np.roll(links[...,nu,:], -1, axis=mu)),
                         qmul(qconj(np.roll(links[...,mu,:], -1, axis=nu)), qconj(U_nu)))
                total += np.mean(P[...,0])
                count += 1
        return total / count


def main():
    print("=" * 70)
    print("COUPLED MC: Δ(t) = ⟨P⟩_per(t) - ⟨P⟩_anti(t) vs MC time")
    print("=" * 70)
    print("Same random numbers for both processes.")
    print("If Δ(t) ≥ 0 at all t → supports Langevin coupling route.")
    print()

    L = 4
    n_sweeps = 60

    for beta in [2.0, 2.3, 3.0]:
        print(f"\nβ = {beta}, L = {L}, {n_sweeps} coupled sweeps")
        lat = CoupledLattice(L)

        print(f"{'sweep':>6} | {'⟨P⟩_per':>10} | {'⟨P⟩_anti':>10} | {'Δ':>12} | {'Δ≥0?':>6}")
        print("-" * 55)

        n_negative = 0
        for sweep in range(n_sweeps):
            lat.coupled_heatbath_sweep(beta)

            if sweep % 5 == 0 or sweep == n_sweeps - 1:
                p_per = lat.avg_plaquette(lat.links_per)
                p_anti = lat.avg_plaquette(lat.links_anti)
                delta = p_per - p_anti
                sign = "✓" if delta >= 0 else "✗"
                if delta < 0: n_negative += 1
                print(f"{sweep:6d} | {p_per:10.6f} | {p_anti:10.6f} | {delta:12.6f} | {sign:>6}")

        print(f"\nNegative Δ count: {n_negative}/{n_sweeps//5 + 1}")

    print("\n" + "=" * 70)
    print("NOTE: The twist implementation here is simplified (single line of")
    print("links). A proper implementation needs the full center twist on a")
    print("non-contractible surface. The qualitative test is whether Δ stays")
    print("positive under coupled dynamics.")


if __name__ == "__main__":
    main()
