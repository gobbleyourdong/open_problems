"""
Fast worst-case search for N=3 S²ê/|ω|² at the global max.
Focus: is the orthogonal symmetric config (1/3) the true worst case?
"""
import numpy as np
from scipy.optimize import minimize

def compute_ratio(k1,v1,k2,v2,k3,v3):
    """Fast: compute S²ê/|ω|² at global max. 8 multi-starts."""
    ks = [np.asarray(k,float) for k in [k1,k2,k3]]
    vs = [np.asarray(v,float) for v in [v1,v2,v3]]

    best_om2 = 0
    best_x = None
    for _ in range(8):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(v * np.cos(k @ xyz) for k,v in zip(ks,vs))
            return -om @ om
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x

    if best_om2 < 0.01 or best_x is None:
        return 0

    omega = np.zeros(3)
    S = np.zeros((3,3))
    for k,v in zip(ks,vs):
        c = np.cos(k @ best_x)
        omega += v * c
        w = np.cross(k, v)
        gu = np.outer(w, k) * c / (k@k)
        S += 0.5 * (gu + gu.T)

    om2 = omega @ omega
    if om2 < 0.01: return 0
    e = omega / np.sqrt(om2)
    Se = S @ e
    return (Se @ Se) / om2

def rand_perp(k):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    r = np.random.randn(3)
    r -= (r @ kn) * kn
    return r / np.linalg.norm(r)

def perp_from_angle(k, theta):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

np.random.seed(42)

# Test 1: Known orthogonal symmetric
print("=== TEST 1: Orthogonal symmetric (known 1/3) ===")
r = compute_ratio([1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[1,0,0])
print(f"S²ê/|ω|² = {r:.6f} (expected 0.333333)")

# Test 2: Optimize v̂ angles for orthogonal k's
print("\n=== TEST 2: Optimize v̂ for orthogonal k's ===")
k1,k2,k3 = [1,0,0.],[0,1,0.],[0,0,1.]
best = 0
for _ in range(500):
    t = np.random.uniform(0, 2*np.pi, 3)
    v1 = perp_from_angle(k1, t[0])
    v2 = perp_from_angle(k2, t[1])
    v3 = perp_from_angle(k3, t[2])
    r = compute_ratio(k1,v1,k2,v2,k3,v3)
    best = max(best, r)
print(f"Worst: {best:.6f} (is 1/3 = {1/3:.6f} the max?)")

# Test 3: Random k-vectors from lattice
print("\n=== TEST 3: Random k's from lattice ===")
all_ks = []
for i in range(-2,3):
    for j in range(-2,3):
        for l in range(-2,3):
            m2 = i*i+j*j+l*l
            if 0 < m2 <= 6:
                all_ks.append(np.array([i,j,l],float))

worst = 0
worst_ks = None
for trial in range(2000):
    idx = np.random.choice(len(all_ks), 3, replace=False)
    k1,k2,k3 = all_ks[idx[0]], all_ks[idx[1]], all_ks[idx[2]]
    v1,v2,v3 = rand_perp(k1), rand_perp(k2), rand_perp(k3)
    r = compute_ratio(k1,v1,k2,v2,k3,v3)
    if r > worst:
        worst = r
        worst_ks = (k1.copy(),v1.copy(),k2.copy(),v2.copy(),k3.copy(),v3.copy())
    if trial % 500 == 0 and trial > 0:
        print(f"  [{trial}] worst = {worst:.6f}")

print(f"Worst: {worst:.6f}")
if worst_ks:
    k1,v1,k2,v2,k3,v3 = worst_ks
    print(f"  k₁={k1.astype(int)}, k₂={k2.astype(int)}, k₃={k3.astype(int)}")
    print(f"  k₁·k₂={k1@k2:.0f}, k₁·k₃={k1@k3:.0f}, k₂·k₃={k2@k3:.0f}")

# Test 4: Specifically test non-orthogonal k's that SHARE components
print("\n=== TEST 4: Adversarial non-orthogonal k's ===")
adversarial_ks = [
    ([1,0,0],[1,1,0],[0,1,0]),  # k₁·k₂ = 1
    ([1,0,0],[1,1,0],[1,0,1]),  # all pairs share
    ([1,1,0],[1,0,1],[0,1,1]),  # all pairs k·k = 1
    ([1,0,0],[0,1,0],[1,1,0]),  # mixed
    ([1,1,0],[1,-1,0],[0,0,1]), # antiparallel pair
    ([1,1,1],[1,-1,0],[0,1,-1]),# tetrahedral-ish
]

for ks_triple in adversarial_ks:
    k1,k2,k3 = [np.array(k,float) for k in ks_triple]
    best_r = 0
    for _ in range(200):
        v1,v2,v3 = rand_perp(k1), rand_perp(k2), rand_perp(k3)
        r = compute_ratio(k1,v1,k2,v2,k3,v3)
        best_r = max(best_r, r)
    dots = f"dots=({k1@k2:.0f},{k1@k3:.0f},{k2@k3:.0f})"
    print(f"  k={ks_triple}: worst={best_r:.4f} {dots}")

print("\n=== SUMMARY ===")
print(f"Orthogonal symmetric: 1/3 = 0.3333")
print(f"Best found over all configs: {max(worst, best, r):.4f}")
print(f"Bound needed: < 0.75")
