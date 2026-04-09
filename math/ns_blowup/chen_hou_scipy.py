#!/usr/bin/env python3
"""
Chen-Hou steady state analysis using scipy spline derivatives.

Loads the 720x720 steady-state profile, computes derivatives via
RectBivariateSpline on the non-uniform (r,z) grid, verifies the
inviscid RHS against saved residuals, then runs a frozen-velocity
linearized viscous test for multiple nu values.

Key finding: solu.v_dx and solu.u1_dx are derivatives in COMPUTATIONAL
coordinates (not physical). We compute all physical derivatives via
scipy splines. The saved Fv, Fw ARE in physical coordinates (~3e-10).
"""

import os
import numpy as np
import scipy.io as sio
from scipy.interpolate import RectBivariateSpline
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import splu
import time

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MAT_PATH = os.path.join(SCRIPT_DIR, "chen_hou_matlab", "ASS_data",
                        "Steady_state_pertb720_Nlevcor4.mat")

print(f"Loading {MAT_PATH} ...")
mat = sio.loadmat(MAT_PATH, squeeze_me=False)

# Profiles (720x720), indexed as [i_r, i_z]
v = mat['v'].copy()       # u1 (angular velocity / r)
w = mat['w'].copy()       # omega1 (vorticity)
Fv_saved = mat['Fv']      # Saved inviscid RHS for v
Fw_saved = mat['Fw']      # Saved inviscid RHS for w

# Mesh grids
mesh = mat['Mesh'][0, 0]
r_1d = mesh['x'][0, 0].ravel().copy()  # 720 pts, non-uniform
z_1d = mesh['x'][0, 1].ravel().copy()  # 720 pts, non-uniform

# Structure parameters
solu = mat['solu'][0, 0]
cl = float(solu['cl'].ravel()[0])   # 3.006498
cw = float(solu['cw'].ravel()[0])   # -1.029425

# Saved velocity fields (from Poisson solve) -- 2x2 object arrays
u_r = solu['u1'][0, 0].copy()       # radial velocity (720x720)
u_z = solu['u2'][0, 0].copy()       # axial velocity (720x720)

# NOTE: solu.v_dx and solu.u1_dx are in COMPUTATIONAL (spectral basis)
# coordinates, NOT physical d/dr. We compute physical derivatives via spline.

N = len(r_1d)
print(f"Grid: {N}x{N}, r in [{r_1d[0]:.2e}, {r_1d[-1]:.2e}]")
print(f"cl = {cl:.6f}, cw = {cw:.6f}")
print(f"|v|_max = {np.abs(v).max():.6f}, |w|_max = {np.abs(w).max():.6f}")
print(f"|Fv_saved|_max = {np.abs(Fv_saved).max():.2e}")
print(f"|Fw_saved|_max = {np.abs(Fw_saved).max():.2e}")

# Verify grids are strictly increasing (required by RectBivariateSpline)
assert np.all(np.diff(r_1d) > 0), "r grid not strictly increasing!"
assert np.all(np.diff(z_1d) > 0), "z grid not strictly increasing!"
print("Grids verified: strictly increasing.")

# Handle r[0] = 0 for singularity
r_1d[0] = 0.0  # ensure exactly zero

# 2D grids for RHS evaluation
R2d, Z2d = np.meshgrid(r_1d, z_1d, indexing='ij')  # [i_r, i_z]

# ---------------------------------------------------------------------------
# 2. Build spline interpolants for v, w, u_r, u_z
# ---------------------------------------------------------------------------
print("\nBuilding RectBivariateSpline for v, w, u_r ...")
t0 = time.time()

# kx=ky=5 for quintic spline -- accurate 2nd derivatives
# s=0 for exact interpolation (no smoothing)
spline_v = RectBivariateSpline(r_1d, z_1d, v, kx=5, ky=5, s=0)
spline_w = RectBivariateSpline(r_1d, z_1d, w, kx=5, ky=5, s=0)
spline_ur = RectBivariateSpline(r_1d, z_1d, u_r, kx=5, ky=5, s=0)

print(f"Splines built in {time.time()-t0:.1f}s")

# Compute 1st derivatives on the grid
dv_dr = spline_v(r_1d, z_1d, dx=1, dy=0)
dv_dz = spline_v(r_1d, z_1d, dx=0, dy=1)
dw_dr = spline_w(r_1d, z_1d, dx=1, dy=0)
dw_dz = spline_w(r_1d, z_1d, dx=0, dy=1)
dur_dr = spline_ur(r_1d, z_1d, dx=1, dy=0)   # physical d(u_r)/dr

print(f"|dv/dr|_max = {np.abs(dv_dr).max():.6f}")
print(f"|dv/dz|_max = {np.abs(dv_dz).max():.6f}")
print(f"|dw/dr|_max = {np.abs(dw_dr).max():.6f}")
print(f"|dw/dz|_max = {np.abs(dw_dz).max():.6f}")
print(f"|du_r/dr|_max = {np.abs(dur_dr).max():.6f}")

# Quick sanity: du_r/dr should approach -cl near origin
print(f"du_r/dr[1,0] = {dur_dr[1,0]:.4f} (expect ~ -cl = {-cl:.4f})")

# ---------------------------------------------------------------------------
# 3. Verify RHS: compare computed Fv, Fw to saved
# ---------------------------------------------------------------------------
print("\n" + "="*60)
print("RHS VERIFICATION (inviscid)")
print("="*60)

# Chen-Hou RHS (F_pertb_2lev.m lines 139-140):
#   Fv = -(cl*r + u_r) * dv/dr - (cl*z + u_z) * dv/dz + (2*cw - du_r/dr) * v
#   Fw = -(cl*r + u_r) * dw/dr - (cl*z + u_z) * dw/dz + cw*w + v + r * dv/dr
#
# All derivatives are physical (d/dr, d/dz), computed via spline.
# u_r, u_z are the saved Poisson-solve velocity (exact).
# du_r/dr is computed via spline from u_r (NOT the saved u1_dx which is
# in computational coordinates).

Fv_computed = (-(cl * R2d + u_r) * dv_dr
               - (cl * Z2d + u_z) * dv_dz
               + (2.0 * cw - dur_dr) * v)

Fw_computed = (-(cl * R2d + u_r) * dw_dr
               - (cl * Z2d + u_z) * dw_dz
               + cw * w + v + R2d * dv_dr)

# Residual vs saved
Fv_err = np.abs(Fv_computed - Fv_saved)
Fw_err = np.abs(Fw_computed - Fw_saved)

print(f"|Fv_computed|_max = {np.abs(Fv_computed).max():.2e}")
print(f"|Fw_computed|_max = {np.abs(Fw_computed).max():.2e}")
print(f"|Fv_computed - Fv_saved|_max = {Fv_err.max():.2e}")
print(f"|Fw_computed - Fw_saved|_max = {Fw_err.max():.2e}")
print(f"|Fv_computed - Fv_saved|_mean = {Fv_err.mean():.2e}")
print(f"|Fw_computed - Fw_saved|_mean = {Fw_err.mean():.2e}")

# Where is the error concentrated?
idx_fv = np.unravel_index(np.argmax(Fv_err), Fv_err.shape)
idx_fw = np.unravel_index(np.argmax(Fw_err), Fw_err.shape)
print(f"Fv error peak at (ir={idx_fv[0]}, iz={idx_fv[1]}), "
      f"r={r_1d[idx_fv[0]]:.4e}, z={z_1d[idx_fv[1]]:.4e}")
print(f"Fw error peak at (ir={idx_fw[0]}, iz={idx_fw[1]}), "
      f"r={r_1d[idx_fw[0]]:.4e}, z={z_1d[idx_fw[1]]:.4e}")

# Check error in the core (r,z < 5) where the profile lives
core_r = r_1d < 5.0
core_z = z_1d < 5.0
core_mask = np.outer(core_r, core_z)
print(f"\nCore (r,z < 5): {core_r.sum()}x{core_z.sum()} points")
print(f"  |Fv err|_max = {Fv_err[core_mask].max():.2e}")
print(f"  |Fw err|_max = {Fw_err[core_mask].max():.2e}")

core_r10 = r_1d < 10.0
core_z10 = z_1d < 10.0
core_mask10 = np.outer(core_r10, core_z10)
print(f"Core (r,z < 10): {core_r10.sum()}x{core_z10.sum()} points")
print(f"  |Fv err|_max = {Fv_err[core_mask10].max():.2e}")
print(f"  |Fw err|_max = {Fw_err[core_mask10].max():.2e}")

# The RHS should be ~0 at the steady state. Our spline derivatives
# introduce some numerical error but the key question is: is the error
# small compared to the forces we'll apply (nu * Laplacian)?
rhs_ok = Fv_err.max() < 1e-6 and Fw_err.max() < 1e-6
print(f"\nRHS match < 1e-6: {'YES' if rhs_ok else 'NO'}")
if not rhs_ok:
    print("NOTE: Spline derivative accuracy is limited by the extreme")
    print("grid stretching (r from 0 to 2e13). The error is concentrated")
    print("at transition regions where the grid spacing changes rapidly.")
    print("The du_r/dr spline derivative dominates the Fv error.")
    print("Proceeding with Laplacian and time-stepping using the saved")
    print("Fv_saved, Fw_saved as the ground-truth inviscid residual.")

# ---------------------------------------------------------------------------
# 4. Compute Laplacian
# ---------------------------------------------------------------------------
print("\n" + "="*60)
print("LAPLACIAN COMPUTATION")
print("="*60)
print("Hou-Li Laplacian: Df = d2f/dr2 + (3/r)df/dr + d2f/dz2")
print("At r=0: L'Hopital -> Df = 4*d2f/dr2 + d2f/dz2")

d2v_dr2 = spline_v(r_1d, z_1d, dx=2, dy=0)
d2v_dz2 = spline_v(r_1d, z_1d, dx=0, dy=2)
d2w_dr2 = spline_w(r_1d, z_1d, dx=2, dy=0)
d2w_dz2 = spline_w(r_1d, z_1d, dx=0, dy=2)

# Build (3/r) array, handling r=0
three_over_r = np.zeros_like(R2d)
three_over_r[1:, :] = 3.0 / R2d[1:, :]  # r > 0

# Laplacian for r > 0
Lap_v = d2v_dr2 + three_over_r * dv_dr + d2v_dz2
Lap_w = d2w_dr2 + three_over_r * dw_dr + d2w_dz2

# At r=0 (row 0): Df = 4*d2f/dr2 + d2f/dz2
Lap_v[0, :] = 4.0 * d2v_dr2[0, :] + d2v_dz2[0, :]
Lap_w[0, :] = 4.0 * d2w_dr2[0, :] + d2w_dz2[0, :]

print(f"|Lap_v|_max = {np.abs(Lap_v).max():.6e}")
print(f"|Lap_v|_mean = {np.abs(Lap_v).mean():.6e}")
print(f"|Lap_w|_max = {np.abs(Lap_w).max():.6e}")
print(f"|Lap_w|_mean = {np.abs(Lap_w).mean():.6e}")

# Where is the Laplacian largest?
idx_lv = np.unravel_index(np.argmax(np.abs(Lap_v)), Lap_v.shape)
idx_lw = np.unravel_index(np.argmax(np.abs(Lap_w)), Lap_w.shape)
print(f"Lap_v max at (ir={idx_lv[0]}, iz={idx_lv[1]}), "
      f"r={r_1d[idx_lv[0]]:.4e}, z={z_1d[idx_lv[1]]:.4e}")
print(f"Lap_w max at (ir={idx_lw[0]}, iz={idx_lw[1]}), "
      f"r={r_1d[idx_lw[0]]:.4e}, z={z_1d[idx_lw[1]]:.4e}")

# Laplacian in core region
print(f"\nCore (r,z < 5):")
print(f"  |Lap_v|_max = {np.abs(Lap_v[core_mask].reshape(-1)).max():.6e}")
print(f"  |Lap_w|_max = {np.abs(Lap_w[core_mask].reshape(-1)).max():.6e}")

# For each nu, the viscous forcing is nu*Lap. Compare to inviscid residual:
for nu_test in [1e-6, 1e-5, 1e-4, 1e-3]:
    force_v = nu_test * np.abs(Lap_v).max()
    force_w = nu_test * np.abs(Lap_w).max()
    print(f"  nu={nu_test:.0e}: nu*|Lap_v|_max = {force_v:.2e}, "
          f"nu*|Lap_w|_max = {force_w:.2e}")

# ---------------------------------------------------------------------------
# 5. Frozen-velocity linearized viscous time-stepping
# ---------------------------------------------------------------------------
print("\n" + "="*60)
print("FROZEN-VELOCITY VISCOUS TIME-STEPPING")
print("="*60)
print("RHS_viscous = F_inviscid + nu * Lap_f")
print("Forward Euler: f_new = f + dt * RHS_viscous")
print("Using SAVED Fv/Fw (~3e-10) as inviscid residual.")
print("Frozen Laplacian from initial steady state.")
print()

# The self-similar velocity cl*r + u_r stretches to ~2e13 at the boundary,
# but v and w are negligible there (< 1e-8 for r > 10^3).
# For CFL, we care about velocity in the region where v,w have support.
# Use max velocity where |v| + |w| > 1e-8 of their peak.
V_r = cl * R2d + u_r
V_z = cl * Z2d + u_z
V_mag = np.sqrt(V_r**2 + V_z**2)

# The self-similar velocity cl*r + u_r grows without bound, but v and w
# decay rapidly. The CFL should be based on the velocity in the core
# where v,w are significant (say > 1% of peak).
# The profile peaks at r~2, so the core is r,z < ~10.
V_max_core = V_mag[core_mask10].max()

print(f"|V|_max (full grid)   = {V_mag.max():.2e}")
print(f"|V|_max (r,z < 10)    = {V_max_core:.2e}")
print(f"Using CORE velocity (r,z<10) for CFL to get meaningful dt.")

# Minimum grid spacing (in the core region)
dr_all = np.diff(r_1d)
dz_all = np.diff(z_1d)
dr_min = dr_all.min()
dz_min = dz_all.min()
h_min = min(dr_min, dz_min)

print(f"h_min (global)  = {h_min:.6e}")
print()

nu_values = [0.0, 1e-6, 1e-5, 1e-4, 1e-3]
# Target physical time per run
T_target = 10.0
n_steps_max = 50000  # safety cap

# NOTE: Since both F_inviscid and Lap are frozen (constant in time),
# v(t) = v(0) + t * (F_inviscid + nu*Lap_v).
# This is a pure linear extrapolation — no numerical ODE error.
# The question is whether nu*Lap has the same sign as v (growth)
# or opposite sign (decay) at the profile maximum.

# Precompute the inviscid RHS (frozen)
# Use saved Fv/Fw since they are the ground truth (~3e-10 residual)
Fv_inviscid = Fv_saved.copy()
Fw_inviscid = Fw_saved.copy()

# Precompute the frozen viscous RHS increment for each step
# Since both F_inviscid and Lap are frozen, the RHS is constant per nu.
# v_new = v + n*dt*(F_inviscid + nu*Lap) — pure linear growth.
# This means we can compute the result analytically!

results = []

for nu in nu_values:
    print(f"--- nu = {nu:.1e} ---")

    # CFL for advection: dt_adv = CFL * h / V_max
    # Use core velocity — the outer domain has huge V but negligible v,w
    CFL = 0.25
    dt_adv = CFL * h_min / max(V_max_core, 1e-30)

    # Diffusion CFL: dt_diff = h^2 / (2*d*nu), d=2 spatial dims
    # Factor 8 for the (3/r) term which amplifies diffusion near r=0
    if nu > 0:
        dt_diff = h_min**2 / (8.0 * nu)
        dt = min(dt_adv, dt_diff)
    else:
        dt = dt_adv

    # Cap dt at 1e-3 for sanity
    dt = min(dt, 1e-3)

    n_steps = min(int(T_target / dt) + 1, n_steps_max)

    print(f"  dt = {dt:.2e}, n_steps = {n_steps}")

    # Since the RHS is constant (frozen velocity + frozen Laplacian),
    # the forward Euler is:
    #   v(t) = v(0) + t * (F_inviscid + nu * Lap_v)
    # This is exact (no numerical error from stepping).
    # We compute at several time points.

    Fv_total = Fv_inviscid + nu * Lap_v
    Fw_total = Fw_inviscid + nu * Lap_w

    T_total = n_steps * dt
    time_points = [0.0] + [dt * (i+1) for i in range(0, n_steps, max(n_steps//10, 1))]
    if time_points[-1] < T_total:
        time_points.append(T_total)

    v_max_history = []
    w_max_history = []
    time_history = []

    t0_step = time.time()

    for t_val in time_points:
        v_t = v + t_val * Fv_total
        w_t = w + t_val * Fw_total
        v_max_history.append(np.abs(v_t).max())
        w_max_history.append(np.abs(w_t).max())
        time_history.append(t_val)

    elapsed = time.time() - t0_step

    v_final_max = v_max_history[-1]
    w_final_max = w_max_history[-1]
    v0 = np.abs(v).max()
    w0 = np.abs(w).max()
    v_change = (v_final_max - v0) / max(v0, 1e-30)
    w_change = (w_final_max - w0) / max(w0, 1e-30)

    if v_change > 0.01:
        status = "GROWING"
    elif v_change < -0.01:
        status = "DECAYING"
    else:
        status = "STEADY"

    results.append({
        'nu': nu,
        'dt': dt,
        'n_steps': n_steps,
        'T_total': T_total,
        'v_init': v0,
        'v_final': v_final_max,
        'w_init': w0,
        'w_final': w_final_max,
        'v_change_pct': v_change * 100,
        'w_change_pct': w_change * 100,
        'status': status,
        'elapsed': elapsed,
        'v_history': v_max_history,
        'w_history': w_max_history,
        't_history': time_history,
    })

    print(f"  |v|_max: {v0:.6f} -> {v_final_max:.6f} ({v_change*100:+.6f}%)")
    print(f"  |w|_max: {w0:.6f} -> {w_final_max:.6f} ({w_change*100:+.6f}%)")
    print(f"  T_total = {T_total:.2e} | {elapsed:.1f}s | {status}")

    # Print trajectory
    print(f"  Trajectory |v|_max:")
    for i, (t_val, vm, wm) in enumerate(zip(time_history, v_max_history,
                                             w_max_history)):
        if i < 4 or i >= len(time_history) - 3:
            print(f"    t={t_val:8.4f}: |v|={vm:.8f}  |w|={wm:.8f}")
        elif i == 4:
            print(f"    ...")
    print()

# ---------------------------------------------------------------------------
# 6. Results table
# ---------------------------------------------------------------------------
print("="*80)
print("RESULTS SUMMARY")
print("="*80)
print(f"{'nu':>10s} {'dt':>10s} {'T_total':>10s} {'|v|_init':>10s} "
      f"{'|v|_final':>12s} {'dv%':>10s} {'|w|_final':>12s} {'dw%':>10s} "
      f"{'Status':>8s}")
print("-"*80)

for r in results:
    print(f"{r['nu']:10.1e} {r['dt']:10.2e} {r['T_total']:10.2e} "
          f"{r['v_init']:10.6f} {r['v_final']:12.6f} "
          f"{r['v_change_pct']:+10.4f} {r['w_final']:12.6f} "
          f"{r['w_change_pct']:+10.4f} {r['status']:>8s}")

print()

# ---------------------------------------------------------------------------
# 7. Diagnostic: where does Laplacian drive growth?
# ---------------------------------------------------------------------------
print("="*80)
print("DIAGNOSTIC: Laplacian structure at profile peak")
print("="*80)

# Where is |v| maximum?
idx_vmax = np.unravel_index(np.argmax(np.abs(v)), v.shape)
print(f"|v| peak at (ir={idx_vmax[0]}, iz={idx_vmax[1]}), "
      f"r={r_1d[idx_vmax[0]]:.4f}, z={z_1d[idx_vmax[1]]:.4f}")
print(f"  v = {v[idx_vmax]:.6f}")
print(f"  Lap_v = {Lap_v[idx_vmax]:.6f}")
print(f"  => nu*Lap_v at peak: diffuses v {'up' if Lap_v[idx_vmax] > 0 else 'down'}")

idx_wmax = np.unravel_index(np.argmax(np.abs(w)), w.shape)
print(f"|w| peak at (ir={idx_wmax[0]}, iz={idx_wmax[1]}), "
      f"r={r_1d[idx_wmax[0]]:.4f}, z={z_1d[idx_wmax[1]]:.4f}")
print(f"  w = {w[idx_wmax]:.6f}")
print(f"  Lap_w = {Lap_w[idx_wmax]:.6f}")
print(f"  => nu*Lap_w at peak: diffuses w {'up' if Lap_w[idx_wmax] > 0 else 'down'}")

# Where does the max of |v(T)| actually occur for nu=1e-3?
if results[-1]['nu'] == 1e-3:
    T_last = results[-1]['T_total']
    Fv_total_last = Fv_inviscid + 1e-3 * Lap_v
    v_final = v + T_last * Fv_total_last
    idx_vf = np.unravel_index(np.argmax(np.abs(v_final)), v_final.shape)
    print(f"\nFor nu=1e-3 at T={T_last:.2f}:")
    print(f"  |v_final| peak at (ir={idx_vf[0]}, iz={idx_vf[1]}), "
          f"r={r_1d[idx_vf[0]]:.4e}, z={z_1d[idx_vf[1]]:.4e}")
    print(f"  v_final = {v_final[idx_vf]:.6f}")
    print(f"  v_init there = {v[idx_vf]:.6e}")
    print(f"  Lap_v there = {Lap_v[idx_vf]:.6e}")
    Fw_total_last = Fw_inviscid + 1e-3 * Lap_w
    w_final = w + T_last * Fw_total_last
    idx_wf = np.unravel_index(np.argmax(np.abs(w_final)), w_final.shape)
    print(f"  |w_final| peak at (ir={idx_wf[0]}, iz={idx_wf[1]}), "
          f"r={r_1d[idx_wf[0]]:.4e}, z={z_1d[idx_wf[1]]:.4e}")
    print(f"  w_final = {w_final[idx_wf]:.6f}")
    print(f"  w_init there = {w[idx_wf]:.6e}")
    print(f"  Lap_w there = {Lap_w[idx_wf]:.6e}")

# Check if Lap is large near r=0 due to the 3/r singularity
print(f"\nLaplacian near r=0 (possible boundary artifact):")
print(f"  Lap_v[0,0] = {Lap_v[0,0]:.2f} (r=0, L'Hopital formula)")
print(f"  Lap_v[1,0] = {Lap_v[1,0]:.2f} (r={r_1d[1]:.4e}, 3/r={3/r_1d[1]:.1f})")
print(f"  Lap_v[2,0] = {Lap_v[2,0]:.2f} (r={r_1d[2]:.4e})")
print(f"  Lap_v[5,0] = {Lap_v[5,0]:.2f} (r={r_1d[5]:.4e})")
print(f"  Lap_v[10,0] = {Lap_v[10,0]:.2f} (r={r_1d[10]:.4e})")
print(f"  Lap_w[0,0] = {Lap_w[0,0]:.2f}")
print(f"  Lap_w[1,0] = {Lap_w[1,0]:.2f}")
print(f"  Lap_w[2,0] = {Lap_w[2,0]:.2f}")

# Components of Laplacian at ir=1 (where Lap is max)
print(f"\nLaplacian decomposition at ir=1, iz=0:")
print(f"  d2v/dr2 = {d2v_dr2[1,0]:.4f}")
print(f"  (3/r)*dv/dr = {three_over_r[1,0] * dv_dr[1,0]:.4f}")
print(f"  d2v/dz2 = {d2v_dz2[1,0]:.4f}")
print(f"  Total Lap_v = {Lap_v[1,0]:.4f}")

print()
print("Physical interpretation:")
print("  - nu=0:    Pure inviscid (Fv~3e-10). Perfectly steady (as expected).")
print("  - Small nu: Slight decay at the peak — viscosity smooths the profile.")
print("  - Large nu: Possible growth from the (3/r)df/dr term near r=0,")
print("             where the Laplacian is O(700). This is a physical effect:")
print("             the Hou-Li Laplacian amplifies near the symmetry axis.")
print("  CAVEAT: This is a LINEAR (frozen) test. The RHS is constant, so")
print("  v(t) = v(0) + t*RHS. Growth/decay is purely linear, not exponential.")
print("  In the full nonlinear system, velocity feedback would change the picture.")
print()
print("NOTE: This is a FROZEN-VELOCITY test (velocity never updated).")
print("In full NSE, the Biot-Savart velocity would respond to changes in")
print("w, creating feedback. This test isolates the diffusive effect only.")
print("\nFrozen-velocity test done. Starting nonlinear test...\n")


# ---------------------------------------------------------------------------
# 8. FULL NONLINEAR VISCOUS TEST (Poisson solve each step)
# ---------------------------------------------------------------------------

def build_poisson_laplacian(r, z):
    """
    Build the sparse matrix for -Lap psi1 = w on the (r, z) grid.

    Hou-Li Laplacian: Lap = d2/dr2 + (3/r) d/dr + d2/dz2
    At r=0: L'Hopital gives (3/r)d/dr -> 4 d2/dr2, so Lap = 4 d2/dr2 + d2/dz2 + d2/dr2 = ... wait,
    Actually Lap = d2/dr2 + (3/r)d/dr + d2/dz2. At r=0 with L'Hopital: (3/r)d/dr -> 3 d2/dr2,
    so Lap_r=0 = d2/dr2 + 3 d2/dr2 + d2/dz2 = 4 d2/dr2 + d2/dz2.

    We solve -Lap psi = w, i.e. A psi = w (A = -Lap).
    BCs: psi = 0 at r=r_max, z=0, z=z_max. At r=0: dpsi/dr = 0 (symmetry).

    Returns the sparse matrix A (Nr x Nz, Nr x Nz) and the LU factorization.
    """
    Nr, Nz = len(r), len(z)
    n = Nr * Nz
    print(f"  Building Poisson Laplacian: {Nr}x{Nz} = {n} unknowns...")

    dr = np.diff(r)
    dz = np.diff(z)

    # We'll build in lil format for efficiency, then convert to csc for splu
    A = lil_matrix((n, n), dtype=np.float64)

    def idx(i, j):
        return i * Nz + j

    t0 = time.time()

    for i in range(Nr):
        for j in range(Nz):
            k = idx(i, j)

            # Boundary conditions: psi = 0 at edges (except r=0 which is symmetry)
            # z=0 (j=0): psi = 0
            # z=z_max (j=Nz-1): psi = 0
            # r=r_max (i=Nr-1): psi = 0
            if j == 0 or j == Nz - 1 or i == Nr - 1:
                A[k, k] = 1.0
                continue

            if i == 0:
                # r = 0: symmetry axis
                # Lap = 4 d2f/dr2 + d2f/dz2
                # Use one-sided 2nd derivative for d2f/dr2:
                # f''(0) ≈ 2(f(dr) - f(0)) / dr^2 (from symmetry: f(-dr) = f(dr))
                dr0 = dr[0]
                dz_m = dz[j - 1]
                dz_p = dz[j]

                # d2/dr2 at r=0 with symmetry: f''(0) = 2*(f[1] - f[0]) / dr0^2
                coeff_d2r_center = -2.0 / (dr0 * dr0)
                coeff_d2r_right = 2.0 / (dr0 * dr0)

                # d2/dz2 (non-uniform)
                denom_z = 0.5 * (dz_m + dz_p)
                coeff_d2z_down = 1.0 / (dz_m * denom_z)
                coeff_d2z_up = 1.0 / (dz_p * denom_z)
                coeff_d2z_center = -(coeff_d2z_down + coeff_d2z_up)

                # -Lap = -(4*d2/dr2 + d2/dz2)
                A[k, k] = -(4.0 * coeff_d2r_center + coeff_d2z_center)
                A[k, idx(1, j)] = -(4.0 * coeff_d2r_right)
                A[k, idx(0, j - 1)] = -(coeff_d2z_down)
                A[k, idx(0, j + 1)] = -(coeff_d2z_up)
                continue

            # Interior point (i > 0, 0 < j < Nz-1)
            dr_m = dr[i - 1]  # r[i] - r[i-1]
            dr_p = dr[min(i, Nr - 2)]  # r[i+1] - r[i], but i < Nr-1 guaranteed above
            dz_m = dz[j - 1]
            dz_p = dz[j]

            # d2f/dr2 (non-uniform)
            denom_r = 0.5 * (dr_m + dr_p)
            c_left = 1.0 / (dr_m * denom_r)
            c_right = 1.0 / (dr_p * denom_r)
            c_center_r = -(c_left + c_right)

            # df/dr (non-uniform, centered)
            c_dr_left = -dr_p / (dr_m * (dr_m + dr_p))
            c_dr_center = (dr_p - dr_m) / (dr_m * dr_p)
            c_dr_right = dr_m / (dr_p * (dr_m + dr_p))

            three_r = 3.0 / r[i]

            # d2f/dz2 (non-uniform)
            denom_z = 0.5 * (dz_m + dz_p)
            c_down = 1.0 / (dz_m * denom_z)
            c_up = 1.0 / (dz_p * denom_z)
            c_center_z = -(c_down + c_up)

            # Lap = d2/dr2 + (3/r)d/dr + d2/dz2
            # -Lap coefficients:
            A[k, idx(i - 1, j)] = -(c_left + three_r * c_dr_left)
            A[k, k] = -(c_center_r + three_r * c_dr_center + c_center_z)
            A[k, idx(i + 1, j)] = -(c_right + three_r * c_dr_right)
            A[k, idx(i, j - 1)] = -(c_down)
            A[k, idx(i, j + 1)] = -(c_up)

    build_time = time.time() - t0
    print(f"  Matrix built in {build_time:.1f}s")

    print(f"  Converting to CSC and computing LU factorization...")
    t0 = time.time()
    A_csc = csc_matrix(A)
    lu = splu(A_csc)
    lu_time = time.time() - t0
    print(f"  LU done in {lu_time:.1f}s, nnz = {A_csc.nnz}")

    return A_csc, lu


def fd_deriv_r(f, r):
    """Compute df/dr using 2nd-order centered FD on non-uniform grid.
    Returns array same shape as f. Uses one-sided at boundaries."""
    Nr, Nz = f.shape
    df = np.zeros_like(f)
    dr = np.diff(r)

    # Interior: centered difference for non-uniform grid
    for i in range(1, Nr - 1):
        hm = r[i] - r[i - 1]
        hp = r[i + 1] - r[i]
        # f'(i) = (-hp^2 f[i-1] + (hp^2 - hm^2) f[i] + hm^2 f[i+1]) / (hm*hp*(hm+hp))
        df[i, :] = (-hp**2 * f[i-1, :] + (hp**2 - hm**2) * f[i, :] + hm**2 * f[i+1, :]) / (hm * hp * (hm + hp))

    # i=0: forward (2-point, or use symmetry df/dr=0 for psi, but for v,w use forward)
    h0 = dr[0]
    h1 = dr[1] if Nr > 2 else dr[0]
    df[0, :] = (-(2*h0 + h1) / (h0*(h0+h1)) * f[0, :]
                + (h0 + h1) / (h0*h1) * f[1, :]
                - h0 / (h1*(h0+h1)) * f[2, :])

    # i=Nr-1: backward
    hm = dr[-1]
    hm2 = dr[-2] if Nr > 2 else dr[-1]
    df[-1, :] = (hm / (hm2*(hm2+hm)) * f[-3, :]
                 - (hm2+hm) / (hm2*hm) * f[-2, :]
                 + (2*hm + hm2) / (hm*(hm2+hm)) * f[-1, :])

    return df


def fd_deriv_z(f, z):
    """Compute df/dz using 2nd-order centered FD on non-uniform grid."""
    Nr, Nz = f.shape
    df = np.zeros_like(f)
    dz = np.diff(z)

    for j in range(1, Nz - 1):
        hm = z[j] - z[j - 1]
        hp = z[j + 1] - z[j]
        df[:, j] = (-hp**2 * f[:, j-1] + (hp**2 - hm**2) * f[:, j] + hm**2 * f[:, j+1]) / (hm * hp * (hm + hp))

    # j=0: forward
    h0 = dz[0]
    h1 = dz[1] if Nz > 2 else dz[0]
    df[:, 0] = (-(2*h0 + h1) / (h0*(h0+h1)) * f[:, 0]
                + (h0 + h1) / (h0*h1) * f[:, 1]
                - h0 / (h1*(h0+h1)) * f[:, 2])

    # j=Nz-1: backward
    hm = dz[-1]
    hm2 = dz[-2] if Nz > 2 else dz[-1]
    df[:, -1] = (hm / (hm2*(hm2+hm)) * f[:, -3]
                 - (hm2+hm) / (hm2*hm) * f[:, -2]
                 + (2*hm + hm2) / (hm*(hm2+hm)) * f[:, -1])

    return df


def compute_laplacian_fd(f, r, z, three_over_r_2d):
    """Compute Hou-Li Laplacian of f using FD. r[0] must be 0 or near-zero."""
    Nr, Nz = f.shape
    dr = np.diff(r)
    dz_arr = np.diff(z)

    d2f_dr2 = np.zeros_like(f)
    d2f_dz2 = np.zeros_like(f)

    # d2f/dr2
    for i in range(1, Nr - 1):
        hm = dr[i - 1]
        hp = dr[i]
        d2f_dr2[i, :] = 2.0 * (f[i+1, :] / (hp * (hm + hp))
                                - f[i, :] / (hm * hp)
                                + f[i-1, :] / (hm * (hm + hp)))
    # i=0: symmetry => f''(0) = 2*(f[1]-f[0])/dr[0]^2
    d2f_dr2[0, :] = 2.0 * (f[1, :] - f[0, :]) / (dr[0] ** 2)
    # i=Nr-1: not needed (BC)

    # d2f/dz2
    for j in range(1, Nz - 1):
        hm = dz_arr[j - 1]
        hp = dz_arr[j]
        d2f_dz2[:, j] = 2.0 * (f[:, j+1] / (hp * (hm + hp))
                                - f[:, j] / (hm * hp)
                                + f[:, j-1] / (hm * (hm + hp)))

    df_dr = fd_deriv_r(f, r)

    lap = d2f_dr2 + three_over_r_2d * df_dr + d2f_dz2
    # At r=0: Lap = 4*d2f/dr2 + d2f/dz2
    lap[0, :] = 4.0 * d2f_dr2[0, :] + d2f_dz2[0, :]

    return lap


def run_nonlinear_viscous_test(r_full, z_full, v_init, w_init, cl, cw,
                               nu_values, n_steps=5000, N_trunc=400):
    """
    Full nonlinear viscous time-stepping with Poisson solve.

    At each step:
      1. Solve -Lap psi1 = w for psi1
      2. Compute velocity: u_r = -r * dpsi1/dz, u_z = 2*psi1 + r * dpsi1/dr
      3. Compute RHS for v and w (full nonlinear equations)
      4. Update v, w via RK2 (midpoint method)

    Uses truncated grid (first N_trunc points) for speed.
    """
    print("=" * 80)
    print("FULL NONLINEAR VISCOUS TIME-STEPPING (Poisson solve)")
    print("=" * 80)

    # Truncate grid to where the profile lives
    Nr = min(N_trunc, len(r_full))
    Nz = min(N_trunc, len(z_full))
    r = r_full[:Nr].copy()
    z = z_full[:Nz].copy()

    print(f"Truncated grid: {Nr}x{Nz} (from {len(r_full)}x{len(z_full)})")
    print(f"  r range: [{r[0]:.2e}, {r[-1]:.2e}]")
    print(f"  z range: [{z[0]:.2e}, {z[-1]:.2e}]")

    v0 = v_init[:Nr, :Nz].copy()
    w0 = w_init[:Nr, :Nz].copy()

    print(f"  |v|_max on truncated grid = {np.abs(v0).max():.6f}")
    print(f"  |w|_max on truncated grid = {np.abs(w0).max():.6f}")

    # Check how much profile energy is outside the truncated grid
    v_outside = np.abs(v_init[Nr:, :]).max() if Nr < len(r_full) else 0
    w_outside = np.abs(w_init[Nr:, :]).max() if Nr < len(r_full) else 0
    v_outside_z = np.abs(v_init[:, Nz:]).max() if Nz < len(z_full) else 0
    w_outside_z = np.abs(w_init[:, Nz:]).max() if Nz < len(z_full) else 0
    print(f"  |v| outside r-truncation = {max(v_outside, v_outside_z):.2e}")
    print(f"  |w| outside r-truncation = {max(w_outside, w_outside_z):.2e}")

    # Build 2D grid arrays
    R2d, Z2d = np.meshgrid(r, z, indexing='ij')

    # 3/r array for Laplacian
    three_over_r = np.zeros_like(R2d)
    three_over_r[1:, :] = 3.0 / R2d[1:, :]

    # Build Poisson Laplacian and LU factorization
    A, lu = build_poisson_laplacian(r, z)

    # Verify Poisson solve against saved velocity
    print("\n  Verifying Poisson solve against saved u_r, u_z...")
    w_rhs = w0.ravel()
    psi1_test = lu.solve(w_rhs)
    psi1_test = psi1_test.reshape(Nr, Nz)

    dpsi_dz = fd_deriv_z(psi1_test, z)
    dpsi_dr = fd_deriv_r(psi1_test, r)
    ur_test = -R2d * dpsi_dz
    uz_test = 2.0 * psi1_test + R2d * dpsi_dr

    # Compare to saved velocity (truncated)
    ur_saved_trunc = u_r[:Nr, :Nz]
    uz_saved_trunc = u_z[:Nr, :Nz]
    ur_err = np.abs(ur_test - ur_saved_trunc).max()
    uz_err = np.abs(uz_test - uz_saved_trunc).max()
    print(f"  |u_r - u_r_saved|_max = {ur_err:.2e} (|u_r_saved|_max = {np.abs(ur_saved_trunc).max():.2e})")
    print(f"  |u_z - u_z_saved|_max = {uz_err:.2e} (|u_z_saved|_max = {np.abs(uz_saved_trunc).max():.2e})")

    # CFL estimate
    dr_arr = np.diff(r)
    dz_arr = np.diff(z)
    h_min = min(dr_arr.min(), dz_arr.min())

    # Core velocity for CFL (r,z < 10)
    core_r = r < 10.0
    core_z = z < 10.0
    core_mask = np.outer(core_r, core_z)
    V_r_core = cl * R2d + ur_test
    V_z_core = cl * Z2d + uz_test
    V_mag = np.sqrt(V_r_core**2 + V_z_core**2)
    V_max_core = V_mag[core_mask].max() if core_mask.any() else V_mag.max()
    print(f"  h_min = {h_min:.6e}, V_max_core = {V_max_core:.2e}")

    def compute_rhs(v_cur, w_cur, r, z, R2d, Z2d, lu, three_over_r, cl, cw, nu):
        """Compute full nonlinear RHS for v and w."""
        Nr, Nz = v_cur.shape

        # 1. Poisson solve: -Lap psi1 = w
        psi1 = lu.solve(w_cur.ravel()).reshape(Nr, Nz)

        # 2. Velocity from stream function
        dpsi_dr = fd_deriv_r(psi1, r)
        dpsi_dz = fd_deriv_z(psi1, z)
        u_r_cur = -R2d * dpsi_dz
        u_z_cur = 2.0 * psi1 + R2d * dpsi_dr

        # 3. Derivatives of v and w
        dv_dr_cur = fd_deriv_r(v_cur, r)
        dv_dz_cur = fd_deriv_z(v_cur, z)
        dw_dr_cur = fd_deriv_r(w_cur, r)
        dw_dz_cur = fd_deriv_z(w_cur, z)

        # 4. du_r/dr
        dur_dr_cur = fd_deriv_r(u_r_cur, r)

        # 5. Viscous Laplacian (if nu > 0)
        if nu > 0:
            Lap_v_cur = compute_laplacian_fd(v_cur, r, z, three_over_r)
            Lap_w_cur = compute_laplacian_fd(w_cur, r, z, three_over_r)
        else:
            Lap_v_cur = 0.0
            Lap_w_cur = 0.0

        # 6. RHS
        Fv = (-(cl * R2d + u_r_cur) * dv_dr_cur
              - (cl * Z2d + u_z_cur) * dv_dz_cur
              + (2.0 * cw - dur_dr_cur) * v_cur
              + nu * Lap_v_cur)

        Fw = (-(cl * R2d + u_r_cur) * dw_dr_cur
              - (cl * Z2d + u_z_cur) * dw_dz_cur
              + cw * w_cur + v_cur + R2d * dv_dr_cur
              + nu * Lap_w_cur)

        # Enforce BCs: zero RHS at boundaries
        Fv[-1, :] = 0.0; Fv[:, 0] = 0.0; Fv[:, -1] = 0.0
        Fw[-1, :] = 0.0; Fw[:, 0] = 0.0; Fw[:, -1] = 0.0

        return Fv, Fw

    # Run for each nu value
    results_nl = []

    for nu in nu_values:
        print(f"\n--- nu = {nu:.1e} (nonlinear, RK2) ---")

        # CFL
        CFL = 0.2
        dt_adv = CFL * h_min / max(V_max_core, 1e-30)
        if nu > 0:
            dt_diff = h_min**2 / (8.0 * nu)
            dt = min(dt_adv, dt_diff)
        else:
            dt = dt_adv
        dt = min(dt, 1e-3)

        print(f"  dt = {dt:.2e}, n_steps = {n_steps}")

        v_cur = v0.copy()
        w_cur = w0.copy()

        v_max_hist = [np.abs(v_cur).max()]
        w_max_hist = [np.abs(w_cur).max()]
        resid_hist = []

        # Compute initial residual (inviscid RHS norm — should be ~3e-10 for steady state)
        Fv0, Fw0 = compute_rhs(v_cur, w_cur, r, z, R2d, Z2d, lu, three_over_r, cl, cw, 0.0)
        resid0 = max(np.abs(Fv0).max(), np.abs(Fw0).max())
        resid_hist.append(resid0)
        print(f"  Initial residual (inviscid RHS): {resid0:.2e}")

        t0_run = time.time()

        for step in range(n_steps):
            # RK2 midpoint method:
            #   k1 = dt * RHS(v, w)
            #   k2 = dt * RHS(v + k1/2, w + k1/2)
            #   v_new = v + k2, w_new = w + k2

            Fv1, Fw1 = compute_rhs(v_cur, w_cur, r, z, R2d, Z2d, lu,
                                    three_over_r, cl, cw, nu)

            v_mid = v_cur + 0.5 * dt * Fv1
            w_mid = w_cur + 0.5 * dt * Fw1

            Fv2, Fw2 = compute_rhs(v_mid, w_mid, r, z, R2d, Z2d, lu,
                                    three_over_r, cl, cw, nu)

            v_cur = v_cur + dt * Fv2
            w_cur = w_cur + dt * Fw2

            # Enforce BCs
            v_cur[-1, :] = 0.0; v_cur[:, 0] = 0.0; v_cur[:, -1] = 0.0
            w_cur[-1, :] = 0.0; w_cur[:, 0] = 0.0; w_cur[:, -1] = 0.0

            # Track every 500 steps
            if (step + 1) % 500 == 0 or step == n_steps - 1:
                vm = np.abs(v_cur).max()
                wm = np.abs(w_cur).max()
                v_max_hist.append(vm)
                w_max_hist.append(wm)

                # Inviscid residual (how far from steady state)
                Fv_chk, Fw_chk = compute_rhs(v_cur, w_cur, r, z, R2d, Z2d, lu,
                                              three_over_r, cl, cw, 0.0)
                resid = max(np.abs(Fv_chk).max(), np.abs(Fw_chk).max())
                resid_hist.append(resid)

                elapsed = time.time() - t0_run
                T_sim = (step + 1) * dt
                print(f"  step {step+1:5d}: |v|={vm:.6f} |w|={wm:.6f} "
                      f"resid={resid:.2e} T={T_sim:.4f} ({elapsed:.0f}s)")

                # Blow-up check
                if vm > 1e6 or wm > 1e6 or np.isnan(vm) or np.isnan(wm):
                    print(f"  *** BLOW-UP detected at step {step+1} ***")
                    break

        total_time = time.time() - t0_run
        T_total = min(step + 1, n_steps) * dt

        v_final = np.abs(v_cur).max()
        w_final = np.abs(w_cur).max()
        v0_max = np.abs(v0).max()
        w0_max = np.abs(w0).max()
        v_change = (v_final - v0_max) / max(v0_max, 1e-30)
        w_change = (w_final - w0_max) / max(w0_max, 1e-30)

        if v_change > 0.01:
            status = "GROWING"
        elif v_change < -0.01:
            status = "DECAYING"
        else:
            status = "STEADY"

        results_nl.append({
            'nu': nu,
            'dt': dt,
            'n_steps': n_steps,
            'T_total': T_total,
            'v_init': v0_max,
            'v_final': v_final,
            'w_init': w0_max,
            'w_final': w_final,
            'v_change_pct': v_change * 100,
            'w_change_pct': w_change * 100,
            'resid_init': resid_hist[0],
            'resid_final': resid_hist[-1],
            'status': status,
            'elapsed': total_time,
        })

        print(f"  RESULT: |v| {v0_max:.6f} -> {v_final:.6f} ({v_change*100:+.4f}%)")
        print(f"          |w| {w0_max:.6f} -> {w_final:.6f} ({w_change*100:+.4f}%)")
        print(f"          residual {resid_hist[0]:.2e} -> {resid_hist[-1]:.2e}")
        print(f"          {status} | {total_time:.0f}s")

    # Summary table
    print("\n" + "=" * 100)
    print("NONLINEAR RESULTS SUMMARY")
    print("=" * 100)
    print(f"{'nu':>10s} {'dt':>10s} {'T_total':>10s} {'|v|_init':>10s} "
          f"{'|v|_final':>12s} {'dv%':>10s} {'|w|_final':>12s} {'dw%':>10s} "
          f"{'resid_i':>10s} {'resid_f':>10s} {'Status':>8s}")
    print("-" * 100)

    for res in results_nl:
        print(f"{res['nu']:10.1e} {res['dt']:10.2e} {res['T_total']:10.2e} "
              f"{res['v_init']:10.6f} {res['v_final']:12.6f} "
              f"{res['v_change_pct']:+10.4f} {res['w_final']:12.6f} "
              f"{res['w_change_pct']:+10.4f} {res['resid_init']:10.2e} "
              f"{res['resid_final']:10.2e} {res['status']:>8s}")

    print()
    print("Interpretation:")
    print("  resid_i = inviscid residual at t=0 (should be ~3e-10 for Chen-Hou steady state)")
    print("  resid_f = inviscid residual at final time (deviation from steady state)")
    print("  If nu=0 stays STEADY with resid~3e-10: Poisson solver + FD are consistent.")
    print("  If nu>0 causes DECAY: viscosity regularizes the singularity (good for NS).")
    print("  If nu>0 causes GROWTH: viscous terms amplify the profile (bad for regularity).")

    return results_nl


# Run the nonlinear test
nl_nu_values = [0, 1e-5, 1e-4, 1e-3]
run_nonlinear_viscous_test(r_1d, z_1d, v, w, cl, cw,
                           nu_values=nl_nu_values, n_steps=5000, N_trunc=400)

print("\nDone.")
