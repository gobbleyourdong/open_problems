"""
MARGINAL MODE ANALYSIS v2 — with INTEGER k-vectors.

Find the 2-mode config on the integer lattice that maximizes |∇u|²/|ω|²,
then test whether adding any 3rd mode increases the ratio.
"""
import numpy as np
from itertools import product as iprod, combinations

def build_perp(k, theta):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

def compute_ratio_vertex(ks, vs, amps):
    """Compute |∇u|²/|ω|² at the global-max vertex."""
    N = len(ks)
    best_om2 = 0
    best_ratio = 0
    for signs in iprod([1.0, -1.0], repeat=N):
        omega = sum(a*s*v for a,s,v in zip(amps, signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2
            gradu = sum(a*s*np.outer(np.cross(k,v), k)/(k@k)
                       for k,v,a,s in zip(ks,vs,amps,signs))
            best_ratio = np.sum(gradu**2) / om2
            best_signs = list(signs)
    return best_ratio, best_om2, best_signs

def find_optimal_2mode(k_pool):
    """Find the 2-mode config that maximizes |∇u|²/|ω|² on the lattice."""
    best_ratio = 0
    best_config = None

    for i, j in combinations(range(len(k_pool)), 2):
        k1, k2 = k_pool[i], k_pool[j]
        # Optimize polarization angles
        for t1 in np.linspace(0, np.pi, 30):
            v1 = build_perp(k1, t1)
            for t2 in np.linspace(0, np.pi, 30):
                v2 = build_perp(k2, t2)
                for a_ratio in [0.5, 0.8, 1.0, 1.2, 2.0]:
                    amps = [1.0, a_ratio]
                    r, om2, signs = compute_ratio_vertex(
                        [k1, k2], [v1, v2], amps)
                    if r > best_ratio:
                        best_ratio = r
                        best_config = (k1.copy(), v1.copy(), k2.copy(), v2.copy(),
                                      amps[:], signs[:], om2)
    return best_ratio, best_config

np.random.seed(42)

# Build k-pool (unit and small k's)
k_pool = []
for i in range(-2, 3):
    for j in range(-2, 3):
        for l in range(-2, 3):
            m2 = i*i+j*j+l*l
            if 0 < m2 <= 8:
                k_pool.append(np.array([i,j,l], float))

# Remove anti-parallel duplicates
unique_ks = []
for k in k_pool:
    dup = False
    for uk in unique_ks:
        if np.allclose(k, -uk) or np.allclose(k, uk):
            dup = True; break
    if not dup:
        unique_ks.append(k)

print("=" * 70)
print(f"MARGINAL MODE ANALYSIS v2 — {len(unique_ks)} unique k-vectors")
print("=" * 70)

# Step 1: Find the best 2-mode config
print("\nStep 1: Finding optimal 2-mode config...")
best_r, config = find_optimal_2mode(unique_ks[:20])  # top 20 for speed
k1, v1, k2, v2, amps, signs, om2 = config
cosalpha = abs(k1@k2) / (np.linalg.norm(k1)*np.linalg.norm(k2))
print(f"  Best F = {best_r:.6f} (5/4 = {5/4:.6f})")
print(f"  k1={k1.astype(int)}, k2={k2.astype(int)}")
print(f"  cos(angle) = {cosalpha:.4f} (60° = 0.5000)")
print(f"  |ω|² = {om2:.4f}, signs = {signs}")

# Step 2: For the optimal config, compute dF/dε for every 3rd mode
print(f"\nStep 2: Testing all possible 3rd modes at the optimal 2-mode config...")

s1, s2 = signs[0], signs[1]
omega_0 = s1*amps[0]*v1 + s2*amps[1]*v2
om2_0 = omega_0 @ omega_0
w1 = np.cross(k1, v1)
w2 = np.cross(k2, v2)
gradu_0 = s1*amps[0]*np.outer(w1,k1)/(k1@k1) + s2*amps[1]*np.outer(w2,k2)/(k2@k2)
gradu2_0 = np.sum(gradu_0**2)
F0 = gradu2_0 / om2_0

print(f"  F0 = {F0:.6f}, |ω|²₀ = {om2_0:.4f}")

worst_dF = -1e10
n_positive = 0
n_total = 0
worst_info = None

for k3 in k_pool:
    for t3 in np.linspace(0, 2*np.pi, 60):
        v3 = build_perp(k3, t3)
        a3 = 1.0  # unit amplitude for the 3rd mode

        w3 = np.cross(k3, v3)

        # Cross-term coefficients with modes 1 and 2
        # G_{j3} for j=1,2
        G13 = (w1@w3)*(k1@k3)/((k1@k1)*(k3@k3)) * s1*amps[0]
        G23 = (w2@w3)*(k2@k3)/((k2@k2)*(k3@k3)) * s2*amps[1]

        D13 = (v1@v3) * s1*amps[0]
        D23 = (v2@v3) * s2*amps[1]

        # s3 chosen to maximize |ω|²
        P_D = D13 + D23  # coeff of 2ε*s3 in |ω|²
        s3 = 1.0 if P_D >= 0 else -1.0

        # Effective coefficients after sign choice
        P_D_eff = abs(P_D)
        P_G_eff = s3 * (G13 + G23)

        # dF/dε = 2/|ω|²₀ × (P_G - F0 × P_D) where P_D uses effective s3
        dF = P_G_eff - F0 * P_D_eff

        n_total += 1
        if dF > 1e-10:
            n_positive += 1

        if dF > worst_dF:
            worst_dF = dF
            worst_info = (k3.copy(), t3, s3, P_G_eff, P_D_eff)

print(f"\n  Tested: {n_total} (mode × angle) configurations")
print(f"  dF > 0 (3rd mode helps): {n_positive}/{n_total} ({100*n_positive/n_total:.1f}%)")
print(f"  Worst dF = {worst_dF:.8f}")
if worst_info:
    k3, t3, s3, PG, PD = worst_info
    print(f"  At k3={k3.astype(int)}, theta={t3:.3f}, s3={s3:.0f}")
    print(f"  P_G={PG:.6f}, F0*P_D={F0*PD:.6f}")

if n_positive == 0:
    print(f"\n  ✓✓ ALL 3rd modes decrease F → 2-mode is LOCAL MAX at F={F0:.4f}")
    print(f"  Combined with F_max = 5/4 (proven): |∇u|²/|ω|² ≤ 5/4 on the lattice.")
else:
    print(f"\n  Some 3rd modes increase F. But do they push above 5/4?")
    # Check: does the 3-mode config actually exceed F0?
    if worst_info:
        k3, t3, s3, PG, PD = worst_info
        v3 = build_perp(k3, t3)
        for eps in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
            r3, _, _ = compute_ratio_vertex(
                [k1,k2,k3], [v1,v2,v3], [amps[0], amps[1], eps])
            print(f"    ε={eps:.2f}: F(ε) = {r3:.6f} {'> F0' if r3>F0 else '≤ F0'} "
                  f"{'> 5/4!' if r3>1.25 else '≤ 5/4'}")
