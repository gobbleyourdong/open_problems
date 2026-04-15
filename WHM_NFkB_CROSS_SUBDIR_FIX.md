# WHM → NF-κB Cross-Subdir Fix-List

**Date**: 2026-04-15
**Purpose**: Consolidate the 4 audit findings (R22 t1dm, R24
dysbiosis, R26 POD-implicit, R29 psoriasis) into a single
cross-subdir sweep actionable list.
**Source audit log entries**: fires 9 (R22), 11 (R24), 12 (R26
note), 16 (R29), reinforced in fires 20/22/24.
**Status**: diagnostic only — no edits applied; awaiting operator
go-ahead for the single coordinated fix.

## The claim being audited

Multiple files assert some form of:

> "WHM breathing → epinephrine → β-arrestin-2 → IKKα sequestration →
> NF-κB LOCKED / locked / lockdown → TNF-α not transcribed"

## The specific concern

**Kox et al. 2014 *PNAS* (PMID 24799686)** is the experimental
citation invoked. What the paper actually demonstrated:

- WHM-trained volunteers voluntarily released **catecholamines
  (epinephrine)** during the breathing/cold protocol
- LPS injection after WHM training produced **attenuated TNF-α,
  IL-6, IL-8** compared to non-trained controls
- **Increased IL-10** anti-inflammatory response
- ~50% reduction in inflammatory cytokines — substantial but
  **modulation, not elimination**

What the paper did NOT demonstrate:

- No **"NF-κB lockdown"** — the term is not in the paper; the
  mechanism described is attenuation-of-response, not physical
  lock of the transcription factor
- Specific **β-arrestin-2 → IKKα sequestration** is not the Kox
  paper's mechanism — this comes from separate β-arrestin
  literature (Gao, Witherow, Farmer) where β-arrestin-2 binds
  IκBα (not IKKα directly) and stabilizes it against degradation.
  The two β-arrestin-2 mechanisms are related but not identical.

## Inventory: every file with the overstated claim

| # | File | Line | Current phrasing | Severity |
|---|------|------|-----------------|---------|
| 1 | `medical/dysbiosis/PROBLEM.md` | 199 | "Wim Hof Method (beta-arrestin-2 → NF-κB lock)" | 🔴 (in threshold-modulation list in PROBLEM.md) |
| 2 | `medical/t1dm/SUPPLEMENT_SCHEDULE.md` | 74 | "WHM … NF-κB lockdown" (in daily-inventory table) | 🔴 (operator-facing regimen) |
| 3 | `medical/t1dm/print_schedule.py` | 122 | "Epinephrine locks NF-kB via beta-arrestin-2 pathway" | 🔴 (generates printed protocol) |
| 4 | `medical/t1dm/print_schedule.py` | 158 | "NEVER skip WHM — only intervention that LOCKS NF-κB completely" | 🔴 (rule phrasing is hyperbolic) |
| 5 | `medical/psoriasis/PROBLEM.md` | 49 | "WHM → β-arrestin-2 → IKKα sequestration → NF-κB lockdown → applies to psoriasis" | 🔴 (cross-propagation target, R29) |
| 6 | `medical/psoriasis/attempts/attempt_002_apremilast_bridge.md` | 65 | "WHM → β-arrestin-2 → NF-κB lockdown (transient, requires daily practice)" | 🟡 — already softened with "transient" + "requires daily practice" |
| 7 | `medical/t1dm/attempts/attempt_060_fasting_whm_molecular.md` | 22 | "Stabilizes IκBα → NF-κB locked in cytoplasm → TNF-α NOT transcribed" | 🟡 — mechanism is about IκBα stabilization (correct direction); "locked" is hyperbole |
| 8 | `medical/t1dm/attempts/attempt_062_gun_bullet_criminal.md` | 64, 125 | "NF-κB lockdown" as section framing in synthesis | 🟡 — used rhetorically; mechanism discussion elsewhere is more nuanced |
| 9 | `medical/t1dm/attempts/attempt_063_epinephrine_spike_catalog.md` | 66, 84 | "NF-κB locked" in mechanism chain | 🟡 |
| 10 | `medical/PATIENT_ZERO_TIMELINE.md` | 251 | "β-arrestin-2 → NF-κB lockdown" | 🔴 (top-level patient timeline) |

## Proposed language fix (single consistent replacement)

Replace all 10 instances with one of these (context-dependent):

**Short form** (tables, lists):
> WHM (epinephrine → β-arrestin-2 → IκBα stabilization → **attenuated
> NF-κB activation**, per Kox 2014 *PNAS* PMID 24799686)

**Long form** (mechanism sections):
> WHM breathing activates the sympathetic axis, producing a voluntary
> epinephrine surge (Kox et al. 2014 *PNAS* PMID 24799686). The
> epinephrine → β2-AR → β-arrestin-2 cascade **attenuates NF-κB-
> driven transcription** (TNF-α, IL-6 reduced ~50% in LPS-challenge
> experiments; IL-10 increased). Mechanistically, β-arrestin-2 binds
> IκBα and stabilizes it against proteasomal degradation, which
> reduces the rate of NF-κB nuclear translocation. This is
> **modulation**, not a permanent "lock" — NF-κB-mediated host defense
> remains functional, and the attenuation is strongest in the ~1-2
> hour window after WHM practice.

**Key removals:**
- "NF-κB lock" / "NF-κB locked" / "NF-κB lockdown" / "LOCKS NF-κB"
  → "attenuated NF-κB activation"
- "only intervention that LOCKS NF-κB completely" (print_schedule.py
  L158) → "one of several interventions that attenuate NF-κB
  activation during the window of daily practice"
- "NEVER skip WHM" (implies irreplaceable) → "WHM is the daily
  anti-inflammatory anchor; if skipped, substitute cold exposure or
  BHB salts for partial NF-κB attenuation"

## Why this is worth the sweep

Per Fire 20's finding from the prior content audit: "**~30% wrong
PMIDs, ~20% wrong numbers, ~5% full hallucinations, qualitative
direction almost always right**".

The WHM claim here falls into a sub-category: **qualitative
direction correct** (WHM does attenuate NF-κB via sympathetic/
β-arrestin cascade per real literature) but **magnitude/effect
framing overstated** ("lock" vs "attenuate" is a ~5× magnitude
difference in how the reader weights it).

This is the pattern "approximation creep from similar studies"
(prior audit's 20% wrong-numeric category) applied to a verbal
intensity rather than a specific number. The fix is small per
file but consistent across the corpus — exactly the kind of
propagation bug that's easier to fix in one coordinated sweep
than 10 uncoordinated ones.

## Operator action required

Two options:

**Option A — single coordinated edit pass** (recommended):
- Apply the short-form replacement to the 5 🔴 locations
  (dysbiosis PROBLEM, t1dm SUPPLEMENT_SCHEDULE, t1dm print_schedule
  both lines, psoriasis PROBLEM, PATIENT_ZERO_TIMELINE) — 6 edits
- Soften the 5 🟡 locations to match (attempt_060, 062, 063,
  psoriasis attempt_002 — already partly softened) — 5 edits
- Thread PMID 24799686 (Kox 2014 PNAS) at the most-cited location
  for downstream reuse

**Option B — deferred**:
- Add one banner at dysbiosis/PROBLEM.md L199 stating "the 'NF-κB
  lock' phrasing is corpus shorthand for Kox 2014 PNAS attenuation;
  see WHM_NFkB_CROSS_SUBDIR_FIX.md" — single-edit workaround
- Leave the per-file phrasings and let a future sweep propagate the
  change

Option A is cleaner but requires 11 coordinated edits across 9
files. Option B requires 1 edit but leaves the overstatement in
visible places.

## Status

Diagnostic complete. No edits applied. Waiting for operator go-ahead
on Option A vs B.

## Tag

WHM/NF-κB cross-subdir overstatement sweep. 10 locations identified
(5 🔴 + 5 🟡) across 7 files in 4 subdirs (medical/t1dm/,
medical/dysbiosis/, medical/psoriasis/, medical/ top-level).
Mechanism direction is correct (Kox 2014 PNAS + β-arrestin
literature) but intensity framing ("lock/lockdown") overstates by
~5×. Fix is small per file, consistent across corpus. Single
coordinated sweep recommended.
