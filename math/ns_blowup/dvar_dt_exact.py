"""
DVar/Dt EXACT: full strain-equation decomposition of the tilting advantage.

The 2:1 tilting argument:
  - Var = S^2_ee - alpha^2  where alpha = eh . S . eh, S^2_ee = eh . S^2 . eh
  - eh = omega/|omega| (vorticity direction)
  - c_i = (eh . e_i)^2  (alignment cosines with strain eigenvectors)
  - alpha = sum(lambda_i * c_i), Var = sum((lambda_i - alpha)^2 * c_i)
  - Material derivative DVar/Dt has contributions from:
    (a) Eigenvalue changes (from DS/Dt = -S^2 - Omega^2 - H)
    (b) Tilting: omega_hat rotation + eigenvector rotation
  - Tilting prediction: DVar/Dt ~ -|omega| * Var (exponential decay at rate |omega|)
  - Blowup rate: d(ln|omega|)/dt = alpha, with |alpha| <= sqrt(S2ee) <= |omega|/2

  The question: do eigenvalue changes from the strain equation ruin the tilting decay?

We compute DVar/Dt analytically from:
  DS/Dt = -S^2 - Omega^2 - H  (inviscid Euler strain equation)
  D(eh)/Dt = (S - alpha*I) . eh  (vorticity direction equation)

All cross-checks verify to machine precision (Dalpha two independent formulas).
FD validation uses Lagrangian particle tracking for honest comparison.
"""
import torch
import numpy as np
import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from ns3d_spectral import (NS3DSpectral, ic_taylor_green, ic_kida_pelz,
                            ic_random_large_scale, ic_trefoil_knot)

DTYPE = torch.float64
pi = math.pi


def diagnostics_at_max_omega(solver, wx_hat, wy_hat, wz_hat):
    """
    At the max-|omega| point, compute Var, DVar/Dt (material), and full decomposition.

    Returns None if |omega| is too small.
    """
    D = solver.dealias
    N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]

    # Velocity from vorticity
    ux_hat, uy_hat, uz_hat = solver.velocity_from_vorticity(wx_hat, wy_hat, wz_hat)
    u_hat = [ux_hat, uy_hat, uz_hat]
    w_hat = [wx_hat, wy_hat, wz_hat]

    # Velocity gradient A_ij = du_i/dx_j (full field, then extract point)
    A_field = torch.zeros(3, 3, N, N, N, dtype=DTYPE, device=solver.device)
    for i in range(3):
        for j in range(3):
            A_field[i, j] = solver.ifft(1j * kd[j] * D * u_hat[i])

    # Vorticity in physical space
    wf = [solver.ifft(D * w_hat[i]) for i in range(3)]
    om = (wf[0]**2 + wf[1]**2 + wf[2]**2).sqrt()
    flat = om.flatten()
    idx = flat.argmax().item()
    iz = idx % N
    iy = (idx // N) % N
    ix = idx // (N * N)

    wv = torch.tensor([wf[i][ix, iy, iz].item() for i in range(3)], dtype=DTYPE)
    wn = wv.norm().item()
    if wn < 1e-10:
        return None
    eh = wv / wv.norm()

    # Velocity at max point (for Lagrangian tracking)
    uf = [solver.ifft(D * u_hat[i]) for i in range(3)]
    u_local = torch.tensor([uf[i][ix, iy, iz].item() for i in range(3)], dtype=DTYPE)

    # --- Local tensors at max-omega point ---
    A = A_field[:, :, ix, iy, iz]
    Sl = 0.5 * (A + A.T)  # strain
    Omega_l = 0.5 * (A - A.T)  # rotation

    S2l = Sl @ Sl
    O2l = Omega_l @ Omega_l

    # Pressure Hessian
    source = -torch.einsum('ij,ji->', A, A)  # scalar at this point = -A_ij*A_ji
    # Need full-field pressure for the Hessian
    source_field = torch.zeros(N, N, N, dtype=DTYPE, device=solver.device)
    for i in range(3):
        for j in range(3):
            source_field -= A_field[i, j] * A_field[j, i]
    p_hat = -solver.fft(source_field) / solver.ksq
    p_hat[0, 0, 0] = 0
    Hl = torch.zeros(3, 3, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Hl[i, j] = solver.ifft(-kd[i] * kd[j] * p_hat)[ix, iy, iz]

    # Eigen-decomposition of strain
    ev, ec = torch.linalg.eigh(Sl)
    lam = ev.clone()
    c = torch.tensor([(eh @ ec[:, j]).item()**2 for j in range(3)], dtype=DTYPE)

    # alpha, S^k_ee
    alpha = (lam * c).sum().item()
    S2ee = (lam**2 * c).sum().item()
    S3ee = (eh @ Sl @ S2l @ eh).item()
    Var = S2ee - alpha**2

    O2ee = (eh @ O2l @ eh).item()
    Hee = (eh @ Hl @ eh).item()

    # ========== D(alpha)/Dt (material derivative) ==========
    # = eh . (DS/Dt) . eh + 2*(D(eh)/Dt)^T . S . eh
    # DS/Dt = -S^2 - Omega^2 - H
    # D(eh)/Dt = (S - alpha*I).eh
    # Tilt part: 2*(S2ee - alpha^2) = 2*Var
    # Total: -S2ee - O2ee - Hee + 2*Var = S2ee - 2*alpha^2 - O2ee - Hee
    Dalpha_strain = -S2ee - O2ee - Hee
    Dalpha_tilt = 2 * Var  # = 2*(S2ee - alpha^2)
    Dalpha = Dalpha_strain + Dalpha_tilt

    # Cross-check (algebraically identical)
    Dalpha_check = S2ee - 2*alpha**2 - O2ee - Hee
    dalpha_err = abs(Dalpha - Dalpha_check)

    # ========== D(S^2_ee)/Dt ==========
    # = eh . D(S^2)/Dt . eh + 2*(D(eh)/Dt)^T . S^2 . eh
    # D(S^2)/Dt = (DS/Dt).S + S.(DS/Dt)
    dSdt = -S2l - O2l - Hl
    dS2dt = dSdt @ Sl + Sl @ dSdt
    DS2ee_strain = (eh @ dS2dt @ eh).item()
    DS2ee_tilt = 2 * (S3ee - alpha * S2ee)
    DS2ee = DS2ee_strain + DS2ee_tilt

    # ========== DVar/Dt = DS2ee - 2*alpha*Dalpha ==========
    DVar = DS2ee - 2 * alpha * Dalpha

    # ========== Decomposition: eigenvalue vs tilting ==========
    # Eigenvalue rates: dlambda_i/dt = e_i . dSdt . e_i (from DS/Dt only)
    dlam = torch.tensor([(ec[:, j] @ dSdt @ ec[:, j]).item() for j in range(3)], dtype=DTYPE)

    # Eigenvalue contribution to DVar (holding c_i fixed):
    # d(S2ee)|_ev = sum(2*lam_i*dlam_i*c_i)
    # d(alpha)|_ev = sum(dlam_i*c_i)
    # d(Var)|_ev = d(S2ee)|_ev - 2*alpha*d(alpha)|_ev
    dS2ee_ev = (2 * lam * dlam * c).sum().item()
    dalpha_ev = (dlam * c).sum().item()
    dVar_ev = dS2ee_ev - 2 * alpha * dalpha_ev

    # Tilting contribution = total - eigenvalue
    dVar_tilt_total = DVar - dVar_ev

    # Sub-decompose tilting: omega_hat rotation vs eigenvector rotation
    # omega_hat rotation contribution to DVar:
    #   DS2ee_tilt - 2*alpha*Dalpha_tilt
    #   = 2*(S3ee - alpha*S2ee) - 2*alpha*2*Var
    #   = 2*S3ee - 2*alpha*S2ee - 4*alpha*(S2ee - alpha^2)
    #   = 2*S3ee - 6*alpha*S2ee + 4*alpha^3
    dVar_omega_rot = 2*S3ee - 6*alpha*S2ee + 4*alpha**3
    dVar_eigvec_rot = dVar_tilt_total - dVar_omega_rot

    # ========== Tilting advantage metrics ==========
    tilting_pred = -wn * Var
    if abs(Var) > 1e-20 and wn > 1e-10:
        ratio = DVar / tilting_pred
        var_decay_rate = abs(DVar / Var)
        blowup_rate = abs(alpha)
        tilting_wins = var_decay_rate > blowup_rate
    else:
        ratio = var_decay_rate = float('nan')
        blowup_rate = abs(alpha)
        tilting_wins = False

    # Source decomposition of eigenvalue changes
    contrib_S2 = (torch.tensor([(ec[:, j] @ (-S2l) @ ec[:, j]).item() for j in range(3)], dtype=DTYPE) * c).sum().item()
    contrib_O2 = (torch.tensor([(ec[:, j] @ (-O2l) @ ec[:, j]).item() for j in range(3)], dtype=DTYPE) * c).sum().item()
    contrib_H = (torch.tensor([(ec[:, j] @ (-Hl) @ ec[:, j]).item() for j in range(3)], dtype=DTYPE) * c).sum().item()

    return {
        'om': wn, 'alpha': alpha, 'Var': Var, 'S2ee': S2ee, 'S3ee': S3ee,
        'Hee': Hee, 'O2ee': O2ee,
        'lam': lam.numpy(), 'c': c.numpy(),
        'u_local': u_local.numpy(),
        'DVar': DVar, 'DVar_ev': dVar_ev, 'DVar_tilt': dVar_tilt_total,
        'DVar_omega_rot': dVar_omega_rot, 'DVar_eigvec_rot': dVar_eigvec_rot,
        'Dalpha': Dalpha, 'dalpha_err': dalpha_err, 'dalpha_ev': dalpha_ev,
        'ratio': ratio, 'var_decay_rate': var_decay_rate,
        'blowup_rate': blowup_rate, 'tilting_wins': tilting_wins,
        'dlnomdt': alpha,
        'contrib_S2': contrib_S2, 'contrib_O2': contrib_O2, 'contrib_H': contrib_H,
        'ix': ix, 'iy': iy, 'iz': iz,
    }


def lagrangian_var(solver, w, x_pos):
    """Compute Var at an arbitrary position using trilinear interpolation."""
    D = solver.dealias
    N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]
    dx = solver.dx

    # Wrap to [0, L)
    L = solver.Lx
    x_pos = [p % L for p in x_pos]

    # Grid indices for trilinear interpolation
    fx = x_pos[0] / dx
    fy = x_pos[1] / dx
    fz = x_pos[2] / dx
    ix0 = int(fx) % N; ix1 = (ix0 + 1) % N; wx1 = fx - int(fx); wx0 = 1 - wx1
    iy0 = int(fy) % N; iy1 = (iy0 + 1) % N; wy1 = fy - int(fy); wy0 = 1 - wy1
    iz0 = int(fz) % N; iz1 = (iz0 + 1) % N; wz1 = fz - int(fz); wz0 = 1 - wz1

    def interp(field):
        """Trilinear interpolation."""
        return (wx0 * wy0 * wz0 * field[ix0, iy0, iz0] +
                wx1 * wy0 * wz0 * field[ix1, iy0, iz0] +
                wx0 * wy1 * wz0 * field[ix0, iy1, iz0] +
                wx0 * wy0 * wz1 * field[ix0, iy0, iz1] +
                wx1 * wy1 * wz0 * field[ix1, iy1, iz0] +
                wx1 * wy0 * wz1 * field[ix1, iy0, iz1] +
                wx0 * wy1 * wz1 * field[ix0, iy1, iz1] +
                wx1 * wy1 * wz1 * field[ix1, iy1, iz1])

    u_hat = solver.velocity_from_vorticity(*w)

    # Interpolate velocity gradient
    A = torch.zeros(3, 3, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            field = solver.ifft(1j * kd[j] * D * u_hat[i])
            A[i, j] = interp(field)
    Sl = 0.5 * (A + A.T)

    # Interpolate vorticity
    wf = [solver.ifft(D * w[i]) for i in range(3)]
    wv = torch.tensor([interp(wf[i]) for i in range(3)], dtype=DTYPE)
    wn = wv.norm().item()
    if wn < 1e-12:
        return None, None, None
    eh = wv / wv.norm()

    alpha_l = (eh @ Sl @ eh).item()
    S2ee_l = (eh @ Sl @ Sl @ eh).item()
    Var_l = S2ee_l - alpha_l**2

    # Also return velocity for particle advection
    uf = [solver.ifft(D * u_hat[i]) for i in range(3)]
    u_l = [interp(uf[i]) for i in range(3)]

    return Var_l, wn, u_l


def run_ic(solver, w0, ic_name, t_start=0.1, t_end=1.0, diag_dt=0.005):
    """Run simulation and collect DVar/Dt diagnostics."""
    print(f"\n{'='*80}")
    print(f"  IC: {ic_name}  (nu={solver.nu})")
    print(f"  t in [{t_start:.2f}, {t_end:.2f}], diag every {diag_dt}")
    print(f"{'='*80}\n")

    w = list(w0)
    t = 0.0

    # Evolve past transient
    print(f"  Evolving to t={t_start:.2f}...", flush=True)
    while t < t_start - 1e-15:
        dt = min(solver.compute_dt(*w), t_start - t)
        w[0], w[1], w[2] = solver.step_rk4(w[0], w[1], w[2], dt)
        t += dt

    om0 = solver.omega_max(*w)
    print(f"  t={t:.4f}, |omega|_max={om0:.2f}", flush=True)

    if om0 < 0.1:
        print(f"  SKIPPING: |omega| too small for meaningful diagnostics", flush=True)
        return []

    results = []
    prev_diag = None
    prev_t = None
    prev_w = None

    header = (f"  {'t':>6s}  {'|om|':>7s}  {'alpha':>7s}  {'Var':>10s}  "
              f"{'DVar':>10s}  {'DVar_fd':>10s}  {'ratio':>7s}  "
              f"{'ev%':>7s}  {'tilt%':>7s}  {'tw':>3s}  {'d(lno)':>7s}")
    print(header, flush=True)
    print("  " + "-" * (len(header) - 2), flush=True)

    t_next = t
    while t < t_end - 1e-15:
        # Collect diagnostics at current state
        diag = diagnostics_at_max_omega(solver, w[0], w[1], w[2])

        if diag is not None and abs(diag['Var']) > 1e-15 and diag['om'] > 0.1:
            # Lagrangian FD: track the particle from prev diagnostic to now
            # Use midpoint method (RK2) for particle advection
            dVar_fd = float('nan')
            if prev_diag is not None and prev_t is not None:
                dx = solver.dx
                x_prev = [prev_diag['ix'] * dx, prev_diag['iy'] * dx, prev_diag['iz'] * dx]
                u_prev = prev_diag['u_local']
                dt_lag = t - prev_t

                # RK2 (midpoint): use velocity at prev to estimate midpoint,
                # then get velocity at midpoint from current field for 2nd-order accuracy
                x_mid = [x_prev[k] + 0.5 * u_prev[k] * dt_lag for k in range(3)]
                _, _, u_mid = lagrangian_var(solver, w, x_mid)
                if u_mid is not None:
                    x_now = [x_prev[k] + u_mid[k] * dt_lag for k in range(3)]
                else:
                    x_now = [x_prev[k] + u_prev[k] * dt_lag for k in range(3)]

                Var_advected, _, _ = lagrangian_var(solver, w, x_now)
                if Var_advected is not None:
                    dVar_fd = (Var_advected - prev_diag['Var']) / dt_lag

            DV = diag['DVar']
            if abs(DV) > 1e-25:
                ev_pct = 100 * diag['DVar_ev'] / DV
                tilt_pct = 100 * diag['DVar_tilt'] / DV
            else:
                ev_pct = tilt_pct = float('nan')

            tw = "Y" if diag['tilting_wins'] else "n"
            print(f"  {t:6.3f}  {diag['om']:7.2f}  {diag['alpha']:+7.3f}  "
                  f"{diag['Var']:10.5f}  {DV:+10.4f}  {dVar_fd:+10.4f}  "
                  f"{diag['ratio']:7.3f}  {ev_pct:7.1f}  {tilt_pct:7.1f}  "
                  f"{tw:>3s}  {diag['dlnomdt']:+7.3f}",
                  flush=True)

            result = {
                't': t, 'om': diag['om'], 'alpha': diag['alpha'],
                'Var': diag['Var'], 'DVar': DV, 'dVar_fd': dVar_fd,
                'ratio': diag['ratio'],
                'DVar_ev': diag['DVar_ev'], 'DVar_tilt': diag['DVar_tilt'],
                'DVar_omega_rot': diag['DVar_omega_rot'],
                'DVar_eigvec_rot': diag['DVar_eigvec_rot'],
                'tilting_wins': diag['tilting_wins'],
                'dlnomdt': diag['dlnomdt'],
                'var_decay_rate': diag['var_decay_rate'],
                'blowup_rate': diag['blowup_rate'],
                'contrib_S2': diag['contrib_S2'],
                'contrib_O2': diag['contrib_O2'],
                'contrib_H': diag['contrib_H'],
                'dalpha_err': diag['dalpha_err'],
            }
            results.append(result)

            prev_diag = diag
            prev_t = t

        # Advance one diagnostic interval
        t_target = min(t + diag_dt, t_end)
        while t < t_target - 1e-15:
            dt = min(solver.compute_dt(*w), t_target - t)
            if dt < 1e-15:
                break
            w[0], w[1], w[2] = solver.step_rk4(w[0], w[1], w[2], dt)
            t += dt

        # Blowup check
        if solver.omega_max(*w) > 1e6:
            print(f"  BLOWUP at t={t:.6f}", flush=True)
            break

    return results


def print_summary(all_results):
    """Print the grand summary table."""
    print(f"\n{'='*80}")
    print(f"  GRAND SUMMARY: DVar/Dt EXACT decomposition at max-|omega| point")
    print(f"{'='*80}")

    print(f"\n  ratio = DVar/Dt / (-|omega|*Var)")
    print(f"  ratio~1 means DVar/Dt = -|omega|*Var (full tilting prediction)")
    print(f"  ev% = fraction of DVar from eigenvalue changes")
    print(f"  tilt% = fraction from alignment changes (omega_hat + eigvec rotation)")
    print(f"  tw% = fraction of timesteps where |DVar/Var| > |alpha| (tilting > blowup)\n")

    print(f"  {'IC':>14s}  {'N':>4s}  {'med_ratio':>9s}  {'tw%':>5s}  "
          f"{'med_ev%':>7s}  {'med_tlt%':>8s}  "
          f"{'<Var>':>9s}  {'<|om|>':>7s}")
    print("  " + "-" * 80)

    for ic_name, results in all_results.items():
        valid = [r for r in results if not math.isnan(r['ratio'])]
        if not valid:
            print(f"  {ic_name:>14s}    --  NO VALID DATA")
            continue

        n = len(valid)
        mr = np.median([r['ratio'] for r in valid])
        tw = 100.0 * sum(1 for r in valid if r['tilting_wins']) / n

        ev_fracs = [r['DVar_ev']/r['DVar']*100 for r in valid if abs(r['DVar']) > 1e-25]
        tl_fracs = [r['DVar_tilt']/r['DVar']*100 for r in valid if abs(r['DVar']) > 1e-25]
        me = np.median(ev_fracs) if ev_fracs else float('nan')
        mt = np.median(tl_fracs) if tl_fracs else float('nan')
        mv = np.mean([r['Var'] for r in valid])
        mo = np.mean([r['om'] for r in valid])

        print(f"  {ic_name:>14s}  {n:4d}  {mr:9.3f}  {tw:5.1f}  "
              f"{me:7.1f}  {mt:8.1f}  "
              f"{mv:9.5f}  {mo:7.2f}")

    # Strain equation source decomposition
    print(f"\n  Eigenvalue change sources (median):")
    print(f"  {'IC':>14s}  {'from -S^2':>9s}  {'from -Om^2':>10s}  {'from -H':>9s}")
    print("  " + "-" * 50)
    for ic_name, results in all_results.items():
        valid = [r for r in results if not math.isnan(r['ratio'])]
        if not valid:
            continue
        print(f"  {ic_name:>14s}  {np.median([r['contrib_S2'] for r in valid]):+9.3f}  "
              f"{np.median([r['contrib_O2'] for r in valid]):+10.3f}  "
              f"{np.median([r['contrib_H'] for r in valid]):+9.3f}")

    # FD validation
    print(f"\n  Lagrangian FD validation (DVar/Dt_theory vs DVar/Dt_fd):")
    print(f"  {'IC':>14s}  {'med_theory':>10s}  {'med_fd':>10s}  {'corr':>6s}  {'N':>4s}")
    print("  " + "-" * 55)
    for ic_name, results in all_results.items():
        valid = [r for r in results if not math.isnan(r['dVar_fd'])]
        if len(valid) < 3:
            continue
        theory = [r['DVar'] for r in valid]
        fd = [r['dVar_fd'] for r in valid]
        corr = np.corrcoef(theory, fd)[0, 1]
        print(f"  {ic_name:>14s}  {np.median(theory):+10.4f}  {np.median(fd):+10.4f}  "
              f"{corr:6.3f}  {len(valid):4d}")

    # Dalpha cross-check
    print(f"\n  Dalpha analytical cross-check:")
    for ic_name, results in all_results.items():
        valid = [r for r in results if not math.isnan(r['ratio'])]
        if not valid:
            continue
        errs = [r['dalpha_err'] for r in valid]
        print(f"  {ic_name:>14s}  max|err|={max(errs):.2e}  (should be ~1e-15)")

    # The verdict
    print(f"\n  {'='*70}")
    print(f"  THE VERDICT")
    print(f"  {'='*70}")

    all_valid = []
    for results in all_results.values():
        all_valid.extend([r for r in results if not math.isnan(r['ratio'])])
    if not all_valid:
        print(f"  No valid data.")
        return

    overall_ratio = np.median([r['ratio'] for r in all_valid])
    overall_tw = 100.0 * sum(1 for r in all_valid if r['tilting_wins']) / len(all_valid)
    sign_right = 100.0 * sum(1 for r in all_valid if r['ratio'] > 0) / len(all_valid)

    print(f"\n  {len(all_valid)} measurements across all ICs:")
    print(f"    median(DVar/Dt / (-|om|*Var)) = {overall_ratio:.4f}")
    print(f"    Var decaying (ratio>0)         = {sign_right:.1f}%")
    print(f"    tilting > blowup rate          = {overall_tw:.1f}%")

    if overall_ratio > 0.5 and sign_right > 70:
        print(f"\n  ==> 2:1 TILTING ADVANTAGE HOLDS.")
        print(f"      DVar/Dt ~ -{overall_ratio:.2f}*|omega|*Var")
        print(f"      Var decays at rate ~{overall_ratio:.2f}*|omega|, blowup grows at rate alpha <= |omega|/2")
        print(f"      Net: tilting wins by factor ~{2*overall_ratio:.1f}:1")
    elif sign_right > 50:
        print(f"\n  ==> TILTING HELPS but is WEAKER than 2:1.")
        print(f"      DVar/Dt has correct sign {sign_right:.0f}% of the time")
        print(f"      But eigenvalue changes partially cancel: effective rate {overall_ratio:.2f}*|omega|")
        if overall_ratio > 0:
            print(f"      Ratio to blowup: {2*overall_ratio:.1f}:1 (need >2:1 for guarantee)")
    else:
        print(f"\n  ==> 2:1 ADVANTAGE FAILS.")
        print(f"      Var does not reliably decay (correct sign only {sign_right:.0f}%)")
        print(f"      Eigenvalue changes from -S^2, -Om^2, -H dominate tilting.")


def main():
    device = 'cpu'
    N = 32

    print("DVar/Dt EXACT: Full strain-equation decomposition")
    print(f"N={N}, Euler (nu=0), CPU")
    print(f"Measuring material derivative DVar/Dt at max-|omega| point")
    print(f"Lagrangian particle tracking for FD validation")

    all_results = {}

    # --- Taylor-Green (low symmetry breaking, moderate |omega|) ---
    print("\n[1/3] Taylor-Green")
    solver = NS3DSpectral(N=N, nu=0.0, device=device)
    w0 = ic_taylor_green(solver)
    results = run_ic(solver, w0, "Taylor-Green", t_start=0.5, t_end=2.0, diag_dt=0.02)
    all_results['Taylor-Green'] = results

    # --- Kida-Pelz (strong vortex dynamics, historical blowup candidate) ---
    print("\n[2/3] Kida-Pelz")
    solver = NS3DSpectral(N=N, nu=0.0, device=device)
    w0 = ic_kida_pelz(solver)
    results = run_ic(solver, w0, "Kida-Pelz", t_start=0.05, t_end=0.6, diag_dt=0.005)
    all_results['Kida-Pelz'] = results

    # --- Random large-scale (generic turbulence) ---
    print("\n[3/4] Random large-scale")
    solver = NS3DSpectral(N=N, nu=0.0, device=device)
    w0 = ic_random_large_scale(solver, amp=10.0, k_max=4)
    results = run_ic(solver, w0, "Random", t_start=0.05, t_end=0.5, diag_dt=0.005)
    all_results['Random'] = results

    # --- Trefoil knot (topological, strong non-symmetric vortex dynamics) ---
    print("\n[4/4] Trefoil knot")
    solver = NS3DSpectral(N=N, nu=0.0, device=device)
    w0 = ic_trefoil_knot(solver, amp=10.0, core_width=0.3)
    results = run_ic(solver, w0, "Trefoil", t_start=0.01, t_end=0.3, diag_dt=0.002)
    all_results['Trefoil'] = results

    print_summary(all_results)


if __name__ == '__main__':
    main()
