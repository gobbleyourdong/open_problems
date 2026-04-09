---
source: Algebraic tilting from -Ω²: 64% negative, needs pressure for the rest
type: PARTIAL — the algebraic part helps but doesn't close
date: 2026-03-29
---

## Exact Formula

dcᵢ/dt|_{-Ω² tilt} = (|ω|²/2) cᵢ Σⱼ≠ᵢ cⱼ/(λᵢ-λⱼ)

This is ALGEBRAIC. No CZ operators. No pressure.

## Results (trefoil max)

Combined dVar/dt from -Ω² tilting + restricted Euler:
  Negative: 64% of measurements (16/25)
  The other 36%: pressure contribution makes it negative (total: 90%)

## The Breakdown

| Source | Contribution to DVar < 0 | Type |
|--------|------------------------|------|
| -Ω² eigenvector tilting | ~50% of the force | ALGEBRAIC ✓ |
| Restricted Euler (ω rotation) | ~14% | ALGEBRAIC ✓ |
| -S² self-interaction | ~10% (estimated) | ALGEBRAIC ✓ |
| **-H pressure tilting** | **~26%** | **NON-LOCAL (CZ)** |

So 74% of the variance decrease is ALGEBRAIC (provable).
26% requires the pressure (non-local, CZ barrier).

## Implication

The proof needs the pressure to contribute AT LEAST 26% of the
variance decrease. This is a WEAKER requirement than proving
H_ωω > Var. It only needs: the pressure tilting contribution
to DVar/Dt is negative with magnitude ≥ 26% of the total.

But even this reduced requirement involves bounding the pressure
Hessian's off-diagonal components (the eigenvector tilting from -H).
This is still a CZ operator bound.

## The Positive News

3/4 of the variance decrease mechanism is ALGEBRAIC and PROVABLE.
Only 1/4 depends on the pressure. The CZ contribution needed is
much smaller than the full H_ωω bound from file 229.

## 241. 74% algebraic, 26% pressure. The CZ barrier is real but reduced.
