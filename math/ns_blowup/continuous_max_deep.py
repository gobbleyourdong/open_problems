"""
Deep test: when IS the max off-lattice? And what constrains S²ê there?
Focus on N≥4 where the off-lattice max can occur.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution
from itertools import product as iproduct

def get_K_shell(K2):
    R = int(np.sqrt(K2)) + 1
    vecs = []
    for kx in range(-R, R+1):
        for ky in range(-R, R+1):
            for kz in range(-R, R+1):
                if kx*kx + ky*ky + kz*kz == K2:
                    vecs.append(np.array([kx, ky, kz], dtype=float))
    half = []
    seen = set()
    for v in vecs:
        t = tuple(v.astype(int))
        neg = tuple(-x for x in t)
        if t not in seen and neg not in seen:
            half.append(v)
            seen.add(t)
    return half

def random_div_free_v(k, amp=None):
    v = np.random.randn(3)
    v -= (v @ k) / (k @ k) * k
    v /= np.linalg.norm(v)
    if amp is not None:
        v *= amp
    else:
        v *= np.random.uniform(0.5, 2.0)
    return v

def omega_at(x, ks, vs):
    return sum(v * np.cos(k @ x) for k, v in zip(ks, vs))

def omega2_at(x, ks, vs):
    w = omega_at(x, ks, vs)
    return w @ w

def strain_at(x, ks, vs):
    S = np.zeros((3,3))
    for k, v in zip(ks, vs):
        u_hat = np.cross(k, v) / (k @ k)
        s = np.sin(k @ x)
        S -= 0.5 * (np.outer(u_hat, k) + np.outer(k, u_hat)) * s
    return S

def S2e_at(x, ks, vs):
    w = omega_at(x, ks, vs)
    w2 = w @ w
    if w2 < 1e-20:
        return 0.0, 0.0, 0.0
    e = w / np.sqrt(w2)
    S = strain_at(x, ks, vs)
    Se = S @ e
    S2e = Se @ Se
    S2_frob = np.sum(S**2)
    return S2e, S2_frob, w2

def find_max(ks, vs, n_restarts=30):
    bounds = [(0, 2*np.pi)]*3
    result = differential_evolution(
        lambda x: -omega2_at(x, ks, vs),
        bounds, seed=42, maxiter=1000, tol=1e-14, polish=True
    )
    best_val = -result.fun
    best_x = result.x.copy()
    for _ in range(n_restarts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        res = minimize(lambda x: -omega2_at(x, ks, vs), x0,
                      method='Nelder-Mead',
                      options={'xatol': 1e-15, 'fatol': 1e-15, 'maxiter': 10000})
        if -res.fun > best_val + 1e-13:
            best_val = -res.fun
            best_x = res.x.copy()
    return best_val, best_x

def main():
    np.random.seed(0)

    # Multi-shell test: mix K²=2 and K²=3 modes
    k2_vecs = get_K_shell(2)
    k3_vecs = get_K_shell(3)
    print(f"K²=2: {len(k2_vecs)} vectors, K²=3: {len(k3_vecs)} vectors")

    configs = [
        ("K2 only, N=4", k2_vecs, 4),
        ("K2 only, N=5", k2_vecs, 5),
        ("K2 only, N=6", k2_vecs, 6),
        ("K3 only, N=4", k3_vecs, 4),
        ("K2+K3 mixed, N=4", k2_vecs + k3_vecs, 4),
        ("K2+K3 mixed, N=5", k2_vecs + k3_vecs, 5),
        ("K2+K3 mixed, N=6", k2_vecs + k3_vecs, 6),
        ("K2+K3 mixed, N=8", k2_vecs + k3_vecs, 8),
    ]

    for name, pool, N in configs:
        if N > len(pool):
            continue
        print(f"\n{'='*60}")
        print(f"{name} ({200} trials)")

        n_off = 0
        worst_S2e = 0.0
        worst_S2 = 0.0
        worst_case = None

        for trial in range(200):
            idx = np.random.choice(len(pool), N, replace=False)
            ks = [pool[i] for i in idx]
            vs = [random_div_free_v(k) for k in ks]

            val, x = find_max(ks, vs)
            max_sin = max(abs(np.sin(k @ x)) for k in ks)

            if max_sin > 1e-6:
                n_off += 1
                S2e, S2_f, w2 = S2e_at(x, ks, vs)
                r_S2e = S2e / w2 if w2 > 1e-15 else 0
                r_S2 = S2_f / w2 if w2 > 1e-15 else 0

                if r_S2e > worst_S2e:
                    worst_S2e = r_S2e
                    worst_S2 = r_S2
                    worst_case = (trial, N, max_sin, r_S2e, r_S2)

        print(f"  Off-lattice: {n_off}/200 ({100*n_off/200:.1f}%)")
        if worst_case:
            t, n, ms, rs, rf = worst_case
            print(f"  Worst: trial={t}, max_sin={ms:.4f}, S²ê/|ω|²={rs:.6f}, |S|²/|ω|²={rf:.6f}")
            print(f"  Threshold S²ê/|ω|² = 0.750, margin = {(0.75-rs)/0.75*100:.1f}%")
        else:
            print(f"  ALL at sin=0 lattice! S=0, Key Lemma trivially holds.")

    # Critical: adversarial search
    print(f"\n{'='*60}")
    print("ADVERSARIAL SEARCH: maximize S²ê/|ω|² at global max of |ω|²")
    print("Trying to find the WORST configuration...")

    all_k = k2_vecs + k3_vecs
    worst_ever = 0.0

    for trial in range(500):
        N = np.random.choice([4, 5, 6, 7, 8])
        N = min(N, len(all_k))
        idx = np.random.choice(len(all_k), N, replace=False)
        ks = [all_k[i] for i in idx]
        vs = [random_div_free_v(k) for k in ks]

        val, x = find_max(ks, vs)
        S2e, S2_f, w2 = S2e_at(x, ks, vs)
        r = S2e / w2 if w2 > 1e-15 else 0

        if r > worst_ever:
            worst_ever = r
            max_sin = max(abs(np.sin(k @ x)) for k in ks)
            print(f"  New worst: trial={trial}, N={N}, S²ê/|ω|²={r:.6f}, "
                  f"|S|²/|ω|²={S2_f/w2:.6f}, max_sin={max_sin:.4f}")

    print(f"\n  WORST S²ê/|ω|² = {worst_ever:.6f}")
    print(f"  Threshold: 0.750")
    print(f"  Margin: {(0.75-worst_ever)/0.75*100:.1f}%")

if __name__ == '__main__':
    main()
