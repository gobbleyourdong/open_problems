"""
Compute the instantaneous viscous force on Chen-Hou's exact steady state.

At the steady state, Fv ≈ Fw ≈ 0 (residual 3.2e-10).
Adding ν·Δv and ν·Δw creates a PERTURBATION force.

If this force pushes the profile toward zero → viscosity kills blowup.
If it pushes the profile to grow → viscosity helps blowup (unlikely but possible).
If it's tangent to the profile → viscosity deforms but doesn't kill.

We compute ν·Δ on THEIR 720×720 grid using THEIR data.
No interpolation. No Poisson solve. Just finite differences on their grid.
"""
import sys, os, math, json
import numpy as np
import scipy.io as sio


def compute_laplacian_nonuniform(f, r, z):
    """
    Compute Δf = (∂²f/∂r² + 3/r·∂f/∂r + ∂²f/∂z²) on non-uniform grid.
    Uses 2nd-order finite differences adapted for non-uniform spacing.

    This is the Hou-Li Laplacian L3 = D²r + (3/r)Dr + D²z
    """
    nr, nz = f.shape
    lap = np.zeros_like(f)

    # Radial part: ∂²f/∂r² + (3/r)·∂f/∂r
    for j in range(nz):
        for i in range(1, nr - 1):
            dr_m = r[i] - r[i-1]
            dr_p = r[i+1] - r[i]
            # 2nd-order FD on non-uniform grid
            f_rr = 2 * (dr_m * f[i+1, j] - (dr_m + dr_p) * f[i, j] + dr_p * f[i-1, j]) / \
                   (dr_m * dr_p * (dr_m + dr_p))
            f_r = (dr_m**2 * f[i+1, j] - (dr_m**2 - dr_p**2) * f[i, j] - dr_p**2 * f[i-1, j]) / \
                  (dr_m * dr_p * (dr_m + dr_p))

            if r[i] > 1e-10:
                lap[i, j] += f_rr + 3.0 / r[i] * f_r
            else:
                # L'Hôpital at r=0: (3/r)f' → 3f'' → total 4f''
                lap[i, j] += 4.0 * f_rr

    # z part: ∂²f/∂z²
    for i in range(nr):
        for j in range(1, nz - 1):
            dz_m = z[j] - z[j-1]
            dz_p = z[j+1] - z[j]
            f_zz = 2 * (dz_m * f[i, j+1] - (dz_m + dz_p) * f[i, j] + dz_p * f[i, j-1]) / \
                   (dz_m * dz_p * (dz_m + dz_p))
            lap[i, j] += f_zz

    return lap


def main():
    mat_path = os.path.join(os.path.dirname(__file__),
        "chen_hou_matlab", "ASS_data", "Steady_state_pertb720_Nlevcor4.mat")
    mat = sio.loadmat(mat_path)

    v = mat['v']        # u₁, 720×720
    w = mat['w']        # ω₁, 720×720
    Fv = mat['Fv']      # residual for v
    Fw = mat['Fw']      # residual for w

    mesh = mat['Mesh'][0, 0]
    r = mesh['x'][0, 0].flatten()  # 720 pts
    z = mesh['x'][0, 1].flatten()  # 720 pts

    solu = mat['solu'][0, 0]
    cl = solu['cl'].item()
    cw = solu['cw'].item()

    print("CHEN-HOU VISCOUS FORCE ANALYSIS")
    print("=" * 60)
    print(f"Profile: 720×720, cl={cl:.4f}, cw={cw:.4f}")
    print(f"|v|_max = {abs(v).max():.6f}")
    print(f"|w|_max = {abs(w).max():.6f}")
    print(f"|Fv|_max = {abs(Fv).max():.2e} (inviscid residual)")
    print(f"|Fw|_max = {abs(Fw).max():.2e}")

    # Compute Laplacian of v and w on their grid
    print(f"\nComputing Δv and Δw on 720×720 non-uniform grid...")
    Lap_v = compute_laplacian_nonuniform(v, r, z)
    Lap_w = compute_laplacian_nonuniform(w, r, z)

    print(f"|Δv|_max = {abs(Lap_v).max():.6e}")
    print(f"|Δw|_max = {abs(Lap_w).max():.6e}")

    # The viscous perturbation at various ν
    print(f"\n{'='*60}")
    print(f"VISCOUS FORCE = ν · Δf")
    print(f"Compared to inviscid residual and profile amplitude")
    print(f"{'='*60}")

    print(f"\n{'ν':>10} {'|ν·Δv|_max':>12} {'vs |Fv|':>12} {'vs |v|':>12} "
          f"{'|ν·Δw|_max':>12} {'vs |Fw|':>12} {'vs |w|':>12}")
    print("-" * 85)

    for nu in [1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]:
        visc_v = nu * abs(Lap_v).max()
        visc_w = nu * abs(Lap_w).max()
        ratio_v_res = visc_v / (abs(Fv).max() + 1e-30)
        ratio_w_res = visc_w / (abs(Fw).max() + 1e-30)
        ratio_v_amp = visc_v / abs(v).max()
        ratio_w_amp = visc_w / abs(w).max()

        marker = ""
        if ratio_v_res > 1 and ratio_v_res < 100:
            marker = " ← COMPARABLE"
        elif ratio_v_res >= 100:
            marker = " ← DOMINANT"

        print(f"{nu:10.1e} {visc_v:12.4e} {ratio_v_res:12.2f}× {ratio_v_amp:12.6f} "
              f"{visc_w:12.4e} {ratio_w_res:12.2f}× {ratio_w_amp:12.6f}{marker}")

    # Spatial structure: WHERE does viscosity act?
    print(f"\n{'='*60}")
    print(f"SPATIAL STRUCTURE OF VISCOUS FORCE")
    print(f"{'='*60}")

    # Find where Δv and Δw are largest
    peak_Lv = np.unravel_index(abs(Lap_v).argmax(), Lap_v.shape)
    peak_Lw = np.unravel_index(abs(Lap_w).argmax(), Lap_w.shape)
    peak_v = np.unravel_index(abs(v).argmax(), v.shape)
    peak_w = np.unravel_index(abs(w).argmax(), w.shape)

    print(f"\nProfile peaks:")
    print(f"  v peaks at r={r[peak_v[0]]:.4f}, z={z[peak_v[1]]:.4f}")
    print(f"  w peaks at r={r[peak_w[0]]:.4f}, z={z[peak_w[1]]:.4f}")
    print(f"\nLaplacian peaks:")
    print(f"  Δv peaks at r={r[peak_Lv[0]]:.4f}, z={z[peak_Lv[1]]:.4f}")
    print(f"  Δw peaks at r={r[peak_Lw[0]]:.4f}, z={z[peak_Lw[1]]:.4f}")

    # Sign analysis: does viscosity OPPOSE or ASSIST the profile?
    # At profile peak, if Δf < 0 → viscosity diffuses the peak (opposes)
    # At profile peak, if Δf > 0 → viscosity sharpens the peak (assists)
    print(f"\nSign at profile peaks:")
    print(f"  Δv at v-peak = {Lap_v[peak_v]:.6e} → {'DIFFUSES (opposes)' if Lap_v[peak_v] < 0 else 'SHARPENS (assists)'}")
    print(f"  Δw at w-peak = {Lap_w[peak_w]:.6e} → {'DIFFUSES (opposes)' if Lap_w[peak_w] < 0 else 'SHARPENS (assists)'}")

    # Inner product: does viscous force project ONTO or AGAINST the profile?
    # <ν·Δv, v> < 0 → viscosity reduces energy → opposes blowup
    # <ν·Δv, v> > 0 → viscosity adds energy → assists blowup
    inner_v = np.sum(Lap_v * v)
    inner_w = np.sum(Lap_w * w)
    print(f"\nInner products (energy projection):")
    print(f"  <Δv, v> = {inner_v:.6e} → {'OPPOSES blowup' if inner_v < 0 else 'ASSISTS blowup'}")
    print(f"  <Δw, w> = {inner_w:.6e} → {'OPPOSES blowup' if inner_w < 0 else 'ASSISTS blowup'}")

    # Critical ν estimate: at what ν does viscous force overwhelm the
    # nonlinear dynamics that maintain the steady state?
    # The steady state is maintained by a balance of terms ~O(|v|·c_l) ~ O(1)
    # Viscous force becomes comparable when ν·|Δv| ~ c_l·|v|
    nu_c_v = cl * abs(v).max() / (abs(Lap_v).max() + 1e-30)
    nu_c_w = cl * abs(w).max() / (abs(Lap_w).max() + 1e-30)
    print(f"\nCritical ν estimate (viscous ~ nonlinear):")
    print(f"  From v: ν_c ≈ {nu_c_v:.4e}")
    print(f"  From w: ν_c ≈ {nu_c_w:.4e}")
    print(f"  Below this → profile might survive")
    print(f"  Above this → viscosity definitely dominates")

    # Save results
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    results = {
        'Lap_v_max': float(abs(Lap_v).max()),
        'Lap_w_max': float(abs(Lap_w).max()),
        'inner_v': float(inner_v),
        'inner_w': float(inner_w),
        'nu_c_v': float(nu_c_v),
        'nu_c_w': float(nu_c_w),
        'Fv_max': float(abs(Fv).max()),
        'Fw_max': float(abs(Fw).max()),
    }
    out_path = os.path.join(out_dir, "chen_hou_viscous_force.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
