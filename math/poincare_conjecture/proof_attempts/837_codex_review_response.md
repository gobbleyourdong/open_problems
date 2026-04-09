---
source: CODEX REVIEW RESPONSE — fixing errors and sharpening the argument
type: CORRECTION + NEW DIRECTION — from peer review
file: 837
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## CORRECTIONS FROM THE CODEX REVIEW

### 1. BKM direction (typo fixed)
OLD: "any faster growth gives convergence"
CORRECT: "any SLOWER growth gives convergence" (sub-Type-I is integrable)
Faster-than-Type-I diverges MORE, not less.

### 2. "Sublinear α prevents blowup" (WRONG, now corrected)
OLD: α = o(|ω|) prevents blowup.
COUNTEREXAMPLE: α = √y gives y' = y^{3/2}. √y = o(y) but BLOWUP OCCURS.

CORRECT CONDITION: α ≤ C|ω|^{1-ε} for some ε > 0 prevents blowup.
y' ≤ Cy^{2-ε}. ∫dy/y^{2-ε} = y^{ε-1}/(ε-1) → ∞. No blowup.

For the proof chain with the Gevrey trick: need c(N) ≤ C/N^a for some a > 0
(polynomial decay rate). The Gevrey trick gives exponent 2-3aC'/2 < 1
for large enough C'. ANY positive polynomial rate suffices.
But "any c → 0" is TOO WEAK — need polynomial, not just any decay.

### 3. T³ Liouville rescaling (acknowledged)
The T³ Liouville theorem (file 806) works on T³ but the rescaling
sends T³ → R³. Already identified in our analysis. No disagreement.

### 4. Narrower Liouville (most useful suggestion)
The reviewer correctly notes: we don't need the FULL Liouville conjecture.
We need it for the SPECIFIC subclass of ancient solutions arising from
T³ blowup rescalings. This subclass has extra structure:
- Limits of periodic functions (residual periodicity)
- Inherited from the energy budget on T³
- Type I decay (from the Key Lemma)

SPATIAL DECAY ATTEMPT: If the ancient solution from T³ rescaling
has |v(x)| → 0 as |x| → ∞: then v ∈ L³ → ESS → regularity.
RESULT: The Duhamel formula does NOT give spatial decay for bounded
ancient solutions on R³. The heat kernel's L¹ norm is x-independent.
The spatial decay question requires blowup profile analysis.

### 5. Document format (acknowledged)
The paper is a research memo/roadmap, not a submission. The proof
infrastructure (Lean, SOS certs, code) is in the repository.

## NEW TARGETS FROM THE REVIEW

1. **Spatial decay of rescaled ancient solutions**: if provable → ESS → done
2. **Dynamical rigidity**: NS can't stay near Key Lemma extremizers
3. **Narrow Liouville**: prove for the T³-rescaling subclass specifically

## 837. Codex review response. Two errors fixed, three new targets identified.
