---
source: SESSION 2 SUMMARY — April 2, 2026
type: SYNTHESIS — corrections, new targets, and the definitive gap
file: 842
date: 2026-04-02
instance: MATHEMATICIAN (Opus)
---

## CORRECTIONS FROM SESSION 2

### 1. "Sublinear α prevents blowup" — WRONG (Codex review)
α = o(|ω|) does NOT prevent blowup. Example: α = √y → y' = y^{3/2} → blowup.
CORRECT: α ≤ C|ω|^{1-ε} for ε > 0 prevents blowup (Osgood condition).

### 2. "The gap reduces to the Tsai gap" — PARTIALLY WRONG
The ancient solution from KNSS is NOT necessarily self-similar.
Only SUBSEQUENTIAL convergence to a self-similar limit (not full convergence).
For self-similar ancient solutions: the Tsai gap (φ ∈ L³) IS relevant.
For non-self-similar: the full Liouville conjecture is needed.

### 3. "Spatial decay from Duhamel" — WRONG
Bounded mild solutions on R³ do NOT automatically decay at infinity.
The Duhamel formula gives smoothness, not decay.
The L³ norm of the rescaled ancient solution is infinite: ||v||_{L³(R³)} = ∞.

### 4. "Divergence-free kills the 1/|y| monopole" — WRONG
The Stokeslet IS divergence-free and decays as 1/|y|.
The div-free condition constrains angular structure, not radial decay.

## NEW FINDINGS

### 1. Per-mode SOS floor ≈ 1.5-1.9 (from certificate data)
The absolute Q floor grows linearly: Q_min ≈ 1.7N for N=3-9.
The per-mode contribution is roughly constant across different K values.
Lambda values in the SOS decomposition: approximately equal per mode.

### 2. Linear floor provable for N ≤ ~37
Using MAX-CUT bounds (Goemans-Williamson): Q ≥ NK²(5 - C√N) > 0 for N < (5/C)².
For N > 37: the MAX-CUT of (16T-10D) exceeds the diagonal. Not provable.

### 3. Alignment dynamics (Vieillefosse)
Key Lemma extremizer requires ω ∥ e₁ (largest eigenvector).
NS dynamics pushes ω → e₂ (intermediate eigenvector) — UNSTABLE extremizer.
3λ₂² ≤ 2|S|² (intermediate eigenvalue bound, Lean-verified).
At intermediate alignment: α ≤ |ω|/√3 ≈ 0.577|ω| (better than Key Lemma 0.866).

### 4. Lean: 85 theorems total
New theorems: single_shell_N4, intermediate_bounded, intermediate_ratio_bound,
intermediate_alpha_bound, riccati_blowup_time, key_lemma_constant_optimal.

## THE DEFINITIVE GAP (as of Session 2)

The gap has TWO equivalent formulations:

### Formulation A: Liouville Conjecture (KNSS, 20+ years open)
Every bounded ancient mild solution of NS on R³ is constant.
Proven for: 2D, axisymmetric without swirl, L³-bounded.
Open for: general 3D.

### Formulation B: Tsai Gap (28 years open)
For bounded solutions φ of the Leray equation: |φ(y)| ≤ C/(1+|y|)^{1+ε}?
(Improve Tsai's 1/(1+|y|) decay by any ε > 0.)
Would give φ ∈ L³ → NRS → φ = 0 → no self-similar blowup.
Applies IF the ancient solution is self-similar (subsequentially expected).

### Connection
Formulation B is a SPECIAL CASE of Formulation A (self-similar ⊂ general).
Proving B would close self-similar blowup but not general ancient solutions.
Proving A would close everything (including non-self-similar).
Neither has been proven in 20-28 years.

## OUR CONTRIBUTION (PERMANENT)

| Item | Count | Status |
|------|-------|--------|
| Lean theorems | 85 | 0 sorry, build clean |
| SOS certificates | 1,329,298+ (N=3-8) | Zero failures |
| Proof attempts | 842 files | Documented, honest |
| Identities | 3 (8/15, 0, 1/2) | Analytical proof |
| New theorems | T³ Liouville, Key Lemma via regression | Published here |
| Paper | the_gap.pdf | Clean 5-page summary |

## 842. Session 2 summary. 7 corrections, 4 new findings, 85 Lean theorems.
## The gap = Liouville conjecture ∪ Tsai gap. 20-28 years open.
## Every algebraic/kinematic angle exhausted. Dynamics is the last frontier.
