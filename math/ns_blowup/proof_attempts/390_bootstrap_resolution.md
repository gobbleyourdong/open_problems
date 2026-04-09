---
source: RESOLVING THE BOOTSTRAP — the continuation argument DOES close
type: PROOF — the formal argument for extending the barrier to T_max
file: 390
date: 2026-03-29
---

## THE BOOTSTRAP ARGUMENT

### Setup
Let u be a smooth NS solution on T³ with maximal existence time T_max.
Assume for contradiction: T_max < ∞.

### Step 1: Define the barrier set
T₁ = sup{t > 0 : R(s) = α(x*,s)/||ω||∞(s) < 1/2 for all s ∈ [0,t]}.

At t = 0: smooth data → |ω| bounded → α bounded → R(0) < 1/2
(or R(0) = 0 if |ω₀| = 0). So T₁ > 0.

### Step 2: On [0, T₁): the barrier gives Type I

For t ∈ [0, T₁): R(t) < 1/2 → α < ||ω||∞/2 → d||ω||∞/dt < ||ω||∞²/2.

Integrating: ||ω||∞(t) ≤ 2||ω||∞(0)/(2 - ||ω||∞(0)t) ≤ C₀/(T₁-t)
for some C₀ depending on initial data.

### Step 3: Type I gives analyticity

By the Foias-Temam theorem: on [0, T₁), the NS solution is analytic
in space with analyticity radius r(t) ≥ cν/||ω||∞(t) ≥ cν(T₁-t)/C₀ > 0.

Consequence: |ω̂_k(t)| ≤ C₁(t) e^{-r(t)|k|} for |k| large enough.

### Step 4: The K-shell bound

**HYPOTHESIS (K-shell certification)**: For all N ≥ 5 mode subsets of
{k ∈ Z³ : |k|² ≤ K₀²}, the regression bound gives:

    |∇u_head|²/|ω_head|² < 13/8 - δ₀

at the global max, for some δ₀ > 0 and fixed K₀.

(This is certified computationally: K₀² = 2 gives δ₀ ≈ 0.39. K₀² = 8
gives δ₀ ≈ 0.21 adversarially.)

### Step 5: At each t < T₁, the FULL field satisfies the barrier

**Claim**: For each t ∈ [0, T₁), S²ê(x*,t) < 3|ω(x*,t)|²/4.

**Proof of Claim**:

Fix t < T₁. The solution at time t has Fourier coefficients satisfying
|ω̂_k| ≤ C₁ e^{-r(t)|k|}. Decompose:

  ω = ω_≤ + ω_> (head: |k| ≤ K, tail: |k| > K)

where K = K(t) is chosen so that:

  ||ω_>||∞ ≤ δ₀ × ||ω||∞ / (4C₂)     (*)

where C₂ is a universal constant from the strain perturbation bound.

This is possible because ||ω_>||∞ ≤ C₁ Σ_{|k|>K} e^{-r(t)|k|} → 0 as K → ∞,
and r(t) > 0 (from Step 3).

Now: for the head modes (at most K³ modes, with N ≤ K³ active):

**Case A**: N ≤ 4 active head modes.
Per-mode bound (file 363): S²ê_head ≤ (N-1)|ω_head|²/4 ≤ 3|ω_head|²/4.
With H_ωω > 0: strict at N=4. Margin: at least some δ_A > 0.

**Case B**: N ≥ 5 active head modes with |k|² ≤ K₀².
K-shell certification (Step 4): |∇u_head|²/|ω_head|² < 13/8 - δ₀.
Trace-free: S²ê_head ≤ (2/3)(13/8-δ₀-1/2)|ω_head|² = (3/4 - 2δ₀/3)|ω_head|².

**Case C**: N ≥ 5 active head modes with some |k|² > K₀².
Choose K ≥ K₀. The modes with |k|² > K₀² are subdominant (they're
below the analyticity cutoff). Their contribution to the excess is O(ε).
The regression bound still applies to the K₀-subshell, with tail
from K₀ < |k| ≤ K absorbed by the margin.

In all cases: S²ê_head < (3/4 - δ)|ω_head|² for some δ > 0.

The tail perturbation: from (*) and standard estimates:
|S²ê_full - S²ê_head| ≤ C₂ × ||ω_>||∞ × ||ω||∞ ≤ δ₀|ω|²/4.

So: S²ê_full < (3/4 - δ + δ₀/4)|ω|².

For δ₀ small enough (δ₀ < 4δ): S²ê_full < 3|ω|²/4. ∎ (Claim proved.)

### Step 6: Extending the barrier

From Step 5: at each t < T₁, the barrier condition S²ê < 3|ω|²/4 holds.

From the barrier mechanism: DR/Dt < 0 at R = 1/2.

Since R(t) < 1/2 on [0, T₁) and R is continuous: R remains < 1/2 in a
neighborhood of T₁. So the barrier extends past T₁.

If T₁ < T_max: this contradicts the definition of T₁ = sup.

**Therefore: T₁ = T_max.**

### Step 7: Conclusion

On [0, T_max): R(t) < 1/2 → ||ω||∞ ≤ C/(T_max-t) (Type I).

By Seregin (2012): Type I blowup is impossible for NS on T³.

Contradiction with T_max < ∞. Therefore: **T_max = ∞. REGULARITY.** ∎


## KEY TECHNICAL POINTS

### Why the circularity resolves:

The argument is NOT circular because:
1. T₁ is defined as a SUPREMUM (not assumed to equal T_max)
2. At each t < T₁: the bound holds by the K-shell certification + tail decay
3. K(t) depends on t (through r(t)), but is FINITE at each t
4. The continuation extends T₁ past any t < T_max
5. T₁ = T_max follows from the supremum property

### What the computer-assisted certification provides:

The certification gives δ₀ > 0 (the margin at the K₀-shell). This δ₀ is
computed ONCE (for the K₀-shell) and applies at ALL times.

The time-dependent part is K(t) (the truncation level), which grows as
||ω||∞ grows. But K(t) only needs to satisfy (*), which is always possible
by analyticity.

### What remains for full rigor:

1. The K-shell certification with INTERVAL ARITHMETIC (not just floating-point)
2. Explicit computation of C₂ (the strain perturbation constant)
3. Verification that the continuation argument extends R continuously

Items 1-2 are computational. Item 3 is standard PDE analysis.


## 390. CORRECTION: THE BOOTSTRAP DOES NOT FULLY CLOSE.

### The gap in Case C:
Near blowup (t → T_max): the analyticity radius r(t) → 0.
All modes with |k| > K₀ become fully activated (relative tail ~ 1/r³ → ∞).
The K₀-shell certification cannot control these modes.

### What IS proven:
- The continuation argument is correct for the per-mode bound (N ≤ 4 head modes)
- The K-shell certification is valid but only covers FINITE K₀

### What FAILS:
- Case C assumes modes beyond K₀ are "subdominant" — FALSE near blowup
- The tail ε(t)/||ω||∞ → ∞ as r(t) → 0
- The bootstrap circularity is NOT resolved by K-shell certification

### What's needed:
- Prove the regression bound ANALYTICALLY for all N (eliminates truncation)
- OR prove an a priori estimate on the effective mode count
- OR use a fundamentally different approach (self-attenuation alignment?)

### HONEST STATUS:
The proof is COMPLETE for N ≤ 4 modes (unconditional).
For general smooth fields: the bootstrap has a GAP at the K-shell extension.
The gap = proving S²ê < 3|ω|²/4 for arbitrarily many modes.
