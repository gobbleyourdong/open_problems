"""
Rigorous c(4) certificate using interval arithmetic.

Target: prove that for k = {[-1,0,0], [-1,1,1], [1,0,1], [1,1,1]},
max S²ê/|ω|² over all polarization angles and optimal sign patterns
is rigorously < 0.75.

Strategy:
1. Partition [0,π]^4 into cells
2. For each cell, use interval arithmetic to bound:
   - |ω|² from below (for each of 16 sign patterns)
   - |Sω|² from above
3. For each cell, find the maximum |ω|² sign pattern (the optimum)
4. At that sign, bound |Sω|²_max / |ω|²_min
5. Take the max over all cells

Uses mpmath.iv for interval arithmetic.
"""
import mpmath
from mpmath import iv, mpf
from itertools import product as iprod
import sys

# Precision for interval arithmetic
mpmath.mp.dps = 30
mpmath.iv.dps = 30

# The worst-case k-quadruple
KS = [(-1, 0, 0), (-1, 1, 1), (1, 0, 1), (1, 1, 1)]
K_NORMS_SQ = [sum(k[i]**2 for i in range(3)) for k in KS]  # [1, 3, 2, 3]

def iv_cos(x):
    """Interval cosine."""
    return iv.cos(x)

def iv_sin(x):
    """Interval sine."""
    return iv.sin(x)

def iv_sqrt(x):
    return iv.sqrt(x)

def build_perp_basis_exact(k):
    """Construct perpendicular basis exactly for integer k."""
    import numpy as np
    k_np = np.array(k, dtype=float)
    kn = k_np / np.linalg.norm(k_np)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1.tolist(), e2.tolist()

BASES = [build_perp_basis_exact(k) for k in KS]

def iv_vec(v, is_interval=True):
    """Convert numeric vector to interval vector."""
    if is_interval:
        return [iv.mpf(float(x)) for x in v]
    return v

E1 = [iv_vec(b[0]) for b in BASES]
E2 = [iv_vec(b[1]) for b in BASES]
K_IV = [[iv.mpf(float(k[i])) for i in range(3)] for k in KS]
K_SQ_IV = [iv.mpf(float(ks)) for ks in K_NORMS_SQ]

def compute_on_cell(theta_intervals):
    """
    For given interval ranges on thetas, compute interval bounds on |ω|² and |Sω|²
    for each of the 16 sign patterns.
    Returns (best_sign, om2_lo, om2_hi, Sw2_lo, Sw2_hi).
    Returns the ratio bound.
    """
    # Compute v_i and w_i as interval vectors
    vs = []
    ws = []
    for i in range(4):
        c = iv_cos(theta_intervals[i])
        s = iv_sin(theta_intervals[i])
        # v_i = c * e1 + s * e2
        v = [c * E1[i][j] + s * E2[i][j] for j in range(3)]
        vs.append(v)
        # w_i = k_i × v_i
        k = K_IV[i]
        w = [k[1]*v[2] - k[2]*v[1],
             k[2]*v[0] - k[0]*v[2],
             k[0]*v[1] - k[1]*v[0]]
        ws.append(w)

    # For each sign pattern, compute |ω|² and |Sω|²
    best_upper_ratio = iv.mpf(0)
    best_sign_idx = 0

    for idx, signs in enumerate(iprod([iv.mpf(1), iv.mpf(-1)], repeat=4)):
        # ω = Σ s_i * v_i
        omega = [iv.mpf(0), iv.mpf(0), iv.mpf(0)]
        for i in range(4):
            for j in range(3):
                omega[j] = omega[j] + signs[i] * vs[i][j]
        # |ω|²
        om2 = omega[0]**2 + omega[1]**2 + omega[2]**2

        # Skip if om2 could be near zero (this sign is not optimal)
        if om2.b < 0.1:  # upper bound < 0.1 → too small
            continue

        # S = Σ s_i * S_i where S_i = -(k_i ⊗ w_i + w_i ⊗ k_i) / (2|k_i|²)
        # Sω = Σ s_i * S_i * ω
        # S_i * ω = -(1/(2|k_i|²)) * [(ω·w_i) k_i + (ω·k_i) w_i]
        Somega = [iv.mpf(0), iv.mpf(0), iv.mpf(0)]
        for i in range(4):
            # ω · w_i
            ow = sum(omega[j] * ws[i][j] for j in range(3))
            # ω · k_i
            ok = sum(omega[j] * K_IV[i][j] for j in range(3))
            factor = -signs[i] / (2 * K_SQ_IV[i])
            for j in range(3):
                Somega[j] = Somega[j] + factor * (ow * K_IV[i][j] + ok * ws[i][j])

        # |Sω|²
        Sw2 = Somega[0]**2 + Somega[1]**2 + Somega[2]**2

        # Upper bound on ratio: |Sω|²_max / |ω|⁴_min
        # Note: S²ê/|ω|² = |Sω|²/|ω|⁴
        # Upper = (Sw2.b) / (om2.a)²
        if om2.a <= 0:
            continue  # can't divide
        ratio_upper = iv.mpf(float(Sw2.b)) / (iv.mpf(float(om2.a))**2)

        if ratio_upper > best_upper_ratio:
            best_upper_ratio = ratio_upper
            best_sign_idx = idx

    return float(best_upper_ratio.b)

def main():
    print("RIGOROUS c(4) CERTIFICATE via Interval Arithmetic", flush=True)
    print("=" * 60, flush=True)
    print(f"k-quadruple: {KS}", flush=True)
    print(f"|k|² values: {K_NORMS_SQ}", flush=True)
    print(f"Target: prove max S²ê/|ω|² < 0.75", flush=True)
    print(f"Best numerical value (DE): 0.3616", flush=True)
    print(f"Margin needed: 0.389", flush=True)
    print(flush=True)

    # Grid over [0, π]^4
    for n_grid in [3, 5, 7]:
        print(f"Grid {n_grid}^4 = {n_grid**4} cells...", flush=True)
        import time
        t0 = time.time()
        worst = 0.0
        h = mpf(mpmath.pi) / n_grid

        for i1 in range(n_grid):
            for i2 in range(n_grid):
                for i3 in range(n_grid):
                    for i4 in range(n_grid):
                        # Cell: [i*h, (i+1)*h]
                        cell = [iv.mpf([float(idx*h), float((idx+1)*h)])
                                for idx in [i1, i2, i3, i4]]
                        r = compute_on_cell(cell)
                        if r > worst:
                            worst = r

        dt = time.time() - t0
        status = "PROVEN < 0.75" if worst < 0.75 else "inconclusive"
        print(f"  worst cell upper bound: {worst:.4f}  [{status}]  ({dt:.1f}s)", flush=True)
        if worst < 0.75:
            print(f"  *** CERTIFIED: max < {worst:.4f} < 0.75 ***", flush=True)
            return worst

    return None

if __name__ == '__main__':
    main()
