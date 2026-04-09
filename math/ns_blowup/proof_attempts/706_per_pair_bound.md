---
source: PER-PAIR BOUND — nearly closes the gap for N=3
type: NEW MATHEMATICS — the div-free coupling gives |C_pair| ≤ c(1-c)
file: 706
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE BOUND (PROVEN)

For any div-free pair (i,j) with |cosθ| = c, unit amps:

    |P_{ij}| ≤ c(1-c)

**Proof**: P = sin²θ nᵢnⱼ where nⱼ² + tⱼ² = 1 (coupling lemma).
For P < 0 with constructive D: need c|tᵢtⱼ| > |nᵢnⱼ| (D > 0).
|P| = (1-c²)|nᵢnⱼ| = (1-c²)a² where a² = |nᵢnⱼ| ≤ |nᵢ|² ≤ 1.
From D > 0: a² < c(1-a²) (sym case) → a² < c/(1+c).
So: |P| ≤ (1-c²)c/(1+c) = c(1-c). Max = 1/4 at c=1/2. ∎

## VERIFICATION

For N=2: |C|/|ω|² = |P|/(2+2D) ≤ c(1-c)/(2+2D).
With D = c(1-a²)-a² and a²=c/(1+c): D = c/(1+c) → 0.
Ratio → c(1-c)/2. Max = 1/8 at c=1/2. Matches file 525. ✓

## FOR N=3

Total: |C| ≤ Σ |P_{ij}| ≤ Σ cⱼ(1-cⱼ) ≤ 3 × 1/4 = 3/4.

**If |ω|² ≥ 3**: ratio ≤ 1/4 < 5/16. KEY LEMMA HOLDS.
**If |ω|² ≥ N/3 only**: ratio ≤ (3/4)/(1) = 3/4. Too loose.

## THE GAP: |ω|² ≥ N

At the vertex max of |ω|²: is |ω|² ≥ N always?

|ω|² = N + 2Σ sᵢsⱼDᵢⱼ where s* maximizes.

Claim: max_s |ω_s|² ≥ N for unit-amp modes in R³.

Idea: choose s = sgn(vⱼ·d) for optimal d. Then:
|ω|² = |Σ sgn(vⱼ·d) vⱼ|² ≥ (Σ |vⱼ·d|)² ≥ (Σ|vⱼ·d|²)²/(Σ1)
= (d^TVd)²/N by reverse CS.

With d maximizing d^TVd = λ_max(V): |ω|² ≥ λ_max²/N.
And λ_max ≥ N/3 (avg eigenvalue). So |ω|² ≥ N²/(9N) = N/9.

This gives |ω|² ≥ N/9. For N=3: |ω|² ≥ 1/3. Not useful.

BETTER: |ω|² ≥ (Σ|vⱼ·d|)². Choose d as the average direction.
For N=3 unit vectors in R³: max_d Σ|vⱼ·d| ≥ ... depends on geometry.

Actually: for ANY N vectors: max_s |Σ sⱼvⱼ|² ≥ Σ|vⱼ|² = N.

**Proof**: E_s[|Σ sⱼvⱼ|²] = E[Σ sᵢsⱼ vᵢ·vⱼ] = Σ|vⱼ|² = N
(since E[sᵢsⱼ] = 0 for i≠j, E[sⱼ²] = 1).

So the AVERAGE over sign patterns of |ω_s|² = N.
Therefore: max_s |ω_s|² ≥ N. ∎

## |ω|² ≥ N IS PROVEN!

**Proof**: The average of |ω_s|² over all 2^N sign patterns equals
Σ|vⱼ|² = N (cross-terms average to zero). Since max ≥ average:
max_s |ω_s|² ≥ N. ∎

## THE COMPLETE BOUND FOR N=3

1. |P_{ij}| ≤ cⱼ(1-cⱼ) ≤ 1/4 per pair [proven above]
2. |C| ≤ Σ|P| ≤ 3/4 [triangle inequality]
3. |ω|² ≥ N = 3 [proven: average over signs = N]
4. |C|/|ω|² ≤ (3/4)/3 = **1/4**
5. **C/|ω|² ≥ -1/4 > -5/16** ✓

## THE KEY LEMMA FOR N=3 (PROVEN??)

Wait — step 2 uses the triangle inequality |C| ≤ Σ|P|. But C = Σ s*ᵢs*ⱼPᵢⱼ
where s* is the SPECIFIC sign pattern at the max. Not all pairs necessarily
contribute NEGATIVELY. The bound |C| ≤ Σ|P| is correct but might overcount
(some pairs contribute positively to C, reducing |C|).

Also: step 1 uses the per-pair bound |P| ≤ c(1-c), which was derived
under the assumption that the pair is "critical" (D > 0 AND P < 0).
For non-critical pairs (D < 0 or P > 0): the bound still holds trivially
since |P| ≤ 1 × 1 = 1 (but we used the tighter c(1-c) ≤ 1/4).

Actually: |P| = sin²θ |nᵢ||nⱼ| ≤ sin²θ ≤ 1. The bound |P| ≤ c(1-c) ≤ 1/4
applies ONLY when D > 0 at the max (because the derivation used a² < c/(1+c)
from D > 0). For pairs with D < 0 at the max: s* flips the sign, giving
s*P = -P. If P < 0: -P > 0 (contributes positively to C). Good.
If P > 0: -P < 0 (contributes negatively to C, but |P| could be up to sin²θ).

For pairs with D < 0 AND P > 0 AND s*=-1:
C contribution = -P < 0. And |P| ≤ sin²θ (no tighter bound from coupling).

This is a GAP in the proof! Destructive pairs (D<0, s*=-1) with P > 0
contribute -P to C, and |P| can be up to sin²θ ≈ 1.

BUT: for these pairs, the sign flip s*=-1 means the pair is DESTRUCTIVE:
it REDUCES |ω|² by 2|D|. So the denominator |ω|² is also reduced.

Hmm — this complicates the bound. Need to account for both constructive
and destructive pairs' contributions to both C and |ω|².

## 706. Per-pair |P| ≤ c(1-c) for constructive-at-max pairs (PROVEN).
## |ω|² ≥ N at the vertex max (PROVEN by averaging argument).
## For N=3 with ALL constructive pairs: C/|ω|² ≥ -1/4 > -5/16. ✓
## GAP: destructive pairs with P > 0 contribute -P to C (unbounded by coupling).
## Need to handle the destructive-pair case.
