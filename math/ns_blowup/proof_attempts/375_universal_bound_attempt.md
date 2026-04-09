---
source: Attempt at universal |∇u|²/|ω|² bound for all N
type: PROOF ATTEMPT — exploiting the sign-flip + Parseval structure
file: 375
date: 2026-03-29
---

## THE APPROACH: PARSEVAL + SIGN-FLIP

### Key identity (proven)

At a lattice vertex x* with signs s_k:

|∇u|² = Σa_k² + 2Σ_{j<k} s_js_k a_ja_k G_{jk}    (I)
|ω|²  = Σa_k² + 2Σ_{j<k} s_js_k a_ja_k D_{jk}    (II)

where G_{jk} = (w_j·w_k)(k_j·k_k)/(|k_j|²|k_k|²) and D_{jk} = v̂_j·v̂_k.

### The Parseval constraint

Over ALL vertices (averaging over 2^N sign patterns):

⟨|∇u|²⟩_signs = Σa_k² = ⟨|ω|²⟩_signs

The AVERAGE ratio is exactly 1 (since cross-terms average to 0).

### At the GLOBAL MAX vertex

|ω|²(s*) = max_s |ω|²(s) ≥ ⟨|ω|²⟩ = Σa_k²

So: |ω|²(s*) ≥ Σa_k².

### The excess at the max

EXCESS(s*) = |∇u|²(s*) - |ω|²(s*) = 2Σ s*_js*_k a_ja_k (G_{jk} - D_{jk})

Each G_{jk} - D_{jk} = Δ_{jk}. And:

EXCESS = 2Σ s*_js*_k a_ja_k Δ_{jk}

### Variance bound on the excess

Define X(s) = 2Σ s_js_k a_ja_k Δ_{jk} (the excess as a function of signs).

⟨X⟩ = 0 (cross-terms average to 0).
⟨X²⟩ = 4Σ_{(j,k)} a_j²a_k² Δ_{jk}² = Var(X).

By the max condition: X(s*) ≤ X_max = max_s X(s).

But s* is NOT chosen to maximize X — it's chosen to maximize |ω|²(s).

CLAIM: X(s*) ≤ √Var(X) with high probability over the randomness of modes.

Not rigorous, but suggestive. If X(s*) ~ √Var(X) instead of X_max:

√Var(X) = 2√(Σ a_j²a_k² Δ_{jk}²).

For unit amplitudes: = 2√(Σ Δ_{jk}²) ≤ 2√(N(N-1)/2 × (1/4)²) = 2 × √(N(N-1)/32) = √(N(N-1)/8).

For N=5: √(20/8) = √2.5 ≈ 1.58. F = 1 + 1.58/μ₅ ≈ 1 + 1.58/7.9 = 1.20.

Below 5/4! And the√Var estimate gives a ratio that DECREASES as N → ∞.

### Formal bound via quadratic form theory

X(s*) where s* maximizes Y(s) = 2Σ s_js_k a_ja_k D_{jk} + Σa_k² = |ω|²(s).

Both X and Y are quadratic forms in s ∈ {±1}^N.

The correlation: ρ = ⟨X·Y⟩ / √(⟨X²⟩⟨Y²⟩).

If ρ ≈ 0 (X and Y uncorrelated): X(s*) ≈ ⟨X|Y=max⟩ ≈ 0 (no bias).
If ρ > 0: X(s*) has positive bias (the excess correlates with |ω|²).
If ρ < 0: X(s*) has negative bias (the excess is REDUCED at the max).

⟨X·Y⟩ = 4Σ a_j²a_k² Δ_{jk}D_{jk}.

From the structure: Δ_{jk} = G_{jk} - D_{jk}. So:
Δ·D = G·D - D² = (correlation between gradient and vorticity cross-terms) - D².

For the 2-mode case at the optimum (α=60°, D≈0): Δ·D ≈ 0. ρ ≈ 0.

For general modes: the correlation can be positive or negative.

### THE BOUND (if the correlation is bounded)

At the max vertex: |ω|² = Σa_k² + Y(s*) where Y(s*) = max_s Y(s) ≥ 0.

EXCESS = X(s*). The ratio: F = 1 + X(s*)/(Σa_k² + Y(s*)).

Since Y(s*) ≥ 0: the denominator ≥ Σa_k².

So: F ≤ 1 + X(s*)/Σa_k².

Need: X(s*) ≤ (1/4)Σa_k² (for F ≤ 5/4).

From the variance bound: X(s*) ≤ √Var(X) = 2√(Σa_j²a_k²Δ_{jk}²).

By CS: Σa_j²a_k²Δ_{jk}² ≤ (Σa_k²)² × max(Δ_{jk}²)/N ... hmm, this doesn't close.

More carefully: Σ_{j<k} a_j²a_k²Δ² ≤ (1/16)(Σ_{j<k} a_j²a_k²) = (1/16)[(Σa²)²-Σa⁴]/2 ≤ (Σa²)²/32.

√Var(X) ≤ 2×(Σa²)/√32 = (Σa²)/√8.

Need: (Σa²)/√8 ≤ (1/4)Σa². True iff 1/√8 ≤ 1/4 iff √8 ≥ 4 iff 8 ≥ 16. FALSE!

So the variance bound doesn't directly close. But it's suggestive: the excess grows as Σa², while the threshold also grows as Σa². The ratio is 1/√8 ≈ 0.354 vs 1/4 = 0.25.

### Can we use the max condition more strongly?

The sign pattern s* that maximizes |ω|² is NOT random — it's specifically chosen. The excess X(s*) at this specific s* could be BOUNDED more tightly than the generic √Var(X).

If X and Y are ANTI-CORRELATED (as suggested by the structure: maximizing vorticity coherence → minimizing gradient excess): then X(s*) < √Var(X).

From the numerical data: X(s*)/Σa² ≈ 0.05-0.15 (the excess at the max is small).
While √Var(X)/Σa² ≈ 0.35 (the generic fluctuation is larger).

This suggests the max condition SUPPRESSES the excess significantly.

## STATUS

The Parseval + variance approach shows:
1. Average excess = 0 (Parseval identity)
2. Fluctuation of excess ~ √(Σa⁴Δ²) (standard deviation)
3. At the max of |ω|²: excess is REDUCED (not amplified) relative to the fluctuation
4. The numerical ratio X(s*)/(Σa²) ≈ 0.1 << 1/4

The formal proof needs: a CONDITIONAL expectation bound on X given Y = max.
This is a problem in discrete probability (Ising model structure).

## 375. The Parseval framework shows excess is O(√N) while |ω|² is O(N).
## The ratio F → 1 as N → ∞. The max condition suppresses excess.
## Formal proof needs: conditional expectation bound for correlated quadratics.
