#!/usr/bin/env python3
"""
FKG Test for SU(2) Lattice Gauge Theory — request_020

Measures plaquette-plaquette covariances at high statistics on L=4, 6
to test whether the SU(2) Wilson measure satisfies FKG:

    Cov(Tr(U_P), Tr(U_Q)) ≥ 0 for all plaquette pairs P, Q.

Also tests the CRITICAL vortex covariance:

    Cov(Σ_P Tr(U_P), e^{-δS})

which FKG predicts is ≤ 0.

Uses vectorized FastLattice from gc_volume_scaling.py for speed.
"""
import numpy as np
import time
import sys, os

# Reuse vectorized lattice from gc_volume_scaling
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)

def qconj(a):
    return a * np.array([1,-1,-1,-1])


class FastLattice:
    def __init__(self, L, d=4):
        self.L, self.d = L, d
        a = np.random.randn(*(L,)*d, d, 4)
        self.U = a / np.linalg.norm(a, axis=-1, keepdims=True)

    def _staple_field(self, mu, nu):
        U_nu_shifted = np.roll(self.U[..., nu, :], -1, axis=mu)
        U_mu_shifted = np.roll(self.U[..., mu, :], -1, axis=nu)
        U_nu = self.U[..., nu, :]
        return qmul(qmul(U_nu_shifted, qconj(U_mu_shifted)), qconj(U_nu))

    def _plaq_trace_field(self, mu, nu):
        """(1/2) Tr(U_P) = a0. Shape (L,L,L,L)."""
        U_mu = self.U[..., mu, :]
        staple = self._staple_field(mu, nu)
        P = qmul(U_mu, staple)
        return P[..., 0]

    def plaq_trace_full(self, mu, nu):
        """Tr(U_P) (not divided by 2). Shape (L,L,L,L)."""
        return 2 * self._plaq_trace_field(mu, nu)

    def heatbath_sweep(self, beta):
        L = self.L
        for mu in range(self.d):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x = (x0,x1,x2,x3)
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


def measure_fkg(L, beta, n_therm, n_meas, n_skip):
    """Measure plaquette correlators for FKG test."""
    lat = FastLattice(L)

    print(f"  L={L}, β={beta}: thermalizing ({n_therm})...", end="", flush=True)
    t0 = time.time()
    for _ in range(n_therm):
        lat.heatbath_sweep(beta)
    print(f" done ({time.time()-t0:.0f}s)")

    plaq_traces = []  # list of (6, L^4) arrays — one per direction pair
    sum_trs = []      # Σ_P Tr(U_P) per config
    t0 = time.time()
    print(f"  Measuring ({n_meas} configs, skip {n_skip})...", end="", flush=True)
    for i in range(n_meas):
        for _ in range(n_skip):
            lat.heatbath_sweep(beta)
        # All 6 plaquette planes
        plaq_all_planes = []
        for mu in range(4):
            for nu in range(mu+1, 4):
                plaq_all_planes.append(lat.plaq_trace_full(mu, nu).flatten())
        plaq_traces.append(np.array(plaq_all_planes))  # (6, L^4)
        sum_trs.append(np.sum(plaq_all_planes))
        if (i+1) % 20 == 0:
            print(f" {i+1}", end="", flush=True)
    print(f" done ({time.time()-t0:.0f}s)")

    plaq_traces = np.array(plaq_traces)  # (n_meas, 6, L^4)
    sum_trs = np.array(sum_trs)  # (n_meas,)

    # Test 1: plaquette-plaquette covariance at same plane, adjacent sites
    # Average plaq_trace across planes and sites
    p_bar = plaq_traces.mean()

    # Cov(P_0, P_i) for i = 0..L-1 at same plane
    # Use plane 0 (mu=0, nu=1)
    p0 = plaq_traces[:, 0, :]  # (n_meas, L^4)

    # Reshape to (n_meas, L, L, L, L)
    p0 = p0.reshape(-1, L, L, L, L)

    # Compute Cov(p(0,0,0,0), p(dx,0,0,0)) for dx = 0..L-1
    cov_by_dist = []
    for dx in range(L):
        p_shifted = np.roll(p0, -dx, axis=1)
        c = np.mean(p0 * p_shifted) - p_bar**2
        cov_by_dist.append(c)

    # Cross-plane covariance
    p1 = plaq_traces[:, 1, :].reshape(-1, L, L, L, L)  # plane (0,2)
    cross_cov = np.mean(p0 * p1) - p_bar**2

    # Plaquette average
    sum_bar = sum_trs.mean()
    sum_var = sum_trs.var()

    # Vortex observable: e^{-δS} for a minimal vortex surface
    # Use the (0,1) plaquettes on slice x3=0 as a surrogate vortex surface Σ
    vortex_obs_vals = []
    for i in range(len(plaq_traces)):
        p01 = plaq_traces[i, 0, :].reshape(L, L, L, L)
        # Sum of plaquettes on x3=0 slice (L³ plaquettes)
        delta_S = 2 * np.sum(p01[:,:,:,0])
        vortex_obs_vals.append(np.exp(-delta_S))
    vortex_obs_vals = np.array(vortex_obs_vals)

    # Cov(O = Σ_P Tr, e^{-δS})
    O_vals = sum_trs
    cov_O_vortex = np.mean(O_vals * vortex_obs_vals) - np.mean(O_vals) * np.mean(vortex_obs_vals)

    # Jackknife error for cov_O_vortex
    n_jack = 10
    bs = len(O_vals) // n_jack
    jacks = []
    for j in range(n_jack):
        mask = np.ones(len(O_vals), dtype=bool)
        mask[j*bs:(j+1)*bs] = False
        O_j = O_vals[mask]
        V_j = vortex_obs_vals[mask]
        c_j = np.mean(O_j * V_j) - np.mean(O_j) * np.mean(V_j)
        jacks.append(c_j)
    cov_err = np.sqrt((n_jack - 1) * np.var(jacks))

    return {
        'p_bar': p_bar,
        'cov_by_dist': cov_by_dist,
        'cross_cov': cross_cov,
        'sum_var': sum_var,
        'cov_O_vortex': cov_O_vortex,
        'cov_err': cov_err,
        'O_mean': np.mean(O_vals),
        'vortex_mean': np.mean(vortex_obs_vals),
    }


def main():
    print("=" * 70)
    print("FKG TEST FOR SU(2) LATTICE — request_020")
    print("=" * 70)
    print("Tests:")
    print("  1. Plaquette-plaquette Cov ≥ 0 at all distances")
    print("  2. Cov(Σ Tr(U_P), e^{-δS}) ≤ 0 (vortex covariance)")
    print()

    results = []
    for L, beta, nt, nm, ns in [
        (4, 2.3, 80, 200, 2),
        (4, 4.0, 80, 200, 2),
        (6, 2.3, 120, 100, 3),
        (6, 4.0, 120, 100, 3),
    ]:
        print(f"--- L={L}, β={beta} ---")
        t0 = time.time()
        r = measure_fkg(L, beta, nt, nm, ns)
        dt = time.time() - t0
        print(f"  ⟨Tr(P)⟩ = {r['p_bar']:+.5f}")
        print(f"  Cov(P_0, P_i) by distance i:")
        for dx, c in enumerate(r['cov_by_dist']):
            sign = "+" if c >= 0 else "-"
            print(f"    dx={dx}: {sign}{abs(c):.5e}")
        print(f"  Cross-plane Cov(P_01, P_02) = {r['cross_cov']:+.5e}")
        print(f"  Cov(O, e^{{-δS}}) = {r['cov_O_vortex']:+.5e} ± {r['cov_err']:.5e}")
        sig = r['cov_O_vortex'] / r['cov_err'] if r['cov_err'] > 0 else float('inf')
        print(f"    significance: {sig:+.1f}σ")
        fkg_ok = "YES" if r['cov_O_vortex'] <= 0 else "NO"
        print(f"    FKG prediction Cov ≤ 0: {fkg_ok}")
        print(f"  Total time: {dt:.0f}s")
        results.append((L, beta, r))
        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'L':>3} {'β':>5} | {'⟨P⟩':>8} | {'Cov_OV':>14} | {'σ':>6} | {'FKG':>5}")
    print("-" * 60)
    fkg_holds = True
    for L, beta, r in results:
        sig = r['cov_O_vortex'] / r['cov_err'] if r['cov_err'] > 0 else float('inf')
        ok = "✓" if r['cov_O_vortex'] <= 0 else "✗"
        if r['cov_O_vortex'] > 2 * r['cov_err']:
            fkg_holds = False  # statistically significant positive
        print(f"{L:3d} {beta:5.1f} | {r['p_bar']:+8.4f} | {r['cov_O_vortex']:+14.5e} | {sig:+6.1f} | {ok:>5}")

    print()
    if fkg_holds:
        print("*** FKG prediction (Cov(O, e^{-δS}) ≤ 0) NOT VIOLATED at any tested (L,β) ***")
        print("*** Consistent with Tomboulis (5.15) → proof route alive ***")
    else:
        print("*** FKG VIOLATED at some (L,β) — need different proof route ***")


if __name__ == "__main__":
    main()
