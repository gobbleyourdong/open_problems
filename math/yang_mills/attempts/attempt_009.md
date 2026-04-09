# Attempt 009 — Literature Integration: What Changed Everything

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Track**: theory (Theory)

## Three Game-Changing Findings

### 1. Adhikari-Butez-Chatterjee (2025): MASS GAP PROVED (in 't Hooft regime)
arXiv:2510.22788

**They proved mass gap for U(N) lattice gauge theory in the 't Hooft limit**
(N → ∞, β·N fixed). This is the FIRST mass gap result for a continuous gauge
group on the infinite lattice.

**What this means for us**: The 't Hooft limit is a specific scaling, not the
full finite-N result we need. But the METHODS they used may extend. This is
the closest anyone has come to Gap A.

### 2. Tomboulis (2007): Claimed Full Proof (Disputed)
arXiv:0707.2179

Tomboulis claimed: SU(2) in d ≤ 4 is confining for ALL 0 < g < ∞.
Method: RG decimation with potential-moving bounds.

Ito-Seiler (arXiv:0711.4930) found missing steps. Tomboulis responded
(arXiv:1210.1794). Community consensus: **unresolved gaps, not accepted**.

**What this means for us**: The approach (RG decimation bounds) is the right
idea. If we can identify and fix the specific gaps, this could work.

### 3. Lee-Yang Route is DEAD for Gauge Theories

The phase transition agent confirmed: there is NO known analog of the
Lee-Yang circle theorem for lattice gauge theories. The partition function
structure is fundamentally different from ferromagnets.

**My attempt_007/008 (Fisher zeros, spin foam positivity) was barking up
the wrong tree.** The character expansion does NOT preserve a zero-free
region because:
(a) 6j-symbols have mixed signs (I already found this in attempt_008)
(b) The gauge theory Z(β) is not a "multiaffine" function like the Ising Z(h)
(c) No one in 50 years has found a gauge Lee-Yang analog

**Kill this route. Redirect effort.**

## Revised Proof Landscape

### DEAD routes (from this tick):
- ❌ Fisher zeros / Lee-Yang analog (attempt_007-008) — no known structure
- ❌ Direct Balaban completion (attempt_005) — entropy obstruction too severe

### ALIVE routes (ranked by promise):

**1. Chatterjee Probabilistic Program** ★★★★★
The most active and productive rigorous program on lattice gauge theory.
Recent results:
- Mass gap in 't Hooft regime (2025) — BREAKTHROUGH
- Confinement from mass gap (2021)
- Random surfaces and lattice YM (2023)
- Expanded area law regimes (2025)
- SU(2) YM-Higgs scaling limit (2024)

**Strategy**: Extend the 't Hooft mass gap to finite N. The methods are
probabilistic (random surfaces, master loop equations, stochastic analysis).
This is the hottest area in rigorous gauge theory right now.

**2. Fix Tomboulis (2007)** ★★★★
The only serious attempt at "confinement for all couplings."
The RG decimation approach gives upper AND lower bounds on the partition
function. The gaps identified by Ito-Seiler need to be understood.

**Strategy**: Read Tomboulis 2007 + Ito-Seiler 2007 carefully. Identify
the exact step that fails. Can it be repaired?

**3. Interpolation (Strong-Weak)** ★★★
Analyticity at strong coupling (Osterwalder-Seiler) + analyticity at weak
coupling (Balaban-type) + convexity of pressure → could interpolate.

**Strategy**: The pressure p(β) is convex. If analytic on (0, β₁) and
(β₂, ∞) with β₁ > β₂, then analytic on (0, ∞). Need to push β₁ and β₂
to overlap.

**4. Tomboulis-Yaffe Inequalities** ★★★
Proved: boundary condition insensitivity ⟹ mass gap.
If we can prove BC insensitivity for all β, we get mass gap.

**Strategy**: Study the Tomboulis-Yaffe framework. What's needed to
prove BC insensitivity at intermediate coupling?

## The Revised Architecture

```
Mass gap for all β
    ↑
    ├── Route 1: Extend Chatterjee 't Hooft mass gap to finite N
    ├── Route 2: Fix Tomboulis RG decimation
    ├── Route 3: Strong-weak interpolation via convexity
    └── Route 4: Tomboulis-Yaffe BC insensitivity
```

All four routes avoid the Balaban infinite-composition problem and the
Lee-Yang dead end. They attack Gap A (lattice mass gap) directly.

Gap B (continuum limit) remains separate but is less urgent — if we get
Gap A, we have the lattice theory under control, and Gap B is "merely"
a renormalization problem.

## Key Structural Insights from the Literature

### Why SU(N) has no transition but U(1) does:
- U(1): π₁(U(1)) = Z → topological monopoles → monopole condensation
  drives the phase transition
- SU(N): π₁(SU(N)) = 0 → no stable monopoles → no condensation transition
- SO(3) = SU(2)/Z₂: HAS a phase transition → center symmetry matters
- d=5 SU(N): HAS a phase transition → asymptotic freedom matters (d=5 is non-renormalizable)

**The mass gap in SU(N) d=4 is protected by:**
1. Trivial fundamental group (no monopoles)
2. Non-trivial center Z(N) (center vortices confine smoothly)
3. Asymptotic freedom (UV completion exists, strong-weak connected)

### Chatterjee (2021): Mass Gap ⟹ Confinement
If we prove Δ(β) > 0 for all β, we automatically get confinement (area law).
The mass gap is the PRIMARY target — confinement follows.

## What the theory track Should Do Next

1. **Read arXiv:2510.22788** (Adhikari-Butez-Chatterjee 2025) in detail.
   Understand the 't Hooft mass gap proof. Identify what prevents extension
   to finite N.

2. **Read arXiv:0707.2179** (Tomboulis 2007) and **arXiv:0711.4930** (Ito-Seiler 2007).
   Identify the exact gap. Can it be fixed?

3. Formalize the convexity of pressure argument in Lean.

4. Study the Tomboulis-Yaffe framework for BC insensitivity.

## Result
Major route correction. Lee-Yang killed. Chatterjee program identified as
the most promising path. Tomboulis 2007 as the closest existing attempt.
Four viable routes remain, all avoiding the known dead ends.
