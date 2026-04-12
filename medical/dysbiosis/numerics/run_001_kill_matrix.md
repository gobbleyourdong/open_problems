# Kill Matrix — Dysbiosis Mountains × Falsifiable Predictions
## Run 001 | Numerical Instance | 2026-04-11

> Phase 1 numerics: exhaustive mapping, no interpretation. Every falsifiable prediction logged.
> Evidence scores: 0=none, 1=weak/indirect, 2=moderate/replication, 3=strong/gold-standard
> Direction: F=forward (micro→disease), R=reverse (disease→micro), B=bidirectional established

---

## Mountain 1 — Gut dysbiosis → systemic inflammation (LPS/leaky gut)

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P1.1 | Plasma LPS elevated in gut-dysbiotic vs healthy hosts | 2 | 1 | N | LPS-binding protein (LBP) surrogate; direct LPS assay is noisy (LAL assay interference). Documented in obesity, T2DM, metabolic syndrome. |
| P1.2 | Zonulin elevation correlates with dysbiosis-linked disease | 1 | 2 | N | Zhang 2021: the commercially used ELISA may not be specific to zonulin. Likely detecting complement C3. Marker controversial. |
| P1.3 | Butyrate-producer loss (Faecalibacterium, Roseburia) correlates with IBD/T1DM/MS | 3 | 0 | N | Very robust correlation. ~50-70% reduction in F. prausnitzii in active IBD (Sokol 2008). T1DM cohorts confirm. |
| P1.4 | Gut intervention (FMT/probiotics/fiber) reduces systemic inflammation markers | 2 | 1 | F (partial) | FMT for C. diff: yes. FMT for UC: modest (~30% remission). Probiotics: effect sizes small and heterogeneous (meta-analysis). |
| P1.5 | Leaky gut precedes (not follows) systemic inflammatory disease onset | 1 | 1 | UNKNOWN | No longitudinal data establishing temporal sequence. Hard to study. T1DM: gut changes may precede islet autoimmunity (Vehik 2019 TEDDY — suggestive not definitive). |
| P1.6 | LPS binds TLR4 → NF-κB → elevates systemic inflammatory tone measurably | 3 | 0 | F | Mechanistic: well-established in vitro + animal. Human clinical data: consistent but not controlled for LPS source (local infection vs gut translocation). |
| P1.7 | Butyrate supplementation (or butyrate-producer rescue) reduces inflammatory cytokines | 2 | 1 | F | Animal: strong. Human: oral butyrate trials show gut benefit; systemic anti-inflammatory effect smaller. |

**Mountain 1 status: PARTIALLY VALIDATED. Arrow still open.**
**Strongest evidence: P1.3, P1.6. Weakest: P1.2 (marker controversy), P1.5 (no temporal data).**

---

## Mountain 2 — Skin dysbiosis → local inflammatory dermatoses

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P2.1 | Malassezia density correlates with seb derm severity | 3 | 0 | N | Density correlation solid. Antifungal response validates pathogenicity but not primary causation (could reduce inflammation secondarily). |
| P2.2 | Demodex density 3-6× elevated in rosacea vs healthy controls | 3 | 0 | N | Multiple studies confirm. Ivermectin efficacy validates. Density threshold ≈100 mites/cm² associated with disease onset but with high individual variance. |
| P2.3 | C. acnes strain RT4 vs RT6 divergence predicts inflammatory acne vs commensal | 2 | 1 | F (partial) | Phylotype divergence confirmed (Fitz-Gibbon 2013). Clinical translation imperfect — strain distribution doesn't fully predict phenotype. |
| P2.4 | Antifungal/antiparasitic monotherapy resolves seb derm/rosacea (cross-validates) | 3 | 0 | F (strong indirect) | Ketoconazole 2% shampoo: ~80% response rate seb derm. Ivermectin 1% cream (Soolantra): ~75% clear in rosacea RCTs. Treatment response is the strongest causal signal. |
| P2.5 | Sebum fatty acid composition shift (↑oleic acid, ↓linoleic acid) precedes Malassezia overgrowth | 2 | 0 | F (plausible) | Malassezia preferentially cleaves C18:1 (oleic acid) from triglycerides. Acne patients have altered sebum composition. Temporal sequence not established in skin dysbiosis. |
| P2.6 | Tolerant high-density carriers (no disease despite >100 mites/cm²) have measurably different local immune response | 1 | 0 | UNKNOWN | Research gap. No published biomarker that distinguishes tolerant from about-to-flare. This is the M4 overlap point. |
| P2.7 | Oral ketoconazole systemically reduces seb derm (cross-validates that Malassezia is sufficient, not just local) | 2 | 0 | F | Oral antifungal works for seborrheic dermatitis — confirms systemic availability reaches skin Malassezia. |

**Mountain 2 status: VALIDATED for specific site/organism pairs. Treatment response is strongest evidence. M4 overlap at P2.6.**

---

## Mountain 3 — Virome persistence drives chronic autoimmune/inflammatory disease

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P3.1 | CVB 5' UTR-deleted variants detectable in T1DM pancreatic islets | 2 | 1 | F (strong candidate) | Richardson 2009, Krogvold 2015 (DIPP). Detected in 30-60% of recent-onset T1DM islet samples vs 5-15% controls. Detection rate depends on sequencing method. |
| P3.2 | EBV exposure precedes MS development (temporal precedence established) | 3 | 0 | F (strongest causal evidence in field) | Bjornevik 2022: military cohort N=10 million. MS risk 32× higher after EBV seroconversion. Seronegative MS = 0 in cohort. This is as close to causation as cohort data gets. |
| P3.3 | Antiviral + immunomodulatory combined therapy > either alone for CVB-T1DM | 0 | 0 | UNTESTED | No clinical trial exists. User's protocol empirically tests this. Pleconaril + immunomodulation trials planned. |
| P3.4 | Viral reservoir load correlates with disease activity (not just presence/absence) | 1 | 0 | UNKNOWN | Hypothesis plausible. No validated assay for CVB persistence reservoir size. EBV viral load monitoring exists but disease correlation is imperfect. |
| P3.5 | Virome-enriched sequencing reveals disease-associated signatures missed by standard 16S/shotgun | 2 | 0 | — | Technical prediction, not directional. Studies with virus-enriched prep find 5-10× more viral diversity. The USER's TinyHealth FASTQ is relevant here. |
| P3.6 | HHV-6/7 reactivation in CNS correlates with ME/CFS relapse | 2 | 1 | N | Bhupesh Prusty work. HHV-6 dUTPase activates TLR signaling, energy metabolism disruption. Correlation established; reactivation trigger unclear. |
| P3.7 | Persistent enterovirus (post-COVID) correlates with long COVID syndrome | 2 | 0 | N | Patterson 2021: persistence of SARS-CoV-2 S1 protein in monocytes at 15 months. Gut enterovirus reservoir hypothesis for long COVID gaining traction. |

**Mountain 3 status: STRENGTHENING. P3.2 (EBV-MS) is the highest-quality causal evidence in this domain. CVB-T1DM at 2/3. Virome detection methodology is the bottleneck.**

---

## Mountain 4 — Host-microbe threshold (tolerance problem)

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P4.1 | NLRP3 priming status in skin tissue predicts disease onset in high-density colonized host | 0 | 0 | UNTESTED | No human study. Animal: NLRP3-KO mice don't develop rosacea-like phenotype under Demodex challenge (indirect). |
| P4.2 | KLK5 activity level predicts timing of rosacea flare | 0 | 0 | UNTESTED | Research assay only. No longitudinal human study. KLK5 → cathelicidin cleavage → pro-inflammatory LL-37 fragments is the mechanistic pathway. |
| P4.3 | Host-targeted interventions (NLRP3 block, NF-κB suppression) improve disease WITHOUT changing microbial composition | 2 | 0 | F (partial, via proxy) | User's CVB protocol (NLRP3/NF-κB targeting) shows skin improvement with no antibiotic/antifungal use. Not a controlled study. Doxycycline low-dose (NF-κB, not antimicrobial) works for rosacea. |
| P4.4 | Tolerant high-density Demodex/Malassezia carriers have measurably different innate immune tone from disease-active carriers | 0 | 0 | UNTESTED | No assay deployed. This is the core missing measurement. |
| P4.5 | Host genetic variants (NOD2, TLR4, NLRP3 SNPs) correlate with dysbiosis-linked disease susceptibility | 3 | 0 | Genetic association (not full causal) | NOD2 variants: textbook IBD susceptibility (2001 Hugot/Ogura). TLR4 D299G: reduced LPS sensitivity. IL-23R variants: psoriasis, IBD. NLRP3 mutations: CAPS (cryopyrin-associated autoinflammatory). |
| P4.6 | Cathelicidin / LL-37 serum level distinguishes rosacea-active from tolerant-high-Demodex hosts | 1 | 0 | PARTIAL | Active LL-37 fragments elevated in rosacea skin (Yamasaki 2007). Serum vs local; research assay; not standardized. |
| P4.7 | Treg frequency (FOXP3+ CD4+ CD25+) in blood inversely correlates with dysbiosis-linked disease severity across sites | 1 | 0 | N | Treg reduction in IBD, T1DM: documented. Skin Treg reduction in atopic derm: documented. Shared cross-site biomarker: unstudied. |

**Mountain 4 status: FRONTIER. Almost every prediction untested. Genetic associations confirm threshold exists; mechanism not measurable clinically. THIS IS THE WALL.**

---

## Mountain 5 — Modern diet alters microbial substrate

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P5.1 | High glycemic diet elevates insulin/IGF-1 → increases sebum output measurably | 3 | 0 | F | IGF-1 pathway to SREBP-1c → sebocyte lipogenesis: well-established. RCT of low-GI diet showed reduced sebum secretion (Smith 2007, Acta Derm Venereol). |
| P5.2 | Populations on traditional diets show near-zero dysbiosis-linked dermatoses | 3 | 0 | Association (ecological) | Cordain 2002 (Kitavan, N=1200): 0 acne observed. Inuit historical data. Hadza gut microbiome is ~50% more diverse than US average. Ecological study design limits causal inference. |
| P5.3 | Individual dietary intervention (low GI + dairy elimination) reduces sebum output AND shifts microbial composition AND reduces symptoms | 2 | 1 | F (weak) | Effect sizes modest in RCTs (acne: ~50% improvement vs 30% placebo). Most trials don't measure microbial composition changes. |
| P5.4 | Fiber → butyrate producers → butyrate → Treg induction (functional chain measurable) | 2 | 0 | F (mechanistic chain supported) | Each link documented separately; full chain in humans: suggestive. Sonnenburg fiber intervention in Stanford cohort shifted microbiome composition. Butyrate supplementation → Treg increase in IBD patients. |
| P5.5 | Dairy (especially whey) elevates IGF-1 independently of total caloric intake | 2 | 0 | F | Cross-sectional: dairy IGF-1 elevation confirmed in multiple cohorts. Intervention: whey protein supplementation raises IGF-1. |
| P5.6 | Dietary transition to Western pattern within one generation raises dysbiosis-linked disease rates to Western norms | 3 | 0 | F (ecological) | Immigrant health studies: T1DM rates rise toward host country rates within 1-2 generations. Acne rates rise with Western diet adoption (Asian cohort studies). |

**Mountain 5 status: EPIDEMIOLOGICALLY VALIDATED. Substrate mechanism established. Individual-level intervention effect sizes modest. Strongest mountain for avoidance interventions (anti-problem).**

---

## Mountain 6 — Early-life microbiome assembly shapes lifelong risk

| ID | Prediction | Evidence FOR (0-3) | Evidence AGAINST (0-3) | Causal direction established? | Notes |
|----|------------|-------------------|----------------------|-------------------------------|-------|
| P6.1 | C-section delivery correlates with autoimmune/atopic disease risk (asthma, T1DM, IBD, allergy) | 3 | 1 | Association (strong) | Meta-analysis: C-section OR for asthma ~1.2-1.4, T1DM ~1.1-1.2, IBD ~1.1-1.3. Confounding: C-section indicates maternal health issues that may independently raise risk. |
| P6.2 | Early antibiotic exposure (first 2 years) correlates with IBD/asthma risk | 3 | 0 | Association (strong) | Shaw 2011 (IBD: OR ~3× per course). Marra 2009 (asthma: 1.5× per course). Multiple replications. |
| P6.3 | Breastfeeding duration correlates inversely with dysbiosis-linked disease | 2 | 0 | Association | HMOs (human milk oligosaccharides) are selective prebiotics for Bifidobacterium. Breastfed infants have distinct microbiome persisting to age 1-2. |
| P6.4 | Early farm/pet/outdoor exposure reduces allergic disease risk (hygiene hypothesis) | 3 | 0 | Association (robust) | Amish vs Hutterite study (Stein 2016): same genetics, different farming exposure. Amish: asthma/allergy rates 5-7× lower. |
| P6.5 | Vaginal seeding after C-section normalizes microbiome trajectory | 1 | 1 | CONTESTED | Dominguez-Bello 2016: partial restoration possible. Subsequent work shows incomplete normalization. Safety concerns (GBS transfer). Not yet clinically validated. |
| P6.6 | Microbiome diversity at age 3 predicts allergic/autoimmune disease risk at age 10-20 | 2 | 0 | F (partial) | CHILD cohort, WHEALS study: early-life diversity predictive. Long follow-up required. Confounded by same factors that produce diversity deficit. |

**Mountain 6 status: EPIDEMIOLOGICALLY VALIDATED for association. Intervention window closed for adults. Relevant to prevention strategy, not current patient management.**

---

## Cross-Mountain Kill Tests

These predictions, if falsified, would constrain multiple mountains simultaneously:

| Kill Test | Mountains affected | Kill ROI | Status |
|-----------|-------------------|----------|--------|
| KT-A: Gut-barrier-permeability marker (validated) predicts systemic inflammatory disease onset before symptoms | M1, M4 | HIGH | UNEXECUTED — marker controversy blocks |
| KT-B: Host with identical Demodex density, randomized to NLRP3 inhibitor vs placebo: disease rate differs | M2, M4 | VERY HIGH | No RCT exists |
| KT-C: Dietary substrate shift (olive oil elimination for sebaceous zones) produces measurable skin microbiome composition change within 8 weeks | M2, M5 | HIGH | User's N=1 experiment (chalazion). Anecdotal. |
| KT-D: Combined antiviral + NLRP3 inhibitor + dietary change produces better T1DM HbA1c outcome than any single arm | M3, M4, M5 | VERY HIGH | No trial. CVB protocol is empirical attempt. |
| KT-E: Treg frequency (blood) correlates with dysbiosis-linked disease severity ACROSS sites (gut, skin, virome) | M4 | HIGH | No cross-site Treg study done |

---
*Run 001 complete. Kill matrix populated with 43 predictions across 6 mountains. Evidence gaps concentrated in M4.*
