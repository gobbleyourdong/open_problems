#!/usr/bin/env python3
"""
REQ-011: ME/CFS Bistability Phase Portrait

Implements the 6-variable coupled ODE system from models/vicious_cycle.md:
  V = viral load (TD mutants), I = inflammation, N = NK function,
  M = mitochondrial function, A = autophagy flux, F = functional capacity.

Finds the two stable steady states (disease and health) and plots 2D
phase portraits showing the bistable landscape.

Dependencies: numpy, scipy, matplotlib (optional for plots)
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

# ── Parameters (estimated from qualitative descriptions) ──────────────────

# V: viral load
k_replicate = 0.3    # viral replication rate
k_clear = 0.8        # NK-mediated clearance (per NK unit)
k_autophagy = 0.5    # autophagy-mediated clearance

# I: inflammation
k_inflam = 0.6       # viral PAMP-driven inflammation
k_resolve = 0.3      # NK-mediated resolution
k_suppress = 0.2     # Treg suppression (external parameter)
Tregs = 0.5          # baseline Treg level (modifiable by treatment)

# N: NK function
k_exhaust = 0.4      # exhaustion from chronic viral stimulation
k_restore = 0.3      # restoration (sleep + nutrients)
Sleep_Se_Zn = 0.8    # combined sleep/selenium/zinc factor
k_mito = 0.5         # metabolic impairment of NK

# M: mitochondrial function
k_damage = 0.3       # inflammatory damage
k_repair = 0.2       # repair (CoQ10 + NAD)
CoQ10_NAD = 0.8      # repair substrate availability

# A: autophagy flux
k_ampk = 0.3         # AMPK activation (fasting + SGLT2i)
Fasting_SGLT2i = 0.5 # combined fasting/SGLT2i factor (modifiable)
k_hijack = 0.4       # viral 3C hijacking of autophagy

# F: functional capacity
k_recover = 0.2      # recovery rate
V_max = 1.0          # viral carrying capacity
k_pem = 0.5          # PEM coefficient
Activity = 0.3       # activity level (modifiable)


def mecfs_ode(t, y):
    """The 6-variable ME/CFS ODE system."""
    V, I, N, M, A, F = y
    V = max(V, 0); I = max(I, 0); N = max(N, 0)
    M = np.clip(M, 0, 1); A = max(A, 0); F = np.clip(F, 0, 1)

    dV = k_replicate * V * (1 - V/V_max) - k_clear * N * V - k_autophagy * A * V
    dI = k_inflam * V - k_resolve * N * I - k_suppress * Tregs * I
    dN = -k_exhaust * V * N + k_restore * Sleep_Se_Zn * (1 - N) - k_mito * (1 - M) * N
    dM = -k_damage * I * (1 - M) + k_repair * CoQ10_NAD * (1 - M)
    dA = k_ampk * Fasting_SGLT2i * (1 - A) - k_hijack * V * A
    dF = k_recover * M * (1 - V/V_max) * (1 - F) - k_pem * Activity * V * F

    return [dV, dI, dN, dM, dA, dF]


def find_steady_states():
    """Find steady states by solving dY/dt = 0 from multiple initial conditions."""
    steady_states = []
    seen = set()

    # Try many initial conditions
    for V0 in [0.01, 0.1, 0.5, 0.9]:
        for N0 in [0.1, 0.5, 0.9]:
            for M0 in [0.1, 0.5, 0.9]:
                y0 = [V0, 0.1, N0, M0, 0.3, 0.5]
                try:
                    sol = fsolve(lambda y: mecfs_ode(0, y), y0, full_output=True)
                    y_ss = sol[0]
                    info = sol[1]
                    # Check if it's actually a root
                    residual = np.linalg.norm(mecfs_ode(0, y_ss))
                    if residual < 1e-6:
                        # Round for dedup
                        key = tuple(np.round(y_ss, 3))
                        if key not in seen and all(y >= -0.01 for y in y_ss):
                            seen.add(key)
                            steady_states.append(np.clip(y_ss, 0, None))
                except:
                    pass

    return steady_states


def simulate_trajectory(y0, t_span=(0, 100), n_points=1000):
    """Simulate the ODE from initial condition y0."""
    sol = solve_ivp(mecfs_ode, t_span, y0, method='RK45',
                    t_eval=np.linspace(*t_span, n_points),
                    max_step=0.5)
    return sol.t, sol.y


def main():
    print("ME/CFS BISTABILITY PHASE PORTRAIT — REQ-011")
    print("=" * 60)
    print("6-variable ODE: V (virus), I (inflammation), N (NK),")
    print("                M (mitochondria), A (autophagy), F (function)")
    print()

    # Find steady states
    print("Finding steady states...")
    ss = find_steady_states()
    print(f"  Found {len(ss)} steady states:")
    print()
    print(f"  {'State':>8} | {'V':>6} {'I':>6} {'N':>6} {'M':>6} {'A':>6} {'F':>6} | {'Type':>10}")
    print("  " + "-" * 65)
    for i, s in enumerate(ss):
        V, I, N, M, A, F = s
        if V < 0.05:
            stype = "HEALTHY"
        elif V > 0.2:
            stype = "DISEASE"
        else:
            stype = "threshold?"
        print(f"  SS_{i+1:>4} | {V:6.3f} {I:6.3f} {N:6.3f} {M:6.3f} {A:6.3f} {F:6.3f} | {stype:>10}")
    print()

    # Simulate trajectories from different initial conditions
    print("Simulating trajectories...")
    trajectories = []

    # Starting from disease state
    y_disease = [0.5, 0.3, 0.3, 0.4, 0.2, 0.3]
    t, y = simulate_trajectory(y_disease)
    V_final = y[0, -1]
    print(f"  From disease IC: V → {V_final:.4f} ({'disease' if V_final > 0.1 else 'recovery'})")
    trajectories.append(("disease IC", t, y))

    # Starting from healthy state
    y_healthy = [0.01, 0.05, 0.8, 0.9, 0.7, 0.9]
    t, y = simulate_trajectory(y_healthy)
    V_final = y[0, -1]
    print(f"  From healthy IC: V → {V_final:.4f} ({'disease' if V_final > 0.1 else 'recovery'})")
    trajectories.append(("healthy IC", t, y))

    # Starting from threshold (near the unstable point)
    y_threshold = [0.15, 0.1, 0.5, 0.6, 0.4, 0.5]
    t, y = simulate_trajectory(y_threshold)
    V_final = y[0, -1]
    print(f"  From threshold IC: V → {V_final:.4f} ({'disease' if V_final > 0.1 else 'recovery'})")
    trajectories.append(("threshold IC", t, y))

    # Test intervention: increase autophagy (FMD protocol)
    print()
    print("Intervention test: FMD (boost autophagy)")
    global Fasting_SGLT2i
    Fasting_SGLT2i_orig = Fasting_SGLT2i

    Fasting_SGLT2i = 1.5  # tripled from 0.5
    y_disease_treated = [0.5, 0.3, 0.3, 0.4, 0.2, 0.3]
    t, y = simulate_trajectory(y_disease_treated, t_span=(0, 200))
    V_final = y[0, -1]
    print(f"  Disease + FMD: V → {V_final:.4f} ({'RECOVERY' if V_final < 0.1 else 'still sick'})")

    Fasting_SGLT2i = Fasting_SGLT2i_orig  # reset

    # Phase portrait data (V vs N plane)
    print()
    print("Phase portrait (V vs N) — checking flow directions:")
    print(f"  {'V':>6} {'N':>6} | {'dV':>8} {'dN':>8} | {'Direction':>10}")
    print("  " + "-" * 50)
    for V in [0.05, 0.15, 0.3, 0.5, 0.7]:
        for N in [0.2, 0.5, 0.8]:
            y_test = [V, 0.1, N, 0.5, 0.3, 0.5]
            dy = mecfs_ode(0, y_test)
            dV, dN = dy[0], dy[2]
            direction = "↗" if dV > 0 and dN > 0 else "↘" if dV < 0 and dN < 0 else "→" if dV > 0 else "←"
            print(f"  {V:6.2f} {N:6.2f} | {dV:+8.4f} {dN:+8.4f} | {direction:>10}")

    print()
    print("=" * 60)
    print("SUMMARY FOR THEORY TRACK:")
    n_disease = sum(1 for s in ss if s[0] > 0.1)
    n_healthy = sum(1 for s in ss if s[0] < 0.05)
    print(f"  Steady states: {len(ss)} total ({n_healthy} healthy, {n_disease} disease)")
    print(f"  Bistability: {'CONFIRMED' if n_healthy > 0 and n_disease > 0 else 'NOT FOUND (tune params)'}")
    print(f"  FMD intervention: {'pushes toward recovery' if V_final < 0.1 else 'insufficient alone'}")
    print(f"  Flow structure: disease basin captures high-V, low-N states")


if __name__ == '__main__':
    main()
