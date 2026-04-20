"""
Test the [S, Ω] commutator's role in rotating e₃ toward ω.

The strain evolution: dS/dt = -S² + [S, Ω] + H + ν·ΔS + advection
The [S, Ω] term rotates strain eigenvectors.

Question: does [S, Ω] specifically rotate e₃ toward ω?
And is it stronger than the pressure opposition?

Decompose de₃/dt into contributions from each term.
"""
import torch
import numpy as np
import math

DTYPE = torch.float64
pi = math.pi


class NS3D:
    def __init__(self, N=32, nu=0.0):
        self.N=N; self.nu=nu; self.Lx=2*pi
        dx=self.Lx/N
        x=torch.linspace(0,self.Lx-dx,N,dtype=DTYPE)
        self.X,self.Y,self.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        self.kx,self.ky,self.kz=torch.meshgrid(k,k,k,indexing='ij')
        self.ksq=self.kx**2+self.ky**2+self.kz**2; self.ksq[0,0,0]=1
        self.D=((self.kx.abs()<N//3)&(self.ky.abs()<N//3)&(self.kz.abs()<N//3)).to(DTYPE)

    def fft(s,f): return torch.fft.fftn(f)
    def ifft(s,f): return torch.fft.ifftn(f).real
    def curl(s,a,b,c):
        I=1j; return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq; p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j; return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D; u=s.vel(*w)
        f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]): f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c): return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        return tuple(s.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)]; return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()


def compute_strain_rhs_terms(solver, w):
    """
    Compute individual terms of dS/dt at each grid point:
    1. -S² (self-interaction)
    2. [S, Ω] = SΩ - ΩS (commutator)
    3. H (pressure Hessian, from full Poisson)
    4. Vorticity contribution: -(1/4)(ωω^T - |ω|²I/3) [this is part of the full equation]

    The full strain equation (Euler, no viscosity, no advection at a max):
    dS/dt = -S² - (1/4)WW^T + (1/4)|ω|²I/3 + H
    where W = antisymmetric part of A, H = pressure Hessian

    Actually the Lagrangian strain evolution is:
    DS/Dt = -S² - Ω² + H_sym
    where Ω² = ΩΩ^T = -(1/4)(ωω^T - |ω|²I) [note: Ω² is symmetric!]
    and H_sym is the symmetric part of H.

    So: DS/Dt = -S² + (1/4)(ωω^T - |ω|²I) + H
    The (1/4)(ωω^T - |ω|²I) term is the vorticity contribution.
    """
    D = solver.D; N = solver.N
    kd = [solver.kx, solver.ky, solver.kz]

    # Velocity and gradient
    u = solver.vel(*w)
    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            A[i,j] = solver.ifft(1j * kd[j] * D * u[i])

    S = 0.5 * (A + A.transpose(0, 1))
    Omega = 0.5 * (A - A.transpose(0, 1))

    # Vorticity
    wf = [solver.ifft(D * w[i]) for i in range(3)]
    om_mag = (wf[0]**2 + wf[1]**2 + wf[2]**2).sqrt()

    # -S²
    neg_S2 = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                neg_S2[i,j] -= S[i,k] * S[k,j]

    # -Ω² = ΩΩ^T (note: Ω is antisymmetric, so Ω^T = -Ω, hence -Ω² = Ω(-Ω) = -ΩΩ... wait)
    # Ω² means Ω_ik Ω_kj. Since Ω_kj = -Ω_jk:
    # Ω_ik Ω_kj = -Ω_ik Ω_jk = -(Ω^T Ω)_ij
    # So Ω² = -Ω^T Ω (not symmetric in general... actually it IS symmetric)
    # (Ω²)^T = (Ω²)_ji = Ω_jk Ω_ki = Ω_jk (-Ω_ik) = -Ω_jk Ω_ik
    # Hmm, need to be careful.
    # Actually Ω_ij = (A_ij - A_ji)/2. Ω_ij Ω_jk = [(A-A^T)/2]_ij [(A-A^T)/2]_jk
    # This IS symmetric (product of antisymmetric matrices is symmetric).

    neg_Omega2 = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                neg_Omega2[i,j] -= Omega[i,k] * Omega[k,j]

    # [S, Ω] = SΩ - ΩS
    comm = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                comm[i,j] += S[i,k] * Omega[k,j] - Omega[i,k] * S[k,j]

    # Pressure Hessian (full, from Poisson)
    source = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            source -= A[i,j] * A[j,i]
    source_h = solver.fft(source)
    p_hat = -source_h / solver.ksq; p_hat[0,0,0] = 0
    H = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H[i,j] = solver.ifft(-kd[i] * kd[j] * p_hat)

    return S, Omega, neg_S2, neg_Omega2, comm, H, wf, om_mag


def analyze_at_high_omega(S, Omega, neg_S2, neg_Omega2, comm, H, wf, om_mag,
                          percentile=0.90, n_sample=500):
    """
    At high-|ω| points, compute how each term in dS/dt
    affects the angle between e₃ and ω.

    The rate of change of cos²(ω̂, e₃) from a perturbation δS:
    If δS rotates e₃ by angle δθ, then δ(cos²) ≈ -2cos·sin·δθ.

    More precisely: the contribution of a strain perturbation δS to
    the rotation of eigenvector e₃ is given by perturbation theory:
    δe₃ = Σ_{i≠3} [e_i^T δS e₃ / (λ₃ - λ_i)] e_i

    The change in c₃ = (ω̂·e₃)²:
    δc₃ = 2(ω̂·e₃)(ω̂·δe₃) = 2(ω̂·e₃) Σ_{i≠3} [(ω̂·e_i)(e_i^T δS e₃)] / (λ₃-λ_i)
    """
    N = S.shape[2]
    thr = torch.quantile(om_mag.flatten(), percentile)
    if thr < 1e-10:
        return None

    idx = (om_mag > thr).nonzero(as_tuple=False)
    n = min(len(idx), n_sample)
    perm = torch.randperm(len(idx))[:n]
    pts = idx[perm]

    results = {'dc3_S2': [], 'dc3_Omega2': [], 'dc3_comm': [], 'dc3_H': [],
               'dc3_total': [], 'c3': [], 'c1': [], 'alpha': []}

    for pt in pts:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        Sl = S[:,:,ix,iy,iz]
        ev, ec = torch.linalg.eigh(Sl)
        # ev sorted ascending: λ₃ (most compressive), λ₂, λ₁ (most stretching)
        lam = ev.clone()
        e3 = ec[:, 0].clone()
        e2 = ec[:, 1].clone()
        e1 = ec[:, 2].clone()

        wv = torch.tensor([wf[i][ix,iy,iz] for i in range(3)], dtype=DTYPE)
        wn = wv.norm()
        if wn < 1e-12: continue
        eh = wv / wn

        c3 = (eh @ e3).item()**2
        c1 = (eh @ e1).item()**2
        alpha_val = sum(lam[j].item() * (eh @ ec[:,j]).item()**2 for j in range(3))

        # For each perturbation term δS, compute δc₃ via perturbation theory
        terms = {
            'S2': neg_S2[:,:,ix,iy,iz],
            'Omega2': neg_Omega2[:,:,ix,iy,iz],
            'comm': comm[:,:,ix,iy,iz],
            'H': H[:,:,ix,iy,iz],
        }

        for name, dS in terms.items():
            # Perturbation: δe₃ = Σ_{i≠3} [e_i^T dS e₃ / (λ₃-λ_i)] e_i
            dc3 = 0.0
            for i_idx, (e_i, lam_i) in enumerate([(e1, lam[2]), (e2, lam[1])]):
                lam_diff = lam[0].item() - lam_i.item()
                if abs(lam_diff) < 1e-12:
                    continue  # degenerate eigenvalues
                coupling = (e_i @ dS @ e3).item()
                dc3 += 2 * (eh @ e3).item() * (eh @ e_i).item() * coupling / lam_diff

            results[f'dc3_{name}'].append(dc3)

        # Total
        dS_total = neg_S2[:,:,ix,iy,iz] + neg_Omega2[:,:,ix,iy,iz] + H[:,:,ix,iy,iz]
        dc3_total = 0.0
        for i_idx, (e_i, lam_i) in enumerate([(e1, lam[2]), (e2, lam[1])]):
            lam_diff = lam[0].item() - lam_i.item()
            if abs(lam_diff) < 1e-12:
                continue
            coupling = (e_i @ dS_total @ e3).item()
            dc3_total += 2 * (eh @ e3).item() * (eh @ e_i).item() * coupling / lam_diff

        results['dc3_total'].append(dc3_total)
        results['c3'].append(c3)
        results['c1'].append(c1)
        results['alpha'].append(alpha_val)

    for k in results:
        results[k] = np.array(results[k])
    return results


def main():
    N = 32; dt = 2e-4; n_steps = 500  # evolve to t=0.1

    print("=" * 70, flush=True)
    print("[S, Ω] COMMUTATOR TEST: which term rotates e₃ toward ω?", flush=True)
    print("=" * 70, flush=True)

    for ic_name in ['TG', 'KP']:
        s = NS3D(N, 0.0)
        X, Y, Z = s.X, s.Y, s.Z
        if ic_name == 'TG':
            ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
            uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
            uz = torch.zeros_like(X)
        else:
            ux = torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z)-torch.cos(Y)*torch.cos(3*Z))
            uy = torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X)-torch.cos(Z)*torch.cos(3*X))
            uz = torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y)-torch.cos(X)*torch.cos(3*Y))

        w = s.curl(s.fft(ux), s.fft(uy), s.fft(uz))

        print(f"\n--- {ic_name}, Euler ---", flush=True)

        t = 0.0
        for epoch in range(6):
            # Evolve
            for _ in range(100 if epoch > 0 else 200):
                w = s.step(w, dt)
                t += dt

            # Compute all terms
            S, Omega, nS2, nO2, comm, H, wf, om = compute_strain_rhs_terms(s, w)
            r = analyze_at_high_omega(S, Omega, nS2, nO2, comm, H, wf, om)

            if r is None or len(r['c3']) == 0:
                print(f"  t={t:.3f}: insufficient data", flush=True)
                continue

            # Note: -Ω² is the vorticity contribution, [S,Ω] is the commutator
            # Actually, let me reconsider the strain equation.
            # The full equation is: DS/Dt = -S² - Ω² + H_sym
            # where -Ω² = (1/4)(ωω^T - |ω|²I) (this is NOT the commutator)
            # The commutator [S,Ω] = SΩ - ΩS does NOT appear in the symmetric strain eq.
            # Wait, it does!
            #
            # From A = S + Ω:
            # dA/dt + A² + H = 0  (Euler, material derivative)
            # A² = S² + SΩ + ΩS + Ω²
            # (A²)_sym = S² + (SΩ+ΩS)_sym + Ω²
            # But (SΩ+ΩS)_sym = SΩ + (SΩ)^T = SΩ + Ω^TS^T = SΩ - ΩS = [S,Ω]
            # Wait: (SΩ)_ij = S_ik Ω_kj. ((SΩ)^T)_ij = (SΩ)_ji = S_jk Ω_ki = -S_jk Ω_ik
            # Hmm... (SΩ + ΩS)_ij = S_ik Ω_kj + Ω_ik S_kj
            # Transpose: (SΩ + ΩS)_ji = S_jk Ω_ki + Ω_jk S_ki = -S_jk Ω_ik - Ω_jk S_ik
            # ... this is getting confusing. Let me just note:
            # SΩ + ΩS is the ANTISYMMETRIC part of A² (since S² and Ω² are symmetric).
            # So the symmetric part of A² is S² + Ω², and the antisymmetric part is SΩ + ΩS.
            #
            # For the STRAIN equation (symmetric part):
            # dS/dt + (A²)_sym + H_sym = 0
            # dS/dt = -S² - Ω² - H_sym ... no wait
            #
            # Actually: dA/dt = -A² - H (from NS/Euler). Taking symmetric part:
            # dS/dt = -(A²)_sym - H_sym = -S² - Ω² - H_sym + advection terms
            #
            # But that's the EULERIAN derivative. The Lagrangian is different.
            # DS/Dt = dS/dt + (u·∇)S = -S² - Ω² - H + additional terms from ∇u
            #
            # Actually: DA/Dt = -A² - H (material derivative on A)
            # Symmetric part: DS/Dt = -(A²)_sym - H_sym
            # The (A²)_sym = S² + Ω² (symmetric parts)
            # And ΩΩ is NOT a familiar object — let me compute.
            # Ω_ij Ω_jk = (-ε_ijl ω_l/2)(-ε_jkm ω_m/2) = (1/4) ε_ijl ε_jkm ω_l ω_m
            # = (1/4)(δ_ik δ_lm - δ_im δ_lk) ω_l ω_m
            # = (1/4)(δ_ik |ω|² - ω_i ω_k)
            # So Ω² = (1/4)(|ω|²I - ω⊗ω)
            # This is SYMMETRIC. ✓

            # So: DS/Dt = -S² - (1/4)(|ω|²I - ω⊗ω) - H
            # = -S² + (1/4)(ω⊗ω - |ω|²I) - H
            # = -S² + (1/4)(ω⊗ω) - (1/4)|ω|²I - H

            # The three strain-RHS terms that affect eigenvector rotation:
            # T1 = -S²  (self-interaction)
            # T2 = -Ω² = (1/4)(ω⊗ω - |ω|²I)  (vorticity contribution)
            # T3 = -H  (pressure Hessian, note sign!)
            # But I computed H with the WRONG sign in the decomposition above!
            # Let me fix this in the printout.

            dc3_s = r['dc3_S2']       # from -S²
            dc3_o = r['dc3_Omega2']   # from -Ω² = (1/4)(ωω^T - |ω|²I)
            dc3_h = -r['dc3_H']       # from -H (note sign flip!)
            # Note: [S,Ω] doesn't appear in the symmetric equation!
            # It's in the ANTIsymmetric part.

            total = dc3_s + dc3_o + dc3_h

            print(f"\n  t={t:.3f}, |ω|={s.om_max(w):.3f}, {len(dc3_s)} pts:", flush=True)
            print(f"    c₃: {r['c3'].mean():.3f}  c₁: {r['c1'].mean():.3f}  "
                  f"α: {r['alpha'].mean():.4f}", flush=True)
            print(f"    dc₃ from -S²:     {dc3_s.mean():+.4f}  "
                  f"(helps: {(dc3_s > 0).mean()*100:.0f}%)", flush=True)
            print(f"    dc₃ from -Ω²:     {dc3_o.mean():+.4f}  "
                  f"(helps: {(dc3_o > 0).mean()*100:.0f}%)", flush=True)
            print(f"    dc₃ from -H:      {dc3_h.mean():+.4f}  "
                  f"(helps: {(dc3_h > 0).mean()*100:.0f}%)", flush=True)
            print(f"    TOTAL:            {total.mean():+.4f}", flush=True)

            # Which term dominates?
            abs_sum = abs(dc3_s.mean()) + abs(dc3_o.mean()) + abs(dc3_h.mean()) + 1e-30
            print(f"    Fraction: -S²={abs(dc3_s.mean())/abs_sum*100:.0f}%  "
                  f"-Ω²={abs(dc3_o.mean())/abs_sum*100:.0f}%  "
                  f"-H={abs(dc3_h.mean())/abs_sum*100:.0f}%", flush=True)

    print(f"\n{'='*70}", flush=True)
    print("DONE.", flush=True)


if __name__ == '__main__':
    main()
