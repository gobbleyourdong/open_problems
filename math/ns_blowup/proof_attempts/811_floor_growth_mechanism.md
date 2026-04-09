---
source: WHY DOES f(N) DECAY AS N^{-3}? — the mechanism behind floor growth
type: ANALYSIS + PROOF ATTEMPT — trying to prove f(N) ≤ C/N^a analytically
file: 811
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE DATA

f(N) = 9 - min(Q/|ω|²) over all N-mode configurations at argmax:

| N | Q/|ω|² | f(N) |
|---|--------|------|
| 3 | 2.25 | 6.75 |
| 4 | 5.55 | 3.45 |
| 5 | 7.94 | 1.06 |
| 6 | 8.22 | 0.78 |
| 7 | 8.45 | 0.55 |

Power-law fit: f(N) ~ 212/N^{3.12}. Exponent a ≈ 3.

## WHAT f(N) MEASURES

f(N) = 8|S|²_worst/|ω|²_worst

where worst means the configuration (k-vectors, polarizations) that
MAXIMIZES |S|²/|ω|² at the argmax of |ω|².

Equivalently: f(N) measures the WORST-CASE strain-to-vorticity ratio.

## THREE MECHANISMS FOR FLOOR GROWTH

### Mechanism 1: Self-Vanishing Dilution

Each mode j has self-contribution |Sⱼ·ê|² = (aⱼ²/4)sin²γⱼ.
But Sⱼ has N-1 cross-terms with other modes.

The self-vanishing removes the DIAGONAL of the S·ê sum.
S·ê = Σⱼ Sⱼ·ê is a sum of N terms, each bounded by 1/2.

|S·ê|² ≤ (N/2)² = N²/4 (worst case: all aligned)

But |ω|² ≥ N (from dimension argument for N ≥ 4).

So S²ê/|ω|² ≤ N²/(4N) = N/4.
And (3/4)|ω|² ≥ 3N/4.

Ratio: (N/4)/(3N/4) = 1/3. This is CONSTANT, not decaying.

**Mechanism 1 alone doesn't give f(N) → 0.**

### Mechanism 2: Direction Spread in ê⊥

The vectors Sⱼ·ê lie in the plane ê⊥ ≅ R².
With N vectors nⱼ in R²:

|Σ nⱼ|² = Σ|nⱼ|² + 2Σ_{j<k} nⱼ·nₖ = N + 2Σ cos(θⱼ - θₖ)

For the WORST case (all aligned): |Σ nⱼ|² = N².
For N random directions: |Σ nⱼ|² ≈ N (CLT).

The directions nⱼ are determined by the k-vectors through Biot-Savart.
For N ≥ 4 modes on T³: the non-parallel theorem says the nⱼ can't
all be parallel. This forces some angular spread.

With spread: |Σ nⱼ|² ≤ N² - c·N (correction of order N from spread).
So S²ê ≤ (N² - cN)/4.

Ratio: S²ê / ((3/4)|ω|²) ≤ (N² - cN)/(3N) → N/3 → ∞.

**Mechanism 2 alone doesn't help: |ω|² grows only as N, not N².**

### Mechanism 3: Argmax Phase Constraint (THE KEY)

At the argmax of |ω|²: ∇|ω|² = 0 ↔ 3 equations on N phases.

For N > 3: the phases are OVERDETERMINED. The argmax condition
constrains the phases, which constrains the cross-terms.

The vorticity at the argmax: |ω|² = N + 2Σ sⱼsₖ Dⱼₖ cos(phase terms).
At the argmax: the cosines are at their MAXIMA (phases align).
This means the cross-terms Dⱼₖ contribute MAXIMALLY to |ω|².

But the STRAIN cross-terms don't align as well. The strain involves
DIFFERENT phase factors (shifted by π/2 from the vorticity). At the
argmax of |ω|², the strain phases are NOT at their maxima.

The mismatch: ω involves cos(k·x), S involves sin(k·x) (90° phase shift).
At the argmax of |ω|²: cos(k·x) terms are maximized → sin(k·x) terms
are at zero or near zero!

**This is the phase suppression mechanism from file 523 (corrected).**

For N modes at the argmax: each sin(kⱼ·x*) ≈ 0 (the cosine terms
are maximized, so the sine terms are near their zeros). The strain
involves these sine terms, so the strain is SUPPRESSED at the argmax.

More precisely: at x* = argmax|ω|²:
- ωⱼ(x*) = kⱼ × pⱼ (no phase: cos(kⱼ·x* + φⱼ) = 1 at argmax)
- Sⱼ(x*) involves sin(kⱼ·x* + φⱼ) = 0 (90° shifted)

Wait, this isn't quite right. The phases φⱼ adjust so that ωⱼ(x*)
is at its maximum contribution. But the Fourier phase of the STRAIN
is shifted. Let me reconsider.

For a single mode: u_k = a sin(k·x + φ) (k × p)
ω_k = a |k| cos(k·x + φ) (k × p) × k / |k| ... no, this depends
on the specific form. Let me use the correct form.

For a divergence-free mode: u_k(x) = a_k (I - k̂k̂ᵀ) p_k sin(k·x + φ_k)
ω_k = ∇ × u_k = a_k |k| (k̂ × p_k) cos(k·x + φ_k)
S_k = (1/2)(∇u_k + ∇u_kᵀ) involves cos(k·x + φ_k) ... wait,
∂u/∂x involves cos(k·x + φ_k) · k, so S also involves cos.

Hmm, I need to check the phase relationship. From file 523 (corrected):
both ω and S involve cos(k·x + φ), NOT sin. The "sine-cosine decoupling"
was WRONG (this was the phase error fixed in file 523).

So the phase suppression mechanism is NOT as described above. Both ω and S
involve the SAME trigonometric function at x*. There's no 90° phase shift.

## REVISED UNDERSTANDING

The decay of f(N) is NOT from phase suppression (which was wrong).
The actual mechanisms must be:

1. **Direction spread**: more modes → more diverse nⱼ → |Σ nⱼ|² < N²
2. **|ω|² growth**: more modes → |ω|² grows faster than N (cross-terms add)
3. **Phase constraints**: argmax pins phases, limiting strain cross-terms

The ratio S²ê/|ω|²: the numerator grows at most as N² (all aligned),
while the denominator grows as... what?

At the WORST configuration: |ω|² is minimized (to make the ratio large).
But the SOS certificates test ALL configurations. The worst ratio occurs
when |ω|² is small AND |S|² is large simultaneously.

For the Gram extremal (N=3): |ω|² = 3 (minimum, orthogonal modes),
S²ê = 27/16 (from the analytical calculation). Ratio = 27/(16·3) = 9/16.
f(3) = 8 · 9/16 / 9 ... hmm, let me recalculate.

Actually, Q/|ω|² = 9 - 8|S|²/|ω|². At the Gram extremal: Q/|ω|² = 2.25 = 9/4.
So 8|S|²/|ω|² = 9 - 9/4 = 27/4. And |S|²/|ω|² = 27/32.

For the trace-free bound: S²ê ≤ (2/3)|S|² = (2/3)(27/32)|ω|² = (9/16)|ω|².
So S²ê/|ω|² ≤ 9/16 = 0.5625. And (3/4) = 0.75. The ratio is 0.75 of
the threshold. This is the TIGHTEST case (N=3).

For N=7: S²ê/|ω|² ≤ (2/3)(9-8.45)/(8) = ... hmm, this isn't right.

Let me compute properly. f(N) = 9 - Q/|ω|² = 8|S|²/|ω|².
f(7) = 0.55. So |S|²/|ω|² = 0.55/8 = 0.069.
S²ê ≤ (2/3) × 0.069 |ω|² = 0.046 |ω|².

The Key Lemma needs S²ê < 0.75 |ω|². With 0.046 at N=7: massive margin!

## THE OPEN PROBLEM

**Prove**: For N divergence-free Fourier modes on T³ with unit amplitudes,
at the argmax of |ω|², the worst-case ratio |S|²/|ω|² satisfies:

    |S|²/|ω|² ≤ 1/2 - c/N^a  for some c > 0, a > 0.

(Here 1/2 comes from the cross-term identity |S|² = |ω|²/2 - 2C,
so |S|²/|ω|² = 1/2 - 2C/|ω|². Need C/|ω|² ≥ c/N^a.)

Equivalently: the cross-term C at the argmax satisfies C ≥ c|ω|²/N^a.

## WHY C GROWS WITH N

C = Σ_{j<k} c_{jk} where c_{jk} are cross-terms between modes j,k.
At the argmax: the sign pattern maximizes |ω|². The cross-terms
that contribute POSITIVELY to |ω|² also tend to make C more positive
(because the alignment that increases |ω| also increases C through
the Biot-Savart coupling).

With more modes: more cross-terms contribute positively → C grows.
The ratio C/|ω|² approaches 1/4 (so that |S|²/|ω|² → 0).

## 811. f(N) ~ 212/N^{3.12}. Exponent a ≈ 3 ≫ 2/3 (threshold).
## Mechanism: direction spread + |ω|² growth + phase constraints.
## Not from phase suppression (debunked: both ω,S use cos).
## Key open problem: prove |S|²/|ω|² ≤ 1/2 - c/N^a at argmax.
## Equivalently: prove C/|ω|² ≥ c/N^a at argmax.
