"""
Shell-by-shell enstrophy transfer T(j,j') = ∫ω_j · S_{j'} · ω_j dx

If T(j,j) ≈ 0 (diagonal vanishing from single-mode orthogonality)
AND T(j,j') ~ 2^{-|j-j'|} (geometric off-diagonal decay):
→ Littlewood-Paley enstrophy balance closes → REGULARITY

THE measurement that could close the proof.
"""
import torch, math, time, json, os
import numpy as np
torch.set_default_dtype(torch.float64)

def run_shell_transfer(N=64, nu=1e-4, device='cuda'):
    Lx=2*math.pi; dx=Lx/N
    k=torch.fft.fftfreq(N,d=dx/(2*math.pi)).to(device)
    kx,ky,kz=torch.meshgrid(k,k,k,indexing='ij')
    ksq=kx**2+ky**2+kz**2; ksq[0,0,0]=1.0
    kmag=ksq.sqrt()
    ikx,iky,ikz=1j*kx,1j*ky,1j*kz
    kmax=N//3; D=((kx.abs()<kmax)&(ky.abs()<kmax)&(kz.abs()<kmax)).to(torch.float64)
    ifft=lambda f:torch.fft.ifftn(f*D).real; fft=torch.fft.fftn
    ik_list=[ikx,iky,ikz]

    # Define shells: j-th shell has 2^j ≤ |k| < 2^{j+1}
    max_shell = int(math.log2(kmax)) + 1
    shell_masks = []
    for j in range(max_shell + 1):
        if j == 0:
            mask = (kmag < 2).to(torch.float64) * D
        else:
            mask = ((kmag >= 2**j) & (kmag < 2**(j+1))).to(torch.float64) * D
        shell_masks.append(mask)

    def ns_rhs(wx_h,wy_h,wz_h):
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
        return(D*fft(sx-ax)-nu*ksq*wx_h,D*fft(sy-ay)-nu*ksq*wy_h,D*fft(sz-az)-nu*ksq*wz_h)

    def rk4(wx_h,wy_h,wz_h,dt):
        def add(a,b,s):return(a[0]+s*b[0],a[1]+s*b[1],a[2]+s*b[2])
        w=(wx_h,wy_h,wz_h);k1=ns_rhs(*w);k2=ns_rhs(*add(w,k1,.5*dt));k3=ns_rhs(*add(w,k2,.5*dt));k4=ns_rhs(*add(w,k3,dt))
        return(wx_h+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),wy_h+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),wz_h+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

    def compute_transfer_matrix(wx_h, wy_h, wz_h):
        """Compute T(j,j') = ∫ω_j · S_{j'} · ω_j dx for all shell pairs."""
        n_shells = len(shell_masks)
        T = np.zeros((n_shells, n_shells))

        # For each target shell j: filter ω to shell j
        for j in range(n_shells):
            mj = shell_masks[j]
            wj_x = ifft(wx_h * mj); wj_y = ifft(wy_h * mj); wj_z = ifft(wz_h * mj)

            # For each source shell j': compute strain from shell j'
            for jp in range(n_shells):
                mjp = shell_masks[jp]
                # Velocity from shell j'
                pxp = (wx_h*mjp)/ksq; pyp = (wy_h*mjp)/ksq; pzp = (wz_h*mjp)/ksq
                pxp[0,0,0]=0; pyp[0,0,0]=0; pzp[0,0,0]=0
                uxp = iky*pzp-ikz*pyp; uyp = ikz*pxp-ikx*pzp; uzp = ikx*pyp-iky*pxp

                # Strain from shell j' (symmetric part of ∇u_{j'})
                # S_{j'}·ω_j = sym(∇u_{j'}) · ω_j
                # = (1/2)[(∇u_{j'})ω_j + (∇u_{j'})^T ω_j]
                # Inner product with ω_j: ω_j · S_{j'} · ω_j = ω_j · (∇u_{j'}) · ω_j
                # (the symmetric part gives the same quadratic form)

                # Compute ω_j · (∇u_{j'}) · ω_j at each point
                val = torch.zeros(N,N,N, device=device, dtype=torch.float64)
                u_hats_jp = [uxp, uyp, uzp]
                wj = [wj_x, wj_y, wj_z]
                for i in range(3):
                    for l in range(3):
                        # (∂u_i^{j'}/∂x_l) = ifft(ik_l * u_i^{j'})
                        du = ifft(ik_list[l] * u_hats_jp[i] * D)
                        val += wj[i] * du * wj[l]

                T[j, jp] = val.sum().item() * (dx**3)  # integrate

        return T

    # TG IC
    x = torch.linspace(0, Lx-dx, N, device=device, dtype=torch.float64)
    X,Y,Z = torch.meshgrid(x,x,x,indexing='ij')
    ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
    uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
    uz = torch.zeros_like(X)
    ux_h=D*fft(ux);uy_h=D*fft(uy);uz_h=D*fft(uz)
    wx_h=D*(iky*uz_h-ikz*uy_h);wy_h=D*(ikz*ux_h-ikx*uz_h);wz_h=D*(ikx*uy_h-iky*ux_h)

    dt = 0.002; n_steps = 1500  # evolve to t=3 (peak stretching)

    print(f'SHELL-BY-SHELL ENSTROPHY TRANSFER — TG N={N}', flush=True)
    print(f'Evolving to t=3 (peak stretching)...', flush=True)

    for step in range(n_steps):
        wx_h,wy_h,wz_h = rk4(wx_h,wy_h,wz_h,dt)

    t0 = time.time()
    T_matrix = compute_transfer_matrix(wx_h, wy_h, wz_h)
    elapsed = time.time() - t0

    print(f'Transfer matrix computed [{elapsed:.0f}s]', flush=True)
    print(f'\nShell transfer T(j,j\') at t=3:')
    print(f'Shells: 0={"|k|<2"}, 1={"2≤|k|<4"}, 2={"4≤|k|<8"}, 3={"8≤|k|<16"}, 4={"16≤|k|<32"}')
    print()

    n_shells = T_matrix.shape[0]
    # Print matrix
    header = '     ' + ''.join(f'  j\'={jp:d}    ' for jp in range(min(n_shells,6)))
    print(header)
    for j in range(min(n_shells, 6)):
        row = f'j={j}: ' + ''.join(f'{T_matrix[j,jp]:+9.2e} ' for jp in range(min(n_shells,6)))
        print(row)

    # Analysis
    print(f'\nDIAGONAL (self-interaction, should be ≈ 0 from single-mode orth):')
    for j in range(min(n_shells, 6)):
        total_j = sum(abs(T_matrix[j,jp]) for jp in range(n_shells))
        diag_frac = abs(T_matrix[j,j]) / (total_j + 1e-30)
        print(f'  T({j},{j}) = {T_matrix[j,j]:+.4e}  ({diag_frac*100:.1f}% of row total)')

    print(f'\nOFF-DIAGONAL DECAY (should decrease with |j-j\'|):')
    for d in range(1, min(4, n_shells)):
        vals = [abs(T_matrix[j,j+d]) for j in range(n_shells-d)]
        if vals:
            print(f'  |j-j\'|={d}: max={max(vals):.4e} mean={np.mean(vals):.4e}')

    # Check geometric decay
    off_diag_by_dist = {}
    for j in range(n_shells):
        for jp in range(n_shells):
            d = abs(j-jp)
            if d > 0:
                if d not in off_diag_by_dist:
                    off_diag_by_dist[d] = []
                off_diag_by_dist[d].append(abs(T_matrix[j,jp]))

    if len(off_diag_by_dist) >= 2:
        dists = sorted(off_diag_by_dist.keys())
        means = [np.mean(off_diag_by_dist[d]) for d in dists]
        if len(means) >= 2 and means[0] > 0 and means[1] > 0:
            decay_rate = means[1] / means[0]
            print(f'\n  Decay rate: T(d+1)/T(d) ≈ {decay_rate:.4f}')
            print(f'  Geometric decay: {"YES ✓" if decay_rate < 0.8 else "NO — need more shells"}')

    out = 'ns_blowup/results/shell_transfer.json'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'T_matrix': T_matrix.tolist(), 'N': N, 'n_shells': n_shells}, f, indent=2)
    print(f'\nSaved: {out}', flush=True)


if __name__ == '__main__':
    run_shell_transfer()
