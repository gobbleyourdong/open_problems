# Viral Pancreatitis (CVB) — Published Statistics Summary

**Disease:** Viral Pancreatitis (CVB-attributable)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `/home/jb/medical_problems/results/epidemiology_all_diseases.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Global acute pancreatitis cases/yr (all causes) | 2,700,000 | GBD 2019, US data |
| Incidence/100k/yr (all-cause) | 34 (range 13-45) | GBD 2019 |
| CVB-attributable fraction | 7.5% (range 5-10%) | Hyoty 2016, Richardson 2009 |
| CVB-attributable annual cases | 202,500 | epidemiology_all_diseases.json |
| Annual deaths (CVB-attributable) | 4,860 | epidemiology_all_diseases.json |
| Economic burden/yr (CVB fraction) | $2.43 billion | epidemiology_all_diseases.json |
| Progression to severe pancreatitis | 8% | Banks PA 2013 (Gut) |
| Severe pancreatitis mortality | 30% | Banks PA 2013 |
| Cost per severe CVB pancreatitis case | ~$12,000 | epidemiology_all_diseases.json |

## T1DM Connection — Critical Data Point

CVB pancreatitis elevates T1DM risk **2-4x** (Hyoty 2016):

Mechanism:
1. CVB1/B4 lyses acinar cells → trypsinogen release → pancreatic autodigestion
2. Adjacent islets sustain **bystander damage** (not direct infection, but inflammatory microenvironment)
3. Bystander-damaged beta cells upregulate stress markers → autoantigen exposure
4. In susceptible HLA genotypes (DR3/DR4): autoimmune cascade triggers against stressed beta cells
5. Result: clinical T1DM onset weeks-to-months after pancreatitis episode

This means **every CVB pancreatitis case is also a T1DM risk event.** CVB pancreatitis in DR3/DR4 carriers should trigger T1DM screening (autoantibody panel).

## Serotype Data

| Serotype | Pancreatic Tropism | Notes |
|----------|-------------------|-------|
| CVB1 | 0.80 (PRIMARY) | Highest exocrine pancreas tropism |
| CVB4 | 0.70 | Also the primary T1DM serotype (endocrine) |
| CVB3 | 0.25 | Occasional |
| CVB2 | 0.15 | Rare |
| CVB5 | 0.10 | Rare |

CVB1 and CVB4 both attack the pancreas but with different targets:
- CVB1: primarily exocrine acinar cells → pancreatitis
- CVB4: primarily endocrine beta cells → T1DM

## 2A/3C Protease Activation of Trypsinogen

- CVB 2A/3C proteases in infected acinar cells activate trypsinogen → trypsin
- Trypsin activates other digestive enzymes (chymotrypsin, elastase, phospholipase)
- Autodigestion of pancreatic tissue begins
- Distinct from gallstone/alcohol pancreatitis but same end-pathway

## Clinical Data

| Feature | Value |
|---------|-------|
| Presenting symptoms | Epigastric pain radiating to back, nausea, vomiting |
| Diagnosis | Serum lipase >3x upper limit + imaging |
| CVB typing rate (routine clinical) | <1% (not done) |
| If CVB typed: stool PCR sensitivity | ~60% in first 2 weeks |
| Exocrine insufficiency (long-term) | 15% of severe cases |
| Recurrence rate | 20-30% (any cause) |

## GEO Datasets

**None found.** Zero GEO datasets for CVB + pancreatitis. This is a field with essentially zero transcriptomic data despite substantial disease burden.

**Research gap:** No human pancreatitis transcriptomics with CVB etiology. No animal model transcriptomic data for CVB-induced pancreatitis in GEO. This is surprising given the T1DM connection and the large literature on pancreatitis.
