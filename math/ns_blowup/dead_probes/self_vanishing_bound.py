"""
Combine the self-vanishing identity with the cross-term identity.

Self-vanishing: |S_k·ê|² = (a_k²/4) sin²γ_k
(per-mode strain in ê direction vanishes for aligned modes)

At x*: ω = |ω|ê = Σ v_k cos(k·x*). So the effective amplitude
along ê is: a_k cosγ_k × cos(k·x*), where cosγ_k = v̂_k · ê.

The sign-flip constraint: a_k cosγ_k cos(k·x*) ≥ 0 for each mode.

The triangle bound on S²ê:
S·ê = Σ (S_k·ê) cos(k·x*)
|S·ê| ≤ Σ |S_k·ê| |cos(k·x*)| ≤ Σ (a_k/2) sinγ_k |cos(k·x*)|

So: S²ê ≤ (Σ (a_k/2) sinγ_k |cos(k·x*)|)²

And: |ω| ≥ Σ a_k cosγ_k cos(k·x*) (with sign-flip: all terms ≥ 0)

Ratio: √(S²ê)/|ω| ≤ Σ(a_k/2)sinγ_k|c_k| / Σ a_k cosγ_k c_k

where c_k = |cos(k·x*)|.

By Cauchy-Schwarz with weights a_k c_k:
Σ (a_k/2)sinγ_k c_k / Σ a_k cosγ_k c_k = (1/2) × (weighted avg of sinγ/cosγ)
= (1/2) × (weighted avg of tanγ)

For tanγ < √3: this ratio < √3/2 = √(3/4). KEY LEMMA!

Question: is tanγ_k < √3 for all modes at the max?
tanγ < √3 ⟺ γ < 60° ⟺ cosγ > 1/2.

At the max: the dominant modes have v̂_k ≈ ê (cosγ ≈ 1, tanγ ≈ 0).
But sub-dominant modes can have any γ.
"""
import numpy as np

def compute_angles_at_max(ks, vs, x_star):
    """Compute γ_k (alignment angle) for each mode at x*."""
    omega = sum(v * np.cos(k @ x_star) for k, v in zip(ks, vs))
    om2 = omega @ omega
    if om2 < 1e-10:
        return None
    e_hat = omega / np.sqrt(om2)

    angles = []
    weights = []
    for k, v in zip(ks, vs):
        c = np.cos(k @ x_star)
        a = np.linalg.norm(v)
        if a < 1e-15:
            continue
        v_hat = v / a
        cos_gamma = abs(v_hat @ e_hat)  # |v̂·ê|
        cos_gamma = min(cos_gamma, 1.0)
        gamma = np.arccos(cos_gamma)
        weight = a * abs(c)  # contribution weight

        angles.append({
            'gamma': gamma,
            'cos_gamma': cos_gamma,
            'sin_gamma': np.sin(gamma),
            'tan_gamma': np.tan(gamma) if cos_gamma > 0.01 else float('inf'),
            'weight': weight,
            'a': a,
            'cos_phase': c,
        })
        weights.append(weight)

    # Weighted average of tanγ
    total_weight = sum(w * d['cos_gamma'] for w, d in zip(weights, angles))
    if total_weight < 1e-10:
        return None

    weighted_tan = sum(w * d['sin_gamma'] for w, d in zip(weights, angles)) / total_weight

    # The triangle bound ratio
    numerator = sum(d['a']/2 * d['sin_gamma'] * abs(d['cos_phase']) for d in angles)
    denominator = np.sqrt(om2)
    ratio = (numerator / denominator)**2 if denominator > 1e-10 else 0

    return {
        'angles': angles,
        'weighted_tan': weighted_tan,
        'triangle_ratio': ratio,
        'om2': om2,
        'max_tan': max(d['tan_gamma'] for d in angles),
        'max_gamma_deg': max(np.degrees(d['gamma']) for d in angles),
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("SELF-VANISHING + TRIANGLE BOUND ANALYSIS")
    print("Need: weighted avg of tanγ < √3 = 1.732")
    print("Or equivalently: Σ(a/2)sinγ|c| / |ω| < √(3/4) = 0.866")
    print("=" * 70)

    worst_wtan = 0
    worst_tratio = 0
    worst_maxgamma = 0

    for trial in range(5000):
        N = np.random.choice([2, 3, 4, 5, 8, 12])
        K_max = 3

        all_modes = []
        for i in range(-K_max, K_max+1):
            for j in range(-K_max, K_max+1):
                for l in range(-K_max, K_max+1):
                    k = np.array([i, j, l], float)
                    if 0 < k @ k <= K_max**2:
                        all_modes.append(k)

        if N > len(all_modes):
            N = len(all_modes)
        idx = np.random.choice(len(all_modes), min(N, len(all_modes)), replace=False)
        ks = [all_modes[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            vs.append(v)

        # Find max
        best_x = np.zeros(3)
        best_om2 = 0
        M = 16
        xs = np.linspace(0, 2*np.pi, M, endpoint=False)
        for i in range(M):
            for j in range(M):
                for l in range(M):
                    x = np.array([xs[i], xs[j], xs[l]])
                    om = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
                    om2 = om @ om
                    if om2 > best_om2:
                        best_om2 = om2
                        best_x = x.copy()

        result = compute_angles_at_max(ks, vs, best_x)
        if result is None:
            continue

        worst_wtan = max(worst_wtan, result['weighted_tan'])
        worst_tratio = max(worst_tratio, result['triangle_ratio'])
        worst_maxgamma = max(worst_maxgamma, result['max_gamma_deg'])

        if trial % 1000 == 0:
            print(f"  {trial}/5000: worst weighted tanγ={worst_wtan:.6f} "
                  f"triangle_ratio={worst_tratio:.6f} "
                  f"max_γ={worst_maxgamma:.1f}°")

    print()
    print(f"RESULTS:")
    print(f"  Worst weighted tanγ: {worst_wtan:.6f} (need < √3 = {np.sqrt(3):.6f})")
    print(f"  Worst triangle ratio: {worst_tratio:.6f} (need < 0.750)")
    print(f"  Worst max γ: {worst_maxgamma:.1f}° (need < 60° for tanγ < √3)")
    print()

    if worst_maxgamma < 60:
        print(f"  All γ < 60°! Weighted tanγ bound gives Key Lemma!")
    else:
        print(f"  Some γ ≥ 60°. Need to check if weighted average still < √3.")

    if worst_wtan < np.sqrt(3):
        print(f"  Weighted tanγ < √3! Triangle bound gives Key Lemma!")
    print(f"  Triangle ratio {worst_tratio:.6f} < 0.750? {worst_tratio < 0.75}")
