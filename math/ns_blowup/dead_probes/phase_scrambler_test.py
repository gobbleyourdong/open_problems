"""
Phase Scrambler Test — Is the pressure Hessian the mechanism
that forces phase decorrelation at high frequencies?

THE EXPERIMENT:
1. Start with a developed NS field (TG at t=3, peak stretching)
2. Measure θ(j) = intra-shell transfer ratio (our phase coherence metric)
3. Evolve for Δt with FULL NS equations → measure θ_after
4. Evolve for Δt WITHOUT pressure (just stretching + viscosity) → measure θ_nopressure
5. Evolve for Δt WITHOUT stretching (just pressure + viscosity) → measure θ_nostretch

If pressure SCRAMBLES phases: θ_after << θ_nopressure
If stretching ALIGNS phases: θ_nostretch << θ_after

Also measure the RATE of phase scrambling:
- dθ/dt from pressure term alone
- dθ/dt from stretching term alone
- Net dθ/dt

This runs on CPU (numpy). ~15 min for N=32.
"""
import numpy as np
import time

def run_phase_scrambler(N=32, nu=1e-4):
    L = 2*np.pi; dx = L/N
    k1d = np.fft.fftfreq(N, d=dx/(2*np.pi))
    kx,ky,kz = np.meshgrid(k1d,k1d,k1d,indexing='ij')
    ksq = kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    kmag = np.sqrt(ksq)
    ikx,iky,ikz = 1j*kx,1j*ky,1j*kz
    kmax = N//3
    D = ((np.abs(kx)<kmax)&(np.abs(ky)<kmax)&(np.abs(kz)<kmax)).astype(np.float64)

    ifft = lambda f: np.fft.ifftn(f*D).real
    fft = np.fft.fftn
    ik = [ikx,iky,ikz]

    # Shell masks
    max_shell = int(np.log2(kmax)) + 1
    shell_masks = []
    for j in range(max_shell+1):
        if j==0: m=(kmag<2).astype(np.float64)*D
        else: m=((kmag>=2**j)&(kmag<2**(j+1))).astype(np.float64)*D
        shell_masks.append(m)

    def compute_theta(wh):
        """Compute θ(j) for each shell."""
        wx_h,wy_h,wz_h = wh
        thetas = []
        for j in range(len(shell_masks)):
            mj = shell_masks[j]
            nm = mj.sum()
            if nm < 3:
                thetas.append(0.0)
                continue
            # Filter vorticity to shell j
            wjh = [c*mj for c in [wx_h,wy_h,wz_h]]
            # Velocity from shell j
            pj = [c/ksq for c in wjh]
            for p in pj: p[0,0,0]=0
            ujh = [iky*pj[2]-ikz*pj[1], ikz*pj[0]-ikx*pj[2], ikx*pj[1]-iky*pj[0]]
            # Physical space
            wj = [ifft(c) for c in wjh]
            # Strain
            Sj = np.zeros((3,3,N,N,N))
            for i in range(3):
                for l in range(3):
                    Sj[i,l] = ifft(ik[l]*ujh[i]*D)
            Sj = 0.5*(Sj+Sj.transpose(1,0,2,3,4))
            # T(j,j)
            wSw = sum(wj[i]*Sj[i,l]*wj[l] for i in range(3) for l in range(3))
            T_jj = wSw.sum()*dx**3
            # Norms
            E_j = sum((wj[c]**2).sum() for c in range(3))*dx**3
            Sf = Sj.reshape(3,3,-1).transpose(2,0,1)
            eigs = np.linalg.eigvalsh(Sf)
            S_inf = np.max(np.abs(eigs))
            theta = abs(T_jj)/(E_j*S_inf+1e-30)
            thetas.append(theta)
        return thetas

    def ns_rhs_full(wh):
        """Full NS RHS: stretching - advection + viscosity."""
        wx_h,wy_h,wz_h = wh
        px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
        ux,uy,uz=ifft(ux_h),ifft(uy_h),ifft(uz_h)
        wx,wy,wz=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
        # Stretching: ω·∇u
        gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
        gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
        gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
        sx=wx*gxx+wy*gxy+wz*gxz
        sy=wx*gyx+wy*gyy+wz*gyz
        sz=wx*gzx+wy*gzy+wz*gzz
        # Advection: u·∇ω
        ax=ux*ifft(ikx*wx_h*D)+uy*ifft(iky*wx_h*D)+uz*ifft(ikz*wx_h*D)
        ay=ux*ifft(ikx*wy_h*D)+uy*ifft(iky*wy_h*D)+uz*ifft(ikz*wy_h*D)
        az=ux*ifft(ikx*wz_h*D)+uy*ifft(iky*wz_h*D)+uz*ifft(ikz*wz_h*D)
        rhs_x = D*fft(sx-ax) - nu*ksq*wx_h
        rhs_y = D*fft(sy-ay) - nu*ksq*wy_h
        rhs_z = D*fft(sz-az) - nu*ksq*wz_h
        return [rhs_x, rhs_y, rhs_z]

    def ns_rhs_no_pressure(wh):
        """NS without pressure projection — keep the k-parallel component.

        Normal NS: dω/dt = curl(P(u×ω)) where P is Leray projector
        Without pressure: dω/dt = curl(u×ω) — no projection

        Actually the vorticity eq ∂ω/∂t + (u·∇)ω = (ω·∇)u + ν∆ω
        doesn't explicitly contain pressure. Pressure enters through
        the velocity field u via the Biot-Savart law, which IS a projection.

        To remove pressure: use a DIFFERENT velocity recovery.
        Instead of u = BS(ω) (which includes pressure projection),
        use u_noproj that includes the irrotational part.

        But wait — for incompressible flow, u = BS(ω) is the UNIQUE
        velocity. There's no "without pressure" version in vorticity form.

        The pressure enters the MOMENTUM equation: Du/Dt = -∇p + ν∆u
        In vorticity form: Dω/Dt = ω·∇u + ν∆ω
        The pressure is IMPLICITLY included through the div-free constraint
        on u (which is enforced by BS).

        A better experiment: compare to a COMPRESSIBLE evolution where
        ∇·u ≠ 0, so there's no pressure constraint. In compressible flow,
        the phases are NOT scrambled by pressure.
        """
        # For the "no pressure" test, let's use a simpler approach:
        # Just the stretching term ω·∇u without the advection term u·∇ω.
        # The advection is the TRANSPORT (conservative), and stretching
        # is the PRODUCTION. Without advection, phases evolve only by
        # stretching (which tends to align them).
        wx_h,wy_h,wz_h = wh
        px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
        wx,wy,wz=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
        # Stretching only: ω·∇u
        gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
        gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
        gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
        sx=wx*gxx+wy*gxy+wz*gxz
        sy=wx*gyx+wy*gyy+wz*gyz
        sz=wx*gzx+wy*gzy+wz*gzz
        rhs_x = D*fft(sx) - nu*ksq*wx_h
        rhs_y = D*fft(sy) - nu*ksq*wy_h
        rhs_z = D*fft(sz) - nu*ksq*wz_h
        return [rhs_x, rhs_y, rhs_z]

    def ns_rhs_advection_only(wh):
        """Just the advection (transport) term — no stretching."""
        wx_h,wy_h,wz_h = wh
        px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
        ux,uy,uz=ifft(ux_h),ifft(uy_h),ifft(uz_h)
        wx_r,wy_r,wz_r=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
        # Advection: -u·∇ω
        ax=ux*ifft(ikx*wx_h*D)+uy*ifft(iky*wx_h*D)+uz*ifft(ikz*wx_h*D)
        ay=ux*ifft(ikx*wy_h*D)+uy*ifft(iky*wy_h*D)+uz*ifft(ikz*wy_h*D)
        az=ux*ifft(ikx*wz_h*D)+uy*ifft(iky*wz_h*D)+uz*ifft(ikz*wz_h*D)
        rhs_x = -D*fft(ax) - nu*ksq*wx_h
        rhs_y = -D*fft(ay) - nu*ksq*wy_h
        rhs_z = -D*fft(az) - nu*ksq*wz_h
        return [rhs_x, rhs_y, rhs_z]

    def euler_step(wh, rhs_func, dt):
        rhs = rhs_func(wh)
        return [wh[c] + dt*rhs[c] for c in range(3)]

    def rk4_step(wh, rhs_func, dt):
        k1 = rhs_func(wh)
        w2 = [wh[c]+0.5*dt*k1[c] for c in range(3)]
        k2 = rhs_func(w2)
        w3 = [wh[c]+0.5*dt*k2[c] for c in range(3)]
        k3 = rhs_func(w3)
        w4 = [wh[c]+dt*k3[c] for c in range(3)]
        k4 = rhs_func(w4)
        return [wh[c]+dt/6*(k1[c]+2*k2[c]+2*k3[c]+k4[c]) for c in range(3)]

    # === SETUP: TG vortex evolved to t=3 (peak stretching) ===
    print(f"PHASE SCRAMBLER TEST — N={N}, ν={nu}")
    print("="*60)

    x = np.linspace(0, L-dx, N)
    X,Y,Z = np.meshgrid(x,x,x,indexing='ij')
    ux = np.cos(X)*np.sin(Y)*np.cos(Z)
    uy = -np.sin(X)*np.cos(Y)*np.cos(Z)
    uz = np.zeros_like(X)
    ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
    wx_h=D*(iky*uz_h-ikz*uy_h)
    wy_h=D*(ikz*ux_h-ikx*uz_h)
    wz_h=D*(ikx*uy_h-iky*ux_h)

    # Evolve to t=3 with full NS
    dt = 0.002; n_steps = 1500
    print(f"Evolving TG to t=3 ({n_steps} steps)...", flush=True)
    t0 = time.time()
    wh = [wx_h, wy_h, wz_h]
    for step in range(n_steps):
        wh = rk4_step(wh, ns_rhs_full, dt)
    print(f"Done [{time.time()-t0:.1f}s]", flush=True)

    # Save the t=3 state
    wh_t3 = [c.copy() for c in wh]

    # Measure θ at t=3
    theta_t3 = compute_theta(wh_t3)
    print(f"\nθ(j) at t=3 (baseline):")
    for j, th in enumerate(theta_t3):
        nm = int(shell_masks[j].sum())
        if nm > 2:
            print(f"  j={j}: θ={th:.6f} (N_modes={nm})")

    # === THE EXPERIMENT ===
    # Evolve from t=3 for a short time with different dynamics
    delta_t = 0.1  # short evolution
    n_short = int(delta_t / dt)

    print(f"\nEvolving from t=3 for Δt={delta_t} ({n_short} steps)...")

    # 1. Full NS
    wh_full = [c.copy() for c in wh_t3]
    for step in range(n_short):
        wh_full = rk4_step(wh_full, ns_rhs_full, dt)
    theta_full = compute_theta(wh_full)

    # 2. Stretching only (no advection — removes the transport/pressure effect)
    wh_stretch = [c.copy() for c in wh_t3]
    for step in range(n_short):
        wh_stretch = rk4_step(wh_stretch, ns_rhs_no_pressure, dt)
    theta_stretch = compute_theta(wh_stretch)

    # 3. Advection only (no stretching — pure transport by pressure-driven flow)
    wh_advect = [c.copy() for c in wh_t3]
    for step in range(n_short):
        wh_advect = rk4_step(wh_advect, ns_rhs_advection_only, dt)
    theta_advect = compute_theta(wh_advect)

    # 4. Viscosity only (no nonlinear terms)
    wh_visc = [c.copy() for c in wh_t3]
    for step in range(n_short):
        wh_visc = [c * np.exp(-nu*ksq*dt) for c in wh_visc]  # exact viscous decay
    theta_visc = compute_theta(wh_visc)

    print(f"\n{'='*60}")
    print(f"RESULTS: θ(j) after Δt={delta_t} from t=3")
    print(f"{'='*60}")
    print(f"{'j':>3} {'θ_baseline':>12} {'θ_fullNS':>12} {'θ_stretch':>12} {'θ_advect':>12} {'θ_visc':>12}")

    for j in range(len(theta_t3)):
        nm = int(shell_masks[j].sum())
        if nm < 3: continue
        print(f"{j:>3} {theta_t3[j]:>12.6f} {theta_full[j]:>12.6f} "
              f"{theta_stretch[j]:>12.6f} {theta_advect[j]:>12.6f} {theta_visc[j]:>12.6f}")

    print(f"\n{'='*60}")
    print("INTERPRETATION:")
    print("  If θ_stretch > θ_fullNS: advection/pressure REDUCES coherence")
    print("  If θ_advect < θ_baseline: advection alone SCRAMBLES phases")
    print("  If θ_stretch > θ_baseline: stretching INCREASES coherence")
    print(f"{'='*60}")

    for j in range(1, min(4, len(theta_t3))):
        nm = int(shell_masks[j].sum())
        if nm < 3: continue
        stretch_effect = (theta_stretch[j] - theta_t3[j]) / (theta_t3[j] + 1e-30)
        advect_effect = (theta_advect[j] - theta_t3[j]) / (theta_t3[j] + 1e-30)
        full_effect = (theta_full[j] - theta_t3[j]) / (theta_t3[j] + 1e-30)

        print(f"\n  Shell j={j} (N_modes={nm}):")
        print(f"    Stretching only: θ changes by {stretch_effect*100:+.1f}%"
              f" {'(ALIGNS)' if stretch_effect > 0.05 else '(neutral)' if abs(stretch_effect) < 0.05 else '(SCRAMBLES)'}")
        print(f"    Advection only:  θ changes by {advect_effect*100:+.1f}%"
              f" {'(ALIGNS)' if advect_effect > 0.05 else '(neutral)' if abs(advect_effect) < 0.05 else '(SCRAMBLES)'}")
        print(f"    Full NS:         θ changes by {full_effect*100:+.1f}%"
              f" {'(ALIGNS)' if full_effect > 0.05 else '(neutral)' if abs(full_effect) < 0.05 else '(SCRAMBLES)'}")

    return theta_t3, theta_full, theta_stretch, theta_advect, theta_visc


if __name__ == '__main__':
    run_phase_scrambler(N=32, nu=1e-4)
