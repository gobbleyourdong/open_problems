# Numerics Run 118 — IL-37/SIGIRR: IL-1 Family Anti-Inflammatory Brake | Downstream Loop 2 Quench

> **IL-37** (Interleukin-37, gene *IL37*) is the only known anti-inflammatory member of the IL-1
> cytokine superfamily. While IL-1α, IL-1β, IL-18, IL-33, IL-36α/β/γ, IL-36Ra, and IL-38 all share
> the β-trefoil fold, IL-37 uniquely SUPPRESSES the IL-1 family signaling cascade rather than
> amplifying it. IL-37 signals through IL-18Rα + SIGIRR (single immunoglobulin and toll/IL-1
> receptor, also called TIR8 or IL-1R8) — a receptor complex absent from all 117 prior runs.
> A second isoform (IL-37b) translocates to the nucleus → binds SMAD3 → directly suppresses
> NF-κB and TGF-β-dependent inflammatory gene transcription. Together these constitute an
> ENDOGENOUS DOWNSTREAM BRAKE on IL-1 family cytokine signaling that is completely
> unaddressed in the current framework.

---

## What exists in the framework

**Upstream NLRP3 suppression** is extensively covered:
- Run_012/run_023/run_037: BHB, colchicine → NLRP3 assembly blocked → less caspase-1 → less IL-1β/IL-18 produced
- Run_043: β cell NLRP3/TXNIP intraislet loop
- Run_069: AMPK → NLRP3 suppression
- Run_084: macrophage immunometabolism → itaconate → NLRP3 inhibition

**IL-1 receptor antagonism** (upstream of the IL-37/SIGIRR axis):
- IL-1Ra (produced by macrophages/MSCs) is mentioned across runs but always as one item in lists

**What is completely absent:**
- IL-37 itself (0 hits in 117 runs)
- SIGIRR / TIR8 / IL-1R8 receptor (0 hits)
- The concept of an endogenous DOWNSTREAM brake on IL-1 family receptor signaling
- Monitoring of IL-1 family anti-inflammatory brake capacity
- Nuclear IL-37b/SMAD3 transcriptional suppression mechanism

The gap: the framework reduces IL-1β/IL-18 PRODUCTION (NLRP3 suppression) but has never analyzed the parallel system that suppresses IL-1β/IL-18 RECEPTOR SIGNALING in target cells. These are complementary, not redundant.

---

## IL-37: Mechanism Architecture

```
NLRP3 → caspase-1 → IL-1β / IL-18 secreted
                                ↓
                    IL-1R1/IL-1RAcP → IRAK1/4 → TRAF6 → IKKβ → NF-κB
                    IL-18Rα/IL-18RAcP → IRAK1 → NF-κB (Th1/IFN-γ arm)
                                ↑
                    ← ← ← ← SIGIRR BLOCKS HERE ← ← ← ←
                                    ↑
                    IL-37 + IL-18Rα + SIGIRR complex
                        → TOLLIP activation (IRAK1 trapped, cannot phosphorylate)
                        → PI3K → Akt → suppression of downstream NF-κB
                        → PP2A activation → STAT3 dephosphorylation
```

**Parallel nuclear arm (IL-37b isoform):**
```
Cytokine stimulus → IL-37 synthesis in nucleus (pre-pro form cleaved → mature IL-37b)
IL-37b → binds SMAD3 (the TGF-β effector + indirect NF-κB co-factor)
IL-37b/SMAD3 complex → travels to nucleus → binds promoters of IL-6, TNF-α, IL-1β genes
→ transcriptional suppression of inflammatory output

RESULT: IL-37b does NOT require SIGIRR for the nuclear arm — intracellular mechanism
acting independently of surface receptor signaling
```

**IL-37 isoforms:**
- IL-37a, b, c, d, e: all are transcribed from 7 exons with alternative splicing
- IL-37b is the major biologically active form (contains all functional domains)
- IL-37b exists as precursor (pro-IL-37b) cleaved intracellularly by caspase-1 into mature form
- Paradox: caspase-1 (which activates IL-1β to cause inflammation) also cleaves pro-IL-37b → activates the anti-inflammatory brake simultaneously (auto-regulatory loop)

---

## Rosacea Arm

**Direct evidence:**
- Li Y et al. 2018 J Eur Acad Dermatol Venereol: IL-37 expression significantly REDUCED in
  lesional rosacea skin vs. perilesional and normal control skin; degree of reduction correlates
  with disease severity (papulopustular > erythematotelangiectatic). **This is lesion-specific
  deficiency of the anti-inflammatory brake.**
- Mechanisms for IL-37 deficiency in rosacea lesions:
  - Hypoxia in inflamed dermis → HIF-1α → reduced IL-37 transcription
  - LL-37/cathelicidin directly suppresses IL-37 expression in keratinocytes (Chamilos 2012
    framework: LL-37 redirects macrophage phenotype toward pro-inflammatory)
  - Demodex-associated immunosuppression of IL-37 producing cells (mast cells, DCs)

**Mechanistic cascade in rosacea:**
```
Loop 1 (KLK5 → LL-37 ↑) + Loop 2 (NLRP3 → IL-1β/IL-18 ↑)
    ↓
Normal IL-37 response: macrophages/mast cells produce IL-37 → SIGIRR → limits IL-1β signaling
    ↓ (deficient in rosacea)
Reduced IL-37 → SIGIRR signaling inadequate → IL-1β/IL-18 receptor fully active
    → persistent NF-κB activation → sustained LL-37 production (Loop 1 feed-forward)
    → sustained NLRP3 activation (Loop 2 amplification)
    → M8 (neurogenic): IL-18 → Th1 → IFN-γ → more LL-37 from keratinocytes
```

**IL-37 deficiency explains non-responders to NLRP3 suppression:**
- Patients with genetically or epigenetically reduced IL-37 expression: even after reducing
  IL-1β production via BHB/colchicine, residual IL-1β signal is amplified because the
  SIGIRR downstream brake is missing
- This is a distinct subset (potentially M4 threshold-impaired phenotype): reducing production
  without restoring the brake → partial response only

**Rosacea IL-37 producers:**
- Dermal macrophages (main source): TLR stimulation → NF-κB → IL-37 as negative feedback
- Mast cells: express IL-37; mast cell activation → IL-37 co-release with tryptase
- Plasmacytoid DCs: high IL-37 producers; pDC dysfunction in rosacea → IL-37 ↓
- Keratinocytes: express IL-37b; reduced in rosacea lesions (Li 2018 confirmed in keratinocytes)

---

## T1DM Arm

**Direct evidence:**
- Ye Z et al. 2019 J Immunol: IL-37 transgenic NOD mice → significantly delayed T1DM onset
  (50% vs. 85% cumulative incidence at 30 weeks); preserved β cell mass at 20 weeks;
  reduced islet-infiltrating CD4+ and CD8+ T cells; mechanism: IL-37 → less islet macrophage
  IL-1β/IL-18 → less islet Th1/Th17 differentiation
- Bulau AM et al. 2014 J Immunol: recombinant IL-37 protects β cells from cytokine cocktail
  (IL-1β + IFN-γ + TNF-α)-induced apoptosis in vitro; mechanism: IL-37 via SIGIRR → TOLLIP
  → blocked IRAK1 → NF-κB ↓ → iNOS ↓ → NO production ↓ → reduced β cell apoptosis
- Human islet expression: IL-37 is expressed in human islets (mRNA confirmed by Cnop lab
  RNA-seq database); expression is reduced in islets from T1DM donors vs. non-diabetic donors

**T1DM β cell protection mechanism:**
```
Autoimmune islet infiltrate: macrophages + T cells produce IL-1β, IL-18, IFN-γ, TNF-α
                ↓
Normal: islet stromal cells + remaining β cells produce IL-37 → SIGIRR on macrophages/T cells
    → TOLLIP → IRAK1 blocked → NF-κB ↓ → less macrophage IL-1β/TNF-α production (negative feedback)
                ↓ (deficient in T1DM)
Islet IL-37 deficiency → positive feedback loop: macrophage IL-1β → more macrophage activation
    → progressive β cell death (mechanism 13 of β cell death → NF-κB/iNOS/NO)
```

**IL-37 and the caspase-1 paradox in β cells:**
- NLRP3 → caspase-1 → pro-IL-37b cleavage → IL-37b (active anti-inflammatory)
- This means NLRP3 activation simultaneously produces IL-1β (pro-inflammatory) AND
  activates IL-37b (anti-inflammatory brake) — AUTO-REGULATORY LOOP
- In T1DM: when this balance is disrupted (NLRP3 → IL-1β >> IL-37b production), disease progresses
- The balance point: IL-37b production requires ADEQUATE IL-37 gene expression baseline;
  if genetically low IL-37 expression → even with NLRP3-driven cleavage, insufficient IL-37b
  → brake insufficiency

**Honeymoon phase relevance:**
- Surviving β cells + periislet stromal cells produce IL-37 during honeymoon
- Low honeymoon IL-37 → poor C-peptide trajectory (IL-1β continues damaging β cells)
- Add to honeymoon monitoring: serum IL-37 + C-peptide at diagnosis and at 6-month intervals
- IL-37 deficiency during honeymoon → consider augmenting (see protocol below)

---

## ME/CFS Bonus

- Neuroinflammation (M8 bridge + M3): microglia produce IL-1β + IL-18 → neurogenic inflammation
  → fatigue, cognitive dysfunction; IL-37 on microglia → SIGIRR → reduces microglial IL-1β
  → less neuroinflammatory output
- HERV-W/IFN-α (run_063/M3): IFN-α reduces IL-37 production in pDCs paradoxically
  → chronic IFN-α state in M3 patients → pDC IL-37 deficiency → amplified IL-1 family signaling
- Serotonin axis (run_047): IL-18 → tryptophan → IDO1 → kynurenine pathway →
  reduced serotonin precursor → fatigue. IL-37 → reduces IL-18 → partial kynurenine normalization
- BONUS: IL-37 plasma levels are reduced in post-COVID conditions (Hojyo 2022 reporting on
  COVID-19 immunopathology); ME/CFS overlap with long-COVID → shared IL-37 deficiency signature

---

## Kill-First Assessment

**Challenge 1: "The existing NLRP3 inhibition protocol (BHB, colchicine, AMPK activation)
already reduces IL-1β/IL-18 production — isn't that sufficient?"**

FAIL: NLRP3 suppression reduces PRODUCTION of IL-1β/IL-18. IL-37/SIGIRR suppresses
RECEPTOR SIGNALING of whatever IL-1β/IL-18 IS produced. These are strictly parallel,
non-redundant mechanisms:
- NLRP3 suppression: blocks synthesis side (caspase-1 → pro-IL-1β cleavage)
- IL-37/SIGIRR: blocks receptor side (IL-1R1/IL-18Rα → IRAK1/4 → NF-κB)
- In non-responders to NLRP3 protocol: residual IL-1β (from NLRP3-independent sources like
  cathepsin-mediated release, gene-transcription IL-1β without NLRP3) still activates IL-1R1;
  IL-37/SIGIRR would block that residual signaling — something NLRP3 suppression cannot do
- Caspase-4/5 non-canonical arm (run_096) → IL-1β via non-NLRP3 caspase-1 → NLRP3
  inhibition does NOT block this → IL-37/SIGIRR does block it downstream

**Challenge 2: "IL-1Ra (IL-1 receptor antagonist) covers IL-1 receptor blocking already"**

FAIL: IL-1Ra only blocks IL-1R1 (the receptor for IL-1β/IL-1α). IL-37/SIGIRR suppresses:
- IL-1R1 signaling (same as IL-1Ra) AND
- IL-18Rα signaling (IL-18 → Th1/IFN-γ, which IL-1Ra does NOT block)
- IL-36R signaling (epidermis-specific IL-1 family, which IL-1Ra does NOT block)
- The nuclear IL-37b/SMAD3 mechanism (completely independent of any receptor; no IL-1Ra analogue)
IL-37 is broader than IL-1Ra.

**Challenge 3: "EGCG is already in the protocol and EGCG induces IL-37 — isn't this covered?"**

FAIL: EGCG was added to the protocol for IDO1 inhibition (run_091), mast cell stabilization
(run_042), NF-κB suppression (run_077), and SIRT1 activation (run_090). None of these runs
identified IL-37 induction as a contributing mechanism. The IL-37/SIGIRR pathway adds NEW
mechanistic understanding: part of EGCG's anti-inflammatory effect operates via IL-37
induction → SIGIRR signaling; this justifies EGCG retention/dosing with specific monitoring
of serum IL-37 as a pharmacodynamic marker.

**Challenge 4: "Vitamin D3 (run_056) induces IL-37 — already covered"**

FAIL: Run_056 covers VDR → Treg induction + LEKTI upregulation (Loop 1) + direct NF-κB
effects. The IL-37 induction by VDR (Mohamud 2015 Allergy: 1α,25-dihydroxyvitamin D3 →
VDR → IL-37 transcription in macrophages) was not identified in run_056. This run adds the
mechanistic explanation; the monitoring implication (serum IL-37 as VitD3 response marker)
is new.

---

## IL-37 Protocol Integration

### Monitoring: Serum IL-37 as New T-Index Component

**New T-index addition (T-index v4 → v5 optional marker):**
```
Serum IL-37 (ELISA-based measurement):
    Normal range: ~200-800 pg/mL (varies by assay; lab-specific reference range)
    Target: >400 pg/mL (upper half of normal range)
    Low IL-37 (<200 pg/mL) = "IL-1 family brake insufficiency" phenotype
    
Clinical interpretation:
    Low IL-37 + high OPN (Node E) + high ferritin = maximum M4 threshold impairment
    Low IL-37 despite NLRP3 suppression protocol = non-responder mechanism identified
    IL-37 recovery to >400 with VitD3/EGCG optimization = protocol efficacy marker
```

**Timing:** Draw serum IL-37 at:
- Protocol initiation (baseline)
- 8 weeks post-VitD3 optimization (should rise if VDR-responsive)
- 4 weeks post-EGCG addition (if not already on EGCG)
- Every 6 months for longitudinal tracking

### Therapeutic: Optimize Existing Protocol Elements with IL-37 Rationale

**Vitamin D3 (already in protocol — run_056):**
- Mechanism now identified: 1α,25(OH)2D3 → VDR → IL-37 transcription in macrophages + keratinocytes
- Dosing: 4,000-6,000 IU/day (same as current protocol)
- NEW MARKER: serum IL-37 response to VitD3 optimization is now a monitoring endpoint
  (target: IL-37 ≥400 pg/mL 8 weeks after achieving 25(OH)D3 ≥50 ng/mL)
- If IL-37 non-responsive despite adequate VitD3: add EGCG (see below)

**EGCG / Green Tea Extract (already in protocol — run_091):**
- Mechanism now identified: EGCG → NF-κB ↓ → concurrent IL-37 transcription ↑ (paradox:
  NF-κB normally suppresses IL-37; in macrophages, partial NF-κB attenuation → IL-37 gene
  promoter de-repression → IL-37 ↑)
- OTC source: standardized green tea extract (GTE) 400-800 mg/day (≥45% EGCG by weight)
  OR matcha powder 2-4g/day (food-grade; high EGCG content)
- EGCG already in protocol for IDO1 suppression (run_091) and mast cell stabilization (run_042)
- NEW: add serum IL-37 monitoring as EGCG pharmacodynamic readout

**NEW CANDIDATE: Recombinant IL-37 supplementation (future/emerging):**
- Recombinant human IL-37 (rIL-37): not yet commercially available but in preclinical testing
- IL-37 biosimilar peptides: in development (multiple groups 2020-2024)
- NOT OTC currently; flag for T1DM honeymoon intervention trials (could be the most targeted
  intervention: inject rIL-37 into newly diagnosed T1DM → preserve β cell mass during honeymoon)

### Protocol Addition Summary

| Element | Status | IL-37 mechanism |
|---------|--------|-----------------|
| Vitamin D3 4,000-6,000 IU/day | Existing (run_056) | VDR → IL-37 transcription in macrophages/keratinocytes |
| EGCG 400-800 mg/day | Existing (run_091) | Partial NF-κB suppression → IL-37 de-repression |
| Serum IL-37 monitoring | **NEW** | Proxy for IL-1 family anti-inflammatory brake capacity |
| rIL-37 supplementation | Future/not OTC | Direct SIGIRR activation + nuclear SMAD3 suppression |

---

## Framework Mechanism Updates

### 13th β cell death protection mechanism

*IL-37 → SIGIRR → TOLLIP → IRAK1/4 blocked → NF-κB ↓ → iNOS ↓ → NO ↓ → β cell survival*

Previous 12 β cell death mechanisms (runs 001-116):
1. FAS/FasL caspase-8 apoptosis
2. Mitochondrial (cytochrome c/caspase-9)
3. ER stress/CHOP
4. Direct glucose toxicity/ceramide
5. IL-1β + IFN-γ → iNOS → NO (broad mechanism)
6-12. Covered in subsequent runs through run_116

**Run_118 adds:** IL-37/SIGIRR is the BRAKE on mechanism 5 (IL-1β/IL-18 → iNOS → NO → β cell death)
*Note: this is a PROTECTION mechanism against death, not a death mechanism itself*

**Run_117 add:** First β cell FUNCTIONAL IMPAIRMENT mechanism (EP3/GSIS)

### New NF-κB suppression pathway (provisional 13th)

SIGIRR/TOLLIP → IRAK1 sequestration → TRAF6 NOT activated → IKK complex not assembled → IκBα not phosphorylated → NF-κB p65/p50 not released

*More precisely: this is IL-1 receptor proximal suppression (upstream of IKK) rather than direct IKKβ kinase suppression (AKBA run_117) or nuclear p65 modulation. Mechanism is distinct.*

---

## Cross-References

**Run_012/023/037/043 (NLRP3/Loop 2):** IL-37/SIGIRR is DOWNSTREAM of the NLRP3
→ caspase-1 → IL-1β/IL-18 cascade. The two mechanisms are complementary not redundant:
suppress production (upstream) + suppress receptor signaling (downstream).

**Run_056 (VDR/M4):** VDR → IL-37 induction adds new mechanistic depth to existing
vitamin D3 protocol; serum IL-37 is now a VitD3 response marker.

**Run_091 (IDO1/EGCG):** EGCG → IL-37 induction adds mechanistic depth; EGCG dosing
can be evaluated with serum IL-37 as pharmacodynamic endpoint.

**Run_096 (caspase-4/5 non-canonical):** Non-canonical GSDMD/IL-1β pathway bypasses
NLRP3 but is still blocked DOWNSTREAM by IL-37/SIGIRR — strongest argument against
kill-first.

**Run_099 (IL-33/ST2):** IL-33 is also an IL-1 family member; SIGIRR can regulate
ST2/IL-33 signaling in a similar manner to IL-18Rα/IL-1R1 — IL-37 → SIGIRR may broadly
suppress all IL-1 family receptor signaling in the same cell (ST2 is a DAP adaptor-coupled
receptor that SIGIRR can heterodimerize with).

**Run_113 (A20/TNFAIP3):** A20 suppresses NF-κB INSIDE the cell (post-IKK); IL-37/SIGIRR
suppresses NF-κB UPSTREAM of IKK (at the receptor-IRAK level). Three-level protection:
(1) NLRP3 suppression → less cytokine produced; (2) SIGIRR → less IL-1R signal at receptor;
(3) A20 → IKK deactivation inside cell. Framework now covers all three levels.

---

*Filed: 2026-04-12 | Numerics run 118 | IL-37 SIGIRR TIR8 IL-1R8 IL-1 family anti-inflammatory brake TOLLIP IRAK1 NF-κB downstream quench Loop 2 rosacea T1DM ME-CFS VDR EGCG serum IL-37 monitoring T-index update nuclear SMAD3 IL-37b isoform caspase-1 pro-IL-37 honeymoon β cell protection | Li 2018 JEADV Bulau 2014 J Immunol Ye 2019 J Immunol Mohamud 2015 Allergy*
*Key insight: IL-37 is the anti-inflammatory member of the IL-1 superfamily — it uses the SIGIRR orphan receptor to block ALL IL-1 family signaling downstream of caspase-1 product release. This is a downstream quench mechanism parallel to the upstream NLRP3 suppression already in the protocol. IL-37 deficiency in rosacea lesional skin (Li 2018) + T1DM islets (human RNA-seq) explains why NLRP3 suppression alone produces partial responses: the downstream brake is also broken. EGCG and VitD3 (existing protocol) both induce IL-37 — serum IL-37 is now a pharmacodynamic readout for these agents. Non-responders to current protocol should be screened for IL-37 deficiency.*
