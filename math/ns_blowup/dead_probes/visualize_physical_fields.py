"""
Visualize the NS fields in PHYSICAL frame (pre-Leray transform).
Same checkpoints, raw u₁ and ω₁ — see what the solver actually computed.
Side-by-side with Leray for comparison.
"""
import sys, os, math
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))


def make_grid(Nr, Nz, L=1.0/6.0):
    j = np.arange(Nr + 1)
    x = np.cos(np.pi * j / Nr)
    r = (1 + x) / 2
    Lz = L / 4.0
    z = np.linspace(0, Lz, Nz + 1)
    return r, z


def plot_physical_vs_leray(checkpoints, T_star=0.0284, out_path=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import TwoSlopeNorm, LogNorm

    n = len(checkpoints)

    # 4 rows: physical u₁, physical ω₁, leray U₁, leray W₁
    fig, axes = plt.subplots(4, n, figsize=(4.5 * n, 16))
    if n == 1:
        axes = axes.reshape(-1, 1)

    fig.suptitle('Physical Frame vs Leray Frame — Nr=256, ν=1e-4', fontsize=14, y=0.99)

    for col, ckpt_path in enumerate(checkpoints):
        data = torch.load(ckpt_path, map_location='cpu', weights_only=False)
        u1 = data['u1'].numpy()
        w1 = data['omega1'].numpy()
        t = data['t']
        step = data['step']

        Nr = u1.shape[0] - 1
        Nz = u1.shape[1] - 1
        r, z = make_grid(Nr, Nz)
        R, Z = np.meshgrid(r, z, indexing='ij')

        lam = math.sqrt(T_star - t)
        tau = -math.log(T_star - t)
        U1 = lam**2 * u1
        W1 = lam**3 * w1

        # Row 0: Physical u₁
        ax = axes[0, col]
        vmax = max(abs(u1.max()), abs(u1.min()), 0.01)
        norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
        im = ax.pcolormesh(Z, R, u1, cmap='RdBu_r', norm=norm, shading='auto')
        ax.set_title(f'step {step}\nt={t:.5f}', fontsize=9)
        if col == 0:
            ax.set_ylabel('r (radial)')
            ax.text(-0.2, 0.5, 'u₁ (physical)', transform=ax.transAxes,
                    fontsize=12, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7)
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

        # Row 1: Physical ω₁
        ax = axes[1, col]
        if abs(w1).max() > 0:
            vmax_w = max(abs(w1.max()), abs(w1.min()))
            norm_w = TwoSlopeNorm(vmin=-vmax_w, vcenter=0, vmax=vmax_w)
        else:
            norm_w = None
        im = ax.pcolormesh(Z, R, w1, cmap='RdBu_r', norm=norm_w, shading='auto')
        if col == 0:
            ax.set_ylabel('r (radial)')
            ax.text(-0.2, 0.5, 'ω₁ (physical)', transform=ax.transAxes,
                    fontsize=12, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7)
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

        # Row 2: Leray U₁
        ax = axes[2, col]
        vmax_U = max(abs(U1.max()), abs(U1.min()), 0.01)
        norm_U = TwoSlopeNorm(vmin=-vmax_U, vcenter=0, vmax=vmax_U)
        im = ax.pcolormesh(Z, R, U1, cmap='RdBu_r', norm=norm_U, shading='auto')
        ax.set_title(f'τ={tau:.3f}, λ={lam:.4f}', fontsize=9)
        if col == 0:
            ax.set_ylabel('ξ (radial)')
            ax.text(-0.2, 0.5, 'U₁ (Leray)', transform=ax.transAxes,
                    fontsize=12, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7)
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

        # Row 3: Leray W₁
        ax = axes[3, col]
        if abs(W1).max() > 0:
            vmax_W = max(abs(W1.max()), abs(W1.min()))
            norm_W = TwoSlopeNorm(vmin=-vmax_W, vcenter=0, vmax=vmax_W)
        else:
            norm_W = None
        im = ax.pcolormesh(Z, R, W1, cmap='RdBu_r', norm=norm_W, shading='auto')
        ax.set_xlabel('z (axial)')
        if col == 0:
            ax.set_ylabel('ξ (radial)')
            ax.text(-0.2, 0.5, 'W₁ (Leray)', transform=ax.transAxes,
                    fontsize=12, fontweight='bold', va='center', rotation=90)
        plt.colorbar(im, ax=ax, shrink=0.7)
        ax.set_ylim(0, 1)
        ax.invert_yaxis()

    plt.tight_layout(rect=[0, 0, 1, 0.97])

    if out_path is None:
        out_path = os.path.join(os.path.dirname(__file__), "physical_vs_leray_nr256.png")
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {out_path}")
    plt.close()

    # Bonus: amplitude comparison plot
    plot_amplitude_evolution(checkpoints, T_star)


def plot_amplitude_evolution(checkpoints, T_star):
    """Show how physical amplitudes grow while Leray amplitudes stay O(1)."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    steps, u1_max, w1_max, U1_max, W1_max, taus = [], [], [], [], [], []

    for ckpt_path in checkpoints:
        data = torch.load(ckpt_path, map_location='cpu', weights_only=False)
        u1 = data['u1'].numpy()
        w1 = data['omega1'].numpy()
        t = data['t']
        lam = math.sqrt(T_star - t)

        steps.append(data['step'])
        u1_max.append(abs(u1).max())
        w1_max.append(abs(w1).max())
        U1_max.append(abs(u1).max() * lam**2)
        W1_max.append(abs(w1).max() * lam**3)
        taus.append(-math.log(T_star - t))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Physical frame: amplitudes exploding
    ax1.semilogy(steps, u1_max, 'b-o', label='|u₁|_max', markersize=6)
    ax1.semilogy(steps, w1_max, 'r-s', label='|ω₁|_max', markersize=6)
    ax1.set_xlabel('Step')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Physical Frame — Amplitudes Growing')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Leray frame: amplitudes O(1)
    ax2.plot(steps, U1_max, 'b-o', label='|U₁|_max (Leray)', markersize=6)
    ax2.plot(steps, W1_max, 'r-s', label='|W₁|_max (Leray)', markersize=6)
    ax2.set_xlabel('Step')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Leray Frame — Amplitudes O(1)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "amplitude_physical_vs_leray.png")
    plt.savefig(out_path, dpi=150)
    print(f"Saved: {out_path}")
    plt.close()


if __name__ == '__main__':
    base = os.path.dirname(__file__)
    ckpt_dir = os.path.join(base, "results", "h200_sync")

    ckpt_files = sorted([
        os.path.join(ckpt_dir, f)
        for f in os.listdir(ckpt_dir)
        if f.startswith("checkpoint_nr256") and f.endswith(".pt")
    ])

    print(f"Found {len(ckpt_files)} checkpoints")
    plot_physical_vs_leray(ckpt_files)
