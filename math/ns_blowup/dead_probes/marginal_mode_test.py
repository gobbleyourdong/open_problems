"""
MARGINAL MODE ANALYSIS: compute dF/dε for adding a 3rd mode to the
optimal 2-mode config (the 5/4 extremum).

If dF/dε ≤ 0 for ALL possible 3rd modes: the 2-mode config is a local
maximum, and (by exhaustive search) the GLOBAL maximum of |∇u|²/|ω|².

The optimal 2-mode config (from file 364):
- k₁, k₂ at angle α₁₂ = 60° (cosα = 1/2)
- Equal amplitudes a₁ = a₂ = 1
- Polarizations chosen so excess is maximized
"""
import numpy as np
from itertools import product as iprod

def build_perp(k, theta):
    """Unit vector perpendicular to k, parameterized by angle theta."""
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

def G_coeff(k1, v1, k2, v2):
    """Gradient cross-term coefficient: (w1·w2)(k1·k2)/(|k1|²|k2|²)"""
    w1 = np.cross(k1, v1)
    w2 = np.cross(k2, v2)
    return (w1@w2) * (k1@k2) / ((k1@k1)*(k2@k2))

def D_coeff(v1, v2):
    """Vorticity cross-term coefficient: v1·v2"""
    return v1 @ v2

def optimal_2mode_config():
    """Construct the optimal 2-mode config that achieves F = 5/4.
    k-angle = 60°, equal amplitudes, optimal polarizations."""
    # k1 along z, k2 at 60° in the xz-plane
    k1 = np.array([0, 0, 1.0])
    k2 = np.array([np.sin(np.pi/3), 0, np.cos(np.pi/3)])  # 60° from k1

    # Optimize polarization angles for max excess
    best_ratio = 0
    best_v1 = best_v2 = None
    for t1 in np.linspace(0, 2*np.pi, 100):
        for t2 in np.linspace(0, 2*np.pi, 100):
            v1 = build_perp(k1, t1)
            v2 = build_perp(k2, t2)
            G12 = G_coeff(k1, v1, k2, v2)
            D12 = D_coeff(v1, v2)
            # At global max: s1*s2 chosen to maximize |ω|²
            om2_pp = 2 + 2*D12  # both positive
            om2_pm = 2 - 2*D12  # opposite signs
            # For each sign choice, compute ratio
            for om2, sG in [(om2_pp, G12), (om2_pm, -G12)]:
                if om2 > 0.1:
                    gradu2 = 2 + 2*sG
                    ratio = gradu2 / om2
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_v1, best_v2 = v1.copy(), v2.copy()
                        best_D12 = D12 if om2 == om2_pp else -D12
                        best_G12 = sG

    print(f"Optimal 2-mode: F = {best_ratio:.6f} (expect 5/4 = {5/4:.6f})")
    print(f"  k1 = {k1}, k2 = {k2.round(4)}")
    print(f"  v1 = {best_v1.round(4)}, v2 = {best_v2.round(4)}")
    print(f"  G12 = {best_G12:.4f}, D12 = {best_D12:.4f}")
    return k1, best_v1, k2, best_v2, best_ratio

def test_marginal_mode(k1, v1, k2, v2, F0):
    """Test dF/dε for all possible 3rd modes."""
    G12 = G_coeff(k1, v1, k2, v2)
    D12 = D_coeff(v1, v2)

    # Determine s1, s2 signs at the 2-mode max
    if 2 + 2*D12 >= 2 - 2*D12:
        s1, s2 = 1.0, 1.0
        D12_eff = D12
    else:
        s1, s2 = 1.0, -1.0
        D12_eff = -D12

    om2_0 = 2 + 2*D12_eff
    gradu2_0 = 2 + 2*G_coeff(k1, v1, k2, s2*v2)  # effective with signs

    # Actually, recompute properly with signs
    omega_0 = s1*v1 + s2*v2
    om2_0 = omega_0 @ omega_0
    w1 = np.cross(k1, v1)
    w2 = np.cross(k2, v2)
    gradu_0 = s1*np.outer(w1, k1)/(k1@k1) + s2*np.outer(w2, k2)/(k2@k2)
    gradu2_0 = np.sum(gradu_0**2)

    F0_check = gradu2_0 / om2_0
    print(f"\n2-mode check: F0 = {F0_check:.6f}")

    # Now: sweep over all possible 3rd mode geometries
    # k3 from integer lattice, theta3 from [0, 2π]
    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                if 0 < i*i+j*j+l*l <= 12:
                    k_pool.append(np.array([i,j,l], float))

    worst_dF = -1e10
    worst_config = None
    n_positive = 0
    n_total = 0

    for k3 in k_pool:
        for t3 in np.linspace(0, 2*np.pi, 50):
            v3 = build_perp(k3, t3)

            G13 = G_coeff(k1, v1, k3, v3)
            G23 = G_coeff(k2, v2, k3, v3)
            D13 = D_coeff(v1, v3)
            D23 = D_coeff(v2, v3)

            # s3 chosen to maximize |ω|² = om2_0 + 2ε(s3(s1*D13 + s2*D23)) + O(ε²)
            P_D = s1*D13 + s2*D23  # coefficient of 2ε in |ω|²
            s3 = 1.0 if P_D >= 0 else -1.0
            P_D = abs(P_D)

            P_G = s3*(s1*G13 + s2*G23)  # coefficient of 2ε in |∇u|²

            # dF/dε at ε=0 = 2/|ω|²_0 × (P_G - F0_check × P_D)
            dF = P_G - F0_check * P_D
            # Note: dF > 0 means the 3rd mode INCREASES the ratio

            n_total += 1
            if dF > 1e-10:
                n_positive += 1

            if dF > worst_dF:
                worst_dF = dF
                worst_config = (k3.copy(), t3, s3, P_G, P_D, dF)

    print(f"\nMARGINAL MODE RESULTS ({n_total} configs tested)")
    print(f"  Positive dF (mode increases ratio): {n_positive}/{n_total}")
    print(f"  Worst dF = {worst_dF:.8f}")
    if worst_config:
        k3, t3, s3, PG, PD, dF = worst_config
        print(f"  At k3={k3.astype(int)}, theta={t3:.4f}, s3={s3:.0f}")
        print(f"  P_G={PG:.6f}, P_D={PD:.6f}, F0*P_D={F0_check*PD:.6f}")

    if worst_dF <= 0:
        print(f"\n  ✓✓ dF ≤ 0 for ALL 3rd modes → 2-mode is a LOCAL maximum")
    else:
        print(f"\n  ✗ Some 3rd modes increase F → 2-mode is NOT a local max!")

    return worst_dF

np.random.seed(42)

print("=" * 70)
print("MARGINAL MODE ANALYSIS AT THE 5/4 EXTREMUM")
print("=" * 70)

k1, v1, k2, v2, F0 = optimal_2mode_config()
worst = test_marginal_mode(k1, v1, k2, v2, F0)

# Also test with other near-optimal 2-mode configs
print("\n" + "=" * 70)
print("ROBUSTNESS: test with sub-optimal 2-mode configs (F close to 5/4)")
print("=" * 70)

for trial in range(10):
    # Random 2-mode config with k-angle near 60°
    alpha = np.pi/3 + np.random.uniform(-0.2, 0.2)
    k1 = np.array([0, 0, 1.0])
    k2 = np.array([np.sin(alpha), 0, np.cos(alpha)])
    # Random polarizations
    v1 = build_perp(k1, np.random.uniform(0, 2*np.pi))
    v2 = build_perp(k2, np.random.uniform(0, 2*np.pi))

    # Compute F0
    omega = v1 + v2
    om2 = omega @ omega
    if om2 < 0.1:
        omega = v1 - v2
        om2 = omega @ omega
    gradu = np.outer(np.cross(k1,v1), k1) + np.outer(np.cross(k2,v2), k2)
    if omega@(v1-v2) < 0:
        gradu = np.outer(np.cross(k1,v1), k1) - np.outer(np.cross(k2,v2), k2)
    gradu2 = np.sum(gradu**2)
    F0 = gradu2/om2

    if F0 > 1.15:
        print(f"\n  Trial {trial}: F0 = {F0:.4f}, alpha = {np.degrees(alpha):.1f}°")
        # Quick marginal test with 100 random 3rd modes
        n_pos = 0
        worst_dF = -1e10
        for _ in range(500):
            k3 = k_pool[np.random.randint(len(k_pool))]
            v3 = build_perp(k3, np.random.uniform(0, 2*np.pi))
            G13 = G_coeff(k1,v1,k3,v3)
            G23 = G_coeff(k2,v2,k3,v3)
            D13 = D_coeff(v1,v3)
            D23 = D_coeff(v2,v3)
            PD = D13 + D23  # assuming s1=s2=1
            s3 = 1 if PD >= 0 else -1
            PG = s3*(G13+G23)
            PD = abs(PD)
            dF = PG - F0*PD
            if dF > 1e-10: n_pos += 1
            worst_dF = max(worst_dF, dF)
        print(f"    Positive: {n_pos}/500, worst dF = {worst_dF:.6f}")
