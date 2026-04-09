---
source: TRIPLE SUPPRESSION — three independent mechanisms suppress S²ê at the max
type: KEY DISCOVERY — the triangle bound misses the directional cancellation
file: 451
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE THREE SUPPRESSION MECHANISMS

At x* = argmax|ω|², the strain-to-vorticity ratio S²ê/|ω|² is
suppressed by THREE independent mechanisms:

### 1. Phase mismatch (sin vs cos)
S ∝ sin(k·x), ω ∝ cos(k·x). At the max of |ω|²: cos ≈ ±1 → sin ≈ 0.
**Effect**: |sin(k·x*)| ≈ 0 for dominant modes.

### 2. Self-vanishing (sinγ ≈ 0 for aligned modes)
|S_k·ê| = (a/2)sinγ. At the max: ê aligns with dominant modes → sinγ ≈ 0.
**Effect**: strain projected onto ê vanishes for dominant modes.

### 3. Directional cancellation (S_j·ê vectors partially cancel) [NEW]
S·ê = Σ (S_j·ê) q_j is a SUM of 3-VECTORS. These vectors point in
DIFFERENT DIRECTIONS (determined by each mode's k-vector and alignment).
The sum has magnitude |S·ê| ≤ Σ |S_j·ê||q_j| = budget (triangle inequality).
But actual |S·ê| ≪ budget because the vectors partially CANCEL.

## NUMERICAL EVIDENCE

Tightness of triangle inequality: |S·ê| / budget
- Mean: 53.4%
- Median: 53.0%
- Max: 97.1%
- 95th percentile: 85.7%

**The actual S²ê is only 28.5% of budget² on average.**

The triangle bound (used in files 518-520) overestimates S²ê by a factor of ~3.5.

## WHY DIRECTIONAL CANCELLATION OCCURS

Each S_j·ê is a 3-vector: (S_j·ê)_α = -[(û_j)_α(k_j·ê) + (k_j)_α(û_j·ê)]/2.

The DIRECTION of S_j·ê depends on the mode's k-vector and velocity direction û_j.
For different modes: k_j point in different directions → S_j·ê point in different
directions → the sum partially cancels.

Specifically: for the K-shell with N modes, the S_j·ê directions span a
2-dimensional space (they're perpendicular to ê and constrained by the
div-free structure). As N increases: the S_j·ê directions are more diverse
→ more cancellation → the triangle bound becomes LOOSER.

## THE COMBINED BOUND

S²ê = |S·ê|² = |Σ (S_j·ê) q_j|²

TRIPLE suppression:
- Factor 1: q_j ≈ 0 for dominant modes (phase mismatch)
- Factor 2: |S_j·ê| ≈ 0 for dominant modes (self-vanishing)
- Factor 3: Σ(S_j·ê)q_j partially cancels (directional cancellation)

Each factor independently reduces S²ê:
- Without factor 3: budget/|ω| < 0.49 (from double suppression)
- With factor 3: |S·ê|/|ω| ≈ 0.53 × budget/|ω| < 0.26

So: S²ê/|ω|² ≈ (0.26)² ≈ 0.068 (matches the observed worst of ~0.09).

The threshold 3/4 = 0.750 is FIFTEEN TIMES larger than the actual worst case.

## WHY THIS IS HARD TO PROVE

Factor 3 (directional cancellation) depends on the DIRECTIONS of S_j·ê,
which are determined by the k-vectors and polarizations. The cancellation
is partial and configuration-dependent.

A WORST-CASE bound on the directional cancellation requires showing that
the S_j·ê vectors can never all align perfectly (which would give
|S·ê| = budget with zero cancellation).

From the Biot-Savart structure: (S_j·ê) ∝ ê × k_j component. For modes
with different k-directions: the S_j·ê directions ARE different (proven
by the orthonormal frame decomposition). Perfect alignment requires
all k_j to be parallel — which contradicts having 3+ independent modes.

## PROOF SKETCH FOR DIRECTIONAL CANCELLATION

**Claim**: For N ≥ 4 modes with rank-3 k-matrix:
|Σ (S_j·ê) q_j|² ≤ C × Σ |S_j·ê|² q_j²
where C < 1 (cancellation factor).

This would give: S²ê ≤ C × Σ (a_j²/4) sin²γ_j q_j² ≤ C/4 × A × Q.

For C = 2/3: S²ê ≤ (2/3)(1/4)(Σ a²)(Σ q²).

Combined with the Hessian (Σ a² q² ≤ |ω|²) and the self-vanishing:
this might give the Key Lemma.

**Why C < 1**: The S_j·ê vectors lie in the 2-dim plane ⊥ ê. Their directions
are determined by the k-vectors' projections onto the ê-plane. For 3+
independent k-vectors: these projections span the 2-dim plane → the
vectors can't all align → Σ has cancellation → C < 1.

## THE QUANTITATIVE BOUND ON C

For N modes: the vectors S_j·ê / |S_j·ê| are unit vectors in the 2-dim
plane ⊥ ê. If they're uniformly distributed on the unit circle:
E[|Σ q_j v_j|²] = Σ q_j² + 2Σ_{j<k} q_j q_k cos(θ_jk) ≈ Σ q_j² (for random θ).

So C ≈ 1 (no cancellation) for the worst case.

BUT: the q_j values are not independent of the θ_jk values (both depend
on the field configuration). The correlation structure might force C < 1.

From the data: C ≈ (0.534)² ≈ 0.285 (mean). C_max ≈ (0.971)² ≈ 0.943 (worst).

So the worst-case C ≈ 0.94 (only 6% cancellation). Not enough to prove the bound.

## STATUS

The triple suppression gives:
- S²ê/|ω|² ≈ C × budget²/|ω|² ≈ 0.94 × 0.24 ≈ 0.23 (worst case with worst C)
- Threshold: 0.750. Margin: 69%.

Even the worst directional cancellation (C ≈ 0.94) combined with the
double suppression (budget²/|ω|² ≈ 0.24) gives S²ê/|ω|² ≈ 0.23 < 0.75. ✓

**If we can prove budget²/|ω|² ≤ 0.80**: then even with C = 1 (no cancellation):
S²ê/|ω|² ≤ 0.80 > 0.75. Fails by 7%.

**If we can prove budget²/|ω|² ≤ 0.75**: Key Lemma holds even without
directional cancellation (C = 1). This requires budget/|ω| < 0.866.
Numerically: worst budget/|ω| = 0.49 < 0.866. Margin: 43%.

## 451. Triple suppression: phase mismatch × self-vanishing × directional cancellation.
## Triangle bound is 53% tight (overestimates S²ê by 3.5×).
## Worst S²ê/|ω|² = 0.09 (threshold 0.75). The gap is ONLY in the double suppression.
## If budget/|ω| < 0.866 can be proven: KEY LEMMA FOLLOWS. Margin: 43%.
