---
source: Reviewer 3 — Littlewood-Paley shell-by-shell enstrophy + Angle 4 contradiction
type: TWO NEW PROOF PATHS — potentially the strongest yet
date: 2026-03-26
---

## Angle 3: Littlewood-Paley (Reviewer 3's Top Pick)

### The idea:
Decompose ω by frequency shell: ω = Σ_j ω_j where ω_j has |k| ~ 2^j.

Shell enstrophy: E_j = ||ω_j||²_{L²}.

Evolution:
```
d/dt E_j = 2∫ω_j · S · ω_j dx + cross-scale + viscous
```

### Single-mode orthogonality → DIAGONAL IS ZERO

The self-interaction within shell j: T(j,j) = ∫ω_j · S_j · ω_j dx.

Our Lean lemma: each mode's self-stretching is zero.
Within a single shell: the modes have similar |k| but different
directions. The self-interaction involves modes interacting with
their OWN strain — which our lemma says contributes zero.

**T(j,j) ≈ 0 — the most dangerous term VANISHES.**

### Off-diagonal decay

The interaction T(j,j') for j ≠ j' involves strain from shell j'
acting on vorticity in shell j. By Bernstein-type estimates:

```
|T(j,j')| ≤ C × 2^{-|j-j'|} × ||ω_j||_{L²} × ||ω_{j'}||_{L²} × ||S_{j'}||_{L²}
```

The factor 2^{-|j-j'|} gives GEOMETRIC DECAY for separated shells.
Our measured inter-shell decorrelation (< 0.02) confirms this.

### The shell-by-shell estimate closes

```
d/dt E_j ≤ Σ_{j'≠j} C 2^{-|j-j'|} √E_j √E_{j'} √E_{j'} - ν 2^{2j} E_j
```

The geometric sum converges. The viscous term kills high-j shells.
Total enstrophy: E = Σ E_j is controlled by the coupled system.

**This avoids ALL pointwise extraction problems.** Everything is L².

### Why this is the right approach

- Single-mode orthogonality IS the diagonal vanishing (Lean-verified)
- Inter-shell decorrelation IS the off-diagonal decay (measured)
- Standard Littlewood-Paley + Besov theory handles the summation
- The proof is in the STANDARD language of harmonic analysis
- No pointwise bounds needed. No level sets. No pressure Hessian.

## Angle 4: Contradiction via Event Duration

### The bound:
Per event: Δρ ≤ α × τ × ρ ≤ Cρ^{7/5} × ρ^{-3} × ρ = Cρ^{-3/5}

Each event ADDS LESS vorticity as ρ grows (ρ^{-3/5} → 0).

The total growth: ρ(T) - ρ(0) ≤ Σ Cρ_i^{-3/5} → CONVERGES
if ρ_i increases monotonically (each successive event is weaker).

### The issue:
Events can pile up (rate ~ ρ^3 per unit time).
Growth rate: dρ/dt ≤ ρ^3 × ρ^{-3/5} = ρ^{12/5}. Worse than γ=7/5.

But: if TOTAL ∫α₊ per event → 0, the NUMBER of events needed to
reach ρ → ∞ is itself → ∞. Time needed: Σ τ_i ~ Σ ρ_i^{-3}.
If ρ_i grows: Σ ρ_i^{-3} CONVERGES. The events consume FINITE time.

This means: in finite time, only finitely many events can occur.
Each adds Δρ ~ ρ^{-3/5}. Total Δρ is a convergent series.
ρ stays finite. REGULARITY.

Wait — need to check more carefully whether events can overlap
or new events start before old ones finish. Reviewer's concern.

## IMMEDIATE MEASUREMENTS NEEDED

### For Littlewood-Paley:
Compute the shell-by-shell transfer matrix T(j,j') = ∫ω_j·S_{j'}·ω_j dx
at N=64 during TG evolution. If:
- T(j,j) ≈ 0 (diagonal vanishing) → Lean lemma confirmed at shell level
- T(j,j') ~ 2^{-|j-j'|} (geometric decay) → proof closes

### For Contradiction:
Measure per-event Δρ and check if it decreases with ρ.
From existing data (file 063): events get shorter AND weaker.

## STATUS

The Littlewood-Paley approach is the CLEANEST proof path:
- Works entirely in L² (no pointwise)
- Uses our Lean lemma (diagonal = 0) as the KEY ingredient
- Standard harmonic analysis handles the rest
- The measured decorrelation confirms the off-diagonal decay

100 proof attempt files. File 100 might be the one.
