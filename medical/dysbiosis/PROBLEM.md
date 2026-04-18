# Dysbiosis — The Umbrella Category

## The Problem

**Dysbiosis is the imbalance of a host-associated microbial community — gut, skin, oral, nasal, vaginal, ocular surface, or virome — that is associated with or drives disease.** It is not a single disease. It is the shared upstream structural failure behind a wide cluster of modern chronic conditions that do not fit the classical germ-theory "one pathogen, one disease" model.

This directory exists because multiple diseases in `../` (the medical directory) are **site-specific manifestations of the same dysbiosis mechanism**, and treating them as independent problems obscures the shared cause. Cross-referenced conditions already in this repo:

| Site | Condition | Directory |
|------|-----------|-----------|
| **Gut** | T1DM (autoimmune initiation) | `../t1dm` |
| **Skin (sebaceous)** | Perioral dermatitis | `../perioral_dermatitis` |
| **Skin (sebaceous)** | Seborrheic dermatitis (user, active) | — |
| **Skin (sebaceous)** | Rosacea (user, suspected) | — |
| **Skin (follicular)** | Eczema / atopic dermatitis | `../eczema` |
| **Skin (follicular)** | Psoriasis | `../psoriasis` |
| **Ocular surface** | Chalazion / MGD / Demodex blepharitis | — |
| **Virome (pancreatic)** | CVB persistence → T1DM | `../t1dm`, `cvb_*` files |
| **Systemic** | ME/CFS (suspected viral + gut) | `../me_cfs` |
| **Gut** | Infertility pathways (gut → hormonal) | `../infertility` |

## Status: MECHANISTICALLY KNOWN AT SURFACE, CAUSALLY UNRESOLVED

We know **what dysbiosis IS** (measurable: 16S, shotgun metagenomics, metatranscriptomics, virome-enriched sequencing). We know the correlations between specific dysbiosis profiles and specific diseases. What remains open:

1. **Causation direction** — does dysbiosis cause disease, or does inflammation/host state cause dysbiosis? Or both, with feedback?
2. **Intervention precision** — probiotics, FMT, antibiotics, diet — all perturb the system, but none reliably restore a "healthy" state because the target is underdefined.
3. **Host threshold problem** — the same microbe can be commensal in one host and pathogenic in another. "Dysbiosis" is host-specific, not microbe-specific.
4. **Substrate shift** — modern diet (insulin/IGF-1 driven sebum output, low fiber, glycemic load) changes the SUBSTRATE the microbes live on, not just which microbes are there.

## Phase 0 Shape-Check (sigma v7)

Running the Phase 0 questionnaire:

1. **Is there a known mechanism?** Partially. We know dysbiosis correlates with disease. We do NOT know the causal arrow for most pairings. → **Mechanistic wall present.**
2. **Do effective treatments/solutions exist?** Partial. FMT works for C. diff. Probiotics have mixed results. Ketoconazole works for seb derm. Ivermectin works for Demodex. There is no "reset dysbiosis" universal treatment. → **Treatment exists for narrow niches, not for the broad condition.**
3. **Can the wall be crossed by producing new information or tools?** Yes. Better strain-level resolution, better intervention targeting, better biomarkers for host-microbe threshold. → **Technological + mechanistic wall, not behavioral.**
4. **Does crossing require changes in recurring human action?** Partial. Diet/lifestyle matter but are not the main wall — the science is the main wall.
5. **Who has tried to cross this wall already?** Huge field. Microbiome research 2010-present. Correlations are well-mapped. Causal arrows + mechanistic precision are the frontier.

**Shape classification**: MECHANISTIC + TECHNOLOGICAL wall, with behavioral contributors. Standard sigma pipeline applies, with the known limit that **some dysbiosis research will hit the causal-direction wall** — a different methodology (RCTs, Koch's-postulate-style challenge studies, gnotobiotic animal models) is required beyond correlation. The method can produce gap maps and rule out hypotheses; crossing to mechanistic proof requires wet-lab work the method does not do.

This problem is **NOT a behavioral wall** (unlike POD, where the treatment works and compliance is the blocker). The wall here is real mechanism-scale uncertainty.

## Key Biology

| Component | Role in dysbiosis |
|-----------|-------------------|
| **Firmicutes:Bacteroidetes ratio** | Classical gut dysbiosis marker; elevated in obesity, metabolic syndrome |
| **Butyrate-producing bacteria** (*Faecalibacterium*, *Roseburia*) | Reduced in IBD, T1DM, MS — butyrate induces FOXP3+ Tregs via HDAC inhibition |
| **Akkermansia muciniphila** | Mucin-degrading; reduced in obesity, T2DM, IBD; emerging therapeutic target |
| **LPS translocation** | Gram-negative cell wall fragment crossing a leaky gut barrier → systemic NF-κB activation |
| **Malassezia globosa / restricta** | Lipid-dependent yeast; universal skin commensal; overgrowth → seb derm, dandruff, Malassezia folliculitis |
| **Demodex folliculorum / brevis** | Universal skin mite; overgrowth → rosacea, POD, blepharitis, chalazion |
| **Cutibacterium (formerly Propionibacterium) acnes** | Follicular bacterium; strain-level divergence drives acne vs commensal behavior |
| **Staphylococcus aureus (skin)** | Overgrows in atopic dermatitis; superantigen production drives T cell expansion |
| **Candida albicans** | Gut + mucosal; overgrowth drives systemic inflammation and cross-reactive autoimmunity |
| **Coxsackievirus B (virome)** | Persistent 5' UTR-deleted variant in pancreatic islets → T1DM trigger |
| **Epstein-Barr virus (virome)** | Latent reactivation → MS, CFS, lupus, nasopharyngeal carcinoma |
| **Cathelicidin (LL-37)** | Antimicrobial peptide; abnormal KLK5 cleavage produces pro-inflammatory fragments (rosacea) |
| **TLR2 / TLR4 / NLRP3** | Pattern recognition receptors; dysbiosis signals through these to produce inflammation |
| **IgA (mucosal)** | Secreted antibody; shapes microbiome composition; deficient IgA correlates with autoimmune risk |

## The Disease Cascade (Generic)

1. **Genetic susceptibility** (HLA risk alleles, sebaceous-spectrum genes, barrier-protein variants)
2. **Environmental trigger** (high glycemic diet, antibiotic exposure, viral infection, topical cosmetic/oil, C-section delivery, formula vs breastfeeding)
3. **Substrate shift** (more sebum, altered gut mucus, disrupted barrier function)
4. **Microbial community reorganization** (loss of diversity, overgrowth of specific taxa, virome expansion)
5. **Host threshold crossed** (TLR/NLRP3 activation, barrier permeability, cytokine production)
6. **Local inflammation** (site-specific disease: chalazion, seb derm, T1DM islet damage)
7. **Systemic spread** (LPS translocation, Treg depletion, autoimmunity initiation)
8. **Chronic loop** (inflammation damages barrier → more microbial translocation → more inflammation)

## The Multiple Mountains

### Mountain 1 — Gut dysbiosis drives systemic inflammation (LPS / leaky gut)
**Claim:** Gut permeability increases → LPS crosses gut wall → binds TLR4 → systemic NF-κB activation → sets the inflammatory tone that lowers thresholds for all other site-specific diseases.
**Evidence:** Zonulin elevation in celiac, T1DM. LPS detectable in plasma of obese, metabolic-syndrome, and T2DM patients. Butyrate-producer loss in IBD, T1DM, MS.
**Wall:** distinguishing LPS translocation from LPS-from-local-infection. Plasma LPS assays are imprecise. Zonulin controversy (is it a real marker?).
**Status:** PARTIALLY VALIDATED. See `attempts/attempt_001_leaky_gut.md` (to be written).

### Mountain 2 — Skin dysbiosis drives local inflammatory dermatoses
**Claim:** Malassezia, Demodex, and C. acnes overgrowth — driven by sebum substrate increase — directly cause seb derm, rosacea, POD, chalazion, acne.
**Evidence:** Topical antifungal/antiparasitic monotherapy resolves specific conditions. Malassezia density correlates with seb derm severity. Demodex density correlates with rosacea severity (3-6× vs controls).
**Wall:** Why do SOME high-density carriers not get disease? Host threshold variability. See Mountain 4.
**Status:** VALIDATED for specific site/organism pairs. Cross-validated by treatment response (ketoconazole, ivermectin, metronidazole).

### Mountain 3 — Virome dysbiosis drives chronic autoimmune/inflammatory disease
**Claim:** Persistent low-replication viruses (CVB in islets, EBV in B cells, HHV-6/7 in CNS) maintain chronic inflammation that presents as autoimmunity.
**Evidence:** CVB 5' UTR-deleted variants detected in T1DM pancreas. EBV causal evidence for MS (2022 Bjornevik study). Post-COVID long-tail syndromes suggesting viral persistence.
**Wall:** Detecting low-titer persistent virus is hard. Standard PCR doesn't find the dormant forms. Requires deep sequencing + enrichment.
**Status:** STRENGTHENING. CVB-T1DM link is increasingly accepted. User has implemented CVB protocol targeting this mountain explicitly.

### Mountain 4 — Host-microbe threshold (the tolerance problem)
**Claim:** Dysbiosis is defined by the HOST's tolerance threshold, not by microbial absolute numbers. Same microbe at same density = disease in one person, commensal in another. Genetic susceptibility + immune tone set the threshold.
**Evidence:** Demodex is universal; only ~5-10% of carriers get rosacea. Malassezia is universal; ~10-30% get seb derm. C. acnes is on everyone; acne is age-dependent and variably expressed.
**Wall:** We don't have assays for "inflammatory threshold" separate from "inflammation is happening." Cathelicidin processing, KLK5 activity, NLRP3 responsiveness are candidate biomarkers but not clinically deployed.
**Status:** FRONTIER. This is where the field is pushing.

### Mountain 5 — Modern diet alters the microbial substrate
**Claim:** High glycemic / dairy / low-fiber Western diet → chronically elevated insulin/IGF-1 → increased sebum output with altered fatty acid composition AND reduced gut microbial diversity → substrate shift that selects for pathogenic overgrowth across sites.
**Evidence:** Kitavan islanders (Papua New Guinea, traditional diet): documented zero-acne cohort of 1200 including 300 adolescents (Cordain et al. 2002). Inuit pre-Westernization: near-zero sebum dermatoses. Rates climb toward Western norms within a generation of dietary transition.
**Wall:** The dietary intervention requires compliance across a lifetime. The mechanism involves a network (insulin, IGF-1, SREBP-1c, sebum composition, gut microbiome, immune tone) — no single pharmaceutical target replicates it.
**Status:** EPIDEMIOLOGICALLY VALIDATED at population level. Individual-level causal testing is hard.

### Mountain 6 — Early-life microbiome assembly shapes lifelong disease risk
**Claim:** The first 3 years establish a microbiome that is stable for life. C-section delivery, formula feeding, early antibiotic exposure, and low-diversity environments (overly sterile) produce a microbiome missing key colonizers. The downstream disease risk appears 20-40 years later.
**Evidence:** C-section correlates with asthma, allergy, T1DM, obesity. Antibiotic exposure in first 2 years correlates with IBD, asthma. Amish vs Hutterite study (same genetics, different farm exposure, very different allergic disease rates).
**Wall:** The intervention window has already closed for adults. The payoff of microbiome-aware pediatric care is 40 years out.
**Status:** VALIDATED epidemiologically. Intervention implications are pediatric-only.
**Phase 3 update:** Rudensky lab (Science 2015) confirmed early-life Tregs are a distinct NON-REDUNDANT long-lived pool — M6 events set a STRUCTURAL TREG FLOOR that adult interventions cannot replace, only supplement. Shared gene-regulation patterns between C-section delivery and islet autoimmunity (PMID 31000755) — M6→M3 link. See `attempts/attempt_010_m6_m4_treg_window.md`.

### Mountain 7 — Oral dysbiosis propagates to distant tissue via bacteremia
**(Added in Phase 3 — was not in original problem scaffold)**

**Claim:** P. gingivalis, the dominant periodontal pathogen, translocates to distant tissues via bacteremia. In pancreatic islets specifically, it localizes intranuclearly in beta cells, activates TLR2, produces local IL-1β/IL-6/TNF-α, and upregulates CAR (Coxsackievirus Adenovirus Receptor) via cytokine-mediated signaling. This makes beta cells more susceptible to CVB infection, creating a synergistic co-infection mechanism for T1DM initiation.

**Evidence:** PMC7305306 (Graves lab 2020): P. gingivalis physically detected in pancreatic beta cells in mice and humans; correlates with bihormonal cell emergence. PMC5129002: CAR upregulated by proinflammatory cytokines in T1DM islets. PMID 31351339: P. gingivalis LPS → TLR2 → Th17 in human cells. Shared HLA loci: periodontitis + T1DM (Liu et al. 2023, Frontiers Genetics).

**Wall:** Combined P. gingivalis + CVB + T1DM mechanism not yet in published literature. Requires nPOD dual IHC test (Graves lab + Richardson lab collaboration).

**Status:** STRONG CANDIDATE. See `attempts/attempt_006_m3m7_local_coinfection.md`.

**Additional bridges from M7 (Phase 3 extension):**
- M7→M1 oral-gut colonization: P. gingivalis reaches gut via swallowed saliva (~10^10/day); under PPI use, acid kill is reduced. Gut P. gingivalis activates TLR2; TLR2+TLR4 co-stimulation is synergistic for IL-23/Th17 — potentiates M1 arm input to M4. See `attempts/attempt_012_m7_m1_oral_gut_axis.md`.
- M5↔M7 upstream link: hyperglycemia (from poor glycemic control/high-GI diet) → impaired PMN → P. gingivalis niche expansion. T1DM-specific positive feedback loop: T1DM → hyperglycemia → P. gingivalis → CAR priming → CVB → more T1DM. See `attempts/attempt_011_m5_m7_diet_oral_chain.md`.

## Integrated Model

Mountains do not compete — they compose. The integrated model:

```
 Early-life assembly failure (M6) ──┐
 Modern diet substrate shift (M5) ──┤
                                    ├──> Altered community composition (gut + skin + virome)
 Genetic susceptibility ────────────┤                    │
                                    │                    ▼
                                    │     Host threshold (M4) — is composition pathogenic
                                    │         for THIS person's immune calibration?
                                    │                    │
                                    │     ┌──────────────┼──────────────┐
                                    ▼     ▼              ▼              ▼
                                Gut wall Skin disease  Virome          Systemic
                                dysfunc. (M2)          persistence     autoimm.
                                (M1)                   (M3)            initiation
                                    │                                    │
                                    └────────────────────────────────────┘
                                                    │
                                            Chronic feedback loop
                                            (inflammation → barrier
                                             damage → more dysbiosis)
```

## The Testable Predictions

If the **host threshold** framing is correct (M4):
- Interventions that calm innate immunity (NLRP3 blockade, cathelicidin/KLK5 modulation, NF-κB suppression) should improve dysbiosis-linked disease WITHOUT changing microbial composition
- **The user's CVB protocol tests this directly** — it targets NF-κB, NLRP3, autophagy (host side) more than microbial elimination. Observed skin improvement validates the prediction.

If **substrate shift** is correct (M5):
- Dietary intervention (low glycemic, reduced dairy, adequate fiber) should shift microbial composition AND resolve symptoms on timescales of weeks
- Populations transitioning to Western diet should show rising dysbiosis-linked disease rates within 1 generation ✓ (validated)

If **early-life assembly** is dominant (M6):
- Adult interventions should have smaller effects than pediatric prevention
- Sibling/twin studies should show early-life-environment > adult-environment for disease risk

If **virome persistence** is dominant (M3):
- Antiviral + immune-modulatory combined therapy should outperform either alone
- Viral reservoir detection should predict disease activity

## Known Treatment Ladders (What Works, By Site)

### Gut dysbiosis
- **Confirmed**: FMT for C. difficile (>90% cure rate); gluten elimination in celiac; lactose avoidance in intolerance
- **Probable**: High-fiber diet for butyrate producer recovery; Akkermansia-favoring compounds (cranberry polyphenols, pomegranate); Saccharomyces boulardii for antibiotic-associated
- **Experimental**: FMT for UC, autism, metabolic syndrome; phage therapy for specific bacterial overgrowth

### Skin dysbiosis
- **Seb derm**: ketoconazole 2% shampoo, zinc pyrithione, selenium sulfide — all topical antifungal
- **Demodex**: topical ivermectin (Soolantra), tea tree oil (Cliradex), lotilaner (Xdemvy for blepharitis)
- **Acne**: benzoyl peroxide, topical retinoids, doxycycline anti-inflammatory dose
- **Atopic derm**: emollients, barrier repair, intermittent topical steroid (rebound risk), tacrolimus/pimecrolimus

### Virome
- **CVB**: no approved antiviral; user's protocol blocks OSBP cholesterol delivery + NLRP3 + NF-κB indirectly
- **EBV**: no good antivirals; valacyclovir has limited effect; emerging EBV vaccines (Moderna trial ongoing)
- **HHV reactivation**: valacyclovir, famciclovir, foscarnet in severe cases

### Host side (threshold modulation)
- Vitamin D3 + K2 (cathelicidin regulation)
- Omega-3 EPA/DHA (resolvins, NF-κB suppression)
- Zinc (innate immune support)
- BHB ketones (NLRP3 direct block)
- NAC (glutathione, ROS suppression)
- Intermittent fasting (autophagy, mTOR)
- Butyrate / tributyrin (Treg induction)
- Wim Hof Method (epinephrine → β-arrestin-2 → IκBα stabilization → attenuated NF-κB activation, per Kox 2014 *PNAS* PMID 24799686)
- Cold exposure (norepinephrine, NK mobilization)

**Note:** the user's CVB protocol (in the local CVB Protocol Schedule PDF) is a multi-site dysbiosis intervention protocol that happens to be framed as CVB-targeted. It addresses Mountains 3, 4, and 5 simultaneously.

## Open Questions

1. Is there a **single measurable biomarker** of "dysbiosis" across sites, or is dysbiosis always site-specific?
2. How many dysbiosis-linked diseases share a **final common pathway** (cathelicidin? NLRP3? NF-κB? LPS?)?
3. Is the **causal direction** genuinely undefinable (bidirectional feedback), or is there a primary driver that current methods can't detect?
4. Can **virome dysbiosis** be fully characterized with current sequencing depth, or are persistent low-titer viruses systematically missed?
5. What is the **minimum intervention set** that reliably restores healthy host-microbe equilibrium across multiple sites?
6. Does **the gut-skin axis** operate via systemic inflammation, direct metabolite transport, or immune education?
7. Why do some populations (Kitavan, Hadza, Yanomami) show **near-zero dysbiosis-linked disease** on traditional diets — is the protection from diet, microbiome, genetics, or all three?

## See Also

- `gap.md` — mechanistic gaps in more detail
- `THEWALL.md` — the convergent obstruction
- `anti_problem.md` — what would make dysbiosis worse (iatrogenic patterns)
- `attempts/` — numbered mountain attempts (to be populated)
- the local CVB Protocol Schedule PDF — the user's active multi-target dysbiosis intervention
- `../t1dm`, `../perioral_dermatitis`, `../eczema`, `../psoriasis`, `../me_cfs` — site-specific instances of the same umbrella problem
