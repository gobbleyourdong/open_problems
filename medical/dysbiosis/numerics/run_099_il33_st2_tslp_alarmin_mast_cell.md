# run_099 — IL-33 / ST2 / TSLP: Alarmin Pathway Mast Cell Activation in Rosacea

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 99
**Mountain:** M2 (skin barrier/keratinocyte damage) → M8 (mast cell/neurogenic) cross-connection
**Loop:** Loop 1 amplification (tryptase → PAR-2 → KLK5)

---

## 1. Kill-First Evaluation

**Gap claim**: IL-33/ST2/TSLP alarmin axis — completely absent from all 98 runs. Present in rosacea lesional skin (Zhao 2020). Potential 4th non-IgE mast cell activation route. ST2 → mast cell → tryptase → PAR-2 → KLK5 = Loop 1 amplification connection not previously mapped.

**Kill pressure applied:**

**Challenge 1**: IL-33 is primarily an atopic dermatitis / Th2 axis alarmin. Rosacea is Th17/Th1-dominant. Is IL-33 merely a minor bystander in rosacea?

**Defense**: The key distinction is that IL-33 → ST2 → mast cell degranulation occurs *before* T cell polarization downstream. The immediate consequence — tryptase + histamine + PGE2 release — feeds into vasodilation and, critically, tryptase → PAR-2 → KLK5 amplification (Loop 1). This is T cell polarization-independent. Even in a Th17-dominant disease, mast cell tryptase release from UV-damaged keratinocytes via IL-33/ST2 is mechanistically plausible and connects to Loop 1. The downstream ILC2/Th2 skewing is less relevant to rosacea — but the mast cell immediate activation route is what matters.

**Challenge 2**: Does the tryptase → PAR-2 → KLK5 link hold in human rosacea skin?

**Defense**: PAR-2 expression is elevated in rosacea skin (Steinhoff 2011 J Invest Dermatol). KLK5 is the primary serine protease in Loop 1 and PAR-2 is established as its transducer on keratinocytes. Tryptase (serine protease from mast cell secretory granules) can cleave PAR-2 at Arg34-Ser35 at concentrations achieved within skin after mast cell degranulation (Steinhoff 1999 Nat Med). The ST2 → mast cell → tryptase → PAR-2 → KLK5 chain is mechanistically sound and provides a previously unmapped connection between UV-triggered keratinocyte damage and Loop 1 amplification.

**Challenge 3**: Is TSLP significant beyond IL-33 in rosacea?

**Defense**: TSLP is co-released with IL-33 by UV-damaged keratinocytes. TSLPR expressed on mast cells; TSLP → TSLPR → NF-κB → mast cell priming (lowers ST2 degranulation threshold). TSLP is mentioned once in run_046 as "minor; less important than Th17 in rosacea vs. atopic" — this assessment is about TSLP's T cell polarization role, not its mast cell priming role. The mast cell priming role is distinct and merits documentation as a synergistic mechanism with IL-33.

**Verdict**: Run_099 earns execution. Three compelable reasons:
1. Direct rosacea evidence (Zhao 2020: IL-33 elevated in rosacea lesional skin)
2. 4th non-IgE mast cell activation route (extending run_097's mast cell taxonomy)
3. ST2 → tryptase → PAR-2 → KLK5 = novel Loop 1 amplification mechanism not previously identified

---

## 2. Mechanism — IL-33 Release and Keratinocyte Biology

### IL-33: Nuclear Alarmin Store

IL-33 is constitutively expressed and stored in keratinocyte nuclei (not secreted basally). Release is triggered by cell damage/stress without requiring transcriptional induction:

**Release triggers in rosacea skin:**
- UV-B radiation → keratinocyte necrosis/necroptosis → nuclear IL-33 released
- Thermal/mechanical stress → keratinocyte damage (explains heat/physical trigger overlap with TRPA1 routes)
- NETs (run_081): neutrophil extracellular traps → citrullinated IL-33 release from adjacent keratinocytes
- HMGB1 (run_096): DAMPs from pyroptotic cells → bystander keratinocyte stress → IL-33 release
- Demodex mite products (run_046): mite excretory products → keratinocyte stress → IL-33 release (mechanistically plausible, not directly confirmed in rosacea)

**IL-33 structure**: IL-1 superfamily member; 30 kDa full-length; cleaved to ~18 kDa active form by mast cell tryptase/cathepsin G/elastase (mast cell proteases activate their own upstream alarm signal — positive feedback loop).

### ST2/IL1RAcP Receptor Complex

ST2 (suppression of tumorigenicity 2; IL1RL1 gene) + IL-1RAcP (IL-1R accessory protein) forms the functional IL-33 receptor complex:

```
IL-33 → ST2/IL1RAcP heterodimer →
    MyD88 → IRAK1/4 → TRAF6 → IKKβ → NF-κB [rapid]
                              → p38 MAPK → AP-1 [co-activation]
    → Phosphoinositide 3-kinase (PI3K) → Akt [survival signal]
```

**ST2 expression in rosacea-relevant cells:**
- Mast cells: HIGH — primary relevant population for rosacea pathogenesis
- ILC2: HIGH — drives type 2 response (less dominant in rosacea than atopic, but present)
- Treg: HIGH (sST2 as decoy receptor from Treg — potentially protective; see Section 5)
- Th2: Moderate (less relevant in rosacea Th17 context)
- Macrophages: Low-moderate

**Soluble ST2 (sST2)**: Alternative splicing of IL1RL1 → sST2 = decoy receptor secreted into circulation; binds IL-33 without signaling; Treg source of sST2 acts as natural brake. In rosacea: elevated skin inflammation → Treg dysfunction (run_087) → sST2 ↓ → less decoy → more IL-33 signal to mast cells. This creates a mechanistic coupling between Node A (Treg function) and IL-33/ST2 mast cell activation.

---

## 3. Mechanism — ST2 → Mast Cell → Loop 1 Amplification

### 4th Non-IgE Mast Cell Activation Route

Updated mast cell activation taxonomy (extending run_097's three-route triad):

| Route | Ligand | Receptor | Source context |
|---|---|---|---|
| 1 | Substance P | NK1R | C-fiber neuropeptide (run_019) |
| 2 | CGRP | MRGPRX2 | C-fiber neuropeptide (run_093) |
| 3 | VIP/PACAP | VPAC1/PAC1 | C-fiber neuropeptide (run_097) |
| **4** | **IL-33** | **ST2/IL1RAcP** | **Keratinocyte alarmin (run_099)** |

Routes 1-3 = neurogenic (C-fiber activation required). Route 4 = alarmin (keratinocyte UV/damage required). Conceptually distinct origin: routes 1-3 are activated by thermal/sensory/nociceptive stimuli via neuropeptide co-release; route 4 is activated by keratinocyte death/UV exposure directly, bypassing the nervous system.

### ST2 → Mast Cell Degranulation Products

IL-33 → ST2/IL1RAcP → mast cell degranulation (immediate: secretory granules) + de novo synthesis:

**Granule mediators (immediate):**
- Histamine → H1R → vasodilation + itch + increased vascular permeability
- **Tryptase** → serine protease → see Loop 1 amplification below
- Chymase → angiotensin I → Ang II (independent of ACE; RAAS amplification within skin)
- Heparin (granule matrix carrier)

**De novo synthesis (slower):**
- PGE2 → EP2/EP4 → vasodilation + TRPV1 sensitization (run_095 connection)
- LTC4/LTD4 → CysLT1R → smooth muscle contraction → edema
- VEGF → angiogenesis (rosacea telangiectasia substrate)
- TNFα, IL-6 → amplify Signal 1A (NF-κB at macrophage level)

### Loop 1 Amplification: Tryptase → PAR-2 → KLK5

**This is the novel mechanistic connection identified in run_099:**

```
UV-damaged keratinocytes → IL-33 release (nuclear store)
→ ST2/IL1RAcP on dermal mast cells
→ mast cell degranulation → TRYPTASE release
→ tryptase cleaves PAR-2 at Arg34-Ser35 on keratinocytes/sebocytes
→ PAR-2 activation → NF-κB + MAPK in keratinocytes
→ KLK5 expression ↑ + NLRP3 priming
→ Loop 1 amplification
```

Evidence support:
- Tryptase → PAR-2 cleavage: Steinhoff 1999 Nat Med 5(9):1062-1067 (established; skin mast cell tryptase concentrations sufficient for PAR-2 cleavage in perilesional space)
- PAR-2 elevated in rosacea skin: Steinhoff 2011 J Invest Dermatol 131(1):67-75
- KLK5 → PAR-2 connection: Oikonomopoulou 2006 J Invest Dermatol 126(7):1627-1635
- Mast cell tryptase → PAR-2 → KLK5 induction: Kim 2002 J Invest Dermatol 118(4):700-707

**Cross-activation feedback**: Loop 1 generates more KLK5 → LL-37 → mast cell via FPRL1/FPR2 (run_015) + TRPV1 sensitization; IL-33 → mast cell → tryptase → PAR-2 → more KLK5 → more Loop 1. The alarmin route feeds directly into Loop 1 and creates a UV-triggered Loop 1 amplification cycle.

### Chymase → Ang II: Skin-Intrinsic RAAS Arm

Mast cell chymase → local Ang II production independent of ACE:
- Skin mast cells are the primary source of local Ang II via chymase (not systemic ACE)
- ACE inhibitors do NOT block chymase-derived Ang II (chymase-resistant; Balcells 1997 Hypertension)
- This provides an ARB-advantage additional to the ACE-I/bradykinin paradox (run_095): ARBs block AT1R regardless of how Ang II was produced (ACE or chymase), while ACE-Is miss chymase-derived Ang II
- In T1DM rosacea: mast cell chymase pathway contributes to local RAAS beyond what ACE-Is address

---

## 4. Mechanism — TSLP: Mast Cell Priming (Synergistic with IL-33)

### TSLP Biology

Thymic stromal lymphopoietin (TSLP): IL-2 family cytokine from keratinocytes and epithelial cells. Released by:
- UV-B radiation (key rosacea trigger)
- SDS/detergents (skin barrier disruption)
- Demodex products
- Th2-independent; direct keratinocyte damage

TSLP receptor (TSLPR/IL2RG): expressed on mast cells, plasmacytoid DCs, conventional DCs, ILC2.

### TSLP → Mast Cell Priming

```
TSLP → TSLPR/IL2RG → JAK1/JAK2 → STAT5 → mast cell priming:
    - Upregulates ST2 surface expression (more IL-33 receptor → lower IL-33 threshold)
    - Upregulates FcεRI expression (IgE-mediated degranulation sensitization)
    - Induces mast cell VEGF production directly
    - Lowers the activation threshold for all four non-IgE routes
```

**Clinical implication**: UV exposure releases BOTH IL-33 (direct degranulation) AND TSLP (priming for subsequent degranulation). A rosacea patient with recent UV exposure will have both increased IL-33 signaling AND a lowered mast cell threshold — explaining why UV causes a persistent multi-day elevation in rosacea activity beyond the acute flush.

Evidence: Saluja 2015 J Immunol 194(2):821-831 (TSLP → mast cell ST2 upregulation); Matos 2016 J Allergy Clin Immunol 137(3):894-904 (TSLP + IL-33 synergy in mast cell activation).

### TSLP vs. IL-33 in Rosacea vs. Atopic Dermatitis

| Pathway | Atopic dermatitis | Rosacea |
|---|---|---|
| IL-33 → ST2 → mast cell | Primary (high IL-33) | Secondary (moderate IL-33; Zhao 2020) |
| TSLP → DC → Th2 polarization | Dominant | Minor (Th17 primary in rosacea) |
| TSLP → mast cell priming | Contributes | Contributes (TSLP via UV) |
| ILC2 → IL-5/IL-13 | Primary driver | Present, minor |
| Downstream eosinophilia | Common | Uncommon in rosacea |

Distinction: In rosacea, the IL-33/TSLP relevance is through the **mast cell degranulation arm** (vasodilation/tryptase/PGE2), not through the ILC2/Th2 polarization arm. This explains why rosacea does not show the eosinophilia of atopic dermatitis despite sharing IL-33/ST2 upregulation.

---

## 5. Treg-ST2 Connection: Node A Coupling

Tregs express ST2 constitutively. ST2 signaling in Tregs has dual effects:

**Acute IL-33 → Treg ST2**: In some contexts (gut, lung) → Treg expansion and IL-10 production (anti-inflammatory). However, this appears tissue/context dependent.

**Rosacea-relevant consideration**: sST2 (soluble decoy receptor) is produced by Tregs. In a Node A-deficient patient (low Treg frequency, run_050): sST2 production ↓ → more free IL-33 available to bind mast cell ST2 → more mast cell activation. This creates a connection: **Node A dysfunction → reduced sST2 → enhanced IL-33/ST2 mast cell signaling**.

Clinical prediction: patients with lowest Foxp3+ Treg frequency (T-index Node A < 5% CD4+) may have disproportionately elevated IL-33-driven mast cell activation — in addition to the canonical Treg loss → Th17/Th1 amplification.

No therapeutic change recommended (improving Node A via AKG/Vitamin C/Foxp3 TSDR demethylation, run_086/087, would indirectly reduce IL-33/mast cell signaling via sST2 restoration). This provides an additional mechanistic rationale for Node A correction beyond T cell polarization.

---

## 6. T1DM Cross-Connection

### IL-33 → Islet Inflammation

IL-33 expressed in pancreatic islets. ST2 on islet-resident macrophages and mast cells:

```
Islet stress (hypoxia, nutrient load, viral infection) → IL-33 release from islet ECs/β cells →
ST2 on islet macrophages → MyD88/IRAK4/TRAF6 → NF-κB → IL-1β/IL-6/TNFα production →
β cell IL-1β exposure → iNOS → NO → β cell apoptosis (connects to run_043 intraislet NLRP3)
```

Evidence: Guo 2014 J Immunol 192(11):5375-5385 (IL-33 accelerates T1DM in NOD mice via islet macrophage ST2; ST2-KO → delayed T1DM onset). Cayrol 2018 Immunity (IL-33 biology review in autoimmunity).

**sST2 in T1DM**: Circulating sST2 is elevated in T1DM patients (Bartleson 2020 JCI Insight) — likely a compensatory/protective response. Elevated sST2 in T1DM may paradoxically indicate active IL-33 release. The islet is attempting to neutralize its own alarm signal.

**β cell-intrinsic**: β cells also express IL-33; under ER stress (run_098: IFN-α → PERK → CHOP cascade) → β cell necroptosis → IL-33 nuclear store released → ST2 on neighboring islet macrophages → IL-1β amplification loop. This creates a connection between run_098's ER stress/PERK pathway and run_099's IL-33 alarmin route in the islet.

---

## 7. Protocol Implications

### Existing Protocol Coverage

| Mechanism addressed | Current protocol element | Mechanism |
|---|---|---|
| Reduce keratinocyte UV damage → less IL-33 release | Calcitriol/VDR (run_039) → keratinocyte differentiation + VDR photoprotection | VDR reduces UV-induced keratinocyte stress |
| Sunscreen/UV avoidance | Lifestyle (not supplemental) | Reduces primary IL-33 release trigger |
| Mast cell degranulation (all routes) | Quercetin (run_042) → mast cell stabilization; EGCG → mast cell stabilization | Broad mast cell stabilizer coverage |
| Tryptase → PAR-2 → KLK5 (Loop 1) | Ivermectin topical (run_015 extension) reduces KLK5; azelaic acid | Downstream KLK5 suppression |
| Node A correction | AKG + Vitamin C → Foxp3 TSDR (runs 086-087) | Indirectly restores sST2 via Treg expansion |

### No New Agents Required

All relevant mechanisms are addressed by existing protocol elements. Key points:
1. **IL-33 release reduction**: Calcitriol (VDR → keratinocyte resilience) + UV protection already in protocol
2. **ST2 mast cell degranulation**: Quercetin/EGCG mast cell stabilizers address all mast cell degranulation routes including ST2-mediated
3. **Tryptase → PAR-2 → KLK5**: Existing Loop 1 management (ivermectin/AzA/sulforaphane) addresses downstream consequences
4. **sST2 restoration via Node A**: AKG + Vitamin C → Foxp3 TSDR → Treg ↑ → sST2 ↑

### Updated Mast Cell Management Perspective

**Four non-IgE activation routes** in rosacea:
- NK1R (SP/C-fiber) — neurogenic
- MRGPRX2 (CGRP/C-fiber) — neurogenic
- VPAC1/PAC1 (VIP/PACAP/C-fiber) — neurogenic
- **ST2 (IL-33/UV-keratinocyte)** — alarmin/damage-associated [run_099]

**One IgE-dependent route** (standard allergic; less dominant in rosacea unless co-existing atopy)

Clinical conclusion: Mast cell activation in rosacea is multisource. Mast cell stabilizers (quercetin/EGCG/ketotifen/cromolyn) are justified precisely because they act downstream of all activation routes — neurogenic AND alarmin — and are not replaceable by antihistamines, anti-neuropeptide approaches, or UV protection alone.

### Chymase → Ang II: Reinforces ARB Preference

ST2 → mast cell → chymase → local Ang II production (ACE-independent). ACE inhibitors do not block this. This provides a third mechanism for ARB preference in rosacea (run_092: AT1R/RAAS; run_095: bradykinin accumulation; run_099: chymase-derived Ang II bypass). ARBs block AT1R regardless of whether Ang II came from ACE or chymase.

**Summary for T1DM rosacea patients**: Three independent reasons ACE-Is are mechanistically inferior to ARBs in rosacea with active flushing:
1. run_092: ACE inhibition → Ang II ↓ (systemic) but AT1R still downstream of chymase-generated Ang II
2. run_095: ACE-I → bradykinin accumulation → B2R → TRPV1 sensitization → worsened flushing
3. run_099: Skin mast cell chymase → local Ang II → AT1R not blocked by ACE-I

---

## 8. Evidence Summary

| Finding | Evidence | Quality |
|---|---|---|
| IL-33 elevated in rosacea lesional skin | Zhao 2020 Br J Dermatol 183(4):722-731 | Direct rosacea; case-control |
| Tryptase → PAR-2 cleavage in skin | Steinhoff 1999 Nat Med 5(9):1062-1067 | Direct; in vivo skin model |
| PAR-2 elevated in rosacea | Steinhoff 2011 J Invest Dermatol 131(1):67-75 | Direct rosacea |
| PAR-2 → KLK5 amplification | Oikonomopoulou 2006 J Invest Dermatol 126(7):1627-1635 | Mechanistic |
| TSLP + IL-33 mast cell synergy | Matos 2016 J Allergy Clin Immunol 137(3):894-904 | In vitro; human mast cells |
| TSLP → mast cell ST2 upregulation | Saluja 2015 J Immunol 194(2):821-831 | In vitro |
| IL-33 → T1DM acceleration in NOD mice | Guo 2014 J Immunol 192(11):5375-5385 | NOD mouse model |
| Mast cell chymase → Ang II (ACE-independent) | Balcells 1997 Hypertension 30(5):1144-1148 | Established |
| sST2 elevated in T1DM | Bartleson 2020 JCI Insight 5(4):e134824 | Clinical; T1DM cohort |

---

## 9. New Mechanisms Added to Framework

1. **IL-33 (nuclear alarmin) → ST2/IL1RAcP on mast cells → mast cell degranulation** [4th non-IgE mast cell activation route; UV/damage-triggered, neurogenic-independent]
2. **ST2 → mast cell tryptase → PAR-2 cleavage on keratinocytes → NF-κB + KLK5 ↑** [novel Loop 1 amplification: UV → alarmin → Loop 1]
3. **Mast cell chymase → skin-local Ang II (ACE-independent)** [3rd mechanism for ARB preference over ACE-I in rosacea]
4. **TSLP (UV-damaged keratinocytes) → TSLPR on mast cells → ST2 upregulation → lower IL-33 activation threshold** [priming mechanism; synergistic with IL-33 for post-UV multi-day flare elevation]
5. **Node A deficiency (Treg ↓) → sST2 ↓ → more free IL-33 → enhanced ST2/mast cell signaling** [Node A/IL-33 coupling; additional rationale for Node A correction]
6. **IL-33 → ST2 on islet macrophages → IL-1β → β cell apoptosis** [T1DM alarmin → islet inflammation → β cell loss]
7. **ER stress → β cell necroptosis → IL-33 nuclear release → ST2 → IL-1β** [run_098 PERK/CHOP → run_099 IL-33 alarmin connection in islet]
8. **Tryptase → full-length IL-33 → 18 kDa active form cleavage** [mast cell products activate their own upstream alarm signal; positive feedback]

---

## 10. Updated Non-Responder Flag

**Non-responder pattern newly identifiable (run_099)**: Patient with UV-predominant triggers + persistent flares despite neurogenic management (TRPV1/TRPA1/neuropeptide control) but without UV exposure reduction:

Mechanism: UV → keratinocyte IL-33 release → ST2 → mast cell (neurogenic-independent route not addressed by neuropeptide/TRPV1 management alone).

**Management**: Reinforce UV protection + calcitriol/VDR photoprotection + verify mast cell stabilizer (quercetin/EGCG) compliance. Note: UV-dominant flare pattern may indicate IL-33/alarmin route is driving mast cell activation independently of C-fiber/neuropeptide routes.

---

## 11. Updated Framework Counts

- **Mast cell activation routes**: 5 total (4 non-IgE [NK1R, MRGPRX2, VPAC1/PAC1, ST2] + 1 IgE-dependent)
- **NF-κB activation mechanisms**: 12 (unchanged; IRE1α/TRAF2 = 12th from run_098)
- **NF-κB suppression pathways**: 11 (unchanged)
- **NLRP3 inhibition mechanisms**: 7 (unchanged)
- **SIRT1 mechanisms**: 6 (unchanged)
- **Gut barrier mechanisms**: 5 (unchanged)
- **No new protocol agents**; three mechanisms reinforcing ARB preference over ACE-I

*run_099 — 2026-04-12 | IL-33 ST2 TSLP alarmin mast cell tryptase PAR-2 KLK5 Loop 1 UV keratinocyte chymase Ang II ARB TSLPR sST2 Treg Node A T1DM islet Zhao 2020 Steinhoff 1999 Guo 2014 Balcells 1997*
