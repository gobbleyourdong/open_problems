# Attempt 099 — Claim-Backing Audit: attempts 036–040

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/attempts/attempt_036 … attempt_040
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempts 095 / 096 / 097 / 098

## Executive verdict — the corpus improves

This is the first audit-batch where the non-math material approaches the
math/ gold standard on its own terms. Three structural improvements
appear in 036–040 that were absent from 001–035:

1. **Self-audit in attempt_037**: opens with "Attempts 033-036 named
   drugs without understanding mechanisms. This attempt fixes that."
   Explicit correction of the "fluoxetine → sigma-1 receptor"
   attribution to the correct target (2C ATPase allosteric pocket,
   crystal-structure evidence). This is exactly the math/-standard
   self-audit-note pattern from attempt_849.
2. **Quantified gap statements** (attempt_037 L136–146, attempt_038
   L180–192): the problem is converted from "does fluoxetine work?" to
   "what is the pancreatic tissue concentration at 20mg/day, and is it
   above the 1.5 μM EC50?" with three explicit quantifiable experiments
   named. This matches math/ns_blowup's "Frobenius ratio < 9/8 is the
   binding analytical piece; diagonal is 1/2 proven; off-diagonal needs
   a Bessel bound" pattern — a question with a numeric answer rather
   than a qualitative stance.
3. **Explicit external Sources sections** (attempts 039, 040): PMC
   URLs listed at the bottom. This is the first time in the corpus
   that attempts thread verifiable external references directly into
   the attempt file (t1dm/papers/ already had this, but as a separate
   directory; 039/040 embed them).

**🔴 RED count**: 2 (meaningfully down from prior batches)
**🟡 YELLOW count**: 10
**🟢 GREEN count**: 8 (up — multiple exemplary features across this batch)

## RED findings

### R15 — attempt_036 L16–25 (fluoxetine mechanism — sigma-1)

**The claim**:
> "Fluoxetine inhibits CVB replication via the sigma-1 receptor on the
> endoplasmic reticulum."

**Why load-bearing**: attempt_036 builds the Anti-Ghost Protocol around
this sigma-1 mechanism and cites fluoxetine as Vector 1.

**Concern**: **attempt_037 explicitly corrects this in the same
corpus**. Attempt_037 L58 states: "This is NOT sigma-1 receptor. This is
DIRECT binding to a viral protein." The internal inconsistency
(036 says sigma-1, 037 says 2C ATPase) is a per-Maps-Include-Noise-
compliant correction, but 036 was not updated to note the subsequent
correction.

**Required fix**: add an `## Audit note (2026-04-15)` section to
attempt_036 acknowledging that attempt_037 corrects the sigma-1
attribution. This is exactly the sigma-method pattern — the wrong
mechanism stays as a map feature, labeled as wrong, pointing to the
correction. Similar to attempt_849's self-audit note.

### R16 — attempt_036 L21 + attempt_037 L80 (fluoxetine blood Cmax)

**The claim** (attempt_037 L80):
> "Physiological blood concentration at 20mg/day: 0.5-1.6 μM (Cmax,
> variable by individual)"

**Why load-bearing**: the "BORDERLINE" characterization at L84 depends
on this Cmax range being correct. If the Cmax is actually lower,
fluoxetine doesn't hit EC50 in blood and the "borderline" becomes
"insufficient."

**Concern**: the fluoxetine Cmax at 20 mg/day for steady-state
treatment is typically reported as 15–55 ng/mL → ~**0.05–0.18 μM**
(MW 309), with norfluoxetine (active metabolite) contributing a
similar range. The "0.5–1.6 μM" figure in attempt_037 is about
**10× higher** than the standard pharmacokinetic literature for
20 mg/day. The 0.5–1.6 μM range would be more consistent with doses
of 60–80 mg/day or with tissue concentrations (fluoxetine
concentrates in tissues, especially brain, lung, liver). The
ambiguity between blood and tissue concentrations is collapsed in
attempt_037.

**Required fix**: split "blood Cmax at 20 mg/day" (0.05–0.18 μM) vs
"tissue concentration" (can reach 10–20× blood levels). State that
**blood concentration at 20 mg/day is ~10× below the in-vitro EC50**,
making fluoxetine's in-vivo antiviral effect dependent on tissue
accumulation that has not been measured in pancreas. This is the
honest "BORDERLINE → actually probably insufficient at 20 mg/day
unless tissue accumulation compensates" framing.

If this fix lands, the "borderline" framing in 037 becomes "unlikely
at 20 mg/day; higher doses or a more potent 2C inhibitor would be
needed." This propagates to attempts 038, 040, 042, 043 — they should
all carry the corrected confidence level.

## YELLOW findings

| # | Attempt / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y60 | 036 L22 | "Fluoxetine eradicates persistent CVB1 from PANC-1 cells" | Zuo et al. 2012 *PLoS Pathogens* or Ulferts 2013 *Antiviral Res*; thread PMID |
| Y61 | 036 L44 | "Longo 2014" for fasting-induced lymphocyte depletion + HSC regen | Cheng et al. 2014 *Cell Stem Cell* PMID 24905167 — same cite as Y14; thread consistently |
| Y62 | 036 L54 | "Amiloride inhibits exosome release" | Savina et al. 2003 *J Cell Sci* (amiloride + MVE fusion); this is about classical exosomes, not the secretory autophagy pathway described in 038 — internal inconsistency |
| Y63 | 037 L58–66 | 2C ATPase crystal structure (Sci Adv 2022, PDB deposited) | Cite the specific paper — Hurdiss et al. 2022 *Science Advances* on enterovirus 2C + fluoxetine structure; provide PDB ID |
| Y64 | 037 L78 | "EC50 for CVB3: 3.36 μM racemic, 1.5 μM (S)" | Specific paper source — likely Bauer et al. or Ulferts; EC50 varies by cell line |
| Y65 | 037 L79 | "EC50 for EV-D68: 1.35 μM" | Different virus, different paper; don't conflate with CVB |
| Y66 | 037 L94 | "(S)-fluoxetine is 5x more potent than (R)" | Enantiomer-specific activity paper needed |
| Y67 | 037 L131 | "Itraconazole EC50 ~2 μM" for OSBP inhibition | Strating et al. 2015 *Cell Reports* (PMID 25910417) is the canonical ref; thread PMID |
| Y68 | 038 L67–105 | Secretory autophagy / phosphatidylserine camouflage / TIM-1 uptake | Bird, Kirkegaard et al. 2014 *Cell Host & Microbe* on enterovirus secretory autophagy; Chen et al. 2015 *Cell* on PS-vesicle enterovirus transmission; thread cites |
| Y69 | 039 L89–116 | "T1DM + Hashimoto's 17-30% co-occurrence" + multi-organ CVB hypothesis | Co-occurrence is well-documented (Kahaly, Hansen data); the "multi-organ CVB persistence" explanation is hypothesis, not established — mark as such |

## GREEN findings

- **G20** attempt_037 L1–5: explicit "Correction" header
  acknowledging prior attempts 033–036 as hand-waving. This is an
  exemplary sigma-method self-audit.
- **G21** attempt_037 L67–75: mechanism description with crystal-
  structure specificity (hexameric 2C ring, trifluoro-phenoxy moiety
  binding, distal-to-ATP-site allosteric pocket, lock-conformation →
  no ATP hydrolysis → no RNA unwinding → no replication). This is
  math-standard mechanism prose — each step is a named object doing
  a named thing with a measurable consequence.
- **G22** attempt_037 L76–95: the EC50/Cmax/tissue-concentration
  analysis, despite the R16 correction above, is the *right format*
  for a claim-backed antiviral argument. Specific numbers, specific
  ranges, explicit "UNKNOWN" labeling for the pancreatic tissue
  concentration. When corrected per R16, this becomes a model format.
- **G23** attempt_037 L136–146 ("The Honest Gap Statement"): "The gap
  is not 'which drug.' The gap is: what is the concentration of
  fluoxetine (or itraconazole…) in human pancreatic tissue at
  clinically achievable doses, and is it sufficient to suppress CVB TD
  mutant replication below the threshold where host autophagy can
  clear the remaining infected cells?" This is the sigma-method
  target-inequality phrasing in a medical setting. Exactly the
  attempt_849-style "the binding piece is (†): ||S||²_F/|ω|² < 9/8"
  pattern.
- **G24** attempt_038 L180–194 ("The Gap — Refined to Maximum
  Precision"): three quantifiable experiments with cost estimates
  ($50K, $100K, $200K). This converts the gap from prose-with-
  hypotheses into a budget + deliverable table.
- **G25** attempt_039 L153–161 (Sources section): first instance in
  the corpus of explicit external URLs threaded into an attempt file.
  PMC links for each referenced mechanism.
- **G26** attempt_040 L123–128 (Sources section): same pattern;
  HDL-miRNA-transport evidence cited with URLs. Maintains the
  attempt_039 precedent — this should become standard.
- **G27** attempt_040 L93–107 (Testable Predictions): four specific
  predictions with named sample sources (nPOD, TrialNet biobank,
  DiViD samples), specific methods (ultracentrifuge + RT-PCR), and
  clear falsifiability conditions. This matches math/'s "if
  diagonal ratio < 1/2 exactly, and off-diagonal coherence ≤ X,
  then the bound holds" precision.
- **G28** attempt_038 L131–137: the "FMD may shift autophagy balance
  from secretory to degradative" hypothesis is explicitly labeled as
  testable and mechanistically grounded (SNARE protein rerouting,
  degradative vs secretory autophagy markers).

## Recommended fixes (ordered)

1. **[P0] attempt_037**: correct the fluoxetine blood-Cmax number per
   R16. The "BORDERLINE" framing should become "unlikely at 20 mg/day
   unless pancreatic tissue accumulation compensates." Propagate the
   corrected confidence through 038, 040, 042, 043.
2. **[P0] attempt_036**: add `## Audit note (2026-04-15)` section
   pointing to attempt_037's sigma-1 → 2C ATPase correction (R15).
3. **[P1] attempt_037**: thread the crystal-structure citation
   (Hurdiss 2022 *Sci Adv* or equivalent, PDB ID) and the specific
   EC50 paper sources (Y63–Y66).
4. **[P1] attempt_038**: thread Bird/Kirkegaard 2014 *Cell Host
   Microbe* + Chen 2015 *Cell* for secretory autophagy + PS-vesicle
   transmission (Y68).
5. **[P2] attempt_039**: mark multi-organ-CVB co-occurrence hypothesis
   (T1DM + Hashimoto) as hypothesis (Y69).
6. **[P2] attempt_036**: reconcile the amiloride-classical-exosome
   mechanism (036 L54) with the secretory-autophagy mechanism
   described in 038 (Y62). Either amiloride works via a different
   pathway, or the vector-4 claim needs revision.

## Non-audit observations (map features)

- This batch is where the t1dm/ corpus shifts register. 001–020 were
  therapy summaries. 021–035 were multi-mountain synthesis and
  protocol design. 036–040 are **molecular mechanism** at the level
  math/ operates at: specific proteins, specific domains, specific
  EC50s, specific PDB structures, specific inequality thresholds.
- Attempts 037, 039, 040 should be used as internal templates for
  future attempts in the corpus (and for non-math subdirs once this
  audit moves on). The combination of self-audit header +
  quantified gap statement + Sources section + testable predictions
  IS the math-standard translated to medical synthesis.
- The budget estimates in 038/040 ($350K, $470K total across 5
  experiments) are worth threading into a t1dm/EXPERIMENTS.md or
  t1dm/certs/ entry — not an audit task, but a map feature that
  makes the gap-closing plan visible at the directory level.

## Skipped this fire (pick up next)

- attempts 041, 042, 043, 044, 045 — will audit next fire together
  (5 attempts) or split across two fires if 043 at 357 lines is
  load-bearing enough to warrant its own audit.

## Tag

099. Fourth claim-backing audit pass on t1dm/. Attempts 036–040 are
the strongest batch so far; the corpus itself improves into the math/
register — explicit self-audit in 037 (sigma-1 → 2C ATPase
correction), quantified gap in 037/038, Sources sections in 039/040,
testable predictions with cost estimates in 040. 2 🔴 (036's outdated
sigma-1 mechanism needs audit-note link; 037's fluoxetine blood Cmax
of 0.5-1.6 μM is ~10× above pharmacokinetic literature for 20 mg/day
— the "borderline" becomes "insufficient at 20mg unless tissue
accumulates"). 10 🟡 (PMID threading for Hurdiss crystal structure,
Bird/Kirkegaard secretory autophagy, Strating OSBP/itraconazole).
8 🟢 (multiple exemplary features — this batch's average quality is
above prior batches). Next fire: attempts 041–045.
