# M4 Proxy Survey — Measuring the Unmeasurable Threshold
## Run 002 | Numerical Instance | 2026-04-11

> M4 (host-microbe threshold) is THE WALL. Direct measurement doesn't exist.
> This file maps every indirect proxy available with current tools.
> Format: proxy → mechanistic rationale → clinical availability → limitation → signal quality.

---

## The Threshold Architecture

The host-microbe threshold is NOT a single variable. It's a product of:

```
THRESHOLD = f(
    Genetic baseline (NOD2/TLR4/NLRP3 SNPs),     ← constitutional, fixed
    Immune calibration state (Treg/Th17 ratio),   ← dynamic, days-weeks
    Barrier function (KLK5, tight junctions),     ← dynamic, hours-days
    Nutrient status (D, zinc, omega-3),           ← dynamic, weeks
    Microbial metabolite input (butyrate, SCFAs)  ← dynamic, days
)
```

No proxy captures the full product. The goal: identify proxies that together give a reading of "threshold state" with the highest signal-to-noise across the clinically available space.

---

## Proxy 1: Vitamin D (25-OH-D serum)

**Mechanistic rationale:**
- Vitamin D receptor (VDR) on keratinocytes + immune cells
- VDR activation → CAMP gene expression → cathelicidin (LL-37) production
- VDR activation → FOXP3 expression → Treg induction
- VDR activation → IL-10 production → anti-inflammatory tone
- Low 25-OH-D → less cathelicidin → weakened antimicrobial defense → threshold shift

**Clinical availability:** Routine. LabCorp/Quest ~$30-60. 25-OH-D (calcidiol) not 1,25-OH-D.

**Reference ranges:** Optimal for immune function: 40-80 ng/mL. Most adults in range 15-40. Deficiency: <20 ng/mL.

**Disease correlations documented:**
- Rosacea: lower vitamin D in rosacea patients vs controls (Ekiz 2014)
- T1DM: low vitamin D in children prior to islet autoimmunity (TEDDY cohort)
- IBD: 70-80% of IBD patients are vitamin D deficient; supplementation → reduced relapse rate
- Atopic dermatitis: inverse correlation with vitamin D; supplementation trials mixed

**Signal quality for M4:** MODERATE
- Real signal for immune calibration but confounded by sun exposure, season, supplementation
- Directional: low D = higher threshold susceptibility
- Not specific to microbial threshold

**User relevance:** T1DM patient → high probability of D insufficiency. Supplement to 60-80 ng/mL is in the CVB protocol already. Monitoring level every 3 months = cheap M4 proxy.

---

## Proxy 2: Blood Treg Frequency (CD4+CD25+FOXP3+)

**Mechanistic rationale:**
- Tregs are the immune tolerance effectors — they actively suppress Th1/Th17/Th2 responses
- Low Treg frequency → lower tolerance threshold for microbial stimuli
- FOXP3 is the master transcription factor for Treg identity
- Treg function (not just number) matters; measuring FOXP3+ alone is imperfect

**Clinical availability:** Flow cytometry, immunology research labs. ~$200-500. Not routine primary care.

**Disease correlations documented:**
- IBD: Treg reduction 30-50% in active disease (Maul 2005)
- T1DM: Treg reduction in recent-onset; some studies show Treg dysfunction even when numbers normal
- Rosacea: NOT studied directly. Gap.
- Atopic dermatitis: peripheral Treg reduction in severe disease
- Psoriasis: Treg-Th17 imbalance well established

**Signal quality for M4:** MODERATE-HIGH
- Most mechanistically direct of the available proxies
- Blood Treg ≠ tissue Treg at the relevant site (gut, skin)
- FOXP3+CD25+ contaminated by activated effector T cells; FOXP3+CD25+CD127low is more specific
- A single measurement is a snapshot; need repeated measurements across disease states

**Cross-site prediction:** If M4 is real (threshold varies by host), rosacea + IBD + T1DM patients should all show lower Treg frequency vs matched tolerant-high-density carriers. This cross-site prediction is UNTESTED.

---

## Proxy 3: IL-10 / IL-17 Ratio (serum cytokines)

**Mechanistic rationale:**
- IL-10: anti-inflammatory, Treg output, dampens NF-κB
- IL-17A: pro-inflammatory, Th17 output, drives neutrophil recruitment, skin inflammation
- Ratio IL-10:IL-17 = tolerance/inflammation balance proxy
- Low ratio → Th17-skewed → lower threshold for inflammatory disease

**Clinical availability:** Cytokine panel, research labs (~$150-300 per panel). Not routine.

**Disease correlations:**
- IBD: IL-17 elevated, IL-10 reduced in active disease
- Psoriasis: IL-17 is THE driver; anti-IL-17 (secukinumab) is first-line
- T1DM: IL-17 elevated in recent-onset
- Rosacea: not well studied for serum cytokines; local skin IL-17 elevated

**Signal quality for M4:** MODERATE
- Cytokine half-lives short (minutes to hours in serum); samples must be processed immediately
- Snapshot only; elevated in active disease, normalized in remission
- More useful as disease activity marker than threshold marker
- TGF-β1 level would be more useful for threshold (Treg-inducing cytokine in tissues)

---

## Proxy 4: Fecal F. prausnitzii + Akkermansia muciniphila Abundance

**Mechanistic rationale:**
- F. prausnitzii → butyrate + MAM (microbial anti-inflammatory molecule) → FOXP3 Treg induction + direct NF-κB inhibition
- Akkermansia → mucin layer maintenance → gut barrier → less systemic LPS exposure → lower M1 inflammatory priming → less threshold sensitization
- Both are inversely depleted in almost all dysbiosis-linked diseases
- Their abundance is a proxy for: (butyrate-mediated Treg induction state) + (gut barrier integrity)

**Clinical availability:** 16S rRNA microbiome testing (TinyHealth, Genova GI-MAP, etc.) detects these at genus level. ~$200-400.

**Disease correlations:**
- F. prausnitzii: reduced 50-70% in active IBD (Sokol 2008); reduced in T1DM, MS, psoriasis; restoration correlates with remission in IBD
- Akkermansia: reduced in obesity, T2DM, IBD; increased by metformin treatment (possibly why metformin has anti-inflammatory properties beyond glucose control)

**Signal quality for M4:** MODERATE
- Compositional proxy for butyrate/Treg pathway status
- 16S is genus-level; can't distinguish F. prausnitzii strains with different anti-inflammatory capacities
- Quantitative: absolute abundance vs relative abundance matters; most clinical tests report relative
- Confounded by diet, antibiotics, recent illness

**USER RELEVANCE:** TinyHealth FASTQ — when processed, F. prausnitzii and Akkermansia relative abundance will be available. These are the two most M4-relevant microbial proxy reads from that test.

---

## Proxy 5: Omega-3 Index (EPA+DHA as % of RBC total fatty acids)

**Mechanistic rationale:**
- EPA/DHA → resolvin/protectin synthesis → active resolution of inflammation
- EPA competes with arachidonic acid for COX-2 → less PGE2 → less mast cell activation
- DHA → lipoxins → TGF-β-dependent Treg induction
- Low omega-3 index → impaired resolution capacity → inflammation resolves poorly → threshold effectively lower (takes less stimulus to cause persistent inflammation)

**Clinical availability:** LabCorp, Quest, Cleveland HeartLab. ~$50-100. Measures EPA+DHA in red blood cell membranes (reflects 2-3 month average intake).

**Reference range:** <4% = high cardiovascular risk. 4-8% = intermediate. >8% = target for chronic disease prevention. Most US adults: 4-5%.

**Disease correlations:**
- Not directly studied for dysbiosis-linked dermatoses
- Well studied for cardiovascular, depression, inflammatory arthritis
- Indirect: omega-3 supplementation reduces rosacea flushing (clinical observation, weak evidence)
- Animal: omega-3 supplementation restores resolvin production → skin barrier improvement in AD models

**Signal quality for M4:** LOW-MODERATE
- Resolution capacity proxy, not immune calibration proxy
- Easy to obtain + directly actionable (omega-3 supplementation)
- Not specific to microbial threshold

---

## Proxy 6: Serum Zinc

**Mechanistic rationale:**
- Zinc required for thymulin (thymic hormone → T cell maturation → Treg function)
- Zinc modulates NLRP3: zinc deficiency → enhanced NLRP3 activation (Guo 2015)
- Zinc required for NOD-like receptor signaling regulation
- Zinc deficiency → impaired cathelicidin function
- Zinc cofactor for DAO (diamine oxidase) → histamine degradation (histamine/mast cell axis)

**Clinical availability:** Serum zinc, routine. ~$20-40. Best measured after 8h fast.

**Optimal range:** 80-120 µg/dL. Common deficiency in modern diet: 15-40% of adults in marginal range.

**Disease correlations:**
- Acne: zinc sulfate 400mg/day equivalent to tetracycline 250mg tid in some RCTs (Michaelsson 1977 — old but replicated). Mechanism: anti-inflammatory (not antimicrobial).
- Rosacea: not well studied
- IBD: zinc deficiency in ~40-50% of IBD patients; zinc supplementation reduces diarrhea duration

**Signal quality for M4:** MODERATE
- NLRP3 modulation and cathelicidin function are directly on the threshold pathway
- Easy to measure and supplement
- Serum zinc is not a reliable indicator of total body zinc status (only 0.1% of zinc is in serum)
- Better marker: RBC zinc or hair zinc (not routine)

---

## Proxy 7: HsCRP (high-sensitivity CRP)

**Mechanistic rationale:**
- Steady-state systemic inflammatory tone
- Reflects the CURRENT state, not the THRESHOLD
- But: chronically elevated hsCRP → systemic NF-κB activation → lower threshold for site-specific disease

**Clinical availability:** Routine. ~$10-30.

**Interpretation:** <1.0 mg/L = low; 1-3 = intermediate; >3 = high. For chronic disease context, want <0.5.

**Signal quality for M4:** LOW
- Activity marker, not threshold marker
- Useful as background signal to contextualize others
- Does not directly measure tolerance capacity

---

## Proxy 8: Genetic Polymorphisms (one-time)

**Mechanistic rationale:** Constitutional component of the threshold — doesn't change with interventions.

| Polymorphism | Effect | Dysbiosis disease | Testing |
|-------------|--------|------------------|---------| 
| NOD2 R702W / G908R / L1007fs | Reduced bacterial sensing → inadequate Paneth cell defensin production | IBD, T1DM | 23andMe (R702W detectable), clinical WGS |
| TLR4 D299G / T399I | Reduced LPS sensitivity | IBD, endotoxin tolerance | Clinical WGS, some specialty panels |
| NLRP3 Q705K | Increased inflammasome activation | IBD, autoinflammatory | Clinical WGS |
| IL23R rs11209026 | Protective against Th17 overactivation | Psoriasis, IBD, AS | 23andMe |
| VDR variants (BsmI, TaqI) | Altered vitamin D receptor function → cathelicidin regulation | T1DM risk, IBD | Clinical WGS |
| FILAGGRIN (FLG) R501X / 2282del4 | Skin barrier protein loss → eczema | Atopic dermatitis | Clinical WGS |

**Clinical availability:** 23andMe detects major common variants. Full clinical exome/genome: $300-500.

**Signal quality for M4:** HIGH (constitutional) but STATIC
- Tells you WHERE on the threshold distribution a person starts
- Does not capture current state
- Complementary to dynamic proxies

---

## Composite "Threshold State Index" (proposed)

Using only clinically available tools:

```
THRESHOLD INDEX (T-index) = 
    Vitamin D (25-OH-D):        optimal 60-80 → +2 pts; deficient <20 → -2 pts
    Omega-3 index:              >8% → +2; <4% → -2
    hsCRP:                      <0.5 → +2; >3 → -2
    F. prausnitzii (relative):  >10% → +2; undetectable → -2
    Akkermansia (relative):     present → +1; absent → -1
    Serum zinc:                 80-120 µg/dL → +1; <60 → -2
    Treg % (if available):      >5% CD4+ → +2; <2% → -2
    NOD2 status (if known):     WT → 0; heterozygous → -1; homozygous/compound → -3
```

**This index does not exist in the literature.** It is a constructed proxy composite.

**Prediction:** A person with T-index < -4 is in a high-threshold-susceptibility state regardless of current microbial density.

**Falsifiable:** Longitudinal study — does T-index at baseline predict disease onset in high-microbial-density carriers who are currently asymptomatic? This is the study that doesn't exist but should.

---

## User Context Application

| Proxy | User's likely status | CVB protocol relevance |
|-------|---------------------|----------------------|
| Vitamin D | In protocol: D3+K2 → probably optimized | Monitored |
| Omega-3 | EPA/DHA in protocol → probably optimized | Monitored |
| hsCRP | Unknown — worth checking | Would reflect protocol efficacy |
| F. prausnitzii | Available from TinyHealth FASTQ | Key read from gut test |
| Akkermansia | Available from TinyHealth FASTQ | Key read from gut test |
| Zinc | In protocol (zinc supplementation) | Should monitor serum zinc to avoid excess |
| Treg % | Unknown — not in standard workup | Would require specialty lab |
| NOD2/TLR4 | Unknown | 23andMe can provide partial data |

**Recommendation for numerics Run 003:** pull TinyHealth results when available, extract F. prausnitzii + Akkermansia quantitative data, map against disease activity timeline.

---
*Run 002 M4 proxy survey: 8 proxies mapped. Best available composite: T-index. Clinical gap: Treg %, genetic panel. Cheapest proxies with signal: vitamin D + F. prausnitzii/Akkermansia + hsCRP.*
