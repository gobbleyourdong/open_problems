---
source: Instance A VALIDATION — attacking Step 5 (DH_ωω/Dt > 0)
type: ADVERSARIAL REVIEW
date: 2026-03-29
---

## Step 5 Claims

"Apply the STATIC Fourier lemma (Step 2) to D(Δp)/Dt instead of Δp.
The z-cosine component of D(Δp)/Dt is positive (from P2, Step 4).
Therefore: DH_ωω/Dt > 0."

## Attack 1: Can we apply the Fourier lemma to D(Δp)/Dt?

The Fourier lemma (Step 2): if f_k > 0 at x* (the k-th z-Fourier
mode of the source is positive): then (Δ_xy - k²)⁻¹ f_k < 0 at x*
→ H_zz contribution > 0.

To apply this to D(Δp)/Dt: need the k-th z-cosine mode of D(Δp)/Dt
to be positive at x*.

Step 4 claims: ∫|ω|²α cos(kz) dz > 0 (the P2 condition).

But D(Δp)/Dt ≠ |ω|²α. The source evolution:
D(Δp)/Dt = D(|ω|²/2 - |S|²)/Dt = |ω|²α - D|S|²/Dt + ...

The D|S|²/Dt term involves the strain evolution, which is complex.

So: Step 5 CONFLATES the enstrophy production |ω|²α with the
full source evolution D(Δp)/Dt. They are DIFFERENT.

## Attack 2: Is D(Δp)/Dt = |ω|²α correct?

D|ω|²/Dt = 2|ω|²α (exact, at a material point).
D|S|²/Dt = -2S_ij S_jk S_ki - 2S_ij Ω²_ij - 2S_ij H_ij + ... (from DS/Dt = -S² - Ω² - H).

So: D(Δp)/Dt = |ω|²α - D|S|²/Dt.

The D|S|²/Dt term is O(|ω|² × |S|²) (from the cubic terms in the
strain equation). It's NOT negligible.

Step 5 appears to assume D(Δp)/Dt ≈ |ω|²α, dropping the D|S|²/Dt term.
This is unjustified.

## Attack 3: Does D(Δp)/Dt have positive z-cosine modes?

Even if we correctly compute D(Δp)/Dt: the z-cosine modes might be
negative (from the D|S|²/Dt contribution). The P2 condition only
bounds the |ω|²α part, not the full source evolution.

## SEVERITY: HIGH

Step 5 has a significant gap: the Fourier lemma applied to D(Δp)/Dt
requires the full source evolution, not just the enstrophy production.
The D|S|²/Dt term could flip the sign of the z-cosine modes.

## RECOMMENDATION: Step 5 needs the full computation of D(Δp)/Dt
## including the strain evolution. The P2 condition (∫|ω|²α cos > 0)
## alone is NOT sufficient for DH_ωω/Dt > 0.

## Alternatively: bound DH_ωω/Dt DIRECTLY without using the Fourier lemma
## on the time derivative. This might require a different approach entirely.
