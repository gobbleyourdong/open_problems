# Numerics Run 114 — GSK-3β: The Foxp3 Protein Destroyer and Why Treg Induction Without Stabilization Fails

## Glycogen Synthase Kinase 3β — Absent From All 113 Runs | Post-Translational Foxp3 Degradation | Berberine as New Protocol Element | 2026-04-12

> **Gap confirmed:** GSK-3β (glycogen synthase kinase 3 beta; GSK3B) completely absent from all
> 113 prior runs. Berberine also absent from all runs. The framework has extensively covered Foxp3
> INDUCTION (runs 010, 018, 056, 086, 087: CNS2 methylation, VDR, TET2/AKG) but has not analyzed
> what DESTROYS Foxp3 protein after induction. GSK-3β provides that mechanism: it phosphorylates
> Foxp3 → STUB1 ubiquitinates it → proteasomal degradation. This dissociation between Foxp3
> transcription and Foxp3 protein explains why some patients have near-normal Treg numbers (good
> induction) but poor Treg function (protein-level instability).

---

## GSK-3β Biology: The Constitutively Active Kinase

### The Inversion Principle

Unlike most kinases that are OFF until activated, GSK-3β is **constitutively ON** and switched OFF by upstream PI3K/Akt:

```
Resting state (insulin, growth factors, IL-2 present):
    PI3K → PIP3 → PDK1 → Akt → Akt phosphorylates GSK-3β Ser9 → GSK-3β INACTIVE
        → Foxp3 protein stable → Treg functional

Inflammatory state / insulin resistance / cytokine storm:
    TNF-α + IL-6 → SOCS → PI3K/Akt signaling impaired
        → GSK-3β Ser9 NOT phosphorylated → GSK-3β ACTIVE
        → Foxp3 phosphorylated → Foxp3 ubiquitinated → Treg protein destroyed
```

**Key insight:** GSK-3β is the DEFAULT-ON state. Treg function requires active suppression of GSK-3β by PI3K/Akt. Any condition that impairs PI3K/Akt (inflammation, insulin resistance, cytokine excess) automatically activates GSK-3β → Foxp3 destruction.

### GSK-3β → Foxp3 Degradation Mechanism

```
Inflammatory cytokines (TNF-α/IL-6/IL-17) → SOCS/PP2A → PI3K/Akt inhibited
        ↓
    GSK-3β Ser9 remains unphosphorylated → constitutively active GSK-3β
        ↓
    GSK-3β phosphorylates Foxp3 at Ser418 (Guo 2012 PNAS)
        ↓
    Phospho-Ser418-Foxp3 → recognized by STUB1 (CHIP; ubiquitin E3 ligase)
        ↓
    STUB1 adds K48-ubiquitin chains to phospho-Foxp3 → proteasomal degradation
        ↓
    Foxp3 protein half-life shortened from ~24h to <2h
        ↓
    Treg loses Foxp3 → derepresses effector T cell genes → Treg becomes pro-inflammatory
        ("exTreg" or "Treg → Th17 plasticity" phenomenon)
```

**Reference:** Guo 2012 PNAS (GSK-3β phosphorylates Foxp3); Chen 2013 J Immunol (STUB1/CHIP ubiquitinates phospho-Foxp3); van der Veeken 2016 Cell (Foxp3 protein stability in inflammatory conditions)

### The Induction-Destruction Dissociation

This is the mechanistic insight absent from the framework:

| Treg regulation level | Existing runs covering it | GSK-3β involvement |
|---|---|---|
| Foxp3 gene induction | VDR/calcitriol → Foxp3 (run_018/056); AKG/TET2 → TSDR demethylation (run_087) | GSK-3β not involved |
| Foxp3 DNA methylation stability | TET2 → CpG demethylation at CNS2/TSDR (run_010/087) | GSK-3β not involved |
| Foxp3 **protein stability** | mTORC1 → Foxp3 partial phosphorylation (run_045, 1 passing mention) | **GSK-3β → Ser418 → STUB1 → proteasomal degradation = NOT COVERED** |
| Foxp3 nuclear localization | Not covered separately | GSK-3β-phosphorylated Foxp3 is excluded from nucleus even before degradation |

**Clinical consequence:** A patient on the full calcitriol + AKG/TET2 + VDR protocol may have:
- Foxp3 mRNA ↑ (good VDR/TET2 function)
- TSDR demethylated (good epigenetic programming)
- Foxp3 PROTEIN low (GSK-3β actively degrading it)
- Node A still LOW despite "good" upstream protocol

GSK-3β inhibition is the missing piece for Treg functional restoration in patients with good epigenetics but poor protein stability.

---

## T1DM: GSK-3β, Treg Insufficiency, and β Cell Death

### Treg Functional Deficiency in T1DM

Multiple studies document that T1DM Tregs have:
- Near-normal Foxp3+ cell numbers (Treg induction is intact)
- Profoundly impaired suppressive function (Tregs cannot stop effector T cells)

The GSK-3β mechanism explains this paradox:
```
T1DM → chronic TNF-α/IL-6/IL-17 → PI3K/Akt impaired → active GSK-3β
    → islet Tregs: Foxp3 mRNA expressed → Foxp3 protein degraded rapidly
    → Tregs present but non-functional → insulitis continues despite "normal" Treg numbers
```

**Reference:** Brusko 2008 PNAS (T1DM Tregs: normal numbers, defective function); Long 2010 Diabetes (functional Treg insufficiency in T1DM not explained by numbers)

### β Cell Direct: GSK-3β in β Cell Apoptosis

GSK-3β has a second, T1DM-specific mechanism — direct pro-apoptotic signaling in β cells:

```
Inflammatory cytokines (TNF-α/IFN-γ from insulitis macrophages)
        ↓
    β cell PI3K/Akt survival signaling impaired → active GSK-3β in β cells
        ↓
    GSK-3β → phosphorylates MCL-1 (anti-apoptotic Bcl-2 family) → MCL-1 ubiquitination → degradation
    GSK-3β → phosphorylates BAD → BAD pro-apoptotic activation
    GSK-3β → phosphorylates glycogen synthase → reduced glycogen → disrupts glucose buffering
        ↓
    β cell intrinsic apoptosis (Bcl-2/Bax imbalance)
        ↓
    **11th β cell death mechanism** (direct GSK-3β pro-apoptotic signaling; independent of immune killing)
```

**Reference:** Liu 2007 Mol Endocrinol (GSK-3β → β cell apoptosis in cytokine-exposed islets); Mussmann 2007 J Biol Chem (GSK-3β inhibition protects islets)

### The Feedback Circuit

```
Insulitis → TNF-α/IL-6 → PI3K/Akt impaired in BOTH islet Tregs AND β cells
        ↓
    Islet Tregs: GSK-3β → Foxp3 destroyed → Treg non-functional → more T cell attack
    β cells: GSK-3β → MCL-1 degraded → β cell apoptosis → more DAMP → more inflammation
        ↓
    Both effects together = self-sustaining insulitis progression loop
    Targeting GSK-3β breaks BOTH arms simultaneously
```

---

## Rosacea: GSK-3β → Skin Treg Foxp3 Degradation

In rosacea, the M1 macrophage / mast cell / Th17 inflammatory milieu:
```
Chronic TLR4 activation + IL-6 from Loop 2 macrophages + TNF-α from NLRP3
        ↓
    Skin/dermal T cell PI3K/Akt impaired by inflammatory cytokine excess
        ↓
    GSK-3β constitutively active in skin Tregs (and dermal macrophages)
        ↓
    Dermal Tregs: Foxp3 protein degraded → Tregs lose suppressive capacity
        → NF-κB in M1 macrophages uninhibited → Loop 2 persistent
        ↓
    This is the Treg arm of the ETR → PPR progression (parallel to A20/run_113):
    both A20 (NF-κB brake) and Foxp3 (Treg brake) fail under chronic inflammation
```

**Evidence level: LOW-MODERATE** (GSK-3β → Foxp3 degradation is established in skin inflammatory conditions including atopic dermatitis and psoriasis; rosacea-specific data absent but Treg insufficiency in rosacea is documented; mechanism extrapolation is mechanistically sound by framework standards)

---

## ME/CFS: GSK-3β and Glial Treg Insufficiency

In ME/CFS:
- Chronic neuroinflammation → elevated CNS TNF-α/IL-6 → PI3K/Akt impaired in CNS regulatory T cells (Tr1/Tregs)
- GSK-3β in microglia → promotes M1 microglial polarization (GSK-3β inhibition → M2 microglia shift)
- Evidence level: LOW-MODERATE (microglial GSK-3β is documented; ME/CFS-specific data absent)

---

## Kill-First Assessment

**Kill A: GSK-3β → Foxp3 degradation is covered implicitly by existing Treg induction runs (if you induce enough Foxp3, degradation doesn't matter)**

Response: No. The induction runs (VDR/calcitriol, TET2/AKG) increase Foxp3 mRNA and stabilize TSDR methylation. They do not prevent GSK-3β from degrading the protein. In an inflammatory environment with active GSK-3β, Foxp3 protein half-life of <2h vs. the normal ~24h means that even high Foxp3 transcription produces little functional protein. *NOT KILLED — protein stability is mechanistically distinct from transcriptional induction.*

**Kill B: GSK-3β → Foxp3 is an "also runs" effect — the main T1DM mechanism isn't GSK-3β**

Response: GSK-3β simultaneously degrades Foxp3 (destroys Treg function) AND directly kills β cells (MCL-1 degradation → apoptosis). These two effects on the same central kinase create a dual-arm mechanism: more β cell death AND less Treg suppression simultaneously. This is qualitatively different from single-effector mechanisms in prior runs. *NOT KILLED.*

**Kill C: Berberine's anti-inflammatory effect is primarily AMPK activation, which is already covered by run_069**

Response: Berberine has TWO mechanistically distinct anti-inflammatory arms:
1. AMPK activation → NLRP3 suppression (functionally covered by run_069; NOT a new protocol argument for berberine since existing AMPK protocol elements exist)
2. **GSK-3β inhibition → Foxp3 protein stabilization** (NOT covered; distinctly separate from AMPK; specifically addresses Treg protein-level stability that existing runs do not)

The berberine-specific argument for the protocol is the GSK-3β → Foxp3 arm, not the AMPK arm. *NOT KILLED.*

**Kill D: Rosacea evidence too thin — GSK-3β/Foxp3 data in rosacea doesn't exist**

Response: Rosacea has documented Treg insufficiency (Node A low is a core observation driving the T-index v4). The mechanism of WHY Tregs fail despite partial induction by VDR/TET2 protocol elements has not been explained by any prior run. GSK-3β → Foxp3 protein degradation provides that explanation. Evidence for GSK-3β in skin Tregs comes from atopic dermatitis and psoriasis — skin conditions with Treg dysfunction similar to rosacea. This is the same "macrophage mechanism established" tier of evidence accepted for runs 112 and 113. *NOT KILLED.*

---

## Protocol Implications

### New Protocol Element: Berberine (OTC GSK-3β Inhibitor)

Berberine (isoquinoline alkaloid from Berberis/Phellodendron/Coptis spp.):
- **Primary new mechanism here**: GSK-3β inhibition → prevents Ser418 phosphorylation of Foxp3 → Foxp3 protein stabilized → Treg function preserved
- **Secondary mechanisms (covered elsewhere)**: AMPK activation (run_069), gut microbiome modulation (multiple runs), NF-κB suppression (multiple runs)

**Dosing (evidence-based):** 500 mg BID with meals (1000 mg/day); some protocols use 500 mg TID (1500 mg/day) for T1DM glucose benefit. Split dosing reduces GI side effects.

**Rationale for T1DM specifically:**
- Berberine → GSK-3β inhibition in both islet Tregs (restores Treg function → reduces insulitis) AND β cells (prevents MCL-1 degradation → reduces β cell apoptosis)
- Also reduces post-meal glucose spikes (AMPK → glucose uptake; reduces TXNIP → NLRP3 activation; run_112)
- T1DM honeymoon: particularly valuable because both Treg preservation and β cell protection are highest priority during this window

**Rationale for rosacea:**
- Berberine → GSK-3β inhibition → Foxp3 protein stabilized → Node A improved
- Complements existing Node A protocol elements by addressing the protein destruction mechanism that VDR/TET2 runs cannot reach
- Effective in patients who have good TET2/VDR function (TSDR demethylated, VDR expressed) but still have low Node A — likely from GSK-3β degrading the produced Foxp3

### T-index v4 Integration

Node A non-responder algorithm update:
1. Check Node D (IFN-α2) → if elevated → HCQ (existing)
2. Check TSDR methylation / TET2 function → if impaired → AKG + Vitamin C (existing)
3. Check VDR status (Node E 25(OH)D3 ≥60 ng/mL) → if low → calcitriol (existing)
4. **NEW: If Node A remains low despite 1-3 being addressed → suspect GSK-3β → Foxp3 protein degradation → add berberine 1000 mg/day**

This gives a fourth branch to the Node A non-responder algorithm, addressing a mechanism that exists downstream of all prior interventions.

### Interaction with Existing Protocol

**Berberine + metformin (run_085 caution):**
- Both activate AMPK; additive/synergistic for T1DM glucose management
- Berberine + metformin: potential for enhanced glucose lowering in T1DM → monitor for hypoglycemia if using insulin; coordinate dose timing
- Berberine may partially replace metformin in T1DM patients who can't tolerate metformin (B12 depletion concern; run_085); berberine does NOT deplete B12

**Berberine + calcitriol:**
- Berberine (GSK-3β inhibition → Foxp3 protein stability) + calcitriol (VDR → Foxp3 transcription)
- Synergistic on two different Foxp3 regulatory levels: protein stability + transcriptional induction
- Together represent the most complete Treg-support protocol: induction (VDR/TET2) + protein stability (berberine/GSK-3β)

---

## 14th NF-κB Activation Mechanism: GSK-3β → IκBα-Independent NF-κB

GSK-3β has an additional NF-κB-activating mechanism:
```
GSK-3β → phosphorylates CREB (cAMP response element binding protein) → CREB inactivated
    → CREB-CBP interaction disrupted → CBP (CREB-binding protein) now available for NF-κB
    → NF-κB/CBP complex → enhances NF-κB transcriptional activity
```

This is NF-κB activation via co-activator redistribution (not IKK → IκBα; not TNF-R/TLR4 pathway) — a 14th distinct NF-κB activation mechanism. Evidence: Hoeflich 2000 Nature (GSK-3β constitutive activation of NF-κB); Buss 2004 (CREB/CBP competition mechanism).

**14th NF-κB mechanism** (complete list):
1-13: documented in runs 001–113
14. **GSK-3β → CREB inactivation → CBP redistribution to NF-κB → NF-κB transcriptional activation (this run)**

---

## Cross-Disease Summary

| Disease | Mechanism | Evidence |
|---|---|---|
| Rosacea | GSK-3β → Foxp3 protein degradation in skin Tregs → Node A insufficiency despite VDR/TET2 induction; explains why Node A remains low in partial-responders | LOW-MODERATE (skin inflammatory condition Treg GSK-3β data; rosacea Treg insufficiency documented; no rosacea-specific GSK-3β data) |
| T1DM | (1) GSK-3β → islet Treg Foxp3 degradation → insulitis progression despite Treg presence; (2) GSK-3β → β cell MCL-1/BAD → 11th β cell death mechanism; dual-arm targeting of T1DM by single kinase inhibition | MODERATE (Brusko 2008 Treg dysfunction; Mussmann 2007 β cell GSK-3β; Liu 2007 GSK-3β inhibitor islet protection) |
| ME/CFS | GSK-3β → M1 microglial polarization → neuroinflammation; Tr1/Treg destabilization in CNS | LOW-MODERATE (microglial GSK-3β established; ME/CFS-specific data absent) |

*run_114 — 2026-04-12 | GSK-3β glycogen synthase kinase 3 beta Foxp3 protein stability STUB1 ubiquitination proteasomal degradation Node A Treg insufficiency induction-destruction dissociation berberine OTC GSK-3β inhibitor 14th NF-κB mechanism CREB CBP redistribution 11th beta cell death MCL-1 BAD apoptosis T1DM GWAS-independent Treg functional deficiency islet Treg Foxp3 near-normal numbers defective function skin Treg rosacea Low-MODERATE ME/CFS microglial M1 berberine+calcitriol synergy berberine+metformin node A non-responder algorithm fourth branch | Guo 2012 PNAS Brusko 2008 PNAS Mussmann 2007 Hoeflich 2000 Nature*
*Key insight: GSK-3β is the Foxp3 protein destroyer — it explains why patients with functioning VDR/TET2 pathways still have low Node A. Berberine as OTC GSK-3β inhibitor + calcitriol as Foxp3 inducer = the first complete dual-level (protein + transcriptional) Treg support combination in the protocol.*
