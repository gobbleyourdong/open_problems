# Attempt 009 — Li Criterion: Structure Revealed

**Date**: 2026-04-07
**Phase**: 1 (Pattern Discovery)
**Track**: numerical

## The Structure

For ρ = 1/2 + iγ on the critical line:
  w = (ρ-1)/ρ satisfies |w| = 1 exactly.
  Per-zero contribution: 2(1 - cos(nφ)) ≥ 0 always.

For ρ OFF the critical line:
  |w| ≠ 1. If |w| > 1: contribution diverges negatively for large n.

**Li's criterion IS RH.** Not a simplification, not a new route — the SAME
statement viewed through the lens of the map w = (ρ-1)/ρ.

## What This Means for the systematic approach

The Li criterion plays the role of the SOS certificate: it CONFIRMS RH
computationally (λ_n > 0 for all tested n) but doesn't provide a proof
path. The difficulty is proving |w| = 1 for ALL zeros, which is RH itself.

**Unlike YM (where the certificate GC > 0 led to a proof architecture),
the RH certificate λ_n > 0 doesn't suggest HOW to prove it.**

## The Phase Structure

The phases φ_k = arg(w_k) ≈ 1/(2γ_k) decay as 1/γ_k.
The Li coefficient: λ_n = Σ_k 2(1 - cos(nφ_k))
            ≈ Σ_k n²φ_k² for small nφ_k (leading term)
            = n² Σ_k 1/(4γ_k²)

This gives λ_n ≈ n² × (constant) for small n, transitioning to
λ_n ≈ (n/2)log(n) for large n (when nφ_k is no longer small).

The transition happens at n ≈ 2γ_1 ≈ 28 (the first zero's "wavelength").

## Comparison Across Problems

| Problem | Certificate | Is it RH-equivalent? |
|---------|-----------|---------------------|
| NS | Q > 0 (SOS) | No — weaker (Key Lemma ≠ regularity) |
| YM | GC > 0 (MC) | Conditional — leads to proof via Langevin |
| RH | λ_n > 0 (Li) | YES — equivalent to RH exactly |

The NS and YM certificates are WEAKER than the full conjecture, which is
why they led to proof architectures. The RH certificate IS the conjecture.

## For theory track

Li's criterion is a DEAD END for proof purposes — it doesn't simplify RH.
The productive routes are:
1. Hilbert-Pólya (find the operator)
2. Arithmetic geometry (Weil analog for Q)
3. Moment methods (prove enough moments of ζ match GUE)
4. Zero-free region improvements (push the 2/3 barrier)

The numerical data (λ_n, Robin, GUE statistics) supports RH overwhelmingly
but doesn't suggest which route will work. This is a HARDER problem than
YM — there's no "Tomboulis framework" to plug into.

## 009. Li's criterion = RH restated. Certificate confirms but doesn't prove.
## The phases φ_k ≈ 1/(2γ_k) control the oscillatory structure.
## RH is structurally harder than YM — no framework to plug the certificate into.
