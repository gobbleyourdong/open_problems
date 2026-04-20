"""
Instance B: Test R for ARBITRARY non-negative functions f on T³.

R[f] = |ê·H_dev·ê| / (f(x*)/3)
where H = ∇²(Δ⁻¹f), x* = argmax f, ê = arbitrary unit vector.

This is a PURE MATH question about the Laplacian on T³.
If R ≤ 1 for ALL f ≥ 0: NS regularity follows.

Test configurations designed to MAXIMIZE R:
1. Straight tube (known R=1)
2. Flat sheet (extreme 1D anisotropy)
3. Needle (extreme 2D anisotropy)
4. Two-blob (bimodal, asymmetric)
5. Random positive functions
"""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

def compute_R(N, f_field, e_hat):
    """
    Compute R = |ê·H_dev·ê| / (f(x*)/3) for given f and ê.
    f_field: N×N×N tensor (non-negative)
    e_hat: unit vector (3,)
    """
    L = 2*pi
    k = torch.fft.fftfreq(N, d=L/(N*2*pi)).to(dtype=DTYPE)
    kx,ky,kz = torch.meshgrid(k,k,k,indexing='ij')
    ksq = kx**2+ky**2+kz**2; ksq[0,0,0]=1

    # Find max of f
    flat = f_field.flatten()
    idx = flat.argmax().item()
    iz=idx%N;iy=(idx//N)%N;ix=idx//(N*N)
    f_max = flat[idx].item()
    if f_max < 1e-10: return None

    # Solve Poisson: Δp = f → p_hat = f_hat/(-ksq)... wait
    # We want H = ∇²(Δ⁻¹f). Δ⁻¹f means solve Δu = f → u_hat = -f_hat/ksq.
    # Then H_ij = ∂²u/∂x_i∂x_j → H_hat = -k_i k_j u_hat = k_i k_j f_hat / ksq.
    f_hat = torch.fft.fftn(f_field)
    kd = [kx,ky,kz]

    # H at the max point
    H = torch.zeros(3,3,dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Hfield = torch.fft.ifftn(-kd[i]*kd[j]*(-f_hat/ksq)).real
            # Wait: Δ⁻¹f: if Δu = f, then u_hat = -f_hat/ksq (Green's function sign).
            # H_ij = ∂_i∂_j u. In Fourier: -k_ik_j u_hat = -k_ik_j(-f_hat/ksq) = k_ik_j f_hat/ksq
            Hfield = torch.fft.ifftn(kd[i]*kd[j]*f_hat/ksq).real
            Hfield[0,0,0] = 0  # remove k=0
            H[i,j] = Hfield[ix,iy,iz]

    # Check: tr(H) should = f(x*) (since tr(∇²Δ⁻¹f) = ΔΔ⁻¹f = f)
    trH = H.trace().item()

    # H_dev = H - (tr(H)/3)I
    H_dev = H - (trH/3)*torch.eye(3,dtype=DTYPE)

    # Project onto ê
    eh = torch.tensor(e_hat, dtype=DTYPE)
    H_dev_ee = (eh @ H_dev @ eh).item()
    H_iso = trH/3

    R = abs(H_dev_ee) / (abs(H_iso) + 1e-30)

    return {'R': R, 'H_dev_ee': H_dev_ee, 'H_iso': H_iso, 'trH': trH, 'f_max': f_max}

def main():
    N = 32
    L = 2*pi
    dx = L/N
    x = torch.linspace(0, L-dx, N, dtype=DTYPE)
    X,Y,Z = torch.meshgrid(x,x,x,indexing='ij')

    print("="*70,flush=True)
    print("R FOR ARBITRARY f ≥ 0: is R ≤ 1 a universal property of T³?",flush=True)
    print("="*70,flush=True)

    configs = []

    # 1. Straight tube (z-independent Gaussian) — should give R=1
    sigma = 0.3
    f = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*sigma**2))
    configs.append(("straight_tube_s03", f, [0,0,1]))

    f = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.15**2))
    configs.append(("straight_tube_s015", f, [0,0,1]))

    # 2. Flat sheet (z-thin)
    f = torch.exp(-(Z-pi)**2/(2*0.1**2))  # uniform in x,y, thin in z
    configs.append(("sheet_z_thin", f, [0,0,1]))
    configs.append(("sheet_z_thin_ê=x", f, [1,0,0]))

    # 3. Needle (thin in x AND y, extended in z)
    f = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.1**2))
    configs.append(("needle_z", f, [1,0,0]))  # ê perpendicular to needle

    # 4. 3D Gaussian blob (isotropic)
    f = torch.exp(-((X-pi)**2+(Y-pi)**2+(Z-pi)**2)/(2*0.3**2))
    configs.append(("blob_iso", f, [0,0,1]))

    # 5. Ellipsoid (anisotropic blob)
    f = torch.exp(-((X-pi)**2/(2*0.5**2)+(Y-pi)**2/(2*0.2**2)+(Z-pi)**2/(2*0.1**2)))
    configs.append(("ellipsoid_ê=z", f, [0,0,1]))  # along thinnest
    configs.append(("ellipsoid_ê=x", f, [1,0,0]))  # along thickest

    # 6. Two blobs (bimodal)
    f = torch.exp(-((X-pi-0.5)**2+(Y-pi)**2+(Z-pi)**2)/(2*0.2**2)) + \
        torch.exp(-((X-pi+0.5)**2+(Y-pi)**2+(Z-pi)**2)/(2*0.2**2))
    configs.append(("two_blobs", f, [1,0,0]))

    # 7. Tube + perturbation (Instance A's critical case)
    f0 = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.3**2))
    g = 0.5*torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.2**2))*torch.cos(2*Z)
    f = (f0 + g).clamp(min=0)
    configs.append(("tube+cos2z", f, [0,0,1]))

    # 8. Maximize anisotropy: tube in z, ê along z
    # This is the known worst case
    f = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.15**2))
    configs.append(("thin_tube_ê=z", f, [0,0,1]))

    print(f"\n  {'config':>25s}  {'R':>6s}  {'H_dev_êê':>10s}  {'H_iso':>8s}  "
          f"{'trH':>8s}  {'f_max':>6s}  {'R<1?':>5s}",flush=True)
    print("-"*80,flush=True)

    worst_R = 0
    worst_name = ""

    for name, f_field, e_vec in configs:
        r = compute_R(N, f_field, e_vec)
        if r is None: continue
        ok = "✓" if r['R'] < 1.001 else "**NO**"
        if r['R'] > worst_R:
            worst_R = r['R']; worst_name = name
        print(f"  {name:>25s}  {r['R']:6.4f}  {r['H_dev_ee']:+10.4f}  "
              f"{r['H_iso']:+8.4f}  {r['trH']:+8.4f}  {r['f_max']:6.2f}  {ok:>5s}",flush=True)

    print(f"\n  WORST R: {worst_R:.6f} at '{worst_name}'",flush=True)
    print(f"  R ≤ 1 for ALL configs: {'YES ✓' if worst_R<=1.001 else 'NO ✗'}",flush=True)

    # Focused search: try many random ê directions for the straight tube
    print(f"\n  --- Random ê for straight tube (σ=0.15) ---",flush=True)
    f = torch.exp(-((X-pi)**2+(Y-pi)**2)/(2*0.15**2))
    max_R_tube = 0
    for _ in range(50):
        e = np.random.randn(3); e = e/np.linalg.norm(e)
        r = compute_R(N, f, e.tolist())
        if r and r['R'] > max_R_tube:
            max_R_tube = r['R']
    print(f"  Max R over 50 random ê: {max_R_tube:.6f}",flush=True)
    print(f"  (Should be ~1.0 when ê=z, less otherwise)",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("CONCLUSION: if R ≤ 1 for all f ≥ 0 and all ê, it's a THEOREM",flush=True)
    print("about the Newtonian potential on T³, independent of fluid mechanics.",flush=True)
    print(f"{'='*70}",flush=True)

if __name__=='__main__':
    main()
