#!/usr/bin/env python3
"""
GC volume scaling: the CRITICAL measurement.

Does GC at β=4.0 increase with lattice size? If yes → finite-size effect,
GC > 0 in thermodynamic limit. If no → GC = 0 at weak coupling.

Optimized for larger lattices: vectorized plaquette/staple computation.
"""

import numpy as np
import time

def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)

def qconj(a):
    return a * np.array([1,-1,-1,-1])


class FastLattice:
    """SU(2) lattice with vectorized operations for speed."""
    def __init__(self, L, d=4):
        self.L, self.d = L, d
        a = np.random.randn(*(L,)*d, d, 4)
        self.U = a / np.linalg.norm(a, axis=-1, keepdims=True)

    def _staple_field(self, mu, nu):
        """Vectorized forward staple in (mu,nu) plane. Shape: (L,L,L,L,4)."""
        U_nu_shifted = np.roll(self.U[..., nu, :], -1, axis=mu)
        U_mu_shifted = np.roll(self.U[..., mu, :], -1, axis=nu)
        U_nu = self.U[..., nu, :]
        return qmul(qmul(U_nu_shifted, qconj(U_mu_shifted)), qconj(U_nu))

    def _plaq_trace_field(self, mu, nu):
        """Vectorized (1/2)Tr(U_P) = a0 of plaquette. Shape: (L,L,L,L)."""
        U_mu = self.U[..., mu, :]
        staple = self._staple_field(mu, nu)
        P = qmul(U_mu, staple)
        return P[..., 0]  # (1/2)Tr = a0

    def _full_staple(self, mu):
        """Sum of all staples for direction mu. Shape: (L,L,L,L,4)."""
        S = np.zeros((*([self.L]*4), 4))
        for nu in range(self.d):
            if nu == mu:
                continue
            # Forward staple
            S += self._staple_field(mu, nu)
            # Backward staple
            xbn = [slice(None)]*4
            U_nu_at_xmn = np.roll(np.roll(self.U[..., nu, :], -1, axis=mu), 1, axis=nu)
            U_mu_at_xbn = np.roll(self.U[..., mu, :], 1, axis=nu)
            U_nu_at_xbn = np.roll(self.U[..., nu, :], 1, axis=nu)
            S += qmul(qmul(qconj(U_nu_at_xmn), qconj(U_mu_at_xbn)), U_nu_at_xbn)
        return S

    def heatbath_sweep(self, beta):
        """One sweep with site-by-site heatbath (Python loop — slow but correct)."""
        L = self.L
        for mu in range(self.d):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x = (x0,x1,x2,x3)
                            # Compute staple at this site
                            A = np.zeros(4)
                            for nu in range(4):
                                if nu == mu: continue
                                xm=list(x);xm[mu]=(xm[mu]+1)%L
                                xn=list(x);xn[nu]=(xn[nu]+1)%L
                                xmn=list(x);xmn[mu]=(xmn[mu]+1)%L;xmn[nu]=(xmn[nu]-1)%L
                                xbn=list(x);xbn[nu]=(xbn[nu]-1)%L
                                A+=qmul(qmul(self.U[tuple(xm)+(nu,)],qconj(self.U[tuple(xn)+(mu,)])),qconj(self.U[tuple(x)+(nu,)]))
                                A+=qmul(qmul(qconj(self.U[tuple(xmn)+(nu,)]),qconj(self.U[tuple(xbn)+(mu,)])),self.U[tuple(xbn)+(nu,)])
                            k = np.sqrt(np.sum(A**2))
                            if k < 1e-10: continue
                            ab = beta * k
                            for _ in range(30):
                                r = np.random.uniform()
                                a0 = 1 + np.log(r + (1-r)*np.exp(-2*ab)) / ab
                                if np.random.uniform() < np.sqrt(max(0, 1-a0*a0)):
                                    break
                            rv = np.random.randn(3)
                            n = np.linalg.norm(rv)
                            if n > 0: rv *= np.sqrt(max(0, 1-a0**2)) / n
                            self.U[x+(mu,)] = qmul(np.array([a0,rv[0],rv[1],rv[2]]), qconj(A/k))

    def measure_gc_all_sites(self):
        """
        Measure GC = (1/2)<chair> - (1/4)<plaq·plaq> averaged over ALL sites
        and ALL cross-plane pairs (mu=0, nu=1 vs mu=0, rho=2).

        Returns scalar GC value for this configuration.
        """
        # Staple fields for (0,1) and (0,2) planes
        s01 = self._staple_field(0, 1)  # shape (L,L,L,L,4)
        s02 = self._staple_field(0, 2)  # shape (L,L,L,L,4)

        # Chair trace: (1/2)Tr(s01† · s02) = a0 of qmul(qconj(s01), s02)
        chair = qmul(qconj(s01), s02)[..., 0]  # shape (L,L,L,L)

        # Plaquette traces
        p01 = self._plaq_trace_field(0, 1) * 2  # Tr(U_P), not (1/2)Tr
        p02 = self._plaq_trace_field(0, 2) * 2

        # GC per site = chair - (1/4) p01 * p02
        gc_field = chair - 0.25 * p01 * p02  # shape (L,L,L,L)

        return np.mean(gc_field)


def run_measurement(L, beta, n_therm, n_meas, n_skip):
    """Run full GC measurement on L^4 lattice."""
    lat = FastLattice(L)

    print(f"  L={L}, β={beta}: thermalizing ({n_therm} sweeps)...", end="", flush=True)
    t0 = time.time()
    for i in range(n_therm):
        lat.heatbath_sweep(beta)
        if (i+1) % 10 == 0:
            print(f" {i+1}", end="", flush=True)
    print(f" done ({time.time()-t0:.0f}s)")

    gc_vals = []
    print(f"  Measuring ({n_meas} configs, skip {n_skip})...", end="", flush=True)
    t0 = time.time()
    for i in range(n_meas):
        for _ in range(n_skip):
            lat.heatbath_sweep(beta)
        gc = lat.measure_gc_all_sites()
        gc_vals.append(gc)
        if (i+1) % 5 == 0:
            print(f" {i+1}", end="", flush=True)
    dt = time.time() - t0
    print(f" done ({dt:.0f}s)")

    gc_vals = np.array(gc_vals)
    avg = np.mean(gc_vals)
    # Jackknife error
    n_jack = min(10, n_meas)
    bs = n_meas // n_jack
    jacks = [np.mean(np.delete(gc_vals, slice(j*bs, (j+1)*bs))) for j in range(n_jack)]
    err = np.sqrt((n_jack-1) * np.var(jacks))
    sig = avg / err if err > 0 else float('inf')

    return avg, err, sig, dt


def main():
    print("=" * 70)
    print("GC VOLUME SCALING — THE CRITICAL MEASUREMENT")
    print("=" * 70)
    print("Does GC increase with L at β=4.0?")
    print("If yes: finite-size effect, GC > 0 in thermodynamic limit.")
    print("If no: GC → 0 at weak coupling (still OK but more delicate).")
    print()

    results = []

    # β = 4.0 at multiple volumes
    for L in [4, 6]:
        n_therm = max(40, 20*L)
        n_meas = max(20, 40 // (L//4))
        n_skip = max(2, L // 2)
        avg, err, sig, dt = run_measurement(L, 4.0, n_therm, n_meas, n_skip)
        results.append(('4.0', L, avg, err, sig, dt))
        print(f"  >> GC = {avg:+.6f} ± {err:.6f} ({sig:.1f}σ)\n")

    # β = 2.3 at L=4 and L=6 (tightest point)
    for L in [4, 6]:
        n_therm = max(40, 20*L)
        n_meas = max(20, 40 // (L//4))
        n_skip = max(2, L // 2)
        avg, err, sig, dt = run_measurement(L, 2.3, n_therm, n_meas, n_skip)
        results.append(('2.3', L, avg, err, sig, dt))
        print(f"  >> GC = {avg:+.6f} ± {err:.6f} ({sig:.1f}σ)\n")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY — VOLUME SCALING")
    print("=" * 70)
    print(f"{'β':>5} | {'L':>3} | {'L⁴':>6} | {'GC':>12} | {'error':>10} | {'σ':>6} | {'time':>6}")
    print("-" * 60)
    for beta, L, avg, err, sig, dt in results:
        print(f"{beta:>5} | {L:3d} | {L**4:6d} | {avg:+12.6f} | {err:10.6f} | {sig:6.1f} | {dt:5.0f}s")

    print()
    # Check: does GC increase with L at β=4.0?
    gc_4_results = [(L, avg) for beta, L, avg, err, sig, dt in results if beta == '4.0']
    if len(gc_4_results) >= 2:
        gc4 = gc_4_results[0][1]
        gc6 = gc_4_results[1][1]
        if gc6 > gc4:
            print(f"β=4.0: GC INCREASES with L ({gc4:.4f} → {gc6:.4f}). Finite-size effect! ✓")
        elif gc6 < gc4 * 0.5:
            print(f"β=4.0: GC DECREASES with L ({gc4:.4f} → {gc6:.4f}). GC may → 0. ⚠️")
        else:
            print(f"β=4.0: GC stable ({gc4:.4f} → {gc6:.4f}). Need larger L to resolve.")


if __name__ == "__main__":
    main()
