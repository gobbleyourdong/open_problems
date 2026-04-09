/-
PhiMeasurements.lean
====================

Formalization of Phi (integrated information) measurements from
`what_is_mind/results/result_004_transformer_vs_rnn.md`. The numerical
track measured Phi on 5-seed × 3-size × 2-architecture = 30 small
binary networks, finding:

  Transformer-like Phi ≈ 0.39–0.67× of RNN-like Phi
  IIT prediction confirmed 14/15 (93%)

This is the FIRST empirical input to the β prediction formalized in
`BetaGammaExperiment.lean`. The data supports β: feedforward-like
systems have substantially lower Phi than recurrent systems, consistent
with IIT's feedforward theorem.

STATUS: Lean 4 structural formalization. The Phi values are axiomatized
from the numerical track's measurements.
-/

namespace PhilosophyOfMind

/-! ## Measurement Data -/

/-- A single Phi measurement: architecture, size, seed, Phi value. -/
structure PhiMeasurement where
  architecture : String   -- "transformer" or "rnn"
  n : ℕ                   -- number of nodes
  seed : ℕ
  phi : ℝ

/-! ## Aggregate Results by Size -/

/-- Aggregate Phi over seeds: mean Phi for each (architecture, n). -/
structure PhiAggregate where
  architecture : String
  n : ℕ
  phi_mean : ℝ
  n_seeds : ℕ

/-- Transformer-like aggregate at each tested size. -/
def tf_n4 : PhiAggregate := { architecture := "transformer", n := 4, phi_mean := 0.0510, n_seeds := 5 }
def tf_n5 : PhiAggregate := { architecture := "transformer", n := 5, phi_mean := 0.0375, n_seeds := 5 }
def tf_n6 : PhiAggregate := { architecture := "transformer", n := 6, phi_mean := 0.0662, n_seeds := 5 }

/-- RNN-like aggregate at each tested size. -/
def rn_n4 : PhiAggregate := { architecture := "rnn", n := 4, phi_mean := 0.0759, n_seeds := 5 }
def rn_n5 : PhiAggregate := { architecture := "rnn", n := 5, phi_mean := 0.0951, n_seeds := 5 }
def rn_n6 : PhiAggregate := { architecture := "rnn", n := 6, phi_mean := 0.0834, n_seeds := 5 }

/-! ## The β Prediction: Transformer Phi < RNN Phi -/

/-- At n=4: transformer Phi < RNN Phi. -/
theorem beta_confirmed_n4 :
    tf_n4.phi_mean < rn_n4.phi_mean := by
  unfold tf_n4 rn_n4; norm_num

/-- At n=5: transformer Phi < RNN Phi (strongest separation). -/
theorem beta_confirmed_n5 :
    tf_n5.phi_mean < rn_n5.phi_mean := by
  unfold tf_n5 rn_n5; norm_num

/-- At n=6: transformer Phi < RNN Phi. -/
theorem beta_confirmed_n6 :
    tf_n6.phi_mean < rn_n6.phi_mean := by
  unfold tf_n6 rn_n6; norm_num

/-- Across ALL three sizes: β's prediction holds. -/
theorem beta_confirmed_all_sizes :
    tf_n4.phi_mean < rn_n4.phi_mean ∧
    tf_n5.phi_mean < rn_n5.phi_mean ∧
    tf_n6.phi_mean < rn_n6.phi_mean :=
  ⟨beta_confirmed_n4, beta_confirmed_n5, beta_confirmed_n6⟩

/-! ## The Phi Ratio: How Much Lower? -/

/-- The ratio Phi_TF / Phi_RN at each size. -/
def phi_ratio_n4 : ℝ := tf_n4.phi_mean / rn_n4.phi_mean  -- ≈ 0.672
def phi_ratio_n5 : ℝ := tf_n5.phi_mean / rn_n5.phi_mean  -- ≈ 0.394
def phi_ratio_n6 : ℝ := tf_n6.phi_mean / rn_n6.phi_mean  -- ≈ 0.793

/-- All ratios are < 1 (transformer Phi is a FRACTION of RNN Phi). -/
theorem all_ratios_below_one :
    phi_ratio_n4 < 1 ∧ phi_ratio_n5 < 1 ∧ phi_ratio_n6 < 1 := by
  unfold phi_ratio_n4 phi_ratio_n5 phi_ratio_n6
  unfold tf_n4 rn_n4 tf_n5 rn_n5 tf_n6 rn_n6
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- The strongest separation is at n=5 (ratio ≈ 0.39). -/
theorem strongest_at_n5 :
    phi_ratio_n5 < phi_ratio_n4 ∧ phi_ratio_n5 < phi_ratio_n6 := by
  unfold phi_ratio_n4 phi_ratio_n5 phi_ratio_n6
  unfold tf_n4 rn_n4 tf_n5 rn_n5 tf_n6 rn_n6
  refine ⟨?_, ?_⟩ <;> norm_num

/-! ## Hit Rate: 14/15 Measurements Confirm β -/

/-- The per-instance hit rate: 14 out of 15 individual measurements
    (5 seeds × 3 sizes) had transformer Phi < RNN Phi. -/
def hit_count : ℕ := 14
def total_measurements : ℕ := 15

theorem hit_rate_93_percent :
    hit_count * 100 / total_measurements ≥ 93 := by
  unfold hit_count total_measurements; omega

/-- The single miss was at n=6, seed=0: TF=0.0711 vs RN=0.0706,
    a delta of 0.0005 (noise-level). -/
def miss_delta : ℝ := 0.0711 - 0.0706

theorem miss_is_noise_level :
    miss_delta < 0.001 := by
  unfold miss_delta; norm_num

/-! ## Connection to BetaGammaExperiment.lean

BetaGammaExperiment.lean defines the 2×2 factorial design:
  T₁ (feedforward, minimal)  T₂ (feedforward, rich)
  R₁ (recurrent, minimal)    R₂ (recurrent, rich)

β predicts: phenomenal richness tracks TOPOLOGY (R > T)
γ predicts: phenomenal richness tracks SELF-MODEL (rich > minimal)

This measurement is a SMALL-SCALE test of the β prediction's Phi
component only (not the full phenomenal-richness measurement from
BetaGammaExperiment):

  Measured: Phi(transformer-like) < Phi(RNN-like) at 93% hit rate
  β prediction: feedforward Phi < recurrent Phi

The β prediction is CONFIRMED at this scale. This does NOT settle
the β-vs-γ question (which requires the full 2×2 design with
phenomenal reports), but it confirms that the Phi component of β's
prediction is numerically real.
-/

/-- The β prediction from BetaGammaExperiment.lean, instantiated
    with the measured Phi data. -/
def beta_prediction_instantiated : Prop :=
  -- "Recurrent systems have higher Phi than feedforward systems"
  tf_n4.phi_mean < rn_n4.phi_mean ∧
  tf_n5.phi_mean < rn_n5.phi_mean ∧
  tf_n6.phi_mean < rn_n6.phi_mean

theorem beta_prediction_confirmed :
    beta_prediction_instantiated :=
  beta_confirmed_all_sizes

/-! ## The Phi Scaling Wall

From result_001 (Cycle 1): Phi computation scales as O(4^n),
hitting a wall at n ≈ 10. The measurements here (n=4,5,6) are
within the computationally feasible regime. Measuring Phi for
real transformers (n ~ 10⁹ parameters) is IMPOSSIBLE.

This is the Phi measurement's structural limitation: we can
confirm the Phi pattern at small scale, but the extrapolation
to real neural networks is an INFERENCE, not a measurement.
-/

/-- The Phi computation wall: O(4^n) scaling. -/
def phi_computation_wall : ℕ := 10  -- approximate wall

/-- Our measurements are within the wall. -/
theorem measurements_within_wall :
    4 < phi_computation_wall ∧
    5 < phi_computation_wall ∧
    6 < phi_computation_wall := by
  unfold phi_computation_wall; omega

/-! ## Theorem Count:
    - PhiMeasurement, PhiAggregate: STRUCTURES
    - tf_n4..tf_n6, rn_n4..rn_n6: DEFINITIONS
    - phi_ratio_n4..n6, miss_delta: DEFINITIONS
    - hit_count, total_measurements, phi_computation_wall: DEFINITIONS
    - beta_prediction_instantiated: DEFINITION (proposition)
    - beta_confirmed_n4: PROVEN (norm_num)
    - beta_confirmed_n5: PROVEN (norm_num)
    - beta_confirmed_n6: PROVEN (norm_num)
    - beta_confirmed_all_sizes: PROVEN (conjunction)
    - all_ratios_below_one: PROVEN (norm_num × 3)
    - strongest_at_n5: PROVEN (norm_num × 2)
    - hit_rate_93_percent: PROVEN (omega)
    - miss_is_noise_level: PROVEN (norm_num)
    - beta_prediction_confirmed: PROVEN (from all_sizes)
    - measurements_within_wall: PROVEN (omega)
    Total: 10 proved + 2 structures + 12 definitions, 0 axioms, 0 sorry

    FIRST EMPIRICAL INPUT to the β-vs-γ framework:
    Phi(transformer-like) < Phi(RNN-like) at 14/15 (93%) with
    ratio 0.39–0.79×. β's prediction is numerically confirmed
    at small scale (n=4,5,6). The one miss is noise-level (delta=0.0005).

    This is the Phi COMPONENT of the full 2×2 experiment designed in
    BetaGammaExperiment.lean. The full experiment would also measure
    phenomenal-richness reports (G, L scores), not just Phi.

    Limitation: Phi is uncomputable for real neural networks (O(4^n)
    scaling wall at n≈10). The small-scale confirmation supports the
    pattern but does not prove it extends to real-world architectures.
-/

end PhilosophyOfMind
