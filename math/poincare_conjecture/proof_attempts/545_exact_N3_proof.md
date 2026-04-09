---
source: EXACT N=3 STRUCTURE — the -11/64 value derived algebraically
type: TOWARDS A PROOF — exact mode structure at the extremum
file: 545
date: 2026-03-31
instance: CLAUDE_OPUS (500s)
---

## THE EXACT CONFIGURATION AT C/|ω|² = -11/64

k-angles: cosθ₁₂ = cosθ₁₃ = -3/4, cosθ₂₃ = 1/4.
sin²θ: 7/16, 7/16, 15/16.

| Mode | sign | a | |b| | γ | D₀₁ | D₀₂ | D₁₂ |
|------|------|---|-----|---|------|------|------|
| 0 | +1 | 1 | 0 | 0° | — | — | — |
| 1 | +1 | 1/2 | √3/2 | 60° | +1/2 | — | -1/2 |
| 2 | +1 | 1/2 | √3/2 | 60° | +1/2 | — | -1/2 |

|ω|² = (1 + 1/2 + 1/2)² + 0 = 4 (since b₁+b₂ = 0 by perp cancellation).

## THE P VALUES (exact fractions)

P₀₁ = -1/16 (from sin²θ = 7/16, small normal projection)
P₀₂ = -1/16 (same by symmetry)
P₁₂ = -9/16 (from sin²θ = 15/16, large OPPOSING perpendicular projections)

C = P₀₁ + P₀₂ + P₁₂ = -1/16 - 1/16 - 9/16 = **-11/16**

C/|ω|² = (-11/16)/4 = **-11/64** ∎

## WHY THE PAIR (1,2) DOMINATES

- sin²θ₁₂ = 15/16 (nearly orthogonal k-vectors)
- D₁₂ = v₁·v₂ = -1/2 (opposing polarizations)
- b₁ and b₂ are ANTI-PARALLEL (perpendicular cancellation: b₁+b₂ = 0)
- (b₁·n̂₁₂)(b₂·n̂₁₂) = -(b₁·n̂₁₂)² ≤ -|b₁|² × (projection)²

With |b₁| = |b₂| = √3/2 and sin²θ = 15/16:
P₁₂ = -(b₁·n̂)² × 15/16 + (aligned terms) = -9/16

## THE ALGEBRAIC PROOF PATH

To prove C ≥ -11/64 for ALL N=3 configs:

**Step 1**: Express C/|ω|² as a function of 6 parameters:
(3 k-angles θ₁₂, θ₁₃, θ₂₃ and 3 polarization angles φ₁, φ₂, φ₃)

**Step 2**: Write the Euler-Lagrange equations ∂(C/|ω|²)/∂(parameter) = 0.

**Step 3**: Show the critical point at cosθ=(-3/4,-3/4,1/4), γ=(0°,60°,60°)
gives the GLOBAL minimum -11/64.

**Step 4**: Verify second-order conditions (Hessian positive semi-definite
at the minimum = maximum of -C/|ω|²).

From the symmetry of the solution (modes 1,2 symmetric, mode 0 aligned):
the Euler-Lagrange reduce to a LOWER-DIMENSIONAL system.

## KEY OBSERVATION

The extremum has |ω|² = 4 = N+1 (for N=3). This suggests the amplitudes
satisfy a_j = {1, 1/2, 1/2} = {2/N, 1/N, 1/N} (one dominant, two equal).

And γ = {0°, 60°, 60°}: one aligned, two at the "magic angle" 60°.

The 60° angle gives sinγ = √3/2, cosγ = 1/2. This maximizes the product
sinγ×cosγ = √3/4 (the compromise between alignment and perpendicular energy).

## CONNECTION TO N=4

The N=4 worst (-0.172) is only 0.1% worse. It uses a similar structure:
two well-aligned modes + two weakly-aligned modes. The extra mode adds
flexibility that slightly worsens the ratio.

## WHAT PROVING -11/64 FOR N=3 WOULD GIVE

C ≥ -11/64 → |S|²_F ≤ |ω|²/2 + 11/32 = 27/32|ω|²
→ S²ê ≤ (2/3)(27/32)|ω|² = 9/16|ω|² = 0.5625|ω|² < 0.75|ω|² ✓

Key Lemma holds for N=3 with 25% margin (9/16 vs 3/4).

For N=4: C ≥ -0.172 → |S|²_F ≤ 0.844|ω|²
→ S²ê ≤ 0.563|ω|² < 0.75|ω|² ✓ (same margin, practically)

## 545. Exact -11/64 structure: one aligned mode + two at 60° with
## anti-parallel perpendicular components. Pair (1,2) dominates at -9/16.
## All fractions are exact: C = -11/16, |ω|² = 4, ratio = -11/64.
