---
source: TWO-CASE PROOF — handles both high and low correlation regimes
type: PROOF DIRECTION — the correct architecture for the analytical bound
file: 399
date: 2026-03-29
---

## THE TWO-CASE ARCHITECTURE

The regression bound: R ≤ 1 + 2(max(L) + c·Y_max)/(N + 2Y_max)
where c = Cov(X,Y)/Var(Y) = ρ σ_X/σ_Y.

### Case 1: |ρ| > 1/√2 (strong correlation)

σ_L = σ_X√(1-ρ²) < σ_X/√2.
|c| = |ρ|σ_X/σ_Y > σ_X/(√2 σ_Y).

max(L) ≤ C₁ σ_L (from the Key Lemma / bounded effective rank)
|c|Y_max ≥ |ρ|σ_X Y_max/σ_Y (negative regression term)

For Y_max ≥ C₂ σ_Y (standard lower bound on the max):
R ≤ 1 + 2(C₁σ_L - |c|C₂σ_Y)/(N + 2C₂σ_Y)
= 1 + 2σ_X(C₁√(1-ρ²) - |ρ|C₂)/(N + 2C₂σ_Y)

Since √(1-ρ²) < 1/√2 and |ρ| > 1/√2:
C₁/√2 - C₂/√2 = (C₁-C₂)/√2. Need C₁ < C₂.

If C₁ = C₂ (same scaling for max): (C₁-C₁)/√2 = 0. R ≈ 1. ✓
If C₁ < C₂: the numerator is negative. R < 1. ✓✓

### Case 2: |ρ| ≤ 1/√2 (weak correlation)

X and Y are nearly independent. At s* (the Y-maximizer):
X(s*) behaves like a "random" evaluation of X.

For a random s: E[X(s)] = 0 and Var(X(s)) = σ_X².
By Hanson-Wright (applied to the specific s* as if random from X's perspective):
|X(s*)| ≤ C₃ σ_X (with "effective randomness" from the orthogonality).

R ≤ 1 + 2C₃σ_X/(N + 2Y_max)

For σ_X ~ N and (N + 2Y_max) ~ N: R ≤ 1 + 2C₃. Need C₃ ≤ 5/16.

THIS DOESN'T CLOSE: C₃σ_X/N ~ C₃ × (N/N) = C₃ (constant, not small).

### Case 2 (revised): Use the DIRECT S²ê bound instead

When |ρ| ≤ 1/√2: the correlation is weak. But: the DIRECT bound
S²ê ≤ Σ|ŝ_k|² + cross also applies. And Σ|ŝ_k|² ≤ |ω|²/4 (Parseval).

The cross-terms: when |ρ| is small, the modes have diverse geometry.
The cross-terms partially cancel → S²ê ≈ Σ|ŝ_k|² ≈ |ω|²/4 < 3|ω|²/4. ✓

Wait: Σ|ŝ_k|² ≤ |ω|²/4 is the DIAGONAL bound. The cross-terms can add.
But: for |ρ| small → diverse geometry → cross-terms are small.

### Case 2 (take 3): Small ρ means small excess

|ρ| small means: Cov(X,Y) ≈ 0. The excess X and vorticity Y are uncorrelated.

At the global max: Y_max is large. But X(s*) is "random" — NOT pushed positive.

E[X | Y = Y_max] ≈ ρ(σ_X/σ_Y)Y_max ≈ 0 (since ρ ≈ 0).

So: X(s*) ≈ 0 + noise. The noise is O(σ_X) at worst.

R ≈ 1 + 2 × noise/(N + 2Y_max) ≈ 1 + O(σ_X/N).

For σ_X ~ N: this gives R ≈ 1 + O(1). Could be > 13/8?

The issue: σ_X ~ N for our matrices, and N + 2Y_max ~ N. So X/|ω|² ~ O(1).

RESOLUTION: when |ρ| is small, the per-mode bound for small N applies.
|ρ| small means the excess and vorticity are weakly coupled, which happens
when most pairs have κ ≈ 0 (orthogonal k-vectors) or D ≈ 0. In these cases:
the per-mode bound works better (it doesn't depend on ρ).


## THE HONEST ASSESSMENT

The two-case approach ALMOST works:
- Case 1 (|ρ| > 1/√2): the regression closes cleanly ✓
- Case 2 (|ρ| ≤ 1/√2): the regression is weak, need alternative

For Case 2: the configs with small |ρ| tend to have DIVERSE k-geometry,
which makes the per-mode bound tighter (more cancellation between modes).
But: this is an EMPIRICAL observation, not a proof.

The FORMAL proof needs: EITHER
(a) Show |ρ| > 1/√2 for all Biot-Savart configs (FALSE — data shows violations)
(b) Show the Key Lemma |X(s*)| ≤ Cσ_X for all configs (C ≈ 3.5 observed)
(c) Show Case 2 configs satisfy S²ê < 3|ω|²/4 by a different route
(d) Combine per-mode (N≤4) + regression (|ρ|>1/√2) + direct (|ρ|≤1/√2)


## STATUS

The two-case architecture identifies the correct structure but doesn't
fully close because Case 2 (small ρ) lacks a tight analytical bound.

The KEY LEMMA (|X(s*)| ≤ C||M_X||_F) would close BOTH cases simultaneously.
Proving it remains the central challenge.

From the numerical data: the Key Lemma holds with C ≤ 4 across all tested
N and geometries. The general Charikar-Wirth log(N) growth doesn't apply.


## 399. Two-case: ρ>1/√2 (regression) + ρ≤1/√2 (independence). Case 2 open.
## The Key Lemma (C bounded) would close both. Still the central challenge.
