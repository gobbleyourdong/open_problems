"""
phi_transformer_vs_rnn.py — Cycle 4
Numerical Track: what_is_mind

Build the smallest possible transformer-like and RNN-like binary networks
and compare their Phi values.

"Transformer-like" means: computation in each step is state-independent
(the forward pass produces output deterministically from input, no internal
state that feeds back). At each step the "state" is just the current token;
the model is a fixed function mapping input → output.

"RNN-like" means: each step's computation depends on a hidden state that
is passed forward from the previous step. The hidden state IS internal state
that evolves.

Since we're working with binary n-node networks:

Transformer-like (n=4, 2 input + 2 output, no hidden state):
  Nodes 0,1: "input" — state-independent (P(x'=1) = fixed constant)
  Nodes 2,3: "output" — depend on nodes 0,1 in current step, but not on 2,3
  This is a 2-layer feedforward network. IIT predicts: Phi = 0 or very small.

RNN-like (n=4, 2 input + 2 hidden state):
  Nodes 0,1: input (same as above)
  Nodes 2,3: hidden state — depend on nodes 0,1 AND 2,3 from current step
  This is recurrent. IIT predicts: Phi > 0.

We construct both and measure Phi.
"""

import math
import numpy as np
from phi_small_systems import phi_state


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -20, 20)))


def build_transformer_like(n: int = 6, seed: int = 42) -> np.ndarray:
    """
    Transformer-like n-node network.

    Architecture: n//2 input nodes + n//2 output nodes.
    Input nodes: state-INDEPENDENT (constant activation probability)
    Output nodes: depend only on input nodes (not on other output nodes, not on self)

    This is the canonical IIT feedforward case.
    Phi prediction: = 0 (or near-0 if we add small noise to input-state independence)
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n
    n_in = n // 2
    n_out = n - n_in

    # Fixed probs for input nodes
    input_probs = rng.uniform(0.2, 0.8, n_in)

    # Weights for output nodes (only from input nodes)
    W_out = rng.normal(0, 1.5, (n_out, n_in))
    b_out = rng.normal(0, 0.1, n_out)

    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state = np.array([(s >> j) & 1 for j in range(n)], dtype=float)
        input_state = state[:n_in]
        output_probs = sigmoid(W_out @ input_state + b_out)

        for s2 in range(n_states):
            prob = 1.0
            for i in range(n_in):
                bit = (s2 >> i) & 1
                p = input_probs[i]
                prob *= p if bit == 1 else (1 - p)
            for i in range(n_out):
                bit = (s2 >> (n_in + i)) & 1
                p = output_probs[i]
                prob *= p if bit == 1 else (1 - p)
            tpm[s, s2] = prob

    return tpm


def build_rnn_like(n: int = 6, seed: int = 42) -> np.ndarray:
    """
    RNN-like n-node network.

    Architecture: n//2 input nodes + n//2 hidden state nodes.
    Input nodes: state-INDEPENDENT (same as above, same seed)
    Hidden nodes: depend on input nodes AND hidden state nodes (recurrent)

    This is the canonical RNN case.
    Phi prediction: > 0 due to hidden state integration.
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n
    n_in = n // 2
    n_hid = n - n_in

    # Fixed probs for input nodes (SAME as transformer variant)
    input_probs = rng.uniform(0.2, 0.8, n_in)

    # Weights for hidden nodes: depend on input AND hidden state
    W_from_input  = rng.normal(0, 1.5, (n_hid, n_in))
    W_recurrent   = rng.normal(0, 1.0, (n_hid, n_hid))  # recurrent weights
    b_hid         = rng.normal(0, 0.1, n_hid)

    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state = np.array([(s >> j) & 1 for j in range(n)], dtype=float)
        input_state  = state[:n_in]
        hidden_state = state[n_in:]

        hidden_probs = sigmoid(W_from_input @ input_state +
                               W_recurrent @ hidden_state + b_hid)

        for s2 in range(n_states):
            prob = 1.0
            for i in range(n_in):
                bit = (s2 >> i) & 1
                p = input_probs[i]
                prob *= p if bit == 1 else (1 - p)
            for i in range(n_hid):
                bit = (s2 >> (n_in + i)) & 1
                p = hidden_probs[i]
                prob *= p if bit == 1 else (1 - p)
            tpm[s, s2] = prob

    return tpm


def mean_phi(tpm: np.ndarray, n: int, n_samples: int = 8, seed: int = 99) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    states = rng.integers(0, 1 << n, size=n_samples).tolist()
    phis = [phi_state(tpm, s, n)[0] for s in states]
    return float(np.mean(phis)), float(np.max(phis))


def tpm_entropy(tpm: np.ndarray) -> float:
    H = 0.0
    for row in tpm:
        H += -sum(p * math.log2(p) for p in row if p > 0)
    return H / len(tpm)


def run():
    import json

    print("=" * 72)
    print("TRANSFORMER-LIKE vs RNN-LIKE Phi — what_is_mind Cycle 4")
    print("Transformer: state-independent input + feedforward output (IIT Phi=0 pred)")
    print("RNN:         state-independent input + recurrent hidden state (IIT Phi>0)")
    print("=" * 72)

    results = []
    for n in [4, 5, 6]:
        for seed in range(5):
            tf_tpm = build_transformer_like(n, seed=seed)
            rn_tpm = build_rnn_like(n, seed=seed)

            tf_mean, tf_max = mean_phi(tf_tpm, n)
            rn_mean, rn_max = mean_phi(rn_tpm, n)
            tf_H = tpm_entropy(tf_tpm)
            rn_H = tpm_entropy(rn_tpm)

            results.append({
                "n": n, "seed": seed,
                "tf_phi": round(tf_mean, 5),
                "rn_phi": round(rn_mean, 5),
                "tf_H": round(tf_H, 3),
                "rn_H": round(rn_H, 3),
                "confirmed": tf_mean < rn_mean,
            })

    print(f"\n  n  seed  TF_H   RN_H  TF_Phi  RN_Phi  TF<RN?")
    print("-" * 55)
    for r in results:
        print(
            f"  {r['n']}  {r['seed']}     {r['tf_H']:.3f}  {r['rn_H']:.3f}  "
            f"{r['tf_phi']:.4f}  {r['rn_phi']:.4f}  {'YES' if r['confirmed'] else 'NO '}"
        )

    confirmed = sum(r["confirmed"] for r in results)
    total = len(results)
    print(f"\n  IIT prediction confirmed: {confirmed}/{total}")

    # Summary by n
    for n in [4, 5, 6]:
        sub = [r for r in results if r["n"] == n]
        tf_mean = np.mean([r["tf_phi"] for r in sub])
        rn_mean = np.mean([r["rn_phi"] for r in sub])
        print(
            f"  n={n}: TF_Phi={tf_mean:.4f}  RN_Phi={rn_mean:.4f}  "
            f"ratio={tf_mean/max(rn_mean,1e-9):.3f}  "
            f"IIT: {'CONFIRMED' if tf_mean < rn_mean else 'NOT CONFIRMED'}"
        )

    print(json.dumps(results, indent=2))
    return results


if __name__ == "__main__":
    run()
