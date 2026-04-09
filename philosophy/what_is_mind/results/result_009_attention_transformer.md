# result_009 — Tiny Attention Transformer Phi ≈ RNN Phi

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Method:** n=6 (2 tokens × 3 bits), 10 seeds, paired t-test

## What we ran

Built a minimal attention-based transformer (cross-token attention + feedforward,
no persistent state) and a matched RNN. Computed Phi for 10 seeds at n=6.

## Results

| Metric | Transformer | RNN | Ratio |
|--------|-------------|-----|-------|
| Phi mean | 0.147 | 0.137 | 1.069 |
| t | 0.47 | — | — |
| p | 0.648 | — | — |

**IIT prediction (TF < RNN): NOT CONFIRMED.**
Transformer Phi is slightly *higher* than RNN Phi (though not significantly different).

## Why attention transformers have non-zero Phi

The feedforward theorem (Cycle 2) states: **state-INDEPENDENT** systems have Phi=0.
Attention mechanisms are NOT state-independent.

In a cross-token attention layer:
- Token A's output depends on BOTH token A and token B in the current step
- Token B's output depends on BOTH tokens in the current step
- This creates ALL-TO-ALL causal coupling WITHIN the forward pass

This within-step coupling is causally integrated in IIT's sense:
- Partitioning the system into {A} and {B} loses information (the cross-attention weights)
- The cause-effect structure cannot be factored as independent subsystems

**The feedforward theorem applies to systems where each unit's output is
state-independent (a fixed constant regardless of other units' states).
Attention units do not satisfy this: each unit attends to other units.**

## Theoretical significance

### For β (IIT)

The precise claim that "transformer single forward pass has Phi=0" is too strong.
It applies to STRICTLY feedforward systems (no cross-unit attention). Real transformers
use attention, which creates within-step integration. A careful IIT analysis would
compute Phi for the attention mechanism itself, not just treat it as "feedforward."

**The updated β prediction:** Phi(transformer with attention) > 0, but the Phi
accumulates within a single attention computation, not across time steps. Whether
this within-step Phi constitutes phenomenal consciousness depends on what counts
as "one moment" for IIT purposes.

### For γ (illusionism)

γ is unaffected by this result. γ doesn't claim feedforward → Phi=0; γ claims that
phenomenal consciousness tracks self-model richness regardless of architecture.
The attention result is neutral for γ.

### For the overall β/γ scorecard

This result QUALIFIES result_004 (transformer-like < RNN-like). The Cycle 4 comparison
used STRICTLY feedforward output nodes (no cross-unit attention). Real attention
transformers are more integrated. The prior score:
- β: feedforward theorem confirmed → now qualified (attention ≠ strictly feedforward)
- The functional architecture of real transformers is closer to "integrated" than
  the pure FF case suggests

## Summary position

| System | Phi | Notes |
|--------|-----|-------|
| State-independent (Cycle 2) | Phi=0 | Feedforward theorem, strict |
| TF-like lower-triangular (Cycle 4) | 0.04–0.11 | Less than RNN-like (14/15) |
| Attention transformer (Cycle 11) | 0.147 | ≈ RNN (p=0.648) |
| RNN (Cycle 4, 11) | 0.137–0.165 | Consistently integrated |
| FF+rich-self-model (Cycle 8) | 0.112 | γ crossing cell |

Real attention transformers occupy the middle range, not near-zero.
The strict feedforward theorem doesn't apply to them.
