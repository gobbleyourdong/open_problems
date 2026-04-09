---
source: MAX CONDITION IS ESSENTIAL — Q < 0 without it, Q > 0 with it
type: KEY STRUCTURAL INSIGHT — the proof MUST use the max condition
file: 516
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE FINDING

Q = 4C + |ω|² (equivalent to |S|²_F < |ω|²) is:
- **MASSIVELY NEGATIVE** at generic points (C/|ω|² as low as -2500)
- **ALWAYS POSITIVE** at x* = argmax|ω| (C/|ω|² ≥ -0.124 in 10K trials)

The bound |S|²_F < |ω|² is NOT a universal inequality for div-free fields.
It holds ONLY at the maximum of |ω|.

## WHY THE MAX CONDITION MAKES IT WORK

**The mechanism** (understood for N=2, conjectured for all N):

At a generic point x₀: perpendicular components can cancel, giving
|ω(x₀)| small while |S(x₀)| stays large → ratio |S|²/|ω|² → ∞.

At x* = argmax|ω|: the phases cos(k·x*) are chosen to make ALL large
components REINFORCE. This means:
1. The dominant perpendicular components ADD (not cancel)
2. The vorticity is large: |ω| ≈ Σ|ω̂_k|
3. The SAME phase arrangement makes C ≥ 0 (or mildly negative)

**Example**: v₁ = εê + An̂, v₂ = εê - An̂ (A >> ε).

At x₀ = 0: ω = 2εê (perpendicular cancels). |ω|² = 4ε².
  C = -A² sin²θ. Q = -4A² + 4ε² << 0. |S|²/|ω|² >> 1.

At x* (actual max): cos factors flip one mode.
  ω = 2An̂ (perpendicular REINFORCES). |ω|² = 4A².
  C = A² sin²θ. Q = 4A² + 4A² >> 0. |S|²/|ω|² << 1.

The max ALWAYS picks up the large components, which simultaneously
makes C positive (or bounded below).

## IMPLICATION FOR THE PROOF

Any proof of |S|²_F < |ω|² MUST use the maximality of |ω| at x*.
The bound is FALSE at generic points.

This rules out:
- Pure Fourier analysis (doesn't use the max condition)
- Triangle inequality + Cauchy-Schwarz (doesn't use the max condition)
- Operator norm bounds on the BS multiplier (doesn't use the max condition)

This REQUIRES:
- Sign-flip constraint (w_k·ê ≥ 0 at the max)
- Perpendicular cancellation (Σ b_k = 0 at the max)
- The GLOBAL maximality (|ω(x*)| ≥ |ω(x)| for all x)

## THE DECOHERENCE ARGUMENT (informal)

At x*: |ω| is near its maximum → modes are approximately aligned
→ |ω| ≈ Σ|ω̂_k| (constructive interference for ω)

Meanwhile: |S| is the sum of BS-rotated modes. The rotation is
k-dependent, so even when ω modes are aligned, S modes are NOT
perfectly aligned.

|S|²_F = |Σ Ŝ_k cos(k·x*)|²_F ≤ (Σ|Ŝ_k|_F)² = (Σ|ω̂_k|/√2)²

|ω|² = |Σ ω̂_k cos(k·x*)|² ≈ (Σ|ω̂_k|)² at the max.

Ratio: |S|²_F/|ω|² ≤ (Σ|ω̂_k|)²/(2|ω|²) ≈ 1/2 at the max.

When modes are NOT perfectly aligned: |ω| < Σ|ω̂_k|. But the same
misalignment also reduces |S| (from decoherence). The net effect:
the ratio stays bounded.

**The gap**: make "decoherence" rigorous. Show that the BS rotation
ensures |S|²/|ω|² < 1 at the max for all configurations.

## 516. Q < 0 at generic points but > 0 at the max. The proof
## MUST use the max condition. The decoherence argument needs
## formalization: BS rotation prevents |S| from growing as fast as |ω|.
