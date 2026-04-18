# Dysbiosis — Mechanistic Gaps

## The Core Gap: Causation Direction

**The single largest unresolved question in the dysbiosis field is which way the arrow points.** For almost every dysbiosis-disease pairing, we can document the correlation but cannot establish whether:

1. **Dysbiosis → Disease** (altered microbes initiate local inflammation or systemic immune activation)
2. **Disease → Dysbiosis** (inflammation/immune state alters the local environment, selecting for different microbes)
3. **Bidirectional feedback** (both, reinforcing)
4. **Confounded by a third variable** (diet, genetics, early-life exposure) that independently produces both

For most conditions (seb derm, rosacea, IBD, T1DM, CFS, autism), the correlation is solid and the arrow is not.

Why this matters for intervention: treating microbes directly (probiotics, antibiotics, antifungals) assumes arrow 1. Treating host state (immunomodulators, diet, stress) assumes arrow 2. The lack of a mechanistic answer means treatment selection is empirical — try something, see if it works.

**Sigma method implication**: this gap is a candidate for the **certificate equivalence** limit. If every piece of evidence for causation is itself the correlation we're trying to explain, accumulating more correlations doesn't close the gap. Crossing it may require intervention studies (challenge models, gnotobiotic animals, RCTs with composition manipulation) that the method's gap-mapping can identify but not execute.

## Gap: The Host Threshold Problem

The same microbe at the same density causes disease in some hosts and not others. Current thresholds are phenomenological (we label something "dysbiosis" when disease appears) not mechanistic.

**What we need to measure that we currently can't:**
- Innate immune activation state at the cellular level (NLRP3 primed vs resting, TLR2/4 sensitivity)
- KLK5 activity / cathelicidin processing status
- Barrier function at the microstructural level (tight junction integrity, mucin thickness)
- Regulatory T cell calibration in target tissues
- Cytokine baseline tone (IL-17, IL-23, IFN-γ, TGF-β ratios)

**Candidate biomarkers not yet deployable:**
- Serum LL-37 vs active LL-37 fragments (cathelicidin processing marker)
- Plasma zonulin (gut barrier — controversial: Zhang 2021 challenged the assay specificity)
- Stool calprotectin (gut inflammation — works, but correlates with disease activity not threshold)
- Demodex-specific IgM (host sensitization — research assay only)
- Gut-derived LPS in plasma (EndoCAb LPS-binding assay — noisy)

Gap: we have **molecular candidates** for what sets the threshold, but no **standardized clinical assay** for "how inflammatory is this host baseline."

## Gap: Virome Sampling Depth

Standard stool / skin metagenomic sequencing is optimized for bacterial 16S rRNA (amplicon) or shotgun bacterial DNA. It systematically undersamples:

1. **RNA viruses** (coxsackievirus, enteroviruses, noroviruses, SARS-CoV-2 post-infection reservoirs) — require RNA → cDNA conversion + different library prep
2. **Low-titer persistent viruses** (CVB 5' UTR-deleted forms at islet tissue) — abundance is 10^3-10^5 copies per sample, below detection without enrichment
3. **Latent DNA viruses** (EBV, HHV-6/7, cytomegalovirus) — integrated or episomal, require host-depletion + viral capture
4. **Bacteriophage population** (>10× more abundant than bacteria in gut, essentially uncharacterized at strain level)
5. **Tissue-resident viruses** (in biopsy material, not feces/skin swab) — requires invasive sampling

**What we need**: virome-enriched shotgun metagenomics with host depletion, RNA capture, and 100× standard sequencing depth. Current cost: ~$500-2000 per sample. Not routinely available.

The user's TinyHealth FASTQ order for CVB detection represents a step into this space. Most microbiome studies published through 2024 are DNA-only bacterial.

## Gap: The Definition of "Healthy" Microbiome

There is no agreed-upon baseline. Candidates:

1. **Hunter-gatherer reference** (Hadza, Yanomami, Matsés) — lowest dysbiosis-linked disease rates. But: not achievable for most people. Ethical sampling limitations. Small N.
2. **Pre-Westernization reference** (archived historical stool samples, coprolites) — exists for some timepoints but biased by preservation conditions.
3. **Statistical normal** (large cohort means, e.g., American Gut Project) — but this "normal" already reflects the dysbiosis-linked disease rates we're trying to explain.
4. **Functional redundancy** (same metabolic capacity regardless of which species provide it) — plausible but measurement-heavy (metatranscriptomics + metabolomics).

Without a baseline, "dysbiosis" is defined only by comparison to disease-associated profiles. Circular.

## Gap: Intervention Precision

Current interventions perturb entire communities:

| Intervention | What it does well | What it can't do |
|--------------|-------------------|------------------|
| Broad-spectrum antibiotics | Reduce total bacterial load | Preserve beneficial taxa |
| FMT | Transfer entire community | Select specific species |
| Probiotics | Transiently deliver specific strains | Establish long-term colonization |
| Prebiotics | Feed broad taxonomic groups | Target specific strains |
| Phage therapy | Target specific bacterial species | Handle taxa with no known phage |
| Antifungals | Reduce fungal load | Do so selectively |
| Narrow-spectrum interventions (bacteriocins, etc.) | Species-specific | Mostly not clinically available |

We lack the equivalent of a "CRISPR for microbiome" — tools that change community composition at strain resolution without collateral effects.

## Gap: Gut-Skin Axis Mechanism

Clinically observed: gut interventions (probiotics, dietary changes, fiber) sometimes resolve skin conditions. Mechanism is unclear among competing hypotheses:

1. **Systemic inflammatory tone** — gut dysbiosis → LPS translocation → circulating cytokines → skin reactivity threshold
2. **Direct metabolite transport** — short-chain fatty acids (butyrate, propionate, acetate) enter circulation → affect skin immune cells (FOXP3+ Tregs, keratinocyte differentiation)
3. **Immune education** — gut-associated lymphoid tissue (GALT) trains T cells → altered calibration affects skin reactivity
4. **Microbiome migration** — gut organisms detected on skin (Staph, Candida) suggest physical translocation
5. **Vagus nerve / HPA axis** — gut signals → CNS → stress axis → cortisol → skin inflammation
6. **Histamine / mast cell axis** — dysbiotic gut bacteria produce histamine or prime mast cells systemically

Most likely all five operate. The dominant mechanism for any specific patient is unknown clinically — nobody measures all five routinely.

## Gap: Early-Life Intervention Window

Epidemiological evidence is strong that the first 1000 days (conception to age 3) set the microbiome trajectory for life. Mechanistic gaps:

1. **When does the "window" close?** Some say 3 years. Others say the microbiome remains plastic into adolescence.
2. **Which exposures matter most?** Vaginal delivery, breastfeeding, solid food introduction timing, antibiotic exposure, pet/farm exposure — all contribute, but the relative weights are unknown.
3. **Can deficits be rescued later?** FMT in adults alters composition transiently but rarely establishes long-term shifts. Is "early-life colonization" a permanent structural limit, or just a strong hysteresis?

For the user's son with POD: the early-life assembly angle is worth considering if there's C-section delivery, early antibiotic exposure, or formula feeding in the history.

## Gap: The "Super-Organism" Frame

The human microbiome contains ~10-100× more genes than the human genome. We operate as a super-organism. But:

1. **We inherit the microbiome through non-germline transmission** — mother at birth, environment thereafter. This is a shadow genetic system that doesn't follow Mendelian rules.
2. **Dysbiosis-linked diseases may be "diseases of mis-inherited microbiome"** — mother with dysbiosis passes it to child, cycle continues.
3. **Treating the individual may not be enough** — if the microbial inheritance is broken, generational intervention is required.

No formal framework exists for treating "multigenerational microbiome dysbiosis" as a medical problem. Pediatric gastroenterology touches the edge of it.

## The Integration Gap

Each of these gaps has its own literature. No one has published a model that integrates:
- Host threshold (innate immune calibration) +
- Microbial community state (strain-level) +
- Substrate state (diet, sebum, mucin) +
- Virome (including persistent low-titer) +
- Early-life trajectory +
- Gut-skin-virome cross-communication

The user's multi-target intervention stack (CVB protocol) is, functionally, an integration attempt at the intervention level even if the mechanistic integration is incomplete. It hits host side (NLRP3, NF-κB, autophagy), substrate side (insulin, IF), microbial side (probiotic, butyrate), and virome side (OSBP cholesterol block) simultaneously.

## Status

Dysbiosis is at the state where individual-organ-system correlations are well-mapped, causal arrows are mostly open, intervention tools are blunt, and the integrative model is missing. The sigma method can map these gaps and rule out hypotheses via stall-point analysis on instances, but crossing to mechanism requires wet-lab work outside the method's domain.

**Sigma recommendation**: use the method to identify which mountain has the highest KILL ROI — the treatment prediction most likely to be falsified by existing data. That's where to focus numerics first.

---


---

## Per-Run Extensions — Archived

The 169 per-run Extension blocks (Apr 11–12, covering runs 001–170) have been moved to `gap_extensions_archive.md`. Each was a derivative summary of a canonical `numerics/run_NNN_*.md` file that still exists in full; the Extensions were append-only sediment that rendered this file unscannable without adding gap-level content beyond what the canonical run files contain.

To find the analysis for run N, read `numerics/run_NNN_*.md` directly.

The archive is preserved verbatim for historical traceability (Maps Include Noise, v6).

---

## 2026-04-18 v9.1 discipline addendum

Per `~/SIGMA_METHOD.md` v9.1 C5 / D2:

**Would falsify (dysbiosis-as-universal-threshold-modulation framework):** LAMP2 expression in PBMCs is proposed across the corpus as a lysosomal-block surrogate that should track protocol response. The framework makes a concrete, falsifiable prediction: **in ≥ 3 diseases from the CVB family (e.g., T1DM, ME/CFS, dilated cardiomyopathy), PBMC LAMP2 expression should rise measurably within 3–6 months of full-protocol engagement, with a per-disease effect size ≥ 1.5× baseline by GSE-style analysis.** If LAMP2 does not rise above measurement noise across ≥ 2 of 3 diseases under a pre-registered sampling schedule, the "zombie autophagy" mechanism (ATG7 elevated + LAMP2 suppressed per GSE184831) is disconfirmed as the dysbiosis→organ-damage bottleneck. Weaker falsifier: if the KILL-ROI ranking across the 170+ numerics runs fails to predict which intervention produces the largest biomarker shift in the patient (n=1, Phase-0 behavioral-wall case at medical/THEWALL.md), the kill-ROI-as-leverage-metric methodology needs recalibration.

**Prior art:** Dysbiosis-as-disease-driver ≈ the "gut–X axis" literature (Round & Mazmanian 2009 *Nat Rev Immunol* for gut-immune; Cryan & Dinan 2012 *Nat Rev Neurosci* for gut-brain; Sonnenburg & Bäckhed 2016 *Nature* general review) + mucosal-barrier dysfunction / "leaky gut" (Fasano 2011 *Physiol Rev* zonulin work). Threshold-modulation framing ≈ bistable-attractor models of autoimmunity (Wachsmuth 2011 on β-cell state transitions; Gardner 2000 *Nature* toggle-switch biology). Sigma addition: unifying **13+ dysbiosis-linked diseases under one threshold-modulation stack with 170+ per-run kill-criteria and cross-run mechanistic bridges** (e.g., run_168 IRF1→LGALS1 feedback bridging into run_170 Gal-1 therapy); treating dysbiosis not as a disease-specific confound but as a **cross-disease common substrate** whose modulation has disease-specific downstream valence (harmine beneficial T1DM / harmful rosacea; Gal-1 anti-Th1 in T1DM / pro-EBV-viral in ME/CFS).
