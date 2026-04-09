#!/usr/bin/env python3
"""
Connected plaquette correlator C(r) vs distance for SU(2) d=4.

C(r) = ⟨Tr(U_P(0)) Tr(U_P(r))⟩ - ⟨Tr(U_P)⟩²

Measures:
1. Sign of C(r) at each distance (positive correlation test)
2. Exponential decay rate = mass gap Δ
3. Statistical significance via jackknife errors

This is the definitive test for the plaquette positive correlation question.
"""

import numpy as np
import time

# Reuse quaternion SU(2) from plaquette_correlation.py
def quat_mul(a, b):
    a0, a1, a2, a3 = a[...,0], a[...,1], a[...,2], a[...,3]
    b0, b1, b2, b3 = b[...,0], b[...,1], b[...,2], b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)

def quat_conj(a): return a * np.array([1,-1,-1,-1])

class LatticeSU2:
    def __init__(self, L, d=4):
        self.L, self.d = L, d
        a = np.random.randn(*(L,)*d, d, 4)
        self.links = a / np.linalg.norm(a, axis=-1, keepdims=True)

    def plaquette_trace_01(self):
        """(1/2)Tr(U_P) for all plaquettes in (0,1) plane. Shape: (L,L,L,L)."""
        U0 = self.links[..., 0, :]
        U1 = self.links[..., 1, :]
        U0s = np.roll(U0, -1, axis=1)  # U_0(x + e_1)
        U1s = np.roll(U1, -1, axis=0)  # U_1(x + e_0)
        P = quat_mul(quat_mul(U0, U1s), quat_mul(quat_conj(U0s), quat_conj(U1)))
        return P[..., 0]  # a_0 component = (1/2)Tr

    def staple_sum(self, x, mu):
        L, d = self.L, self.d
        S = np.zeros(4)
        for nu in range(d):
            if nu == mu: continue
            xm = list(x); xm[mu] = (xm[mu]+1)%L
            xn = list(x); xn[nu] = (xn[nu]+1)%L
            xmn = list(x); xmn[mu]=(xmn[mu]+1)%L; xmn[nu]=(xmn[nu]-1)%L
            xbn = list(x); xbn[nu] = (xbn[nu]-1)%L
            S += quat_mul(quat_mul(self.links[tuple(xm)+(nu,)],
                          quat_conj(self.links[tuple(xn)+(mu,)])),
                          quat_conj(self.links[tuple(x)+(nu,)]))
            S += quat_mul(quat_mul(quat_conj(self.links[tuple(xmn)+(nu,)]),
                          quat_conj(self.links[tuple(xbn)+(mu,)])),
                          self.links[tuple(xbn)+(nu,)])
        return S

    def heatbath_sweep(self, beta):
        L, d = self.L, self.d
        for mu in range(d):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x = (x0,x1,x2,x3)
                            A = self.staple_sum(x, mu)
                            k = np.sqrt(np.sum(A**2))
                            if k < 1e-10: continue
                            ab = beta * k
                            while True:
                                r = np.random.uniform()
                                a0 = 1 + np.log(r + (1-r)*np.exp(-2*ab)) / ab
                                if np.random.uniform() < np.sqrt(max(0, 1-a0*a0)):
                                    break
                            rv = np.random.randn(3)
                            rv *= np.sqrt(max(0, 1-a0**2)) / (np.linalg.norm(rv)+1e-30)
                            U = np.array([a0, rv[0], rv[1], rv[2]])
                            self.links[x+(mu,)] = quat_mul(U, quat_conj(A/k))


def correlator_vs_distance(L, beta, n_configs, n_therm=100, n_skip=5):
    """
    Compute C(r) = ⟨P(0)P(r)⟩_c for r = 0, 1, ..., L/2.

    Uses zero-momentum projection: sum over spatial positions at fixed
    temporal separation in the (0,1) plaquette plane.
    """
    lat = LatticeSU2(L)
    max_r = L // 2

    print(f"  Thermalizing ({n_therm} sweeps)...", end="", flush=True)
    for _ in range(n_therm):
        lat.heatbath_sweep(beta)
    print(" done.")

    # Storage for per-timeslice plaquette averages
    # P_slice[t] = (1/L³) Σ_{x1,x2,x3} (1/2)Tr(U_P(t, x1, x2, x3))
    slice_data = []  # list of arrays, each shape (L,)

    print(f"  Measuring ({n_configs} configs)...", end="", flush=True)
    for i in range(n_configs):
        for _ in range(n_skip):
            lat.heatbath_sweep(beta)

        P = lat.plaquette_trace_01()  # shape (L,L,L,L)
        # Average over spatial directions (axes 1,2,3), keep time (axis 0)
        P_t = P.mean(axis=(1, 2, 3))  # shape (L,)
        slice_data.append(P_t.copy())

        if (i+1) % 20 == 0:
            print(f" {i+1}", end="", flush=True)
    print(" done.")

    slice_data = np.array(slice_data)  # (n_configs, L)
    avg_P = np.mean(slice_data)

    # Connected correlator: C(r) = ⟨P(t) P(t+r)⟩ - ⟨P⟩²
    # Average over all t (translational invariance)
    C = np.zeros(max_r + 1)
    C_err = np.zeros(max_r + 1)

    for r in range(max_r + 1):
        # For each config: compute P(t)*P(t+r) averaged over t
        corr_per_config = np.zeros(n_configs)
        for ic in range(n_configs):
            P_t = slice_data[ic]
            corr = 0.0
            for t in range(L):
                corr += P_t[t] * P_t[(t + r) % L]
            corr_per_config[ic] = corr / L

        C[r] = np.mean(corr_per_config) - avg_P**2
        # Jackknife error
        n_jack = min(20, n_configs)
        jack_size = n_configs // n_jack
        jack_vals = []
        for j in range(n_jack):
            mask = np.ones(n_configs, bool)
            mask[j*jack_size:(j+1)*jack_size] = False
            jack_avg = np.mean(corr_per_config[mask]) - np.mean(slice_data[mask])**2
            jack_vals.append(jack_avg)
        C_err[r] = np.sqrt((n_jack - 1) * np.var(jack_vals))

    return C, C_err, avg_P


def main():
    print("=" * 70)
    print("CONNECTED CORRELATOR C(r) vs DISTANCE — SU(2) d=4")
    print("=" * 70)
    print("C(r) = ⟨P(0)P(r)⟩ - ⟨P⟩²")
    print("Sign of C(r) tests plaquette positive correlation.")
    print("Decay rate = mass gap Δ.")
    print()

    L = 4
    n_configs = 200
    betas = [1.5, 2.0, 2.3, 3.0, 4.0]

    all_results = {}

    for beta in betas:
        print(f"\n{'='*40}")
        print(f"β = {beta}, L = {L}, {n_configs} configs")
        print(f"{'='*40}")
        t0 = time.time()
        C, C_err, avg_P = correlator_vs_distance(L, beta, n_configs, n_therm=80, n_skip=3)
        dt = time.time() - t0
        all_results[beta] = (C, C_err, avg_P)

        print(f"\n  ⟨P⟩ = {avg_P:.6f}  (time: {dt:.0f}s)")
        print(f"  {'r':>3} | {'C(r)':>12} | {'err':>10} | {'C/err':>8} | {'sign':>6}")
        print(f"  {'-'*50}")
        for r in range(len(C)):
            sig = C[r] / C_err[r] if C_err[r] > 0 else 0
            sign = "+" if C[r] > 0 else "-"
            marker = " ✓" if C[r] > 0 else " ✗" if abs(sig) > 2 else " ?"
            print(f"  {r:3d} | {C[r]:12.2e} | {C_err[r]:10.2e} | {sig:8.1f} | {sign:>4}{marker}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY: IS C(r) ≥ 0 FOR ALL β AND r?")
    print("=" * 70)

    any_significant_negative = False
    for beta in betas:
        C, C_err, avg_P = all_results[beta]
        neg_count = 0
        sig_neg = 0
        for r in range(1, len(C)):
            if C[r] < 0:
                neg_count += 1
                if C_err[r] > 0 and C[r] / C_err[r] < -2:
                    sig_neg += 1
                    any_significant_negative = True
        status = "ALL ≥ 0 ✓" if neg_count == 0 else f"{neg_count} neg ({sig_neg} sig)"
        print(f"  β = {beta}: {status}")

    print()
    if not any_significant_negative:
        print("NO statistically significant negative correlations found.")
        print("Consistent with plaquette positive correlation → Tomboulis (5.15) holds.")
    else:
        print("SIGNIFICANT negative correlations found — positive correlation may FAIL.")

    # Mass gap extraction
    print("\n" + "=" * 70)
    print("MASS GAP EXTRACTION: Δ = -ln(C(1)/C(0))")
    print("=" * 70)
    for beta in betas:
        C, C_err, avg_P = all_results[beta]
        if C[0] > 0 and C[1] > 0:
            m_eff = -np.log(C[1] / C[0])
            print(f"  β = {beta}: Δ_eff = {m_eff:.3f}")
        else:
            print(f"  β = {beta}: cannot extract (C[0]={C[0]:.2e}, C[1]={C[1]:.2e})")


if __name__ == "__main__":
    main()
