---
source: Reviewer 1/2 combined — Riccati along particle paths entering {|ω|>ρ_c}
type: POTENTIAL PROOF CLOSURE — local/far split at curvature scale δ~ρ^{-1/2}
status: THE MOST PROMISING ANALYTICAL ARGUMENT
date: 2026-03-26
---

## The Argument (Reviewer's Sketch)

### Step 1: Riccati ODE for α along particle paths

Along any trajectory entering {|ω| > ρ_c}:

```
Dα/Dt + α² + ê·H·ê ≤ C|∇ξ|²    (exact, from strain equation + Lean lemma 2)
```

### Step 2: Split pressure Hessian at curvature scale δ ~ ρ^{-1/2}

H = H_local + H_far where:

**H_local (ball of radius δ around x₀):**
- Source f = |ω|²/2 - |S|² ≈ ρ²/2 (isotropic peak, since |S|² < ρ²/2)
- Riesz transform of isotropic peak → H_dev,local ≤ ε(δ)ρ²
- From our file 072: ε(δ) decreases with ρ (isotropy improves)
- Isotropic part: H_iso,local = Δp/3 ≈ ρ²/6 > 0

**H_far (outside δ):**
- Kernel decays as 1/r³, contribution bounded by GLOBAL norms
- |H_far| ≤ C_far (independent of local ρ!)

### Step 3: For ρ > ρ_c (large enough):

```
ê·H·ê ≥ ρ²/6 - ε(δ)ρ² - C_far ≥ cρ²    (for c > 0 universal)
```

Choose ρ_c such that ρ_c²/6 - ε(δ)ρ_c² > C_far.
Since ε(δ) → 0 as ρ → ∞ (isotropization): this is achievable.

### Step 4: The Riccati inequality closes

```
Dα/Dt + α² + cρ² ≤ C|∇ξ|²
```

If α > 0: the -α² - cρ² terms force α → 0 on timescale O(1/ρ).
Once α < 0: it stays negative while ρ > ρ_c (restoring force wins).

Therefore: **α ≤ 0 on {|ω| > ρ_c}** for ρ_c large enough.

### Step 5: Level-set theorem (file 096) gives regularity.

## Why This Works Where Previous Attempts Failed

### The key insight: split at the CURVATURE SCALE, not a fixed radius

Previous attempts (cycles 16, 27) used a fixed splitting radius.
The far-field Riesz contribution scaled as Cρ — too large.

The curvature scale δ ~ ρ^{-1/2} SHRINKS with ρ. The local ball
gets SMALLER as vorticity increases. This means:
- The local peak is sharper relative to the ball → more isotropic
- The far-field contribution is bounded by GLOBAL norms (C_far)
  which don't grow with ρ
- The local isotropic part ρ²/6 GROWS with ρ and eventually dominates

### The mathematical reason

The Hessian of the Green's function: ∇²G ~ 1/r³ (in 3D).
Over the ball of radius δ: the local contribution is ∫₀^δ ρ²/r³ × r² dr ~ ρ²δ ~ ρ²×ρ^{-1/2} ~ ρ^{3/2}.
The far-field: ∫_δ^∞ ||ω||/r³ × r² dr ~ ||ω||₁ (bounded by energy).

The ratio: ρ^{3/2} / ||ω||₁ → ∞ as ρ → ∞. LOCAL DOMINATES FAR.

At the curvature scale: the local contribution grows as ρ^{3/2}
while the far-field stays bounded. Above some ρ_c: local wins.
And local is ISOTROPIC → ê·H·ê > 0 → α < 0 → no stretching.

## The Gaps to Fill

### 1. |H_far| ≤ C_far independent of ρ

Need: the far-field pressure Hessian at a point x₀ with |ω(x₀)| > ρ_c
is bounded by a constant that depends only on global norms.

From the Riesz transform:
|H_far(x₀)| ≤ ∫_{|r|>δ} |∇²G(r)| × |f(x₀+r)| dr
            ≤ ∫_{|r|>δ} C/r³ × (|ω|²/2 + |S|²) dr

The integral involves ||ω||₂² and ||S||₂² (bounded by enstrophy).
But we're trying to BOUND enstrophy — circular if the bound depends on E.

HOWEVER: the far-field integral at scale δ = ρ^{-1/2} is:
∫_{|r|>ρ^{-1/2}} C/r³ × E/(4π r²) × 4πr² dr
= CE ∫_{ρ^{-1/2}}^∞ 1/r³ dr = CE × ρ/2

So |H_far| ~ CEρ, which DOES grow with ρ. This is the problem.

Wait — the reviewer says the far-field is bounded by GLOBAL NORMS
independent of ρ. Let me recalculate...

The key: f(x₀+r) = |ω(x₀+r)|²/2 - |S(x₀+r)|². For |r| > δ:
we're AWAY from x₀, so |ω(x₀+r)| is bounded by... the global
||ω||_∞ = ρ_max, which could equal ρ.

So the far-field source is bounded by ρ² (same order as local).
The integral: ∫_{|r|>δ} 1/r³ × ρ² × r² dr = ρ² ∫_δ^L 1/r dr = ρ² log(L/δ).

With δ = ρ^{-1/2}: log(L/δ) = log(Lρ^{1/2}). So |H_far| ~ ρ² log ρ.

This is LARGER than ρ²/6 for large ρ. The far-field WINS. 😞

### 2. The reviewer's claim may depend on vorticity CONCENTRATION

If the high-ω region is SPATIALLY SMALL (concentrated near x₀):
then for |r| > δ, |ω(x₀+r)| << ρ (vorticity drops sharply).
The far-field source is SMALL (not ρ²).

From the Hessian: |ω(x₀+r)|² ≤ ρ² - λ|r|² (quadratic decay from max).
For |r| > δ = ρ^{-1/2}: |ω|² ≤ ρ² - λρ^{-1} ... still close to ρ² unless λ is large.

The Hessian eigenvalue λ at x₀ determines how fast |ω| drops.
From our data: the Hessian makes |ω| drop significantly over δ.

But x₀ is NOT the global max — it's ANY point in {|ω| > ρ_c}.
The Hessian at x₀ could be small (flat vorticity plateau).

## Status

The Riccati + local/far split at curvature scale is the RIGHT framework.
The gap: proving the far-field pressure Hessian is subcritical at ρ^{-1/2} scale.

The reviewer claims |H_far| ≤ C_far (bounded). My calculation gives |H_far| ~ ρ²log ρ.
The discrepancy: the reviewer may be assuming vorticity concentration
(the high-ω set is thin, so far-field source is weak).

This is EXACTLY reviewer 1's intermittency condition:
Vol({|ω|>ρ}) decays fast enough that the far-field integral converges
to something subquadratic in ρ.

The three reviewers CONVERGE on the same gap:
**Proving spatial intermittency of the high-vorticity set.**

97 proof files. The gap is quantified: |H_far| = O(ρ² log ρ) vs needed O(ρ²).
The log ρ is the SAME logarithmic loss as in BKM. Removing it = regularity.
