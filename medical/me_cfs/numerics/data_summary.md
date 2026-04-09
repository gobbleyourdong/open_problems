# ME/CFS — Published Statistics Summary

**Disease:** Myalgic Encephalomyelitis / Chronic Fatigue Syndrome
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `~/medical_problems/results/mecfs_cvb_burden_analysis.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| US prevalence | 2.5 million | IOM/NAM 2015 |
| Global prevalence (estimated) | 17 million | IOM/NAM 2015 extrapolation |
| Enteroviral prevalence in ME/CFS vs controls | 42% vs 9% | Chia JD 2008 |
| CVB-attributable fraction (central estimate) | 42% | mecfs_cvb_burden_analysis.json |
| CVB-attributable prevalent cases (central) | 7,140,000 | cross_disease_burden_results.json |
| Annual CVB-attributable new cases | 357,000 | cross_disease_burden_results.json |
| Annual deaths (CVB-attributable) | 0 (not directly fatal) | cross_disease_burden_results.json |
| Total DALYs (CVB-attributable) | 17,802,876 | **Highest of all 12 CVB diseases** |
| Disability weight | 0.274 | GBD 2019 |
| Annual economic burden (CVB fraction) | $178.5 billion | mecfs_cvb_burden_analysis.json |
| Annual US economic burden (all-cause ME/CFS) | $17-24 billion | IOM 2015 range |

## Three-Scenario Burden Model

Source: `mecfs_cvb_burden_analysis.json`

| Scenario | ME/CFS US Total | CVB Cases | Protocol Responsive | CVB Econ Burden |
|----------|----------------|-----------|---------------------|-----------------|
| Conservative | 836,000 | 66,880 | 66,880 (8%) | $1.36B |
| Central | 1,500,000 | 315,000 | 420,000 (28%) | $4.2B |
| Optimistic | 2,500,000 | 1,060,000 | 927,500 (37%) | $10.2B |

## CVB Persistence in ME/CFS

| Parameter | Value | Source |
|-----------|-------|--------|
| Skeletal muscle persistence probability | 51.2% | pattern_010 |
| Critical infection threshold (muscle) | 105 cells | pattern_010 |
| CAR density in skeletal muscle | 0.35 | pattern_010 |
| Blood-testis barrier immune access equivalent | 0.30 | pattern_010 |

## The Vicious Cycle (Quantitative)

```
Fatigue → less activity → less AMPK activation → less ULK1 phosphorylation →
less autophagy flux → more TD mutant accumulation →
more MAVS activation → more NLRP3 → more IL-1beta + IFN-alpha →
more mitochondrial dysfunction → more fatigue
```

Every node is addressable:
- Less AMPK → FMD/caloric restriction restores AMPK
- Less autophagy → fluoxetine lysosomal disruption releases blockade
- More NLRP3 → colchicine blocks NLRP3
- More IFN → fluoxetine reduces viral load driving IFN

## Diagnostic Criteria (No Biomarker)

Current criteria: Institute of Medicine 2015 (SEID criteria)
1. Substantial reduction in ability to engage in pre-illness activities
2. Post-exertional malaise (worsening after exertion)
3. Unrefreshing sleep
4. PLUS at least one of: cognitive impairment OR orthostatic intolerance

**No validated blood or tissue biomarker.** This is the research blocker.

## Treatment Data

| Treatment | Trial Result | Notes |
|-----------|-------------|-------|
| Graded exercise therapy (GET) | Positive in PACE trial, but harmed many patients | PACE trial methodology contested; patient advocacy opposes |
| CBT | Positive in PACE trial | Same controversy |
| Rintatolimod (Ampligen) | Failed Phase 3 | FDA rejected |
| Rituximab (anti-CD20) | Phase 3 failed (Norway) | 2019 negative trial |
| Low-dose naltrexone | Case series only | No RCT |
| Fluoxetine + FMD | Not trialed | Proposed protocol |

## GEO Datasets

**None found.** The ME/CFS transcriptomic literature does not include CVB-specific studies.
Most ME/CFS GEO data examines immune profiling (NK cells, cytokines) without enteroviral etiology subset analysis.

**The critical missing study:** Stool CVB PCR + muscle biopsy transcriptomics in ME/CFS patients stratified by enteroviral status.
