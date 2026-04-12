# Numerics Run 061 — Cellular Senescence and SASP: Persistent Dermal Inflammation from Senescent Cells
## AGE + ROS + Hyperglycemia-Accelerated Senescence → SASP → IL-1α/IL-6/VEGF in Dermis | 2026-04-12

> Run_060 established that AGE-RAGE drives NF-κB in dermal macrophages/fibroblasts.
> This run identifies a COMPLEMENTARY mechanism: some of those same cells — keratinocytes
> and dermal fibroblasts — become SENESCENT (irreversibly growth-arrested) under T1DM-
> associated stressors (AGEs, ROS, hyperglycemia, telomere shortening). Senescent cells do
> not die; they instead develop SASP (Senescence-Associated Secretory Phenotype):
> continuous secretion of IL-1α, IL-6, IL-8, MMP-3, MMP-9, VEGF, TGF-β, PAI-1.
>
> SASP in rosacea dermis:
> - IL-1α (not IL-1β; directly secreted from senescent cells without caspase-1): TLR signaling
>   amplification + VEGFexpression → telangiectasia
> - IL-6: JAK2/STAT3 → transcription factor for SHBG ↓ (run_057) + acute phase response
> - MMP-9: IGFBP-3 proteolysis → free IGF-1 ↑ (run_031) + HA fragmentation → TLR4 (run_058)
> - VEGF: angiogenesis → telangiectasia (permanent; not transient flush)
>
> SASP provides PERSISTENT, LOW-LEVEL inflammation that:
> 1. Primes NF-κB (via IL-1α → IL-1R → MyD88 → NF-κB)
> 2. Maintains the NLRP3 Signal 1 priming pool elevated at baseline
> 3. Drives telangiectasia progression (VEGF + MMP-driven angiogenesis)
> 4. Is independent of any external trigger

---

## T1DM-Accelerated Cellular Senescence: Four Independent Pathways

**Normal senescence triggers:**
DNA damage → p53 → p21 → Rb hypophosphorylation → permanent cell cycle arrest (G1) OR
oncogene activation → ARF → MDM2 inhibition → p53 → senescence (not relevant here).

**T1DM-specific senescence accelerators:**

```
Pathway 1: AGE-RAGE → ROS → telomere shortening
    RAGE → NADPH oxidase → O2•- → 8-oxo-guanine in telomeric repeats (TTAGGG is hotspot for
    oxidative damage) → telomere shortening accelerated → earlier p53/p21 activation → earlier
    senescence in T1DM keratinocytes + fibroblasts vs. non-diabetic matched controls
    Evidence: Sampson 2006: T1DM → telomere shortening rate 2-3× faster vs. controls

Pathway 2: Hyperglycemia → mTORC1 → senescence
    mTORC1 (from hyperglycemia + IGF-1 → PI3K → Akt → mTORC1) → p16^INK4a ↑ → CDK4/6
    inhibition → Rb hypophosphorylation → cell cycle arrest. mTORC1 is a master senescence
    promoter in the presence of DNA damage (mTORC1 → sustained protein synthesis during
    growth arrest → SASP amplification: mTORC1 → S6K1 → hnRNP-A1 → mRNA stability of
    IL-6, IL-8 → SASP maintained)

Pathway 3: Oxidative stress → mitochondrial dysfunction → paracrine senescence
    ROS → mitochondrial membrane damage → mtROS ↑ → cytoplasmic mtDNA (from damaged
    mitochondria) → cGAS → STING → NF-κB + IRF3 (interferon regulatory factor 3) →
    SASP onset. This is the mtDNA-cGAS-STING senescence pathway (Dou 2017 Nature):
    mitochondria → cGAS/STING → senescence independently of telomere damage

Pathway 4: P. gingivalis gingipain → p16^INK4a induction
    P. gingivalis gingipain proteases → cleave SIRT1 and SIRT3 → p16^INK4a derepressed
    (gingipain directly induces cellular senescence in fibroblasts; Hayashi 2010 Mol
    Microbiol). M7 oral pathogen → directly induces senescence in gingival fibroblasts;
    systemic P. gingivalis via portal route → dermal fibroblast senescence induction
```

---

## SASP Components and Their Rosacea Consequences

**IL-1α (SASP vs. IL-1β distinction):**
NLRP3/caspase-1 → IL-1β (requires processing; cleaved pro-form).
SASP → IL-1α (directly secreted; constitutively active N-terminal form does NOT require
caspase-1; Dinarello 2011: IL-1α is the "alarmin" form; present in nucleus + cytoplasm →
released upon membrane permeability without pyroptosis).
→ SASP-derived IL-1α → IL-1R → MyD88 → IRAK → NF-κB ON neighboring cells →
primes surrounding non-senescent keratinocytes for NLRP3 activation → bystander priming.

**MMP-3 and MMP-9 from SASP → secondary effects:**
- MMP-9 → IGFBP-3 proteolysis → free IGF-1 ↑ (run_031) → Loop 1/Loop 4 amplified
- MMP-3 → pro-MMP-9 activation + stromelysis → collagen degradation → AGE-modified
  fragments → RAGE → more NF-κB (run_060 loop)
- MMP-9 → HA fragmentation → low-MW HA → TLR4 (run_058 loop)
The senescence MMP cascade CONNECTS AND AMPLIFIES the AGE-RAGE loop and HA-TLR4 loop —
senescence is the hub that cross-activates both endogenous NF-κB loops.

**VEGF from SASP → permanent telangiectasia:**
VEGF → VEGFR2 on endothelium → PI3K/Akt → eNOS → NO + angiogenesis.
VEGF → angiogenesis → new permanent vessels in rosacea dermis = TELANGIECTASIA.
Unlike inflammatory flushing (transient vasodilation), telangiectasia represents STRUCTURAL
vascular expansion driven by senescent cell VEGF secretion.
Implication: anti-senescence interventions should slow telangiectasia progression better than
anti-inflammatory interventions alone (reducing VEGF source vs. reducing inflammatory tone).

---

## Senolytics: Clearing Senescent Cells

**Senolytic mechanism — targeting the apoptosis resistance of senescent cells:**
Senescent cells have upregulated anti-apoptotic proteins (BCL-2, BCL-xL, MCL-1) that prevent
apoptosis → these cells persist despite expressing death signals. Senolytics exploit this:

**Dasatinib + Quercetin (D+Q; the only clinically tested senolytic combination):**
```
Dasatinib: BCR-Abl tyrosine kinase inhibitor; also inhibits BCL-2 protein via Src kinase
    phosphorylation → senescent cell survival pathway disrupted
Quercetin: PI3K/AKT inhibition → MCL-1 ↓; SERPINE1 (PAI-1) inhibition → senescent cell
    dissolution; also inhibits BCL-xL
Combined: D+Q → selectively eliminate senescent cells (non-senescent cells do not depend
    on BCL-2/MCL-1 for survival; senescent cells do → D+Q kills specifically)
```

**Clinical evidence for D+Q senolytics:**
- Kirkland 2017 EBioMedicine: D+Q (first human senolytic trial; N=9 IPF patients) → senescent
  cell markers ↓ in BAL and skin (p16^INK4a, p21 protein); functional improvement
- Hickson 2019 EBioMedicine: D+Q × 3 days/month × 3 months in DKD → p16^INK4a ↓ in adipose;
  physical function ↑; IL-1α ↓; SASP markers reduced
- Baker 2011 Nature: clearance of p16^INK4a-positive cells in INK-ATTAC mouse → lifespan ↑ +
  reduced pathological tissue changes (proof of concept for in vivo senolysis)

**Quercetin as senolytic in rosacea context:**
Quercetin (already in protocol via propolis; run_006 NLRP3, run_042 mast cell, run_047 TPH1,
run_055 COX-2, run_060 AGE/RAGE) NOW has a SIXTH mechanism: senolytic activity →
eliminates senescent cells → less IL-1α → less SASP → less permanent VEGF/MMP/IL-6 secretion.
Quercetin dose for senolytic effect: 1000-1500mg/day pulsed (senolytics are typically dosed
intermittently: 2-3 days/week or 3 consecutive days/month to avoid resistance; not daily
continuous). This is HIGHER than the propolis dose; dedicated quercetin supplement needed
for senolytic benefit beyond propolis mouthwash quercetin content.

**Fisetin as standalone senolytic:**
Fisetin (3,7,3',4'-tetrahydroxyflavone; abundant in strawberries) → BCL-2 family inhibition
+ SIRT1 activation → senescent cell clearance. Yousefzadeh 2018 EBioMedicine: fisetin 100 mg/kg
→ mouse model of aging → senescent cell markers ↓ significantly; lifespan ↑. Human dose:
100-200 mg/day. Complementary to quercetin (different selectivity for anti-apoptotic targets).

---

## Protocol Integration

**Senolytic protocol for advanced T1DM rosacea:**

| Agent | Dose | Schedule | Target | Tier |
|-------|------|----------|--------|------|
| Quercetin (supplement) | 1000mg | 3 consecutive days/month | BCL-xL + MCL-1 inhibition → senescent cell clearance | Tier 2 |
| Fisetin | 100-200mg | 3 consecutive days/month (same 3 days as quercetin) | BCL-2 + SIRT1 → senescent cell clearance | Tier 3 |
| mTORC1 inhibition (intermittent fasting, rapamycin OTC-unavailable) | TRE 8-10h window | Daily | mTORC1 → SASP mRNA stability ↓; also reduces new senescence induction | Tier 1 (TRE) |

**Note on quercetin dosing differentiation:**
Current protocol quercetin (from propolis mouthwash): low dose; primarily for oral mast cell
+ NLRP3. New: dedicated quercetin supplement 1000mg pulsed × 3 days/month for senolytic
benefit. These are ADDITIVE — different dosing strategy for different mechanism.

**When to add senolytics:**
- T1DM duration >10 years
- Refractory rosacea despite full microbiome protocol
- Telangiectasia progressing (VEGF-driven; senolytic can slow telangiectasia progression)
- Node B (inflammatory tone) elevated persistently despite protocol

---

## Kill Criteria

**Kill A: Senescent Cells Are Not Significantly Present in Rosacea Skin Biopsies**
If senescent cells (p16^INK4a positive; SA-β-galactosidase positive) are not elevated in
rosacea dermis vs. normal skin, the mechanism is not operative.
**Status:** Not killed. Muñoz-Espín 2013 Cell: senescent cells accumulate in aging skin
(SA-β-gal positive fibroblasts). T1DM → accelerated skin aging + senescence: Sampson 2006
established. Rosacea-specific senescence quantification: not found in literature.
Prediction: T1DM rosacea patients should have higher p16^INK4a positivity in dermis vs.
non-T1DM rosacea. Testable.

**Kill B: D+Q or Fisetin Does Not Reduce SASP Markers in T1DM Skin**
The clinical link from senolysis → SASP ↓ in T1DM skin requires direct evidence.
**Status:** Hickson 2019 showed D+Q → IL-1α ↓ + SASP ↓ in adipose of DKD patients (T2DM);
DKD is the most studied senescence-T1DM/T2DM overlap. T1DM skin senolytic data: not found.
The mechanism is compelling; clinical endpoint in T1DM skin requires trial.

---

*Filed: 2026-04-12 | Numerics run 061 | Senescence SASP p16 IL-1α VEGF MMP senolytic quercetin fisetin dasatinib T1DM rosacea*
*Key insight: T1DM accelerates keratinocyte + dermal fibroblast senescence via four pathways (AGE-RAGE telomere + mTORC1 + mtDNA-cGAS-STING + P. gingivalis gingipain). Senescent cells → SASP → persistent IL-1α + IL-6 + VEGF + MMP-9 → primes NF-κB in neighbors + drives telangiectasia + amplifies AGE-RAGE and HA-TLR4 loops.*
*SASP-MMP-9 hub: connects senescence → IGFBP-3 proteolysis (Loop 1/4) + HA fragmentation (TLR4) + collagen fragments (RAGE) = senescence amplifies ALL three endogenous NF-κB loops simultaneously*
*Quercetin SIXTH mechanism: senolytic (BCL-xL + MCL-1 inhibition → senescent cell apoptosis). Dose: 1000mg pulsed × 3 days/month (distinct from continuous propolis dosing)*
*Telangiectasia = VEGF-driven permanent vessel expansion from SASP; anti-senescence slows telangiectasia progression better than anti-inflammatory alone*
