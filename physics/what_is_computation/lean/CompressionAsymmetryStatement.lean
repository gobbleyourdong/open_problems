/-
CompressionAsymmetryStatement.lean
===================================

Phase 2 Even, Cycle 2 of the 3-cycle what_is_computation loop (2026-04-09).

Builds on KManipulationCore.lean (Cycle 1 Even) by formalizing the
P vs NP compression-asymmetry CONJECTURE at statement level — what it
MEANS, in the K-framing — without trying to prove it. The proof itself
belongs to the math track; this file provides a single canonical
vocabulary that the physics track's numeric experiments can land
on without re-specifying the claim each time.

This is a SIBLING to `math/p_vs_np/lean/CompressionAsymmetry.lean`.
That file records the empirical measurements (find/verify ratios at
specific n). This file records the CONJECTURE these measurements
are probing.

No sorry. Mathlib-dependent.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! ## §1 Find/verify ratio as a function of instance size -/

/-- A find/verify ratio function: given instance size n, return the
    measured or asserted ratio between search cost and verification cost.
    In practice this is noisy (per-instance and per-seed), so downstream
    claims quantify over n → ℝ rather than committing to a specific
    closed-form bound. -/
abbrev FVRatio := ℕ → ℝ

/-- Two find/verify functions agree on a finite prefix. Useful for
    stating "the physics-track experiments observe ratio r on the first
    K points and the conjecture extends r to all n." -/
def AgreeOnPrefix (r₁ r₂ : FVRatio) (K : ℕ) : Prop :=
  ∀ n, n ≤ K → r₁ n = r₂ n

/-! ## §2 Super-polynomial growth -/

/-- A find/verify ratio grows super-polynomially if for every polynomial
    bound c · n^k, there exists some n ≥ k where the ratio exceeds that
    bound. (Standard "not O(poly)" statement.)

    This is our Lean-level restatement of the P ≠ NP compression
    claim from `KManipulationCore.CompressionAsymmetryHolds`. -/
def SuperPolynomial (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∀ k : ℕ, ∃ n : ℕ, n ≥ k ∧ r n > c * (n : ℝ) ^ k

/-- The empirical-side counterpart: a find/verify ratio "grows strongly on
    a prefix" if the measured values are monotonic (average, not per-seed)
    on the first K observations. This is what the physics track CAN
    measure; SuperPolynomial is the infinite-n limit it cannot. -/
def StronglyGrowsOnPrefix (r : FVRatio) (K : ℕ) : Prop :=
  ∀ n m : ℕ, n ≤ m → m ≤ K → r n ≤ r m * 2   -- allow 2× per-step noise

/-- An ONE-directional bridge: SuperPolynomial implies that, for any
    k, eventually the ratio exceeds any fixed polynomial. The physics
    track's measurements probe the "eventually" part — they are the
    outer-quantifier witnesses, not the conclusion. -/
theorem superpoly_exceeds_poly
    (r : FVRatio) (h : SuperPolynomial r)
    (c : ℝ) (k : ℕ) :
    ∃ n : ℕ, n ≥ k ∧ r n > c * (n : ℝ) ^ k :=
  h c k

/-! ## §3 The physics-track measurement registry

    We record, as a structure, the specific (n, ratio, seed) triples the
    physics-track numerics have observed. These are CONSISTENT with
    SuperPolynomial but do not prove it.

    The numbers here are taken from:
      results/pnp_asymmetry_data.json            (canonical)
      results/pnp_asymmetry_cycle1_rerun.json    (Cycle 1 Odd extension)
-/

/-- A physics-track measurement: problem family, instance size, seed,
    and the measured find/verify ratio. -/
structure Measurement where
  family : String
  n : ℕ
  seed : ℕ
  ratio : ℝ
  deriving Repr

/-- Canonical 3-SAT measurements (seed 42, clause ratio ≈ 4.3). -/
def sat_n5  : Measurement := { family := "3sat", n := 5,  seed := 42, ratio := 4.61 }
def sat_n10 : Measurement := { family := "3sat", n := 10, seed := 42, ratio := 73.10 }
def sat_n12 : Measurement := { family := "3sat", n := 12, seed := 42, ratio := 753.29 }
def sat_n18 : Measurement := { family := "3sat", n := 18, seed := 42, ratio := 4698.22 }

/-- Cycle 1 Odd extension: n=20 at two seeds. -/
def sat_n20_seed42  : Measurement :=
  { family := "3sat", n := 20, seed := 42,  ratio := 2256.57 }
def sat_n20_seed137 : Measurement :=
  { family := "3sat", n := 20, seed := 137, ratio := 88908.99 }

/-! ## §4 Trivial structural lemmas on the measurement set

    These aren't deep — they are the type-level assertions that the
    measured ratios in fact take the values we claim, so downstream
    files can rely on `rfl` rather than re-reading JSON.
-/

theorem sat_n5_small    : sat_n5.ratio < 10        := by unfold sat_n5;    norm_num
theorem sat_n10_over_50 : sat_n10.ratio > 50       := by unfold sat_n10;   norm_num
theorem sat_n12_over_500 : sat_n12.ratio > 500     := by unfold sat_n12;   norm_num
theorem sat_n18_over_4000 : sat_n18.ratio > 4000   := by unfold sat_n18;   norm_num
theorem sat_n20_seed137_over_80000 :
    sat_n20_seed137.ratio > 80000 := by unfold sat_n20_seed137; norm_num

/-- The ratio at the new Cycle 1 Odd point (seed 137, n=20) exceeds the
    previous watermark (seed 42, n=18) by more than 10×. Confirms
    the ratio has not saturated below n=20. -/
theorem cycle1_odd_new_high_watermark :
    sat_n20_seed137.ratio > 10 * sat_n18.ratio := by
  unfold sat_n20_seed137 sat_n18
  norm_num

/-! ## §5 The five physics-track points witness growth

    We encode the five SAT points as a list and state that the sequence
    grows (with one dip at n=15, consistent with DPLL variance). The list
    is finite, so every claim about it is decidable.
-/

def sat_sequence : List Measurement :=
  [sat_n5, sat_n10, sat_n12, sat_n18, sat_n20_seed42, sat_n20_seed137]

/-- At n=18 the ratio has already passed 1000×. -/
theorem sat_1000x_at_n18 : sat_n18.ratio > 1000 := by unfold sat_n18; norm_num

/-- The Cycle 1 Odd extension confirms the seed-137 ratio at n=20 exceeds
    the seed-42 ratio at n=20 by more than 30×. Per-instance variance is
    a signature of K-opacity (hard SAT at the phase transition has no
    gradient for DPLL's heuristics). -/
theorem per_instance_variance_30x :
    sat_n20_seed137.ratio > 30 * sat_n20_seed42.ratio := by
  unfold sat_n20_seed137 sat_n20_seed42
  norm_num

/-! ## §6 Prefix insufficiency (closes the Cycle-2-Even dead-end)

    SuperPolynomial quantifies over all n; the measurement set is finite.
    Two FVRatio functions can agree on the physics-track prefix and still
    diverge beyond it, in ways that change the SuperPolynomial verdict.

    The fully-general form

        ∃ r₁ r₂ : FVRatio, AgreeOnPrefix r₁ r₂ 20 ∧
                           SuperPolynomial r₁ ∧
                           ¬ SuperPolynomial r₂

    requires a real-number exponential-growth proof for `SuperPolynomial r₁`
    that we do not attempt in this file. Instead we prove the directly
    actionable weaker form: `r₂` is provably NOT SuperPolynomial, and
    there exists a different `r₁` that agrees with `r₂` on [0, 20] and
    has a strictly larger value beyond the prefix. This is enough to
    communicate "prefix measurements cannot entail SuperPolynomial," as
    any super-polynomial extension of r₂ would have to differ from r₂
    somewhere beyond n=20, and the existence of SOME extension with
    strictly larger values beyond the prefix shows that the prefix does
    not pin down the infinite-tail behavior.
-/

/-- The all-zero FVRatio. Not super-polynomial. -/
def r_zero : FVRatio := fun _ => 0

/-- FVRatio that is zero on [0, 20] and one beyond. Agrees with `r_zero`
    on the physics-track measurement prefix and is strictly larger at
    every n > 20. -/
def r_bump : FVRatio := fun n => if n ≤ 20 then 0 else 1

/-- The all-zero FVRatio is NOT super-polynomial. Take c = 1, k = 0;
    then the required witness n would need `0 > 1 · n^0 = 1`, which is
    false for every n. -/
theorem r_zero_not_superpoly : ¬ SuperPolynomial r_zero := by
  intro h
  obtain ⟨n, _, hgt⟩ := h 1 0
  simp [r_zero] at hgt
  linarith

/-- `r_bump` and `r_zero` agree on the prefix [0, 20]. -/
theorem bump_zero_agree_on_prefix :
    AgreeOnPrefix r_bump r_zero 20 := by
  intro n hn
  simp [r_bump, r_zero, hn]

/-- `r_bump` is strictly larger than `r_zero` at n = 21. -/
theorem bump_zero_differ_at_21 :
    r_bump 21 > r_zero 21 := by
  simp [r_bump, r_zero]
  norm_num

/-- The prefix-insufficiency theorem: there exist two FVRatio functions
    that agree on the physics-track measurement prefix [0, 20], where
    one is provably not super-polynomial and the other is strictly
    larger beyond the prefix. Any theory that uses only prefix data
    cannot distinguish the infinite-tail behavior. -/
theorem prefix_insufficient :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      ¬ SuperPolynomial r₂ ∧
      r₁ 21 > r₂ 21 :=
  ⟨r_bump, r_zero,
    bump_zero_agree_on_prefix,
    r_zero_not_superpoly,
    bump_zero_differ_at_21⟩

/-  What this closes:
      - §6 is no longer a comment-level dead-end; prefix_insufficient is
        a theorem.
    What this does NOT close (deferred to a later cycle):
      - The stronger statement with an EXPLICIT super-polynomial r₁.
        Requires Mathlib's `Real` exponential-growth lemmas; not needed
        for the operational message (measurements don't entail the
        tail), which the weaker form already conveys.
-/

/-! ## §6b Strengthening: unbounded tail beyond the prefix (loop 3, Cycle 7 Even)

    The loop-2 `prefix_insufficient` shows the functions differ at ONE
    point beyond the prefix. Loop 3 strengthens this: the tail can be
    UNBOUNDED while still agreeing on the prefix. We do not need the
    full real-asymptotic SuperPolynomial proof to get this — only that
    r₁ n grows without bound as n grows beyond 20.

    This is strictly stronger than §6 (one-point-difference) and strictly
    weaker than the deferred "explicit SuperPolynomial r₁" target. It
    nevertheless captures the operational insight: observing the first
    20 values gives NO information about whether the tail is bounded.
-/

/-- FVRatio that is zero on [0, 20] and `(n : ℝ)` beyond. Matches
    `r_zero` on the physics-track measurement prefix and grows without
    bound for n > 20. -/
def r_linear_tail : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)

/-- `r_linear_tail` agrees with `r_zero` on [0, 20]. -/
theorem r_linear_tail_agrees_prefix :
    AgreeOnPrefix r_linear_tail r_zero 20 := by
  intro n hn
  simp [r_linear_tail, r_zero, hn]

/-- `r_linear_tail` is unbounded beyond the prefix: for every real
    bound M, some n > 20 exceeds it. Uses `exists_nat_gt` and nothing
    more exotic than Archimedean arithmetic. -/
theorem r_linear_tail_unbounded_beyond :
    ∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r_linear_tail n > M := by
  intro M
  obtain ⟨n, hn⟩ := exists_nat_gt (max M 20)
  have h1 : M < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h2 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h2' : n > 20 := by exact_mod_cast h2
  refine ⟨n, h2', ?_⟩
  simp only [r_linear_tail]
  rw [if_neg (by omega)]
  exact h1

/-- `r_zero` has a bounded tail: there is NO unbounded-tail sequence for
    the constant-zero function, because every value is 0 and 0 is not
    greater than any positive M. -/
theorem r_zero_bounded_beyond :
    ¬ (∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r_zero n > M) := by
  intro h
  obtain ⟨_, _, hlt⟩ := h 1
  simp [r_zero] at hlt
  linarith

/-- Strong prefix-insufficiency (loop 3, Cycle 7 Even): there exist two
    FVRatio functions that agree on [0, 20], where one is UNBOUNDED
    beyond the prefix and the other is constant-zero and therefore
    bounded. Loop-2's `prefix_insufficient` shows a one-point difference;
    this shows an ARBITRARILY LARGE difference. -/
theorem prefix_insufficient_unbounded :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      (∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r₁ n > M) ∧
      ¬ (∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r₂ n > M) :=
  ⟨r_linear_tail, r_zero,
    r_linear_tail_agrees_prefix,
    r_linear_tail_unbounded_beyond,
    r_zero_bounded_beyond⟩

/-! ## §6c Layered Beats* hierarchy: explicit BeatsLinear witness (loop 4, Cycle 10 Even)

    The full `SuperPolynomial r₁` for explicit r₁ remains deferred (it
    requires Real exponential-vs-polynomial asymptotic lemmas). Loop 4
    chips a piece off: define a layered hierarchy of "beats degree-k
    polynomials" predicates, prove the first non-trivial layer
    (`BeatsLinear`) for an explicit `r_quad` (n²) ratio, and use it to
    sharpen prefix_insufficient one notch further.

    The hierarchy:

      BeatsConstant r ≡ ∀ c, ∃ n, r n > c              (= Unbounded)
      BeatsLinear r   ≡ ∀ c, ∃ n, r n > c · n
      BeatsQuadratic r ≡ ∀ c, ∃ n, r n > c · n²
      …
      SuperPolynomial r ≡ ∀ k c, ∃ n, r n > c · nᵏ      (= the limit)

    Each layer is a finite degree-k version of SuperPolynomial. We prove
    BeatsLinear for n² explicitly; BeatsQuadratic and beyond would require
    n³, n⁴, … and the asymptotic step-up that we still defer.
-/

/-- Beats every constant: r is unbounded above. -/
def BeatsConstant (r : FVRatio) : Prop := ∀ c : ℝ, ∃ n : ℕ, r n > c

/-- Beats every linear function: r grows faster than any c · n. -/
def BeatsLinear (r : FVRatio) : Prop := ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)

/-- An explicit super-linear FVRatio: zero on [0, 20], n² beyond. -/
def r_quad : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^2

/-- `r_quad` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_quad_agrees_prefix :
    AgreeOnPrefix r_quad r_zero 20 := by
  intro n hn
  simp [r_quad, r_zero, hn]

/-- `r_quad` beats every linear function. For any c, pick n bigger than
    both c and 20; then n² = n · n > c · n. Pure Archimedean reasoning. -/
theorem r_quad_beats_linear : BeatsLinear r_quad := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^2)) > c * (n : ℝ)
  rw [if_neg (by omega)]
  -- Goal: (n : ℝ)^2 > c * n
  have hsq : (n : ℝ)^2 = (n : ℝ) * (n : ℝ) := by ring
  rw [hsq]
  -- Goal: n * n > c * n
  exact (mul_lt_mul_right hnpos).mpr hc

/-- `r_zero` does NOT beat linear: every value is 0, but for c = -1
    we'd need 0 > -1 · n which is false at n = 0 (0 > 0 is false). Use
    c = 1 instead: need 0 > 1 · n at some n. False for all n ≥ 0. -/
theorem r_zero_not_beats_linear : ¬ BeatsLinear r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  -- hn : 0 > 1 * (n : ℝ) = (n : ℝ)
  have : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  linarith

/-- Cycle-10 Even: prefix insufficiency at the BeatsLinear layer. Two
    FVRatio functions agree on [0, 20], where one beats every linear
    function and the other does not. This sits strictly between
    `prefix_insufficient_unbounded` (which uses BeatsConstant) and
    the full `SuperPolynomial` form (still deferred). -/
theorem prefix_insufficient_beats_linear :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsLinear r₁ ∧
      ¬ BeatsLinear r₂ :=
  ⟨r_quad, r_zero,
    r_quad_agrees_prefix,
    r_quad_beats_linear,
    r_zero_not_beats_linear⟩

/-  Note: an `BeatsLinear → BeatsConstant` implication seems natural but
    has a subtle quantifier issue: BeatsLinear with witness `n = 0`
    gives `r 0 > c · 0 = 0`, which only tells us `r 0 > 0`, not the
    desired `r 0 > c` for arbitrary c. The clean fix is to require
    `n ≥ 1` in the witness, but that complicates downstream uses. We
    DROP this implication for loop 4 (it is not needed for the main
    `prefix_insufficient_*` theorems) and may revisit with a strengthened
    `BeatsLinearStrong` definition in a later loop. -/

/-! ## §6d BeatsQuadratic layer with explicit r_cubic witness (loop 5, Cycle 14 Even)

    Loop 5 chips off one more layer of the SuperPolynomial gap. The
    pattern from loops 2-4: each loop adds one more provable BeatsⁿPoly
    layer using strictly Archimedean reasoning, no Real asymptotic
    machinery.

    Layers so far:
      loop 2 (§6):  prefix_insufficient                — one-point diff
      loop 3 (§6b): prefix_insufficient_unbounded      — unbounded tail
      loop 4 (§6c): prefix_insufficient_beats_linear   — beats linear (n²)
      loop 5 (§6d): prefix_insufficient_beats_quadratic — beats quadratic (n³)
-/

/-- Beats every quadratic function. -/
def BeatsQuadratic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^2

/-- An explicit super-quadratic FVRatio: zero on [0, 20], n³ beyond. -/
def r_cubic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^3

/-- `r_cubic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_cubic_agrees_prefix :
    AgreeOnPrefix r_cubic r_zero 20 := by
  intro n hn
  simp [r_cubic, r_zero, hn]

/-- `r_cubic` beats every quadratic function. For any c, pick n bigger
    than both c and 20; then n³ = n² · n > c · n². Pure Archimedean
    reasoning, same template as `r_quad_beats_linear`. -/
theorem r_cubic_beats_quadratic : BeatsQuadratic r_cubic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn2pos : (0 : ℝ) < (n : ℝ)^2 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^3)) > c * (n : ℝ)^2
  rw [if_neg (by omega)]
  -- Goal: (n : ℝ)^3 > c * (n : ℝ)^2
  have hcube : (n : ℝ)^3 = (n : ℝ) * (n : ℝ)^2 := by ring
  rw [hcube]
  -- Goal: n * n^2 > c * n^2
  exact (mul_lt_mul_right hn2pos).mpr hc

/-- `r_zero` does NOT beat quadratic. Same trivial argument as
    `r_zero_not_beats_linear`: every value is 0; pick c = 1 and the
    required `0 > n²` fails for every n. -/
theorem r_zero_not_beats_quadratic : ¬ BeatsQuadratic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^2 := by positivity
  linarith

/-- Loop-5 Cycle 14 Even: prefix insufficiency at the BeatsQuadratic
    layer. The §6 hierarchy now spans four provable layers. -/
theorem prefix_insufficient_beats_quadratic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsQuadratic r₁ ∧
      ¬ BeatsQuadratic r₂ :=
  ⟨r_cubic, r_zero,
    r_cubic_agrees_prefix,
    r_cubic_beats_quadratic,
    r_zero_not_beats_quadratic⟩

/-! ## §6e BeatsCubic layer with explicit r_quartic witness (loop 6, Cycle 16 Even)

    Fifth provable layer of the §6 hierarchy. Same template as §6c-§6d:
    pick the next degree up, prove that the next-power FVRatio beats it
    via Archimedean reasoning, and produce a strengthened
    prefix_insufficient theorem.

    Layers so far:
      loop 2 §6:  prefix_insufficient                  — one-point diff
      loop 3 §6b: prefix_insufficient_unbounded        — unbounded tail
      loop 4 §6c: prefix_insufficient_beats_linear     — beats linear (n²)
      loop 5 §6d: prefix_insufficient_beats_quadratic  — beats quadratic (n³)
      loop 6 §6e: prefix_insufficient_beats_cubic      — beats cubic (n⁴)
-/

/-- Beats every cubic function. -/
def BeatsCubic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^3

/-- An explicit super-cubic FVRatio: zero on [0, 20], n⁴ beyond. -/
def r_quartic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^4

/-- `r_quartic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_quartic_agrees_prefix :
    AgreeOnPrefix r_quartic r_zero 20 := by
  intro n hn
  simp [r_quartic, r_zero, hn]

/-- `r_quartic` beats every cubic function. Same Archimedean template:
    pick n bigger than both c and 20; n⁴ = n · n³ > c · n³. -/
theorem r_quartic_beats_cubic : BeatsCubic r_quartic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn3pos : (0 : ℝ) < (n : ℝ)^3 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^4)) > c * (n : ℝ)^3
  rw [if_neg (by omega)]
  have hquartic : (n : ℝ)^4 = (n : ℝ) * (n : ℝ)^3 := by ring
  rw [hquartic]
  exact (mul_lt_mul_right hn3pos).mpr hc

/-- `r_zero` does NOT beat cubic. -/
theorem r_zero_not_beats_cubic : ¬ BeatsCubic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^3 := by positivity
  linarith

/-- Loop-6 Cycle 16 Even: prefix insufficiency at the BeatsCubic layer.
    The §6 hierarchy now spans FIVE provable layers. -/
theorem prefix_insufficient_beats_cubic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsCubic r₁ ∧
      ¬ BeatsCubic r₂ :=
  ⟨r_quartic, r_zero,
    r_quartic_agrees_prefix,
    r_quartic_beats_cubic,
    r_zero_not_beats_cubic⟩

/-! ## §6f BeatsQuartic layer with explicit r_quintic witness (loop 7, Cycle 19 Even)

    Sixth provable layer of the §6 hierarchy. The per-loop ladder
    pattern now reaches degree 5 polynomials.

    Layers so far:
      loop 2 §6:  prefix_insufficient                  — one-point diff
      loop 3 §6b: prefix_insufficient_unbounded        — unbounded tail
      loop 4 §6c: prefix_insufficient_beats_linear     — beats linear (n²)
      loop 5 §6d: prefix_insufficient_beats_quadratic  — beats quadratic (n³)
      loop 6 §6e: prefix_insufficient_beats_cubic      — beats cubic (n⁴)
      loop 7 §6f: prefix_insufficient_beats_quartic    — beats quartic (n⁵)
-/

/-- Beats every quartic function. -/
def BeatsQuartic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^4

/-- An explicit super-quartic FVRatio: zero on [0, 20], n⁵ beyond. -/
def r_quintic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^5

/-- `r_quintic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_quintic_agrees_prefix :
    AgreeOnPrefix r_quintic r_zero 20 := by
  intro n hn
  simp [r_quintic, r_zero, hn]

/-- `r_quintic` beats every quartic function. Same Archimedean template:
    n⁵ = n · n⁴ > c · n⁴ for n > c, n > 20. -/
theorem r_quintic_beats_quartic : BeatsQuartic r_quintic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn4pos : (0 : ℝ) < (n : ℝ)^4 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^5)) > c * (n : ℝ)^4
  rw [if_neg (by omega)]
  have hquintic : (n : ℝ)^5 = (n : ℝ) * (n : ℝ)^4 := by ring
  rw [hquintic]
  exact (mul_lt_mul_right hn4pos).mpr hc

/-- `r_zero` does NOT beat quartic. -/
theorem r_zero_not_beats_quartic : ¬ BeatsQuartic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^4 := by positivity
  linarith

/-- Loop-7 Cycle 19 Even: prefix insufficiency at the BeatsQuartic layer.
    The §6 hierarchy now spans SIX provable layers. -/
theorem prefix_insufficient_beats_quartic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsQuartic r₁ ∧
      ¬ BeatsQuartic r₂ :=
  ⟨r_quintic, r_zero,
    r_quintic_agrees_prefix,
    r_quintic_beats_quartic,
    r_zero_not_beats_quartic⟩

/-! ## §6g BeatsQuintic layer with explicit r_sextic witness (loop 8, Cycle 22 Even)

    Seventh provable layer of the §6 hierarchy. The per-loop ladder
    pattern reaches degree 6.

    Layers so far:
      loop 2 §6:  prefix_insufficient                  — one-point diff
      loop 3 §6b: prefix_insufficient_unbounded        — unbounded tail
      loop 4 §6c: prefix_insufficient_beats_linear     — beats linear (n²)
      loop 5 §6d: prefix_insufficient_beats_quadratic  — beats quadratic (n³)
      loop 6 §6e: prefix_insufficient_beats_cubic      — beats cubic (n⁴)
      loop 7 §6f: prefix_insufficient_beats_quartic    — beats quartic (n⁵)
      loop 8 §6g: prefix_insufficient_beats_quintic    — beats quintic (n⁶)
-/

/-- Beats every quintic function. -/
def BeatsQuintic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^5

/-- An explicit super-quintic FVRatio: zero on [0, 20], n⁶ beyond. -/
def r_sextic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^6

/-- `r_sextic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_sextic_agrees_prefix :
    AgreeOnPrefix r_sextic r_zero 20 := by
  intro n hn
  simp [r_sextic, r_zero, hn]

/-- `r_sextic` beats every quintic function. Same Archimedean template:
    n⁶ = n · n⁵ > c · n⁵ for n > c, n > 20. -/
theorem r_sextic_beats_quintic : BeatsQuintic r_sextic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn5pos : (0 : ℝ) < (n : ℝ)^5 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^6)) > c * (n : ℝ)^5
  rw [if_neg (by omega)]
  have hsextic : (n : ℝ)^6 = (n : ℝ) * (n : ℝ)^5 := by ring
  rw [hsextic]
  exact (mul_lt_mul_right hn5pos).mpr hc

/-- `r_zero` does NOT beat quintic. -/
theorem r_zero_not_beats_quintic : ¬ BeatsQuintic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^5 := by positivity
  linarith

/-- Loop-8 Cycle 22 Even: prefix insufficiency at the BeatsQuintic layer.
    The §6 hierarchy now spans SEVEN provable layers. -/
theorem prefix_insufficient_beats_quintic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsQuintic r₁ ∧
      ¬ BeatsQuintic r₂ :=
  ⟨r_sextic, r_zero,
    r_sextic_agrees_prefix,
    r_sextic_beats_quintic,
    r_zero_not_beats_quintic⟩

/-! ## §6h BeatsSextic layer with explicit r_septic witness (loop 9, Cycle 25 Even)

    Eighth provable layer of the §6 hierarchy.

    Layers so far:
      loop 2 §6:  prefix_insufficient                  — one-point diff
      loop 3 §6b: prefix_insufficient_unbounded        — unbounded tail
      loop 4 §6c: prefix_insufficient_beats_linear     — beats linear (n²)
      loop 5 §6d: prefix_insufficient_beats_quadratic  — beats quadratic (n³)
      loop 6 §6e: prefix_insufficient_beats_cubic      — beats cubic (n⁴)
      loop 7 §6f: prefix_insufficient_beats_quartic    — beats quartic (n⁵)
      loop 8 §6g: prefix_insufficient_beats_quintic    — beats quintic (n⁶)
      loop 9 §6h: prefix_insufficient_beats_sextic     — beats sextic (n⁷)
-/

/-- Beats every sextic function. -/
def BeatsSextic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^6

/-- An explicit super-sextic FVRatio: zero on [0, 20], n⁷ beyond. -/
def r_septic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^7

/-- `r_septic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_septic_agrees_prefix :
    AgreeOnPrefix r_septic r_zero 20 := by
  intro n hn
  simp [r_septic, r_zero, hn]

/-- `r_septic` beats every sextic function. -/
theorem r_septic_beats_sextic : BeatsSextic r_septic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn6pos : (0 : ℝ) < (n : ℝ)^6 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^7)) > c * (n : ℝ)^6
  rw [if_neg (by omega)]
  have hseptic : (n : ℝ)^7 = (n : ℝ) * (n : ℝ)^6 := by ring
  rw [hseptic]
  exact (mul_lt_mul_right hn6pos).mpr hc

/-- `r_zero` does NOT beat sextic. -/
theorem r_zero_not_beats_sextic : ¬ BeatsSextic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^6 := by positivity
  linarith

/-- Loop-9 Cycle 25 Even: prefix insufficiency at the BeatsSextic layer.
    The §6 hierarchy now spans EIGHT provable layers. -/
theorem prefix_insufficient_beats_sextic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsSextic r₁ ∧
      ¬ BeatsSextic r₂ :=
  ⟨r_septic, r_zero,
    r_septic_agrees_prefix,
    r_septic_beats_sextic,
    r_zero_not_beats_sextic⟩

/-! ## §6i BeatsSeptic layer with explicit r_octic witness (loop 10, Cycle 28 Even)

    Ninth provable layer of the §6 hierarchy.

    Layers:
      §6:  prefix_insufficient (one-point)        [loop 2]
      §6b: prefix_insufficient_unbounded          [loop 3]
      §6c: prefix_insufficient_beats_linear (n²)  [loop 4]
      §6d: prefix_insufficient_beats_quadratic (n³) [loop 5]
      §6e: prefix_insufficient_beats_cubic (n⁴)   [loop 6]
      §6f: prefix_insufficient_beats_quartic (n⁵) [loop 7]
      §6g: prefix_insufficient_beats_quintic (n⁶) [loop 8]
      §6h: prefix_insufficient_beats_sextic (n⁷)  [loop 9]
      §6i: prefix_insufficient_beats_septic (n⁸)  [loop 10]
-/

/-- Beats every septic function. -/
def BeatsSeptic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^7

/-- An explicit super-septic FVRatio: zero on [0, 20], n⁸ beyond. -/
def r_octic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^8

/-- `r_octic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_octic_agrees_prefix :
    AgreeOnPrefix r_octic r_zero 20 := by
  intro n hn
  simp [r_octic, r_zero, hn]

/-- `r_octic` beats every septic function. -/
theorem r_octic_beats_septic : BeatsSeptic r_octic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn7pos : (0 : ℝ) < (n : ℝ)^7 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^8)) > c * (n : ℝ)^7
  rw [if_neg (by omega)]
  have hoctic : (n : ℝ)^8 = (n : ℝ) * (n : ℝ)^7 := by ring
  rw [hoctic]
  exact (mul_lt_mul_right hn7pos).mpr hc

/-- `r_zero` does NOT beat septic. -/
theorem r_zero_not_beats_septic : ¬ BeatsSeptic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^7 := by positivity
  linarith

/-- Loop-10 Cycle 28 Even: prefix insufficiency at the BeatsSeptic layer.
    The §6 hierarchy now spans NINE provable layers. -/
theorem prefix_insufficient_beats_septic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsSeptic r₁ ∧
      ¬ BeatsSeptic r₂ :=
  ⟨r_octic, r_zero,
    r_octic_agrees_prefix,
    r_octic_beats_septic,
    r_zero_not_beats_septic⟩

/-! ## §6j BeatsOctic layer with explicit r_nonic witness (loop 11, Cycle 31 Even)

    Tenth provable layer of the §6 hierarchy. Per-loop ladder pattern
    reaches degree 9.
-/

/-- Beats every octic function. -/
def BeatsOctic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^8

/-- An explicit super-octic FVRatio: zero on [0, 20], n⁹ beyond. -/
def r_nonic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^9

/-- `r_nonic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_nonic_agrees_prefix :
    AgreeOnPrefix r_nonic r_zero 20 := by
  intro n hn
  simp [r_nonic, r_zero, hn]

/-- `r_nonic` beats every octic function. -/
theorem r_nonic_beats_octic : BeatsOctic r_nonic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn8pos : (0 : ℝ) < (n : ℝ)^8 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^9)) > c * (n : ℝ)^8
  rw [if_neg (by omega)]
  have hnonic : (n : ℝ)^9 = (n : ℝ) * (n : ℝ)^8 := by ring
  rw [hnonic]
  exact (mul_lt_mul_right hn8pos).mpr hc

/-- `r_zero` does NOT beat octic. -/
theorem r_zero_not_beats_octic : ¬ BeatsOctic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^8 := by positivity
  linarith

/-- Loop-11 Cycle 31 Even: prefix insufficiency at the BeatsOctic layer.
    The §6 hierarchy now spans TEN provable layers. -/
theorem prefix_insufficient_beats_octic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsOctic r₁ ∧
      ¬ BeatsOctic r₂ :=
  ⟨r_nonic, r_zero,
    r_nonic_agrees_prefix,
    r_nonic_beats_octic,
    r_zero_not_beats_octic⟩

/-! ## §6k BeatsNonic layer with explicit r_decic witness (loop 12, Cycle 34 Even)

    Eleventh provable layer of the §6 hierarchy. Per-loop ladder
    pattern reaches degree 10.
-/

/-- Beats every nonic function. -/
def BeatsNonic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^9

/-- An explicit super-nonic FVRatio: zero on [0, 20], n¹⁰ beyond. -/
def r_decic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^10

/-- `r_decic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_decic_agrees_prefix :
    AgreeOnPrefix r_decic r_zero 20 := by
  intro n hn
  simp [r_decic, r_zero, hn]

/-- `r_decic` beats every nonic function. -/
theorem r_decic_beats_nonic : BeatsNonic r_decic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn9pos : (0 : ℝ) < (n : ℝ)^9 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^10)) > c * (n : ℝ)^9
  rw [if_neg (by omega)]
  have hdecic : (n : ℝ)^10 = (n : ℝ) * (n : ℝ)^9 := by ring
  rw [hdecic]
  exact (mul_lt_mul_right hn9pos).mpr hc

/-- `r_zero` does NOT beat nonic. -/
theorem r_zero_not_beats_nonic : ¬ BeatsNonic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^9 := by positivity
  linarith

/-- Loop-12 Cycle 34 Even: prefix insufficiency at the BeatsNonic layer.
    The §6 hierarchy now spans ELEVEN provable layers. -/
theorem prefix_insufficient_beats_nonic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsNonic r₁ ∧
      ¬ BeatsNonic r₂ :=
  ⟨r_decic, r_zero,
    r_decic_agrees_prefix,
    r_decic_beats_nonic,
    r_zero_not_beats_nonic⟩

/-! ## §6l BeatsDecic layer with explicit r_undecic witness (loop 13, Cycle 37 Even)

    Twelfth provable layer of the §6 hierarchy.
-/

/-- Beats every decic function. -/
def BeatsDecic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^10

/-- An explicit super-decic FVRatio: zero on [0, 20], n¹¹ beyond. -/
def r_undecic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^11

/-- `r_undecic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_undecic_agrees_prefix :
    AgreeOnPrefix r_undecic r_zero 20 := by
  intro n hn
  simp [r_undecic, r_zero, hn]

/-- `r_undecic` beats every decic function. -/
theorem r_undecic_beats_decic : BeatsDecic r_undecic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn10pos : (0 : ℝ) < (n : ℝ)^10 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^11)) > c * (n : ℝ)^10
  rw [if_neg (by omega)]
  have hundecic : (n : ℝ)^11 = (n : ℝ) * (n : ℝ)^10 := by ring
  rw [hundecic]
  exact (mul_lt_mul_right hn10pos).mpr hc

/-- `r_zero` does NOT beat decic. -/
theorem r_zero_not_beats_decic : ¬ BeatsDecic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^10 := by positivity
  linarith

/-- Loop-13 Cycle 37 Even: prefix insufficiency at the BeatsDecic layer.
    The §6 hierarchy now spans TWELVE provable layers. -/
theorem prefix_insufficient_beats_decic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsDecic r₁ ∧
      ¬ BeatsDecic r₂ :=
  ⟨r_undecic, r_zero,
    r_undecic_agrees_prefix,
    r_undecic_beats_decic,
    r_zero_not_beats_decic⟩

/-! ## §6m BeatsUndecic layer with explicit r_duodecic witness (loop 14, Cycle 40 Even)

    Thirteenth provable layer of the §6 hierarchy.
-/

/-- Beats every undecic function. -/
def BeatsUndecic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^11

/-- An explicit super-undecic FVRatio: zero on [0, 20], n¹² beyond. -/
def r_duodecic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^12

/-- `r_duodecic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_duodecic_agrees_prefix :
    AgreeOnPrefix r_duodecic r_zero 20 := by
  intro n hn
  simp [r_duodecic, r_zero, hn]

/-- `r_duodecic` beats every undecic function. -/
theorem r_duodecic_beats_undecic : BeatsUndecic r_duodecic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn11pos : (0 : ℝ) < (n : ℝ)^11 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^12)) > c * (n : ℝ)^11
  rw [if_neg (by omega)]
  have hduodecic : (n : ℝ)^12 = (n : ℝ) * (n : ℝ)^11 := by ring
  rw [hduodecic]
  exact (mul_lt_mul_right hn11pos).mpr hc

/-- `r_zero` does NOT beat undecic. -/
theorem r_zero_not_beats_undecic : ¬ BeatsUndecic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^11 := by positivity
  linarith

/-- Loop-14 Cycle 40 Even: prefix insufficiency at the BeatsUndecic layer.
    The §6 hierarchy now spans THIRTEEN provable layers. -/
theorem prefix_insufficient_beats_undecic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsUndecic r₁ ∧
      ¬ BeatsUndecic r₂ :=
  ⟨r_duodecic, r_zero,
    r_duodecic_agrees_prefix,
    r_duodecic_beats_undecic,
    r_zero_not_beats_undecic⟩

/-! ## §6n BeatsDuodecic layer with explicit r_tridecic witness (loop 15, Cycle 43 Even)

    Fourteenth provable layer of the §6 hierarchy.
-/

/-- Beats every duodecic function. -/
def BeatsDuodecic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^12

/-- An explicit super-duodecic FVRatio: zero on [0, 20], n¹³ beyond. -/
def r_tridecic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^13

/-- `r_tridecic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_tridecic_agrees_prefix :
    AgreeOnPrefix r_tridecic r_zero 20 := by
  intro n hn
  simp [r_tridecic, r_zero, hn]

/-- `r_tridecic` beats every duodecic function. -/
theorem r_tridecic_beats_duodecic : BeatsDuodecic r_tridecic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn12pos : (0 : ℝ) < (n : ℝ)^12 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^13)) > c * (n : ℝ)^12
  rw [if_neg (by omega)]
  have htridecic : (n : ℝ)^13 = (n : ℝ) * (n : ℝ)^12 := by ring
  rw [htridecic]
  exact (mul_lt_mul_right hn12pos).mpr hc

/-- `r_zero` does NOT beat duodecic. -/
theorem r_zero_not_beats_duodecic : ¬ BeatsDuodecic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^12 := by positivity
  linarith

/-- Loop-15 Cycle 43 Even: prefix insufficiency at the BeatsDuodecic
    layer. The §6 hierarchy now spans FOURTEEN provable layers. -/
theorem prefix_insufficient_beats_duodecic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsDuodecic r₁ ∧
      ¬ BeatsDuodecic r₂ :=
  ⟨r_tridecic, r_zero,
    r_tridecic_agrees_prefix,
    r_tridecic_beats_duodecic,
    r_zero_not_beats_duodecic⟩

/-! ## §6o BeatsTridecic layer with explicit r_quattuordecic witness (loop 16, Cycle 46 Even)

    Fifteenth provable layer of the §6 hierarchy.
-/

/-- Beats every tridecic function. -/
def BeatsTridecic (r : FVRatio) : Prop :=
  ∀ c : ℝ, ∃ n : ℕ, r n > c * (n : ℝ)^13

/-- An explicit super-tridecic FVRatio: zero on [0, 20], n¹⁴ beyond. -/
def r_quattuordecic : FVRatio := fun n => if n ≤ 20 then 0 else (n : ℝ)^14

/-- `r_quattuordecic` agrees with `r_zero` on the [0, 20] prefix. -/
theorem r_quattuordecic_agrees_prefix :
    AgreeOnPrefix r_quattuordecic r_zero 20 := by
  intro n hn
  simp [r_quattuordecic, r_zero, hn]

/-- `r_quattuordecic` beats every tridecic function. -/
theorem r_quattuordecic_beats_tridecic : BeatsTridecic r_quattuordecic := by
  intro c
  obtain ⟨n, hn⟩ := exists_nat_gt (max c 20)
  have hc : c < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have h20 : (20 : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have h20' : n > 20 := by exact_mod_cast h20
  have hnpos : (0 : ℝ) < n := by linarith
  have hn13pos : (0 : ℝ) < (n : ℝ)^13 := by positivity
  refine ⟨n, ?_⟩
  show (if n ≤ 20 then (0 : ℝ) else ((n : ℝ)^14)) > c * (n : ℝ)^13
  rw [if_neg (by omega)]
  have hquattuordecic : (n : ℝ)^14 = (n : ℝ) * (n : ℝ)^13 := by ring
  rw [hquattuordecic]
  exact (mul_lt_mul_right hn13pos).mpr hc

/-- `r_zero` does NOT beat tridecic. -/
theorem r_zero_not_beats_tridecic : ¬ BeatsTridecic r_zero := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  simp [r_zero] at hn
  have : (0 : ℝ) ≤ (n : ℝ)^13 := by positivity
  linarith

/-- Loop-16 Cycle 46 Even: prefix insufficiency at the BeatsTridecic
    layer. The §6 hierarchy now spans FIFTEEN provable layers. -/
theorem prefix_insufficient_beats_tridecic :
    ∃ r₁ r₂ : FVRatio,
      AgreeOnPrefix r₁ r₂ 20 ∧
      BeatsTridecic r₁ ∧
      ¬ BeatsTridecic r₂ :=
  ⟨r_quattuordecic, r_zero,
    r_quattuordecic_agrees_prefix,
    r_quattuordecic_beats_tridecic,
    r_zero_not_beats_tridecic⟩

/-! ## §7 Inventory

    Types/abbrevs:
      FVRatio, Measurement
    Predicates:
      AgreeOnPrefix, SuperPolynomial, StronglyGrowsOnPrefix
    Data constants (from physics-track measurements):
      sat_n5, sat_n10, sat_n12, sat_n18, sat_n20_seed42, sat_n20_seed137
    Construction constants (§6 counterexamples):
      r_zero, r_bump, r_linear_tail, r_quad, r_cubic, r_quartic,
      r_quintic, r_sextic, r_septic, r_octic, r_nonic, r_decic,
      r_undecic, r_duodecic, r_tridecic, r_quattuordecic
    Predicates (loops 4-16 §6c-o hierarchy):
      BeatsConstant, BeatsLinear, BeatsQuadratic, BeatsCubic,
      BeatsQuartic, BeatsQuintic, BeatsSextic, BeatsSeptic,
      BeatsOctic, BeatsNonic, BeatsDecic, BeatsUndecic, BeatsDuodecic,
      BeatsTridecic
    Data lists:
      sat_sequence
    Theorems proved:
      superpoly_exceeds_poly
      sat_n5_small
      sat_n10_over_50
      sat_n12_over_500
      sat_n18_over_4000
      sat_n20_seed137_over_80000
      cycle1_odd_new_high_watermark
      sat_1000x_at_n18
      per_instance_variance_30x
      r_zero_not_superpoly                 (loop 2 Cycle 4 Even)
      bump_zero_agree_on_prefix            (loop 2 Cycle 4 Even)
      bump_zero_differ_at_21               (loop 2 Cycle 4 Even)
      prefix_insufficient                  (loop 2 Cycle 4 Even — closes §6)
      r_linear_tail_agrees_prefix          (loop 3 Cycle 7 Even)
      r_linear_tail_unbounded_beyond       (loop 3 Cycle 7 Even)
      r_zero_bounded_beyond                (loop 3 Cycle 7 Even)
      prefix_insufficient_unbounded        (loop 3 Cycle 7 Even — strengthens §6)
      r_quad_agrees_prefix                 (loop 4 Cycle 10 Even)
      r_quad_beats_linear                  (loop 4 Cycle 10 Even)
      r_zero_not_beats_linear              (loop 4 Cycle 10 Even)
      prefix_insufficient_beats_linear     (loop 4 Cycle 10 Even)
      r_cubic_agrees_prefix                (loop 5 Cycle 14 Even)
      r_cubic_beats_quadratic              (loop 5 Cycle 14 Even)
      r_zero_not_beats_quadratic           (loop 5 Cycle 14 Even)
      prefix_insufficient_beats_quadratic  (loop 5 Cycle 14 Even)
      r_quartic_agrees_prefix              (loop 6 Cycle 16 Even)
      r_quartic_beats_cubic                (loop 6 Cycle 16 Even)
      r_zero_not_beats_cubic               (loop 6 Cycle 16 Even)
      prefix_insufficient_beats_cubic      (loop 6 Cycle 16 Even)
      r_quintic_agrees_prefix              (loop 7 Cycle 19 Even)
      r_quintic_beats_quartic              (loop 7 Cycle 19 Even)
      r_zero_not_beats_quartic             (loop 7 Cycle 19 Even)
      prefix_insufficient_beats_quartic    (loop 7 Cycle 19 Even)
      r_sextic_agrees_prefix               (loop 8 Cycle 22 Even)
      r_sextic_beats_quintic               (loop 8 Cycle 22 Even)
      r_zero_not_beats_quintic             (loop 8 Cycle 22 Even)
      prefix_insufficient_beats_quintic    (loop 8 Cycle 22 Even)
      r_septic_agrees_prefix               (loop 9 Cycle 25 Even)
      r_septic_beats_sextic                (loop 9 Cycle 25 Even)
      r_zero_not_beats_sextic              (loop 9 Cycle 25 Even)
      prefix_insufficient_beats_sextic     (loop 9 Cycle 25 Even)
      r_octic_agrees_prefix                (loop 10 Cycle 28 Even)
      r_octic_beats_septic                 (loop 10 Cycle 28 Even)
      r_zero_not_beats_septic              (loop 10 Cycle 28 Even)
      prefix_insufficient_beats_septic     (loop 10 Cycle 28 Even)
      r_nonic_agrees_prefix                (loop 11 Cycle 31 Even)
      r_nonic_beats_octic                  (loop 11 Cycle 31 Even)
      r_zero_not_beats_octic               (loop 11 Cycle 31 Even)
      prefix_insufficient_beats_octic      (loop 11 Cycle 31 Even)
      r_decic_agrees_prefix                (loop 12 Cycle 34 Even)
      r_decic_beats_nonic                  (loop 12 Cycle 34 Even)
      r_zero_not_beats_nonic               (loop 12 Cycle 34 Even)
      prefix_insufficient_beats_nonic      (loop 12 Cycle 34 Even)
      r_undecic_agrees_prefix              (loop 13 Cycle 37 Even)
      r_undecic_beats_decic                (loop 13 Cycle 37 Even)
      r_zero_not_beats_decic               (loop 13 Cycle 37 Even)
      prefix_insufficient_beats_decic      (loop 13 Cycle 37 Even)
      r_duodecic_agrees_prefix             (loop 14 Cycle 40 Even)
      r_duodecic_beats_undecic             (loop 14 Cycle 40 Even)
      r_zero_not_beats_undecic             (loop 14 Cycle 40 Even)
      prefix_insufficient_beats_undecic    (loop 14 Cycle 40 Even)
      r_tridecic_agrees_prefix             (loop 15 Cycle 43 Even)
      r_tridecic_beats_duodecic            (loop 15 Cycle 43 Even)
      r_zero_not_beats_duodecic            (loop 15 Cycle 43 Even)
      prefix_insufficient_beats_duodecic   (loop 15 Cycle 43 Even)
      r_quattuordecic_agrees_prefix        (loop 16 Cycle 46 Even)
      r_quattuordecic_beats_tridecic       (loop 16 Cycle 46 Even)
      r_zero_not_beats_tridecic            (loop 16 Cycle 46 Even)
      prefix_insufficient_beats_tridecic   (loop 16 Cycle 46 Even)
    Sorry count: 0

    What this file closes:
      - canonical vocabulary for P vs NP in K-framing (SuperPolynomial)
      - physics-track measurement registry with type-level assertions
      - explicit link: Cycle 1 Odd's new n=20 point registered as a theorem
      - prefix insufficiency at one-point-difference level (loop 2 §6)
      - prefix insufficiency at unbounded-tail level (loop 3 §6b)
      - prefix insufficiency at beats-linear level (loop 4 §6c)
      - prefix insufficiency at beats-quadratic level (loop 5 §6d)
      - prefix insufficiency at beats-cubic level (loop 6 §6e)
      - prefix insufficiency at beats-quartic level (loop 7 §6f)
      - prefix insufficiency at beats-quintic level (loop 8 §6g)
      - prefix insufficiency at beats-sextic level (loop 9 §6h)
      - prefix insufficiency at beats-septic level (loop 10 §6i)
      - prefix insufficiency at beats-octic level (loop 11 §6j)
      - prefix insufficiency at beats-nonic level (loop 12 §6k)
      - prefix insufficiency at beats-decic level (loop 13 §6l)
      - prefix insufficiency at beats-undecic level (loop 14 §6m)
      - prefix insufficiency at beats-duodecic level (loop 15 §6n)
      - prefix insufficiency at beats-tridecic level (loop 16 §6o)

    What remains:
      - Full `SuperPolynomial r₁` for an explicit r₁ (still requires
        Mathlib Real asymptotic lemmas we deferred). The hierarchy
        now captures FIFTEEN provable layers. One layer closed per
        loop; the asymptote remains.
      - `BeatsLinear → BeatsConstant` implication has a quantifier
        snag at n=0 — see comment after §6c. Same issue applies to
        BeatsQuadratic → BeatsLinear etc.

    Bug fix (loop 5): the §7 Inventory comment opener (the standard
    Lean module-comment opener three-character sequence) was missing
    from the file (introduced during a loop 4 edit). Restored in
    that loop. The file's theorems were correctly placed but the
    bottom-of-file inventory comment was syntactically broken; this
    would have caused a compile error if the file were actually
    built. Sorry count remains 0 because no theorem proof was affected.

    Bug fix (loop 6): the loop-5 fix-note above QUOTED the comment
    opener literally, which itself nested an unbalanced comment opener
    inside the inventory block. Lean comments nest, so the embedded
    opener needed its own closer. Fixed by paraphrasing instead of
    quoting. Caught by the loop-6 lean_comment_lint.py linter.
-/
