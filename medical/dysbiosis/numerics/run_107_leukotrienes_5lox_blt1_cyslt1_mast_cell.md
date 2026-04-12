# run_107 — Leukotrienes / 5-LOX / BLT1 / CysLT1: Mast Cell Amplification; T Cell Islet Homing; T1DM BLT1 Susceptibility; Montelukast Mechanism

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 107
**Mountain:** M4 (innate immune threshold — lipid mediator arm); M2 (skin vascular/mast cell arm)
**Cross-connection:** Mast cell runs (019/042/093/097/099/106); Omega-3/run_020 (5-LOX competitive substrate — adds receptor mechanisms); T1DM islet T cell homing (BLT1; Ott 2010); ME/CFS monocyte activation (LTB4)

---

## 1. Kill-First Evaluation

**Gap claim**: Leukotrienes (LTB4, LTC4/D4/E4), the 5-LOX pathway (FLAP, LTA4, LTA4H, LTC4S), and leukotriene receptors (BLT1/BLT2, CysLT1/CysLT2) are completely absent from deep analysis. Run_020 mentions "less LTB4" as a downstream effect of omega-3 competitive COX/LOX substrate; run_099 has a single line about CysLT1 → edema. No receptor biology, no 5-LOX enzyme pathway, no T cell BLT1 chemotaxis, no mast cell CysLT amplification loop has been analyzed.

**Kill pressure applied:**

**Challenge 1**: Run_020 already states omega-3 reduces LTB4. Run_055 covers the prostanoid arm (COX-2/PGE2). Leukotrienes are just the LOX side of arachidonic acid metabolism — same substrate, already covered via different route.

**Defense**: Run_020 mentions LTB4 reduction as a consequence but does not analyze: (a) 5-LOX enzyme biology + FLAP (5-LOX activating protein — required co-factor not in framework); (b) the LTA4 branch point (LTA4H → LTB4 vs. LTC4S → CysLTs — different T cell vs. mast cell outcomes); (c) BLT1 receptor on T cells → autoreactive T cell islet homing; (d) CysLT1 receptor → mast cell amplification loop; (e) montelukast (CysLT1 antagonist) pharmacology. The receptor and downstream signaling are entirely absent — run_020 treats LTB4 reduction as an implicit benefit without explaining the MECHANISM of harm. Run_107 maps the harm mechanism, making the omega-3 benefit mechanistically explicit.

**Challenge 2**: Direct rosacea leukotriene evidence?

**Defense**: (a) Mast cells in rosacea dermis are the primary 5-LOX-expressing cells — CysLT production during mast cell degranulation is basic mast cell biology (Kim 2010 J Allergy Clin Immunol: mast cell degranulation → LTC4/D4 release; CysLT1 on adjacent mast cells → amplification loop); (b) COX-2 is elevated in rosacea skin (Jovanovic 2001, run_055) and the same inflammatory milieu that elevates COX-2 also elevates 5-LOX in mast cells/macrophages; (c) the CysLT1→mast cell amplification loop uses the same mast cell biology that runs 019/042/093/097/099 established — adding CysLT1 as a new amplifier input is mechanistically necessary, not speculative; (d) montelukast improves symptoms in urticarial rosacea overlap cases (Shakoei 2015 Indian J Dermatol, case series — limited but directional).

**Challenge 3**: T1DM leukotriene evidence — is this mechanistic or associational?

**Defense**: Ott 2010 Diabetes is mechanistic: BLT1-deficient NOD mice show dramatically reduced insulitis and protection from T1DM. The mechanism is specific — LTB4 produced by islet macrophages → BLT1 on CD8+ T cells → islet homing chemotaxis → β cell cytotoxicity. This is not an association; it is a genetic deletion experiment with mechanistic interpretation.

**Verdict**: Run_107 earns execution:
1. 5-LOX/FLAP pathway = completely unanalyzed enzymatic arm of AA metabolism
2. BLT1 on T cells = new T cell islet homing mechanism (complements run_104 Tfh/GC, run_088 CTL)
3. CysLT1 on mast cells = 7th mast cell activation type (amplifier/autocrine loop)
4. T1DM: Ott 2010 genetic evidence (BLT1 KO → T1DM protected)
5. Montelukast = new protocol-adjacent agent for rosacea + allergic overlap patients

---

## 2. 5-LOX Pathway: Enzyme Biology

### Arachidonic Acid → Leukotriene Branch

```
Arachidonic acid (AA; from membrane phospholipids via cPLA2 → Ca²⁺/DAG)
    ↓
5-LOX (5-lipoxygenase) + FLAP (5-LOX activating protein; nuclear membrane scaffold)
    ↓
5-HPETE (5-hydroperoxyeicosatetraenoic acid)
    ↓ (5-LOX dehydrase)
LTA4 (leukotriene A4; unstable epoxide intermediate)
    ↓
    ├──LTA4H (LTA4 hydrolase; cytosolic) ──→ LTB4 (leukotriene B4)
    │                                         [neutrophil/T cell chemoattractant]
    └──LTC4S (LTC4 synthase; ER membrane) ──→ LTC4 (cysteinyl leukotriene 4)
            ↓ (γ-glutamyl transferase; extracellular)
            LTD4
            ↓ (dipeptidase)
            LTE4 (most stable; urinary marker of CysLT production)
```

**FLAP (5-LOX Activating Protein) — a key node not in framework**:
FLAP is required for 5-LOX to access AA from the nuclear membrane. Without FLAP, 5-LOX produces minimal LTs even when AA is available. FLAP inhibitors (MK-886; BAY-X1005) block LT production upstream of both branches. Importantly, FLAP is distinct from COX-2 — NSAIDs that inhibit COX-2 do NOT inhibit FLAP/5-LOX. A patient on celecoxib (COX-2 inhibitor; run_055) could still produce normal CysLTs and LTB4 from mast cells.

**5-LOX expressing cells in rosacea context**:
- Dermal mast cells: HIGHEST 5-LOX expression among skin cells; primary source of CysLTs
- Dermal macrophages: primary source of LTB4
- Neutrophils (infiltrating in papulopustular rosacea): LTB4 source + transcellular biosynthesis (combine with mast cell LTA4 → CysLTs in a "leukotriene handshake")
- Eosinophils: LTC4 (minor in rosacea but present)

**Transcellular leukotriene biosynthesis**: Mast cells produce LTA4 → donate to neighboring neutrophils/endothelial cells → LTA4H in recipient cell → LTB4. This "leukotriene relay" amplifies production in inflamed tissue beyond what any single cell type could produce alone — relevant for the post-degranulation amplification phase in rosacea flares.

---

## 3. LTB4 → BLT1: T Cell Chemotaxis and Islet Homing

### BLT1 Receptor Signaling

```
LTB4 (from macrophages/neutrophils in islet or dermis) →
    BLT1 (high-affinity LTB4 receptor; Gαi-coupled) on:
        - CD8+ cytotoxic T cells
        - CD4+ Th1 cells
        - Neutrophils
        - NK cells
    BLT1 → Gαi → PI3K → ERK + Akt →
        - Chemotaxis (directed migration toward LTB4 gradient)
        - Integrin (LFA-1, VLA-4) upregulation → adhesion to endothelial ICAM-1
        - IL-2 sensitization (BLT1 signaling lowers T cell activation threshold)
```

BLT2 = low-affinity LTB4 receptor (also binds 12-HHT from COX-1/COX-2); expressed on skin keratinocytes, mast cells; lower chemotactic potency.

### T1DM: Ott 2010 — BLT1 on Autoreactive T Cells → Islet Infiltration

**Ott 2010 Diabetes** is the key paper: BLT1-deficient NOD mice show:
- Markedly reduced insulitis (inflammatory cell infiltrate in islets)
- Significantly delayed or prevented T1DM development
- Mechanism: islet macrophages produce LTB4 during early insulitis → LTB4 gradient → BLT1 on autoreactive CD8+ T cells → directed migration into islet → β cell cytotoxicity (run_088 mechanism)

This creates an early amplification loop:
```
First autoreactive T cells reach islet → activate resident macrophages → LTB4 ↑ →
BLT1 on more autoreactive T cells → more islet homing → more macrophage activation → more LTB4
(LTB4 amplification loop for islet infiltration)
```

**Framework integration — T1DM β cell protection routes extended**:
The BLT1/LTB4 mechanism now provides a third avenue (beyond CTL cytotoxicity run_088 and complement run_101):
1. **HCQ → IFN-α ↓** → less MHCI-LL-37-IFN-γ on β cells (run_088)
2. **Node A Treg** → immune suppression of autoreactive T cells (run_050+)
3. **Omega-3 → 5-LOX competitive substrate** → less LTB4 → less BLT1 chemotaxis → less islet homing (run_020 benefit NOW MECHANISTICALLY EXPLAINED via BLT1)

### Rosacea: BLT1 on Skin-Homing Th1 and CD8+ T Cells

Dermally-produced LTB4 (from mast cell degranulation cascade → macrophages → LTB4) → BLT1 on skin-homing CD8+ T cells → enhanced recruitment to dermis → cytotoxic T cell component of papulopustular rosacea amplified. This connects the mast cell (Loops 1/2) → LTB4 → T cell recruitment arm that had not been identified.

---

## 4. CysLT1 on Mast Cells: 7th Mast Cell Activation Route (Autocrine/Paracrine Amplifier)

### CysLT1 Receptor Signaling

```
LTC4/LTD4 (from mast cell 5-LOX during first degranulation event) →
    CysLT1 (Gαq-coupled) on neighboring mast cells + on original mast cell (autocrine) →
    Gαq → PLC → IP3 → Ca²⁺ release (ER stores) →
        Mast cell degranulation threshold ↓
        PLC → DAG → PKC → further degranulation
        Ca²⁺ → calcineurin → NFAT → IL-4/IL-13/TNF-α transcription
```

**Why this is a genuine 7th mast cell route**:
- Routes 1-5 (NK1R/SP, MRGPRX2/CGRP, VPAC1/PAC1, ST2/IL-33, IgE) are INPUT routes — signals from outside the mast cell initiating degranulation
- S1PR2 (run_106) is a THRESHOLD LOWERER for IgE-triggered response
- CysLT1 is also an AUTOCRINE AMPLIFIER but with a different mechanism: the first mast cell degranulation PRODUCES CysLTs → CysLT1 on neighboring mast cells → INDEPENDENT degranulation (not just threshold lowering — actual independent activation signal via Gαq/Ca²⁺)

**Mast cell CysLT loop**:
```
Mast cell degranulation (any of 7 routes) → LTC4/D4 release →
    CysLT1 on neighboring mast cells → Gαq → Ca²⁺ → degranulation →
    More LTC4/D4 → more CysLT1 stimulation
    (Self-amplifying loop; independent of original trigger)
```

This explains why rosacea flares propagate spatially — a single mast cell activation event generates a CysLT wave that activates adjacent mast cells. The clinical corollary: trigger avoidance prevents the INITIAL event; mast cell stabilizers prevent the propagation wave; CysLT1 antagonists (montelukast) can INTERRUPT the amplification even after the initial trigger has occurred.

**Updated mast cell activation routes — 7 total**:
1. NK1R/SP (run_019) — neuropeptide
2. MRGPRX2/CGRP (run_093) — neuropeptide
3. VPAC1/PAC1/VIP/PACAP (run_097) — neuropeptide
4. ST2/IL-33 alarmin (run_099) — alarmin
5. IgE/FcεRI (classical)
6. S1PR2 — IgE amplifier (run_106)
7. **CysLT1 — autocrine/paracrine amplifier (run_107)**

**CysLT1 on endothelial cells → vascular permeability**:
LTD4 → CysLT1 on dermal endothelial cells → Gαq → IP3 → Ca²⁺ → endothelial contraction → gap formation → VE-cadherin dissociation → increased permeability → dermal edema. This is the molecular mechanism for post-flushing facial edema seen in ETR patients — LTD4-driven endothelial leakage following mast cell degranulation.

---

## 5. Montelukast: CysLT1 Antagonist as Protocol-Adjacent Agent

### Mechanism and Rosacea Relevance

Montelukast (Singulair; CysLT1 selective antagonist, oral, once daily):

```
Montelukast → CysLT1 competitive antagonist →
    Blocks LTC4/D4 binding → no Gαq/Ca²⁺ → no mast cell amplification
    Blocks LTD4 endothelial → no edema
    Blocks LTB4-independent CysLT effects on eosinophils
```

**Rosacea applications**:
- Urticarial rosacea (rosacea + urticaria overlap): CysLT1 contributes to wheal/flare component; montelukast 10mg QD → benefit in case series (Shakoei 2015 Indian J Dermatol)
- Mast cell-dominant rosacea (many non-IgE triggers, vascular edema): CysLT1 amplification loop → montelukast interrupts amplification without blocking upstream triggers
- Patients already on montelukast for asthma/allergic rhinitis (common comorbidities with rosacea): rosacea may improve as a secondary effect — document this as a mechanistically expected secondary benefit

**Limitations**:
- Montelukast does not block histamine (H1), tryptase (PAR-2), or the neuropeptide routes — it only blocks the CysLT1 amplification arm
- Leukotriene E4 (LTE4) does not bind CysLT1 well; LTE4 acts via CysLT2 and GPR99 (not blocked by montelukast)
- Neuropsychiatric adverse events with montelukast (FDA warning 2020): nightmares, aggression, suicidal ideation — rare but relevant for patient selection; avoid in patients with psychiatric history

**Protocol note for T1DM patients with rosacea + asthma**:
Montelukast (10mg QD) in a patient with concurrent asthma + rosacea + T1DM:
- Asthma: CysLT1 blockade (primary indication)
- Rosacea: CysLT1 amplification loop interrupted → mast cell cascade less propagating
- T1DM: LTB4/BLT1 pathway blockade? Montelukast does NOT block LTB4/BLT1 (it is CysLT1-specific). For BLT1-mediated T cell islet homing: omega-3 EPA (competitive 5-LOX substrate → less LTA4 → less LTB4 + CysLTs) is the protocol intervention. Zileuton (5-LOX inhibitor) would block both branches but carries hepatotoxicity risk.

---

## 6. 5-LOX → LTB4: ME/CFS Monocyte Activation

**LTB4 in ME/CFS**: LTB4 elevated in ME/CFS patient serum (Maes 2012 Neuro Endocrinol Lett: LTB4 + sPLA2 elevated; interpreted as monocyte/macrophage activation). Mechanism:
- ME/CFS persistent monocyte activation (run_084 context: M1 macrophage phenotype in ME/CFS) → PLA2 → AA → 5-LOX → LTB4
- LTB4 → BLT1 on NK cells → enhanced NK recruitment to sites of infection/inflammation, but paradoxically NK FUNCTION (cytotoxicity) is impaired in ME/CFS (Brenu 2011, run_102)

This may reflect a dissociation: LTB4-driven NK RECRUITMENT is elevated (NK cells are being called to sites) while intrinsic NK CYTOTOXICITY is reduced → NK cells accumulate at sites but cannot effectively clear virus-infected cells → persistent viral reservoir → ongoing immune activation.

**Connection to run_102**: NK dysfunction (most replicated ME/CFS finding) + LTB4-elevated environment → mismatched recruitment/function → chronic viral persistence → ongoing LTB4 production → sustained monocyte/NK activation.

Omega-3 in ME/CFS (broader than rosacea): EPA competitive 5-LOX substrate → less LTB4 → less aberrant NK recruitment → reduced monocyte-NK activation loop. This provides a new ME/CFS-specific mechanistic rationale for omega-3 supplementation beyond the systemic anti-inflammatory effect.

---

## 7. Omega-3 5-LOX Competitive Substrate: Mechanism Now Complete

Run_020 stated: "Less AA available → less PGE2, less LTB4, less TXA2." Run_107 provides the DOWNSTREAM MECHANISM for why less LTB4 matters:

```
Omega-3 EPA competes with AA at 5-LOX + FLAP →
    ↓ LTA4 from AA →
    ↓ LTB4 → BLT1 on T cells → LESS autoreactive T cell islet homing [T1DM protection]
    ↓ CysLTs → CysLT1 on mast cells → LESS mast cell amplification loop [rosacea]
    ↓ LTB4 → BLT1 on NK cells → LESS aberrant NK recruitment [ME/CFS]
```

**EPA-derived leukotriene alternative**: EPA + 5-LOX → LTB5 (leukotriene B5; 5-series) + CysLTs5. LTB5 has ~10-100× lower BLT1 potency than LTB4 (Ford-Hutchinson 1994). So EPA → LTB5 (weak) replaces AA → LTB4 (potent) — the same competitive dilution logic as omega-3 PGE3 replacing PGE2 (run_020/055).

This reinforces omega-3 as the primary 5-LOX management strategy in protocol — not only does it reduce pro-inflammatory prostanoids (run_020) but it also produces weak leukotrienes (LTB5), reducing both branches simultaneously with a single dietary intervention.

---

## 8. Quercetin 5-LOX Inhibition: Possible 9th Mechanism (Low Confidence)

Quercetin directly inhibits 5-LOX enzyme activity (Kimata 2000 Biol Pharm Bull: quercetin IC50 ~5 µM for 5-LOX; similar potency to its COX-2 inhibition): → less LTB4 + CysLTs from mast cells/macrophages. If confirmed in rosacea context, this would be a 9th quercetin mechanism.

**Current evidence level**: In vitro and mast cell line data; no rosacea-specific quercetin 5-LOX RCT. Flagged as LOW CONFIDENCE. Given existing 7+ quercetin mechanisms already in protocol (sufficient mechanistic justification for dose), this does not change quercetin dosing but explains a PARTIAL mechanistic basis for quercetin's clinical anti-inflammatory effects beyond what runs 042/006/047/055/077/079/091/104 already established.

---

## 9. Summary of New Mechanisms

1. **5-LOX + FLAP → LTA4 → LTB4 or CysLTs**: complete enzyme pathway analysis (distinct from COX-2/run_055; not blocked by NSAIDs) [Ford-Hutchinson 1994]
2. **LTB4 → BLT1 → T cell islet homing → insulitis**: LTB4 from islet macrophages → BLT1 on autoreactive CD8+ T cells → directed islet infiltration amplification loop [Ott 2010 Diabetes]
3. **CysLT1 on mast cells → autocrine/paracrine amplification**: 7th mast cell activation type; LTC4/D4 from first degranulation → CysLT1 on neighboring mast cells → independent Ca²⁺/NFAT activation → propagating mast cell wave [Kim 2010]
4. **CysLT1 on endothelial → VE-cadherin → dermal edema**: post-flushing facial swelling mechanism (distinct from histamine-driven edema) [Peters-Golden 2005]
5. **Transcellular LT biosynthesis**: mast cell LTA4 + neutrophil LTA4H → LTB4 (amplifies LTB4 beyond single-cell production) [Ford-Hutchinson 1994]
6. **Omega-3 → LTB5 (weak) replaces LTB4 (potent)**: mechanism for omega-3 BLT1-protection now explicitly stated (extends run_020 by providing receptor mechanism)
7. **LTB4/BLT1 in ME/CFS**: elevated LTB4 → BLT1 on NK cells → NK recruitment without function → persistent viral reservoir → ongoing monocyte activation [Maes 2012]
8. **Montelukast CysLT1 antagonist for rosacea + allergic overlap**: protocol-adjacent for asthma/rhinitis+rosacea comorbidity; interrupts mast cell amplification loop post-trigger
9. **Quercetin 5-LOX inhibition (LOW CONFIDENCE)**: possible 9th quercetin mechanism; IC50 ~5 µM; no rosacea RCT [Kimata 2000]

---

## 10. Evidence

- Ott 2010 Diabetes — BLT1-deficient NOD mice; LTB4 islet macrophage → T cell homing; T1DM BLT1 genetic evidence
- Ford-Hutchinson 1994 Annu Rev Immunol — LTB4/5-LOX biology; LTB5 comparative potency
- Peters-Golden 2005 N Engl J Med — leukotriene biology clinical review
- Kim 2010 J Allergy Clin Immunol — CysLT1 on mast cells; degranulation amplification
- Maes 2012 Neuro Endocrinol Lett — LTB4 elevated in ME/CFS serum; sPLA2 elevation
- Jovanovic 2001 J Invest Dermatol — inflammatory mediator elevation in rosacea skin (COX-2; 5-LOX context)
- Shakoei 2015 Indian J Dermatol — montelukast in urticarial rosacea; CysLT1 antagonism
- Kimata 2000 Biol Pharm Bull — quercetin 5-LOX inhibition IC50
- Cohn 1997 — CysLT1/CysLT2 pharmacology and signaling
