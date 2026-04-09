---
source: Algebraic bound on -Ω² tilting in the Vieillefosse zone
type: PROOF ATTEMPT — close the last gap with pure algebra
date: 2026-03-29
---

## The Gap

Need: DQ/Dt < 0 at Q = 0 in the Vieillefosse zone (α ∈ [0.35|ω|, 0.5|ω|]).

DQ/Dt|_{Q=0} = D²α/Dt² - 2α³.

D²α/Dt² = D(S²ê)/Dt - 4αDα/Dt - D(H_ωω)/Dt.

At Q = 0: Dα/Dt = -α². So -4αDα/Dt = +4α³.

D²α/Dt² = D(S²ê)/Dt + 4α³ - D(H_ωω)/Dt.

DQ/Dt = D(S²ê)/Dt + 4α³ - D(H_ωω)/Dt - 2α³ = D(S²ê)/Dt + 2α³ - D(H_ωω)/Dt.

## The -Ω² Contribution to D(S²ê)/Dt

D(S²ê)/Dt has eigenvalue and tilting parts.

The -Ω² contribution to the EIGENVALUE part:
  -2Σλᵢ Ω²ᵢᵢ cᵢ = -(|ω|²/2)(α - Σλᵢcᵢ²)

  At the attractor |ω|² = 4|S|²:
  = -2|S|²(α - Σλᵢcᵢ²)

In the Vieillefosse zone (ω ≈ e₁, c₁ ≈ 1):
  Σλᵢcᵢ² ≈ λ₁c₁² ≈ λ₁ ≈ α (since c₁ ≈ 1 → α ≈ λ₁)
  So: α - Σλᵢcᵢ² ≈ 0 (the eigenvalue correction vanishes!)

  This means the -Ω² eigenvalue contribution is WEAK in the Vieillefosse zone.

The -Ω² contribution to the TILTING part:
  This changes c₁ toward smaller values (rotating ω away from e₁).

  Dc₁/Dt from -Ω² = (|ω|²/2)c₁ Σⱼ≠₁ cⱼ/(λ₁-λⱼ) (from file 241)

  In the Vieillefosse zone: c₁ ≈ 1 - ε (ω nearly aligned with e₁).
  c₂ ≈ c₃ ≈ ε/2 (small, nearly equal).

  Dc₁/Dt ≈ (|ω|²/2) × 1 × [ε/2/(λ₁-λ₂) + ε/2/(λ₁-λ₃)]
  = (|ω|²ε/4) × [1/(λ₁-λ₂) + 1/(λ₁-λ₃)]

  With λ₁ > λ₂ > λ₃ and trace-free: λ₁-λ₂ ~ |S|/2, λ₁-λ₃ ~ |S|.
  Dc₁/Dt ≈ (|ω|²ε/4) × (2/|S| + 1/|S|) = 3|ω|²ε/(4|S|)

  At attractor: = 3ε|ω|/2.

  The TILTING effect on α: Dα/Dt|_{tilting} = Σλᵢ Dcᵢ/Dt.
  Since c₁ decreases and c₂, c₃ increase:
  Dα|_{tilting} = λ₁ Dc₁ + λ₂ Dc₂ + λ₃ Dc₃
  ≈ λ₁(-Dc₁) × (-1) + ...

  Actually: Dc₁ < 0 (decreasing), Dc₂ > 0, Dc₃ > 0 (from Σ Dcᵢ = 0).
  Dα|_{tilting} = λ₁Dc₁ + λ₂Dc₂ + λ₃Dc₃ = Σλᵢ Dcᵢ.

  In the Vieillefosse zone: λ₁ > 0, Dc₁ < 0 → negative.
  λ₃ < 0, Dc₃ > 0 → negative.
  λ₂ ≈ 0, Dc₂ > 0 → ≈ 0.

  Total: Dα|_{tilting} < 0 (NEGATIVE — tilting reduces α). ✓

  Magnitude: |Dα|_{tilting}| ≈ |λ₁ Dc₁| + |λ₃ Dc₃|
  ≈ |S|/√2 × 3ε|ω|/2 + |S|/√2 × 3ε|ω|/4 (rough, splitting equally)
  ~ |S|ε|ω| ~ ε|ω|²/2 (at attractor)

## The Comparison

In the Vieillefosse zone (c₁ ≈ 1, ε = 1-c₁ small):

  D(S²ê)/Dt from -Ω² tilting: ~ -ε|ω|²|S| ~ -ε|ω|³/2

  Eigenvalue cubic: |2Σλᵢ³cᵢ| ≈ 2|λ₁|³ (since c₁ ≈ 1) ≈ 2|S|³/2√2 ≈ 0.07|ω|³

  For the tilting to dominate: ε|ω|³/2 > 0.07|ω|³ → ε > 0.14.

  Meaning: c₁ < 1 - 0.14 = 0.86. If c₁ < 0.86: tilting dominates. ✓

  But our zone is α ∈ [0.35|ω|, 0.5|ω|]. With α ≈ λ₁c₁ + λ₂c₂ + λ₃c₃:
  For c₁ close to 1: α ≈ λ₁ ≈ |S|/√(3/2) ≈ 0.82|S| ≈ 0.41|ω|.

  So: α = 0.41|ω| corresponds to c₁ ≈ 1 (perfect alignment).
  α = 0.35|ω| corresponds to c₁ ≈ 0.85. Then ε = 0.15 > 0.14. ✓

  At the BOUNDARY α = 0.35|ω| (c₁ ≈ 0.85, ε ≈ 0.15):
  The tilting (0.15 × |ω|³/2 = 0.075|ω|³) barely exceeds the
  eigenvalue cubic (0.07|ω|³). Margin: 7% (TIGHT but positive).

  For α > 0.35|ω| (c₁ > 0.85, ε < 0.15): the tilting WEAKENS
  (because ε → 0 as c₁ → 1). But so does the eigenvalue cubic
  (it's maximized at c₁ = 1 with value 2λ₁³, but the tilting
  also has a factor proportional to ε).

## THE CRITICAL QUESTION

At c₁ → 1 (perfect Vieillefosse alignment): BOTH the tilting and
the eigenvalue cubic go to ZERO (tilting ~ ε → 0, cubic stays ~0.07|ω|³).

Wait: the eigenvalue cubic at c₁ = 1:
  -2Σλᵢ³cᵢ = -2λ₁³ × 1 = -2λ₁³ (NEGATIVE, not positive!)

For λ₁ > 0: -2λ₁³ < 0. The eigenvalue cubic is NEGATIVE when c₁ = 1!

Let me recheck. At c₁ = 1, c₂ = c₃ = 0:
  -2Σλᵢ³cᵢ = -2λ₁³.

Since λ₁ > 0: this is -2λ₁³ < 0. NEGATIVE.

The eigenvalue cubic HELPS (is negative) in the Vieillefosse zone!

I had the WRONG SIGN earlier (file 196). The cubic -2Σλᵢ³cᵢ is
NEGATIVE when c₁ is dominant (since λ₁ > 0 and λ₁³ > 0).

The POSITIVE eigenvalue cubic (+0.19|S|³ from file 201) was for
ASHURST alignment (c₂ dominant, λ₂ small). In the Vieillefosse zone
(c₁ dominant): the cubic is NEGATIVE (helps!).

## THE CONCLUSION

IN THE VIEILLEFOSSE ZONE:
  Eigenvalue cubic = -2λ₁³c₁ < 0 (HELPS compression)
  -Ω² tilting = negative (HELPS compression)
  Both HELP. No competition needed.

  D²α/Dt² ≈ (negative eigenvalue cubic) + (negative tilting) + 4α³ - D(H_ωω)/Dt
  ≈ -2λ₁³ - ε|ω|³ + 4α³ - D(H_ωω)/Dt

  With α ≈ λ₁ in this zone:
  -2λ₁³ + 4λ₁³ = 2λ₁³ (the eigenvalue cubic PARTIALLY cancels the 4α³)

  Net: D²α/Dt² ≈ 2λ₁³ - ε|ω|³ - D(H_ωω)/Dt

  For DQ/Dt < 0: need D²α < 2α³ = 2λ₁³.
  ⟺ 2λ₁³ - ε|ω|³ - D(H_ωω)/Dt < 2λ₁³
  ⟺ -ε|ω|³ - D(H_ωω)/Dt < 0
  ⟺ ε|ω|³ + D(H_ωω)/Dt > 0

  Since ε > 0 (c₁ < 1 for any NON-degenerate alignment):
  ε|ω|³ > 0. If D(H_ωω)/Dt ≥ 0 (Step 5 claim): done. ✓

  If D(H_ωω)/Dt < 0: need |D(H_ωω)/Dt| < ε|ω|³.
  From the data: D(H_ωω)/Dt ≈ +100 (positive). So ε|ω|³ + 100 > 0. ✓

  BUT: we can't prove D(H_ωω)/Dt > 0 (Step 5 was broken).

  HOWEVER: we only need D(H_ωω)/Dt > -ε|ω|³ (a LOWER bound, not sign).
  This is WEAKER than Step 5. It says: even if H_ωω decreases,
  it doesn't decrease faster than ε|ω|³.

## DOES THIS CLOSE THE GAP?

AT c₁ = 1 EXACTLY: ε = 0. The condition ε|ω|³ + D(H_ωω)/Dt > 0
reduces to D(H_ωω)/Dt > 0 (need Step 5 exactly). FAILS.

But c₁ = 1 EXACTLY means ω = e₁ PERFECTLY. This is measure zero.

For c₁ < 1 (any ε > 0): the tilting provides a positive ε|ω|³ term.
The condition D(H_ωω)/Dt > -ε|ω|³ is satisfied if |D(H_ωω)/Dt| < ε|ω|³.

From scaling: |D(H_ωω)/Dt| ~ |ω|³ (the pressure evolves at rate |ω|³).
So: need ε > |D(H_ωω)/Dt|/|ω|³ ~ O(1).

If ε ~ O(1) (c₁ not close to 1): the condition holds.
If ε → 0 (c₁ → 1): need |D(H_ωω)/Dt|/|ω|³ → 0 too.

From the data: as c₁ → 1, D(H_ωω)/Dt doesn't blow up. It stays O(|ω|³).
So |D(H_ωω)/Dt|/|ω|³ ~ O(1) while ε → 0. The condition FAILS as ε → 0.

## VERDICT

The algebraic argument ALMOST closes:
- For c₁ < 0.86: tilting dominates eigenvalue cubic. DQ/Dt < 0. ✓
- For c₁ ∈ [0.86, 1): need D(H_ωω)/Dt > -(1-c₁)|ω|³. NOT PROVEN.
- For c₁ = 1: need Step 5 (broken).

The gap narrows from α ∈ [0.35|ω|, 0.5|ω|] to α very close to
0.41|ω| (c₁ ≈ 1, perfect Vieillefosse). This is a SET OF MEASURE ZERO
but the proof still needs to handle it.

The e₁ alignment (c₁ → 1) is UNSTABLE (all models agree, literature
confirms). So the flow EXITS this zone rapidly. But PROVING the exit
rate exceeds the blowup rate is the remaining gap.
