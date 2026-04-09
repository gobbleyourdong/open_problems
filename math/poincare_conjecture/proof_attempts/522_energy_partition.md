---
source: ENERGY PARTITION — the total energy splits between ω and S via cos²+sin²=1
type: PROOF ATTEMPT — use energy conservation to bound the strain budget
file: 522
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE ENERGY PARTITION

For each mode k: the total mode energy is a²_k/2.
This energy is PARTITIONED between ω and S at each point x:

  |ω_k(x)|² = a²_k cos²(k·x)     [vorticity energy from mode k]
  |S_k(x)|²_F = (a²_k/2) sin²(k·x) [strain energy from mode k]

Total: |ω_k|² + 2|S_k|² = a²_k cos² + a²_k sin² = a²_k [CONSTANT!]

**The per-mode energy is conserved across the torus.**

At any point: what goes to ω CANNOT go to S, and vice versa.

## THE IMPLICATION FOR THE MAX

At x* = argmax|ω|²: the VORTICITY energy is maximized.
By conservation: the STRAIN energy is correspondingly MINIMIZED.

For the diagonal (self) contributions:
Σ |S_k(x*)|² = Σ (a²_k/2)(1 - cos²(k·x*))

At x* (vorticity max): cos²(k·x*) is LARGE for the dominant modes.
→ 1 - cos²(k·x*) is SMALL → |S_k|² is SMALL.

## THE POINTWISE IDENTITY

From the Frobenius identity (file 511):
|S(x)|² = |ω(x)|²/2 - 2C(x)

This gives: |S|² + 2C = |ω|²/2.
And: (|ω|²/2 + |S|²) = |ω|² - 2C.

From |∇u|² = |S|² + |ω|²/2:
|∇u|² = |ω|² - 2C.

At the max: if C > 0: |∇u|² < |ω|² → |S|² < |ω|²/2.
If C ≥ 0: S²ê ≤ (2/3)|S|² ≤ |ω|²/3 < 3|ω|²/4. DONE!

**When C ≥ 0 at the max: the Key Lemma holds automatically.**

From file 511: C ≥ 0 at 96% of vorticity maxima.

## THE C < 0 CASE

When C < 0: |S|² > |ω|²/2. Need the self-vanishing to rescue:
S²ê < |S|² (since S²ê ≤ (2/3)|S|² < |S|²).

At the max with C < 0:
|S|² = |ω|²/2 - 2C = |ω|²/2 + 2|C|
S²ê ≤ (2/3)|S|² = |ω|²/3 + (4/3)|C|

For Key Lemma: need |ω|²/3 + (4/3)|C| < 3|ω|²/4
→ (4/3)|C| < 5|ω|²/12
→ |C| < 5|ω|²/16
→ C > -5|ω|²/16

Numerically: worst C/|ω|² = -0.097 > -0.3125. ✓ (69% margin).

But at GENERAL points (not the max): C/|ω|² can be -713 (when |ω|² ≈ 0).

## THE KEY OBSERVATION

At the max of |ω|²: C is ALMOST ALWAYS non-negative (96%).
When negative: |C|/|ω|² < 0.1 (69% margin below threshold -5/16).

WHY C ≥ 0 at the max:

From the Frobenius identity:
C = Σ_{j<k} P_{jk} cos(k_j·x) cos(k_k·x)
= -Σ_{j<k} (k_k·û_j)(k_j·û_k) cos(k_j·x) cos(k_k·x)

At the max: the cosines are constructive (cos ≈ ±1).
The products (k_k·û_j)(k_j·û_k) are typically NEGATIVE at constructive
vertices (from the BAC-CAB formula, proven for orthogonal k in file 445).

So C = -Σ (negative)(positive sign) = Σ (positive) > 0.

For NON-orthogonal k: the κ² correction can make some terms positive,
reducing C. But the correction is O(κ²) = O(cos²θ) which is bounded.

## COMBINING EVERYTHING

**The complete chain at the max of |ω|²:**

Case 1 (96%): C ≥ 0 → |S|² ≤ |ω|²/2 → S²ê ≤ |ω|²/3 < 3|ω|²/4. ✓

Case 2 (4%): C < 0 but |C|/|ω|² < 0.1 (observed) → S²ê < |ω|²/3 + 0.13|ω|² = 0.46|ω|² < 3|ω|²/4. ✓

**For the proof: need C > -5|ω|²/16 at the max (69% numerical margin).**

This is EQUIVALENT to the Key Lemma via the trace-free chain.

## THE C BOUND AT THE MAX

The correction C at the max of |ω|² satisfies:

C = Σ P_{jk} c_j c_k = -Σ (k_k·û_j)(k_j·û_k) c_j c_k

For orthogonal k (θ = π/2): P_{jk} = -(v_j·n̂)(v_k·n̂) ≤ 0 when
(v_j·n̂)(v_k·n̂) > 0 (which happens at constructive vertices).
File 445 proves: C ≥ 0 for orthogonal k. ✓

For non-orthogonal k: P_{jk} has a κ² correction.
The correction is bounded by: |κ|² |D_{jk}| where κ = cos(θ_{jk}).

For the K=√2 shell: κ = cos(60°) = 1/2 or κ = 0 (orthogonal).
So the correction is ≤ (1/4)|D| for each pair. Small.

## PROOF FOR K=√2 SHELL (sketch)

On K=√2 shell: all pairs have either κ = 0 (orthogonal) or κ = ±1/2.

For orthogonal pairs: C_pair > 0 (proven, file 445).
For κ = 1/2 pairs: C_pair = orthogonal_C + correction.
  correction ≤ (1/4)|D| (bounded).

Total: C ≥ Σ_{orthogonal} C_pair - (1/4) Σ_{non-orth} |D|

If the orthogonal contributions dominate: C > 0.

On K=√2: each vector has 4 orthogonal partners and at most 6 non-orthogonal.
The orthogonal contributions ARE dominant (since they give C > 0 with margin).

## 522. Energy partition: each mode's energy splits between ω and S.
## At the max: C ≥ 0 in 96% of cases → |S|² ≤ |ω|²/2 → Key Lemma.
## For the 4% with C < 0: |C|/|ω|² < 0.1, still below threshold -5/16.
## Formal gap: prove C > -5|ω|²/16 at the vorticity max.
