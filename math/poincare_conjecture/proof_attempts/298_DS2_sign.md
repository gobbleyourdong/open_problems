---
source: Can we prove D|S|²/Dt ≤ 0 at the vorticity maximum?
type: PROOF ATTEMPT — this would close the entire gap
file: 298
date: 2026-03-29
---

## If D|S|²/Dt ≤ 0 at the max: THE PROOF IS COMPLETE

D(Δp)/Dt = |ω|²α - D|S|²/Dt.
If D|S|²/Dt ≤ 0: D(Δp)/Dt ≥ |ω|²α > 0 (when α > 0).
Then: the dynamic Fourier lemma applies → DH_ωω/Dt > 0.
Then: DQ/Dt = DVar/Dt - DH_ωω/Dt < 0 (both help).
Then: Q < 0 maintained → regularity. ∎

## D|S|²/Dt at the max

D|S|²/Dt = 2S:(DS/Dt) = 2S:(-S²-Ω²-H) = -2tr(S³) - 2tr(SΩ²) - 2tr(SH).

### Term 1: -2tr(S³)

tr(S³) = 3λ₁λ₂λ₃ = 3det(S) (for trace-free S).

Sign of det(S): depends on eigenvalue configuration.
- If λ₁ > 0, λ₂ > 0, λ₃ < 0 (two positive): det > 0 → -2tr(S³) < 0. ✓
- If λ₁ > 0, λ₂ < 0, λ₃ < 0 (one positive): det > 0 → -2tr(S³) < 0. ✓
- Actually for trace-free: one of {λ₂ > 0, λ₂ < 0}.
  With λ₁ > 0 > λ₃ and λ₁+λ₂+λ₃ = 0:
  λ₂ = -(λ₁+λ₃). If λ₁ > -λ₃: λ₂ < 0 (one positive eigenvalue).
  det = λ₁λ₂λ₃ = λ₁(-(λ₁+λ₃))λ₃.

In 3D turbulence: det(S) > 0 preferentially (strain production positive).
But it CAN be negative.

For the |ω|²/|S|² = 4 attractor: eigenvalues scale as λ ~ |ω|/2.
tr(S³) ~ |S|³ ~ |ω|³/8. So -2tr(S³) ~ ±|ω|³/4.

### Term 2: -2tr(SΩ²)

tr(SΩ²) = Σᵢ λᵢ(Ω²)ᵢᵢ = Σᵢ λᵢ(|ω|²/4)(1-cᵢ)
= (|ω|²/4)[Σλᵢ - Σλᵢcᵢ] = (|ω|²/4)[0 - α] = -|ω|²α/4.

So: -2tr(SΩ²) = -2(-|ω|²α/4) = +|ω|²α/2. POSITIVE. ✓

This term is always POSITIVE and equals |ω|²α/2.

### Term 3: -2tr(SH)

tr(SH) = Σᵢⱼ SᵢⱼHᵢⱼ. In the eigenbasis: = Σᵢ λᵢHᵢᵢ.
The diagonal of H in the strain eigenbasis: Hᵢᵢ = H_iso + H_dev,ii.
H_iso = Δp/3 = |ω|²/12. So: Σλᵢ H_iso = 0 (trace-free).
Remaining: Σλᵢ H_dev,ii. This depends on the deviatoric pressure.

|tr(SH_dev)| ≤ ||S|| × ||H_dev|| ≤ (|ω|/2)(R × |ω|²/12) = R|ω|³/24.

So: -2tr(SH) = -2tr(SH_dev) with |-2tr(SH_dev)| ≤ R|ω|³/12.

### Total

D|S|²/Dt = -2tr(S³) + |ω|²α/2 - 2tr(SH_dev).

The sign depends on the balance:
  +|ω|²α/2 (positive, from -Ω²)
  -2tr(S³) (either sign, from self-interaction)
  -2tr(SH_dev) (either sign, from pressure)

For D|S|²/Dt ≤ 0: need -2tr(S³) - 2tr(SH_dev) ≤ -|ω|²α/2.

### At the MAX of |ω|: the Ω² term dominates?

|ω|²α/2 = positive, scaling as |ω|³ × (α/|ω|) = c|ω|³.
|-2tr(S³)| ~ |ω|³/4 (from |S|³).
|-2tr(SH_dev)| ~ R|ω|³/12.

The positive term: c|ω|³ where c = α/(2|ω|) ≈ 0.05 (from data α/|ω| ≈ 0.1).
The negative terms: up to (1/4 + R/12)|ω|³ ≈ (0.25 + 0.07)|ω|³ = 0.32|ω|³.

0.05|ω|³ vs 0.32|ω|³: the negative terms CAN dominate!

So D|S|²/Dt ≤ 0 is NOT guaranteed from scaling alone.

### Why the DATA shows D|S|²/Dt ≤ 0

From the measurement (10/10 negative): the ACTUAL -2tr(S³) and -2tr(SH_dev)
happen to sum to less than |ω|²α/2 in magnitude. But the scaling allows
either sign.

The specific reason: at the max of |ω|, the strain configuration has
det(S) > 0 (from the vorticity-dominated dynamics), making -2tr(S³) < 0.
And tr(SH_dev) is also negative (from the pressure-strain correlation at
the attractor). Both terms help.

But PROVING det(S) > 0 at the max requires... the dynamics again.

## VERDICT

D|S|²/Dt ≤ 0 at the max is MEASURED (10/10) but NOT PROVABLE from
the scaling arguments. The sign depends on det(S) and tr(SH_dev),
both of which require the dynamic attractor.

The gap remains: either prove D|S|²/Dt ≤ 0 at the max (which gives
DH > 0 → DQ < 0 → regularity), or find a different route.

## 298. D|S|²/Dt ≤ 0 measured 10/10 but not provable from scaling.
