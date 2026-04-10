/-
CompressibilityGain.lean
========================

The micro/macro K resolution and the compressibility gain theorem.
From `what_is_time/results/micro_macro_K_findings.md` and
`what_is_time/results/lz78_micro_macro_findings.md`.

THE RESOLUTION:
  gzip-K ≠ algorithmic K. The gap.md claim about micro/macro K
  behavior during thermalization is correct for algorithmic K
  but not for gzip-K. The numerical proxy conflates byte-level
  redundancy (gzip) with description-length (Kolmogorov).

THE CORRECTED CLAIM:
  "The compressibility GAIN from macro vs micro description INCREASES
  along the thermodynamic arrow — not because micro-K decreases, but
  because macro-K stays bounded (short description: 'uniform') while
  the micro state grows increasingly incompressible."

This file encodes:
  1. The gzip-K data (as measured — the honest map)
  2. The S-entropy data (monotone increase — the arrow)
  3. The resolution: why gzip and algorithmic K diverge
  4. The corrected compressibility gain as S-entropy minus macro-K

Sixth Lean file in physics/what_is_time.
-/

/-! ## The Measurement Data -/

/-- A simultaneous measurement of S-entropy, micro-K, and macro-K
    during gas diffusion (500 particles, collision-free, 200 steps). -/
structure ThermalizationSnapshot where
  step : ℕ
  S_entropy : ℝ       -- Shannon entropy (bits) of spatial distribution
  micro_K_gzip : ℝ    -- gzip compression ratio of raw float positions
  macro_K_gzip : ℝ    -- gzip compression ratio of 10×10 histogram

/-- t=0: all particles in left half (low entropy, structured). -/
def therm_t0 : ThermalizationSnapshot := {
  step := 0, S_entropy := 5.5722, micro_K_gzip := 0.9130, macro_K_gzip := 0.4100
}
/-- t=100: partial diffusion. -/
def therm_t100 : ThermalizationSnapshot := {
  step := 100, S_entropy := 6.4106, micro_K_gzip := 0.9127, macro_K_gzip := 0.5150
}
/-- t=200: near equilibrium (uniform). -/
def therm_t200 : ThermalizationSnapshot := {
  step := 200, S_entropy := 6.4765, micro_K_gzip := 0.9083, macro_K_gzip := 0.5100
}

/-! ## Finding 1: S-Entropy Increases (the arrow, confirmed) -/

/-- Shannon entropy increases monotonically during thermalization. -/
theorem S_increases :
    therm_t0.S_entropy < therm_t100.S_entropy ∧
    therm_t100.S_entropy < therm_t200.S_entropy := by
  unfold therm_t0 therm_t100 therm_t200
  refine ⟨?_, ?_⟩ <;> norm_num

/-- Total entropy increase: +0.9043 bits. -/
def delta_S_total : ℝ := therm_t200.S_entropy - therm_t0.S_entropy

theorem delta_S_positive :
    delta_S_total > 0.9 := by
  unfold delta_S_total therm_t200 therm_t0; norm_num

/-! ## Finding 2: Micro-K (gzip) is FLAT -/

/-- Micro-K stays within 0.005 of 0.91 throughout. The raw float
    positions are approximately equally incompressible at all times. -/
theorem micro_K_flat :
    |therm_t0.micro_K_gzip - therm_t200.micro_K_gzip| < 0.005 := by
  unfold therm_t0 therm_t200; norm_num

/-- Micro-K barely changes: Δ = -0.0047 (within noise). -/
def delta_micro_K : ℝ := therm_t200.micro_K_gzip - therm_t0.micro_K_gzip

theorem micro_K_change_negligible :
    |delta_micro_K| < 0.01 := by
  unfold delta_micro_K therm_t200 therm_t0; norm_num

/-! ## Finding 3: Macro-K (gzip) INCREASES — the surprise -/

/-- Macro-K increases from 0.41 to 0.51: the histogram becomes LESS
    compressible as the gas spreads (fewer zero-runs for gzip). -/
theorem macro_K_increases :
    therm_t0.macro_K_gzip < therm_t100.macro_K_gzip := by
  unfold therm_t0 therm_t100; norm_num

/-- Total macro-K increase: +0.1000. -/
def delta_macro_K : ℝ := therm_t200.macro_K_gzip - therm_t0.macro_K_gzip

theorem macro_K_increases_total :
    delta_macro_K > 0.09 := by
  unfold delta_macro_K therm_t200 therm_t0; norm_num

/-! ## Finding 4: The Resolution — gzip-K ≠ Algorithmic K

GZIP-K finds local byte-level redundancy:
  - t=0: particles in left half → repeated low x-coordinates → gzip wins
  - t=200: particles uniform → no byte patterns → gzip loses

ALGORITHMIC K is the shortest PROGRAM:
  - t=0 macro: "particles in left half" — SHORT (~20 bits)
  - t=200 macro: "particles uniform" — SHORT (~20 bits)
  - Both extremes: macro algorithmic K is LOW and CONSTANT

The divergence between gzip-K and algorithmic K is the lesson:
proxy metrics can mislead when the redundancy they detect differs
from the redundancy the theory posits.
-/

/-- Algorithmic K of the macrostate (estimated program length in bits).
    Both "left half" and "uniform" are short descriptions. -/
def algo_K_macro_t0 : ℝ := 20    -- "500 particles, x ∈ [0, 0.5]"
def algo_K_macro_t200 : ℝ := 20  -- "500 particles, uniform in [0,1]²"

/-- Algorithmic macro-K is constant (same description length). -/
theorem algo_macro_K_constant :
    algo_K_macro_t0 = algo_K_macro_t200 := by
  unfold algo_K_macro_t0 algo_K_macro_t200; rfl

/-- Algorithmic K of the microstate is high at both times
    (random positions are incompressible). -/
def algo_K_micro : ℝ := 4000 * 8  -- ~32000 bits for 500 × float32

theorem algo_micro_K_high :
    algo_K_micro > 30000 := by
  unfold algo_K_micro; norm_num

/-! ## Finding 5: The Compressibility Gain Theorem (corrected)

The descriptional gain from coarse-graining:
  gain(t) = K_micro(t) − K_macro(t)

Under ALGORITHMIC K (not gzip):
  - K_micro ≈ constant (high: random positions always incompressible)
  - K_macro ≈ constant (low: short descriptions at all extremes)
  - gain ≈ constant in the limit

Under GZIP-K (measured):
  - micro-K flat (~0.91)
  - macro-K increases (0.41 → 0.51)
  - gain_gzip DECREASES — opposite of the theory!

The S-entropy divergence captures the correct arrow:
  S_divergence(t) = S(t) − algo_K_macro
  This increases because S grows and macro-K is constant.
-/

/-- S-divergence from macro description at each timepoint. -/
def S_div_t0 : ℝ := therm_t0.S_entropy - algo_K_macro_t0
def S_div_t200 : ℝ := therm_t200.S_entropy - algo_K_macro_t200

/-- S-divergence is negative (S is in bits, K_macro is in bits,
    but they measure different things). The relative ordering is
    what matters: divergence INCREASES with time. -/
theorem S_divergence_increases :
    S_div_t200 > S_div_t0 := by
  unfold S_div_t200 S_div_t0 therm_t200 therm_t0 algo_K_macro_t200 algo_K_macro_t0
  norm_num

/-! ## The Honest Map (maps include noise) -/

/-- The gzip-K data contradicts the naive theoretical prediction.
    This is INFORMATION: it means the compressibility gain must be
    stated in terms of algorithmic K, not proxy K. The discrepancy
    between theory and proxy is itself a finding. -/
theorem gzip_contradicts_naive_theory :
    -- Naive prediction: gain_gzip(0) < gain_gzip(200)
    -- Reality: gain_gzip(0) > gain_gzip(200)
    (therm_t0.micro_K_gzip - therm_t0.macro_K_gzip) >
    (therm_t200.micro_K_gzip - therm_t200.macro_K_gzip) := by
  unfold therm_t0 therm_t200; norm_num

/-! ## Theorem Count:
    - ThermalizationSnapshot: STRUCTURE
    - therm_t0, therm_t100, therm_t200: 3 DEFINITIONS
    - delta_S_total, delta_micro_K, delta_macro_K: 3 DEFINITIONS
    - algo_K_macro_t0, algo_K_macro_t200, algo_K_micro: 3 DEFINITIONS
    - S_div_t0, S_div_t200: 2 DEFINITIONS
    - S_increases: PROVEN (norm_num × 2)
    - delta_S_positive: PROVEN (norm_num)
    - micro_K_flat: PROVEN (norm_num)
    - micro_K_change_negligible: PROVEN (norm_num)
    - macro_K_increases: PROVEN (norm_num)
    - macro_K_increases_total: PROVEN (norm_num)
    - algo_macro_K_constant: PROVEN (rfl)
    - algo_micro_K_high: PROVEN (norm_num)
    - S_divergence_increases: PROVEN (norm_num)
    - gzip_contradicts_naive_theory: PROVEN (norm_num)
    Total: 10 proved + 1 structure + 11 definitions, 0 axioms, 0 sorry

    THE RESOLUTION:
    gzip-K ≠ algorithmic K. The thermodynamic arrow is about S-entropy
    increase and ALGORITHMIC compressibility gain, not gzip-K. The gzip
    proxy misses the macro description-length constancy because gzip
    detects byte-level patterns, not semantic descriptions.

    The corrected claim: the descriptional gain from macro vs micro
    grows because S increases while macro algorithmic K stays bounded.
    The gzip data is an honest map feature showing WHERE the proxy fails.
-/
