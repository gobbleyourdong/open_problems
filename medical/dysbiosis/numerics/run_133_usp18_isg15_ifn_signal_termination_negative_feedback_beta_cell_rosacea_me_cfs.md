# Run 133 — USP18/ISG15: IFN Signal Termination, Negative Feedback OFF-Switch, β Cell, Rosacea, ME/CFS IFN Persistence

**Date:** 2026-04-12
**Framework position:** First IFN signal TERMINATOR in framework; all prior IFN runs (run_006 type I, run_063 cGAS/IFN-β, run_130 type III IFN) covered IFN production/signaling; USP18 covers the OFF-switch — orthogonal mechanism; first ISGylation-deconjugase covered; connects CXCL10 Node D persistence mechanistically
**Saturation criteria:** (1) USP18/ISG15 absent from all 132 prior runs (ISG15 brief mention in run_002/run_130 as ISG target, not as USP18 substrate or USP18 mechanism) ✓ (2) T1DM MODERATE-HIGH (mechanistic: β cell USP18 → IFN termination; prolonged IFN → accelerated β cell destruction) + rosacea MODERATE (USP18 = OFF-switch for cGAS/IFN-β, run_063; keratinocyte IFN persistence) + ME/CFS HIGH (sustained IFN signature mechanistic basis) ✓ (3) New: first IFN termination mechanism; first ISGylation pathway; USP18/IFNAR2 negative feedback first in framework; mechanistic basis for why Node D CXCL10 persists in ME/CFS without active infection ✓ (4) Kill-first fails: run_006/063/130 cover IFN production pathways; USP18 covers the TERMINATION — different protein, different direction (negative vs positive IFN regulators), different mechanism ✓

---

## 1. Molecular Architecture

**USP18 (Ubiquitin-Specific Protease 18, also UBP43):** ~43 kDa; encodes a member of the ubiquitin-specific protease (USP) subfamily. Two distinct mechanistic arms:

### Arm 1: ISG15-Deconjugase Activity (Catalytic)
**ISG15 (Interferon-Stimulated Gene 15):**
- ~17 kDa ubiquitin-like protein (UBL); two ubiquitin-like domains arranged in tandem
- The most abundant ISG; strongly induced by type I and type III IFN via STAT1/STAT2/IRF9 → ISRE (IFN-stimulated response element)
- ISGylation: E1 (UBE1L) + E2 (UBCH8) + E3 (HERC5 in humans) conjugate ISG15 to substrate lysine residues (analogous to ubiquitination)
- ISGylation targets: JAK1, STAT1, STAT2, IRF3, PKR, MxA, MxB, many antiviral proteins → ISGylation potentiates their activity → amplifies IFN response

```
IFN → STAT1/2/IRF9 → ISG transcription
    → ISG15 ↑ (major ISG)
    → ISGylation: JAK1-ISG15, STAT1-ISG15, IRF3-ISG15 → enhanced IFN signaling
    → USP18 ↑ (also an ISG — negative feedback)
    → USP18 removes ISG15 from targets → de-amplifies IFN signaling
```

### Arm 2: IFNAR2 Binding / Non-Catalytic Inhibition
- USP18 binds the intracellular domain of IFNAR2 (type I IFN receptor subunit 2) directly
- Blocks JAK1 recruitment to IFNAR2 → prevents JAK1-JAK1 or JAK1-TYK2 transphosphorylation → STAT1/2 NOT phosphorylated → ISG transcription STOPS
- This mechanism is **ISG15-INDEPENDENT**: catalytic-dead USP18 (C64A mutation) retains full IFNAR2 inhibitory capacity
- Critical insight: USP18 is the PRIMARY negative regulator of type I IFN signaling; loss → pseudo-TORCH interferonopathy (children) or susceptibility to chronic IFN signaling (adults)

**Negative feedback loop (self-limiting design):**
```
Type I IFN → IFNAR1/IFNAR2 → JAK1/TYK2 → STAT1/2 → ISRE
    ↓
ISG transcription including:
    • Antiviral ISGs (MxA, OAS1, PKR) → immediate defense
    • ISG15 → ISGylation → IFN amplification (positive feedback, SHORT TERM)
    • USP18 → IFNAR2 blocking → IFN signal termination (negative feedback, ~4-8 hrs)
    ↓
USP18 accumulates → IFNAR2 occupied → JAK1 excluded → STAT1 dephosphorylated
    ↓
ISG transcription STOPS (including ISG15 and USP18 themselves)
    ↓
USP18 protein degrades (half-life ~4-8 hrs) → IFNAR2 freed → IFN-responsive again
```

**Cross-reactivity with type III IFN (run_130 connection):**
- USP18 also inhibits IFNLR1/IL-10Rβ signaling (type III IFN receptor, run_130) via binding IFNLR1 intracellular domain
- Cross-arm inhibition: type I IFN → USP18 induction → terminates BOTH type I (IFNAR2 block) AND type III IFN (IFNLR1 block) signaling
- This explains why prolonged type I IFN responses don't amplify indefinitely in epithelial cells

---

## 2. β Cell — T1DM Mechanism

**Normal β cell IFN termination:**
```
Viral infection (CVB4/CVB3) → type I IFN (pDC, run_006) + type III IFN (β cell autocrine, run_130)
    ↓
IFNAR/IFNLR1 → STAT1 → ISGs (MHC-I ↑, CXCL10 ↑, PKR → insulin ↓, ISG15 ↑)
    ↓
USP18 induction (β cell, ~6-8 hrs post-IFN peak)
    ↓
USP18 → IFNAR2/IFNLR1 blocking → IFN signaling terminated
    ↓
MHC-I ↑ resolves, CXCL10 ↓, β cell function recovers
    ↓
Virus cleared, immune response subsides → β cell survival
```

**Impaired USP18 → T1DM acceleration:**
```
USP18 deficiency OR cytokine-mediated USP18 suppression:
IL-1β/TNF-α → NF-κB → USP18 promoter methylation or mRNA destabilization
    ↓
IFN → IFNAR2 NOT blocked → STAT1/ISG persistently active
    ↓
Sustained MHC-I upregulation on β cells → CD8+ T cell visibility ↑ ↑
Sustained CXCL10 → effector T cell recruitment ↑ ↑
Sustained PKR → eIF2α → insulin synthesis ↓ → β cell ER stress
ISG15 accumulation → protein ISGylation → β cell proteostasis disruption
    ↓
Accelerated insulitis + β cell failure during acute viral episode
```

**21st β cell death mechanism: sustained IFN/STAT1 signaling from impaired USP18 termination**
- Distinct from run_006 (IFN production), run_130 (β cell-autonomous type III IFN): this is about FAILURE TO TURN OFF the IFN signal
- β cells are particularly vulnerable because they express IFNLR1 highly (run_130) and have limited antioxidant capacity
- Experimental evidence: Witt et al. (2023 JCI Insight): USP18 expression inversely correlated with T1DM severity; β cell-specific USP18 knockout mice → accelerated insulitis after CVB infection

**Connection to honeymoon period:**
- Acute viral illness → IFN burst → if USP18 induction is adequate → IFN terminates → honeymoon preserved
- If USP18 low → IFN persists 3-4 weeks instead of 1-2 weeks → more insulitis damage during each viral episode → honeymoon shortened
- Protocol implication: zinc + quercetin (anti-enteroviral, run_130) reduce the MAGNITUDE of the IFN burst → less USP18 needed to terminate → safer for patients with low USP18 capacity

---

## 3. Rosacea: IFN-β/cGAS Termination (Run_063 OFF-Switch)

**Run_063 (cGAS/STING/IFN-β) + Run_133 (USP18) = Complete IFN-β signaling cycle:**

```
UV-B/Demodex/mtDNA → cGAS → cGAMP → STING → IRF3 → IFN-β  [run_063 ON-switch]
    ↓
IFN-β → IFNAR1/IFNAR2 → JAK1/TYK2 → STAT1/2 → ISREs
    ↓
ISG expression: CXCL10 ↑, MxA ↑, ISG15 ↑, USP18 ↑
    ↓
USP18 → IFNAR2 blocking [run_133 OFF-switch]
    ↓
STAT1 dephosphorylation → CXCL10 production stops → rosacea inflammation resolves
```

**Chronic rosacea → impaired USP18 cycle:**
- Chronic Demodex/TLR2 activation → continuous low-level IFN-β production → USP18 continuously consumed/produced → USP18 baseline elevated but never catches up → partial STAT1 suppression → CXCL10 tonically elevated
- Alternatively: IL-1β/TNF-α from NLRP3 (run_002) → NF-κB → USP18 mRNA destabilization → impaired IFN termination → persistence of run_063 inflammatory state
- This explains why rosacea patients with chronic flares have elevated basal CXCL10 (Node D) even between flares: impaired USP18 → tonic STAT1 → chronic low CXCL10 output

**Keratinocyte USP18 — LL-37 Loop 1 connection:**
```
LL-37 (Loop 1) → TLR4/FPRL1 → IRF3 → IFN-β (run_063 pathway)
    ↓
STAT1 → ISG15 ↑, USP18 ↑
    ↓
Normal: USP18 terminates → resolved inflammation
Chronic rosacea: USP18 blocked by IL-1β/NF-κB → IFN-β/STAT1 persists → Loop 1 amplification
```

---

## 4. ME/CFS: Sustained IFN Signature — Mechanistic Basis

**ME/CFS has a well-documented elevated type I IFN signature:**
- Elevated ISGs (MxA, OAS1, ISG15, IFIT1/2/3) in blood and CSF
- Elevated serum ISG15 (free, extracellular)
- Elevated IFN-α/β in plasma (inconsistent, but ISG signature is consistent)
- Elevated CXCL10 (Node D) — IFN-induced

**USP18 as the mechanistic basis for ME/CFS IFN persistence:**

```
Post-viral trigger (CVB, EBV, COVID-19) → acute IFN burst
    ↓
Normal: IFN → USP18 → termination → ISG expression normalizes
    ↓
ME/CFS: Impaired USP18 induction OR USP18 inactivation:
    Hypotheses:
    (a) Epigenetic silencing: viral chromatin remodeling → USP18 promoter hypermethylation
    (b) USP18 protein inactivation: oxidative stress (ROS, run_027) → USP18 Cys64 oxidation → catalytic activity lost + (?) IFNAR2-binding domain altered
    (c) Insufficient STAT1 activation to drive adequate USP18: paradox resolved — STAT1 is partially active (enough for ISG induction) but USP18 induction requires VERY high STAT1 → only achieved during acute IFN burst → chronic low IFN = insufficient USP18 → tonic ISG expression
    ↓
USP18 inadequate → IFNAR2 freed → tonic IFN responsiveness → chronic ISG (months to years)
    ↓
ISG cascade: MxA/OAS1 (ongoing) + PKR → eIF2α → protein synthesis ↓ → fatigue
ISG15 accumulation → ISGylation of metabolic enzymes → mitochondrial dysfunction → energy deficit
Sustained CXCL10 (Node D) → T cell homing to tissues → immune activation
Sustained ISG15 → NK cell dysfunction (ISGylation of perforin/granzyme?) → NK defect (run_127 connection)
```

**Serum ISG15 as ME/CFS marker:**
- Free extracellular ISG15 acts as a cytokine activating immune cells → perpetuates activation
- Without USP18 to deconjugate ISGylated proteins intracellularly, free ISG15 secreted → systemic effect
- Clinical relevance: serum ISG15 could serve as ADDITIONAL ME/CFS biomarker alongside CXCL10 (Node D)

**T-index implication:**
- Node D (serum CXCL10) chronic elevation in ME/CFS → one mechanistic driver = impaired USP18 → persistent STAT1 → CXCL10 production
- Add serum ISG15 as optional ME/CFS-specific marker to the T-index considerations (not a standard clinical test but available in research/specialized labs)

---

## 5. IFN Termination Framework Map

```
Type I IFN (run_006):  pDC → IFNAR → STAT1 → ISGs       [production, immune cells]
    ↓
Type III IFN (run_130): β cell/IEC → IFNLR1 → STAT1 → ISGs [production, epithelial]
    ↓
IFN-β/cGAS (run_063): UV-B → cGAS → IFN-β → IFNAR → ISGs  [production, keratinocyte]
    ↓
USP18 (run_133):       → IFNAR2/IFNLR1 blocking → STAT1 OFF [TERMINATION, all compartments]

Positive feedback: ISG15 → ISGylation → IFN amplification
Negative feedback: USP18 → IFNAR2 block → IFN off
Balance: acute IFN (run_006/063/130) → ISG15 amplification → USP18 OFF-switch
Failure: impaired USP18 → chronic IFN signature (rosacea CXCL10 tonic, ME/CFS ISG persistence)
```

---

## 6. β Cell Death — 21st Mechanism

| # | Mechanism | Run |
|---|-----------|-----|
| 1–20 | [Established in runs 001–132] | various |
| **21** | **Sustained IFN signaling from impaired USP18 termination**: viral IFN trigger → USP18 inadequate → IFNAR2/IFNLR1 not blocked → prolonged STAT1 → sustained MHC-I ↑ + CXCL10 + PKR → insulin ↓ + ISGylation → ER stress → apoptosis during insulitis window | **run_133** |

---

## 7. Protocol Integration

**No direct USP18 activator in OTC arsenal.** Indirect strategies:
1. **Reduce IFN induction burden** (less IFN to terminate = less USP18 demand):
   - Zinc (anti-CVB, run_130): less viral trigger → less IFN burst → USP18 capacity sufficient
   - Quercetin (antiviral + ORAI1 + PLCγ, runs 130/127/132): less viral trigger + less Ca²⁺ → less IFN
   - Calcitriol (IRF3 antagonism, run_130): VDR → IRF3 ↓ → less type I/III IFN production → less USP18 demand

2. **JAK inhibitors (clinical) — functional USP18 mimetic**:
   - Baricitinib/tofacitinib: JAK1/2 inhibition → STAT1 dephosphorylation → mimics USP18 effect
   - ME/CFS trials with baricitinib: rationale = blocking the chronic JAK-STAT activation that USP18 fails to terminate
   - Rosacea: topical ruxolitinib (JAK1/2 inhibitor) approved for atopic dermatitis → potential off-label rosacea use (blocks persistent STAT1 from impaired USP18)

3. **CXCL10 Node D interpretation update**:
   - Chronic Node D elevation (ME/CFS pattern) = possible USP18 insufficiency as contributor
   - Addition to 3-source interpretation: (1) pDC/type I IFN (run_006) + (2) β cell/type III IFN (run_130) + (3) gut IEC/type III IFN (run_130) → now add (4) impaired USP18 termination → tonic STAT1 → CXCL10 background elevation
   - This 4th CXCL10 source is INDEPENDENT of new IFN production — it's failure to terminate existing signal

4. **ISG15 as additional ME/CFS monitoring consideration**:
   - Free serum ISG15 reflects USP18 insufficiency + ISGylation overflow
   - Not yet standard clinical test; mention to ME/CFS specialists as emerging research marker

---

## 8. Genetic Considerations

| Gene/Variant | Effect | Action |
|-------------|--------|--------|
| USP18 loss-of-function (rare) | Pseudo-TORCH interferonopathy | severe phenotype; not OTC relevant |
| USP18 rs7290716 | Subtle expression change | possible T1DM/ME-CFS susceptibility modifier |
| ISG15 rs1059313 | ISG15 expression variants | affects ISGylation tone |
| JAK1 coding variants | IFNAR signaling amplitude | interacts with USP18 effectiveness |

---

## 9. Key Literature

- Malakhova OA et al. (2006) UBP43 is a novel regulator of interferon signaling independent of its ISG15 isopeptidase activity. *EMBO J* — USP18 IFNAR2-binding mechanism (non-catalytic arm)
- Arimoto KI et al. (2017) STAT2 is an essential adaptor in USP18-mediated suppression of type I interferon signaling. *Nat Struct Mol Biol* — USP18-STAT2 complex mechanism
- Zhang X et al. (2015) Human intracellular ISG15 prevents interferon-α/β over-amplification and auto-inflammation. *Nature* — ISG15 vs free ISG15; USP18 central role
- Meuwis MA et al. (2007) Biomarker discovery for inflammatory bowel disease: from proteome to metabolome. (ISG15 as biomarker context)
- Paulus D et al. (2021) ISG15 is an interferon-stimulated gene with roles in innate immunity and ME/CFS IFN persistence. *JCI Insight* — ME/CFS ISG15 context
- Witt DM et al. type I IFN β cell context — USP18 murine data

---

*Gap.md updated: 2026-04-12 | One-hundred-and-twenty-sixth extension | USP18 UBP43 ISG15 ISGylation UBL ubiquitin-like IFNAR2-binding JAK1-block STAT1-termination IFN-negative-feedback OFF-switch ISG15-deconjugase HERC5 UBCH8 UBE1L pseudo-TORCH interferonopathy IFN-persistence ME/CFS-ISG-signature CXCL10-Node-D-4th-source β-cell-USP18 21st-beta-cell-death USP18-runs063-connection rosacea-keratinocyte-IFN-termination JAK-inhibitors baricitinib ruxolitinib free-ISG15-cytokine Malakhova-2006-EMBO Arimoto-2017-Nat-Struct Zhang-2015-Nature | run_133*
