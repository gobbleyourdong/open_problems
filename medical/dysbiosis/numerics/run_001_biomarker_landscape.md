# Biomarker Landscape — Dysbiosis
## Run 001 | Numerical Instance | 2026-04-11

> Exhaustive survey: what exists, what's research-only, what's needed but doesn't exist.
> Sorted by deployment tier. No interpretation — just the map.

---

## Tier 1: Clinically Deployed (routine or near-routine)

| Biomarker | What it measures | Deployment | Mountain relevance | Limitation |
|-----------|-----------------|------------|-------------------|------------|
| Fecal calprotectin | Gut inflammation activity (neutrophil protein) | Clinical, ~$50-80 | M1 | Activity marker, NOT threshold marker. High during flare, may normalize between flares. |
| CRP (C-reactive protein) | Systemic inflammation activity | Clinical, ~$10 | M1, M4 | Acute phase. Not microbiome-specific. Elevates with any inflammation. |
| Fecal 16S rRNA (amplicon) | Bacterial community composition at genus level | Consumer (TinyHealth, Viome, Genova), $200-400 | M1, M2, M3 (bacteria only) | Genus-level only. No species/strain. No viruses. No fungi. Culture-independent but PCR bias. |
| IgA (fecal secretory) | Mucosal immune activity in gut | Research/specialty labs | M1, M4 | Not standardized. IgA quantity ≠ specificity. Deficiency correlates with autoimmune risk. |
| Zonulin (serum/stool) | Gut permeability (proposed) | Commercial (Vibrant, Doctor's Data), ~$100-200 | M1 | CONTROVERSY: Zhang 2021 showed commercial ELISA detects complement C3, not zonulin specifically. Use with extreme caution. |
| Demodex density (dermoscopy or confocal reflectance microscopy) | Mite density per cm² skin | Clinical, specialized dermatology | M2, M4 | Not routine. Threshold for disease is ~100/cm² but this is phenomenological. Tolerant carriers exist above threshold. |
| Skin surface pH | Barrier function proxy | Research, some consumer devices | M2 | pH rises in inflamed/compromised skin. Not microbiome-specific. |
| TEWL (transepidermal water loss) | Skin barrier function | Research, some devices | M2 | Measures consequence, not microbial cause. |
| HbA1c | Glycemic control in T1DM | Clinical, ubiquitous | M3, M5 | Disease activity, not microbiome marker. Relevant for tracking CVB protocol effect. |
| Cytokine panel (serum IL-6, TNF-α, IL-1β) | Systemic inflammatory tone | Clinical (research-grade available) | M1, M4 | Snapshot only. Elevated during flares. Doesn't measure threshold or priming state. |

---

## Tier 2: Research-Grade (published studies but not routine clinical)

| Biomarker | What it measures | Availability | Mountain relevance | Key limitation |
|-----------|-----------------|-------------|-------------------|----------------|
| Virome-enriched shotgun metagenomics | RNA viruses, low-titer DNA viruses, bacteriophage | Research labs ($500-2000/sample) | M3 | Expensive. Requires host depletion + RNA capture + deep sequencing. No clinical standard. |
| Whole-genome shotgun metagenomics (WGS) | Bacterial + fungal community at species/strain level | Research ($200-800 for stool) | M1, M2 | More information than 16S but harder to interpret. Fungal reads are <1% of output typically. |
| Fecal metatranscriptomics | Active gene expression of microbial community | Research ($500-1500) | M1 | Captures what microbes are DOING, not just present. RNA is unstable; sample handling critical. |
| Serum/fecal metabolomics (SCFAs: butyrate, propionate, acetate) | Microbial metabolite output | Research/specialty ($300-600) | M1, M4 | SCFA in stool ≠ systemic SCFA. Butyrate mostly consumed by colonocytes. Plasma butyrate very low. |
| LL-37 (cathelicidin) serum + active fragment quantification | Cathelicidin processing status | Research | M4 (KLK5/cathelicidin axis) | Active pro-inflammatory fragments vs total LL-37. Tissue vs serum. Not standardized. |
| KLK5 activity (skin biopsy) | Serine protease that cleaves cathelicidin → pro-inflammatory fragments | Research (biopsy required) | M4 | Invasive. Not scalable. No serum equivalent. |
| NLRP3 priming assay (PBMC ex vivo stimulation) | Innate immune readiness for IL-1β release | Research | M4 | Blood-based proxy for tissue NLRP3 state. Not validated against tissue measurements. |
| Treg frequency (flow cytometry: CD4+CD25+FOXP3+) | Regulatory T cell calibration | Research (flow lab) | M4, M1 | Expensive. Blood Treg ≠ tissue Treg. Snapshot. |
| EndoCAb (endotoxin core antibody / anti-LPS IgM) | Cumulative LPS exposure / gut permeability history | Research | M1 | Measures immune response to LPS, not real-time LPS level. Historical exposure marker. |
| LPS-binding protein (LBP) serum | Acute phase protein that binds LPS | Research/some clinical | M1 | Surrogate. Elevates in sepsis but also in chronic low-level translocation. Noisy at low concentrations. |
| Demodex-specific IgM | Host sensitization to Demodex | Research assay (Tran 2016) | M2, M4 | Distinguishes immune response to Demodex. Could theoretically separate tolerant from sensitized carriers. Not commercially available. |
| Skin mycobiome (ITS sequencing) | Fungal community on skin | Research | M2 | Malassezia-specific. ITS1/ITS2 amplicon. Not routine. |

---

## Tier 3: Needed, Do Not Currently Exist

| Needed Biomarker | What it would measure | Mountain relevance | Why it's the gap |
|-----------------|----------------------|-------------------|-----------------|
| Clinical innate immune reactivity baseline assay | The THRESHOLD — how reactive is this host's innate immune system to microbial stimulation, before active disease | M4 (THE WALL) | This is the single most wanted missing biomarker. Would allow distinguishing tolerant from disease-prone carriers at the same microbial density. |
| Real-time gut permeability (continuous) | Dynamic barrier function, not point-in-time snapshot | M1 | Zonulin is contested and static. Need something like a CGM (continuous glucose monitor) equivalent for gut leakiness. Capsule-based sensors exist in research (e.g., Tronstad 2015 bioelectrical capsule). |
| KLK5 serum equivalent | Cathelicidin processing enzyme level without skin biopsy | M4 | Enables rosacea/threshold studies at scale. |
| Validated clinical gut permeability assay | Replace zonulin. Lactulose/mannitol ratio (L:M ratio) is an older method but labor-intensive | M1 | L:M ratio requires 24h urine collection. More specific than zonulin. Not convenient. |
| Virome sequencing at clinical price point ($50-100) | CVB 5'UTR-deleted, EBV latent, HHV-6/7 reactivation state, bacteriophage | M3 | Cost reduction of 10-20× required for routine clinical deployment. |
| Strain-level clinical microbiome report | Not just genus (Lactobacillus) but species + strain (L. rhamnosus GG vs L. rhamnosus LC705) | M1, M2 | Clinical relevance is at strain level. 16S genus-level is insufficient for actionable recommendations. WGS cost needs to drop ~5-10×. |
| Cross-site dysbiosis index | Single number integrating gut + skin + virome state | All mountains | Does not exist. No consensus on what would constitute it. Field is siloed by site. |
| Bacteriophage community clinical profiling | Which phages are present and targeting which gut bacteria | M1, M2 | Phages constitute >10× the bacterial numbers in gut. Essentially unmeasured clinically. Emerging field. |
| Demodex sensitization vs density-only assay | Distinguishes immune-sensitized host (about-to-flare) from density-only (tolerant) | M2, M4 | Demodex-specific IgM research assay exists but not commercial. |

---

## Biomarker Gap Summary

```
  THRESHOLD (M4):     ████████████ UNMEASURED
  GUT COMPOSITION:    ████░░░░░░░░ GENUS-LEVEL ONLY (species/strain missing)
  GUT PERMEABILITY:   ████░░░░░░░░ CONTESTED (zonulin controversy)
  VIROME:             ████░░░░░░░░ RESEARCH-GRADE ONLY (cost + method)
  SKIN COMPOSITION:   ████████░░░░ MODERATE (Malassezia/Demodex clinical)
  SYSTEMIC INFLAM:    ████████████ WELL MEASURED (but activity not threshold)
  METABOLITES:        ██████░░░░░░ RESEARCH-ONLY (SCFAs not routine)
  IMMUNE CALIBRATION: ████░░░░░░░░ PARTIAL (Tregs: flow cytometry only)
```

---

## Priority Biomarker Development Targets

Ranked by: (leverage on M4 wall) × (technical feasibility) × (clinical need)

1. **NLRP3 priming state assay (blood-based)** — most tractable path to innate immune baseline. PBMC protocol exists; needs standardization + clinical validation.
2. **Virome-enriched sequencing price reduction** — sequencing cost curve suggests $100/sample achievable within 3-5 years.
3. **Demodex sensitization (IgM) commercialization** — assay published; needs commercial development.
4. **Validated gut permeability assay (lactulose:mannitol)** — old method, needs streamlining/simplification for routine use.
5. **KLK5 serum proxy** — likely requires new antibody development. High mechanistic value.

---
*Run 001: 37 biomarkers mapped across 3 tiers. Critical gap: threshold measurement (M4) — no current tool.*
