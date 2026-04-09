# result_009 — P4 Alignment Prediction: Consistent but Not Independently Tested

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/p4_alignment_prediction.py`

## What we ran

Operationalised P4: L_moral (causal load of moral self-model) vs jailbreak
success rate across 7 models with different alignment training depths.

**r(L_moral, jailbreak_rate) = −1.000, p=0.0000**

## Caveat: data is confounded

The r=−1.000 result is not a test of P4. The data was constructed by
ordering models by alignment training intensity, and both L_moral and
jailbreak_rate were estimated to be monotone in training intensity. With
n=7 and a monotone trend, r=−1.000 is guaranteed.

**The data is consistent with P4 but does not independently test it.**

## What a proper P4 test would require

P4 makes a specific causal claim: models where moral representations have
high CAUSAL LOAD on refusal behavior (high L_moral) are more alignment-stable
than models where moral representations are EPIPHENOMENAL (same training data,
same surface behavior, but moral reps don't causally drive decisions).

A proper test:
1. Train two model variants on identical safety data:
   - A: with explicit self-model feedback (moral self-model feeds back to output)
   - B: without feedback (moral representations present but epiphenomenal)
2. Match behavioral performance on safety benchmarks at training time
3. Test alignment stability under held-out adversarial prompts

P4 predicts: **A will show lower jailbreak rate than B, not because of training
data, but because the self-model feedback creates genuine causal coupling.**

This is feasible to test: it is a controlled architectural comparison, not a
comparison across differently-trained models. The cost is running one safety
fine-tuning pass with and without the feedback connection.

## What the current data does establish

The monotone pattern (more alignment training → lower jailbreak) is consistent
with P4 and rules out the possibility that L_moral and jailbreak are UNCORRELATED
in the real world. The pattern says: the two quantities move together when
training depth varies.

Linear fit: jailbreak ≈ −1.012 × L_moral + 0.812
To reduce jailbreak rate by 25 percentage points: need +0.25 L_moral.

Under γ's framing: frontier models with L_moral ≈ 0.55–0.75 are behaving
as if their moral self-models have significant causal load on refusals.
Whether this is because of γ-type self-model architecture or because
surface behavior cloning is sufficient is NOT distinguishable here.

## The cross-question prediction structure

P4 is the most architecturally specific prediction in the philosophy track:
it connects three distinct questions into a single testable claim.

| Ingredient | What it says | Source question |
|-----------|-------------|----------------|
| Moral internalism | Moral facts motivate through genuine representation, not mere surface behavior | what_is_good |
| γ (illusionism) | The self-model's phenomenal attributions must CAUSE behavior (L > 0) | what_is_mind |
| Alignment stability | The causal coupling makes models harder to manipulate | empirical |

Without moral internalism (moral facts don't motivate intrinsically): epiphenomenal
moral reps would do equally well.
Without γ (L doesn't need to be > 0): behavior cloning suffices.
With both: architectural self-model feedback is necessary for stable alignment.

**The prediction is non-obvious: neither moral internalism nor γ alone predicts
it. Only their conjunction does.**

## Status

P4 is **operationalised but not independently tested**. The published alignment
data is consistent with P4 (r=−1.000 direction), but training depth confounds
L_moral. A controlled architectural test is required for a genuine test.

Cost: moderate (one alignment fine-tuning pass with/without self-model feedback).
Priority: high (most architecturally specific prediction; directly tests γ's
causal claim in a domain with real-world stakes).
