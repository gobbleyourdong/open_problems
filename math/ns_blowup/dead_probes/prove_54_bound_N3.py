"""
Prove |∇u|²/|ω|² ≤ 5/4 for N=3 modes at the global max.

From file 364: the 2-mode case achieves 5/4 exactly at α=60°.
Question: can 3 modes produce a higher ratio?

Strategy:
1. Gradient-based adversarial optimization (maximize the ratio)
2. Exhaustive search over k-vector triples
3. Analytical bound via pairwise excess decomposition
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def compute_ratio_from_params(params, N_modes, all_ks):
    """Compute -|∇u|²/|ω|² from optimization parameters."""
    # params: [k_indices(N), v_angles(N), amplitudes(N)]
    # Each mode: k from lattice, v = perp to k parametrized by angle, amplitude
    N = N_modes
    k_idx = np.clip(np.round(params[:N]).astype(int), 0, len(all_ks)-1)
    angles = params[N:2*N]
    amps = np.exp(params[2*N:3*N])  # positive amplitudes

    ks, vs = [], []
    for i in range(N):
        k = all_ks[k_idx[i]]
        kn = k / np.linalg.norm(k)
        # Perpendicular basis
        e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        v = np.cos(angles[i])*e1 + np.sin(angles[i])*e2
        ks.append(k)
        vs.append(v)

    # Find global max
    best_om2 = 0
    best_x = None
    for _ in range(12):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
            return -(om@om)
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x

    if best_om2 < 0.01 or best_x is None:
        return 0

    # Compute |∇u|² and |ω|² at global max
    omega = np.zeros(3)
    gradu = np.zeros((3,3))
    for k,v,a in zip(ks,vs,amps):
        c = np.cos(k@best_x)
        omega += a*v*c
        w = np.cross(k,v)
        gradu += a*np.outer(w,k)*c/(k@k)

    om2 = omega@omega
    if om2 < 0.01: return 0
    gradu2 = np.sum(gradu**2)
    return gradu2/om2

def random_search(N_modes, n_trials=2000, max_k=2):
    """Random search for worst |∇u|²/|ω|²."""
    all_ks = []
    for i in range(-max_k, max_k+1):
        for j in range(-max_k, max_k+1):
            for l in range(-max_k, max_k+1):
                if 0 < i*i+j*j+l*l <= max_k*max_k*3:
                    all_ks.append(np.array([i,j,l],float))

    worst = 0
    worst_config = None

    for trial in range(n_trials):
        idx = np.random.choice(len(all_ks), N_modes, replace=False)
        ks = [all_ks[i] for i in idx]
        vs = []
        for k in ks:
            kn = k/np.linalg.norm(k)
            v = np.random.randn(3)
            v -= (v@kn)*kn
            v /= np.linalg.norm(v)
            vs.append(v)
        amps = np.exp(np.random.uniform(-0.5, 0.5, N_modes))

        # Find global max
        best_om2 = 0
        best_x = None
        for _ in range(15):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            def f(xyz):
                om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
                return -(om@om)
            res = minimize(f, x0, method='Nelder-Mead',
                          options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000})
            if -res.fun > best_om2:
                best_om2 = -res.fun
                best_x = res.x

        if best_om2 < 0.01 or best_x is None:
            continue

        omega = np.zeros(3)
        gradu = np.zeros((3,3))
        S = np.zeros((3,3))
        for k,v,a in zip(ks,vs,amps):
            c = np.cos(k@best_x)
            omega += a*v*c
            w = np.cross(k,v)
            gu = a*np.outer(w,k)*c/(k@k)
            gradu += gu
            S += 0.5*(gu+gu.T)

        om2 = omega@omega
        if om2 < 0.01: continue
        gradu2 = np.sum(gradu**2)
        S2 = np.sum(S**2)
        e = omega/np.sqrt(om2)
        Se = S@e
        S2e = Se@Se

        ratio = gradu2/om2
        if ratio > worst:
            worst = ratio
            worst_config = {
                'ratio': ratio, 'S2e_ratio': S2e/om2, 'S_ratio': S2/om2,
                'ks': [k.copy() for k in ks], 'vs': [v.copy() for v in vs],
                'amps': amps.copy(), 'om2': om2
            }

        if trial % 500 == 0 and trial > 0:
            print(f"  [{trial}] worst |∇u|²/|ω|² = {worst:.6f}", flush=True)

    return worst, worst_config

# Also: test the PAIRWISE EXCESS BOUND
def test_pairwise_excess(N_modes, n_trials=1000):
    """Test if total EXCESS ≤ |ω|²/4 (would prove 5/4 bound for all N)."""
    all_ks = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                if 0 < i*i+j*j+l*l <= 12:
                    all_ks.append(np.array([i,j,l],float))

    worst_excess_ratio = 0

    for trial in range(n_trials):
        idx = np.random.choice(len(all_ks), min(N_modes, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]
        vs = []
        for k in ks:
            kn = k/np.linalg.norm(k)
            v = np.random.randn(3)
            v -= (v@kn)*kn
            v /= np.linalg.norm(v)
            vs.append(v)
        amps = np.ones(len(ks))

        best_om2 = 0
        best_x = None
        for _ in range(12):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            def f(xyz):
                om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
                return -(om@om)
            res = minimize(f, x0, method='Nelder-Mead',
                          options={'xatol':1e-10,'fatol':1e-12,'maxiter':3000})
            if -res.fun > best_om2:
                best_om2 = -res.fun
                best_x = res.x

        if best_om2 < 0.01 or best_x is None: continue

        omega = np.zeros(3)
        gradu2 = 0
        for k,v,a in zip(ks,vs,amps):
            c = np.cos(k@best_x)
            omega += a*v*c
            w = np.cross(k,v)
            gu = a*np.outer(w,k)*c/(k@k)
            gradu2 += np.sum(gu**2)
            # Cross terms
            for k2,v2,a2 in zip(ks,vs,amps):
                if k2 is not k:
                    c2 = np.cos(k2@best_x)
                    w2 = np.cross(k2,v2)
                    gu2 = a2*np.outer(w2,k2)*c2/(k2@k2)
                    gradu2 += np.sum(gu*gu2)

        # Actually compute properly
        gradu_full = np.zeros((3,3))
        for k,v,a in zip(ks,vs,amps):
            c = np.cos(k@best_x)
            w = np.cross(k,v)
            gradu_full += a*np.outer(w,k)*c/(k@k)
        gradu2 = np.sum(gradu_full**2)

        om2 = omega@omega
        excess = gradu2 - om2
        excess_ratio = excess / om2

        worst_excess_ratio = max(worst_excess_ratio, excess_ratio)

    return worst_excess_ratio


if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 60)
    print("|∇u|²/|ω|² BOUND TEST — seeking to prove ≤ 5/4 for all N")
    print("=" * 60)

    for N in [2, 3, 4, 5, 7]:
        n = 1500 if N <= 4 else 800
        print(f"\nN = {N} modes ({n} trials)...")
        worst, config = random_search(N, n_trials=n)
        if config:
            print(f"  Worst |∇u|²/|ω|² = {worst:.6f} (threshold 5/4 = 1.250)")
            print(f"  At this config: S²ê/|ω|² = {config['S2e_ratio']:.6f}")
            if worst < 1.25:
                print(f"  ✓ Below 5/4 threshold (margin: {1.25-worst:.4f})")
            else:
                print(f"  ✗ EXCEEDS 5/4!")

    print("\n" + "=" * 60)
    print("PAIRWISE EXCESS TEST: is EXCESS/|ω|² ≤ 1/4?")
    print("=" * 60)
    for N in [3, 5, 8, 12]:
        n = 500
        worst_ex = test_pairwise_excess(N, n)
        status = "✓" if worst_ex < 0.25 else "✗"
        print(f"  N={N:2d}: worst EXCESS/|ω|² = {worst_ex:.6f} (threshold 1/4 = 0.250) {status}")
