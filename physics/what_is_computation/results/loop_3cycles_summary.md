# loop_3cycles_summary — 2026-04-09

Narrative summary of the 3-cycle Even/Odd Sigma loop on
`physics/what_is_computation`. The formal cert is at
`certs/loop_3cycles_cert.md`; this file is the human-readable version.

## Intent

Serve as both the Even (theory) and Odd (numerics) instance across three
alternating cycles, starting from the existing attempts (attempts/001-004,
gap.md, the lean/ dir, and the extensive numerics/results corpus) and
advancing the Phase 2 state rather than duplicating Phase 1.

## Cycle-by-cycle

### Cycle 1

**Even** — wrote `lean/KManipulationCore.lean`. The core K-manipulation
framing from `attempts/attempt_001.md` was prose-only; I lifted it to
type level. Six structures (SContent, KContent, CompState, KFunction,
Computation, FiniteKSpec), three predicates (TuringSpecifiable,
NonComputational, CompressionAsymmetryHolds), five theorems proved
(composition closure, Church-Turing at type level, PCTT corollary),
one empirical axiom (`physical_church_turing`). Zero sorry.

**Odd** — wrote `numerics/pnp_rerun_and_extend.py` to reproduce the
canonical `pnp_compression_asymmetry` measurements. All six SAT points
match within 5% of the canonical values. Then I added a single new data
point at n_vars=20, two seeds. Seed 42 gives 2,256×; seed 137 gives
**88,909×** — more than 18× the previous n=18 record. Canonical file
preserved, rerun written to
`results/pnp_asymmetry_cycle1_rerun.json` + findings.md per "Maps
include noise."

Incident: on first run I accidentally overwrote the canonical data file
via the existing script's default output path. Restored via git, wrote
a driver that targets a distinct output filename.

### Cycle 2

**Even** — wrote `lean/CompressionAsymmetryStatement.lean`. The file
defines `SuperPolynomial r` as the Lean Prop for the P vs NP
compression-asymmetry conjecture, and registers the measurement data
(including Cycle 1 Odd's new n=20 points) as typed `Measurement`
constants. Nine theorems, including
`cycle1_odd_new_high_watermark : sat_n20_seed137.ratio > 10 * sat_n18.ratio`,
proved by `norm_num`. Zero sorry.

Mid-file dead-end: attempted a
`finite_measurements_do_not_prove_superpoly` theorem with a broken
quantifier structure. Honored "zero sorry" by recording the intended
lemma as a §6 comment with the sharper form spelled out, rather than
committing a broken theorem. This is the difference between a marked
dead-end and a broken artifact: both are map features, but only one
compiles.

**Odd** — wrote `numerics/landscape_k_coloring.py` to test whether the
SAT K-trajectory fingerprint (decreasing K = easy, flat K = hard)
generalizes to 3-coloring. First run hit a max-step exponential wall on
n=60 hard instances; killed and restarted with a step budget and
smaller n (20, 30). Result: all measurable configurations show K-proxy
*increasing*, contradicting the SAT fingerprint.

Investigation traced this to a measurement artifact: the K-proxy is
`gzip_ratio(remaining_unresolved_edges)`, but as the search progresses
the unresolved-edge blob shrinks below 50 bytes and gzip header
overhead dominates. This is a methodological dead-end, not a domain
negative result — the K-trajectory question for 3-coloring is still
open, the current proxy just can't answer it. Fix paths recorded in
`results/landscape_k_coloring_findings.md` §"What would answer the
question."

### Cycle 3

**Even** — wrote `lean/HypercomputationAntiProblem.lean`. Formalizes
R1 from gap.md at statement level. Defines `PCTT f` (strong), `WeakPCTT f`
(weak), `HyperScenario` (inductive with three named scenarios), and
`HypercomputationClaim`. Four theorems (strong→weak, PCTT kills
hypercomputation pointwise and universally, and the corollary that
the empirical axiom `pctt_universal` refutes the claim). Zero sorry.

**Odd** — this file, plus `certs/loop_3cycles_cert.md` (the formal
certificate). No new numerical experiments in Cycle 3 — the Odd lane
synthesized instead.

## What the loop produced, numerically

| new claim | where                                            |
|----------:|:------------------------------------------------|
|       C11 | KManipulationCore.lean is type-level and sorry-free |
|       C12 | pnp_asymmetry canonical data reproduces within 5% |
|       C13 | new high-watermark: 88,909× at SAT n=20 seed 137 |
|       C14 | SuperPolynomial + measurement registry in Lean   |
|       C15 | K-trajectory proxy is SAT-specific (methodological) |
|       C16 | PCTT/hypercomputation anti-problem is type-level |

C13 is the most interesting numerical result: the find/verify ratio
has not saturated at n=18; per-seed variance at n=20 already spans
40×, signature of DPLL's K-opacity. This strengthens C8 (K-flat
landscape at n=50) by showing the ratio grows along the extrapolated
trajectory, and is consistent with the sat_large_n exponential fit
k=26.6 variables.

C15 is the most interesting dead-end: the K-trajectory fingerprint
that worked in landscape_k.py is NOT a universal NP signature, at
least not under the gzip-on-small-inputs proxy. Fix paths are
recorded; the structural question (is hard 3-coloring K-flat under a
better proxy?) is a live Cycle-4 Odd target.

## Lane coherence check

Each Even artifact landed on the Odd lane that followed, and Odd data
fed back into the next Even lane's type registry:

- K1 Even's `CompressionAsymmetryHolds` → C1 Odd's rerun + extension
- C1 Odd's n=20 points → C2 Even's `sat_n20_seed42`/`sat_n20_seed137`
  constants and `cycle1_odd_new_high_watermark` theorem
- C2 Even's `StronglyGrowsOnPrefix` → C2 Odd's instrumentation design
- C2 Odd's dead-end → C3 Odd's recommendation to improve the K-proxy
- C3 Even's `HypercomputationClaim` → no direct numerical landing
  (R1 is empirical, not computable)

## What stays open

1. **R1 (hypercomputation):** named in Lean, not decided by Lean. A
   genuinely empirical question about physics.
2. **R2 (P ≠ NP):** named in Lean as `SuperPolynomial`, empirical
   evidence strengthened, proof is math-track work.
3. **R3 (BQP substrate-dependence):** already closed before this loop
   (QuantumClassicalHierarchy.lean + ShorStructuredQuantum.lean).
4. **K-trajectory in 3-coloring:** methodologically open; needs the
   fixed-size state encoding or a length-robust compression proxy.
5. **The §6 dead-end:** constructing two explicit FVRatio functions
   that agree on a 20-point prefix but differ on `SuperPolynomial` is
   a concrete Cycle-4 Even exercise and would replace the C14 §6
   comment with a theorem.

## Status

Phase 2, 3-cycle Even/Odd loop complete. All five committed Lean files
in `lean/` compile-consistent (Mathlib-dependent, zero sorry). Seven
new results/certs files. One incident (overwriting canonical data)
caught and resolved via git. One measurement dead-end (C15)
characterized and fix paths recorded.

Next natural step, whenever it comes: Cycle 4 Odd either applies the
fixed-size K-proxy fix to 3-coloring or probes a third problem family
(Hamiltonian cycle is the obvious candidate — small dense state plus
local edge constraints, well-suited to byte encoding). Cycle 4 Even
constructs the explicit FVRatio counterexample to close the §6
dead-end.
