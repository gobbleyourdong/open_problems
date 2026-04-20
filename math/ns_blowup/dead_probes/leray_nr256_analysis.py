"""
Leray transform analysis on Nr=256 data.

Goal: Map physical (r,z,t) data into Leray self-similar coordinates:
  ξ = r / √(T*-t),  τ = -ln(T*-t)
  Ω̃ = (T*-t) · |ω|_max   (should be constant for self-similar blowup)
  Ã = (T*-t)^{1/2} · α     (strain in Leray frame)

We fit T* by minimizing variance of Ω̃ over the spectrally clean range.
Then check for limit cycle behavior in the (Γ, Ω̃) phase plane.
"""
import sys, os, json
import numpy as np

def load_log(path):
    """Parse log format: step=... t=... G=... R=... a=... spec=... |w|=..."""
    entries = []
    with open(path) as f:
        for line in f:
            if not line.startswith('step=') or 'CHECKPOINT' in line:
                continue
            try:
                tokens = line.split()
                e = {
                    'step': int(tokens[0].replace('step=', '')),
                    't': float(tokens[1].replace('t=', '')),
                    'gamma': float(tokens[2].replace('G=', '')),
                }
                for tok in tokens[3:]:
                    if tok.startswith('R='):
                        e['R_rms'] = float(tok.replace('R=', ''))
                    elif tok.startswith('a='):
                        e['alpha'] = float(tok.replace('a=', ''))
                    elif tok.startswith('spec='):
                        e['spectral'] = float(tok.replace('spec=', ''))
                    elif tok.startswith('|w|='):
                        e['om1'] = float(tok.replace('|w|=', ''))
                entries.append(e)
            except:
                pass
    return entries

def load_json(path):
    with open(path) as f:
        return json.load(f)

def fit_T_star(t_arr, omega_arr, t_max_clean):
    """
    Fit T* by minimizing variance of Ω̃ = (T*-t) · |ω|_max.
    Only use spectrally clean data (t < t_max_clean).
    """
    mask = (t_arr > 0) & (t_arr < t_max_clean) & (omega_arr > 0)
    t_c = t_arr[mask]
    w_c = omega_arr[mask]

    if len(t_c) < 5:
        return None, None

    # Try different T* values and find the one that makes Ω̃ most constant
    best_T = None
    best_cv = 1e30  # coefficient of variation

    t_last = t_c[-1]
    # Search T* from just beyond data to 10x beyond
    for T_star in np.linspace(t_last * 1.01, t_last * 5.0, 10000):
        omega_tilde = (T_star - t_c) * w_c
        cv = omega_tilde.std() / (omega_tilde.mean() + 1e-30)
        if cv < best_cv:
            best_cv = cv
            best_T = T_star

    return best_T, best_cv

def main():
    # Load data
    base = os.path.dirname(__file__)

    # Try log first, then JSON
    log_path = os.path.join(base, "results", "h200_sync", "gamma_nr256_full_final.log")
    json_path = os.path.join(base, "results", "h200_sync", "gamma_nr256_extended.json")

    if os.path.exists(log_path):
        data = load_log(log_path)
        print(f"Loaded {len(data)} entries from log")
    elif os.path.exists(json_path):
        data = load_json(json_path)
        print(f"Loaded {len(data)} entries from JSON")
    else:
        print("No data found!")
        return

    # Filter to step > 0
    data = [d for d in data if d['step'] > 0 and d.get('om1', 0) > 0]

    t_arr = np.array([d['t'] for d in data])
    omega_arr = np.array([d['om1'] for d in data])
    gamma_arr = np.array([d['gamma'] for d in data])
    step_arr = np.array([d['step'] for d in data])
    spec_arr = np.array([d.get('spectral', 0) for d in data])
    alpha_arr = np.array([d.get('alpha', 0) for d in data])
    R_arr = np.array([d.get('R_rms', 0) for d in data])

    # Find spectrally clean range (spec < 0.01)
    clean_mask = spec_arr < 0.01
    t_max_clean = t_arr[clean_mask][-1] if clean_mask.any() else t_arr[-1]
    step_max_clean = step_arr[clean_mask][-1] if clean_mask.any() else step_arr[-1]
    print(f"Spectrally clean range: t < {t_max_clean:.6f} (step {step_max_clean})")

    # =========================================================
    # 1. Fit T* assuming Leray scaling: |ω| ~ (T*-t)^{-1}
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 1: FIT T* (LERAY BLOWUP TIME)")
    print("="*60)

    T_star, cv = fit_T_star(t_arr, omega_arr, t_max_clean)
    if T_star is None:
        print("FAILED to fit T*")
        return

    print(f"T* = {T_star:.8f}")
    print(f"CV(Ω̃) = {cv:.6f}  (0 = perfect self-similarity)")
    print(f"Time to blowup from last clean: {T_star - t_max_clean:.6f}")

    # Also fit with different scaling exponents
    # |ω| ~ (T*-t)^{-γ}  → Ω̃ = (T*-t)^γ · |ω|
    print("\n--- Scaling exponent scan ---")
    for gamma_exp in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
        best_T = None
        best_cv = 1e30
        for T_try in np.linspace(t_max_clean * 1.01, t_max_clean * 5.0, 5000):
            mask = (t_arr > 0) & (t_arr < t_max_clean)
            tau = T_try - t_arr[mask]
            omega_tilde = tau**gamma_exp * omega_arr[mask]
            cv_try = omega_tilde.std() / (omega_tilde.mean() + 1e-30)
            if cv_try < best_cv:
                best_cv = cv_try
                best_T = T_try
        print(f"  γ={gamma_exp:.2f}: T*={best_T:.6f}  CV={best_cv:.6f}")

    # =========================================================
    # 2. Compute Leray-scaled quantities with best T*
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 2: LERAY-SCALED DIAGNOSTICS")
    print("="*60)

    tau = T_star - t_arr
    tau_log = -np.log(tau)  # Leray time
    omega_tilde = tau * omega_arr  # Ω̃ = (T*-t)|ω|
    alpha_tilde = np.sqrt(tau) * alpha_arr  # Ã = √(T*-t) · α
    R_tilde = R_arr / np.sqrt(tau)  # R̃ = R/√(T*-t)

    # Print evolution in Leray frame
    print(f"\n{'step':>6} {'t':>10} {'τ':>8} {'Γ':>8} {'Ω̃':>10} {'Ã':>10} {'R̃':>8} {'spec':>8}")
    print("-" * 80)
    for i in range(0, len(data), 10):  # every 10th entry (every 2000 steps)
        if i < len(data):
            print(f"{step_arr[i]:6.0f} {t_arr[i]:10.6f} {tau_log[i]:8.4f} "
                  f"{gamma_arr[i]:8.4f} {omega_tilde[i]:10.2f} "
                  f"{alpha_tilde[i]:10.4f} {R_tilde[i]:8.4f} {spec_arr[i]:8.5f}")

    # =========================================================
    # 3. Self-similarity quality
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 3: SELF-SIMILARITY QUALITY")
    print("="*60)

    # Over clean range
    clean = (t_arr > 0.001) & (t_arr < t_max_clean)
    om_t_clean = omega_tilde[clean]
    print(f"\nΩ̃ over clean range:")
    print(f"  Mean: {om_t_clean.mean():.2f}")
    print(f"  Std:  {om_t_clean.std():.2f}")
    print(f"  CV:   {om_t_clean.std()/om_t_clean.mean():.4f}")
    print(f"  Min:  {om_t_clean.min():.2f} at step {step_arr[clean][om_t_clean.argmin()]:.0f}")
    print(f"  Max:  {om_t_clean.max():.2f} at step {step_arr[clean][om_t_clean.argmax()]:.0f}")

    # Check if Ω̃ has any periodicity
    # Detrend and compute autocorrelation
    om_detrended = om_t_clean - np.mean(om_t_clean)
    if len(om_detrended) > 10:
        autocorr = np.correlate(om_detrended, om_detrended, mode='full')
        autocorr = autocorr[len(autocorr)//2:]
        autocorr /= autocorr[0] + 1e-30

        # Find first peak after lag 0
        peaks = []
        for j in range(2, len(autocorr)-1):
            if autocorr[j] > autocorr[j-1] and autocorr[j] > autocorr[j+1] and autocorr[j] > 0.3:
                peaks.append((j, autocorr[j]))

        if peaks:
            print(f"\n  Autocorrelation peaks (lag, corr):")
            for lag, corr in peaks[:5]:
                period_steps = lag * 200  # 200 steps per sample
                print(f"    lag={lag} ({period_steps} steps): corr={corr:.4f}")
        else:
            print(f"\n  No significant autocorrelation peaks (no periodicity detected)")

    # =========================================================
    # 4. Phase plane analysis: (Γ, Ω̃)
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 4: PHASE PLANE (Γ, Ω̃)")
    print("="*60)

    # Compute dΓ/dτ and dΩ̃/dτ (numerical derivatives in Leray time)
    d_tau_log = np.diff(tau_log)
    d_gamma = np.diff(gamma_arr)
    d_omega_t = np.diff(omega_tilde)

    dG_dtau = d_gamma / (d_tau_log + 1e-30)
    dOm_dtau = d_omega_t / (d_tau_log + 1e-30)

    # Look for Γ minimum and characterize the trajectory there
    gamma_min_idx = np.argmin(gamma_arr[clean])
    # Map back to full array
    clean_indices = np.where(clean)[0]
    min_full_idx = clean_indices[gamma_min_idx]

    print(f"\nΓ minimum in clean range:")
    print(f"  Γ_min = {gamma_arr[min_full_idx]:.6f} at step {step_arr[min_full_idx]:.0f}")
    print(f"  t = {t_arr[min_full_idx]:.6f}")
    print(f"  Ω̃ at Γ_min = {omega_tilde[min_full_idx]:.2f}")
    print(f"  Ã at Γ_min = {alpha_tilde[min_full_idx]:.4f}")

    # Trajectory curvature near minimum
    if min_full_idx > 2 and min_full_idx < len(gamma_arr) - 3:
        window = 5
        g_near = gamma_arr[min_full_idx-window:min_full_idx+window+1]
        om_near = omega_tilde[min_full_idx-window:min_full_idx+window+1]
        print(f"\n  Trajectory near minimum (window ±{window} samples = ±{window*200} steps):")
        for j in range(len(g_near)):
            marker = " ←" if j == window else ""
            print(f"    Γ={g_near[j]:.6f}  Ω̃={om_near[j]:.2f}{marker}")

    # =========================================================
    # 5. S/νP ratio in Leray frame
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 5: S/νP RATIO EVOLUTION")
    print("="*60)

    # From Γ = (S-νP)/(S+νP), we can recover S/νP = (1+Γ)/(1-Γ)
    ratio_SvP = (1 + gamma_arr) / (1 - gamma_arr + 1e-30)

    print(f"\nS/(νP) ratio evolution:")
    print(f"{'step':>6} {'Γ':>8} {'S/νP':>10}")
    print("-" * 30)
    for i in range(0, len(data), 10):
        if i < len(data) and gamma_arr[i] < 0.999:
            print(f"{step_arr[i]:6.0f} {gamma_arr[i]:8.4f} {ratio_SvP[i]:10.2f}")

    # In Leray frame, both S and νP scale as (T*-t)^{-2}
    # So their RATIO should be constant (or slowly varying) for self-similar blowup
    ratio_clean = ratio_SvP[clean]
    print(f"\nS/νP over clean range:")
    print(f"  Initial: {ratio_clean[0]:.2f}")
    print(f"  At Γ_min: {ratio_SvP[min_full_idx]:.2f}")
    print(f"  Final clean: {ratio_clean[-1]:.2f}")
    print(f"  Trend: {'monotonically decreasing' if all(np.diff(ratio_clean[:20]) < 0) else 'non-monotonic'}")

    # =========================================================
    # 6. Key diagnostic: is this approaching a fixed point or limit cycle?
    # =========================================================
    print("\n" + "="*60)
    print("PHASE 6: FIXED POINT vs LIMIT CYCLE")
    print("="*60)

    # If Ω̃ → constant AND Γ → constant in Leray time → fixed point (Type I blowup)
    # If Ω̃ and Γ oscillate with period in Leray time → limit cycle (Type II / DSS blowup)
    # If Γ → 0 monotonically → viscosity wins (regularity)

    # Check late-time behavior of Γ in Leray frame
    late = clean & (step_arr > step_max_clean * 0.5)
    if late.any():
        g_late = gamma_arr[late]
        om_late = omega_tilde[late]
        tau_late = tau_log[late]

        # Fit Γ vs τ (Leray time) to see if it's approaching 0 or a constant
        coeffs = np.polyfit(tau_late - tau_late[0], g_late, 1)
        slope = coeffs[0]
        intercept = coeffs[1]

        # Project: at what Leray time does Γ hit 0?
        if slope < 0:
            tau_zero = -intercept / slope + tau_late[0]
            t_zero = T_star * np.exp(-tau_zero) if tau_zero < 50 else 0
            print(f"\nΓ linear fit in Leray time (late half):")
            print(f"  dΓ/dτ = {slope:.6f}")
            print(f"  Γ intercept = {intercept:.6f}")
            print(f"  Γ→0 at τ = {tau_zero:.4f}")
            if t_zero > 0:
                print(f"  Corresponds to t = {t_zero:.8f}")
                print(f"  That's BEFORE T* = {T_star:.8f}" if t_zero < T_star else
                      f"  That's AFTER T* (inconsistent)")

            # What does this mean?
            if tau_zero < tau_log[clean][-1] + 5:
                print(f"\n  INTERPRETATION: Γ→0 in finite Leray time")
                print(f"  → Viscosity wins BEFORE blowup")
                print(f"  → This is REGULARITY, not blowup")
            else:
                print(f"\n  INTERPRETATION: Γ→0 very slowly in Leray time")
                print(f"  → Race is close but stretching still leads")
        else:
            print(f"\nΓ is NOT decreasing in Leray time (slope = {slope:.6f})")
            print(f"  → Stretching may permanently dominate")

    # Check Ω̃ trend
    if late.any():
        om_coeffs = np.polyfit(tau_late - tau_late[0], om_late, 1)
        print(f"\nΩ̃ linear fit in Leray time:")
        print(f"  dΩ̃/dτ = {om_coeffs[0]:.4f}")
        if abs(om_coeffs[0]) < 0.1 * om_late.mean():
            print(f"  → Ω̃ approximately CONSTANT (self-similar!)")
        elif om_coeffs[0] > 0:
            print(f"  → Ω̃ growing — super-Leray blowup rate")
        else:
            print(f"  → Ω̃ decaying — sub-Leray rate (regularity?)")

    # =========================================================
    # 7. PLOT
    # =========================================================
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(3, 2, figsize=(16, 14))
        fig.suptitle(f'Leray Analysis — Nr=256, ν=1e-4, T*={T_star:.6f}', fontsize=14)

        # 1. Γ vs physical time
        ax = axes[0, 0]
        ax.plot(t_arr, gamma_arr, 'b-', linewidth=1.5)
        ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        ax.axvline(x=t_max_clean, color='orange', linestyle=':', alpha=0.7, label=f'spec limit')
        ax.set_ylabel('Γ')
        ax.set_xlabel('t (physical)')
        ax.set_title('Gap Frame Γ')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # 2. Γ vs Leray time
        ax = axes[0, 1]
        ax.plot(tau_log, gamma_arr, 'b-', linewidth=1.5)
        ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        clean_boundary_tau = tau_log[clean][-1] if clean.any() else tau_log[-1]
        ax.axvline(x=clean_boundary_tau, color='orange', linestyle=':', alpha=0.7)
        ax.set_ylabel('Γ')
        ax.set_xlabel('τ = -ln(T*-t)')
        ax.set_title('Γ in Leray Time')
        ax.grid(True, alpha=0.3)

        # 3. Ω̃ vs Leray time
        ax = axes[1, 0]
        ax.plot(tau_log, omega_tilde, 'k-', linewidth=1.5)
        ax.axvline(x=clean_boundary_tau, color='orange', linestyle=':', alpha=0.7)
        ax.set_ylabel('Ω̃ = (T*-t)|ω|_max')
        ax.set_xlabel('τ = -ln(T*-t)')
        ax.set_title('Rescaled Vorticity')
        ax.grid(True, alpha=0.3)

        # 4. Phase plane: Γ vs Ω̃
        ax = axes[1, 1]
        # Color by time
        sc = ax.scatter(gamma_arr[clean], omega_tilde[clean],
                       c=tau_log[clean], cmap='viridis', s=10, alpha=0.7)
        ax.set_xlabel('Γ')
        ax.set_ylabel('Ω̃')
        ax.set_title('Phase Plane (Γ, Ω̃) — color=τ')
        plt.colorbar(sc, ax=ax, label='τ')
        ax.grid(True, alpha=0.3)
        # Mark start and end
        ax.plot(gamma_arr[clean][0], omega_tilde[clean][0], 'go', markersize=10, label='start')
        ax.plot(gamma_arr[clean][-1], omega_tilde[clean][-1], 'r*', markersize=15, label='end')
        ax.legend()

        # 5. S/νP ratio vs Leray time
        ax = axes[2, 0]
        ax.plot(tau_log[clean], ratio_SvP[clean], 'g-', linewidth=1.5)
        ax.set_ylabel('S / (νP)')
        ax.set_xlabel('τ = -ln(T*-t)')
        ax.set_title('Stretching/Dissipation Ratio')
        ax.axhline(y=1, color='r', linestyle='--', alpha=0.5, label='S=νP')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # 6. |ω| with Leray fit
        ax = axes[2, 1]
        ax.semilogy(t_arr, omega_arr, 'k-', linewidth=1.5, label='|ω|_max')
        # Plot Leray prediction
        t_pred = np.linspace(t_arr[1], T_star * 0.99, 200)
        omega_pred = omega_tilde[clean].mean() / (T_star - t_pred)
        ax.semilogy(t_pred, omega_pred, 'r--', linewidth=1, alpha=0.7, label=f'Leray: C/(T*-t)')
        ax.axvline(x=T_star, color='red', linestyle=':', alpha=0.5, label=f'T*={T_star:.5f}')
        ax.set_xlabel('t')
        ax.set_ylabel('|ω|_max')
        ax.set_title('Vorticity Growth vs Leray Prediction')
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        out_path = os.path.join(base, "leray_nr256_analysis.png")
        plt.savefig(out_path, dpi=150)
        print(f"\nSaved plot to {out_path}")
        plt.close()

    except ImportError:
        print("\nmatplotlib not available, skipping plots")

    # =========================================================
    # VERDICT
    # =========================================================
    print("\n" + "="*60)
    print("VERDICT")
    print("="*60)

    # Summarize
    ratio_at_min = ratio_SvP[min_full_idx]
    print(f"\n1. Best-fit T* = {T_star:.8f}")
    print(f"   Last clean data at t = {t_max_clean:.6f}")
    print(f"   Gap to T*: {T_star - t_max_clean:.6f}")
    print(f"   CV(Ω̃) = {cv:.4f} ({'good' if cv < 0.1 else 'poor'} self-similarity)")

    print(f"\n2. At Γ minimum (step {step_arr[min_full_idx]:.0f}):")
    print(f"   Γ = {gamma_arr[min_full_idx]:.6f}")
    print(f"   S/νP = {ratio_at_min:.2f}")
    print(f"   Stretching {'still leads' if ratio_at_min > 1 else 'has lost'}")

    print(f"\n3. Trajectory type:")
    if cv < 0.05:
        print(f"   STRONG self-similarity (CV < 5%)")
        print(f"   → Consistent with Type I blowup")
    elif cv < 0.15:
        print(f"   APPROXIMATE self-similarity (CV {cv:.1%})")
        print(f"   → Could be approaching fixed point or slow orbit")
    else:
        print(f"   WEAK self-similarity (CV {cv:.1%})")
        print(f"   → Not clearly self-similar at this resolution")

if __name__ == '__main__':
    main()
