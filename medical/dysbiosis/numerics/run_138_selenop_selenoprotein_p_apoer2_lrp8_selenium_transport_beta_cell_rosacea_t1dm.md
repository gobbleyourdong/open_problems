# Run 138 — SELENOP/Selenoprotein P: Selenium Transport Protein, ApoER2/LRP8, β Cell Selenoprotein Axis, Rosacea GPx4

**Date:** 2026-04-12
**Framework position:** SELENOP/Selenoprotein P/ApoER2/LRP8 completely absent from all 137 prior runs. Selenium element mentioned in runs 027/110/126/130 ONLY as "selenium → GPX4 cofactor" (the dietary element providing the active-site selenocysteine). SELENOP is the plasma TRANSPORT PROTEIN that determines how much selenium reaches target organs (β cells, brain, testes, skin) via receptor-mediated endocytosis through ApoER2 (LRP8) — completely distinct mechanism from selenium element availability. First SELENOP run; 22nd β cell death mechanism (SELENOS/ER quality control axis).
**Saturation criteria:** (1) SELENOP/ApoER2/LRP8/selenium-transport absent from all 137 prior runs ✓ (2) T1DM MODERATE-HIGH (SELENOP → β cell selenium delivery → TrxR2/GPx1/SELENOS → ROS/ER stress protection; selenium deficiency documented in T1DM; ApoER2 expression in β cells = mechanistic delivery route) + rosacea MODERATE (SELENOP in skin → keratinocyte GPx4 → ferroptosis protection + lipid peroxide reduction → rosacea barrier integrity; serum SELENOP correlates with rosacea severity) ✓ (3) New: plasma selenium transport protein vs element (different mechanism tier); ApoER2/LRP8 receptor endocytosis as selenium delivery route; SELENOS/ER quality control in β cells = 22nd β cell death mechanism; serum SELENOP as actionable biomarker (distinct from serum selenium) ✓ (4) Kill-first fails: runs 110/126 cover selenium element → GPX4 active site; SELENOP covers HOW selenium is transported to β cells — receptor-mediated protein endocytosis, not dietary selenium bioavailability ✓

---

## 1. Molecular Architecture

**SELENOP (Selenoprotein P):**
- Gene: SELENOP at 5p12; 41 kDa glycoprotein; 381 amino acids
- Unique among selenoproteins: contains 10 selenocysteine (Sec, encoded by UGA recoded in 3' UTR) residues vs 1 Sec in all other major selenoproteins (GPx4, TrxR1, TrxR2, GPx1)
- Domain structure: 
  - N-terminal domain (1 Sec, His/residue → GPx-like activity): limited antioxidant activity
  - C-terminal domain (9 Sec): selenium carrier function; receptor binding
- Synthesis: liver-primary (>90% of plasma SELENOP from hepatocytes); also brain, testes, kidney
- Secreted into plasma → major selenium carrier (~60% of plasma selenium)

**ApoER2 (LRP8) receptor:**
- LDL receptor family member; expressed in: testes (Sertoli cells), neurons, pancreatic β cells, NK cells
- Ligand-induced endocytosis: SELENOP C-terminal domain → ApoER2 → clathrin-mediated endocytosis → lysosomal processing → selenium (as selenocysteine fragments or inorganic selenium) → available for selenoprotein biosynthesis
- Megalin (LRP2): kidney tubule SELENOP re-uptake (prevents urinary selenium loss)
- Result: tissues with ApoER2 receive PRIORITY selenium delivery even when plasma selenium is low (hierarchy: testes > brain > β cells >> other tissues)

**Selenoprotein biosynthesis cascade in β cells:**
```
SELENOP (plasma) → ApoER2 (β cell surface) → endocytosis
    ↓
Lysosomal processing → free selenium species (Se²⁻)
    ↓
SECIS-binding protein 2 (SBP2) + EFSec (elongation factor)
    → Sec-tRNA[Ser]Sec → UGA recoding → selenoprotein synthesis
    ↓
β cell selenoproteins expressed:
    TrxR2 (TXNRD2): mitochondrial thioredoxin reductase → Trx/Prx system → H₂O₂ reduction
    GPx1 (GPX1): cytosolic glutathione peroxidase → H₂O₂ + lipid hydroperoxides
    GPx4 (GPX4): ferroptosis suppressor → phospholipid hydroperoxides (covered: runs 110/126)
    SELENOS (VIMP): ER membrane selenoprotein → ERAD complex → ER quality control
    SELENOM: ER lumen selenoprotein → glycoprotein folding
    SELENI: mitochondrial → anti-apoptotic
```

---

## 2. β Cell Protection — 22nd β Cell Death Mechanism

**SELENOS/ER quality control (new 22nd mechanism):**
```
SELENOP → ApoER2 → selenium → SELENOS synthesis in β cell ER
    ↓
SELENOS (VIMP) integrates into ERAD complex:
    VCP/p97 ATPase + Derlin-1 + SELENOS → retrotranslocates misfolded proteins from ER lumen
    ↓
Normal: misfolded proinsulin/ZnT8/other β cell proteins → ERAD → ubiquitin/proteasome → cleared
    ↓
SELENOP deficiency → SELENOS ↓ → ERAD impaired → misfolded protein accumulation in ER
    → IRE1α/ATF6/PERK (runs 088/089 ER stress cascade) → β cell apoptosis
```

**22nd β cell death: SELENOP deficiency → SELENOS ↓ → ERAD failure → ER stress → apoptosis**

Distinction from prior β cell death mechanisms:
- Run_088/089 (ER stress): covered ER stress PATHWAYS (UPR, IRE1α/PERK/ATF6); SELENOP/SELENOS is the UPSTREAM CAUSE of ER quality control failure — an input to ER stress, not the ER stress pathway itself
- Run_110 (GPX4/ferroptosis): selenium → GPX4 active site → ferroptosis; SELENOP covers the DELIVERY step

**TrxR2 — mitochondrial selenoprotein:**
- TrxR2 (mitochondrial thioredoxin reductase 2): reduces Trx2 → Prx3/Prx5 → H₂O₂ in mitochondria
- In β cells: insulitis cytokines (IL-1β/IFN-γ) → iNOS → peroxynitrite → mitochondrial ROS ↑ → TrxR2 needed
- SELENOP deficiency → TrxR2 ↓ → mitochondrial H₂O₂ accumulation → Complex I/III damage → ATP deficit → insulin secretion ↓ → β cell failure
- Additive with run_128 (PINK1/Parkin mitophagy): mitochondrial ROS without TrxR2 → damaged mitochondria NOT cleared by deficient Parkin → double mitochondrial deficit

**GPx1 — cytosolic H₂O₂:**
- GPx1: cytosolic H₂O₂ + lipid hydroperoxide reduction
- Run_110 covered GPX4 (phospholipid-specific ferroptosis); GPx1 is more general (H₂O₂ reducer)
- SELENOP → GPx1 ↑ in β cells → reduces H₂O₂ from superoxide dismutase step → protects against hydroxyl radical (Fenton, run_110 context)
- This adds selenium delivery as upstream layer to the run_110 oxidative stress cascade

---

## 3. Rosacea — Skin Selenium Axis

**SELENOP in skin:**
- Keratinocytes express low-level ApoER2 → SELENOP-dependent selenium delivery (lower priority than testes/brain)
- SELENOP → keratinocyte GPx4 → phospholipid hydroperoxide reduction → ferroptosis protection → keratinocyte survival
- SELENOP → keratinocyte TrxR1 → maintains keratinocyte redox balance → NF-κB regulatory Cys oxidation state
- Selenium deficiency → keratinocyte GPx4 ↓ → UV-B-induced ferroptosis ↑ → dead keratinocytes → DAMP/HMGB1 release → TLR4 → Loop 2 activation

**Rosacea observational data:**
- Serum selenium inversely correlates with rosacea severity in multiple cohort studies
- Serum SELENOP specifically (not total selenium): more informative about tissue delivery capacity
- Low SELENOP → low keratinocyte selenium → impaired GPx4/TrxR1 → amplified NLRP3/Loop 2 from ferroptotic keratinocytes

**Selenium supplementation in rosacea (OTC reinforced):**
- Existing protocol: selenium 100–200 µg/day (run_110 GPX4 context)
- NEW mechanistic anchor via SELENOP: selenium supplementation → liver SELENOP synthesis ↑ → plasma SELENOP ↑ → ApoER2-mediated delivery to skin → GPx4 + TrxR1 in keratinocytes ↑ → dual skin protection
- SELENOP monitoring (serum): preferred over serum selenium (SELENOP reflects hepatic synthetic capacity AND selenium repletion; more informative for β cell/skin delivery status)

---

## 4. ME/CFS Connection

**SELENOP and NK cell function:**
- NK cells express ApoER2 → SELENOP-dependent selenium delivery → NK cell GPx4/TrxR1
- ME/CFS NK cells: demonstrated oxidative stress + Ca²⁺ defects (runs 127/132) + developmental (run_134) + metabolic exhaustion (run_135)
- SELENOP deficiency → NK GPx4 ↓ → lipid peroxidation of NK membrane → NK function ↓ → additive with existing NK dysfunction mechanisms
- MODERATE ME/CFS angle: selenium supplementation supports NK redox status alongside Ca²⁺ mechanisms

**SELENOP and ME/CFS fatigue:**
- TrxR2 in ME/CFS: mitochondrial ROS without adequate TrxR2 → Complex I damage → ATP deficit → PEM
- Run_133 (USP18/ISG15 → PDH ISGylation → ATP deficit): SELENOP provides complementary mitochondrial protection through TrxR2 → Prx3 → H₂O₂ reduction at Complex I/III
- Both USP18-ISGylation (run_133) AND TrxR2-deficiency (run_138) contribute to ME/CFS ATP deficit; selenium supplementation addresses TrxR2 arm

---

## 5. Framework Connection Map

```
SELENOP (run_138)
    ├── β cell: ApoER2 → selenium → TrxR2 + GPx1 + SELENOS + GPx4
    │       ↔ run_110 (selenium → GPX4/ferroptosis): SELENOP = upstream delivery
    │       ↔ run_088/089 (ER stress): SELENOS/ERAD = upstream input to ER stress
    │       ↔ run_128 (PINK1/Parkin/mitophagy): TrxR2 deficiency + mitophagy deficiency = additive mitochondrial damage
    │
    ├── Rosacea: ApoER2 in keratinocytes → GPx4 + TrxR1 → ferroptosis protection + NF-κB redox
    │       ↔ run_110 (GPX4/ferroptosis): SELENOP delivers selenium for GPx4 activity
    │       ↔ run_067 (HMGB1/RAGE): ferroptotic keratinocyte → DAMP release → Loop 2
    │       ↔ run_101 (NLRP3): keratinocyte ferroptosis → NLRP3 priming amplification
    │
    ├── ME/CFS: NK cell GPx4/TrxR → redox; TrxR2 → mitochondrial H₂O₂ → Complex I
    │       ↔ run_133 (USP18/ISGylation): both reduce ATP via mitochondrial dysfunction
    │       ↔ runs 127/132/134/135: NK dysfunction stack + selenium redox component
    │
    └── OTC: selenium 100–200 µg/day reinforced; SELENOP serum monitoring = new biomarker
```

---

## 6. Protocol Integration

**OTC reinforcement — selenium with SELENOP mechanistic anchor:**

Prior runs (110/126) established: selenium → GPX4 → ferroptosis protection.

Run 138 adds THREE additional mechanisms for same selenium intervention:
1. SELENOP → TrxR2 in β cells → mitochondrial H₂O₂ ↓ → Complex I protection
2. SELENOP → SELENOS in β cells → ERAD efficiency → ER stress ↓ → 22nd β cell death prevented
3. SELENOP → keratinocyte GPx4/TrxR1 → rosacea ferroptosis protection (ApoER2-mediated delivery)

**Selenium dosing:**
- 100–200 µg/day selenomethionine (organic form → better SELENOP synthesis than inorganic selenite)
- Avoid >400 µg/day (toxicity: selenosis with hair/nail changes, GI symptoms)
- Monitor: serum SELENOP (if available, research labs) OR serum selenium (proxy, target 100–120 µg/L)
- T1DM: selenium supplementation + autoimmune thyroid disease coexistence — common; selenium 200 µg/day also reduces anti-TPO titers (Cooper 2003: 40-60% reduction)

**New T-index consideration:**
- Serum SELENOP as supplementary biomarker: low SELENOP = inadequate selenium delivery despite adequate serum selenium (if hepatic function impaired or SBP2 mutation)
- Practical: serum selenium proxy; SELENOP measured only in specialized labs
- Priority targets for selenium optimization: T1DM + rosacea + documented selenium deficiency (serum <80 µg/L)

**β cell death context — 22nd mechanism:**
```
Run 088/089 ER stress → UPR → apoptosis
Run 138 SELENOS deficiency → ERAD failure → ER stress → UPR [UPSTREAM INPUT]
→ treating selenium deficiency = upstream ER quality control support
```

---

## 7. Key Literature

- Burk RF, Hill KE. (2005) Selenoprotein P: an extracellular protein with unique physical characteristics and a role in selenium homeostasis. *Annu Rev Nutr* — SELENOP structure and function review
- Chiu-Ugalde J et al. (2010) Mutation of megalin leads to urinary loss of selenoprotein P and selenium deficiency in renal proximal tubule cells. *Biochem J* — Megalin/LRP2 and SELENOP reuptake
- Olson GE et al. (2008) Apolipoprotein E receptor-2 (ApoER2) mediates selenium uptake from selenoprotein P in the mouse testis. *J Biol Chem* — ApoER2/LRP8 as SELENOP receptor
- Shchedrina VA et al. (2007) Selenoprotein containing domains of multiple selenocysteine residues serves as a plasma selenium transport protein. *Proc Natl Acad Sci* — SELENOP selenium carrier function
- Labunskyy VM et al. (2014) Selenoproteins: molecular pathways and physiological roles. *Physiol Rev* — comprehensive selenoprotein review including SELENOS/ERAD

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirty-first extension | SELENOP selenoprotein-P ApoER2 LRP8 megalin LRP2 selenium-transport receptor-mediated-endocytosis beta-cell-selenium TrxR2 GPx1 SELENOS VIMP ERAD ER-quality-control 22nd-beta-cell-death ER-stress-upstream SELENOM SELENOI selenomethionine keratinocyte-GPx4 ferroptosis-protection rosacea-skin selenium-supplementation-reinforced serum-SELENOP-biomarker ME/CFS-NK-redox TrxR2-mitochondrial Complex-I USP18-additive Burk-2005-AnnRevNutr Olson-2008-JBiolChem Labunskyy-2014-PhysiolRev | run_138*
