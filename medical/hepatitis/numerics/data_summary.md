# CVB Hepatitis — Published Statistics Summary

**Disease:** CVB Hepatitis (Acute + Neonatal)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `~/open_problems/medical/results/epidemiology_all_diseases.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Adult CVB hepatitis annual cases | 280,000 | WHO Global Hepatitis Report 2022 |
| Neonatal CVB hepatitis annual cases | 90,000 | epidemiology_all_diseases.json |
| Total CVB hepatitis annual cases | 370,000 | cross_disease_burden_results.json |
| Annual CVB hepatitis deaths | 54,500 | cross_disease_burden_results.json |
| Total DALYs | 4,582,882 | cross_disease_burden_results.json |
| YLL | 4,082,050 | cross_disease_burden_results.json |
| Disability weight | 0.282 | GBD 2019 |
| Economic burden/yr | $5.55 billion | cross_disease_burden_results.json |
| Average age at death | 0.1 years (neonates dominate mortality) | cross_disease_burden_results.json |

## Adult vs Neonatal Disease

| Feature | Adult | Neonatal |
|---------|-------|---------|
| Severity | Mild, self-limiting | SEVERE — fulminant possible |
| Mortality | <1% | 60% (fulminant) |
| Persistence probability | 38.7% | 72.5% (multi-organ model) |
| Immune access to liver | 0.90 (best of any organ) | Immature — effectively 0.20 |
| Regenerative capacity | 0.95 (best of any organ) | High but overwhelmed |
| Treatment | Supportive | IVIG + supportive + consider transplant |

## Why Adults Clear CVB Hepatitis

The liver is the most CVB-resistant organ for chronic disease:
1. **Highest immune access** (0.90) — sinusoidal blood supply, resident Kupffer cells, NK cells
2. **Highest regenerative capacity** (0.95) — hepatocytes can divide; dead hepatocytes replaced
3. **Second-highest persistence threshold** (362 cells required) — virus must reach high load before TD mutants form
4. **Kupffer cell surveillance** — hepatic macrophages rapidly phagocytose CVB

The neonatal exception: immature Kupffer cell function + lack of maternal antibodies + high viral load from vertical transmission → persistence probability jumps to 72.5%.

## Serotype Data

| Serotype | Hepatic Tropism | Notes |
|----------|----------------|-------|
| CVB1 | 0.65 (PRIMARY) | Most hepatotropic |
| CVB4 | 0.55 | Secondary hepatotrope (also pancreatic) |
| CVB3 | 0.15 | Occasional |
| CVB2 | 0.20 | Occasional |
| CVB5 | 0.10 | Rare |

## Neonatal Fulminant Hepatic Failure Data

- Fulminant CVB hepatitis: ALT/AST >1000 IU/L, coagulopathy (PT >20s), encephalopathy
- Mortality without transplant: 60-80%
- Liver transplant: cure if available but limited by organ shortage + neonatal surgical risk
- IVIG: only intervention with clinical data; mechanism = CVB neutralization
- Time from symptoms to death (untreated fulminant): 24-72 hours

## GEO Datasets

**None found** for CVB hepatitis. The hepatitis GEO literature is dominated by HBV/HCV studies. CVB hepatitis is clinically underrecognized (CVB not tested in standard hepatitis workup) and scientifically understudied.

The hepatitis datasets needed:
1. Human liver biopsy RNA-seq from CVB hepatitis cases (does not exist in GEO)
2. Neonatal liver transcriptomics with CVB etiology (does not exist in GEO)
