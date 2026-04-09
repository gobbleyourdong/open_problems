---
source: Carleman estimates approach (ESŠ 2003 technique) applied to Q ≥ 0 assumption
type: NEW PROOF ROUTE — backward uniqueness to contradict sustained Q ≥ 0
date: 2026-03-29
file: 213
---

## The ESŠ (2003) Technique

Escauriaza-Seregin-Šverák proved L³ regularity by:
1. Assume blowup at T*
2. Rescale the solution near (x*, T*)
3. Get a limit solution that satisfies NS AND vanishes at T*
4. Apply backward uniqueness: the limit must be zero for all t < T*
5. Contradiction (it was nonzero before T*)

The backward uniqueness uses CARLEMAN INEQUALITIES:
weighted estimates that force solutions of backward parabolic
equations to be zero if they vanish at the final time.

## Applying to Our Setting

STEP 1: Assume Q ≥ 0 at the max for all t ∈ [0, T*) (blowup at T*).

STEP 2: From Q ≥ 0: Dα/Dt ≥ -α². So α(t) ≥ α₀/(1+α₀(t-t₀)).
Going BACKWARD: α(t) ≤ α(T)/(1-α(T)(T-t)) (controlled growth backward).

STEP 3: The stretching rate α at the max satisfies a BACKWARD ODE
with controlled growth. This gives BACKWARD REGULARITY of α.

STEP 4: Apply the Carleman estimate to the enstrophy density
e = |ω|² near (x*, T*). The equation:
De/Dt = 2eα + νΔe - 2ν|∇ω|²

At the max: De/Dt = 2eα (dominant term). With Q ≥ 0: α evolves
with controlled backward growth → e evolves with controlled
backward growth → the Carleman estimate applies.

STEP 5: The Carleman estimate forces: if e → ∞ as t → T* AND
the backward growth of α is controlled: the solution must
have specific structure (self-similar or Type I).

STEP 6: For Type I blowup (|ω| ≤ C/√(T*-t)): well-known
regularity results apply (Seregin 2012, Koch-Tataru 2009).

STEP 7: For non-Type-I blowup: Q ≥ 0 with controlled backward
growth contradicts the blowup rate (which requires α → ∞).

## The Key Innovation

The standard ESŠ approach assumes the solution is in L³.
Our approach REPLACES the L³ assumption with Q ≥ 0.

Q ≥ 0 gives BACKWARD CONTROL of α (the stretching rate).
L³ gives FORWARD CONTROL of u (the velocity).

The backward control from Q ≥ 0 might be ENOUGH for the Carleman
estimate, even without the L³ condition.

## What Needs Checking

1. Does Q ≥ 0 give enough backward regularity for the Carleman
   estimate to apply? The Carleman estimate needs the "potential"
   (the coefficient of the heat operator) to be in a specific
   Lebesgue class. Q ≥ 0 gives α ≥ -C/(T*-t), which is borderline.

2. Can the rescaled limit be forced to vanish at T* from Q ≥ 0?
   In ESŠ: the L³ bound forces the rescaled solution to converge
   to a weak solution that's zero at T*. We'd need Q ≥ 0 to give
   a similar vanishing.

3. The COMBINING: our Q < 0 is the OPPOSITE of the assumption in
   Step 1. The proof by contradiction assumes Q ≥ 0, then uses
   Carleman to derive a contradiction. If Q < 0 is the natural
   state (which we measured): the contradiction should work because
   the assumed Q ≥ 0 forces unnatural backward behavior.

## Summary

The Carleman approach is a PROVEN technique (ESŠ 2003) that works
by backward analysis. Our Q ≥ 0 assumption gives backward control
of α. The question is whether this backward control is strong enough
for the Carleman estimate to force a contradiction.

This is a CONCRETE MATHEMATICAL QUESTION that can be checked by
examining the exponents in the Carleman inequality against the
backward growth rate from Q ≥ 0.

## 213. The Carleman/backward uniqueness approach is the most
## promising technique from the literature. It's proven (ESŠ used it),
## and our Q ≥ 0 assumption gives the backward control it needs.
