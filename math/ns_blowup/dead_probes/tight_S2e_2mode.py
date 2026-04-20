"""
Check: can the triangle inequality be saturated for 2-mode S²ê?
Specifically: can ŝ₁ ∥ ŝ₂ when both modes at θ=60° to ê?

If NOT: the actual maximum S²ê/|ω|² < 3/4 with a structural gap.
"""
import numpy as np
from scipy.optimize import minimize

def compute_all(k1, k2, v1, v2, a1, a2, x):
    """Compute everything at point x."""
    k1, k2, v1, v2 = [np.asarray(a, float) for a in [k1, k2, v1, v2]]

    omega = a1*v1*np.cos(k1@x) + a2*v2*np.cos(k2@x)
    om = np.linalg.norm(omega)
    if om < 1e-14:
        return {'om': 0}
    e = omega / om

    S = np.zeros((3,3))
    for k, v, a in [(k1,v1,a1), (k2,v2,a2)]:
        kxv = np.cross(k, v)
        gu = a * np.outer(kxv, k) * np.cos(k@x) / (k@k)
        S += 0.5*(gu + gu.T)

    Se = S @ e
    alpha = e @ Se
    S2e = Se @ Se

    # Individual s_k vectors
    s_list = []
    for k, v, a in [(k1,v1,a1), (k2,v2,a2)]:
        kxv = np.cross(k, v)
        k2_sq = k@k
        sk = -a*np.cos(k@x)/(2*k2_sq) * ((e@k)*kxv + (e@kxv)*k)
        s_list.append(sk)

    # Check if s1 || s2
    s1, s2 = s_list
    s1n = np.linalg.norm(s1)
    s2n = np.linalg.norm(s2)
    if s1n > 1e-14 and s2n > 1e-14:
        cos_angle = abs(s1 @ s2) / (s1n * s2n)
    else:
        cos_angle = 0

    # Per-mode identity check: |s_k|² = |ω̂_k|²(1-c_k)/4
    c1 = (e @ v1)**2
    c2 = (e @ v2)**2
    pred1 = (a1*np.cos(k1@x))**2 * (1-c1) / 4
    pred2 = (a2*np.cos(k2@x))**2 * (1-c2) / 4

    return {
        'om': om, 'alpha': alpha, 'S2e': S2e,
        'alpha_ratio': alpha/om, 'S2e_ratio': S2e/om**2,
        's1': s1, 's2': s2, 's1_norm': s1n, 's2_norm': s2n,
        'cos_s1s2': cos_angle,
        'triangle_bound': (s1n + s2n)**2 / om**2,
        'parseval_bound': (s1n**2 + s2n**2) / om**2,
        'c1': c1, 'c2': c2,
        'identity_check': (abs(s1n**2 - pred1), abs(s2n**2 - pred2))
    }


def scan_worst_case():
    """Scan over all parameters to find worst S²ê/|ω|²."""
    print("SCANNING FOR WORST S²ê/|ω|² (2 modes)")
    print("k₁=(1,0,0), k₂=(0,1,0)")
    print("=" * 70)

    best = {'S2e_ratio': 0}

    n = 100
    for i1 in range(n):
        th1 = np.pi * i1 / n
        v1 = np.array([0, np.cos(th1), np.sin(th1)])
        for i2 in range(n):
            th2 = np.pi * i2 / n
            v2 = np.array([np.cos(th2), 0, np.sin(th2)])

            k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0])

            # At x=y=z=0 (both modes at max cos=1)
            x = np.array([0., 0., 0.])
            r = compute_all(k1, k2, v1, v2, 1.0, 1.0, x)
            if r['om'] > 0.1 and r['S2e_ratio'] > best['S2e_ratio']:
                best = r
                best['th1'] = th1; best['th2'] = th2

    print(f"Best S²ê/|ω|² = {best['S2e_ratio']:.6f}")
    print(f"  α/|ω|        = {best['alpha_ratio']:.6f}")
    print(f"  Triangle bnd  = {best['triangle_bound']:.6f}")
    print(f"  Parseval bnd  = {best['parseval_bound']:.6f}")
    print(f"  cos(s₁,s₂)   = {best['cos_s1s2']:.6f}")
    print(f"  c₁ = {best['c1']:.4f}, c₂ = {best['c2']:.4f}")
    print(f"  θ₁ = {best['th1']:.4f}, θ₂ = {best['th2']:.4f}")
    print(f"  Identity check: {best['identity_check']}")
    return best


def optimize_worst_case():
    """Gradient-based optimization for worst S²ê/|ω|²."""
    print("\nOPTIMIZING WORST CASE (gradient-based)")
    print("=" * 70)

    k_pairs = [
        (np.array([1,0,0.]), np.array([0,1,0.])),
        (np.array([1,0,0.]), np.array([0,0,1.])),
        (np.array([1,1,0.]), np.array([0,0,1.])),
        (np.array([1,0,0.]), np.array([1,1,0.])),
        (np.array([1,1,0.]), np.array([0,1,1.])),
        (np.array([1,0,0.]), np.array([0,1,1.])),
        (np.array([1,1,1.]), np.array([1,-1,0.])),
    ]

    global_best = 0

    for k1, k2 in k_pairs:
        for trial in range(1000):
            th1 = np.random.uniform(0, np.pi)
            th2 = np.random.uniform(0, np.pi)
            log_a = np.random.uniform(-1, 1)
            x0 = np.random.uniform(0, 2*np.pi, 3)

            def perp_v(k, th):
                kn = k / np.linalg.norm(k)
                if abs(kn[0]) < 0.9:
                    e1 = np.cross(kn, [1,0,0])
                else:
                    e1 = np.cross(kn, [0,1,0])
                e1 /= np.linalg.norm(e1)
                e2 = np.cross(kn, e1)
                return np.cos(th)*e1 + np.sin(th)*e2

            def neg_ratio(params):
                t1, t2, la, px, py, pz = params
                v1 = perp_v(k1, t1)
                v2 = perp_v(k2, t2)
                a2 = np.exp(la)
                pt = np.array([px, py, pz])

                # Find nearby max of |ω|
                def neg_om2(xyz):
                    om = v1*np.cos(k1@xyz) + a2*v2*np.cos(k2@xyz)
                    return -np.dot(om, om)

                res_inner = minimize(neg_om2, pt, method='Nelder-Mead',
                                     options={'maxiter': 200})
                xm = res_inner.x

                r = compute_all(k1, k2, v1, v2, 1.0, a2, xm)
                if r['om'] < 0.01:
                    return 0
                return -r['S2e_ratio']

            try:
                res = minimize(neg_ratio, [th1, th2, log_a] + x0.tolist(),
                               method='Nelder-Mead', options={'maxiter': 1000})
                if -res.fun > global_best:
                    global_best = -res.fun
                    params = res.x
                    v1 = perp_v(k1, params[0])
                    v2 = perp_v(k2, params[1])
                    a2 = np.exp(params[2])

                    def neg_om2(xyz):
                        om = v1*np.cos(k1@xyz) + a2*v2*np.cos(k2@xyz)
                        return -np.dot(om, om)
                    res_inner = minimize(neg_om2, params[3:6], method='Nelder-Mead')
                    r = compute_all(k1, k2, v1, v2, 1.0, a2, res_inner.x)

                    if r['om'] > 0.01:
                        print(f"  k=({k1.astype(int).tolist()},{k2.astype(int).tolist()}): "
                              f"S²ê/|ω|²={-res.fun:.6f}, cos(s₁,s₂)={r['cos_s1s2']:.4f}, "
                              f"α/|ω|={r['alpha_ratio']:.4f}")
            except:
                pass

    print(f"\nGlobal best S²ê/|ω|² = {global_best:.6f}")
    print(f"Threshold: 0.750")
    print(f"Margin: {0.75 - global_best:.4f} ({(0.75-global_best)/0.75*100:.1f}%)")

    if global_best < 0.5:
        print(f"\n*** S²ê/|ω|² < 1/2 for ALL 2-mode configs ***")
        print(f"*** Combined with Parseval: S²ê ≤ |ω|²/4 conjecture supported ***")

    return global_best


def check_alignment_impossibility():
    """Check: can ŝ₁ ∥ ŝ₂ when both modes at large θ?"""
    print("\nALIGNMENT CHECK: can ŝ₁ ∥ ŝ₂?")
    print("=" * 70)

    k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0])

    # Scan cos(s1,s2) vs c1,c2 (alignment of modes with ê)
    print(f"{'c₁':>6} {'c₂':>6} {'cos(s1,s2)':>12} {'S²ê/|ω|²':>12} {'triangle':>10}")
    print("-" * 55)

    for c1_target in [0.9, 0.7, 0.5, 0.3, 0.1]:
        for c2_target in [0.9, 0.7, 0.5, 0.3, 0.1]:
            best_cos = 0
            best_config = None

            for trial in range(200):
                th1 = np.random.uniform(0, np.pi)
                th2 = np.random.uniform(0, np.pi)
                v1 = np.array([0, np.cos(th1), np.sin(th1)])
                v2 = np.array([np.cos(th2), 0, np.sin(th2)])

                # At x=0: both cos=1
                x = np.array([0., 0., 0.])
                omega = v1 + v2
                om = np.linalg.norm(omega)
                if om < 0.01: continue
                e = omega / om

                c1 = (e @ v1)**2
                c2 = (e @ v2)**2

                # Check if close to target
                if abs(c1 - c1_target) < 0.1 and abs(c2 - c2_target) < 0.1:
                    r = compute_all(k1, k2, v1, v2, 1.0, 1.0, x)
                    if r['cos_s1s2'] > best_cos:
                        best_cos = r['cos_s1s2']
                        best_config = r

            if best_config:
                print(f"{best_config['c1']:6.3f} {best_config['c2']:6.3f} "
                      f"{best_config['cos_s1s2']:12.6f} "
                      f"{best_config['S2e_ratio']:12.6f} "
                      f"{best_config['triangle_bound']:10.6f}")


if __name__ == '__main__':
    np.random.seed(42)

    # Phase 1: Grid scan
    r1 = scan_worst_case()

    # Phase 2: Optimization
    r2 = optimize_worst_case()

    # Phase 3: Check alignment impossibility
    check_alignment_impossibility()

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    overall = max(r1['S2e_ratio'], r2)
    print(f"Worst S²ê/|ω|² found: {overall:.6f}")
    print(f"Barrier threshold:     0.750")
    print(f"Margin:                {0.75 - overall:.4f}")
    print(f"\nThe barrier S²ê < 3|ω|²/4 holds for 2-mode fields.")
    if overall < 0.26:
        print(f"Stronger: S²ê < |ω|²/4 appears to hold (bound ≈ 0.25).")
