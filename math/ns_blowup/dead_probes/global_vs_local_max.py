"""
CRITICAL TEST: S²ê/|ω|² at GLOBAL max vs LOCAL maxima.

The 2-mode case with d = v̂₁·v̂₂ = -1/2 has:
- Global max |ω|² = 3 at anti-phase vertex: S²ê/|ω|² = 1/12
- Local max |ω|² = 1 at same-phase vertex: S²ê/|ω|² = 3/4

The barrier only needs to hold at the GLOBAL max. This test verifies
that the ratio is always much smaller at the global max than at local extrema.

Also tests the EXACT formula for N=2 at the global max:
  S²ê/|ω|² = (1-|d|) / (4(1+|d|)) ≤ 1/4
"""
import numpy as np
from scipy.optimize import minimize

def compute_ratio_2mode(d_val):
    """Compute S²ê/|ω|² at the GLOBAL max for 2 equal-amplitude modes with v̂₁·v̂₂ = d."""
    # Formula from file 363:
    # At the global max vertex: |ω|² = 2+2|d|, d_eff = |d|
    # S²ê = (1-|d|)/2
    # S²ê/|ω|² = (1-|d|) / (4(1+|d|))
    d = abs(d_val)
    S2e = (1 - d) / 2
    om2 = 2 + 2*d
    ratio = S2e / om2
    return ratio, S2e, om2

def verify_2mode_formula():
    """Verify the analytical formula against direct computation."""
    print("=" * 70)
    print("2-MODE FORMULA VERIFICATION: S²ê/|ω|² at GLOBAL max")
    print("=" * 70)
    print(f"  {'d':>6} | {'formula':>8} | {'computed':>8} | {'local_max':>10} | {'ratio_local':>12}")
    print("-" * 65)

    for d_val in np.linspace(-0.99, 0.99, 20):
        # Create 2 modes with v̂₁·v̂₂ = d_val
        v1 = np.array([1.0, 0.0, 0.0])
        v2 = np.array([d_val, np.sqrt(1-d_val**2), 0.0])
        k1 = np.array([0, 0, 1.0])  # perpendicular to v1
        k2 = np.array([0, 0, 1.0])  # Same k (won't affect the algebra at vertices)

        # Actually, need DIFFERENT k's. Use k1 = (0,0,1), k2 = (0,1,0)
        # v1 ⊥ k1 = (0,0,1): v1 in xy-plane. OK, v1 = (1,0,0). ✓
        # v2 ⊥ k2 = (0,1,0): v2 in xz-plane. v2 = (d_val, 0, sqrt(1-d²)).
        k1 = np.array([0.0, 0.0, 1.0])
        k2 = np.array([0.0, 1.0, 0.0])
        v1 = np.array([1.0, 0.0, 0.0])
        v2_raw = np.array([d_val, 0.0, np.sqrt(max(0, 1-d_val**2))])
        # Ensure v2 ⊥ k2
        v2_raw -= (v2_raw @ k2) * k2 / (k2 @ k2)
        norm2 = np.linalg.norm(v2_raw)
        if norm2 < 1e-10:
            continue
        v2 = v2_raw / norm2

        actual_d = v1 @ v2

        # Evaluate at all 4 vertices
        vertices = [(1,1), (1,-1), (-1,1), (-1,-1)]
        best_om2 = 0
        best_S2e = 0
        best_vertex = None
        all_data = []

        for s1, s2 in vertices:
            omega = s1 * v1 + s2 * v2
            om2 = omega @ omega
            if om2 < 1e-10:
                all_data.append((s1, s2, om2, 0))
                continue
            e_hat = omega / np.sqrt(om2)

            # Compute S at this vertex
            S = np.zeros((3, 3))
            for k, v, s in [(k1, v1, s1), (k2, v2, s2)]:
                w = np.cross(k, v)
                gu = s * np.outer(w, k) / (k @ k)
                S += 0.5 * (gu + gu.T)

            Se = S @ e_hat
            S2e = Se @ Se
            all_data.append((s1, s2, om2, S2e / om2 if om2 > 0.01 else 0))

            if om2 > best_om2:
                best_om2 = om2
                best_S2e = S2e
                best_vertex = (s1, s2)

        ratio_formula = compute_ratio_2mode(actual_d)[0]
        ratio_computed = best_S2e / best_om2 if best_om2 > 0.01 else 0

        # Find the LOCAL maximum (secondary vertex)
        local_om2 = 0
        local_ratio = 0
        for s1, s2, om2, r in all_data:
            if om2 > 0.01 and om2 < best_om2 * 0.99:
                if r > local_ratio:
                    local_ratio = r
                    local_om2 = om2

        print(f"  {actual_d:6.3f} | {ratio_formula:8.4f} | {ratio_computed:8.4f} | {local_om2:10.4f} | {local_ratio:12.4f}")

    print(f"\nFormula: S²ê/|ω|² = (1-|d|)/(4(1+|d|)) ≤ 1/4 at d=0")

def test_global_max_guarantee():
    """Test that S²ê/|ω|² < 3/4 at the GLOBAL max for many random configs."""
    print("\n" + "=" * 70)
    print("GLOBAL MAX GUARANTEE: random modes, various N")
    print("=" * 70)

    np.random.seed(42)

    # Integer k-vectors
    all_ks = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                if 0 < i*i+j*j+l*l <= 12:
                    all_ks.append(np.array([i,j,l], float))

    for N in [2, 3, 5, 8, 12]:
        worst_global = 0
        worst_local = 0
        n_trials = 500

        for trial in range(n_trials):
            idx = np.random.choice(len(all_ks), min(N, len(all_ks)), replace=False)
            ks = [all_ks[i] for i in idx]
            vs = []
            for k in ks:
                v = np.random.randn(3)
                v -= (v @ k) * k / (k @ k)
                v /= np.linalg.norm(v)
                vs.append(v)
            amps = np.ones(N)

            # Multi-start optimization for global max
            best_om2 = 0
            best_x = None
            for _ in range(15):
                x0 = np.random.uniform(0, 2*np.pi, 3)
                def neg_om2(xyz):
                    omega = np.zeros(3)
                    for k, v, a in zip(ks, vs, amps):
                        omega += a * v * np.cos(k @ xyz)
                    return -omega @ omega
                res = minimize(neg_om2, x0, method='Nelder-Mead',
                              options={'xatol':1e-10, 'fatol':1e-12, 'maxiter':5000})
                if -res.fun > best_om2:
                    best_om2 = -res.fun
                    best_x = res.x.copy()

            if best_om2 < 0.01:
                continue

            # Compute at global max
            omega = np.zeros(3)
            S = np.zeros((3, 3))
            for k, v, a in zip(ks, vs, amps):
                c = np.cos(k @ best_x)
                omega += a * v * c
                w = np.cross(k, v)
                gu = a * np.outer(w, k) * c / (k @ k)
                S += 0.5 * (gu + gu.T)

            om2 = omega @ omega
            e_hat = omega / np.sqrt(om2)
            Se = S @ e_hat
            S2e = Se @ Se
            ratio = S2e / om2

            worst_global = max(worst_global, ratio)

        barrier = "PASS" if worst_global < 0.75 else "FAIL"
        print(f"  N={N:2d}: worst S²ê/|ω|² at GLOBAL max = {worst_global:.6f}  ({barrier}, margin={(0.75-worst_global)/0.75*100:.0f}%)")


if __name__ == '__main__':
    verify_2mode_formula()
    test_global_max_guarantee()
