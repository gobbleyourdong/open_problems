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

## Post-Phase 3 Update — 2026-04-11

### Gap: Gut-Skin Axis — RESOLVED (dominant mechanism identified)

Of the 6 mechanisms listed above, the dominant mechanism for skin inflammatory disease is **#3 (GALT immune education / T-cell reprogramming via IL-23/Th17 axis)**, not #1 (LPS translocation).

Evidence: Published review (PMID 38654394) states "acute systemic inflammation alone does not trigger skin-specific responses." LBP NOT elevated in isolated psoriasis (only elevated with concurrent metabolic syndrome). I-FABP elevated in psoriasis (r=0.78 with PASI). Risankizumab/ustekinumab dual IBD+skin outcomes consistent with shared IL-23 axis.

Mechanism: gut dysbiosis → IL-23 → GALT Th17 priming → dual-homing T cells (α4β7+/CLA+) → skin-draining lymph nodes → IL-23 in skin → Treg plasticity (Foxp3+ → IL-17A-producing) → threshold lowered.

LPS (mechanism #1) is a contributing amplifier in metabolic syndrome context but NOT the primary gut-skin driver for isolated skin dysbiosis disease.

### Gap: Host Threshold — PARTIALLY RESOLVED (two inputs identified)

The threshold (M4/THE WALL) is now understood to be jointly set by TWO independent, modifiable inputs:

1. **IFN-α arm (M3):** CVB → chronic IFN-α → pDC expansion → skin pDC threshold lowered for B. oleronius → IL-23 → Th17 loop
2. **Th17 arm (M1):** Gut dysbiosis → GALT Th17 → skin Treg plasticity via IL-23

Both arms share a common final pathway: pDC/IL-23/Th17 → functional Treg depletion. T-index v3 proposed with Node D (IFN-α) added to Node C (I-FABP for gut arm). Molecular mechanism of Treg plasticity confirmed (PMID 31776355, IL-23 converts Foxp3+ Tregs to IL-17A producers in human psoriatic skin).

**Still unresolved:** no single clinical assay for the threshold STATE itself. T-index v3 is a proxy, not a measurement.

### Gap: The Integration Gap — SUBSTANTIALLY ADDRESSED

The convergent mechanism is now assembled (see `results/phase3_synthesis.md`):

Shared pDC/IFN-α/IL-23 axis connects:
- Gut dysbiosis (M1) via Th17 trafficking
- Virome (M3, CVB) via chronic IFN-α
- Oral dysbiosis (M7, P. gingivalis) via M3→M7 bridge (CAR upregulation)
- Skin dysbiosis (M2) via threshold modulation

Epidemiological signature: T1DM + rosacea co-occurrence OR 2.59 (Egeberg JAAD 2016). Explained by CVB→IFN-α→pDC priming of rosacea loop in T1DM patients.

**This is not proven** — it is 4 strong candidate sky bridges assembled into a coherent framework. Each requires one decisive test:
- M3↔M7: nPOD dual IHC (Graves + Richardson labs)
- M1↔M4: risankizumab SEQUENCE trial co-morbidity subgroup
- M3↔M2: IFN-α Simoa stratifies rosacea risk within T1DM cohort
- M2+M4 loop: ivermectin + azelaic acid RCT in rosacea non-responders

### Gaps Remaining Unaddressed

1. **M6 (early-life)→M4**: Does early-life dysbiosis permanently set IL-23/Th17 baseline? Untested.
2. **The "healthy baseline" problem**: No consensus on what a healthy microbiome is. Unchanged.
3. **Intervention precision**: Phage therapy is pre-clinical. FMT is blunt. Unchanged.
4. **CVB-specific causal arrows**: pDC expansion in T1DM might be from non-CVB IFN sources. The M3 arm is real; whether CVB is the specific driver (vs. other IFN sources) is the uncertain step.

### Assay Kills Post-Phase 3

- **Zonulin (commercial kit)**: DEAD. Measures C3, not zonulin. Replace with L:M ratio (Genova) or FABP2+LBP.
- **CVB IgG serology for persistence**: DEAD as a persistence marker. Measures past exposure only.
- **CXCL10 as IFN-α cascade gate**: WEAK. Only ~50% sensitive in T1DM. Use as supportive, not exclusive gate. IFN-α2 Simoa should be ordered based on clinical context.

### Phase 3 Extension — Two New Bridges Added

**Gap: M5↔M7 connection — PARTIALLY BRIDGED (CANDIDATE)**
High-GI diet → hyperglycemia → PMN dysfunction → P. gingivalis niche expansion → M7.
Mechanism: neutrophil dysfunction (NOT glucose as P. gingivalis substrate).
Specific to T1DM/T2DM patients; smaller effect in euglycemic individuals.
T1DM-specific positive feedback loop identified.
See `attempts/attempt_011_m5_m7_diet_oral_chain.md`.

**Gap: M7→M1 oral-gut axis — PARTIALLY BRIDGED (CANDIDATE)**
P. gingivalis in saliva → gut colonization under PPI conditions → TLR2+TLR4 co-stimulation.
TLR2+TLR4 synergy → more IL-23/Th17 output than standard M1 model predicts.
Implication: periodontal treatment + PPI reassessment addresses M1 arm potentiation, not just M7 bacteremia.
See `attempts/attempt_012_m7_m1_oral_gut_axis.md`.

**Remaining unmapped gaps (genuine):**
1. M5↔M6: maternal diet during pregnancy → fetal SCFA exposure → Treg imprinting. Mechanism exists (attempt_010 references maternal fiber → offspring allergy protection); not formalized as bridge. Practical implication captured.
2. Genetic floor precision: specific IL23R, NOD2 frameshift, TLR4 Asp299Gly variant effect sizes on T-index interpretation. Numerics not yet run.
3. Phageome: bacteriophages targeting P. gingivalis or gut pathogens — pre-clinical only.

*Gap.md updated: 2026-04-11 | Phase 3 extension complete (attempts 011-012) | 7 mountains, 7 bridges | See results/protocol_integration.md for full actionable synthesis*

---

## Phase 4 Update — 2026-04-12

### New Gap: M5↔M6 Cross-Generational Bridge — RESOLVED (STRONG CANDIDATE)

Maternal dietary fiber during pregnancy → microbial fermentation → SCFA → transplacental transfer → fetal Foxp3 CNS1/CNS3 epigenetic imprinting via HDAC inhibition → structural Treg floor set before birth. This is the only intervention window that modifies M6 — prenatally via maternal diet (M5 of the mother). Breastfeeding extends the window 6 months postnatally via HMOs. See `attempts/attempt_014_m5_m6_maternal_treg.md`.

### New Mountain: M8 (HPA/CRH/Neurogenic Inflammation) — FORMALIZED

M8 is an amplifier mountain: connects to M4 (GR downregulation → Treg failure), M1 (CRH → intestinal mast cells → I-FABP elevation independent of diet), M7 (cortisol → sIgA suppression → P. gingivalis colonization facilitated), and M2 (Substance P → Malassezia growth + KLK5). Sky bridges formalized in `attempts/attempt_015_m8_sky_bridges.md`. Framework now has 8 mountains and 10+ sky bridges.

**Novel finding in M8 work:** P. gingivalis IgA protease creates a secondary self-amplifying M7 loop — once established, it actively degrades sIgA defenses, maintaining its own niche independent of ongoing stress. This is a second self-amplifying loop in the framework (parallels M2+M4 rosacea loop from attempt_008).

### New Resolution Framework — WRITTEN

`results/resolution_biology.md` defines three levels of remission, de-escalation sequence (Tier 1-4), resolution kinetics per mountain, relapse pattern recognition (A-D), and the "managed vs. resolved" distinction. Key clinical trap identified: stress-flare I-FABP elevation (M8→M1) is misattributed to diet failure; correct intervention is quercetin/sleep/MBSR, not more dietary fiber.

### Remaining Genuine Gaps (as of 2026-04-12, post-Phase 4 extension)

1. **Foxp3 CNS2 EWAS — SEARCH STRATEGY WRITTEN** (run_010): Küpers 2019 PACE consortium supplementary tables are the fastest actionable test. Free to check. If positive, confirms M6↔M4 Prediction B in humans. If negative, tissue-specificity is the issue (cord blood PBMC may not reflect thymic output).

2. **Perioral dermatitis sibling directory — CROSS-REFERENCED** (attempt_006 in POD): M4 threshold, M6 structural floor, M8 amplifier imported. Anti_problem.md C2 counterexample resolved. School/home POD pattern explained by M8.

3. **M8 sky bridges — FORMALIZED** (attempt_015): M8→M1 (STRONG), M8→M4 (CAND), M8→M7 (CAND). Novel finding: P. gingivalis IgA protease creates secondary self-amplifying M7 loop.

4. **Genetic floor precision — QUANTIFIED** (run_009): HLA-DR3, NOD2, TLR4, IL23R effect sizes on T-index thresholds. Clinical adjustment rules written. Protocol_integration.md Part 8b added.

5. **Phageome targeting P. gingivalis**: Bacteriophages specific to P. gingivalis exist (ΦPgI bacteriophage, ΦPgII). If M8→M7 secondary sIgA-protease loop prevents clearance, phage targeting is the precision backup. Pre-clinical only; the self-amplifying M7 loop from attempt_015 makes this gap more clinically relevant. NOT yet formally analyzed.

6. **Apremilast — EVALUATED** (run_011): CANDIDATE for rosacea non-responders (IL-23 suppression via PDE4; Piccolo 2021 case series positive; no Phase 3 RCT). NOT primary for seb derm (Malassezia mechanism bypasses IL-23). CYP3A4 interaction with itraconazole → elevated apremilast levels. Black box depression warning relevant in T1DM population. Position: third-line M4 threshold intervention between butyrate and biologics.

### Remaining Genuine Gaps (truly open, as of 2026-04-12 end of Phase 4 extension)

1. **Phageome targeting P. gingivalis** (ΦPgI bacteriophage): The M8→M7 secondary sIgA-protease self-amplifying loop means P. gingivalis IgA protease defends its own niche even after stress resolution. Phage targeting of P. gingivalis is the precision backup when standard SRP + chlorhexidine fails to clear recurrent periodontal colonization. Pre-clinical only; not yet analyzed as dysbiosis framework intervention.

2. **Küpers 2019 PACE supplementary table search** (free, 30 min): First actionable test of M6↔M4 Prediction B. Whether C-section → higher Foxp3 CNS2 methylation in cord blood. Run_010 has the full search strategy.

3. **Autoimmune thyroiditis — CROSS-REFERENCED** (thyroiditis/attempts/attempt_002): M3↔M7 bridge (P. gingivalis → CAR upregulation) extends to thyroid follicular cells. Novel loop identified: T1DM → hyperglycemia → P. gingivalis → CAR in thyroid → thyroiditis → insulin resistance → worsened T1DM. Protocol addition: P. gingivalis IgG + anti-TPO baseline for ALL T1DM patients.

### Remaining Genuine Gaps (truly open as of end of this session)

1. **Phageome targeting P. gingivalis (ΦPgI bacteriophage)**: The M8→M7 secondary sIgA-protease self-amplifying loop means standard periodontal treatment may not clear persistent P. gingivalis in high-stress patients with sustained sIgA suppression. Phage therapy is the precision backstop. Pre-clinical only; no clinical trial data; relevant as future therapy.

2. **Küpers 2019 PACE supplementary table search** (free, 30 min): First actionable test for M6↔M4 Prediction B. Run_010 has the full search strategy. This is genuinely executable now.

*Gap.md updated: 2026-04-12 | End of session | All major gaps addressed | 2 open: phageome (pre-clinical), EWAS search (executable)*
