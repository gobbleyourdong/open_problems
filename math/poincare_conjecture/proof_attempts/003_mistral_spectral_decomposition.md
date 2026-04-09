---
source: Mistral
approach: Fourier spectral decomposition + concentration inequalities
status: SOLID FRAMEWORK — complements Grok's approach
---

## Summary
Mistral provides a systematic framework. Less sharp than Grok but identifies the same key structure.

## Core Insight
Rewrite Q in Fourier space:
```
Q(ω) = Σ_k ω̂_k* (Ŝ_k - ν|k|²) ω̂_k
```
The term (Ŝ_k - ν|k|²) is the KEY OBJECT. For large |k|, the -ν|k|² dominates Ŝ_k, making Q negative for high-frequency modes. For low |k|, Ŝ_k may dominate — but there are only finitely many such modes.

## The Argument (Mistral's version)
1. **High-k modes**: Ŝ_k decays as 1/|k|² (from kernel), so (Ŝ_k - ν|k|²) < 0 for |k| > k_c where k_c = (Ŝ_max/ν)^{1/4} or similar
2. **Low-k modes**: finite number, bounded contribution
3. **The fraction** of points where Q > 0 is controlled by the low-k mode count vs total points → decays as the ratio of low modes to total modes

## Key Technical Point
"The number of low-frequency modes grows POLYNOMIALLY with grid size, while the number of high-frequency modes grows EXPONENTIALLY."

**Wait — this isn't right for uniform grids.** On an N³ grid, modes up to k_c are O(k_c³) and total modes are O(N³). The ratio is (k_c/N)³ which decays as N^{-3}, not exponentially. For exponential decay, we need something stronger.

## What Mistral Adds Beyond Grok
1. **Rayleigh quotient interpretation** — Q as a generalized eigenvalue problem. The sign of Q depends on whether the "generalized eigenvalue" exceeds the dissipation threshold.
2. **Compact operator** — S is compact (spectrum decays), which limits how many modes can contribute positive Q.
3. **Explicit tool list** — Chernoff bounds, Gaussian concentration, Fourier localization, Parseval.

## What Mistral Gets Wrong
1. The mode counting argument gives polynomial decay, not exponential. For exponential, need the spectral convergence argument (Grok's Step 3) or the MGF bound (Gemini's approach).
2. Says Ŝ_k ~ 1/|k|² but Gemini correctly notes the full Biot-Savart symbol is degree-0, not degree-2. The 1/|k|² is cancelled by the gradient in the numerator.

## Assessment
- Good framework but less precise than Grok
- The Fourier-space Q formula is useful and matches our computational setup
- The Rayleigh quotient idea could lead to an eigenvalue bound
- The polynomial vs exponential decay issue needs resolution
- Best used as supporting framework, not lead proof

## Action Items
1. Compute Ŝ_k explicitly for divergence-free fields — what IS the symbol?
2. Find k_c where (Ŝ_k - ν|k|²) changes sign — this is the dissipation cutoff
3. Count modes below k_c and compare to our N_d ≈ 8
4. The Rayleigh quotient approach might give the tightest bound on Q_max
