"""
HESSIAN CONSTRAINT at x* = argmax|ω|².

At x*: H = ∂²|ω|²/∂x∂x ≤ 0 (negative semi-definite).

H_αβ = -2Σ_k (ω·v_k)(k_k)_α(k_k)_β cos(k·x*)
       -2Σ_k Σ_j≠k (v_j·v_k)(k_j)_α sin(k_j·x*)(k_k)_β sin(k_k·x*) ...

Wait, need to be more careful. Let me compute H directly.

|ω(x)|² = Σ_{j,k} (v_j·v_k) cos(k_j·x) cos(k_k·x)

∂²|ω|²/∂x_α∂x_β = Σ_{j,k} (v_j·v_k) {
  -(k_j)_α sin(k_j·x) × -(k_k)_β sin(k_k·x)
  + cos(k_j·x) × -(k_k)_α(k_k)_β cos(k_k·x)  [if j=k only?]
}

Actually simpler: |ω|² = ω·ω.
∂(ω·ω)/∂x_α = 2ω·∂ω/∂x_α
∂²(ω·ω)/∂x_α∂x_β = 2(∂ω/∂x_α·∂ω/∂x_β + ω·∂²ω/∂x_α∂x_β)

∂ω/∂x_α = -Σ_k v_k (k_k)_α sin(k_k·x)
∂²ω/∂x_α∂x_β = -Σ_k v_k (k_k)_α (k_k)_β cos(k_k·x)

At x*:
H_αβ = 2Σ_{j,k} (v_j·v_k)(k_j)_α(k_k)_β sin(k_j·x*)sin(k_k·x*)
      - 2Σ_k (ω·v_k)(k_k)_α(k_k)_β cos(k_k·x*)

H ≤ 0 at the max. This gives constraints on the sin values.

The second term is negative for dominant modes (ω·v_k > 0, cos > 0):
contributes to making H negative (good).

The first term can be positive or negative. For H ≤ 0: the first term
can't be too positive.

KEY QUESTION: Does H ≤ 0 constrain C from below?

C involves cos·cos terms. The Hessian involves sin·sin and cos terms.
The connection is through cos² + sin² = 1.
"""
import numpy as np

def compute_hessian_and_correction(ks, vs, x_star):
    """Compute the Hessian of |ω|² and the correction C at x*."""
    N = len(ks)

    omega = sum(v * np.cos(k @ x_star) for k, v in zip(ks, vs))
    om2 = omega @ omega
    if om2 < 1e-10:
        return None

    # Hessian
    # First term: Σ (v_j·v_k)(k_j)_α(k_k)_β sin_j sin_k
    # Second term: -Σ (ω·v_k)(k_k)_α(k_k)_β cos_k

    sines = [np.sin(k @ x_star) for k in ks]
    cosines = [np.cos(k @ x_star) for k in ks]

    H = np.zeros((3, 3))

    # First term
    for j in range(N):
        for l in range(N):
            vv = vs[j] @ vs[l]
            for a in range(3):
                for b in range(3):
                    H[a,b] += 2 * vv * ks[j][a] * ks[l][b] * sines[j] * sines[l]

    # Second term
    for k_idx in range(N):
        ov = omega @ vs[k_idx]
        for a in range(3):
            for b in range(3):
                H[a,b] -= 2 * ov * ks[k_idx][a] * ks[k_idx][b] * cosines[k_idx]

    # Check H ≤ 0
    eigenvalues = np.linalg.eigvalsh(H)
    max_eigenvalue = np.max(eigenvalues)

    # Correction C
    correction = 0.0
    for j in range(N):
        for l in range(j+1, N):
            n = np.cross(ks[j], ks[l])
            n_norm = np.linalg.norm(n)
            if n_norm < 1e-12:
                continue
            n_hat = n / n_norm
            cos_theta = (ks[j] @ ks[l]) / (np.linalg.norm(ks[j]) * np.linalg.norm(ks[l]))
            sin2_theta = 1 - cos_theta**2
            P = (vs[j] @ n_hat) * (vs[l] @ n_hat) * sin2_theta
            phase = cosines[j] * cosines[l]
            correction += P * phase

    # Sum of sin²
    sin2_sum = sum(s**2 for s in sines)
    cos2_sum = sum(c**2 for c in cosines)

    # Trace of Hessian: simple expression
    # Tr(H) = 2Σ_{j,k} (v_j·v_k)(k_j·k_k) sin_j sin_k - 2Σ_k (ω·v_k)|k|² cos_k
    trace_H = 0
    for j in range(N):
        for l in range(N):
            trace_H += 2 * (vs[j]@vs[l]) * (ks[j]@ks[l]) * sines[j]*sines[l]
    for k_idx in range(N):
        trace_H -= 2 * (omega@vs[k_idx]) * (ks[k_idx]@ks[k_idx]) * cosines[k_idx]

    return {
        'om2': om2,
        'correction': correction,
        'corr_ratio': correction / om2,
        'max_eigenvalue': max_eigenvalue,
        'trace_H': trace_H,
        'sin2_sum': sin2_sum,
        'cos2_sum': cos2_sum,
        'eigenvalues': eigenvalues,
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("HESSIAN CONSTRAINT ANALYSIS")
    print("At x* = argmax|ω|²: H ≤ 0 constrains sin values")
    print("=" * 70)

    # Collect data on the relationship between H and C
    data = []

    for trial in range(5000):
        N = np.random.choice([2, 3, 4, 5, 6, 8])
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

        result = compute_hessian_and_correction(ks, vs, best_x)
        if result is None:
            continue

        data.append(result)

    # Analyze
    corr_ratios = [d['corr_ratio'] for d in data]
    max_eigs = [d['max_eigenvalue'] for d in data]
    traces = [d['trace_H'] for d in data]

    print(f"\nHessian at the max:")
    print(f"  Max eigenvalue: always ≤ 0? {all(e <= 1e-6 for e in max_eigs)}")
    print(f"  Worst max eigenvalue: {max(max_eigs):.6f}")
    print(f"  Mean trace: {np.mean(traces):.6f}")

    print(f"\nCorrection at the max:")
    print(f"  Worst C/|ω|²: {min(corr_ratios):.6f} (need > -0.250)")
    print(f"  Mean C/|ω|²: {np.mean(corr_ratios):.6f}")

    # Is there a correlation between trace(H) and C?
    neg_corr = [(d['corr_ratio'], d['trace_H']/d['om2']) for d in data if d['corr_ratio'] < 0]
    if neg_corr:
        cr, tr = zip(*neg_corr)
        correlation = np.corrcoef(cr, tr)[0,1]
        print(f"\n  Correlation(C/|ω|², Tr(H)/|ω|²) for C<0 cases: {correlation:.4f}")

    # KEY: For H ≤ 0, the trace is negative: Tr(H) ≤ 0
    # Tr(H) = 2|∇ω|²_sin - 2Σ(ω·v_k)|k|²c_k  [simplified]
    # where |∇ω|²_sin = Σ(v_j·v_k)(k_j·k_k)s_j s_k

    # At the max: Tr(H) ≤ 0 means the "ω gradient energy" from sines
    # is bounded by the "ω diagonal energy" from cosines.

    print(f"\n  Tr(H) ≤ 0 at all maxima? {all(d['trace_H'] <= 1e-6 for d in data)}")

    # Check: does Tr(H) ≤ 0 give C > -|ω|²/4?
    # Tr(H) involves different quantities than C. The link is through cos²+sin²=1.

    print(f"\n  sin²_sum mean: {np.mean([d['sin2_sum'] for d in data]):.4f}")
    print(f"  cos²_sum mean: {np.mean([d['cos2_sum'] for d in data]):.4f}")
    print(f"  For N modes: cos² + sin² = N per mode, so sum = N")
