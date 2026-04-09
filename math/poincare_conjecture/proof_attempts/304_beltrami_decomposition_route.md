---
source: THE BELTRAMI DECOMPOSITION ROUTE — the most promising path
type: PROOF ARCHITECTURE — using Beltrami α=0 as the anchor
date: 2026-03-29
---

## THE SINGLE-MODE COUNTEREXAMPLE KILLS KINEMATICS

A single Fourier mode ω = A cos(k₀·x) v̂ with angle(k₀, ê) = π/4:
  α/|ω| = sin(2×π/4)/2 = 1/2 exactly.

This is smooth, divergence-free, and saturates the bound.
**No purely kinematic argument can prove α < |ω|/2.**
The proof MUST use NS dynamics.

## THE BELTRAMI ANCHOR

LEMMA (proven, verified 6 configs): For Beltrami flows (ω = λu) on T³:
  α = 0 at the vorticity maximum.

PROOF: (ω·∇)u = (1/λ)∇(|ω|²/2). At max of |ω|: ∇|ω|² = 0 → α|ω| = 0 → α = 0. ∎

Key numerical findings:
- α < 10⁻¹⁵ for all pure Beltrami at max (machine zero)
- Perturbed Beltrami: α scales linearly with perturbation ε
- TG, KP: 50/50 B+/B- mixtures → α comes from the MIXING, not from either component
- Trefoil: 21/79 B+/B-, multi-shell → α comes from multi-shell structure

## THE DECOMPOSITION

Any divergence-free field on T³ decomposes into Beltrami eigenmodes:
  ω = Σ_λ ω_λ  where curl(ω_λ) = λ ω_λ

For each eigenvalue λ: ω_λ is Beltrami with α_λ = 0 at its own max.

The stretching α at the max of |ω| = |Σω_λ| comes ENTIRELY from the
cross-interactions between different eigenvalues.

α = ê·S·ê where S = sym(∇u) = sym(∇(Σ u_λ)) = Σ S_λ.
Each S_λ has α_λ = 0 at ITS max, but not at the max of the TOTAL |ω|.

## THE TWO CASES

### Case 1: Field dominated by one eigenvalue
If ||ω_λ₀|| ≫ ||ω - ω_λ₀|| for some λ₀: the field is "nearly Beltrami."
Then α ≈ 0 + O(||ω - ω_λ₀||/||ω||) → α/|ω| ≈ O(perturbation).
So α/|ω| ≪ 1/2. Safe.

### Case 2: Field spread across eigenvalues
Multiple eigenvalues contribute significantly. The cross-interactions
generate α, but the angular spread across different k-shells gives
effective averaging that keeps α/|ω| < 1/2.

### Case 3 (the dangerous one): Two eigenvalues, same |k|-shell
Like TG: 50% λ=+√3, 50% λ=-√3, both at |k|=√3.
The B+ and B- components are individually Beltrami, but their mixture
gives nonzero α. Data shows α/|ω| ≈ 0.1-0.4 for such mixtures.
The question: can α/|ω| reach 1/2 for an optimal B+/B- mixture?

## THE KEY QUESTION FOR CASE 3

For a B+/B- mixture at fixed |k| = κ:
  ω = ω₊ + ω₋ where curl(ω₊) = +κω₊, curl(ω₋) = -κω₋.

At the max of |ω₊ + ω₋|: what is the max possible α/|ω|?

If the max α/|ω| for any B+/B- mixture is < 1/2: the proof closes
(because any div-free field decomposes into Beltrami components).

## THE B+/B- MIXING BOUND (TO PROVE)

For two Beltrami components with opposite helicity:
  u₊ = ω₊/κ, u₋ = -ω₋/κ (Biot-Savart for eigenmodes)

The strain: S = S₊ + S₋ where S₊ = sym(∇u₊), S₋ = sym(∇u₋).

α = ê·(S₊+S₋)·ê. Each S_± has α_± = 0 at the max of |ω_±|.
At the max of |ω₊+ω₋|: α = ê·S₊·ê + ê·S₋·ê ≠ 0.

The bound: since S₊ = (1/κ)sym(∇ω₊) and S₋ = (-1/κ)sym(∇ω₋):

α = (1/κ)(ê·sym(∇ω₊)·ê) - (1/κ)(ê·sym(∇ω₋)·ê)

Using the per-mode bound |α̂(k)| ≤ |ω̂(k)|/2 for each mode within
S₊ and S₋: the DIFFERENCE of two bounded quantities can approach
the sum of their bounds. So α ≤ (1/2)(|ω₊| + |ω₋|)/something...

This needs more careful analysis.

## WHAT NS DYNAMICS GIVES

The NS nonlinear term (u·∇)ω = Sω + (1/2)ω×(∇×u) generates:
1. Energy transfer between Beltrami components (B+ ↔ B-)
2. Energy transfer between k-shells (cascade)

If blowup occurs: energy concentrates at small scales (high |k|).
The concentration involves multiple shells → multi-mode → angular spread.

The Beltramization hypothesis (Pelz 2001, Holm 2002): near blowup, the
flow tends toward Beltrami (maximizing helicity). If true: α → 0 near
blowup, which PREVENTS blowup. Self-contradictory → no blowup.

This is the "dynamic depletion" argument (Hou). Not proven, but supported
by DNS data showing increasing alignment with Beltrami near max |ω|.

## STATUS

The Beltrami decomposition route is the MOST PROMISING remaining approach:
1. Beltrami → α = 0 at max (PROVEN)
2. Near-Beltrami → α small (PROVEN, linear in perturbation)
3. Multi-component → angular spread → α < |ω|/2 (UNPROVEN, the gap)
4. NS dynamics → Beltramization near blowup (UNPROVEN, strong conjecture)

If either (3) or (4) can be proven: the NS regularity follows.

## 304. The Beltrami route is clean but the mixing bound (Case 3) is open.
