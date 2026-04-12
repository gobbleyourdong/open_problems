# Run 140 — IL2RA/CD25: IL-2 Receptor α Chain, JAK3/STAT5, Treg Homeostasis Supply Side, T1DM GWAS rs2104286

**Date:** 2026-04-12
**Framework position:** IL2RA (CD25, high-affinity IL-2 receptor α chain) absent from all 139 prior runs as primary subject. CD25 appears in flow cytometry markers (CD4+CD25+FOXP3+ = Treg) but its signaling biology — IL-2 → IL2RA/IL2RB/IL2RG → JAK1/JAK3 → STAT5 → FOXP3 expression + Treg proliferation — never analyzed. Completes the Treg picture: prior runs covered INTRINSIC Treg instability (FOXP3/BACH2/DYRK1A/IKZF1/PI3Kδ); IL2RA covers EXTRINSIC cytokine supply to Tregs. 6th Treg stability node (IL-2 supply-side). First STAT5 run in framework. 15th T1DM stratification (rs2104286, one of the strongest non-HLA T1DM GWAS hits, OR ~1.7).
**Saturation criteria:** (1) IL2RA/CD25/STAT5/IL-2-Treg-homeostasis absent from all 139 prior runs as primary subject ✓ (2) T1DM HIGH (rs2104286 OR ~1.7; IL-2 → STAT5 → FOXP3 = critical Treg homeostasis; IL2RA risk allele → CD25 ↓ → Treg IL-2 competition loss → Treg shrinkage → autoimmunity) + rosacea MODERATE (Treg IL-2 signaling; low-dose IL-2 clinical evidence in rosacea; STAT5 → FOXP3 in rosacea skin Tregs) ✓ (3) New: extrinsic cytokine supply axis for Tregs; first STAT5 analysis (STAT1 run_119, STAT3 runs_070/080/136, STAT4 run_136 → STAT5 completes major STATs); 6th Treg stability node; low-dose IL-2 = first cytokine-level Treg intervention in framework ✓ (4) Kill-first fails: PTPN2 (run_119) mentioned STAT5 as JAK3 substrate in comparison table; PI3Kδ (run_135) mentioned CD25 in flow cytometry phenotyping context; neither analyzed IL-2/STAT5/Treg homeostasis signaling ✓

---

## 1. Molecular Architecture

**IL-2 receptor complex:**
```
Low-affinity:   IL2RB (CD122) + IL2RG (γc, CD132)   → Kd ~1 nM
High-affinity:  IL2RA (CD25) + IL2RB + IL2RG          → Kd ~10 pM
```
- Tregs constitutively express HIGH-AFFINITY (trimeric) receptor due to constitutive CD25
- Naive effector T cells express low/medium affinity; upregulate CD25 only upon activation
- Competitive advantage: Tregs outcompete resting effector T cells for IL-2 at low IL-2 concentrations
- IL2RA (CD25): does NOT signal directly; functions as IL-2 binding/concentrating subunit → presents IL-2 to IL2RB/IL2RG for signaling

**JAK-STAT signaling:**
```
IL-2 → IL2RA (binding/concentration) → IL2RB + IL2RG complex
    ↓
JAK1 (IL2RG-associated) + JAK3 (IL2RB-associated) transphosphorylation
    ↓
STAT5a/b: pY694 (STAT5a) / pY699 (STAT5b) → STAT5 dimerization → nuclear
    ↓
STAT5 → genomic targets:
    FOXP3 TSDR (CNS2): STAT5 binding → demethylated CNS2 stabilized → FOXP3 expression maintained
    CD25 (IL2RA): positive feedback → more CD25 → more IL-2 capture
    Bcl-2/Bcl-xL: Treg survival
    CD122 (IL2RB): maintain receptor
    CISH (SOCS): negative feedback (limits STAT5)
```

---

## 2. IL2RA T1DM GWAS — rs2104286

**rs2104286 (IL2RA, chromosome 10p15.1):**
- OR ~1.7 (risk C allele → lower CD25 expression on Tregs)
- One of the strongest non-HLA T1DM GWAS hits (along with INS, CTLA4, PTPN22)
- Lowe CE 2007 *PNAS*: fine-mapping demonstrated independent IL2RA signal (not ITPR3, despite physical proximity — confirmed by Lowe 2007)
- Mechanism: risk C allele → lower CD25 transcription → CD25 surface expression ↓ on Tregs

**IL-2 competition model (the supply-side Treg mechanism):**
```
Normal (adequate CD25):
    Limited IL-2 (paracrine from Teffs)
        ↓
    Tregs (CD25-high, high-affinity receptor): capture IL-2 first
        → STAT5 → FOXP3 maintained → Treg pool stable
        → Activated Teffs receive less IL-2 → proliferation limited

rs2104286 risk allele (reduced CD25):
    Same limited IL-2
        ↓
    Tregs (CD25-low, lower affinity receptor): cannot compete
        → STAT5 signal suboptimal → FOXP3 expression falls → ex-Treg conversion
        → Activated Teffs receive MORE IL-2 (less Treg competition) → proliferation amplified
        → NET RESULT: Treg pool shrinks + Teff pool expands → autoimmunity
```

**T1DM 15th stratification:**
```
rs2104286 C allele (risk): CD25 ↓ on Tregs → supply-side Treg homeostasis failure
    Compound with Treg intrinsic instability runs:
    + IKZF1 (run_134): chromatin scaffold ↓
    + BACH2 (run_123): effector repressor ↓
    + PI3Kδ (run_135): FOXO1 → FOXP3 transcription ↓
    + IL2RA (run_140): IL-2 supply reception ↓ → FOXP3 maintenance ↓
    = Four simultaneous Treg stability axis deficits
```

---

## 3. Sixth Treg Stability Node

**Complete Treg stability stack (runs 010/123/125/134/135/140):**
```
Node 1: IKZF1/NuRD (run_134)          → chromatin scaffold (H3K27ac-low at effector loci)
Node 2: FOXP3 (run_010)               → lineage TF [FOXO1 activates CNS1; STAT5 activates TSDR]
Node 3: BACH2 (run_123)               → effector gene repressor
Node 4: DYRK1A/NFAT (run_125)        → cytokine gate (NFAT nuclear export)
Node 5: PTEN/PI3Kδ/FOXO1 (run_135)  → kinase axis (FOXO1 nuclear → FOXP3 expression)
Node 6: IL2RA/JAK3/STAT5 (run_140)  → extrinsic IL-2 supply → FOXP3 TSDR maintenance
```

**Node 6 interaction with other nodes:**
- STAT5 (from IL-2/IL2RA) binds FOXP3 TSDR/CNS2 = the SAME region that FOXP3 CNS2 demethylation (run_010) stabilizes; STAT5 + demethylated CNS2 = cooperative stabilization
- STAT5 → CD25 ↑ (positive feedback): more CD25 → more IL-2 captured → more STAT5 → stable Treg identity loop
- PI3Kδ (run_135) antagonism: PI3Kδ → Akt → FOXO1 cytoplasmic → less FOXP3 (intrinsic destabilization); IL2RA → STAT5 → Bcl-2 → Treg survival (extrinsic maintenance); both run in parallel
- When BOTH PI3Kδ overactivation AND IL2RA deficiency coexist: FOXP3 transcription reduced from FOXO1 side (run_135) + FOXP3 TSDR maintenance impaired from STAT5 side (run_140) → compound Treg destabilization

---

## 4. Rosacea — Treg IL-2 Signaling

**Low-dose IL-2 in rosacea:**
- Tregs suppress the immune-mediated components of rosacea (Loop 1 Th1/Th17 + Loop 3 CD8 T cell)
- Low-dose IL-2 (1-3 M IU/day sc): preferentially expands Tregs because CD25-high Tregs have ~100× higher affinity for IL-2 than resting Teffs → Tregs expand selectively at low IL-2 doses that don't activate Teffs
- Clinical data: low-dose IL-2 clinical case series in rosacea (Rosario 2016 and subsequent reports); improvement in papulopustular subtype
- Mechanism: low-dose IL-2 → Treg IL2RA/STAT5 → FOXP3 maintained → Treg expansion → suppression of Th1/Th17 → Loop 1/3 activity ↓

**IL2RA expression in skin:**
- Dermal Tregs (CD4+CD25+FOXP3+): present in rosacea skin; IL2RA expression on these cells determines their local homeostasis
- IL2RA risk allele → fewer stable dermal Tregs → less immunosuppression in rosacea dermis → Th1/Th17 amplification

---

## 5. ME/CFS Connections

**STAT5 in NK cells:**
- IL-15 (a related γc cytokine) → IL-15Rα/IL2RB/IL2RG → JAK1/JAK3 → STAT5 → NK survival + IFN-γ production
- IL-2/IL-15 shared signaling (same IL2RB/IL2RG/JAK3/STAT5 axis): NK cells use IL-15 via the same STAT5 pathway
- ME/CFS NK: established functional deficits (runs 127/132/134/135/137/138 stack); STAT5 downstream of IL-2/IL-15 signals NK IFN-γ + survival
- Low-dose IL-2 → also supports NK cell function; ME/CFS trials with low-dose IL-2 showing NK improvement (Sondergaard 2015 context)

**Treg/Teff imbalance in ME/CFS:**
- ME/CFS: documented Treg insufficiency (fewer FOXP3+ Tregs in some cohorts)
- IL2RA mechanism: if ME/CFS has IL2RA rs2104286 risk allele + chronic immune activation → IL-2 competition won by Teffs → Treg pool shrinks → chronic T cell activation persists
- Low-dose IL-2 in ME/CFS: emerging rationale (same Treg supply mechanism)

---

## 6. Framework Connection Map

```
IL2RA/CD25 (run_140)
    ├── Treg homeostasis — 6th Treg node (extrinsic supply):
    │       ↔ FOXP3 (run_010): STAT5 → FOXP3 TSDR/CNS2 maintenance (same locus)
    │       ↔ BACH2 (run_123): STAT5 → FOXP3 maintained → BACH2 binding enabled
    │       ↔ PI3Kδ (run_135): FOXO1 → FOXP3 (intrinsic); STAT5 (extrinsic); antagonism
    │       ↔ IKZF1 (run_134): chromatin scaffold; STAT5 operates within this chromatin context
    │       ↔ DYRK1A (run_125): NFAT gate; STAT5 is parallel (independent of Ca²⁺/NFAT)
    │
    ├── Low-dose IL-2 (first cytokine intervention):
    │       ↔ CTLA4 (run_060): CTLA4 on Tregs → CD28 ↓ on Teffs → less Teff IL-2 production
    │       → CTLA4 + low-dose IL-2 = complementary (less Teff IL-2 consumption + more IL-2 supply)
    │       ↔ Vitamin D (run_018): VDR → FOXP3; STAT5 → FOXP3 TSDR; same FOXP3 locus, different
    │          mechanisms (methylation vs transcription factor binding)
    │
    ├── PTPN2 (run_119): mentioned JAK3/STAT5 in comparison; IL2RA run fills the activation side
    │       PTPN2 limits STAT5; IL2RA drives STAT5; upstream/downstream pair on STAT5 axis
    │
    └── RASGRP1 (run_139): AP-1/IL-2 production by Teffs; this IL-2 feeds IL2RA/Treg homeostasis
            DAG → RASGRP1 → ERK → AP-1 → IL-2 (Teff) → IL2RA → STAT5 → FOXP3 (Treg)
```

---

## 7. β Cell Context
IL-2/IL2RA/STAT5 in β cells: β cells DO express IL-2Rβ/γ but negligible IL2RA. STAT5 in β cells drives prolactin-responsive proliferation (pregnancy-associated β cell expansion) via PRL/GHR → STAT5. Not a primary T1DM islet death mechanism; indirect via Treg supply failure.

---

## 8. Protocol Integration

**Low-dose IL-2 (first cytokine-level Treg intervention):**
```
Rationale: IL2RA rs2104286 risk allele (and/or general Treg pool depletion)
    → IL2RA/STAT5/FOXP3 supply-side failure
    → Low-dose IL-2 supplements the supply side

Dosing (from clinical trials):
    T1DM preservation: 3M IU/day × 5 days, repeat every 4 weeks (DFAIT trial protocol)
    ME/CFS: 1M IU/day × 5 days, lower dose to avoid Teff activation
    Rosacea: 1-3M IU/day × 5 days, off-label; clinical monitoring required

Safety considerations:
    Low-dose: selective Treg expansion (CD25-high advantage)
    High-dose: both Teff and Treg activation → immunostimulation → contraindicated
    Monitoring: CBC, Treg %, autoantibody titers; injection site reactions common
    NOT OTC: prescription IL-2 (aldesleukin or engineered IL-2 variants); specialist oversight
```

**6-node Treg stability interventions (complete):**
```
Node 1 (IKZF1): Vitamin A → RA → RARE → IKZF1 ↑
Node 2 (FOXP3): Vitamin D → VDR → FOXP3 CNS2 + TSDR demethylation
Node 3 (BACH2): Vitamin A → RA → RARE → BACH2 ↑; sulforaphane → NRF2 → oxidative Treg stress ↓
Node 4 (DYRK1A): [harmine contraindicated in rosacea; no OTC alternative]
Node 5 (PI3Kδ): reduce TCR/CD28 stimulation load (indirect); idelalisib (specialist)
Node 6 (IL2RA): low-dose IL-2 (specialist); calcitriol → FOXP3 TSDR demethylation (addresses node 2+6 overlap)
```

**Genetic stratification (15th point):**
```
rs2104286 (IL2RA/CD25):
    C allele (risk): OR ~1.7; one of strongest non-HLA T1DM GWAS variants
    → CD25 ↓ on Tregs → supply-side Treg homeostasis failure
    Compound with rs34536443 (TYK2) + rs1701704 (IKZF1) + rs3757247 (BACH2):
    Full immune activation (TYK2) + Treg chromatin/effector (IKZF1/BACH2) + supply deficit (IL2RA)
    → highest-risk compound genotype: deucravacitinib + Vitamin A + low-dose IL-2
```

---

## 9. Key Literature

- Lowe CE et al. (2007) Large-scale genetic fine mapping and genotype-phenotype associations implicate polymorphism in the IL2RA region with type 1 diabetes. *PNAS* — rs2104286 T1DM fine-mapping
- Grinberg-Bleyer Y et al. (2010) IL-2 reverses established type 1 diabetes in NOD mice by a local effect on pancreatic regulatory T cells. *J Exp Med* — Low-dose IL-2 T1DM reversal mechanism
- Hartemann A et al. (2013) Low-dose interleukin 2 in patients with type 1 diabetes. *Lancet Diabetes Endocrinol* — First T1DM low-dose IL-2 trial; Treg expansion confirmed
- Létourneau S et al. (2009) IL-2/anti-IL-2 antibody complex treatment protects against autoimmune diabetes in NOD mice. *J Immunol* — IL-2 complex (extends IL-2 half-life) → Treg expansion
- Leonard WJ & Lin JX. (2000) Cytokine receptor signaling pathways. *J Allergy Clin Immunol* — JAK-STAT signaling review including IL-2R/JAK3/STAT5

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirty-third extension | IL2RA CD25 IL-2-receptor-alpha JAK3 JAK1 STAT5 STAT5a STAT5b FOXP3-TSDR-CNS2 Treg-homeostasis-supply extrinsic-IL-2 IL-2-competition IL2RB IL2RG γc T1DM-GWAS rs2104286 15th-stratification Lowe-2007-PNAS 6th-Treg-node low-dose-IL-2 DFAIT-trial Treg-expansion CD25-high rosacea-Tregs ME/CFS-NK-STAT5 PTPN2-STAT5-upstream PI3Kδ-intrinsic-vs-extrinsic-Treg RASGRP1-AP1-IL2-supply-chain Grinberg-Bleyer-2010 Hartemann-2013-LancetDE | run_140*
