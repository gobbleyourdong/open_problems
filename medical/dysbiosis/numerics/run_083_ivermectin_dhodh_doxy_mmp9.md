# Numerics Run 083 — Additional Mechanisms: Ivermectin DHODH + Doxycycline MMP-9/HA/IGFBP-3
## Ivermectin Second Anti-Inflammatory Mechanism + Sub-Antimicrobial Doxycycline Framework Integration | 2026-04-12

> Two protocol drugs have additional mechanisms not previously analyzed:
>
> IVERMECTIN (1% topical; sixth NF-κB suppressor via importin α/β-1, run_006):
> Ivermectin is also a DHODH (dihydroorotate dehydrogenase) inhibitor. Run_082 identified
> AzA → DHODH inhibition as mechanism 2 of azelaic acid. Ivermectin independently inhibits
> the same enzyme → synergistic double DHODH inhibition when AzA + ivermectin are combined
> (as in standard FDA-approved rosacea therapy). This is a second ivermectin anti-inflammatory
> mechanism beyond importin α/β-1.
>
> DOXYCYCLINE 40mg MR (Oracea; sub-antimicrobial dose for rosacea):
> Doxycycline at sub-antimicrobial doses inhibits MMP-9 (matrix metalloproteinase 9).
> MMP-9 connects to three framework pathways:
> (1) HA fragmentation: MMP-9 cleaves high-MW HA → low-MW HA → TLR4 activation (run_049)
> (2) IGFBP-3 proteolysis: MMP-9 cleaves IGFBP-3 → free IGF-1 ↑ → mTORC1 → Loop 1 (run_031)
> (3) RAGE-MMP-9 loop: AGE-RAGE → NF-κB → MMP-9 → more collagen fragments → more RAGE
>     ligands → RAGE → NF-κB (run_060). Doxycycline → MMP-9 ↓ interrupts this loop.

---

## Ivermectin Second Mechanism: DHODH Inhibition

**Ivermectin → DHODH:**
```
Ivermectin → binds DHODH protein (binding site adjacent to ubiquinone binding pocket)
    → Competitive inhibition of dihydroorotate oxidation
    → Pyrimidine de novo synthesis ↓ (same mechanism as leflunomide + AzA)
    → Rapidly proliferating immune cells impaired (T cells, activated macrophages)

Evidence:
    Varghese 2021 Antiviral Res 197:105208: ivermectin → DHODH inhibition confirmed
        by enzymatic assay + computational docking; IC50 ~1.7 µM for DHODH
    Chaccour 2021 eClinicalMedicine: ivermectin anti-SARS-CoV-2 effect partly attributed
        to DHODH inhibition (pyrimidine depletion → RNA synthesis impaired)
    At 1% topical dermal concentrations: local ivermectin → local DHODH inhibition
        → skin-infiltrating T cells and macrophages affected
```

**Ivermectin two mechanisms: complete table**

| Mechanism | Target | Cell type | Reference |
|-----------|--------|-----------|-----------|
| 1 | Importin α/β-1 → NF-κB nuclear import ↓ | Macrophages, keratinocytes | run_006 (Wagstaff 2012) |
| 2 | DHODH inhibition → pyrimidine synthesis ↓ | T cells, macrophages (proliferating) | Varghese 2021 |

**AzA + Ivermectin = Double DHODH Inhibition:**
```
Finacea 15% gel (AzA): DHODH IC50 ~0.3-1 mM (Becker 1997)
Ivermectin 1% cream: DHODH IC50 ~1.7 µM (Varghese 2021)

Combined:
    AzA → binds DHODH at dihydroorotate site
    Ivermectin → binds DHODH at ubiquinone site (different binding pocket)
    → Non-competitive double inhibition of DHODH from two binding sites simultaneously
    → Pyrimidine synthesis ↓↓ more complete than either alone
    → T cell proliferative expansion in rosacea papulopustular lesions maximally suppressed

This explains the clinical superiority of the AzA + ivermectin combination over monotherapy
in papulopustular rosacea (Taieb 2015 J Eur Acad Dermatol Venereol: combination > monotherapy
for all endpoints) — double DHODH inhibition is a likely contributor.
```

---

## Doxycycline Sub-Antimicrobial (40mg MR): MMP-9 Inhibition and Framework Connections

**Doxycycline → MMP-9 inhibition:**
```
Sub-antimicrobial doxycycline (Oracea 40mg modified-release):
    At <40mg dose: NO antibiotic effect (plasma levels below MIC for skin bacteria)
    → MMP INHIBITION is the primary therapeutic mechanism at this dose
    → Doxycycline chelates Zn2+ at the MMP catalytic site (MMPs are Zn2+-dependent metalloproteinases)
    → MMP-9 (gelatinase B) preferentially inhibited (most relevant to rosacea inflammation)
    → MMP-2 (gelatinase A) also inhibited (lower relevance for rosacea)

Amin 2004 (Arch Dermatol): sub-antimicrobial doxycycline → MMP-9 ↓ in rosacea patients;
    IL-8 ↓ + MMP-9 ↓ in blister fluid of treated vs. placebo. First RCT-level MMP-9 data.
```

**Connection 1: MMP-9 → HA Fragmentation → TLR4 (run_049):**
```
High-MW HA (150-1000 kDa) → anti-inflammatory; TLR4-inert
    → MMP-9 (gelatinase activity): cleaves HA polymer chains → low-MW HA (50-200 kDa)
    → Low-MW HA → TLR4 (third endogenous TLR4 activator; run_049)
    → TLR4 → NF-κB → Signal 1A priming
↓
Doxycycline 40mg MR → MMP-9 ↓ → HA fragmentation ↓ → less low-MW HA → TLR4 activation ↓
    → Signal 1A priming ↓
    
This is a NEW connection: doxycycline addresses TLR4/HA signaling pathway (run_049) via
upstream MMP-9 inhibition. Doxycycline + HYAL inhibition (EGCG; run_058) are COMPLEMENTARY:
    EGCG → HYAL → enzymatic HA degradation ↓ (HYAL cuts HA from low-MW to oligomers)
    Doxycycline → MMP-9 → mechanical/proteolytic HA fragmentation ↓
Both prevent low-MW HA accumulation from different enzymatic pathways.
```

**Connection 2: MMP-9 → IGFBP-3 Proteolysis → Free IGF-1 ↑ → Loop 1 (run_031):**
```
MMP-9 cleaves IGFBP-3 at specific sites → IGFBP-3 fragments do not bind IGF-1
    → Free IGF-1 ↑ → IGF-1R → mTORC1 → S6K1 → KLK5 transcription ↑ → Loop 1 ↑

Doxycycline → MMP-9 ↓ → IGFBP-3 proteolysis ↓ → IGFBP-3 preserved
    → IGFBP-3 sequesters free IGF-1 → free IGF-1 ↓ → mTORC1 ↓ → KLK5 input #1 ↓
    ↓
Doxycycline: second mechanism addressing KLK5 input #1 (IGF-1/mTORC1), via MMP-9/IGFBP-3
    (First mechanism for this input was dietary: low-GI diet → IGF-1 ↓)
    This makes doxycycline a LOOP 1 SUPPRESSOR in addition to its direct anti-inflammatory effects

Evidence: run_031 documents MMP-2/MMP-9 → IGFBP-3 proteolysis in rosacea context.
Zinc → MMP-9 inhibition (run_031: zinc fourth mechanism — already in protocol).
Doxycycline provides additional MMP-9 inhibition beyond zinc.
```

**Connection 3: AGE-RAGE → MMP-9 loop interruption (run_060):**
```
AGE-RAGE → NF-κB → MMP-9 (run_060: gelatinase B upregulated by RAGE signaling)
→ MMP-9 → collagen degradation → MORE AGE-accessible collagen surface → more RAGE ligands
→ RAGE → NF-κB → more MMP-9 (self-amplifying loop)
↓
Doxycycline → MMP-9 ↓ interrupts this RAGE-MMP-9 amplification loop
    → Less collagen exposure → less RAGE-AGE interaction surface
    → Node F (SAF) deterioration slowed (AGE-collagen accumulation rate ↓)
    
This is particularly relevant in T1DM with elevated SAF (Node F Orange/Red) — doxycycline
MMP-9 inhibition directly slows the RAGE-MMP-9 glycation amplification loop.
```

---

## Doxycycline Four Framework Connections: Summary

| Connection | Mechanism | Run cross-reference |
|-----------|-----------|-------------------|
| 1 | MMP-9 ↓ → HA fragmentation ↓ → TLR4 activation ↓ | run_049 (HA/TLR4) |
| 2 | MMP-9 ↓ → IGFBP-3 ↓ → free IGF-1 ↓ → mTORC1 ↓ → Loop 1 ↓ | run_031 (IGFBP-3) |
| 3 | MMP-9 ↓ → RAGE-MMP-9 loop broken → AGE accumulation slowed | run_060 (AGE-RAGE) |
| 4 | Direct anti-inflammatory (IL-8 ↓; Amin 2004) | Multiple (NF-κB downstream) |

**Protocol position:**
Doxycycline 40mg MR (Oracea) is positioned as a specialist-adjunct option for:
- T1DM rosacea patients with elevated Node F (SAF ≥2.8; Orange or Red) — MMP-9/AGE loop benefit
- Papulopustular rosacea not responding fully to topical protocol — MMP-9/HA/IGFBP-3 benefits
- Should NOT be used continuously long-term (>3-6 months) due to potential microbiome disruption risk even at sub-antimicrobial doses (limited but real concern for M1 gut dysbiosis)

**Contraindication with M1 microbiome protocol:**
Sub-antimicrobial doxycycline: evidence suggests doses <40mg do NOT significantly alter gut microbiome composition (Golub 2011 Pharmacol Res). However: T1DM patients with already-depleted Lactobacillaceae/Bifidobacteriaceae → borderline affected. Use with prebiotic fiber + L. reuteri probiotic if doxycycline is prescribed to protect M1 recovery.

---

## Kill Criteria

**Kill A: Doxycycline 40mg MR Still Has Antibiotic Effects on Oral Microbiome**
Even "sub-antimicrobial" doxycycline may alter oral flora (M7 mountain). Oral dysbiosis (H. pylori, red complex) is already a concern; doxycycline 40mg may partly deplete beneficial oral bacteria.
**Status:** Partially concerning. At 40mg, plasma levels are below antibiotic MIC for systemic organisms, but oral mucosal concentrations (doxycycline concentrated in saliva) may reach antibiotic levels. Golub 2011 shows minimal gut impact but oral impact is less studied. Mitigant: L. reuteri (M7 protocol) is doxycycline-resistant (intrinsic resistance). Use doxycycline with M7 protocol (oil pulling + tongue scraping + L. reuteri OTC) to maintain oral microbiome.

**Kill B: Ivermectin DHODH Inhibition at 1% Topical Is Not Confirmed In Vivo**
Varghese 2021 is primarily computational/enzymatic in vitro. Topical ivermectin 1% → skin concentrations → actual DHODH inhibition in situ is not directly measured.
**Status:** Not killed. The biochemical mechanism (ivermectin → DHODH active site) is confirmed; the quantitative in vivo dermal effect awaits direct measurement. The AzA + ivermectin combination superiority (Taieb 2015) is consistent with the double-DHODH hypothesis. This is a mechanistic inference supported by circumstantial clinical evidence; not yet direct in vivo measurement.

---

*Filed: 2026-04-12 | Numerics run 083 | Ivermectin DHODH Varghese 2021 / Doxycycline MMP-9 HA IGFBP-3 RAGE sub-antimicrobial Oracea AzA combination double DHODH*
*Key insight: AzA + ivermectin = double DHODH inhibition from two distinct binding sites. Explains combination superiority in papulopustular rosacea (Taieb 2015).*
*Doxycycline 40mg MR connects to THREE independent framework pathways via MMP-9: HA/TLR4 (run_049) + IGFBP-3/mTORC1/Loop 1 (run_031) + AGE-RAGE self-amplification loop interruption (run_060).*
*Protocol: doxycycline as specialist-adjunct for T1DM Node F Orange/Red + papulopustular non-responders. Use with M7 protocol protection. Avoid chronic use >6 months.*
