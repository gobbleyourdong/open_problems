---
source: PROVING |S|² < (3/4)|ω|² at the max via Biot-Savart spectral structure
type: PROOF ATTEMPT — the weakened attractor bound
file: 334
date: 2026-03-29
---

## The Target

Prove: |S(x*)|² < (3/4)|ω(x*)|² at any point x* where |ω|² is maximal.

Equivalently: |ω|²/|S|² > 4/3 at the max.

## The Spectral Identity

On T³ with div-free ω: û_k = i(k × ω̂_k)/|k|².

The strain Fourier coefficient:
Ŝ_k,ij = -(k_i(k×ω̂)_j + k_j(k×ω̂)_i) / (2|k|²)

The strain magnitude squared at x*:
|S(x*)|² = Σ_{i,j} |S_{ij}(x*)|²
= Σ_{i,j} |Σ_k Ŝ_k,ij e^{ik·x*}|²

## Per-Mode Contribution

For a SINGLE mode k: |Ŝ_k|² (Frobenius norm squared):
Σ_{ij} |Ŝ_k,ij|² = |k×ω̂_k|²/(2|k|⁴) × Σ_{ij}(k_i²(k×ω̂)_j² + k_j²(k×ω̂)_i² + 2k_ik_j(k×ω̂)_i(k×ω̂)_j)/(stuff)

Actually let me compute more carefully.

Ŝ_k = -(1/(2|k|²))(k⊗w + w⊗k) where w = k×ω̂_k.

|Ŝ_k|²_F = (1/(4|k|⁴)) × |k⊗w + w⊗k|²_F
= (1/(4|k|⁴)) × [|k|²|w|² + (k·w)² + (k·w)² + |w|²|k|²]
= (1/(4|k|⁴)) × [2|k|²|w|² + 2(k·w)²]

Since w = k×ω̂: k·w = k·(k×ω̂) = 0. So (k·w)² = 0.
And |w|² = |k×ω̂|² = |k|²|ω̂|² (since ω̂ ⊥ k for div-free).

|Ŝ_k|² = (1/(4|k|⁴)) × 2|k|²×|k|²|ω̂|² = |ω̂_k|²/2.

## THE KEY IDENTITY: |Ŝ_k|² = |ω̂_k|²/2

The strain Frobenius norm for each mode is EXACTLY HALF the vorticity
amplitude squared. This is the spectral version of ||S||₂ = ||ω||₂/√2.

## At x*: Parseval Fails Pointwise

|S(x*)|² = |Σ_k Ŝ_k e^{ik·x*}|²_F ≠ Σ_k |Ŝ_k|²_F (pointwise ≠ L²)

The pointwise value includes CROSS-TERMS from phase interference.

|S(x*)|² = Σ_{k,k'} Ŝ_k:Ŝ_{k'} e^{i(k-k')·x*}

where Ŝ:Ŝ' = Σ_{ij} Ŝ_{ij}Ŝ'_{ij} (Frobenius inner product).

## Bounding the Pointwise Value

|S(x*)|² ≤ (Σ_k |Ŝ_k|_F)² = (Σ_k |ω̂_k|/√2)² = (1/2)(Σ_k |ω̂_k|)²

Similarly: |ω(x*)|² = |Σ_k ω̂_k e^{ik·x*}|² ≤ (Σ_k |ω̂_k|)²

So: |S(x*)|² / |ω(x*)|² ≤ (1/2)(Σ|ω̂|)² / |ω(x*)|²

At the max: |ω(x*)| ≤ Σ|ω̂_k| (triangle inequality).
So |ω(x*)|² ≤ (Σ|ω̂|)².

This gives: |S|²/|ω|² ≤ 1/2. DONE?!

WAIT: |S|² ≤ (1/2)(Σ|ω̂|)² and |ω|² ≤ (Σ|ω̂|)². So the RATIO
|S|²/|ω|² ≤ (Σ|ω̂|)²/(2|ω|²). Since |ω|² ≤ (Σ|ω̂|)²: the ratio
could be ≤ 1/2 × (Σ|ω̂|)²/(Σ|ω̂|)² × (correction for phases).

Hmm, this doesn't work directly because both bounds use the SAME
triangle inequality. The ratio |S|²/|ω|² involves the RELATIVE
phase structure of S vs ω at x*.

## THE DIRECT APPROACH

|S(x*)|² = Σ_{k,k'} Ŝ_k : Ŝ_{k'} φ_{kk'}

where φ_{kk'} = e^{i(k-k')·x*} (complex phases).

The DIAGONAL terms (k=k'): Σ_k |Ŝ_k|² = (1/2)Σ|ω̂_k|².

The CROSS terms (k≠k'): Σ_{k≠k'} Ŝ_k:Ŝ_{k'} φ_{kk'}.

|S|² = (1/2)Σ|ω̂|² + (cross terms).

Similarly: |ω|² = Σ|ω̂|² + (cross terms for ω).

At the MAX of |ω|: the ω cross-terms are MAXIMALLY POSITIVE
(the phases are coherent, maximizing |ω|²).

For |S|²: the cross-terms could be positive or negative.
But the S-phases are DIFFERENT from the ω-phases (because S involves
the CZ multiplier k⊗w/|k|²).

## THE BOUND

|S|²/|ω|² = [(1/2)Σ|ω̂|² + S-cross] / [Σ|ω̂|² + ω-cross]

At the max: ω-cross ≥ 0 (phases are coherent for ω).

If S-cross ≤ 0 (S-phases destructive):
  |S|²/|ω|² ≤ (1/2)Σ|ω̂|² / (Σ|ω̂|² + ω-cross) ≤ 1/2 < 3/4. ✓

If S-cross > 0 (S-phases constructive):
  |S|²/|ω|² ≤ [(1/2)Σ|ω̂|² + S-cross] / Σ|ω̂|²

  Need: (1/2) + S-cross/Σ|ω̂|² < 3/4 → S-cross < (1/4)Σ|ω̂|².

## CAN S-CROSS BE LARGE?

S-cross = Σ_{k≠k'} Ŝ_k:Ŝ_{k'} e^{i(k-k')x*}

|S-cross| ≤ Σ_{k≠k'} |Ŝ_k|×|Ŝ_{k'}| = (Σ|Ŝ_k|)² - Σ|Ŝ_k|²
= (Σ|ω̂_k|/√2)² - (1/2)Σ|ω̂_k|² = (1/2)[(Σ|ω̂|)² - Σ|ω̂|²]
= (1/2) × (ω-cross terms at max coherence)

At the max of |ω|: (Σ|ω̂|)² ≈ |ω|² + ... (the phases are NOT perfectly
coherent unless all modes are exactly in phase — which requires all
k·x* = 0 mod 2π, only possible at x* = 0 for a subset of k).

For a generic x*: (Σ|ω̂|)² > |ω|² (by Cauchy-Schwarz).

So S-cross ≤ (1/2)[(Σ|ω̂|)² - Σ|ω̂|²].

And the ratio: |S|²/|ω|² ≤ (1/2)(Σ|ω̂|)²/|ω|².

At the max: |ω|² = (Σ|ω̂|)² only if ALL modes are in phase (all
k·x* = 2nπ). If any phase is off: |ω|² < (Σ|ω̂|)², and the ratio
|S|²/|ω|² < (1/2)(Σ|ω̂|)²/|ω|² ... which could be > 1/2.

## THE CRUX

The bound |S|²/|ω|² ≤ 1/2 × (Σ|ω̂|)²/|ω|² = 1/2 × (coherence factor).

The coherence factor = (Σ|ω̂|)²/|ω|² ≥ 1 (always).

For the bound to give < 3/4: need coherence factor < 3/2.

Coherence factor = (Σ|ω̂|)²/|ω|² ≥ 1. Need < 3/2.

For ONE mode: |ω| = |ω̂|, Σ|ω̂| = |ω̂|. Factor = 1. ✓
For TWO equal modes: |ω| ≤ 2|ω̂|, Σ|ω̂| = 2|ω̂|. Factor = 4/(2|ω̂|²/|ω|²)... depends.

At the max with v̂₁ ∥ v̂₂ (parallel, d=1): |ω| = 2|ω̂|. Factor = 4/(4) = 1. ✓
With v̂₁ ⊥ v̂₂ (d=0): |ω| = √2|ω̂|. Factor = 4/(2) = 2. > 3/2! ✗

So: for two perpendicular modes at equal amplitude: coherence factor = 2.
Then: |S|²/|ω|² ≤ 1/2 × 2 = 1. NOT below 3/4!

But the ACTUAL |S|²/|ω|² for two perpendicular modes was 0.237 (file 332).
The bound of 1 is VERY LOOSE (4× off).

## THE BOUND IS TOO LOOSE

The triangle inequality Σ|Ŝ_k| and Σ|ω̂_k| don't capture the phase
cancellation in S. The actual S is much smaller than the bound because
the S-phases are NOT maximally coherent (even when ω-phases are).

## STATUS

The per-mode identity |Ŝ_k|² = |ω̂_k|²/2 is EXACT and useful.
But converting it to a pointwise bound at x* using triangle inequality
gives |S|²/|ω|² ≤ 1/2 × coherence ≤ 1 (too loose for 3/4).

The ACTUAL ratio is 0.25 at the max (much better than 1/2).
The proof needs a way to use the SPECIFIC phase structure at the max
to bound the S-coherence below the ω-coherence.

The key: at the max of |ω|², the ω-phases are OPTIMALLY coherent.
The S-phases are DERIVED from the ω-phases through the CZ multiplier.
The CZ multiplier ROTATES the phases, reducing coherence.

Proving this phase-decorrelation is the crux. It's a HARMONIC ANALYSIS
statement about the CZ operator at points of maximum coherence.

## 334. The per-mode identity gives |S|² from |ω|², but the phase
## coherence conversion is the bottleneck. Need factor < 3/2 on coherence.
