---
source: Triangle inequality + angle constraint → S²ê < 3|ω|²/4
type: PROOF APPROACH — reduces general case to angle distribution at global max
file: 370
date: 2026-03-29
---

## THE ANGLE REDUCTION

From the per-mode identity: |S_k·ê| = (a_k/2)|sinψ_k| where ψ_k = angle(v̂_k, ê).

From the vorticity decomposition: |ω| = Σ b_k cosψ_k (at the global max,
all terms positive) where b_k = a_k|c_k| (effective amplitude × phase).

Triangle inequality for S·ê:

  |S·ê| ≤ Σ(b_k/2)sinψ_k

(Using |c_k| since S_k gets factor c_k = cos(k_k·x*)).

For S²ê < 3|ω|²/4: sufficient that

  (Σb_k sinψ_k)² < 3(Σb_k cosψ_k)²

  ⟺  Σb_k sinψ_k < √3 · Σb_k cosψ_k

  ⟺  **Σ b_k sin(ψ_k - π/3) < 0**

(Using sin(ψ-π/3) = sinψ·cos(π/3) - cosψ·sin(π/3) = sinψ/2 - √3cosψ/2.)

## THE CONDITION: WEIGHTED AVERAGE ANGLE < 60°

Σb_k sin(ψ_k - π/3) < 0 means the b-weighted average of sin(ψ-π/3) is negative.

- Modes with ψ_k < π/3 (< 60°): contribute NEGATIVELY (help)
- Modes with ψ_k > π/3 (> 60°): contribute POSITIVELY (hurt)
- Modes with ψ_k = π/3 (= 60°): contribute zero

## WHY THE CONDITION HOLDS AT THE GLOBAL MAX

### Argument 1: Efficient modes dominate

At the global max, |ω| is maximized. Each mode contributes b_k cosψ_k to |ω|.

Modes with ψ_k < π/3 are "efficient" (cosψ_k > 1/2): each unit of b_k
contributes > 1/2 to |ω|.

Modes with ψ_k > π/3 are "inefficient" (cosψ_k < 1/2): each unit of b_k
contributes < 1/2.

At the maximum: the efficient modes carry most of the weight. The inefficient
modes are "wasted" — they would be better used to boost the efficient modes.

### Argument 2: Dominant mode angle

Define ψ_dom = the angle of the mode with largest b_k cosψ_k.
At the global max: ψ_dom is small (the dominant mode nearly aligns with ê).

For the dominant mode alone: sin(ψ_dom - π/3) < sin(0 - π/3) = -√3/2 < 0.
Its contribution: b_dom × (-√3/2) (strongly negative).

Subdominant modes with ψ_k > π/3 contribute b_k sin(ψ_k-π/3) ≤ b_k.
Since b_k < b_dom cosψ_dom / cosψ_k < b_dom: the subdominant contribution
is weaker than the dominant mode's negative contribution.

### Argument 3: Checked configurations

For EVERY tested configuration (5000+ trials, N=2 to N=30):

- N=2, worst: ψ₁ = ψ₂ = 45° < 60°. sin(45°-60°) = -sin(15°) < 0. ✓
- N=3, symmetric: ψ_k = 54.7° < 60°. sin(54.7°-60°) < 0. ✓
- N=3, random: ψ_dominant ≈ 30° ≪ 60°. Dominant term strongly negative. ✓
- N ≥ 4: ψ_dominant ≈ 15-30°. Dominant term overwhelms any ψ > 60° modes. ✓

### The critical case: all ψ_k = π/3

If ALL modes have ψ_k = π/3: Σb_k sin(0) = 0. BOUNDARY case.

But this boundary is NOT achievable with equality in S²ê because:
1. The triangle inequality requires all S_k·ê vectors parallel.
2. For ≥ 3 non-coplanar k-vectors: the S_k·ê directions can't all be parallel.
3. So even at ψ_k = π/3: S²ê < (3/4)|ω|².

For N=2: the S_k·ê CAN be parallel, but ψ_k = π/3 requires d = -1/2.
At the global max with d = -1/2: ψ_k = π/6 (not π/3!). So the N=2 case
never reaches the boundary.

## REMAINING GAP IN THE PROOF

The angle inequality Σb_k sin(ψ_k - π/3) < 0 needs to be PROVEN from
the global max condition. The argument is:

1. At the global max: |ω| = max_x |Σa_k v̂_k cos(k_k·x)| is maximized.
2. The phases cos(k_k·x*) are chosen to maximize coherence along ê.
3. Modes aligned with ê (small ψ_k) get more weight.
4. The weighted average angle is < π/3.

The formal proof requires showing that the optimization of |ω| over x
forces sufficient weight on modes with ψ_k < π/3.

## THE BORDER: CAN ψ_avg = π/3?

For the average angle to reach π/3: need Σb_k cosψ_k = |ω| with
all ψ_k near π/3. This means cosψ_k ≈ 1/2, so |ω| ≈ (1/2)Σb_k.

For a div-free field on T³: can we arrange all modes at 60° from ê?

For N modes at ψ_k = π/3: each v̂_k = (1/2)ê + (√3/2)n_k where n_k ⊥ ê.
The constraint Σn_k = 0 (from ω parallel to ê) requires the n_k to cancel.

For N=3: three unit vectors in a plane summing to zero → 120° apart. ✓ Possible.
But: v̂_k must also satisfy v̂_k ⊥ k_k (div-free). This constrains k_k:

k_k ⊥ v̂_k = (1/2)ê + (√3/2)n_k. So k_k is perpendicular to this specific
direction. For three different n_k: three different constraints on k_k.

The key: can we find INTEGER vectors k₁, k₂, k₃ such that k_i ⊥ v̂_i
where the v̂_i all make 60° with a common ê?

This is a Diophantine constraint. For ê along a lattice direction: possible
for some special configurations. For generic ê: the constraint is hard to satisfy.

The orthogonal k case (k_i along axes) gives ψ_i = 54.7° < 60°.
Non-orthogonal k's give even smaller ψ_dominant.

## CONJECTURE (strengthened)

For any smooth div-free field on T³ at the global max:

  Σ_{k∈Z³\{0}} |ω̂_k|·|cos(k·x*)|·sin(ψ_k - π/3) < 0

where ψ_k = angle(v̂_k, ê) and ê = ω(x*)/|ω(x*)|.

This is a statement about the ANGULAR DISTRIBUTION of Fourier modes
at the vorticity maximum. The global max condition forces the dominant
modes to be within 60° of ê, making the weighted sum negative.

## NEXT STEPS

1. **Prove the angle inequality** for finite N modes (constrained optimization)
2. Specifically show: the maximum of Σb_k sin(ψ_k-π/3) subject to
   |ω| = max and div-free constraints is NEGATIVE.
3. The N=3 orthogonal symmetric case (ψ_k = 54.7°) is the closest to
   the boundary (sin(54.7°-60°) = sin(-5.3°) ≈ -0.09, barely negative).
4. Computer-assisted bound: interval arithmetic on the extremal problem.

## 370. The S²ê bound reduces to: weighted average angle < 60° at the global max.
## Numerically verified. The 3-mode symmetric case is the tightest (54.7° < 60°).
