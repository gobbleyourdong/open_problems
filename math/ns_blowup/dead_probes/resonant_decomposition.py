"""
Resonant vs Non-Resonant Triad Decomposition

For the normal form approach, we need to split the enstrophy transfer
T_j = ∫ ω_j · F_j dx into:

  T_j = T_j^{res} + T_j^{non-res}

where:
- Non-resonant: triads where the sweeping phase k·u_{<j} is large (~ 2^j)
  → these oscillate fast and can be absorbed into the corrector B_j
- Resonant: triads where k·u_{<j} ≈ 0 (phase is stationary)
  → these need separate treatment

The SPLIT is determined by the "resonance function":
  Ω(k,p,q) = (k·u_{<j}) at the triad (k,p,q)

If |Ω| > λ (some threshold): non-resonant → absorbed by normal form
If |Ω| ≤ λ: resonant → remains as cubic remainder

KEY QUESTIONS:
1. What fraction of T_j is resonant?
2. Does the resonant fraction decrease with j?
3. Is the resonant part subcritical on its own?

Also validate at multiple resolutions (N=32, 64) and ICs (TG + random seeds).
"""
import numpy as np
import time

def run_resonant_decomposition(N=64, nu=1e-4, T_evolve=3.0, seed=None):
    L = 2*np.pi; dx = L/N
    k1d = np.fft.fftfreq(N, d=dx/(2*np.pi))
    kx,ky,kz = np.meshgrid(k1d,k1d,k1d, indexing='ij')
    ksq = kx**2+ky**2+kz**2; ksq[0,0,0] = 1.0; kmag = np.sqrt(ksq)
    ikx,iky,ikz = 1j*kx, 1j*ky, 1j*kz
    kmax = N//3
    D = ((np.abs(kx)<kmax)&(np.abs(ky)<kmax)&(np.abs(kz)<kmax)).astype(np.float64)
    ifft = lambda f: np.fft.ifftn(f*D).real
    fft = np.fft.fftn
    ik = [ikx, iky, ikz]

    # Shells
    max_shell = int(np.log2(kmax)) + 1
    shells = []
    for j in range(max_shell+1):
        m = ((kmag<2) if j==0 else ((kmag>=2**j)&(kmag<2**(j+1)))).astype(np.float64)*D
        shells.append((m, int(m.sum())))

    def ns_rhs(wh):
        wx_h,wy_h,wz_h = wh
        px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq;px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px
        ux,uy,uz=ifft(ux_h),ifft(uy_h),ifft(uz_h)
        wx,wy,wz=ifft(wx_h*D),ifft(wy_h*D),ifft(wz_h*D)
        gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
        gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
        gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
        sx=wx*gxx+wy*gxy+wz*gxz;sy=wx*gyx+wy*gyy+wz*gyz;sz=wx*gzx+wy*gzy+wz*gzz
        ax=ux*ifft(ikx*wx_h*D)+uy*ifft(iky*wx_h*D)+uz*ifft(ikz*wx_h*D)
        ay=ux*ifft(ikx*wy_h*D)+uy*ifft(iky*wy_h*D)+uz*ifft(ikz*wy_h*D)
        az=ux*ifft(ikx*wz_h*D)+uy*ifft(iky*wz_h*D)+uz*ifft(ikz*wz_h*D)
        return [D*fft(sx-ax)-nu*ksq*wx_h, D*fft(sy-ay)-nu*ksq*wy_h, D*fft(sz-az)-nu*ksq*wz_h]

    def rk4(wh, dt):
        k1=ns_rhs(wh);w2=[wh[c]+.5*dt*k1[c] for c in range(3)]
        k2=ns_rhs(w2);w3=[wh[c]+.5*dt*k2[c] for c in range(3)]
        k3=ns_rhs(w3);w4=[wh[c]+dt*k3[c] for c in range(3)]
        k4=ns_rhs(w4)
        return [wh[c]+dt/6*(k1[c]+2*k2[c]+2*k3[c]+k4[c]) for c in range(3)]

    # IC
    x = np.linspace(0, L-dx, N)
    X,Y,Z = np.meshgrid(x,x,x, indexing='ij')

    if seed is None:
        # TG vortex
        ux0 = np.cos(X)*np.sin(Y)*np.cos(Z)
        uy0 = -np.sin(X)*np.cos(Y)*np.cos(Z)
        uz0 = np.zeros_like(X)
        ic_name = "TG"
    else:
        # Random curl noise
        np.random.seed(seed)
        mag = 10.0/(ksq+1); mag[0,0,0] = 0
        ic_mask = (ksq <= 64).astype(np.float64)
        Ax = mag*ic_mask*(np.random.randn(N,N,N)+1j*np.random.randn(N,N,N))
        Ay = mag*ic_mask*(np.random.randn(N,N,N)+1j*np.random.randn(N,N,N))
        Az = mag*ic_mask*(np.random.randn(N,N,N)+1j*np.random.randn(N,N,N))
        ux_h = D*(iky*Az-ikz*Ay); uy_h = D*(ikz*Ax-ikx*Az); uz_h = D*(ikx*Ay-iky*Ax)
        ux0 = ifft(ux_h); uy0 = ifft(uy_h); uz0 = ifft(uz_h)
        ic_name = f"random(seed={seed})"

    ux_h = D*fft(ux0); uy_h = D*fft(uy0); uz_h = D*fft(uz0)
    wh = [D*(iky*uz_h-ikz*uy_h), D*(ikz*ux_h-ikx*uz_h), D*(ikx*uy_h-iky*ux_h)]

    # Evolve to T_evolve
    dt = 0.002; n_steps = int(T_evolve/dt)
    print(f"  Evolving {ic_name} N={N} to t={T_evolve}...", end='', flush=True)
    t0 = time.time()
    for step in range(n_steps):
        wh = rk4(wh, dt)
    print(f" [{time.time()-t0:.0f}s]", flush=True)

    # Now decompose the transfer at this snapshot
    wx_h, wy_h, wz_h = wh

    # Get velocity
    px=wx_h/ksq;py=wy_h/ksq;pz=wz_h/ksq;px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
    ux_h=iky*pz-ikz*py;uy_h=ikz*px-ikx*pz;uz_h=ikx*py-iky*px

    results = {}

    for j in range(1, max_shell+1):
        mj, nm = shells[j]
        if nm < 10:
            continue

        # Shell j vorticity and velocity
        wjh = [c*mj for c in [wx_h, wy_h, wz_h]]
        ujh_j = [c*mj for c in [ux_h, uy_h, uz_h]]
        wj = [ifft(c) for c in wjh]
        uj = [ifft(c) for c in ujh_j]

        # Low-frequency velocity u_{<j} (for sweeping frequency)
        low_mask = (kmag < 2**j).astype(np.float64) * D
        u_low = [ifft(c*low_mask) for c in [ux_h, uy_h, uz_h]]

        # The "resonance function" Ω_k = k · u_{<j}
        # In physical space, this becomes the local sweeping speed
        # For each grid point x: Ω(x) = |∇(u_{<j} · x-hat)| at scale 2^j
        # Simpler: Ω ~ 2^j × |u_{<j}|
        u_low_mag = np.sqrt(sum(u_low[c]**2 for c in range(3)))
        omega_sweep = 2**j * u_low_mag  # local sweeping frequency

        # Compute the FULL nonlinear RHS restricted to shell j
        # F_j = [ω·∇u - u·∇ω]_j
        ux_full = ifft(ux_h); uy_full = ifft(uy_h); uz_full = ifft(uz_h)
        wx_full = ifft(wx_h*D); wy_full = ifft(wy_h*D); wz_full = ifft(wz_h*D)

        # Stretching ω·∇u
        gxx=ifft(ikx*ux_h*D);gxy=ifft(iky*ux_h*D);gxz=ifft(ikz*ux_h*D)
        gyx=ifft(ikx*uy_h*D);gyy=ifft(iky*uy_h*D);gyz=ifft(ikz*uy_h*D)
        gzx=ifft(ikx*uz_h*D);gzy=ifft(iky*uz_h*D);gzz=ifft(ikz*uz_h*D)
        sx=wx_full*gxx+wy_full*gxy+wz_full*gxz
        sy=wx_full*gyx+wy_full*gyy+wz_full*gyz
        sz=wx_full*gzx+wy_full*gzy+wz_full*gzz
        # Advection u·∇ω
        ax=ux_full*ifft(ikx*wx_h*D)+uy_full*ifft(iky*wx_h*D)+uz_full*ifft(ikz*wx_h*D)
        ay=ux_full*ifft(ikx*wy_h*D)+uy_full*ifft(iky*wy_h*D)+uz_full*ifft(ikz*wy_h*D)
        az=ux_full*ifft(ikx*wz_h*D)+uy_full*ifft(iky*wz_h*D)+uz_full*ifft(ikz*wz_h*D)

        # Full RHS projected to shell j
        Fj = [ifft(D*mj*fft(sx-ax)), ifft(D*mj*fft(sy-ay)), ifft(D*mj*fft(sz-az))]

        # The transfer T_j = ∫ ω_j · F_j dx
        T_j_field = sum(wj[c]*Fj[c] for c in range(3))  # pointwise ω·F
        T_j = T_j_field.sum() * dx**3

        # Now split into resonant and non-resonant REGIONS
        # Resonant: where the sweeping frequency is SMALL (|Ω| < threshold)
        # Non-resonant: where Ω is large (|Ω| ≥ threshold)
        #
        # The threshold λ should be comparable to the eddy turnover: λ ~ 2^j × U_rms
        U_rms = np.sqrt(np.mean(u_low_mag**2))
        lambda_threshold = 0.5 * 2**j * U_rms  # half the typical sweeping freq

        resonant_mask = (omega_sweep < lambda_threshold)
        nonres_mask = ~resonant_mask

        T_resonant = (T_j_field * resonant_mask).sum() * dx**3
        T_nonresonant = (T_j_field * nonres_mask).sum() * dx**3

        # Fraction of volume that is resonant
        frac_resonant = resonant_mask.sum() / resonant_mask.size

        # Also measure: what is the RMS sweeping frequency?
        omega_rms = np.sqrt(np.mean(omega_sweep**2))
        omega_max = omega_sweep.max()

        results[j] = {
            'nm': nm, 'T_total': T_j,
            'T_resonant': T_resonant, 'T_nonresonant': T_nonresonant,
            'frac_res_volume': frac_resonant,
            'frac_res_transfer': abs(T_resonant)/(abs(T_j)+1e-30),
            'omega_rms': omega_rms, 'omega_max': omega_max,
            'U_rms': U_rms, 'lambda': lambda_threshold,
        }

    return results, ic_name


def main():
    print("RESONANT vs NON-RESONANT TRIAD DECOMPOSITION")
    print("="*65)
    print()

    all_results = {}

    # Test at N=64 with TG and 3 random seeds
    for ic_config in [('TG', None), ('rand0', 0), ('rand1', 1), ('rand2', 42)]:
        label, seed = ic_config
        results, ic_name = run_resonant_decomposition(N=64, nu=1e-4, T_evolve=3.0, seed=seed)
        all_results[label] = results

        print(f"\n  {ic_name} at t=3:")
        print(f"  {'j':>3} {'N_modes':>8} {'T_total':>12} {'T_res':>12} {'T_nonres':>12} "
              f"{'%res_vol':>9} {'%res_T':>8} {'Ω_rms':>8}")
        for j in sorted(results.keys()):
            r = results[j]
            print(f"  {j:>3} {r['nm']:>8} {r['T_total']:>+12.3e} {r['T_resonant']:>+12.3e} "
                  f"{r['T_nonresonant']:>+12.3e} {r['frac_res_volume']*100:>8.1f}% "
                  f"{r['frac_res_transfer']*100:>7.1f}% {r['omega_rms']:>8.1f}")

    # Also run at N=32 for resolution check
    print(f"\n{'='*65}")
    print("RESOLUTION CHECK: N=32 TG")
    results_32, _ = run_resonant_decomposition(N=32, nu=1e-4, T_evolve=3.0, seed=None)
    print(f"\n  TG N=32 at t=3:")
    print(f"  {'j':>3} {'N_modes':>8} {'%res_vol':>9} {'%res_T':>8} {'Ω_rms':>8}")
    for j in sorted(results_32.keys()):
        r = results_32[j]
        print(f"  {j:>3} {r['nm']:>8} {r['frac_res_volume']*100:>8.1f}% "
              f"{r['frac_res_transfer']*100:>7.1f}% {r['omega_rms']:>8.1f}")

    # Summary
    print(f"\n{'='*65}")
    print("SUMMARY")
    print(f"{'='*65}")
    print()

    # Key question: does the resonant fraction decrease with j?
    print("Resonant fraction of transfer (% of |T_j| in resonant region):")
    for label in all_results:
        res = all_results[label]
        fracs = [(j, res[j]['frac_res_transfer']) for j in sorted(res.keys())]
        print(f"  {label:>6}: " + "  ".join(f"j={j}:{f*100:.1f}%" for j,f in fracs))

    print()
    print("KEY: If resonant fraction DECREASES with j → normal form works")
    print("     If resonant fraction is CONSTANT → normal form insufficient")


if __name__ == '__main__':
    main()
