"""
Visual QA for NS blowup runs.
Generates a 4-panel PNG: Γ, α, R_rms, spectral vs step.
Usage: python3 plot_run.py <json_file> [output.png]
       python3 plot_run.py --log <log_file> [output.png]
"""
import sys, json, os
import numpy as np

def parse_log(path):
    """Parse a log file with format: step=... t=... G=... R=... a=... spec=... |w|=..."""
    entries = []
    with open(path) as f:
        for line in f:
            if not line.startswith('step=') or 'CHECKPOINT' in line:
                continue
            try:
                tokens = line.split()
                e = {
                    'step': int(tokens[0].replace('step=', '')),
                    't': float(tokens[1].replace('t=', '')),
                    'gamma': float(tokens[2].replace('G=', '')),
                }
                # Try to get R and alpha (may not exist in older logs)
                for tok in tokens[3:]:
                    if tok.startswith('R='):
                        e['R_rms'] = float(tok.replace('R=', ''))
                    elif tok.startswith('a='):
                        e['alpha'] = float(tok.replace('a=', ''))
                    elif tok.startswith('spec='):
                        e['spectral'] = float(tok.replace('spec=', ''))
                    elif tok.startswith('|w|='):
                        e['om1'] = float(tok.replace('|w|=', ''))
                entries.append(e)
            except:
                pass
    return entries

def plot_run(data, title, out_path):
    """Generate 4-panel plot."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available, trying bare-bones ASCII plot")
        ascii_plot(data, title)
        return

    steps = [d['step'] for d in data if d['step'] > 0]
    gamma = [d['gamma'] for d in data if d['step'] > 0]

    has_alpha = 'alpha' in data[1] if len(data) > 1 else False
    has_R = 'R_rms' in data[1] if len(data) > 1 else False
    has_spec = 'spectral' in data[1] if len(data) > 1 else False
    has_omega = 'om1' in data[1] if len(data) > 1 else False

    n_panels = 2 + (1 if has_alpha else 0) + (1 if has_spec else 0)
    fig, axes = plt.subplots(n_panels, 1, figsize=(12, 3 * n_panels), sharex=True)
    if n_panels == 1:
        axes = [axes]

    panel = 0

    # Panel 1: Γ
    axes[panel].plot(steps, gamma, 'b-', linewidth=1.5)
    axes[panel].axhline(y=0, color='r', linestyle='--', alpha=0.5)
    axes[panel].set_ylabel('Γ (gap frame)')
    axes[panel].set_title(title)
    g_min = min(gamma)
    g_min_step = steps[gamma.index(g_min)]
    axes[panel].annotate(f'min={g_min:.4f}', xy=(g_min_step, g_min),
                        fontsize=8, color='red')
    axes[panel].grid(True, alpha=0.3)
    panel += 1

    # Panel 2: |ω| (log scale)
    if has_omega:
        omega = [d['om1'] for d in data if d['step'] > 0]
        axes[panel].semilogy(steps, omega, 'k-', linewidth=1.5)
        axes[panel].set_ylabel('|ω₁|_max')
        axes[panel].grid(True, alpha=0.3)
        panel += 1

    # Panel 3: α and R_rms (if available)
    if has_alpha:
        alpha = [d['alpha'] for d in data if d['step'] > 0]
        ax_a = axes[panel]
        ax_a.plot(steps, alpha, 'g-', linewidth=1.5, label='α (strain)')
        ax_a.set_ylabel('α (strain rate)', color='g')
        if has_R:
            R = [d['R_rms'] for d in data if d['step'] > 0]
            ax_r = ax_a.twinx()
            ax_r.plot(steps, R, 'r-', linewidth=1, alpha=0.7, label='R_rms')
            ax_r.set_ylabel('R_rms (core width)', color='r')
        ax_a.grid(True, alpha=0.3)
        panel += 1

    # Panel 4: Spectral ratio
    if has_spec:
        spec = [d['spectral'] for d in data if d['step'] > 0]
        axes[panel].semilogy(steps, spec, 'm-', linewidth=1.5)
        axes[panel].axhline(y=0.01, color='orange', linestyle='--', alpha=0.7, label='MARGINAL')
        axes[panel].axhline(y=0.1, color='red', linestyle='--', alpha=0.7, label='UNDER')
        axes[panel].set_ylabel('Spectral ratio')
        axes[panel].legend(fontsize=8)
        axes[panel].grid(True, alpha=0.3)
        panel += 1

    axes[-1].set_xlabel('Step')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    print(f"Saved plot to {out_path}")
    plt.close()

def ascii_plot(data, title):
    """Fallback ASCII summary."""
    steps = [d['step'] for d in data if d['step'] > 0]
    gamma = [d['gamma'] for d in data if d['step'] > 0]
    print(f"\n{title}")
    print(f"Steps: {steps[0]}-{steps[-1]}, Γ: {max(gamma):.4f} → {gamma[-1]:.4f}")
    g_min = min(gamma)
    print(f"Γ_min = {g_min:.4f} at step {steps[gamma.index(g_min)]}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 plot_run.py <json_or_log> [output.png]")
        sys.exit(1)

    path = sys.argv[1]
    is_log = path.endswith('.log') or '--log' in sys.argv

    if '--log' in sys.argv:
        sys.argv.remove('--log')
        path = sys.argv[1]

    if path.endswith('.json'):
        with open(path) as f:
            data = json.load(f)
    else:
        data = parse_log(path)

    title = os.path.basename(path).replace('.json', '').replace('.log', '')
    out = sys.argv[2] if len(sys.argv) > 2 else path.rsplit('.', 1)[0] + '.png'

    plot_run(data, title, out)
