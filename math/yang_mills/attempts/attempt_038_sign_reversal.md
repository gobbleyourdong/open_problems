# Attempt 038 — The Sign Reversal: Why (5.15) is Strong-Coupling-Specific

**Date**: 2026-04-07
**Phase**: 4 (Understanding the Wall)
**Track**: theory (Theory)

## Critical Observation

The comparison ⟨O⟩₋ vs ⟨O⟩₊ REVERSES between strong and weak coupling.

### At Strong Coupling (β → 0)
Disorder dominates. All states are nearly equally populated.
The center-odd sector has slightly MORE plaquette response than even sector
(cluster expansion gives ⟨O⟩₋ > ⟨O⟩₊ by a small margin).
→ (5.15) HOLDS ✓

### At Weak Coupling (β → ∞), Large N_t
The vacuum |0⟩ (center-even) dominates both sectors.
⟨O⟩₊ → ⟨0|Ô|0⟩ = max ordering (vacuum is maximally ordered)
⟨O⟩₋ → ⟨1|Ô|1⟩ = less ordering (flux tube state, partially disordered)

So ⟨O⟩₊ > ⟨O⟩₋ at weak coupling, large N_t.
→ (5.15) would FAIL ✗

### But This Is NOT a Problem for Tomboulis

Tomboulis's argument DECIMATES to strong coupling. After n₀ MK steps,
the coefficients are small. (5.15) is applied ONLY to the decimated theory
(where it holds by cluster expansion), not to the original theory.

**The sign reversal explains WHY (5.15) can't hold at all couplings — and
why Tomboulis doesn't need it to.** His framework uses the MK decimation
to move the problem to the right regime.

## What This Means for the Earlier Attempts

**Attempts 028-036 were asking the wrong question.** I was trying to prove
(5.15) at arbitrary coupling. This is IMPOSSIBLE (the sign reverses at
weak coupling). The correct question is:

"Does Tomboulis's propagation from step n₀ (where (5.15) holds) back
to step 0 work correctly?"

This is purely about the INTERPOLATION MACHINERY, not about (5.15) itself.

## Re-reading Ito-Seiler with Fresh Eyes

Ito-Seiler's critique (arXiv:0711.4930) is NOT about (5.15) failing.
They agree (5.15) holds at strong coupling. Their concern is about the
INTERPOLATION: specifically, whether the common interpolation parameter
α^{(m)} exists at each decimation step, and whether it's uniform in |Λ|.

The interpolation requires eq. 5.14 (existence of a common t = t^{(n)})
which requires (5.15) only at the FINAL step (strong coupling).

**So what exactly is Ito-Seiler's objection?**

Re-reading their paper carefully: they say the implicit function theorem
argument (Tomboulis's Appendix C) breaks down because the inequality
(5.15) is needed to ensure Ψ_t ≠ 0 (the denominator in the IFT).
Tomboulis claims this is only at strong coupling. Ito-Seiler say
"it is not clear where and how his claim is proven for large beta."

**The resolution**: If the decimation correctly flows to strong coupling
(proved: sandwich theorem), and (5.15) holds at strong coupling (proved:
cluster expansion), then the IFT applies at the FINAL step. The question
is whether the IFT at the final step PROPAGATES correctly to the original.

This propagation is a FINITE number of IFT steps (n₀ steps). At each
step m < n₀: the IFT gives α^{(m)} as a function of α^{(m+1)}, ..., α^{(n₀)}.
The existence of α^{(m)} requires the IFT conditions at step m.

**But the IFT conditions at step m involve the coefficients at step m,
which may NOT be in the strong coupling regime.**

## The Crux (Final Formulation)

At step m < n₀: the coefficients c̃_j(m) are BETWEEN the upper and lower
bounds, but not necessarily small. The IFT requires Ψ_t ≠ 0 at step m,
which is equivalent to (5.15) at step m.

(5.15) at step m: holds if c̃_j(m) is in the cluster expansion regime.
But c̃_j(m) may be too large for the cluster expansion at intermediate steps.

**The sign reversal at weak coupling confirms**: (5.15) can fail at
intermediate coupling. So the IFT might not apply at intermediate steps.

## Is There a Way Around?

The sign reversal occurs at large N_t (weak coupling limit). But the
Tomboulis construction works at FINITE N_t. At finite N_t with the
MK-decimated coefficients:

- After n₀ steps: coefficients small → (5.15) holds → IFT works at step n₀
- After n₀-1 steps: coefficients slightly larger → (5.15) might still hold
- ...
- After 0 steps: original coupling → (5.15) might fail (sign reversal)

The MK decimation SMOOTHLY interpolates between the original and decimated
theories. The sign reversal happens at WEAK coupling with LARGE N_t. At
FINITE N_t (as in Tomboulis's construction), the sign reversal is suppressed
by the mass gap: the difference ⟨O⟩₋ - ⟨O⟩₊ is O(e^{-ΔN_t}) at weak coupling.

**At finite N_t**: the sign reversal becomes:
⟨O⟩₋ - ⟨O⟩₊ = O(e^{-ΔN_t}) × (negative for vacuum dominance)

But for the DECIMATED lattice at step m: N_t is REDUCED by the decimation
(N_t → N_t/b^m). After enough steps, N_t is O(1) and the sign is controlled
by the cluster expansion.

**So**: at step n₀, the time extent is N_t/b^{n₀} which is small, so the
cluster expansion (which also controls finite-N_t effects) gives (5.15).
At earlier steps, the time extent is larger, and (5.15) depends on the
competition between cluster expansion decay and finite-volume effects.

## The Real Question (Definitive)

**Does the MK decimation reduce BOTH the spatial and temporal extents fast
enough that (5.15) holds at every step, UNIFORMLY in the original lattice?**

This is a QUANTITATIVE question about the rates:
- Rate of coefficient decay: c̃_j(m) ≤ c_j^U(m) (super-exponential)
- Rate of lattice shrinking: |Λ^m| = |Λ|/b^{dm} (exponential)
- Rate of time extent reduction: N_t^{(m)} = N_t/b^m (exponential)
- Cluster expansion convergence condition: c̃_j < ε₀(d) (volume-independent)

If the coefficient decay BEATS the lattice shrinking, then at step m:
c̃_j(m) < ε₀ AND N_t^{(m)} is small → cluster expansion converges
→ (5.15) holds → IFT applies.

The coefficient decay is super-exponential: c_j^U(m) ~ c_j(0)^{b^{2m}}.
The lattice shrinking is polynomial in b^m.
Super-exponential beats polynomial: c_j^U(m) reaches ε₀ BEFORE the
lattice becomes too small to be meaningful.

## Conclusion

The sign reversal of ⟨O⟩₋ - ⟨O⟩₊ at weak coupling is REAL but doesn't
invalidate Tomboulis's approach. The MK decimation reduces coefficients
super-exponentially while shrinking the lattice only exponentially.
This means (5.15) becomes valid BEFORE the lattice degenerates.

**The remaining gap is quantitative**: does n₀ (steps to reach ε₀) satisfy
n₀ < n_max (steps before lattice becomes trivial)?

Since c_j^U(n) decays super-exponentially and the lattice size decreases
exponentially (b^{dm} per step), the race is super-exp vs exp:

n₀ ~ log log(1/ε₀) / log(b²)  (super-exp: very few steps needed)
n_max ~ log(N_t) / log(b)       (exp: O(log N_t) steps available)

For any fixed β and ε₀: n₀ is a CONSTANT (independent of |Λ|).
n_max grows as log(N_t) → ∞.
So n₀ < n_max for large enough lattice. ✓

**THIS CLOSES THE GAP** (modulo the quantitative estimate of ε₀ vs n₀).

## Status: POTENTIALLY RESOLVED

The sign reversal motivated a re-examination that actually SUPPORTS
Tomboulis's argument: the super-exponential coefficient decay ensures
(5.15) becomes valid while the lattice is still large enough.

The wall may have just developed a crack.
