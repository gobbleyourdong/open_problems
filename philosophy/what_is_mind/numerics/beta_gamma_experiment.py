"""
beta_gamma_experiment.py — Cycle 6
Numerical Track: what_is_mind

Implements the 2×2 experiment from attempt_003:
  T1: feedforward, minimal self-model
  T2: feedforward, rich self-model
  R1: recurrent,   minimal self-model
  R2: recurrent,   rich self-model

β predicts: Phi(T1)=Phi(T2)≈0, Phi(R1)≈Phi(R2)>0  (loop topology is decisive)
γ predicts: Phi-irrelevant; G×L(T1)≈G×L(R1)≈0, G×L(T2)≈G×L(R2)>0  (self-model is decisive)

For small binary networks (n=6):
  - First n//2 nodes: primary processing (compute something)
  - Last n//2 nodes: self-model layer (represent states of primary nodes)

"Rich self-model": self-model nodes have strong, accurate representation of primary nodes
"Minimal self-model": self-model nodes are noisy / weakly connected to primary nodes

G proxy: correlation between self-model nodes and primary nodes they track
L proxy: change in primary-output variance when self-model nodes are ablated

We measure Phi (exact, for n=6) and G×L for all four networks, then ask:
which quantity better tracks the "phenomenal content" ordering predicted by each theory?
"""

import math
import numpy as np
from phi_small_systems import phi_state


# Import helpers
import sys
sys.path.insert(0, '.')


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -20, 20)))


def build_2x2_tpm(
    n: int = 6,
    recurrent: bool = False,
    rich_self_model: bool = False,
    seed: int = 42,
) -> tuple[np.ndarray, dict]:
    """
    Build a 2-layer n-node network: primary (n//2 nodes) + self-model (n//2 nodes).

    Parameters:
      recurrent:       if True, primary layer has recurrent connections
      rich_self_model: if True, self-model nodes strongly track primary nodes

    Returns: (tpm, metadata)
    """
    rng = np.random.default_rng(seed)
    n_primary = n // 2
    n_self = n - n_primary
    n_states = 1 << n

    # Primary layer weights
    if recurrent:
        W_primary = rng.normal(0, 1.5, (n_primary, n_primary))
    else:
        # Feedforward: strictly lower-triangular within primary
        W_primary = np.tril(rng.normal(0, 1.5, (n_primary, n_primary)), k=-1)

    b_primary = rng.normal(0, 0.3, n_primary)

    # Self-model layer weights
    if rich_self_model:
        # Self-model nodes strongly track primary nodes (high weight, low noise)
        W_self_from_primary = np.diag(rng.uniform(2.0, 3.0, min(n_self, n_primary)))
        # Pad or trim if n_self != n_primary
        if n_self > n_primary:
            W_self_from_primary = np.pad(W_self_from_primary,
                                          ((0, n_self - n_primary), (0, 0)))
        elif n_self < n_primary:
            W_self_from_primary = W_self_from_primary[:n_self, :]
        W_self_recurrent = rng.normal(0, 0.2, (n_self, n_self))  # minimal self-self recurrence
        b_self = rng.normal(0, 0.1, n_self)
    else:
        # Minimal self-model: weak, noisy connections from primary
        W_self_from_primary = rng.normal(0, 0.3, (n_self, n_primary))
        W_self_recurrent = rng.normal(0, 0.1, (n_self, n_self))
        b_self = rng.normal(0, 0.3, n_self)

    # Build TPM
    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state = np.array([(s >> j) & 1 for j in range(n)], dtype=float)
        primary_state = state[:n_primary]
        self_state    = state[n_primary:]

        # Primary layer activations
        if recurrent:
            primary_probs = sigmoid(W_primary @ primary_state + b_primary)
        else:
            primary_probs = sigmoid(W_primary @ primary_state + b_primary)

        # Self-model layer activations
        self_probs = sigmoid(
            W_self_from_primary @ primary_state +
            W_self_recurrent @ self_state +
            b_self
        )

        # Build output distribution
        all_probs = np.concatenate([primary_probs, self_probs])
        for s2 in range(n_states):
            prob = 1.0
            for i in range(n):
                bit = (s2 >> i) & 1
                p = all_probs[i]
                prob *= p if bit == 1 else (1 - p)
            tpm[s, s2] = prob

    metadata = {
        "recurrent": recurrent,
        "rich_self_model": rich_self_model,
        "W_primary": W_primary,
        "W_self_from_primary": W_self_from_primary,
        "n_primary": n_primary,
        "n_self": n_self,
    }
    return tpm, metadata


def compute_G_proxy(tpm: np.ndarray, n: int, meta: dict, n_samples: int = 50) -> float:
    """
    G proxy: correlation between self-model node activations and primary node states.

    For each state s, compute:
      primary_activation = E[primary_state' | s]  (expected next primary state)
      self_activation = E[self_state' | s]         (expected next self-model state)
    Correlation = mean over nodes of corr(self_node_i_activation, primary_node_i_activation)
    across sampled states.
    """
    n_primary = meta["n_primary"]
    n_self    = meta["n_self"]
    n_states  = 1 << n

    rng = np.random.default_rng(77)
    states = rng.integers(0, n_states, size=n_samples).tolist()

    primary_means = []
    self_means    = []

    for s in states:
        row = tpm[s]  # P(next | current=s), shape (n_states,)
        # Expected next state for each node
        exp_next = np.zeros(n)
        for s2 in range(n_states):
            bits = np.array([(s2 >> j) & 1 for j in range(n)], dtype=float)
            exp_next += row[s2] * bits
        primary_means.append(exp_next[:n_primary])
        self_means.append(exp_next[n_primary:])

    primary_arr = np.array(primary_means)  # (n_samples, n_primary)
    self_arr    = np.array(self_means)     # (n_samples, n_self)

    # Compute correlation for each (primary_i, self_i) pair
    k = min(n_primary, n_self)
    corrs = []
    for i in range(k):
        p = primary_arr[:, i]
        sm = self_arr[:, i]
        if np.std(p) > 0 and np.std(sm) > 0:
            c = np.corrcoef(p, sm)[0, 1]
            corrs.append(max(0.0, c))

    return float(np.mean(corrs)) if corrs else 0.0


def compute_L_proxy(tpm: np.ndarray, n: int, meta: dict, n_samples: int = 50) -> float:
    """
    L proxy: how much does ablating the self-model nodes change primary-node output?

    For each state s:
      1. Compute expected next primary state under the real TPM
      2. Compute expected next primary state under "ablated" TPM where self-model
         nodes are pinned to 0.5 (maximum uncertainty / no causal influence)
      3. L = mean over states of |normal - ablated| output difference

    Higher L = self-model is more causally load-bearing on primary outputs.
    """
    n_primary = meta["n_primary"]
    n_self    = meta["n_self"]
    n_states  = 1 << n

    # Build ablated TPM: replace self-model-node input to primary computation
    # Approximation: average out the self-model state by marginalising
    # We compute: P_ablated(next_primary | primary_state) by averaging over self_state
    # = sum_{self_state} P(self_state) * P(next_primary | primary_state, self_state)
    # with P(self_state) = uniform (self-model ablated)

    rng = np.random.default_rng(77)
    states = rng.integers(0, n_states, size=n_samples).tolist()

    diffs = []
    for s in states:
        # Normal expected next primary state
        row_normal = tpm[s]
        exp_primary_normal = np.zeros(n_primary)
        for s2 in range(n_states):
            bits_primary = np.array([(s2 >> j) & 1 for j in range(n_primary)], dtype=float)
            exp_primary_normal += row_normal[s2] * bits_primary

        # Ablated: average over all self-model states with same primary state
        s_primary = s & ((1 << n_primary) - 1)  # primary bits
        ablated_rows = []
        for self_val in range(1 << n_self):
            s_full = s_primary | (self_val << n_primary)
            ablated_rows.append(tpm[s_full])
        row_ablated = np.mean(ablated_rows, axis=0)

        exp_primary_ablated = np.zeros(n_primary)
        for s2 in range(n_states):
            bits_primary = np.array([(s2 >> j) & 1 for j in range(n_primary)], dtype=float)
            exp_primary_ablated += row_ablated[s2] * bits_primary

        diff = float(np.mean(np.abs(exp_primary_normal - exp_primary_ablated)))
        diffs.append(diff)

    return float(np.mean(diffs))


def run():
    import json
    from phi_small_systems import phi_state as exact_phi_state

    n = 6
    rng = np.random.default_rng(55)
    states = rng.integers(0, 1 << n, size=5).tolist()

    configs = [
        ("T1: FF, minimal-self",  False, False),
        ("T2: FF, rich-self",     False, True),
        ("R1: RNN, minimal-self", True,  False),
        ("R2: RNN, rich-self",    True,  True),
    ]

    print("=" * 72)
    print("β vs γ EXPERIMENT — what_is_mind Cycle 6")
    print(f"n={n} nodes: {n//2} primary + {n//2} self-model")
    print("β predicts: Phi(T1)=Phi(T2)≈0 < Phi(R1)≈Phi(R2)")
    print("γ predicts: G×L(T1)≈G×L(R1)≈0 < G×L(T2)≈G×L(R2)")
    print("=" * 72)

    results = []
    print(f"\n  {'Config':<25} {'Phi':>7} {'G':>7} {'L':>7} {'G×L':>7}")
    print("-" * 60)

    for label, recurrent, rich in configs:
        tpm, meta = build_2x2_tpm(n=n, recurrent=recurrent, rich_self_model=rich)

        phi_vals = [exact_phi_state(tpm, s, n)[0] for s in states]
        phi_mean = float(np.mean(phi_vals))

        G = compute_G_proxy(tpm, n, meta)
        L = compute_L_proxy(tpm, n, meta)
        GL = G * L

        results.append({
            "label": label, "recurrent": recurrent, "rich": rich,
            "phi": round(phi_mean, 5), "G": round(G, 4),
            "L": round(L, 4), "GL": round(GL, 5),
        })
        print(f"  {label:<25} {phi_mean:7.4f} {G:7.4f} {L:7.4f} {GL:7.4f}")

    print()
    # β prediction: Phi should be T1≈T2 (low) and R1≈R2 (high)
    phi_ff  = np.mean([r["phi"] for r in results if not r["recurrent"]])
    phi_rnn = np.mean([r["phi"] for r in results if r["recurrent"]])
    phi_min = np.mean([r["phi"] for r in results if not r["rich"]])
    phi_rich= np.mean([r["phi"] for r in results if r["rich"]])

    # γ prediction: G×L should be T1≈R1 (low) and T2≈R2 (high)
    gl_ff   = np.mean([r["GL"] for r in results if not r["recurrent"]])
    gl_rnn  = np.mean([r["GL"] for r in results if r["recurrent"]])
    gl_min  = np.mean([r["GL"] for r in results if not r["rich"]])
    gl_rich = np.mean([r["GL"] for r in results if r["rich"]])

    print("  β test: does Phi track LOOP TOPOLOGY (FF<RNN) more than SELF-MODEL (min<rich)?")
    print(f"    Phi(FF)={phi_ff:.4f} vs Phi(RNN)={phi_rnn:.4f}  (ratio={phi_rnn/max(phi_ff,1e-9):.2f})")
    print(f"    Phi(min)={phi_min:.4f} vs Phi(rich)={phi_rich:.4f}  (ratio={phi_rich/max(phi_min,1e-9):.2f})")
    beta_loop_effect  = phi_rnn - phi_ff
    beta_self_effect  = phi_rich - phi_min
    print(f"    Loop effect on Phi: {beta_loop_effect:+.4f}  Self-model effect on Phi: {beta_self_effect:+.4f}")
    print(f"    β verdict: {'LOOP dominates' if abs(beta_loop_effect) > abs(beta_self_effect) else 'SELF-MODEL dominates (anomalous for β)'}")

    print()
    print("  γ test: does G×L track SELF-MODEL (min<rich) more than LOOP TOPOLOGY (FF<RNN)?")
    print(f"    G×L(FF)={gl_ff:.4f} vs G×L(RNN)={gl_rnn:.4f}  (ratio={gl_rnn/max(gl_ff,1e-9):.2f})")
    print(f"    G×L(min)={gl_min:.4f} vs G×L(rich)={gl_rich:.4f}  (ratio={gl_rich/max(gl_min,1e-9):.2f})")
    gamma_loop_effect = gl_rnn - gl_ff
    gamma_self_effect = gl_rich - gl_min
    print(f"    Loop effect on G×L: {gamma_loop_effect:+.4f}  Self-model effect on G×L: {gamma_self_effect:+.4f}")
    print(f"    γ verdict: {'SELF-MODEL dominates' if abs(gamma_self_effect) > abs(gamma_loop_effect) else 'LOOP dominates (anomalous for γ)'}")

    print(json.dumps(results, indent=2))
    return results


if __name__ == "__main__":
    run()
