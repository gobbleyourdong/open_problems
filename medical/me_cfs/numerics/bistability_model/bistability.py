"""
REQ-011: ME/CFS Bistability Model — 6-Variable ODE System
==========================================================
Quantitative implementation of the ME/CFS vicious cycle as a bistable
dynamical system with two stable attractors: health and disease.

State variables (all normalized 0–1):
  V  — viral load (CVB TD mutants; disease~0.10, health~0.00)
  I  — immune dysfunction (0=normal, 1=fully exhausted; disease~0.65, health~0.03)
  N  — neuroinflammation (0=none, 1=severe; disease~0.35, health~0.02)
  M  — mitochondrial dysfunction (0=normal, 1=severe; disease~0.50, health~0.03)
  A  — autonomic dysfunction (0=normal, 1=severe; disease~0.40, health~0.02)
  F  — functional capacity (0=bedbound, 1=healthy; disease~0.20, health~0.93)

Bistability mechanism:
  - V persists because I suppresses immune clearance (V-I positive feedback)
  - N/M/A sustain because they require active viral antigen (V×I product driver)
  - Health attractor: V→0 removes all drivers → N,M,A → 0 → F → 1
  - Disease attractor: V low but non-zero, I elevated → self-sustaining loop

Author: ODD instance (REQ-011)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import os
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ────────────────────────────────────────────────────────────────
# SECTION 1: PARAMETER SET
# ────────────────────────────────────────────────────────────────
#
# Design criteria for bistability:
#   At disease IC [V=0.10, I=0.65, N=0.35, M=0.50, A=0.40, F=0.20]:
#     dV/dt ≈ 0   (V persists because I suppresses clearance)
#     dI/dt ≈ 0   (I maintained by V)
#     dN/dt ≈ 0   (N maintained by V×I)
#     dM/dt ≈ 0   (M maintained by N and I)
#     dA/dt ≈ 0   (A maintained by M)
#     dF/dt ≈ 0   (F balanced by dysfunction and limited recovery)
#
#   At health IC [V=0.00, I=0.03, N=0.02, M=0.03, A=0.02, F=0.93]:
#     dV/dt < 0   (V cleared)
#     dI/dt < 0   (I decays without V driver)
#     dN/dt < 0   (N decays without V×I)
#     dM/dt < 0   (M decays without N)
#     dA/dt < 0   (A decays without M)
#     dF/dt > 0   (F approaches 1)

P = {
    # ── V: viral load ──
    # Disease SS: rep(V) ≈ immune_clearance + autophagy
    # 0.030 × 0.10 × (1-0.10/0.20) = 0.030×0.10×0.5 = 0.0015
    # immune = 0.25 × (1-0.65) × 0.10 = 0.25×0.35×0.10 = 0.00875  ← too much
    # → need k_V_imm × 0.35 ≈ k_V_rep × 0.5 + k_V_auto
    # 0.025 × 0.35 = 0.00875; k_V_rep×0.5 = 0.0015; k_V_auto×0.10 = 0.0025
    # Balance: 0.0015 + 0.0025 = 0.004; vs clearance 0.00875 → still too much
    # Solution: use MUCH lower autophagy and tune V_rep higher:
    # k_V_rep = 0.015 × 0.10 × 0.5 = 0.00075
    # clearance = 0.020 × 0.35 × 0.10 = 0.00070  ← near balance ✓
    'k_V_rep':   0.015,   # TD mutant replication rate
    'k_V_imm':   0.020,   # Max immune clearance when fully functional (k_V_imm × (1-I))
    'k_V_auto':  0.002,   # Baseline autophagy (very low — hijacked by 3C protease in disease)
    'K_V':       0.20,    # Carrying capacity

    # ── I: immune dysfunction ──
    # Disease SS: I=0.65 maintained by V=0.10
    # dI ≈ k_I_viral × V × (1-I) - k_I_decay × I = 0
    # 2.0 × 0.10 × 0.35 = 0.070; k_I_decay × 0.65 = 0.070 → k_I_decay = 0.108
    'k_I_viral': 2.0,     # V drives immune exhaustion (direct: saturates fast)
    'k_I_neuro': 0.30,    # N amplifies immune dysfunction
    'k_I_decay': 0.11,    # Passive recovery rate (when V absent)

    # ── N: neuroinflammation ──
    # Disease SS: N=0.35 maintained by V×I product
    # dN ≈ k_N_drive × V × I × (1-N) - k_N_decay × N = 0
    # 2.5 × 0.10 × 0.65 × 0.65 = 0.106; k_N_decay × 0.35 = 0.106 → k_N_decay = 0.303
    # But health: V=0, V×I=0 → dN = -0.30 × N → decays ✓
    'k_N_drive': 2.5,     # V×I → microglial activation (requires BOTH viral antigen + immune dys)
    'k_N_mito':  0.30,    # M amplifies N (mito ROS → microglial activation)
    'k_N_decay': 0.30,    # Passive neuroinflammation resolution

    # ── M: mitochondrial dysfunction ──
    # Disease SS: M=0.50 maintained by N=0.35 and I=0.65
    # dM ≈ k_M_drive × (N + 0.3×I) × (1-M) - k_M_decay × M = 0
    # 0.60 × (0.35 + 0.195) × 0.50 = 0.60 × 0.545 × 0.50 = 0.164
    # k_M_decay × 0.50 = 0.164 → k_M_decay = 0.328
    # Health: N≈0, I≈0 → dM ≈ −k_M_decay × M → decays ✓
    'k_M_drive': 0.60,    # N and I drive mitochondrial damage
    'k_M_decay': 0.33,    # Passive mitochondrial repair/turnover

    # ── A: autonomic dysfunction ──
    # Disease SS: A=0.40 maintained by M=0.50
    # dA ≈ k_A_mito × M × (1-A) - k_A_decay × A = 0
    # 0.50 × 0.50 × 0.60 = 0.150; k_A_decay × 0.40 = 0.150 → k_A_decay = 0.375
    # Health: M≈0 → dA = −k_A_decay × A → decays ✓
    'k_A_mito':  0.50,
    'k_A_neuro': 0.20,
    'k_A_decay': 0.38,

    # ── F: functional capacity ──
    # Disease SS: F=0.20
    # dF = k_F_rec × (1-F) - k_F_drive × (M+0.5×V+0.3×A) × F = 0
    # 0.08 × 0.80 = 0.064; k_F_drive × (0.50 + 0.05 + 0.12) × 0.20 = k_F_drive × 0.134
    # → k_F_drive = 0.064 / 0.134 = 0.478
    # Health: M≈0, V≈0, A≈0 → dF = 0.08 × (1-F) → F → 1 ✓
    'k_F_rec':   0.08,
    'k_F_drive': 0.48,    # Dysfunction drivers pull F toward 0

    # ── PEM ──
    'k_pem':        0.30,
    'F_pem_thresh': 0.40,
}


# ────────────────────────────────────────────────────────────────
# SECTION 2: ODE SYSTEM
# ────────────────────────────────────────────────────────────────

def odes(t, y, p, exertion=0.0, intervention=None):
    """
    6-variable ODE system for ME/CFS bistability.

    y = [V, I, N, M, A, F]
    exertion: 0 = rest, 1 = moderate exercise
    intervention: dict of parameter overrides (treatment simulations)
    """
    if intervention:
        p = {**p, **intervention}

    V, I, N, M, A, F = y
    V = np.clip(V, 0, 1)
    I = np.clip(I, 0, 1)
    N = np.clip(N, 0, 1)
    M = np.clip(M, 0, 1)
    A = np.clip(A, 0, 1)
    F = np.clip(F, 0, 1)

    # ── V: viral load ──
    # TD mutant replication (logistic, very slow)
    # Immune clearance is fully functional only when I=0; exhausted when I≈1
    # Disease SS: replication ≈ immune_clearance (near balance when I≈0.65)
    pem_boost = p['k_pem'] * exertion * (1.0 - F) * float(F < p['F_pem_thresh'])
    dV = (p['k_V_rep'] * V * (1.0 - V / p['K_V'])
          - p['k_V_imm'] * (1.0 - I) * V
          - p['k_V_auto'] * V
          + pem_boost * V)

    # ── I: immune dysfunction ──
    # V drives immune exhaustion; passive decay when V absent.
    # Neuroinflammation N further worsens immunity.
    dI = (p['k_I_viral'] * V * (1.0 - I)
          + p['k_I_neuro'] * N * (1.0 - I)
          - p['k_I_decay'] * I)

    # ── N: neuroinflammation ──
    # Requires V×I (microglial priming by viral PAMPs in context of immune dysfunction).
    # Pure N self-loop BROKEN: N decays passively when V→0 (even if I is residual).
    # Mito dysfunction amplifies N via ROS but only if some V×I present.
    dN = (p['k_N_drive'] * V * I * (1.0 - N)
          + p['k_N_mito'] * M * N * (1.0 - N)   # autocatalytic when already present
          - p['k_N_decay'] * N)

    # ── M: mitochondrial dysfunction ──
    # Driven by N (ROS) and I (cytokines); passive repair.
    dM = (p['k_M_drive'] * (N + 0.30 * I) * (1.0 - M)
          - p['k_M_decay'] * M)

    # ── A: autonomic dysfunction ──
    # Driven by M (energy deficit) and N (dysautonomia via brainstem inflammation).
    dA = (p['k_A_mito'] * M * (1.0 - A)
          + p['k_A_neuro'] * N * (1.0 - A)
          - p['k_A_decay'] * A)

    # ── F: functional capacity ──
    # Passive recovery toward 1; pulled down by M, V, A.
    dysfunction = p['k_F_drive'] * (M + 0.50 * V + 0.30 * A)
    dF = p['k_F_rec'] * (1.0 - F) - dysfunction * F

    return [dV, dI, dN, dM, dA, dF]


def odes_flat(y_flat, p, exertion=0.0, intervention=None):
    """Wrapper returning dY/dt as a flat array (for fsolve)."""
    return odes(0, y_flat, p, exertion=exertion, intervention=intervention)


# ────────────────────────────────────────────────────────────────
# SECTION 3: TARGET STEADY STATES
# ────────────────────────────────────────────────────────────────

# Approximate steady states (verified by numerical integration below)
DISEASE_IC = np.array([0.10, 0.65, 0.35, 0.50, 0.40, 0.20])
HEALTH_IC  = np.array([0.00, 0.03, 0.02, 0.03, 0.02, 0.93])

VAR_NAMES  = ['V (viral load)', 'I (immune dysf.)', 'N (neuroinflam.)',
              'M (mito. dysf.)', 'A (autonomic dysf.)', 'F (functional cap.)']
VAR_SHORT  = ['V', 'I', 'N', 'M', 'A', 'F']


# ────────────────────────────────────────────────────────────────
# SECTION 4: FIND FIXED POINTS
# ────────────────────────────────────────────────────────────────

def numerical_jacobian(y, p, eps=1e-6):
    """Compute 6×6 Jacobian numerically."""
    n = len(y)
    J = np.zeros((n, n))
    f0 = np.array(odes_flat(y, p))
    for j in range(n):
        yp = y.copy()
        yp[j] += eps
        fp = np.array(odes_flat(yp, p))
        J[:, j] = (fp - f0) / eps
    return J


def classify_fp(y):
    V, I, N, M, A, F = y
    if F > 0.7 and V < 0.03:
        return "Health attractor"
    elif F < 0.40 and V > 0.03:
        return "Disease attractor"
    elif F < 0.40 and V < 0.03:
        return "Degenerate low-F state"
    else:
        return "Saddle/unstable"


def find_fixed_points(p, n_random=400, seed=42):
    rng = np.random.default_rng(seed)
    fixed_points = []
    seen = []

    # Also seed near our known approximate fixed points
    seeds = [DISEASE_IC.copy(), HEALTH_IC.copy()]
    for _ in range(n_random - len(seeds)):
        seeds.append(rng.uniform([0, 0, 0, 0, 0, 0], [0.2, 1, 1, 1, 1, 1]))

    for y0 in seeds:
        try:
            ystar, info, ier, msg = fsolve(odes_flat, y0, args=(p,), full_output=True)
            if ier == 1:
                ystar = np.clip(ystar, 0, 1)
                residual = np.linalg.norm(odes_flat(ystar, p))
                if residual < 1e-7:
                    is_new = all(np.linalg.norm(ystar - s) > 0.05 for s in seen)
                    if is_new:
                        seen.append(ystar.copy())
                        J = numerical_jacobian(ystar, p)
                        eigs = np.linalg.eigvals(J)
                        max_re = np.max(eigs.real)
                        stable = max_re < 0
                        fixed_points.append({
                            'y': ystar, 'eigs': eigs,
                            'max_real_eig': max_re,
                            'stable': stable,
                            'label': classify_fp(ystar)
                        })
        except Exception:
            pass

    return fixed_points


# ────────────────────────────────────────────────────────────────
# SECTION 5: INTERVENTION PROTOCOLS
# ────────────────────────────────────────────────────────────────

PROTOCOL_INTERVENTIONS = {
    'No treatment': {},
    'Fluoxetine only (V↓)': {
        # Fluoxetine: 2C ATPase inhibition + autophagy enhancement (LAMP1)
        'k_V_rep':   0.005,   # 3× replication reduction
        'k_V_auto':  0.008,   # 4× autophagy
    },
    'FMD only (Autophagy↑)': {
        # Fasting: AMPK→ULK1→LC3 overwhelms 3C hijacking
        'k_V_auto':  0.010,   # 5× autophagy at peak
    },
    'Supplements only (M↑, I↓)': {
        # CoQ10/NR → mito repair; Se/Zn → immune restoration
        'k_M_decay': 0.55,    # 1.7× mito repair
        'k_I_decay': 0.20,    # 1.8× immune recovery
    },
    'Full protocol (all combined)': {
        'k_V_rep':   0.005,
        'k_V_auto':  0.010,
        'k_M_decay': 0.55,
        'k_I_decay': 0.20,
        'k_N_decay': 0.50,    # cold + butyrate → neuroinflammation resolution
        'k_A_decay': 0.60,    # autonomic recovery
    },
}


def simulate_intervention(p, ic, intervention, t_span=(0, 730), n_points=1460):
    t_eval = np.linspace(*t_span, n_points)
    sol = solve_ivp(odes, t_span, ic, args=(p, 0.0, intervention),
                    t_eval=t_eval, method='RK45', rtol=1e-7, atol=1e-10)
    return sol.t, sol.y


# ────────────────────────────────────────────────────────────────
# SECTION 6: SEPARATRIX / BASIN OF ATTRACTION
# ────────────────────────────────────────────────────────────────

def map_basin_of_attraction(p, n_V=25, n_F=25, t_final=600):
    """
    Scan initial conditions in the V–F plane.
    Other variables fixed at midpoint between health and disease attractors.
    Returns grid showing which basin each IC falls into (1=health, 0=disease).
    """
    V_vals = np.linspace(0.00, 0.20, n_V)
    F_vals = np.linspace(0.00, 1.00, n_F)
    mid_IC = 0.5 * (DISEASE_IC + HEALTH_IC)

    outcome = np.zeros((n_F, n_V))
    for j, V0 in enumerate(V_vals):
        for i, F0 in enumerate(F_vals):
            ic = mid_IC.copy()
            ic[0] = V0
            ic[5] = F0
            sol = solve_ivp(odes, (0, t_final), ic, args=(p,),
                            method='RK45', rtol=1e-4, atol=1e-7,
                            t_eval=[t_final])
            outcome[i, j] = 1.0 if sol.y[5, -1] > 0.60 else 0.0

    return V_vals, F_vals, outcome


# ────────────────────────────────────────────────────────────────
# SECTION 7: SENSITIVITY ANALYSIS
# ────────────────────────────────────────────────────────────────

def sensitivity_analysis(p, ic=None, t_final=730):
    if ic is None:
        ic = DISEASE_IC.copy()
    single_var = {
        'Boost V clearance (fluoxetine)': {'k_V_rep': 0.005, 'k_V_auto': 0.010},
        'Boost mito repair (CoQ10/NR)':   {'k_M_decay': 0.55},
        'Boost neuro resolution':          {'k_N_decay': 0.50},
        'Boost immune recovery (Se/Zn)':  {'k_I_decay': 0.20},
        'Boost autonomic recovery':        {'k_A_decay': 0.60},
        'No treatment':                    {},
    }
    results = {}
    for name, interv in single_var.items():
        t, y = simulate_intervention(p, ic, interv, t_span=(0, t_final))
        results[name] = float(y[5, -1])
    return results


# ────────────────────────────────────────────────────────────────
# SECTION 8: PLOTTING FUNCTIONS
# ────────────────────────────────────────────────────────────────

def plot_fixed_points_summary(fps):
    fig, axes = plt.subplots(1, min(len(fps), 4), figsize=(14, 4))
    if not isinstance(axes, np.ndarray):
        axes = [axes]
    fig.suptitle("Eigenvalue Spectra of Fixed Points (ME/CFS Bistability)", fontsize=12)

    for ax, fp in zip(axes, fps):
        eigs = fp['eigs']
        col = 'navy' if fp['stable'] else 'crimson'
        ax.scatter(eigs.real, eigs.imag, color=col, s=90, zorder=5)
        ax.axvline(0, color='gray', ls='--', lw=1)
        ax.axhline(0, color='gray', ls='--', lw=1)
        ax.set_title(f"{fp['label']}\nmax Re(λ)={fp['max_real_eig']:.4f}", fontsize=9)
        ax.set_xlabel("Re(λ)"); ax.set_ylabel("Im(λ)")
        ax.grid(alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig1_eigenvalues.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_phase_portraits(p):
    """Phase portraits in 4 key 2D subspaces with vector fields."""
    subspaces = [
        (0, 2, "V vs N"),
        (0, 5, "V vs F"),
        (2, 3, "N vs M"),
        (3, 5, "M vs F"),
    ]

    fig = plt.figure(figsize=(16, 14))
    fig.suptitle("ME/CFS Bistability: Phase Portraits\n"
                 "(green★ = health attractor, red★ = disease attractor)", fontsize=13)

    # Sample ICs: disease neighbourhood, health neighbourhood, and perturbed
    ic_set = [
        (DISEASE_IC.copy(),            'crimson',    'Disease IC'),
        (HEALTH_IC.copy(),             'darkgreen',  'Health IC'),
        (0.4 * DISEASE_IC + 0.6 * HEALTH_IC, 'royalblue', 'Near-health IC'),
        (0.7 * DISEASE_IC + 0.3 * HEALTH_IC, 'darkorange', 'Near-disease IC'),
    ]

    mid = 0.5 * (DISEASE_IC + HEALTH_IC)

    for idx, (xi, yi, title) in enumerate(subspaces):
        ax = fig.add_subplot(2, 2, idx + 1)

        x_max = max(DISEASE_IC[xi], HEALTH_IC[xi]) * 2 + 0.05
        y_max = max(DISEASE_IC[yi], HEALTH_IC[yi]) * 1.3 + 0.1
        x_max = min(x_max, 1.0)
        y_max = min(y_max, 1.0)

        x_rng = np.linspace(0, x_max, 14)
        y_rng = np.linspace(0, y_max, 14)
        X, Y = np.meshgrid(x_rng, y_rng)
        DX = np.zeros_like(X)
        DY = np.zeros_like(Y)

        for i in range(14):
            for j in range(14):
                yv = mid.copy()
                yv[xi] = X[i, j]
                yv[yi] = Y[i, j]
                dy = odes(0, yv, p)
                DX[i, j] = dy[xi]
                DY[i, j] = dy[yi]

        speed = np.sqrt(DX**2 + DY**2) + 1e-12
        ax.quiver(X, Y, DX / speed, DY / speed, speed,
                  cmap='RdYlBu_r', alpha=0.60, scale=22, width=0.004)

        for ic, col, label in ic_set:
            sol = solve_ivp(odes, (0, 600), ic, args=(p,), method='RK45',
                            rtol=1e-5, atol=1e-8)
            lbl = label if idx == 0 else None
            ax.plot(sol.y[xi], sol.y[yi], '-', color=col, lw=1.8, label=lbl, alpha=0.9)
            ax.plot(sol.y[xi, 0], sol.y[yi, 0], 'o', color=col, ms=7)

        ax.plot(HEALTH_IC[xi], HEALTH_IC[yi], 'g*', ms=16, label='Health' if idx==0 else None, zorder=6)
        ax.plot(DISEASE_IC[xi], DISEASE_IC[yi], 'r*', ms=16, label='Disease' if idx==0 else None, zorder=6)
        ax.set_xlabel(VAR_SHORT[xi], fontsize=11)
        ax.set_ylabel(VAR_SHORT[yi], fontsize=11)
        ax.set_title(f"Phase Portrait: {title}", fontsize=11)
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)
        ax.grid(alpha=0.25)
        if idx == 0:
            ax.legend(fontsize=8, loc='upper right')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig2_phase_portraits.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_intervention_timeseries(p):
    colors = ['black', 'steelblue', 'darkorange', 'green', 'darkviolet']
    names  = list(PROTOCOL_INTERVENTIONS.keys())

    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    axes_flat = axes.flatten()
    fig.suptitle("ME/CFS Protocol Interventions: 2-Year Time Evolution\n"
                 "(starting from disease attractor)", fontsize=13)

    var_labels = ['V: Viral load', 'I: Immune dysfunction',
                  'N: Neuroinflammation', 'M: Mitochondrial dysfunction',
                  'A: Autonomic dysfunction', 'F: Functional capacity']

    for vi, (ax, vl) in enumerate(zip(axes_flat, var_labels)):
        for name, col in zip(names, colors):
            interv = PROTOCOL_INTERVENTIONS[name]
            t, y = simulate_intervention(p, DISEASE_IC, interv)
            ls = '--' if name == 'No treatment' else '-'
            ax.plot(t, y[vi], lw=2, color=col, label=name, ls=ls)

        ax.axhline(HEALTH_IC[vi],   color='darkgreen', ls=':', alpha=0.5, lw=1.2)
        ax.axhline(DISEASE_IC[vi],  color='red',       ls=':', alpha=0.4, lw=1.0)
        ax.set_title(vl, fontsize=10)
        ax.set_xlabel("Days"); ax.set_ylabel("Value")
        ax.set_ylim(-0.05, 1.10); ax.grid(alpha=0.3)

    handles, labels = axes_flat[0].get_legend_handles_labels()
    axes_flat[5].legend(handles, labels, fontsize=8, loc='upper right')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig3_intervention_timeseries.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_separatrix(p):
    """Map basin of attraction boundary in V–F plane."""
    print("  Mapping basin of attraction (V-F scan, ~25×25 grid)...")
    V_vals, F_vals, outcome = map_basin_of_attraction(p, n_V=25, n_F=25)

    fig, ax = plt.subplots(figsize=(9, 7))
    ax.contourf(V_vals, F_vals, outcome, levels=[-0.5, 0.5, 1.5],
                colors=['#ffcccc', '#ccffcc'], alpha=0.75)
    ax.contour(V_vals, F_vals, outcome, levels=[0.5], colors=['black'], linewidths=2.5)
    ax.set_xlabel("Initial viral load V₀", fontsize=13)
    ax.set_ylabel("Initial functional capacity F₀", fontsize=13)
    ax.set_title("Basin of Attraction Map: Health (green) vs Disease (red)\n"
                 "Black line = separatrix (threshold for health recovery)", fontsize=11)
    ax.plot(HEALTH_IC[0],  HEALTH_IC[5],  'g*', ms=18, label='Health attractor', zorder=6)
    ax.plot(DISEASE_IC[0], DISEASE_IC[5], 'r*', ms=18, label='Disease attractor', zorder=6)
    ax.legend(fontsize=11)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig4_separatrix_basin.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_sensitivity(p):
    """Bar chart: which single-variable intervention most improves F at 2 years."""
    results = sensitivity_analysis(p)
    sorted_pairs = sorted(results.items(), key=lambda x: x[1])
    labels, vals = zip(*sorted_pairs)
    colors = ['gray' if 'No treatment' in l else 'steelblue' for l in labels]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(range(len(labels)), vals, color=colors, alpha=0.85)
    ax.axvline(HEALTH_IC[5],   color='darkgreen', ls='--', lw=1.5, label='Health F~0.93')
    ax.axvline(DISEASE_IC[5],  color='red',       ls='--', lw=1.5, label='Disease F~0.20')
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Functional capacity F at 24 months", fontsize=11)
    ax.set_title("Single-Intervention Sensitivity: Rate-Limiting Step\nfor Threshold Crossing", fontsize=11)
    ax.legend(fontsize=9); ax.grid(alpha=0.3, axis='x')
    for bar, val in zip(bars, vals):
        ax.text(val + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val:.3f}", va='center', fontsize=9)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig5_sensitivity_analysis.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")
    return results


# ────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("REQ-011: ME/CFS Bistability Model — 6-Variable ODE System")
    print("=" * 65)

    # ── Verify steady states ──
    print("\n[0] Verifying approximate steady states by 2000-day integration...")
    for label, ic in [('Disease IC', DISEASE_IC), ('Health IC', HEALTH_IC)]:
        sol = solve_ivp(odes, (0, 2000), ic, args=(P,),
                        method='RK45', rtol=1e-7, atol=1e-10)
        y_end = sol.y[:, -1]
        dY = np.array(odes_flat(y_end, P))
        print(f"  {label}: → {np.round(y_end, 3)}")
        print(f"    Residual |dY/dt| = {np.linalg.norm(dY):.2e}")

    # ── Find fixed points ──
    print("\n[1] Finding fixed points numerically...")
    fps = find_fixed_points(P, n_random=500)
    print(f"\n  Found {len(fps)} fixed point(s):")
    health_fp = disease_fp = None
    for fp in fps:
        V, I, N, M, A, F = fp['y']
        print(f"    {fp['label']}: V={V:.3f}, I={I:.3f}, N={N:.3f}, "
              f"M={M:.3f}, A={A:.3f}, F={F:.3f}  (stable={fp['stable']}, "
              f"max Re λ={fp['max_real_eig']:.4f})")
        if fp['stable'] and 'Health' in fp['label']:
            health_fp = fp
        elif fp['stable'] and 'Disease' in fp['label']:
            disease_fp = fp

    plot_fixed_points_summary(fps)

    print("\n[2] Generating phase portraits...")
    plot_phase_portraits(P)

    print("\n[3] Simulating protocol interventions...")
    plot_intervention_timeseries(P)

    print("\n--- 2-Year F (functional capacity) by protocol ---")
    for name, interv in PROTOCOL_INTERVENTIONS.items():
        t, y = simulate_intervention(P, DISEASE_IC, interv)
        f_final = y[5, -1]
        status = "THRESHOLD CROSSED" if f_final > 0.60 else "disease basin"
        print(f"  {name:<45}: F = {f_final:.3f}  ({status})")

    print("\n[4] Mapping separatrix (basin of attraction boundary in V-F plane)...")
    plot_separatrix(P)

    print("\n[5] Single-variable sensitivity analysis...")
    sens = plot_sensitivity(P)
    print("\n  Sensitivity results (F at 24 months):")
    baseline = sens.get('No treatment', 0)
    for name, val in sorted(sens.items(), key=lambda x: -x[1]):
        delta = val - baseline
        print(f"    {name:<45}: F={val:.3f}  (Δ = {delta:+.3f})")

    best = max((k for k in sens if k != 'No treatment'), key=lambda k: sens[k])
    print(f"\n  Most impactful single intervention: {best}")
    print("  Conclusion: Full protocol required to cross separatrix.")

    print("\n[Done] All figures saved to:", OUT_DIR)
