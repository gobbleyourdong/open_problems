# Attempt 007 — Claim-Backing Audit: physics/ top-level + what_is_time/ + what_is_self_reference/

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: physics/README.md (56 lines), physics/what_is_time/PROBLEM.md
(94 lines), what_is_time/gap.md (105 lines), what_is_self_reference/
PROBLEM.md (69 lines). Other physics subdirs (what_is_reality /
nothing / change / information / computation) surveyed for size only.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–16.

## Executive verdict

**physics/what_is_time/ is the strongest single piece of non-math
claim-backing in the entire audit**. gap.md is written at the math-
standard register: 81 Lean theorems with 0 sorry across 7 files,
explicit residual questions with RESOLVED / RESOLVED NEGATIVELY
markers, explicit "remaining inputs (not gaps)" separating the
chain's two free parameters from its derivations, falsification tests
with two specific kill criteria, four weaknesses labeled
MODERATE/LOW, a confirmation bias audit that honestly labels "Not
yet mathematically real — pending experimental Q10 test," and a
self-applicability correction that DOWNGRADES a prior "resolved"
label to "explained but not predicted."

physics/what_is_self_reference/ applies similar structure with
specific K_laws / S_holo / K/S ratio numbers, five physical
instantiations, competing framings with explicit winner.

**Variance between the two**: what_is_time/gap.md is carefully
calibrated; physics/README.md's "parameter-free" framing of the SP
= 2.56 s derivation is LOUDER than what gap.md defends. This is a
framing gap, not a finding gap.

**🔴 RED count**: 1
**🟡 YELLOW count**: 7
**🟢 GREEN count**: 12 (highest green count in any audit)

## RED findings

### R30 — physics/README.md L18 (SP "parameter-free" overclaim)

**The claim** (README L18):
> "The specious present (2.56s) is derived **parameter-free** from
> Kramers ion-channel kinetics + Page-Wootters quantum clock. Two
> independent physics domains combine arithmetically to reproduce the
> measured duration of 'now.'"

**Why load-bearing**: the "parameter-free" claim is the headline
synthesis for the whole physics/ directory, featured on the README
and in the infographic. If it's an overclaim, the directory's
marquee result is weaker than advertised.

**Concern**: what_is_time/gap.md L8 explicitly states:
> "Time is a five-level causal chain from substrate to phenomenology
> with **two inputs beyond fundamental physics**: ΔE = 16.58 kT (ion
> channel barrier, molecular biophysics) and SP ≈ 3 s (evolutionary
> optimization for human ecological niche)."

These are TWO free parameters that enter the derivation. The gap.md's
"Remaining inputs (not gaps)" section L29–34 further clarifies:
"ΔE = 16.58 kT … The value is determined by protein folding
energetics, not fundamental physics. It is **the chain's single
free parameter** for neural/phenomenal predictions" and "SP ≈ 3 s …
Evolutionary optimization."

The bit-optimal constraint (gap.md L26: "N = SP × B = 2.56 × 50 =
128 = 2⁷") derives the 7-qubit threshold from the two inputs —
which is internally consistent, but PRESUPPOSES the inputs.

**Required fix**: README L18 should match gap.md's honest framing.
Replace "parameter-free" with something like "derived from two inputs
(ΔE = 16.58 kT from Nav1.x biophysics; SP ≈ 3 s from ecological
optimization) and shown to predict the 7-qubit Page-Wootters threshold
via the bit-optimal constraint N = SP × B = 128 = 2⁷." This is still
a striking result (two-input to emergent integer) but not a zero-
parameter one.

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y151 | README L13 | "Lyapunov arrow: λ = 0.110/step" | Which dynamical system generates this? Should point to specific numerics/LyapunovArrow simulation file |
| Y152 | README L15 | "128 quantum-clock moments at 50 bits/s" | "50 bits/s conscious bandwidth" — this is a famous-but-contested number (Koch ~20 bits/s; Sziklai 1956 ~10 bits/s reading; Norretranders ~40 bits/s). Pick-and-cite a specific source |
| Y153 | what_is_time PROBLEM L54 | "Kramers barrier kinetics: ΔE = 16.583 k_BT" | Molecular biophysics source for Nav1.x gating energy — Hille textbook or specific paper |
| Y154 | what_is_time PROBLEM L56 | "8.6×10²⁰ active channels compressed to 50 bits/s" | Derivation of 8.6×10²⁰: is it neurons × channels/neuron × density × active fraction? Show the arithmetic |
| Y155 | what_is_self_reference PROBLEM L38 | "K_laws = 21,834 bits" | Where does this specific number come from? Compressed Standard Model Lagrangian + constants? State the derivation |
| Y156 | what_is_self_reference PROBLEM L38 | "S_holo = 10^124 bits" | Bekenstein-Hawking of observable universe gives ~10^123; Hawking 1971 or Padmanabhan reviews; thread |
| Y157 | what_is_time gap.md L66 | "Compression ratio (1.72×10^19) is phenomenological, not derived" | **Already honestly labeled by the corpus** as a MODERATE weakness — this is a GREEN in disguise, the number is known to be fit. Matches confirmation-bias-audit compliance. |

## GREEN findings

- **G106** what_is_time gap.md overall — **81 Lean theorems across 7
  files with 0 sorry** is the math-standard Lean backbone translated
  to physics-of-time. Each theorem has a name and a named file.
- **G107** gap.md L8 "The gap, in one sentence" — captures the entire
  chain in ~200 words. Each claim in the sentence is backed by a
  specific Lean file referenced later. Matches math-standard "the
  binding analytical piece is (†)" sharp-gap-statement.
- **G108** gap.md L20–27 "Three residual questions (updated
  attempt_003)" — each with RESOLVED or RESOLVED NEGATIVELY label.
  R2 ("Does primitivist felt-time survive?") is RESOLVED NEGATIVELY —
  this is a rare explicit refutation of a proposed hypothesis.
- **G109** gap.md L28–34 "Remaining inputs (not gaps)" — separates
  chain parameters (not closable) from unsolved questions. ΔE = 16.58
  kT and SP ≈ 3 s are explicitly labeled as inputs, not free
  parameters to tune. This is exactly the math-standard "assumptions
  not proved here" pattern from attempt_849.
- **G110** gap.md L58–68 "Anti-problem results (attempt_005):
  Falsification tests" — two specific experimental tests that could
  kill the chain (Q10 = 1.68 under hypothermia; bit-optimal
  constraint in non-human species). Concrete falsification criteria.
- **G111** gap.md L64–68 "Four weaknesses identified" labeled
  MODERATE / LOW — sigma-method confirmation-bias-audit applied:
  "Compression ratio is phenomenological, not derived — MODERATE";
  "PW mechanism is metaphorical for brains — LOW"; etc. The chain's
  own author labels its weak points.
- **G112** gap.md L78 — **"Confirmation bias audit: Strong candidate
  pattern with genuine predictions. Not yet mathematically real —
  pending experimental Q10 test."** Explicit self-downgrade from
  "proven" to "pending-experimental-test." Confirmation-bias-audit
  compliance.
- **G113** gap.md L99–101 "Self-applicability correction (attempt_006):
  SP ≈ 3 s **reclassified from 'resolved (evolutionary)' to
  'explained but not predicted.'**" — a LIVE downgrade of a prior
  claim, preserved in the gap.md. This is sigma-method
  Maps-Include-Noise compliance at the document level.
- **G114** gap.md L82 — "Robust prediction: Q10 ≈ 1.68 across all
  species (depends only on conserved ΔE). **Fragile: threshold
  predictions (N values) depend on poorly constrained compression
  ratio — the chain's Achilles' heel.**" Explicit robust-vs-fragile
  labeling per prediction.
- **G115** what_is_self_reference PROBLEM L30–41 — **Three Numbers**
  (K_laws / S_holo / K/S ratio) as structural constants of self-
  reference. Whether the specific numerics hold up under audit
  (Y155/Y156), the framing of self-reference as a **physical
  resource-constraint gap** is a legitimate sigma-method move.
- **G116** what_is_self_reference PROBLEM L52–55 — **"THEOREM or
  CONTINGENCY?"** open question. This is the right sharpness for a
  tier-0 question: not "what is self-reference?" (vague) but "is the
  self-reference gap provably unclosable, or closable with enough
  resources/architecture?" (falsifiable).
- **G117** physics/README.md L50 — **"These are generative questions
  — they don't get closed, they get mapped. The contribution is the
  map with the gaps marked precisely."** Matches sigma v2 "sky
  bridges as deliverable" — the output is a map of the gaps, not a
  closure.

## Recommended fixes (ordered)

1. **[P0]** physics/README.md L18: replace "parameter-free" with the
   gap.md's honest two-input framing (R30).
2. **[P1]** Thread sources for 50 bits/s (Y152) — specific paper
   from the Zimmermann/Koch/Norretranders literature rather than
   unattributed.
3. **[P1]** Derive or cite 8.6×10²⁰ active channels (Y154) — show
   the arithmetic (N neurons × channels/neuron × active fraction
   with sources for each).
4. **[P1]** K_laws = 21,834 bits (Y155) — state the derivation
   method (Kolmogorov complexity of compressed Standard Model
   Lagrangian?).
5. **[P2]** Thread Hille textbook or specific Nav1.x paper for the
   ΔE = 16.583 kT gating energy (Y153).
6. **[P2]** Thread Hawking 1971 / Padmanabhan review for S_holo
   (Y156).

## Non-audit observations

- **physics/what_is_time/gap.md is a template for generative-question
  subdirs**: single-sentence gap + residual questions with resolution
  markers + remaining inputs (not gaps) explicit + falsification
  tests + confirmation-bias audit + self-applicability correction.
  All in ~100 lines. This structure should propagate to the other
  6 physics "what_is_*" subdirs and to philosophy/.
- **The "remaining inputs (not gaps)" section** is a move I haven't
  seen elsewhere. It separates parameters-of-the-chain from
  unsolved-problems. Medical/ subdirs don't distinguish these; every
  non-predicted number is lumped into "gaps." The physics/ convention
  is cleaner.
- **The self-applicability correction** (gap.md L99) is live evidence
  that the Phase 5 self-applicability check (sigma v5 principle) is
  actually being run — not just documented. A claim that was
  "resolved" got DOWNGRADED on self-check. This is the best
  confirmation-bias-audit compliance in the corpus.
- **Surveyed physics subdirs** (attempts/PROBLEM.md line counts):
  what_is_computation (7 attempts, 44+66), what_is_nothing (6
  attempts, 43+132), what_is_self_reference (3 attempts, 69+122),
  what_is_time (6 attempts, 94+105). Others (reality/change/
  information) smaller (2 attempts each). Deeper subdirs (nothing/
  self_reference/time/computation) deserve dedicated audit passes;
  shallower ones may be Phase 0 scaffolds.

## Tag

007 (what_is_time). First audit pass on physics/. **physics/what_is_
time/gap.md is the strongest non-math claim-backing in the entire
audit**: 81 Lean theorems / 0 sorry, RESOLVED/RESOLVED-NEGATIVELY
labels, explicit two-input framing, falsification tests, four
weaknesses with MODERATE/LOW labels, confirmation-bias-audit
self-downgrade ("Not yet mathematically real"), self-applicability
correction that DOWNGRADES a prior 'resolved' to 'explained but not
predicted.' 1 🔴: README "parameter-free" framing contradicts gap.md's
honest two-input framing — needs single-line fix. 7 🟡 (50 bits/s
attribution; 8.6×10²⁰ channel derivation; K_laws = 21,834 bits
source; ΔE = 16.58 kT biophysics source; S_holo Bekenstein source).
**12 🟢** (highest green count in audit): 81 Lean theorems, sharp
gap statement, residual-question resolutions, "remaining inputs
(not gaps)" convention, falsification tests, 4-weakness honest
labeling, confirmation-bias self-downgrade, self-applicability
correction as live map feature, robust-vs-fragile prediction
labeling, three-numbers structural claim, THEOREM-or-CONTINGENCY
sharp open-question, "generative questions don't close, they get
mapped" framing. **Recommendation: physics/what_is_time/gap.md
template should propagate to other generative-question subdirs
(physics + philosophy).** Next fire: other physics what_is_*
subdirs OR philosophy/ OR cross-subdir WHM sweep.
