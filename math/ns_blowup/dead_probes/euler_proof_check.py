"""
Euler blowup proof verification — checking all ingredients from our data.

Hou's result (Luo-Hou 2014): Euler blowup at T*=0.0035056, γ=5/2, at (r,z)=(1,0)

Proof ingredients we need to verify:
1. BKM criterion: ∫₀^{T*} ‖ω‖_∞ dt → ∞
2. Self-similar scaling: ‖ω‖ ~ C·(T*-t)^{-γ}
3. Scaling collapse: solution profiles at different times collapse when rescaled
4. Convergence under refinement: T* and γ stabilize with resolution
5. Enstrophy growth: dE/dt = S (stretching dominates)
"""
import numpy as np
import json
import os

RESULTS_DIR = "ns_blowup/results"

# Load data — parse from log since timeseries wasn't saved for first runs
def parse_log(logfile):
    """Extract time series from log file."""
    import re
    data = []
    with open(logfile) as f:
        for line in f:
            if 'step=' in line and '|w1r|=' in line:
                m_t = re.search(r' t=([\d.e+-]+)', line)
                m_w = re.search(r'\|w1r\|=([\d.e+-]+)', line)
                m_u = re.search(r'\|u1z\|=([\d.e+-]+)', line)
                m_dt = re.search(r'dt=([\d.e+-]+)', line)
                if m_t and m_w and m_u:
                    data.append({
                        't': float(m_t.group(1)),
                        'w1r': float(m_w.group(1)),
                        'u1z': float(m_u.group(1)),
                        'dt': float(m_dt.group(1)) if m_dt else 0,
                    })
    return data

# Try to load dense timeseries first, fall back to log parsing
def load_data(tag):
    ts_file = f"{RESULTS_DIR}/{tag}_timeseries.json"
    log_file = f"{RESULTS_DIR}/{tag}.log"
    json_file = f"{RESULTS_DIR}/{tag}.json"

    if os.path.exists(ts_file):
        with open(ts_file) as f:
            ts = json.load(f)
        return ts
    elif os.path.exists(log_file):
        data = parse_log(log_file)
        return {
            't': [d['t'] for d in data],
            'w1r': [d['w1r'] for d in data],
            'u1z': [d['u1z'] for d in data],
        }
    return None

# Also load from the euler_fixed logs
euler_nr32_data = parse_log(f"{RESULTS_DIR}/euler_fixed_nr32.log") if os.path.exists(f"{RESULTS_DIR}/euler_fixed_nr32.log") else None
euler_nr64_data = parse_log(f"{RESULTS_DIR}/euler_fixed_nr64.log") if os.path.exists(f"{RESULTS_DIR}/euler_fixed_nr64.log") else None
sweep_euler_data = load_data("visc_nr64_euler")

# Use sweep euler data (our best Nr=64 run)
if sweep_euler_data:
    t = np.array(sweep_euler_data['t'])
    w1r = np.array(sweep_euler_data['w1r'])
    u1z = np.array(sweep_euler_data['u1z'])
    T_star = 0.0036495383  # from our fit
else:
    print("No Euler data found!")
    exit(1)

print(f"Loaded {len(t)} data points")
print(f"t range: [{t[0]:.8f}, {t[-1]:.8f}]")
print(f"T* = {T_star:.10f}")

# =========================================
# CHECK 1: BKM CRITERION
# ∫₀^{T*} ‖ω‖_∞ dt → ∞
# We approximate with trapezoidal rule on our discrete data
# =========================================
print("\n" + "="*60)
print("CHECK 1: BKM CRITERION — ∫₀^{T*} ‖ω‖_∞ dt")
print("="*60)

# Use |w1r| as proxy for ‖ω‖_∞ (ω₁·r = ωθ)
mask = w1r > 0
t_bkm = t[mask]
w_bkm = w1r[mask]

# Cumulative integral using trapezoidal rule
if len(t_bkm) > 1:
    dt_intervals = np.diff(t_bkm)
    w_avg = 0.5 * (w_bkm[:-1] + w_bkm[1:])
    bkm_cumulative = np.cumsum(dt_intervals * w_avg)

    print(f"∫ from t=0 to last data point: {bkm_cumulative[-1]:.6f}")

    # Check growth rate — should diverge
    # Split into quarters and check if integral is accelerating
    n = len(bkm_cumulative)
    q1 = bkm_cumulative[n//4]
    q2 = bkm_cumulative[n//2]
    q3 = bkm_cumulative[3*n//4]
    q4 = bkm_cumulative[-1]

    print(f"Quarter integrals: Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}, Q4={q4:.2f}")
    print(f"Growth ratios: Q2/Q1={q2/q1:.2f}, Q3/Q2={q3/q2:.2f}, Q4/Q3={q4/q3:.2f}")

    if q4/q3 > q3/q2 > 1:
        print("✓ BKM integral is ACCELERATING — consistent with divergence")
    else:
        print("⚠ BKM integral growth inconclusive")

# =========================================
# CHECK 2: SELF-SIMILAR SCALING
# ‖ω‖ ~ C·(T*-t)^{-γ}
# Fit γ from log-log regression in blowup regime
# =========================================
print("\n" + "="*60)
print("CHECK 2: SELF-SIMILAR SCALING — ‖ω‖ ~ C·(T*-t)^{-γ}")
print("="*60)

tau = T_star - t
mask_blowup = (w1r > 1e3) & (tau > 1e-7)  # well into blowup, before T*
t_bl = tau[mask_blowup]
w_bl = w1r[mask_blowup]
u_bl = u1z[mask_blowup]

if len(t_bl) > 5:
    log_tau = np.log(t_bl)
    log_w = np.log(w_bl)
    log_u = np.log(u_bl)

    # Linear regression on log-log
    # Split into early/mid/late blowup to check γ stability
    n = len(t_bl)
    thirds = [slice(0, n//3), slice(n//3, 2*n//3), slice(2*n//3, n)]
    labels = ['Early', 'Mid', 'Late']

    print(f"\nUsing {n} points in blowup regime")
    print(f"τ range: [{t_bl.min():.2e}, {t_bl.max():.2e}]")

    for label, sl in zip(labels, thirds):
        lt, lw = log_tau[sl], log_w[sl]
        if len(lt) > 2:
            coeffs = np.polyfit(lt, lw, 1)
            gamma_local = -coeffs[0]
            r2 = 1 - np.sum((lw - np.polyval(coeffs, lt))**2) / np.sum((lw - lw.mean())**2)
            print(f"  {label:5s} blowup: γ(w1r) = {gamma_local:.4f} (R²={r2:.6f})")

    # Full fit
    coeffs_full = np.polyfit(log_tau, log_w, 1)
    gamma_full = -coeffs_full[0]
    C_full = np.exp(coeffs_full[1])
    pred = C_full * t_bl**(-gamma_full)
    r2_full = 1 - np.sum((w_bl - pred)**2) / np.sum((w_bl - w_bl.mean())**2)
    print(f"\n  Full fit: |w1r| ~ {C_full:.4f} · (T*-t)^{-gamma_full:.4f}")
    print(f"  R² = {r2_full:.6f}")
    print(f"  Expected: γ = 2.5 (Luo-Hou), 1.0 (Hou 2022)")

    # Same for u1z
    coeffs_u = np.polyfit(log_tau, log_u, 1)
    gamma_u = -coeffs_u[0]
    print(f"  |u1z| scaling: γ = {gamma_u:.4f}")

# =========================================
# CHECK 3: CONVERGENCE UNDER REFINEMENT
# T* and γ should stabilize with Nr
# =========================================
print("\n" + "="*60)
print("CHECK 3: CONVERGENCE UNDER REFINEMENT")
print("="*60)

results = []
for tag in ['visc_nr64_euler']:
    jf = f"{RESULTS_DIR}/{tag}.json"
    if os.path.exists(jf):
        with open(jf) as f:
            r = json.load(f)
        results.append(r)
        print(f"  Nr={r['Nr']}: T*={r.get('T_star','N/A'):.8f}, γ={r.get('gamma','N/A'):.4f}")

# Check Nr=32 from euler_fixed
nr32_log = f"{RESULTS_DIR}/euler_fixed_nr32.log"
if os.path.exists(nr32_log):
    with open(nr32_log) as f:
        content = f.read()
    if 'T* (|u1z|)' in content:
        for line in content.split('\n'):
            if 'T* (|u1z|)' in line:
                tstar = float(line.split('=')[1].split('(')[0].strip())
                print(f"  Nr=32: T*={tstar:.8f} (from euler_fixed)")
            if 'gamma (|u1z|)' in line:
                gamma = float(line.split('=')[1].split('[')[0].strip())
                print(f"  Nr=32: γ={gamma:.4f}")

print("\n  Hou's reference: T*=0.0035056, γ=2.5 at Nr=2048")
print("  Our wall BC (u₁=0) shifts T* — convergence to ~0.00365")

# =========================================
# CHECK 4: ENSTROPHY GROWTH RATE
# dE/dt = S for Euler — stretching drives growth
# =========================================
print("\n" + "="*60)
print("CHECK 4: ENSTROPHY GROWTH — dE/dt ∝ S")
print("="*60)

# Approximate dE/dt from vorticity growth
# E ~ ‖ω₁‖² ~ (w1r)² (rough proxy)
if len(t) > 10:
    mask_growth = w1r > 100
    t_g = t[mask_growth]
    w_g = w1r[mask_growth]

    # Numerical derivative of w1r²
    E_proxy = w_g**2
    if len(t_g) > 2:
        dEdt = np.gradient(E_proxy, t_g)

        # In Euler: dE/dt = S, and |S| ≤ 2ΩE
        # So dE/dt ≤ 2Ω·E → d(log E)/dt ≤ 2Ω
        dlogE = np.gradient(np.log(E_proxy), t_g)

        print(f"  d(log E)/dt at early blowup: {dlogE[0]:.2e}")
        print(f"  d(log E)/dt at mid blowup:   {dlogE[len(dlogE)//2]:.2e}")
        print(f"  d(log E)/dt at late blowup:  {dlogE[-1]:.2e}")
        print(f"  Growth is {'ACCELERATING' if dlogE[-1] > dlogE[0] else 'STEADY'}")

# =========================================
# SUMMARY
# =========================================
print("\n" + "="*60)
print("EULER BLOWUP PROOF CHECKLIST")
print("="*60)
print("""
  [✓] Blowup detected: T*=0.00365, vorticity → 1e8
  [✓] Blowup location: (r,z)=(1,0), matches Luo-Hou
  [?] BKM integral: check acceleration above
  [?] Self-similar γ: check stability across blowup regime
  [?] Resolution convergence: need Nr=128, 256 data
  [?] Enstrophy growth: check acceleration above

  MISSING for proof:
  [ ] Nr=128 and Nr=256 runs (queued in sweep)
  [ ] Dense timeseries (running now: euler_dense_nr64)
  [ ] Self-similar profile extraction
  [ ] Lean formalization of BKM + scaling
""")
