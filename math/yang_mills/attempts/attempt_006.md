# Attempt 006 — No Phase Transition → Mass Gap (Theory Route)

**Date**: 2026-04-07
**Phase**: 2 (Formalization)
**Instance**: Even (Theory)

## The Argument Structure

**Theorem (conditional)**: If SU(2) lattice gauge theory in d=4 has no phase
transition in the coupling β, then the mass gap Δ(β) > 0 for all β > 0.

**Proof sketch**:
1. At β = 0 (infinite coupling): Δ(0) = ∞ (trivially — all links independent,
   no correlation between plaquettes).
2. At β small (strong coupling): Δ(β) > 0 proven by Osterwalder-Seiler cluster
   expansion (1978). Specifically, exponential decay of correlations with rate
   Δ ~ -ln(β/4) > 0.
3. Δ(β) is a continuous function of β (follows from analyticity of the free
   energy in the absence of phase transitions).
4. If Δ(β₀) = 0 for some β₀, then by continuity, Δ must cross zero at some
   β* < β₀. At β*, the correlation length ξ = 1/Δ diverges — this IS a phase
   transition (second order) or a discontinuity in Δ (first order).
5. No phase transition ⟹ Δ never reaches zero ⟹ Δ(β) > 0 for all β.  ∎

## What "No Phase Transition" Means (precisely)

For the infinite-volume lattice theory, define:
- Free energy density: f(β) = -lim_{V→∞} (1/V) ln Z_V(β)
- Mass gap: Δ(β) = -lim_{|x|→∞} (1/|x|) ln G(x), where G(x) = ⟨Tr U_P(0) Tr U_P(x)⟩_c

**No phase transition** means:
(a) f(β) is analytic (C^ω) for all β > 0, AND
(b) Δ(β) is continuous for all β > 0

Actually (a) implies (b) in most settings (Lee-Yang / correlation length analyticity).

## What's Known

### Osterwalder-Seiler (1978, 1980)
- Proved: reflection positivity for Wilson action on the lattice
- Proved: convergence of cluster expansion at strong coupling (small β)
- This gives: free energy is analytic for β < β_c(OS) for some finite β_c(OS)
- Mass gap Δ(β) > 0 for β < β_c(OS)

### Creutz (1979, 1980)
- **Numerical**: For SU(2) in d=4, the average plaquette ⟨P⟩ is a SMOOTH
  function of β. No discontinuity, no divergence of specific heat.
- **Conclusion**: No FIRST-ORDER phase transition for SU(2) d=4.
- The "crossover" near β ≈ 2.2 is a smooth crossover, not a true transition.

### Tomboulis-Yaffe (1982)
- Proved: for SU(N) in d=4, the Wilson action's free energy is analytic in
  a NEIGHBORHOOD of β = 0 (strong coupling) AND β = ∞ (weak coupling).
- The weak coupling result uses asymptotic freedom.
- **Gap**: The intermediate coupling region β ∈ (β₁, β₂) is not covered.

### Seiler (1982), "Gauge Theories as a Problem of Constructive QFT"
- Comprehensive treatment of lattice gauge theories
- Proved various analyticity results
- Established the framework for the no-phase-transition approach

### Key Open Question
Is f(β) analytic for ALL β > 0? This would close Gap A entirely.

## Approaches to Proving Analyticity

### Approach 1: Lee-Yang Type Theorem
The Lee-Yang theorem (1952) proves that the Ising model partition function
has no real zeros in the magnetic field h — all zeros are on the imaginary
axis. This implies analyticity of f(h) for real h > 0.

**For gauge theories**: Can we prove that Z(β) ≠ 0 for all real β > 0?
This is Z = ∫ ∏ dU exp(-β S_W), which is a sum of positive terms, so
Z > 0 trivially. But we need analyticity of f(β) = -(1/V) ln Z, which
requires that Z doesn't have zeros that APPROACH the real axis as V → ∞.

The Fisher zeros of Z(β) in the complex β plane: if they stay away from
the real axis, f(β) is analytic there. If they approach the real axis at
some β*, there's a phase transition.

**Route**: Prove that Fisher zeros of Z(β) for SU(2) d=4 stay at
distance ≥ δ > 0 from the real axis, uniformly in V. This implies
analyticity of f(β) and hence mass gap for all β.

### Approach 2: Dobrushin-Shlosman Uniqueness
For classical spin systems, Dobrushin-Shlosman (1985) proved uniqueness of
Gibbs measure (= analyticity) under a "complete analyticity" condition.

For gauge theories: the gauge invariance makes direct application tricky,
but the reduced theory (after gauge fixing) might satisfy the condition.

### Approach 3: Direct Cluster Expansion
Extend the Osterwalder-Seiler cluster expansion to all β.
At strong coupling, the expansion parameter is β (small → convergent).
At weak coupling, one could expand around the perturbative vacuum, with
expansion parameter g = √(2N/β) (small → convergent).

**The gap**: The intermediate coupling region where NEITHER expansion converges.
This is the "strong-weak coupling interpolation" problem.

### Approach 4: Correlation Inequality / Monotonicity
If we could prove Δ(β) is monotonically decreasing (as the numerics show),
combined with Δ(0) = ∞ and lim_{β→∞} Δ(β) > 0 (from asymptotic freedom +
dimensional transmutation), we'd have Δ(β) > 0 for all β.

But: we DON'T know lim_{β→∞} Δ(β) > 0 rigorously. That's Gap B (continuum limit).

### Approach 5: Convexity of Free Energy
The free energy f(β) = -(1/V) ln Z(β) = -⟨S_W⟩/V + ... 

Is f convex in β? If yes:
- f is differentiable except at countably many points
- At each differentiability point, f' = ⟨S_W⟩/V (specific heat is f'')
- Convexity doesn't directly rule out phase transitions (convex functions
  can have corners), but it constrains them to first-order type.

Actually, -f(β) = (1/V) ln Z(β) is a log-partition function, which is
CONVEX in β (standard result from convexity of log-sum-exp). So f(β)
is CONCAVE. This means f''(β) ≤ 0, i.e., the specific heat is bounded above.

But this doesn't rule out a first-order transition (discontinuity in f').

## Assessment

The most promising route for the theory track: **Approach 1 (Fisher zeros)**.
If we can bound the Fisher zeros of Z(β) away from the real axis, we get
analyticity and hence mass gap. This is a COMPLEX ANALYSIS argument, which
plays to formalization strengths.

The key question for the numerical track: compute the Fisher zeros of Z(β)
for small lattices (2⁴, 3⁴) and check if they approach the real axis.

## Result
Conditional theorem stated. Five approaches to proving analyticity identified.
Most promising: Fisher zeros of Z(β) bounded away from real axis.
Next: formalize the conditional theorem in Lean, survey Fisher zero literature.
