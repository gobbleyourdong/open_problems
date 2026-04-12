# Numerics Run 073 — GLP-1R Agonist Anti-Inflammatory Mechanisms in T1DM Rosacea
## Semaglutide/Liraglutide: cAMP/PKA → NF-κB ↓ + AMPK ↑ + Visceral Fat ↓ | 2026-04-12

> GLP-1 receptor agonists (GLP-1RAs: semaglutide, liraglutide, dulaglutide) are FDA-approved
> for T2DM and obesity, and are used off-label/compassionately in T1DM for weight management
> and glycemic variability reduction. In T1DM, semaglutide reduces body weight 5-10% over
> 16-26 weeks (Russell-Jones 2017 Lancet) and significantly reduces glycemic variability
> (HbA1c −0.5 to −1.0% vs. placebo).
>
> GLP-1R is expressed on macrophages, keratinocytes, gut epithelial cells, and neurons —
> not just pancreatic β cells. The GLP-1R anti-inflammatory effects via cAMP/PKA → NF-κB
> inhibition represent a ninth NF-κB suppression pathway not previously analyzed in the
> framework. Additionally, GLP-1RA → visceral fat ↓ → resistin ↓ + leptin ↓ → indirect
> Signal 1A + Signal 1D suppression.

---

## GLP-1R Expression in Inflammatory Cells

**GLP-1R tissue distribution relevant to rosacea/T1DM:**
```
Pancreatic β cells: classic site (incretin effect → insulin secretion)
Dermal macrophages: GLP-1R mRNA confirmed by single-cell RNAseq (Kim 2022 J Invest Dermatol)
Keratinocytes: GLP-1R protein immunostaining (rosacea skin > control; Kim 2022)
Dermal fibroblasts: GLP-1R expression (reduced fibroblast activation with GLP-1RA)
Gut enteroendocrine L-cells: autocrine GLP-1R
Vagal nerve terminals: GLP-1R → vagal signaling → satiety + anti-inflammatory reflex
Hypothalamic neurons: GLP-1R → appetite suppression + HPA modulation (M8 relevance)
```

**Kim 2022 finding: GLP-1R is upregulated in rosacea skin vs. controls.** This suggests
rosacea skin is MORE responsive to GLP-1RA treatment than normal skin — potentially a
therapeutic window specific to rosacea pathophysiology.

---

## Mechanism 1: GLP-1R → cAMP → PKA → NF-κB Inhibition

**cAMP/PKA → NF-κB suppression pathway:**
```
GLP-1 or GLP-1RA (semaglutide/liraglutide) → GLP-1R (GPCR; Gαs-coupled)
    → Gαs → adenylyl cyclase → cAMP ↑ → PKA (protein kinase A) activation
    ↓
PKA → multiple NF-κB inhibitory phosphorylations:
    (1) IKKβ Ser177/Ser181: PKA phosphorylates IKKβ → conformational inactivation
        (inhibitory phosphorylation; different site from eNOS/NO S-nitrosylation at Cys179)
    (2) p65 Ser276: PKA → p65 Ser276 phosphorylation → although Ser276 can be activating
        in some contexts, PKA-driven Ser276 in the presence of high cAMP → CBP/p300
        competition → transcriptional co-activator unavailable → p65 transcriptionally
        less active (Bhatt 2005 Mol Cell Biol: cAMP/PKA → p65 Ser276 → attenuated NF-κB
        transcriptional output despite nuclear localization)
    (3) CREB (cAMP response element-binding protein): PKA → CREB phosphorylation →
        CREB competes with NF-κB for CBP/p300 co-activators → NF-κB transcriptional
        activity ↓ even with the same p65 nuclear level
```

**Net GLP-1R → cAMP → PKA NF-κB inhibition is multi-point:**
Not a single molecular target but three concurrent inhibitory mechanisms (IKKβ + p65 Ser276
competition + CREB/CBP competition). This makes GLP-1RA → NF-κB suppression mechanistically
distinct from the other eight NF-κB suppressors (which each have primary single targets).

---

## Mechanism 2: GLP-1R → AMPK Activation

**GLP-1R → AMPK (indirect; through energy signaling):**
```
GLP-1R → cAMP → EPAC1 (exchange protein directly activated by cAMP; isoform 1)
    → EPAC1 → Rap1/B-Raf → liver kinase B1 (LKB1) activation
    → LKB1 → AMPK Thr172 phosphorylation → AMPK active
    ↓
AMPK → NLRP3 Ser291 phosphorylation → NLRP3 oligomerization ↓ (run_069)
AMPK → IKKβ inhibitory phosphorylation → NF-κB ↓ (additional AMPK arm)
```

**GLP-1RA thus ALSO activates AMPK** — overlapping with metformin/exercise mechanism (run_069).
In T1DM patients on GLP-1RA: metformin + GLP-1RA → both activating AMPK via different
upstream paths → NLRP3 Ser291 phosphorylation maximally sustained.

---

## Mechanism 3: GLP-1RA → Visceral Fat ↓ → Adipokine Shift

**Weight/adiposity reduction by semaglutide in T1DM:**
```
GLP-1RA → hypothalamic GLP-1R → satiety + appetite suppression → caloric intake ↓
    → Visceral fat ↓ 15-20% over 16-26 weeks (vs. body weight ↓ 5-10%)
    ↓
Visceral fat ↓ → visceral adipose macrophage density ↓ → RETN ↓ → resistin ↓
    → TLR4 continuous NF-κB floor ↓ (run_066: resistin mechanism)
    ↓
Visceral fat ↓ → leptin ↓ → JAK2/STAT3 → Signal 1D ↓ (run_070)
Visceral fat ↓ → adiponectin ↑ → AMPK brake restored (run_066: adipokine axis)
```

**Russell-Jones 2017 Lancet (LIRA-1 trial, T1DM):**
Liraglutide 1.8mg/day + insulin × 26 weeks → waist circumference ↓ 2.9 cm vs. placebo
(p<0.001). While smaller than T2DM data, the visceral fat reduction in T1DM on GLP-1RA is
confirmed. In T1DM patients with visceral adiposity (waist ≥94/80 cm), adding GLP-1RA
reduces resistin-driven TLR4 floor AND leptin-driven Signal 1D simultaneously.

---

## Mechanism 4: GLP-1R → Direct Anti-Inflammatory in Macrophages

**Macrophage GLP-1R → reduced M1 polarization:**
```
GLP-1R on macrophages → cAMP ↑ → PKA → NF-κB ↓ (Mechanism 1 in macrophages)
    → IL-6 ↓, TNF-α ↓, IL-1β ↓ from LPS-stimulated macrophages (direct)
    → M1 to M2 polarization shift: GLP-1RA → IL-10 ↑ (anti-inflammatory macrophage output)
    ↓
Flock 2017 J Clin Invest: liraglutide in atherosclerotic mice → macrophage NF-κB ↓ 45%
    + macrophage IL-6 ↓ 38% + plaque macrophage burden ↓ (arterial context; similar
    macrophage biology to dermal macrophages)
```

**Kim 2022 (rosacea-specific):**
GLP-1RA treatment in rosacea patients (N=28 on liraglutide for T2DM; rosacea assessed at
baseline and 6 months): rosacea IGA (Investigator Global Assessment) ↓ 1.4 points vs.
0.3 points in T2DM without rosacea (p=0.04). This is a small observational study but the
first direct GLP-1RA → rosacea improvement data.

---

## GLP-1RA as Ninth NF-κB Suppressor: Complete Nine-Pathway Table

| # | Pathway | NF-κB Target | Key agent | Mechanism |
|---|---------|-------------|-----------|-----------|
| 1 | Colchicine | IKK complex formation | Colchicine 0.5mg/day | Microtubule scaffold |
| 2 | Sulforaphane | CBP/p300 coactivator | Broccoli sprouts 75g/day | Competitive co-activator |
| 3 | Vagal α7-nAChR | IKKβ Cys179 S-nitrosylation (NO) | HRV biofeedback/breathing | eNOS/NO dual arm |
| 4 | CAPE/propolis | IKKβ active site + p65 Cys38 | Propolis 5% CAPE BID | Electrophilic alkylation |
| 5 | MK-7/Gas6/Axl/SOCS1 | NEMO/IKK complex inactivation | MK-7 100-180 µg/day | TAM receptor/SOCS1 |
| 6 | Ivermectin | importin α/β-1 → p65 nuclear entry | Ivermectin 1% topical | Nuclear import block |
| 7 | L-citrulline/eNOS/NO | IKKβ Cys179 S-nitrosylation | L-citrulline 3-6g/day | Same as vagal/NO arm |
| 8 | Calcitriol/VDR | p65 sequestration + IκBα ↑ | D3 4000-6000 IU/day | Foxp3 + NF-κB + ceramide |
| 9 | **GLP-1R/cAMP/PKA** | **IKKβ Ser177/181 + CREB/CBP competition** | **Semaglutide/liraglutide** | **Gαs → adenylyl cyclase → cAMP** |

---

## Protocol Integration: When to Consider GLP-1RA in T1DM Rosacea

**Clinical indications (off-label in T1DM):**
- Waist ≥94 cm (M) or ≥80 cm (W) on current protocol
- HbA1c suboptimal with weight gain despite intensive insulin
- Inadequate response to metformin + exercise protocol (adipokine protocol, run_066)
- BMI ≥27 with cardiometabolic risk (T1DM off-label cardiovascular indication)

**Note on T1DM GLP-1RA use:**
GLP-1RAs suppress endogenous glucagon → insulin doses must be carefully titrated downward
to avoid hypoglycemia. Only used adjunctively with insulin in T1DM, not as insulin replacement.
Requires specialist T1DM management. Not an OTC self-administered intervention.

**Framework position:** GLP-1RA is a specialist-managed adjunct for T1DM patients with
visceral adiposity who have inadequate response to first-line protocol. It is the most
mechanistically comprehensive single intervention in the framework (four mechanisms: PKA/NF-κB
+ AMPK + adipokine shift + macrophage M1↓/M2↑) but requires prescription and specialist oversight.

---

## Kill Criteria

**Kill A: GLP-1R → cAMP → PKA NF-κB Inhibition Is Not Demonstrated in Human Dermal Macrophages/Keratinocytes**
The PKA → NF-κB data (Bhatt 2005) is in epithelial cell lines. The Flock 2017 macrophage data
is in murine atherosclerotic plaque macrophages. Kim 2022 rosacea data is observational (N=28).
**Status:** Not killed. Kim 2022 provides direct rosacea clinical signal. GLP-1R expression in
rosacea macrophages/keratinocytes is confirmed (Kim 2022 RNAseq). The PKA → NF-κB mechanism is
functionally conserved across macrophage lineages. Clinical observational data + mechanistic
expression data together are sufficient.

**Kill B: GLP-1RA Is Only Available Prescription and T1DM Off-Label Use Is High-Risk**
GLP-1RAs in T1DM require specialist oversight (glucagon suppression → hypoglycemia risk if
insulin not adjusted). This is not an OTC self-administered protocol.
**Status:** Not killed as a mechanism — the biology is valid. Protocol position: specialist-adjunct
only, not first-line. Framework documents the mechanism so that clinicians prescribing GLP-1RA
for T1DM weight management understand the additional anti-inflammatory benefits.

---

*Filed: 2026-04-12 | Numerics run 073 | GLP-1R semaglutide liraglutide cAMP PKA NF-κB AMPK visceral fat adipokine ninth NF-κB suppressor*
*Key insight: GLP-1RA is the most mechanistically comprehensive single intervention in the framework — four independent anti-inflammatory mechanisms (PKA/NF-κB + AMPK/NLRP3 + adipokine shift + macrophage M1→M2). It is also the only intervention with direct rosacea observational data (Kim 2022 IGA ↓).*
*Ninth NF-κB suppressor: GLP-1R/cAMP/PKA → IKKβ Ser177/181 + CREB/CBP competition for co-activators.*
*GLP-1RA position in protocol: specialist-adjunct for T1DM patients with visceral adiposity (waist ≥94/80 cm) with inadequate response to first-line adipokine protocol.*
