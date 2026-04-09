# Attempt 846 — Anatomy of the Worst Configuration

**Date**: 2026-04-08
**Instance**: Both

## Finding

The worst configurations (maximizing S²ê/|ω|²) have:
- INCOHERENT vorticity: |ω|²/N² ≈ 0.35-0.48 (well below 1)
- k-vectors from perpendicular directions (K²=1 shell: ±eᵢ)
- Polarizations spread across ~80°-100° angles

## Why This Gives 1/N Decay

1. Vorticity at the max: |ω|² ~ αN² where α ≈ 0.4 (partial coherence)
2. Each mode contributes O(1) to the strain (k × v structure)
3. The stretching ê·S·ê is a sum of N terms with RANDOM SIGNS
   (because ê ⊥ to most k×v contributions for perpendicular k-vectors)
4. By concentration: |ê·S·ê|² ~ N (variance of N random-sign terms)
5. Ratio: S²ê/|ω|² ~ N/(αN²)² ... no, S²ê = |Sê|² not (ê·S·ê)²

Corrected:
- S²ê = |Sê|² = Σᵢ (Sê)ᵢ² (vector norm squared)
- (Sê)ᵢ = Σₙ contribution from mode n to the i-th component
- For N modes with random-ish contributions: |Sê|² ~ N
- |ω|² ~ 0.4 N²
- Ratio: N / (0.4N²) = 2.5/N

This gives c(N) ~ 2.5/N. The data gives c(N) ~ 1.2/N. Same order!

## The Proof Ingredient

To prove c(N) ~ C/N analytically:
1. Show that at the vorticity argmax, |ω|² ≥ αN² for some α > 0
   (partial coherence — the max over sign patterns gives ≥ αN²)
2. Show that |Sê|² ≤ βN for some β (strain incoherence from Biot-Savart)
3. Then: c(N) ≤ β/(αN) → 0 as N → ∞

Step 1: The max of |Σ sₙ vₙ|² over ±1 signs is ≥ N (pigeonhole:
at least one sign pattern gives |ω|² ≥ Σ|vₙ|² = N).
Actually: E[|ω|²] = Σ|vₙ|² = N (by independence of sign choices).
The MAX over signs is ≥ the AVERAGE = N. So |ω|²_max ≥ N.

Step 2: The strain S is a sum of N rank-2 matrices.
|Sê|² ≤ ||S||²_F × |ê|² = ||S||²_F.
||S||²_F = Σₙ ||Sₙ||²_F = Σₙ |kₙ|²|wₙ|²/(2|kₙ|⁴) ≤ Σ 1/(2|kₙ|²)
For |kₙ|² = 1 (K²=1 shell): ||S||²_F ≤ N/2.

So: S²ê/|ω|² ≤ ||S||²_F / |ω|²_max ≤ (N/2) / N = 1/2.

WAIT — that gives c(N) ≤ 1/2 for ALL N. Not 1/N, but a CONSTANT bound!
And 1/2 < 3/4 (the threshold). THIS IS THE KEY LEMMA!

## POSSIBLE PROOF

**Claim**: S²ê/|ω|² ≤ 1/2 for all N-mode configurations at the vorticity max.

**Proof**:
1. |ω|²_max ≥ N (by averaging: E[|ω|²] = N, max ≥ average)
2. ||S||²_F ≤ N/2 (from Biot-Savart: each mode contributes ≤ 1/(2|k|²))
3. S²ê ≤ ||S||²_F ≤ N/2
4. S²ê/|ω|² ≤ (N/2)/N = 1/2 < 3/4 ✓

**CAVEAT**: Step 3 uses S²ê ≤ ||S||²_F which is TIGHT only if Sê is
along the largest singular vector of S. The actual S²ê could be much smaller.
Step 1 uses max ≥ average which is TIGHT only if there's no variance.
The data shows c(N) ~ 1/N << 1/2, so the bound 1/2 is VERY LOOSE.

But 1/2 < 3/4 SUFFICES. We don't need the tight 1/N bound for the proof.
We need c(N) < 3/4. The bound c(N) ≤ 1/2 would do.

## 846. The 1/2 bound: ||S||²_F ≤ N/2 and |ω|²_max ≥ N → ratio ≤ 1/2.
## THIS MIGHT BE THE KEY LEMMA PROOF.
## Need to verify: is Step 1 (|ω|²_max ≥ N) rigorous?
## And: is Step 2 (||S||²_F ≤ N/2) correct for all k-configs?
