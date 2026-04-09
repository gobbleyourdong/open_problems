# Attempt 044 — CORRECTION: Elitzur Argument Was Wrong

**Date**: 2026-04-07
**Phase**: 4 (Verification — self-correction)
**Instance**: Even (Theory)

## The Error in Attempt 042

I claimed the disconnected term ⟨Tr(M₁)Tr(M₂†)⟩ vanishes by Elitzur's
theorem. **This is WRONG.**

### The Actual Computation

The gradient inner product (Fierz identity for SU(2), T^a = σ^a/2):

  Σ_a Tr(T^a A) Tr(T^a B)† = (1/2)Tr(AB†) - (1/4)Tr(A)Tr(B†)

With A = U_e · staple_P(e), B = U_e · staple_Q(e):

  = (1/2)Tr(staple_P · staple_Q†) - (1/4)Tr(U_P)Tr(U_Q†)

**Both terms are gauge-invariant.** Elitzur does NOT kill either.

- Tr(staple_P · staple_Q†) = chair loop (closed, gauge-invariant)
- Tr(U_P) · Tr(U_Q†) = product of two plaquette traces (gauge-invariant)

## The Actual Gradient Correlation

E[⟨∇O, ∇ΔS⟩] = Σ_e Σ_{P∋e, Q∈Σ∩e} w_P · 2d_j c_j ×
    [(1/2)⟨Tr(chair_{P,Q})⟩ - (1/4)⟨Tr(U_P)Tr(U_Q†)⟩]

## Sign Analysis

### Strong coupling (β → 0):
- ⟨Tr(chair)⟩ ≈ 2c_{1/2}² (leading character expansion term)
- ⟨Tr(U_P)Tr(U_Q†)⟩ ≈ 4c_{1/2}² (if P,Q close) or ~ 0 (if far)
- For ADJACENT plaquettes (sharing link e): both O(c_{1/2}²)
- Combination: c_{1/2}² - c_{1/2}² = 0 at leading order!
  Need next order to determine sign.

Actually: ⟨Tr(U_P)Tr(U_Q†)⟩ = ⟨Tr(U_P)⟩⟨Tr(U_Q†)⟩ + Cov
At strong coupling: ⟨Tr(U_P)⟩ = 2c_{1/2} + O(c^3)
So: ⟨Tr(U_P)⟩² = 4c_{1/2}² + O(c^4)
And: Cov = O(c_{1/2}^{dist}) which is O(c_{1/2}²) for adjacent plaquettes.

So: (1/4)⟨Tr(U_P)Tr(U_Q†)⟩ = c_{1/2}² + O(c^3)
And: (1/2)⟨Tr(chair)⟩ = c_{1/2}² + O(c^3)

The LEADING TERMS CANCEL. The sign comes from O(c^3) corrections.

### Weak coupling (β → ∞):
- ⟨Tr(chair)⟩ → 2 (both plaquettes ≈ I)
- ⟨Tr(U_P)Tr(U_Q†)⟩ → 4 (both traces ≈ 2)
- Combination: (1/2)·2 - (1/4)·4 = 1 - 1 = 0

**The margin goes to ZERO at weak coupling.**

The sign at weak coupling depends on O(1/β) corrections:
  (1/2)(2 + a/β) - (1/4)(4 + b/β) = (2a - b)/(4β)

where a, b are the 1/β corrections to the chair and plaquette-product
expectations respectively. The sign of (2a - b) determines whether the
gradient correlation is positive or negative at weak coupling.

## The Deeper Issue

The gradient correlation (1/2)⟨chair⟩ - (1/4)⟨plaq·plaq⟩ is:
- Positive at strong coupling? (need O(c³) analysis)
- Zero at weak coupling (leading cancellation)
- Sign from subleading terms at both extremes

**This is NOT "obviously positive." The leading-order terms cancel at
BOTH strong and weak coupling.** The sign is a delicate O(c³) or O(1/β)
effect.

## Does the Odd Instance's Argument Survive?

The Odd instance's claim was: "character expansion for connected loops has
all positive terms, so ⟨Tr(chair)⟩ > 0." This is TRUE but INSUFFICIENT.
We need (1/2)⟨chair⟩ > (1/4)⟨plaq·plaq⟩, which is a COMPARISON, not just
positivity.

The 6j wall manifests HERE: the comparison involves both connected and
disconnected quantities, and their relative size determines the sign.

## The Revised Status

**The wall is NOT broken.** My attempt_042 verification was wrong (Elitzur
doesn't apply — both terms are gauge-invariant). The gradient correlation
has a leading-order cancellation, and the sign depends on subleading terms.

The Odd instance's numerical results (pattern_033: Δ(t) ≥ 0 at all times)
suggest the gradient correlation IS positive, but the proof is not in hand.

## What Would Close It

Need to prove: (2a - b) > 0 at weak coupling, where:
  a = (d/dβ) ⟨Tr(chair)⟩
  b = (d/dβ) ⟨Tr(U_P)Tr(U_Q†)⟩

This is a COMPUTABLE quantity in perturbation theory (Feynman diagrams
in lattice perturbation theory). The Odd instance should compute it.

At strong coupling: need the O(c³) term in the character expansion.
This involves 3-plaquette tilings of the minimal surface bounded by
the chair loop minus the minimal surface bounded by the two plaquettes.
The combinatorics of the tiling determines the sign.

## Result

**CORRECTION**: The wall is not broken. The gradient correlation has a
leading-order cancellation. The sign depends on subleading terms that
need explicit computation.

The Odd instance's numerical evidence (Δ(t) ≥ 0) is still valid and
suggests the sign is correct. But the Even instance's "proof" was wrong.

**For Odd Instance**: Compute the gradient correlation
(1/2)⟨Tr(chair)⟩ - (1/4)⟨Tr(P)Tr(Q†)⟩ numerically at various β.
Track its sign. If always positive: the Langevin argument works but
needs a proof of the subleading sign.
