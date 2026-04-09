---
source: THE BARRIER + BELTRAMI MIXING — formalizing the self-limiting mechanism
type: PROOF ATTEMPT — the cleanest architecture we have
date: 2026-03-29
---

## THE BARRIER ARGUMENT

Define R(x,t) = α(x,t)/|ω(x,t)| at any point where |ω| > 0.
Define Φ(t) = sup over {x : |ω(x,t)| = ||ω(t)||∞} of R(x,t).

At the max of |ω|, along a Lagrangian trajectory:
  D|ω|/Dt = α|ω|  and  Dα/Dt = S²ê - 2α² - H_ωω

So: DR/Dt = D(α/|ω|)/Dt = (Dα/Dt - α²)/|ω| = (S²ê - 3α² - H_ωω)/|ω| = Q/|ω|
    [where we used Q = Var - H_ωω = S²ê - α² - H_ωω and
     D(α/|ω|)/Dt = (S²ê - 2α² - H_ωω - α²)/|ω| = (S²ê - 3α² - H_ωω)/|ω|]

Wait, let me recompute. DR/Dt at the max:
  DR/Dt = (Dα/Dt)/|ω| - α(D|ω|/Dt)/|ω|²
         = (S²ê - 2α² - H_ωω)/|ω| - α²/|ω|
         = (S²ê - 3α² - H_ωω)/|ω|
         = (Var - 2α² - H_ωω)/|ω|
         = (Q - 2α²)/|ω|

So DR/Dt = (Q - 2α²)/|ω|. Note: this is NOT Q/|ω|. It's B/|ω| where B = Q - 2α².

At Q = 0: B = -2α² < 0. So R ALWAYS decreases when Q = 0 (regardless of α). ✓

## AT α/|ω| = 1/2 WITH c₁ = 1

α = λ₁ = |ω|/2. Var = 0. Q = -H_ωω < 0.
B = Q - 2α² = -H_ωω - |ω|²/2 < 0 (strongly negative).
DR/Dt = B/|ω| < 0. R decreases. ✓

## AT α/|ω| = 1/2 WITH c₁ < 1

α = |ω|/2, c₁ < 1. Var > 0. Q = Var - H_ωω.
B = Q - 2α² = Var - H_ωω - |ω|²/2.
Since Var ≤ |S|² and H_ωω > 0:
B ≤ |S|² - |ω|²/2.

For B < 0: need |S|² < |ω|²/2. THIS IS THE ATTRACTOR CONDITION (weakened).
At the attractor |S|² = |ω|²/4 < |ω|²/2: B < 0. ✓
Without the attractor: |S|² could exceed |ω|²/2, making B > 0. ✗

## THE GAP: |S|² < |ω|²/2 AT α/|ω| = 1/2

For R = α/|ω| = 1/2: α = |ω|/2. And α ≤ |S| (since α ≤ λ₁ ≤ |S|).
So |S| ≥ |ω|/2, meaning |S|² ≥ |ω|²/4.

We need: |S|² < |ω|²/2 at the max of |ω| when α = |ω|/2.

From the global L² identity: ∫|S|² = ∫|ω|²/2. So the AVERAGE |S|²/|ω|² = 1/2.
At the max of |ω|: we want |S|²/|ω|² < 1/2, i.e., BELOW the average.

This is plausible (the max of |ω| has ω concentrated, strain more spread out),
but we showed |S|² can exceed |ω|²/4 at the max (Kida-Pelz: |ω|²/|S|² = 1.94,
meaning |S|² ≈ |ω|²/1.94 ≈ 0.515|ω|², which EXCEEDS |ω|²/2 = 0.5|ω|²).

SO THE CONDITION |S|² < |ω|²/2 IS VIOLATED at early transient times!

However: at those times, α/|ω| is much less than 1/2 (the alignment prevents it).

The joint condition: α = |ω|/2 AND |S|² > |ω|²/2 simultaneously is NOT observed.
Because α = |ω|/2 requires c₁ near 1, which requires ω aligned with e₁.
And when ω ≈ e₁: α ≈ λ₁ and Var ≈ 0. So Q ≈ -H_ωω < 0.

## THE BELTRAMI DECOMPOSITION PERSPECTIVE

Every div-free field on T³: ω = Σ_{k,σ} â_{k,σ} ψ_{k,σ}(x)
where ψ_{k,σ} are curl eigenmodes: curl(ψ_{k,σ}) = σ|k| ψ_{k,σ}, σ = ±1.

For a SINGLE eigenmode ψ_{k,+1}: Beltrami → α = 0 at max |ω|.
For a PAIR ψ_{k,+1} + ψ_{k,-1} (same |k|, opposite helicity): NOT Beltrami.

TG and KP are 50/50 B+/B- mixtures. α comes from the mixing.
Trefoil is multi-shell + mixed helicity. α comes from both effects.

## THE MIXING BOUND

For ω = aψ₊ + bψ₋ (two modes, same |k|, opposite helicity):
  u = (a/κ)ψ₊ - (b/κ)ψ₋ (Biot-Savart for eigenmodes, κ = |k|)

The strain:
  S = sym(∇u) = (a/κ)sym(∇ψ₊) - (b/κ)sym(∇ψ₋)

At the max of |ω| = |aψ₊ + bψ₋|:
  α = ê·S·ê = (a/κ)ê·sym(∇ψ₊)·ê - (b/κ)ê·sym(∇ψ₋)·ê

Each term: ê·sym(∇ψ_σ)·ê is the strain of a Beltrami mode projected onto ê.
The Beltrami property: at the max of |ψ_σ|, this projection is zero.
But at the max of |aψ₊ + bψ₋|: it's NOT zero (different max location).

The KEY: the max of the MIXTURE is at a DIFFERENT point than the max of
each component. At this mixture-max: neither component has vanishing strain.

## CAN α/|ω| = 1/2 FOR A B+/B- MIXTURE?

For the ABC flow with A = B = C (pure B+, single mode):
  α = 0 at max. α/|ω| = 0.

For a mixture 50/50 B+/B-:
  α/|ω| ≈ 0.1-0.4 (from numerical data).

For an OPTIMAL mixture: what's the max α/|ω|?

The answer depends on the SPECIFIC Fourier modes. For modes at |k| = √3
(like TG): the geometry constrains α/|ω| through the per-mode bound.

From the per-mode bound: each mode contributes |α̂| ≤ |ω̂|/2.
For a B+ mode: ω̂ = a × ê_+ with curl eigenvalue +κ.
For a B- mode: ω̂ = b × ê_- with curl eigenvalue -κ.

The strain contributions: S_+ = (1/κ)sym(∇(aψ_+)), S_- = (-1/κ)sym(∇(bψ_-)).

Since the Biot-Savart FLIPS the sign for B-: u_- = -ψ_-/κ (the minus sign).

So α = ê·S₊·ê + ê·S₋·ê. The S₊ and S₋ can ADD or CANCEL depending on
the relative phase of the B+ and B- components at the mixture max.

For MAXIMUM α: S₊ and S₋ should ADD (same sign).
For each: |ê·S_σ·ê| ≤ |S_σ| ≤ |ω_σ| (from |S_σ| ≤ |ω_σ|...
actually |S_σ| = |ω_σ|/κ × |∇ψ_σ|/|ψ_σ| × (geometric factor)).

For Beltrami modes: |S_σ| = |ω_σ|/(2κ) × (geometric factor at each point).
Actually for a single Fourier mode ψ_σ = e^{ik·x} × v̂:
  S_σ = (σ/κ)sym(ik ⊗ v̂)e^{ik·x}
  |S_σ| = |k||v̂|/(2κ) = |v̂|/2 = |ω_σ|/2 (since |k| = κ for an eigenmode).

Hmm, |S_σ| = |ω_σ|/2 for a single eigenmode. And α_σ = ê·S_σ·ê ≤ |S_σ| = |ω_σ|/2.

For the mixture: α = α₊ + α₋ ≤ |ω₊|/2 + |ω₋|/2 = (|ω₊|+|ω₋|)/2.
And |ω| = |ω₊ + ω₋| ≤ |ω₊| + |ω₋|.

So: α/|ω| ≤ (|ω₊|+|ω₋|) / (2|ω₊+ω₋|).

By triangle inequality: |ω₊+ω₋| ≤ |ω₊|+|ω₋|.
So: α/|ω| ≤ (|ω₊|+|ω₋|)/(2|ω₊+ω₋|) ≥ 1/2.

WAIT — this gives α/|ω| ≤ something ≥ 1/2. The bound is NOT < 1/2!

The bound: α ≤ (|ω₊|+|ω₋|)/2 and |ω| = |ω₊+ω₋| ≤ |ω₊|+|ω₋|.
So: α/|ω| ≤ (|ω₊|+|ω₋|)/(2|ω₊+ω₋|).

At the max of |ω₊+ω₋|: if ω₊ and ω₋ are ANTI-PARALLEL (worst case for |ω|):
|ω₊+ω₋| = ||ω₊|-|ω₋|| (if anti-parallel).
Then: α/|ω| ≤ (|ω₊|+|ω₋|)/(2||ω₊|-|ω₋||) → ∞ as |ω₊| → |ω₋|.

But |ω| = ||ω₊|-|ω₋|| → 0 in this limit. So α/|ω| blows up, but |ω| → 0.
This is not a blowup point (|ω| is small, not maximal).

At the ACTUAL max of |ω₊+ω₋|: the components are CO-ALIGNED (not anti-parallel).
So |ω₊+ω₋| = |ω₊|+|ω₋| (maximum addition).
Then: α/|ω| ≤ (|ω₊|+|ω₋|)/(2(|ω₊|+|ω₋|)) = 1/2.

Equality requires: α₊ = |ω₊|/2 and α₋ = |ω₋|/2 simultaneously at the max of |ω|.
This requires OPTIMAL alignment of both components with the strain eigenvectors.

For a SINGLE k-shell (like TG): the modes have specific k-vectors and the
alignment is fixed by the geometry. The max α_σ/|ω_σ| at the MIXTURE max is
generally < 1/2 for each component (because the mixture max is not the
component max).

## THE FUNDAMENTAL BOUND

α/|ω| ≤ 1/2 FOR B+/B- MIXTURES at the max of |ω| (from per-mode bound).

Equality iff:
1. ω₊ and ω₋ are co-aligned at the max (max of |ω₊+ω₋|)
2. α₊ = |ω₊|/2 and α₋ = |ω₋|/2 at that point (each component at its strain max)

Condition 2 is GENERICALLY impossible at the MIXTURE max (which differs from
each component's max). But for special configurations: it might hold.

## STATUS

The per-mode bound gives α ≤ |ω|/2 (tight). The question is whether equality
is achievable at the max of |ω| for NS solutions. The Beltrami observation
(α = 0 for single helicity) and the mixing analysis suggest the bound is
approachable but not achievable for solutions with nontrivial dynamics.

THE PROOF NEEDS: either
(a) Show equality in per-mode bound is not achievable at max for smooth fields
(b) Show NS dynamics prevents the special configuration
(c) Prove the attractor |S|² < |ω|²/2 which gives B < 0 in the barrier

## 305. The barrier + Beltrami mixing gives α/|ω| ≤ 1/2 (tight).
## Equality requires a special conspiracy that is not observed in NS dynamics.
## The proof needs one more step to make this rigorous.
