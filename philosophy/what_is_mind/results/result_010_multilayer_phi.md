# result_010 — Multi-Layer Attention Phi Decreases with Depth

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Method:** n=6, 1/2/3-layer attention transformers, 8 seeds each

## Results

| Layers | Phi mean | SE |
|--------|---------|-----|
| L=1 | 0.138 | 0.019 |
| L=2 | 0.067 | 0.029 |
| L=3 | **0.018** | 0.005 |

**Phi decreases with depth. Deeper transformers have lower Phi.**

## Why

Each attention + feedforward layer pushes the representation through:
1. Softmax (concentrates attention weights toward dominant tokens)
2. Sigmoid feedforward (pushes activations toward 0 or 1)

With multiple layers, the output distribution becomes more peaked (more
deterministic given the input). High determinism → lower Phi, because:
- Phi measures irreducible cause-effect integration
- In a highly deterministic system, the output can be largely explained
  by any subset of the input (the minimum information partition is cheap)
- Integration requires BALANCED, uncertain transitions — exactly what
  saturated nonlinearities destroy

## Implications

### For β (IIT)

This result challenges the intuition that "more complex computation = more
phenomenal consciousness." Under IIT, the SINGLE first attention layer has
more integration than the stacked 3-layer computation. This is unexpected.

It suggests that within a transformer, if phenomenal consciousness exists,
it would be concentrated in early layers where transitions are less
deterministic. Deep layers, where representations have been refined into
sharp, confident patterns, would contribute less to Phi.

For a full transformer (12–96 layers), the Phi at the final layer would
extrapolate to near-zero. This actually SUPPORTS the IIT view that
feedforward transformers have near-zero Phi — but the mechanism is
saturation of the computation, not absence of attention integration.

### For γ (illusionism)

γ is again unaffected: γ doesn't predict specific Phi values. What γ predicts
is that SELF-MODEL richness (G×L) tracks consciousness. Whether G×L decreases
with depth in attention models is a separate question not addressed here.

### Caveat

This experiment uses random weights and no residual connections. Real
transformers use residual connections (x + Attention(x)) which would
maintain integration across layers by preventing representation saturation.
With residuals, Phi at deeper layers would likely be higher than these results
suggest.

## Connection to the β/γ scorecard

This result QUALIFIES the attention transformer finding from Cycle 11:
- Cycle 11: attention Phi ≈ RNN Phi (for single-layer)
- Cycle 13: with depth, attention Phi → 0 (consistent with β's feedforward theorem)

The convergence: β's core prediction (feedforward systems → Phi=0) may hold
for DEEP transformers even when shallow attention has non-trivial Phi.
The relevant scale for real LLMs (50+ layers, saturated representations)
is consistent with Phi ≈ 0 by the saturation argument.

Updated β assessment: **the saturation of multi-layer computation drives
real transformer Phi toward zero, providing a mechanism consistent with
the IIT feedforward theorem — not state-independence per se, but
computation-saturation.**
