"""
Visualize the NS fields in Leray frame.
Load physical checkpoints, transform to Leray variables, render 2D fields.

Shows what the singularity looks like from INSIDE the self-similar frame:
- U₁(ξ,ζ): rescaled azimuthal velocity
- W₁(ξ,ζ): rescaled azimuthal vorticity
- Ψ₁(ξ,ζ): rescaled stream function (contours = flow lines)
- Velocity arrows (Uʳ, Uᶻ) + Leray drift (ξ/2, ζ/2)
"""
import sys, os, math, json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))


def load_and_transform(ckpt_path, T_star=0.0284):
    """Load physical checkpoint, transform to Leray variables."""
    data = torch.load(ckpt_path, map_location='cpu', weights_only=False)
    u1 = data['u1'].numpy()
    w1 = data['omega1'].numpy()
    t = data['t']
    step = data['step']

    lam = math.sqrt(T_star - t)
    tau = -math.log(T_star - t)

    # Leray transform
    U1 = lam**2 * u1
    W1 = lam**3 * w1

    return U1, W1, t, step, lam, tau


def make_grid(Nr, Nz, L=1.0/6.0):
    """Recreate the Chebyshev-r, uniform-z grid."""
    j = np.arange(Nr + 1)
    x = np.cos(np.pi * j / Nr)
    r = (1 + x) / 2  # r[0]=1, r[Nr]=0

    Lz = L / 4.0
    z = np.linspace(0, Lz, Nz + 1)

    return r, z


def plot_fields(checkpoints, T_star=0.0284, out_path=None):
    """Multi-panel visualization of Leray-frame fields across time."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.colors import TwoSlopeNorm
    except ImportError:
        print("matplotlib not available")
        return

    n_ckpts = len(checkpoints)

    # Load all checkpoints
    fields = []
    for ckpt_path in checkpoints:
        U1, W1, t, step, lam, tau = load_and_transform(ckpt_path, T_star)
        Nr = U1.shape[0] - 1
        Nz = U1.shape[1] - 1
        r, z = make_grid(Nr, Nz)
        fields.append({
            'U1': U1, 'W1': W1, 't': t, 'step': step,
            'lam': lam, 'tau': tau, 'r': r, 'z': z,
        })

    # In Leray frame, ξ = r/λ but we keep the same grid (ξ ∈ [0,1])
    # The physical meaning changes: ξ=1 is at r=λ, not r=1

    # Create figure: 2 rows (U₁, W₁) × n_ckpts columns
    fig, axes = plt.subplots(3, n_ckpts, figsize=(5 * n_ckpts, 14))
    if n_ckpts == 1:
        axes = axes.reshape(-1, 1)

    fig.suptitle(f'Leray-Frame Fields — Nr={Nr}, ν=1e-4, T*={T_star:.4f}',
                 fontsize=14, y=0.98)

    for col, f in enumerate(fields):
        U1, W1 = f['U1'], f['W1']
        r, z = f['r'], f['z']
        R, Z = np.meshgrid(r, z, indexing='ij')

        # Row 0: U₁ (rescaled azimuthal velocity)
        ax = axes[0, col]
        vmax_u = max(abs(U1.max()), abs(U1.min()), 0.01)
        norm_u = TwoSlopeNorm(vmin=-vmax_u, vcenter=0, vmax=vmax_u)
        im = ax.pcolormesh(Z, R, U1, cmap='RdBu_r', norm=norm_u, shading='auto')
        ax.set_title(f'step {f["step"]}\nt={f["t"]:.5f}, τ={f["tau"]:.3f}\nλ={f["lam"]:.4f}',
                     fontsize=9)
        ax.set_ylabel('ξ (radial)' if col == 0 else '')
        if col == 0:
            ax.text(-0.15, 0.5, 'U₁', transform=ax.transAxes,
                    fontsize=14, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7, label='U₁')
        ax.set_xlim(z[0], z[-1])
        ax.set_ylim(0, 1)
        ax.invert_yaxis()  # axis (ξ=0) at top

        # Row 1: W₁ (rescaled vorticity)
        ax = axes[1, col]
        vmax_w = max(abs(W1.max()), abs(W1.min()), 0.01)
        norm_w = TwoSlopeNorm(vmin=-vmax_w, vcenter=0, vmax=vmax_w)
        im = ax.pcolormesh(Z, R, W1, cmap='RdBu_r', norm=norm_w, shading='auto')
        ax.set_ylabel('ξ (radial)' if col == 0 else '')
        if col == 0:
            ax.text(-0.15, 0.5, 'W₁', transform=ax.transAxes,
                    fontsize=14, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7, label='W₁')
        ax.set_xlim(z[0], z[-1])
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

        # Row 2: |W₁| log scale (shows structure better)
        ax = axes[2, col]
        W1_abs = np.abs(W1) + 1e-10
        im = ax.pcolormesh(Z, R, np.log10(W1_abs), cmap='inferno',
                           shading='auto')
        ax.set_ylabel('ξ (radial)' if col == 0 else '')
        ax.set_xlabel('ζ (axial)')
        if col == 0:
            ax.text(-0.15, 0.5, 'log₁₀|W₁|', transform=ax.transAxes,
                    fontsize=14, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7, label='log₁₀|W₁|')
        ax.set_xlim(z[0], z[-1])
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    if out_path is None:
        out_path = os.path.join(os.path.dirname(__file__), "leray_fields_nr256.png")
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {out_path}")
    plt.close()

    # Also make a zoomed version focusing on the vorticity core
    plot_zoomed(fields, out_path.replace('.png', '_zoom.png'))


def plot_zoomed(fields, out_path):
    """Zoom into the vorticity core region."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import TwoSlopeNorm

    n = len(fields)
    fig, axes = plt.subplots(2, n, figsize=(5 * n, 8))
    if n == 1:
        axes = axes.reshape(-1, 1)

    fig.suptitle('Leray Fields — Zoomed to Core Region', fontsize=13)

    for col, f in enumerate(fields):
        W1 = f['W1']
        U1 = f['U1']
        r, z = f['r'], f['z']

        # Find where the vorticity is concentrated
        w_abs = np.abs(W1)
        peak_idx = np.unravel_index(w_abs.argmax(), w_abs.shape)
        r_peak = r[peak_idx[0]]
        z_peak = z[peak_idx[1]]

        # Zoom window: ±0.2 around peak in r, full z
        r_lo = max(0, r_peak - 0.25)
        r_hi = min(1, r_peak + 0.25)

        # Find grid indices
        r_mask = (r >= r_lo) & (r <= r_hi)
        r_sub = r[r_mask]
        W1_sub = W1[r_mask, :]
        U1_sub = U1[r_mask, :]

        R_sub, Z_sub = np.meshgrid(r_sub, z, indexing='ij')

        # W₁ zoomed
        ax = axes[0, col]
        vmax = max(abs(W1_sub.max()), abs(W1_sub.min()), 0.01)
        norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
        im = ax.pcolormesh(Z_sub, R_sub, W1_sub, cmap='RdBu_r', norm=norm, shading='auto')
        ax.set_title(f'step {f["step"]}, τ={f["tau"]:.3f}', fontsize=9)
        ax.plot(z_peak, r_peak, 'k+', markersize=10, markeredgewidth=2)
        ax.set_ylabel('ξ' if col == 0 else '')
        plt.colorbar(im, ax=ax, shrink=0.8, label='W₁')
        ax.invert_yaxis()

        # Radial profile at z_peak
        ax = axes[1, col]
        z_idx = peak_idx[1]
        ax.plot(r, W1[:, z_idx], 'b-', linewidth=1.5, label=f'W₁(ξ, ζ={z_peak:.4f})')
        ax.plot(r, U1[:, z_idx], 'r--', linewidth=1, label=f'U₁(ξ, ζ={z_peak:.4f})')
        ax.axvline(x=r_peak, color='gray', linestyle=':', alpha=0.5)
        ax.set_xlabel('ξ (radial)')
        ax.set_ylabel('Amplitude' if col == 0 else '')
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {out_path}")
    plt.close()


if __name__ == '__main__':
    base = os.path.dirname(__file__)
    ckpt_dir = os.path.join(base, "results", "h200_sync")

    # Load all available checkpoints
    ckpt_files = sorted([
        os.path.join(ckpt_dir, f)
        for f in os.listdir(ckpt_dir)
        if f.startswith("checkpoint_nr256") and f.endswith(".pt")
    ])

    if not ckpt_files:
        print("No checkpoints found!")
        sys.exit(1)

    print(f"Found {len(ckpt_files)} checkpoints:")
    for f in ckpt_files:
        print(f"  {os.path.basename(f)}")

    plot_fields(ckpt_files)
