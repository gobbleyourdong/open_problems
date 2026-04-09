---
source: DIRECT R BOUND — combine self-vanishing + phase mismatch → R < 1/2 directly
type: PROOF ATTEMPT — bypass the Key Lemma entirely
file: 446
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE SHORTCUT

The barrier framework needs R = α/|ω| < 1/2 at the vorticity max.
The Key Lemma proves this via S²ê < 3|ω|²/4 → DR/Dt < 0 at R=1/2.

But there's a DIRECT route: prove α < |ω|/2 at the max.

## THE CHAIN

### Step 1: Self-vanishing (proven, 500s file 518)
    |S_k · ê|² = (a_k²/4) sin²γ_k

### Step 2: Sine-cosine decoupling (proven)
    S(x) = Σ S_k sin(k·x), ω(x) = Σ a_k v̂_k cos(k·x)

### Step 3: Stretching rate bound
    α = ê·S·ê = Σ (ê·S_k·ê) sin(k·x*)
    |α| ≤ Σ |S_k·ê| |sin(k·x*)|
    ≤ Σ (a_k/2) sinγ_k |sin(k·x*)|     [by self-vanishing]
    = budget

### Step 4: Vorticity magnitude
    |ω| = Σ a_k cosγ_k cos(k·x*)         [projection onto ê]

### Step 5: Need budget < |ω|/2
    Σ (a_k/2) sinγ_k |q_k| < (1/2) Σ a_k c_k cosγ_k
    ⟺ Σ a_k sinγ_k |q_k| < Σ a_k c_k cosγ_k = |ω|

**This is WEAKER than the Key Lemma** (which needs budget < √(3/4)|ω| ≈ 0.866|ω|).
We only need budget < |ω| (the "half-barrier" condition).

## THE PER-MODE ANALYSIS

For each mode: define the "excess"
    e_k = sinγ_k |q_k| - |c_k| cosγ_k

If e_k < 0 for all k: the bound holds trivially (each mode contributes
more to |ω| than to the budget).

**When is e_k < 0?**
Using q² + c² = 1: sinγ√(1-c²) < |c|cosγ ⟺ sin²γ(1-c²) < c²cos²γ ⟺ sin²γ < c².

**e_k < 0 iff sinγ_k < |c_k|** (alignment better than phase offset).

For DOMINANT modes (γ_k ≈ 0, |c_k| ≈ 1): sinγ ≈ 0 ≪ 1 ≈ |c|. ✓ (massive margin)
For PERPENDICULAR modes (γ_k ≈ π/2): sinγ ≈ 1. Need |c_k| > 1. IMPOSSIBLE.

So: perpendicular modes ALWAYS have e_k > 0.

## THE PERPENDICULAR MODE PROBLEM

Modes with v̂_k ⊥ ê (cosγ = 0, sinγ = 1):
- Contribute ZERO to |ω| (since cosγ = 0)
- Contribute a_k|q_k|/2 to the budget

These modes ADD to the budget without helping |ω|.

**Critical question**: can the total perpendicular budget exceed |ω|/2?

Perpendicular budget: B_⊥ = Σ_{⊥ modes} (a_k/2)|q_k| ≤ Σ_{⊥ modes} a_k/2.

Aligned |ω|: |ω| = Σ_{aligned} a_k |c_k| cosγ_k ≥ (sum of dominant modes).

For B_⊥ < |ω|/2: need the aligned modes to carry 2× the perpendicular energy.

## THE CONSTRAINT FROM THE VORTICITY MAX

At the max of |ω|²: the perpendicular modes contribute to |ω_⊥| = 0 (perpendicular
cancellation: Σ a_k c_k sinγ_k ê_k^⊥ = 0).

This means: the perpendicular mode amplitudes are CONSTRAINED. Their contributions
must CANCEL in the perpendicular direction. This limits the total perpendicular energy.

Specifically: |Σ a_k c_k (v̂_k - cosγ_k ê)|² = 0 (since ω_⊥ = 0).

Expanding: Σ a_k² c_k² sin²γ_k + cross terms = 0.

Wait, this isn't exactly zero. Let me reconsider.

ω = |ω| ê. So ω_⊥ = ω - |ω|ê = 0. But:
ω = Σ a_k v̂_k c_k = Σ a_k c_k (cosγ_k ê + sinγ_k ê_k^⊥)

Taking the component ⊥ ê: Σ a_k c_k sinγ_k ê_k^⊥ = 0.

This doesn't mean each term is zero — the perpendicular components cancel vectorially.

But: the BUDGET counts |q_k| sinγ_k, which involves DIFFERENT weights (q instead of c).

## THE CRITICAL POINT CONSTRAINT (from 500s file 514)

At the max: Σ a_k cosγ_k q_k k_k = 0.

For modes with cosγ_k ≈ 0 (perpendicular): their contribution a_k × 0 × q_k × k = 0.
So perpendicular modes don't contribute to the critical point equation!

This means: the perpendicular modes' sines q_k are UNCONSTRAINED by the max condition.
They can have any q_k value, adding freely to the budget.

BUT: their amplitude a_k is constrained by the field's energy.

## THE ENERGY CONSTRAINT

Total mode energy: E = Σ a_k²/2.
At the max: |ω|² ≤ (Σ a_k)² ≤ N × 2E (Cauchy-Schwarz).

Perpendicular budget: B_⊥ ≤ Σ_⊥ a_k/2 ≤ √(N_⊥) × √(E_⊥) [CS].

For B_⊥ < |ω|/2: need √(N_⊥ E_⊥) < |ω|/2.

If the aligned modes dominate energy: E_⊥ ≪ E. And |ω|² ≈ E_aligned.
Then: √(N_⊥ E_⊥) < √(E)/2 iff N_⊥ E_⊥ < E/4 iff E_⊥ < E/(4N_⊥).

For N_⊥ = 1: need E_⊥ < E/4 (perpendicular mode < 25% of energy). Plausible.
For N_⊥ = N-3: need E_⊥ < E/(4(N-3)). Harder for large N.

## THE SMOOTH FIELD ARGUMENT

For smooth fields: a_k ~ |k|^{-s} for s > 5/2 (Sobolev embedding on T³).

The LOWEST 3 modes have the largest amplitudes. From the N ≤ 3 theorem:
these 3 modes give S = 0 at the max (sin = 0 for all 3).

The 4th mode onwards contributes to the budget:
B_tail ≤ Σ_{k ≥ 4} (a_k/2) ≤ Σ_{k ≥ 4} a_k/2

For Sobolev decay: Σ_{k ≥ 4} a_k ≤ C × K_4^{-s+3/2} (using Cauchy-Schwarz + Weyl law).

And |ω| ≥ a_1 - Σ_{k ≥ 2} a_k ≈ a_1 (dominant mode).

So: B_tail/|ω| ≈ (Σ_{k ≥ 4} a_k)/(2a_1) → 0 as the spectrum steepens.

**For any smooth field: budget/|ω| → 0 as the Sobolev index s → ∞.**

For finite s > 5/2: the ratio is bounded by a function of s and the
spectral gap a_1/a_4.

## THE GAP (STILL)

The argument requires: the first 3 modes have independent k-vectors
AND dominate the energy (a_4 ≪ a_1).

For fields where all modes have EQUAL amplitude: a_1 = a_4. The tail
is not small. The N ≤ 3 theorem doesn't help.

But: equal-amplitude fields on T³ are NOT smooth (their Sobolev norm
diverges). So they don't arise as NS solutions.

For NS solutions near a potential blowup: the vorticity concentrates
at small scales (high k). The amplitudes grow at high k, violating
the smooth-field assumption.

This is the BOOTSTRAP problem (file 417): near blowup, the field is
NOT smooth, and the Sobolev decay fails.

## NUMERICAL DATA (from 500s instance)

| Metric | Worst observed | Threshold | Margin |
|--------|---------------|-----------|--------|
| budget/|ω| | 0.489 | 1.000 | 51.1% |
| budget/|ω| | 0.489 | 0.500 (for R<1/2) | 2.2% |
| S²ê/|ω|² | 0.091 | 0.750 | 87.9% |

The 2.2% margin for R < 1/2 is TIGHT. The 87.9% margin for the Key Lemma is HUGE.

## 446. Direct R bound: α ≤ budget ≤ Σ(a/2)sinγ|q|.
## For R < 1/2: need budget < |ω|/2 (margin 2.2%, too tight to prove).
## For Key Lemma: need budget < √(3/4)|ω| (margin 43%, more room).
## Perpendicular modes are the obstruction. Their energy must be bounded.
## For smooth fields: tail decays. But bootstrap fails near blowup.
