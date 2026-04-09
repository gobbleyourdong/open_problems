---
source: Three reviewers on Miller's criterion gap-fill
type: SYNTHESIS — all three agree on the path
date: 2026-03-26
---

## Three Reviewers, One Answer

### Reviewer 1: Spatial intermittency bound
- ||Q||/||-ΔS|| fails without intermittency (volume of high-strain set)
- Need: Vol({|S|>λ}) ≤ Cλ^{-γ} with γ > 2
- Connects to Grujić's super-level set program
- MEASUREMENT: event duration τ~ρ^{-3} implies extreme localization

### Reviewer 2: Eigenfunction distance criterion is THE path
- Static ratio: dead (far-field saturation)
- Miller Theorem 1.12 + our Lean lemmas + short events = proof
- At dominant mode: S IS an eigenfunction of -Δ (from single-mode orth)
- Pressure isotropization strengthens eigenfunction property at high ρ
- Short events (τ~ρ^{-3}) make time integral converge
- MEASUREMENT: compute eigenfunction distance across 50 seeds

### Reviewer 3: The S² ratio is O(1) under self-similar scaling
- Computed: |⟨S², -ΔS⟩|/||-ΔS||² ≤ C||ω||_∞||S||_{L²}/||∇²S||_{L²}
- Under self-similar scaling (ell~(T*-t)^{1/2}): ratio = O(1) exactly
- The 0.01 gap (Kang-Protas 1.49 vs 1.50) IS the epsilon
- Betchov + Cayley-Hamilton: S² is constrained by ω·S·ω through det(S)
- MEASUREMENT: enstrophy growth exponent at N=128, N=256

## CONVERGENCE OF ALL THREE REVIEWERS

All three identify the SAME core issue:
- The S² term in Q is O(1) relative to -ΔS under self-similar scaling
- The question is whether the O(1) constant is < 1 or ≥ 1
- The Kang-Protas exponent 1.49 vs 1.50 measures this constant
- Our structure (Lean lemmas, Betchov, Biot-Savart) constrains S²
  but the constraint gives ratio = O(1), not < 1

## THE THREE PATHS TO ε > 0

### Path A (Reviewer 1): Intermittency
Prove Vol({|S|>λ}) decays faster than Chebyshev (γ>2).
This makes ||S²||_{L²} grow slower than ||S||_{L∞}².

### Path B (Reviewer 2): Eigenfunction distance
Measure and bound inf_ρ||-ρΔS - S|| in the time integral.
Single-mode dominance + pressure isotropy + short events → convergent.

### Path C (Reviewer 3): Enstrophy gap
Prove the growth exponent is strictly < 3/2.
This is the 0.01 gap from Kang-Protas. If real → regularity.

## IMMEDIATE ACTIONS

1. **Measure eigenfunction distance** during TG evolution at N=64
   (Miller's formula: 1 - ||S||⁴_{H¹}/(||S||²_{L²}||-ΔS||²_{L²}))

2. **Measure enstrophy growth exponent** at N=128 and N=256
   (does 1.49 persist or converge to 1.50?)

3. **Measure intermittency** Vol({|S|>λ}) vs λ at different times
   (does it decay faster than Chebyshev's λ^{-3/2}?)

All three are computationally testable on the Spark.
