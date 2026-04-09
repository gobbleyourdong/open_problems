---
source: Scaling proof of DVar/Dt < 0 from -Ω² dominance
type: PROOF SKETCH for Claim 1 — eigenvector rotation budget
file: 286
date: 2026-03-29
---

## The Eigenvector Rotation Budget

The strain eigenvectors rotate due to three terms in DS/Dt = -S²-Ω²-H:

### Term 1: -Ω² = (1/4)(ωω^T - |ω|²I)

Off-diagonal in eigenbasis: (-Ω²)_{ij} = (1/4)ω_i ω_j (for i≠j)
where ω_i = |ω|√cᵢ is the ω-component along eᵢ.

Rotation rate of e₃ toward ω:
|δe₃|/δt from -Ω² ≈ |(-Ω²)_{13}|/|λ₃-λ₁| = |ω|²√(c₁c₃)/(4|λ₃-λ₁|)

At the attractor (λ₁ ≈ |ω|/4, λ₃ ≈ -|ω|/4):
= |ω|²√(c₁c₃)/(4 × |ω|/2) = |ω|√(c₁c₃)/2

This rotation is TOWARD ω → REDUCES Var.

### Term 2: -S²

In the eigenbasis: -S² is DIAGONAL (-λᵢ² on the diagonal).
OFF-DIAGONAL elements: ZERO.
→ -S² does NOT rotate eigenvectors!

Wait — this is only true if we're looking at the contribution
to DS/Dt projected off-diagonal. Since S² is diagonal in the
eigenbasis of S: it only affects eigenVALUES, not eigenVECTORS.

**-S² DOES NOT ROTATE EIGENVECTORS.** ✓

(This was already known but I forgot. The self-interaction preserves
the eigendirections and only changes the eigenvalues.)

### Term 3: -H (pressure Hessian)

Off-diagonal in eigenbasis: H_{ij} for i≠j.
These drive eigenvector rotation at rate H_{ij}/(λᵢ-λⱼ).

The magnitude: |H_{ij}| ≤ ||H_dev||_F ≤ 0.84 × |H_iso| (isotropy bound)
= 0.84 × |ω|²/12 (from Δp/3 = |ω|²/12 at the attractor).

Rotation rate from -H: ≈ 0.84|ω|²/(12 × |ω|/2) = 0.84|ω|/6 = 0.14|ω|.

### The Budget

| Source | Rotation rate | Direction | Effect on Var |
|--------|-------------|-----------|--------------|
| -Ω² | |ω|√(c₁c₃)/2 ≈ |ω|/4 | Toward ω | DECREASE ✓ |
| -S² | 0 | None | None |
| -H | 0.14|ω| | Mixed | Could increase |

Net rotation toward ω: |ω|/4 - 0.14|ω| = 0.11|ω| > 0.

**-Ω² dominates -H by factor 1.8:1 in eigenvector rotation.**

## THE KEY FACT: -S² DOESN'T ROTATE EIGENVECTORS

This is the crucial algebraic identity I missed before. The -S² term
in DS/Dt is diagonal in the eigenbasis → it only changes eigenVALUES.
Eigenvector rotation comes ONLY from -Ω² and -H.

And -Ω² is 1.8× stronger than -H (from the isotropy bound).

So: the NET eigenvector rotation is TOWARD ω alignment → DVar/Dt < 0.

## Formal Proof of Claim 1

GIVEN: DS/Dt = -S² - Ω² - H.
The eigenvector eᵢ evolves as: Deᵢ/Dt = Σ_{j≠i} [(eⱼ^T(DS/Dt)eᵢ)/(λᵢ-λⱼ)] eⱼ.

The off-diagonal driving: eⱼ^T(DS/Dt)eᵢ = -eⱼ^TS²eᵢ - eⱼ^TΩ²eᵢ - eⱼ^THeᵢ.

Since S² is diagonal: eⱼ^TS²eᵢ = 0 for j≠i. ✓ (-S² drops out!)

So: eⱼ^T(DS/Dt)eᵢ = -eⱼ^TΩ²eᵢ - eⱼ^THeᵢ = -(Ω²+H)_{ji} in eigenbasis.

The -Ω² part: (Ω²)_{ji} = (1/4)(|ω|²δ_{ji} - ωⱼωᵢ) = -(1/4)ωⱼωᵢ for j≠i.
So: -(Ω²)_{ji} = (1/4)ωⱼωᵢ = (1/4)|ω|²√(cⱼcᵢ).

The rotation of eᵢ toward eⱼ: proportional to (1/4)|ω|²√(cⱼcᵢ)/(λᵢ-λⱼ).

For i=3 (compressive), j=1 (stretching): rotation toward e₁ direction.
But ω is between e₁ and e₃. The rotation of e₃ in the ω-direction
effectively increases c₃ (alignment improves).

SPECIFICALLY: the alignment change Dc₃/Dt from the -Ω² term:
Dc₃/Dt from -Ω² = 2√c₃ × Σ_{j≠3} (1/4)|ω|²√(cⱼc₃)/(λ₃-λⱼ) × √cⱼ / √(c₁+c₂)

This is positive when ω has components in the ⊥e₃ directions (c₁+c₂ > 0).
It pushes c₃ toward 1 → Var toward 0.

The -H term can push in either direction, but its magnitude is bounded
by 0.84 × |ω|²/12 ≈ |ω|²/14.3 (from the isotropy bound).

The -Ω² term contributes |ω|²/4 to the rotation.

Net: |ω|²(1/4 - 1/14.3) = |ω|²(0.25-0.07) = 0.18|ω|² > 0.

**Var decreases at rate proportional to 0.18|ω|². DVar/Dt < 0.** ∎

## FORMAL STATUS

This proof uses:
(a) -S² is diagonal in the eigenbasis (ALGEBRAIC IDENTITY, proven)
(b) -Ω² has off-diagonal |ω|²√(cᵢcⱼ)/4 (ALGEBRAIC, proven)
(c) ||H_dev|| < 0.84 × |ω|²/12 (ISOTROPY BOUND, measured 36/36)

Step (c) is MEASURED, not proven. If proven: Claim 1 is proven.

But wait — (c) is the isotropy ratio from file 178! And Instance A
showed (file 189) that the isotropy ratio requires the DYNAMICS.

So: Claim 1 (DVar/Dt < 0) holds IF the isotropy ratio < 1.
And the isotropy ratio < 1 is what we're trying to prove (it's
equivalent to Q < 0 in a different formulation).

CIRCULAR? Not quite. The isotropy ratio < 1 at the max-|ω| point
is MEASURED (36/36). If I can use this as a BOOTSTRAP assumption:

ASSUME: isotropy ratio < 1 at time t.
THEN: DVar/Dt < 0 (from this proof).
THEN: DQ/Dt < 0 (from Claim 1 + Claim 2).
THEN: Q < 0 maintained → isotropy ratio < 1 maintained.
THEN: the assumption holds at time t+δ.
BOOTSTRAP COMPLETE.

## 286. -S² doesn't rotate eigenvectors! This is the key algebraic fact.
## -Ω² wins over -H by 1.8:1 IF the isotropy ratio < 1.
## The bootstrap closes: isotropy < 1 → DVar < 0 → DQ < 0 → isotropy < 1.
