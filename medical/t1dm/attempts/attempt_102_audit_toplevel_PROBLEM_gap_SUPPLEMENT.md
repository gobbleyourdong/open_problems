# Attempt 102 — Claim-Backing Audit: t1dm/ top-level files (PROBLEM.md, gap.md, SUPPLEMENT_SCHEDULE.md)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/PROBLEM.md (64 lines), gap.md (66 lines),
SUPPLEMENT_SCHEDULE.md (124 lines). **THEWALL.md (2022 lines) deferred**
to next fire on its own.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempts 095–101

## Executive verdict

gap.md reveals the t1dm/ corpus has advanced substantially past
attempts 001–045 — it references attempts 051, 064, 072–075, an ODD
(agent-based) model in unified v2, real transcriptomic data
(GSE184831), and formalized Lean theorems (`crown_jewel` in
`InequalityReversal.lean`, `Lysosomotropic.lean`). This is the
strongest claim-backing structure in the non-math corpus so far:
resolved gaps logged as map features, quantitative predictions with
confidence tiers and sources, and a tight focus on one remaining
clinical-validation question.

**PROBLEM.md is outdated.** It reflects the initial framing from
before the Mountain-4/5 work; its "Phase: 0 (Not started)" marker and
"Gap: antigen-specific immune tolerance" framing contradict gap.md's
current "Gap is a blood draw and a bottle of trehalose" synthesis.

**SUPPLEMENT_SCHEDULE.md is a detailed N=1 personal regimen** (12
supplements, specific doses/timing, $230/mo). Many mechanism claims
are plausible-but-extrapolated.

**🔴 RED count**: 3
**🟡 YELLOW count**: 10
**🟢 GREEN count**: 5

## RED findings

### R21 — PROBLEM.md L1–64 (stale framing)

**The claim**: PROBLEM.md presents the directory's gap as "antigen-
specific immune tolerance" (L52) and declares "systematic approach
Phase: 0 (Not started)" (L64).

**Why load-bearing**: PROBLEM.md is the canonical entry document per
sigma method v3 ("PROBLEM.md ← formal statement + known results" in
SIGMA_METHOD.md). A new reader arriving at t1dm/ reads PROBLEM.md
first. The stale framing misrepresents the actual state of the
directory (which per gap.md is at 75+ attempts, Phase 4/5, with
resolved gaps and formalized theorems).

**Concern**:
1. "Gap: antigen-specific immune tolerance" (L52) — resolved per
   gap.md L7 ("Bypassed: CVB clearance + Treg restoration, not
   tolerance per se").
2. "Phase: 0 (Not started)" (L64) — contradicts gap.md's "After 75
   attempts, 8+ numerical rounds, and first real transcriptomic data"
   (gap.md L39–40).
3. The "Current Approaches" table (L32–44) matches attempts
   001–010 content but doesn't acknowledge the Mountain-4/5 framework
   that became the directory's main contribution.
4. Per v3 working-dir discipline: PROBLEM.md should stay as the
   formal statement but be updated when framing changes are validated.
   Instead, it has drifted into stale state while the work moved on.

**Required fix**: bring PROBLEM.md into sync with gap.md. Either
(a) update PROBLEM.md to reflect the Mountain-4/5 framework and
current Phase, or (b) keep PROBLEM.md as the initial formal statement
but add a "Current State (see gap.md)" pointer at the top. Option (b)
is Maps-Include-Noise compliant — preserves the initial framing as a
historical map feature while directing readers to current work.

### R22 — SUPPLEMENT_SCHEDULE.md L54 (WHM NF-κB "LOCKED")

**The claim**:
> "WHM Breathing … Epinephrine → β-arrestin-2 → IKKα sequestered →
> NF-κB LOCKED → no TNF-α/IL-1β transcription."

**Why load-bearing**: "NEVER skip WHM — only intervention that LOCKS
NF-κB completely" (L103) makes WHM the single irreplaceable component
of the daily regimen. If the mechanism claim is overstated, the rule
is overstated.

**Concern**:
1. Kox et al. 2014 *PNAS* (PMID: 24799686) studied the Wim Hof Method
   and demonstrated increased epinephrine, increased IL-10, and
   attenuated pro-inflammatory response to LPS injection — a
   significant effect, but NOT a demonstration that NF-κB is "locked."
2. The β-arrestin-2 → IKKα sequestration mechanism at epinephrine-
   induced doses has been described in β2-adrenergic signaling
   (Farmer et al., Gao et al.), but this is a *modulation* of NF-κB
   activity, not a complete block. Normal physiological NF-κB
   signaling is still required for host defense — a "LOCKED" NF-κB is
   inconsistent with being alive.
3. "Only intervention that LOCKS NF-κB completely" is false: other
   NF-κB inhibitors exist (parthenolide, curcumin, sulfasalazine,
   many more) — none "lock" NF-κB completely either.

**Required fix**: soften to "reduces NF-κB activation" or
"attenuates pro-inflammatory response" (per Kox 2014); cite Kox 2014
*PNAS* directly. Remove "LOCKED" framing. Remove "only intervention"
— WHM is one of several anti-inflammatory interventions in the
regimen, not the unique one.

### R23 — SUPPLEMENT_SCHEDULE.md L45, L85, L94 (red yeast rice as
"cholesterol supply to virus" cutter)

**The claim**:
> "Red Yeast Rice + CoQ10 … Monacolin K cuts cholesterol supply to
> virus. CoQ10 replaces what statins deplete." (L45)
> "OSBP cholesterol delivery | Berberine (indirect), Red Yeast Rice
> (cholesterol synth)" (L85)

**Why load-bearing**: red yeast rice + berberine combination in the
schedule is justified explicitly as an anti-CVB mechanism. If the
"cuts cholesterol supply to virus" framing is extrapolation, the
specific rationale for including RRY (as opposed to a statin under
physician supervision, or as opposed to diet) doesn't hold.

**Concern**:
1. Monacolin K = lovastatin (structurally identical). RRY is an
   unregulated source of a drug. In some jurisdictions (notably the
   US post-2007 FDA action) RRY products may contain variable amounts
   of monacolin K, with a warning that FDA-standardized statins are
   preferred for cholesterol management.
2. "Cuts cholesterol supply to virus" extrapolates from the Mountain-5
   cholesterol/OSBP hypothesis (attempts 039, 043). The OSBP pathway
   uses ER cholesterol that OSBP shuttles to replication organelles;
   reducing hepatic cholesterol synthesis doesn't directly starve
   OSBP's ER pool in the pancreas. This is a hypothesis about
   systemic-to-tissue cholesterol flux, not an established mechanism.
3. The rationale for RRY over pravastatin/atorvastatin (which are
   standardized, safer, insurance-covered) is not given. RRY is
   chosen because it's OTC, but the attempt-level reasoning for
   including any statin for antiviral purposes is itself hypothesis-
   grade.

**Required fix**: label "cuts cholesterol supply to virus" as
hypothesis-grade (Mountain-5 rationale, attempt_039). Acknowledge
that RRY = lovastatin and note that prescription statins are more
reliably standardized. Acknowledge that statin use for antiviral
purpose in T1DM has no clinical evidence.

## YELLOW findings

| # | Line | Claim | Source gap |
|---|------|-------|------------|
| Y90 | PROBLEM L33 | "Teplizumab … FDA approved 2022 for Stage 2 T1DM. Delays onset by ~2 years. Does NOT prevent." | Prior audit Y (attempt_095 R1 — Herold 2019 NEJM median 48.4 vs 24.4 mo); same correction applies here |
| Y91 | PROBLEM L36 | "Abatacept (CTLA-4-Ig): Preserved C-peptide at 2 years, effect waned" | Orban et al. 2011 Lancet; thread |
| Y92 | gap.md L25–26 | "GSE184831 (persistent CVB1 in PANC-1 pancreatic cells) shows LAMP2 down -2.7x" | GSE184831 is verifiable at NCBI GEO; thread link; note -2.7x needs contrast-specific source (which comparison group?) |
| Y93 | gap.md L30 | "Trehalose (1–3 g/day) … TFEB activation → lysosomal biogenesis" | Sarkar 2007 *JBC* for trehalose/TFEB/autophagy; DeBosch 2016 *Sci Signal* for human dose-response; thread refs |
| Y94 | gap.md L42 | "crown_jewel in InequalityReversal.lean — 0 sorry" | Verify: does `medical/lean/InequalityReversal.lean` exist? What theorem is `crown_jewel`? Not audited yet — flag for Lean-audit fire |
| Y95 | gap.md L60 | "P(insulin independence at 3yr) 20–35%" from "Monte Carlo, 2000 sims" | Which model? Monte Carlo is valid but the generating script should be cited (beta_cell_dynamics.py referenced at L58) |
| Y96 | SUPPLEMENT L14 | "Complete Biotic … Tributyrin = butyrate prodrug … Fasted = HDAC inhibition during peak autophagy → FOXP3 → Tregs" | Arpaia 2013 *Nature* for butyrate/FOXP3; tributyrin-specific PK is different |
| Y97 | SUPPLEMENT L22 | "Target >1mM blood BHB" | Newport 2015 Alzheimer BHB paper cites similar target; Newman 2014 *Cell Metab* for BHB-NLRP3; thread |
| Y98 | SUPPLEMENT L35 | "Berberine 500mg × 2 daily, Blunts glucose spike + AMPK activation + indirect OSBP" | Berberine-glucose: Yin 2008 *Metabolism*; AMPK: Lee 2006 *Diabetes*; "indirect OSBP" is unsourced extrapolation |
| Y99 | SUPPLEMENT L45 | "CoQ10 replaces what statins deplete" | Well-documented statin → mitochondrial CoQ10 depletion (Folkers 1990 PNAS); thread |

## GREEN findings

- **G40** gap.md L4–15 — the "Previous Gaps (Resolved)" table is an
  exemplary sigma-method map artifact: each former gap labeled with
  when identified AND how resolved. Matches math/ns_blowup's pattern
  of "killed algebraically, formalized as theorem" — dead ends are
  kept, explained, and indexed.
- **G41** gap.md L17–36 — "Current Gap (Narrowed to Three Questions)"
  with each sub-gap stated as a question, with "how to close it"
  either as a protocol addition (trehalose) or a specific experiment
  (biopsied islet + IHC). This is math-standard gap-as-checklist
  framing.
- **G42** gap.md L53–66 — quantitative predictions table with
  confidence tier (HIGH / MODERATE / LOW-MODERATE) and a named source
  for each prediction (ODD unified v2, beta_cell_dynamics.py, Monte
  Carlo). This matches math/ns_blowup's "measured max
  ||S||²_F/|ω|² ≈ 0.66 (gap.md line 101)" style — numeric prediction
  + specific generating script.
- **G43** gap.md L51 — "The gap is a blood draw and a bottle of
  trehalose. Everything else is done." Sharp sigma-method-compatible
  closure statement. Matches attempt_043's "$1,200 of bloodwork"
  framing and extends it.
- **G44** SUPPLEMENT_SCHEDULE.md L80–89 — the "What This Stack Hits"
  table maps each biological target (OSBP, NLRP3, NF-κB, autophagy,
  lysosomal function, Treg, beta cell protection) to the specific
  supplements addressing it. Whatever concerns exist about individual
  mechanism claims, the table's structure is a good translation of
  mechanism synthesis into a regimen-design matrix.

## Recommended fixes (ordered)

1. **[P0] PROBLEM.md**: resolve the stale-framing issue (R21). Simplest
   fix: add a banner at the top `> **Note**: this is the initial
   framing (~2024/2025). Current gap and state live in gap.md
   (updated 2026-04-15). See attempts/ for the evolution.` This is
   Maps-Include-Noise compliant and avoids the need to rewrite the
   initial document.
2. **[P0] SUPPLEMENT_SCHEDULE.md**: soften R22 WHM "LOCKED" framing to
   match Kox 2014 PNAS findings. Remove "only intervention that LOCKS
   NF-κB completely." Cite Kox 2014.
3. **[P0] SUPPLEMENT_SCHEDULE.md**: label R23 red yeast rice "cuts
   cholesterol supply to virus" as Mountain-5 hypothesis, not
   established mechanism. Note RRY = lovastatin; suggest prescription
   statin alternative.
4. **[P1] gap.md**: verify/cite GSE184831 correctly with contrast
   group (Y92); thread trehalose refs (Sarkar, DeBosch; Y93);
   thread butyrate/FOXP3 ref (Arpaia 2013; Y96).
5. **[P1] Lean audit**: check that `lean/InequalityReversal.lean` and
   `lean/Lysosomotropic.lean` exist and that the `crown_jewel` theorem
   is real with 0 sorry (Y94). This is its own audit fire.
6. **[P2] Back-propagate audit to attempt files**: the resolutions in
   gap.md (Gap 1 resolved via crown_jewel theorem, Gap 2 via LAMP2
   trehalose, Gap 3 via FOXP1 IHC experiment) should be reflected in
   attempts 064, 074, 075. Earlier audits only went to attempt 045;
   gap.md tells me 046–075 exist with substantive content.

## Non-audit observations (map features)

- The corpus between attempt_045 and attempt_075+ has made major
  advances my earlier audit batches missed: Lean formalization (Y94),
  real transcriptomic data analysis (GSE184831), sequence-level TD
  mutant analysis (attempts 072–073 per gap.md), ODD/agent-based
  modeling (unified v2, 8 organs). The audit should resume at
  attempt_046 with higher priority for these later attempts — they
  are where the corpus reaches its strongest claim-backing state.
- gap.md is the best single document in the non-math corpus so far.
  Its "Previous Gaps (Resolved)" + "Current Gap (three questions)" +
  "Quantitative Predictions with confidence" structure is a model for
  other non-math subdirs. Consider recommending this template to
  physics/ and philosophy/ subdirs when they come up in the audit
  queue.
- SUPPLEMENT_SCHEDULE.md's operator-protocol register is clearly
  labeled (patient name, date, "12 supplements + WHM + 18:6 IF"
  header). This is N=1 regimen design, not research synthesis. The
  RED findings here are because the mechanism claims are stated as
  facts in a document framed as a personal schedule; softening them
  to "rationale" or "hypothesis" would resolve most concerns.

## Tag

102. Seventh claim-backing audit pass on t1dm/. 3 🔴: (i) PROBLEM.md
is stale (Phase 0, gap = antigen-specific tolerance) while gap.md is
at Phase 4/5, 75+ attempts, with resolved gaps — Maps-Include-Noise
fix: banner pointing PROBLEM.md readers to gap.md; (ii) WHM "LOCKED
NF-κB" overstates Kox 2014 PNAS (attenuation, not lock; other NF-κB
inhibitors exist); (iii) Red yeast rice "cuts cholesterol supply to
virus" extrapolates Mountain-5 hypothesis, RRY = lovastatin,
prescription statins are standardized alternatives, no clinical T1DM
evidence for statin antiviral use. 10 🟡 (PMID threading, GSE184831
contrast group, trehalose/butyrate refs, Lean file existence check).
5 🟢: gap.md's Previous-Gaps-Resolved table, narrowed-to-3-questions
gap, quantitative predictions with confidence tiers and named sources,
"blood draw + trehalose" closure, SUPPLEMENT target-to-supplement
mapping table. **Key discovery: t1dm/ corpus has advanced significantly
past attempt_045 — attempts 046–075+ include Lean formalization,
transcriptomic data, sequence analysis, ODD models. Later attempts
may be HIGHER-quality than 001–045.** Next fire: THEWALL.md (2022
lines) OR resume attempt audit at 046 with priority for later attempts.
