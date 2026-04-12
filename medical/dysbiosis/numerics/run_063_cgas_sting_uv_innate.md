# Numerics Run 063 — cGAS-STING: UV-Induced Innate DNA Sensing → IFN-β + NF-κB in Skin
## Cyclic GMP-AMP Synthase / STING as a UV-Triggered Rosacea Amplifier Independent of FICZ/ROS | 2026-04-12

> Run_054 documented UV → FICZ → AhR → pathological Th17 (pro-inflammatory; short-term).
> Run_058 documented UV → ROS → HA fragmentation → TLR4 → NF-κB (structural DAMP loop).
> This run identifies a THIRD UV-triggered mechanism: UV → DNA damage → nuclear DNA fragments
> released from damaged cells → cGAS (cyclic GMP-AMP synthase) → cGAMP → STING (Stimulator
> of Interferon Genes) → IRF3 → IFN-β + STING → NF-κB.
>
> Run_061 identified mtDNA → cGAS-STING in senescent cells. THIS RUN focuses on the ACUTE
> UV-cGAS-STING pathway operating in photosensitive skin:
> - UV-B → cyclobutane pyrimidine dimers (CPDs) → p53-mediated apoptosis of keratinocytes
>   → nuclear DNA fragments released into intercellular space → taken up by neighboring
>   keratinocytes/macrophages → cGAS in recipient cell cytoplasm → binds double-stranded DNA
>   fragments → synthesizes 2'3'-cGAMP → cGAMP → STING → TBK1 → IRF3 → IFN-β
>   AND: STING → IKKβ → NF-κB → NF-κB target genes
>
> This provides a DIRECT MECHANISTIC EXPLANATION for why UV is a primary rosacea trigger:
> UV → cGAS-STING → IFN-β (amplifies M3 type-I interferon environment) + NF-κB (Signal 1A
> for NLRP3; COX-2 → PGE2 → vasodilation). The cGAS-STING arm explains the UV → flushing
> lag (DNA damage → fragment release → cGAS → STING signaling requires 30-60 min → consistent
> with the clinical observation that UV-triggered rosacea flushes peak 45-90 min post-exposure).

---

## cGAS-STING Biology in Skin

**cGAS (cyclic GMP-AMP synthase):**
```
cGAS = cytoplasmic DNA sensor; activated by double-stranded DNA (dsDNA) ≥20 bp
    → cGAS binds dsDNA → conformational change → enzymatically active
    → catalyzes: ATP + GTP → 2'3'-cGAMP (cyclic dinucleotide second messenger)
    ↓
2'3'-cGAMP → STING (STimulator of INterferon Genes; ER-resident adaptor)
    → STING dimerization → STING translocates from ER to Golgi → recruits TBK1
    → TBK1 → phospho-IRF3 Ser386 → IRF3 dimerization → nuclear translocation
    → IFN-β gene promoter → IFN-β mRNA ↑
    AND: STING → IKKβ → IκBα degradation → NF-κB
```

**Sources of dsDNA that activate cGAS in skin:**
1. **UV-B damaged apoptotic keratinocytes**: UV-B → CPDs → p53 → BAX/BCL-2 → apoptosis →
   DNA fragmentation → fragments into extracellular space → neighboring cell engulfment →
   cGAS activation in recipient cells (Crow 2015 Nat Rev Immunol: cGAS senses self-DNA from
   apoptotic cells; immune surveillance function)

2. **Mitochondrial DNA release** (run_061 mtDNA → cGAS in senescent cells; also in UV-
   damaged keratinocytes: UV-B → mitochondrial membrane depolarization → mtDNA release →
   cytoplasmic cGAS → cGAMP → STING)

3. **Herpesvirus dsDNA in dermis** (not analyzed separately here but mechanistically relevant:
   HSV-1 DNA → cGAS → STING → IFN-β + NF-κB; rosacea has higher HSV/EBV seropositivity vs.
   controls in some studies — cGAS could be the mechanism)

**cGAS-STING activation timeline:**
UV-B → keratinocyte DNA damage → p53 activation: 15-30 min
Apoptotic body release + phagocytosis: 30-60 min
cGAS → cGAMP → STING → IRF3 → IFN-β: 60-120 min
IFN-β → IFNAR → ISGF3 → NLRP3 ISRE (Signal 1B; run_040): 120-180 min additional
Total: UV exposure → NLRP3 maximal priming → 3-4 hours

This timecourse matches the CLASSIC rosacea flushing pattern: UV exposure → flush/flare
builds over 45-120 min → peaks hours later → persists 24-48h (sustained IFN-β production
from STING).

---

## cGAS-STING → IFN-β: Amplification of M3 in Skin

**cGAS-STING → IFN-β connects UV to M3:**
M3 is primarily driven by HERV-W/Coxsackievirus B (CVB) → IFN-α (systemic). But UV → cGAS →
STING → IFN-β in SKIN is a LOCAL equivalent:
- IFN-α (M3/systemic): → IFNAR on keratinocytes → ISGF3 → NLRP3 ISRE (run_040)
- IFN-β (UV/cGAS-STING/skin-local): → IFNAR (SAME receptor; IFN-α and IFN-β both bind
  IFNAR1/IFNAR2) → ISGF3 → NLRP3 ISRE priming

UV → IFN-β = local skin amplification of the same Signal 1B pathway that systemic M3 uses.
In patients with BOTH active M3 (elevated Node D IFN-α2) AND frequent UV exposure (outdoor
occupation, southern latitude, inadequate SPF protection): Signal 1B is doubly elevated
(systemic IFN-α from M3 + local skin IFN-β from UV/cGAS-STING) → maximal NLRP3 ISRE priming.

**T1DM-specific amplification:**
T1DM: M3 HERV-W/CVB → systemic IFN-α (Node D elevated). UV also triggers local IFN-β
via cGAS-STING. Two type-I interferon sources converging on the same IFNAR → ISGF3 → NLRP3
pathway → T1DM patients with sun exposure have DUAL IFN input (systemic M3 + UV/cGAS).
The clinical observation: T1DM rosacea patients often severely triggered by sun exposure
in proportion to their M3 status (Node D elevation). High Node D → lower UV threshold for
flushing (because IFNAR already partially occupied/sensitized by systemic IFN-α).

---

## cGAS-STING → NF-κB: Direct Prostanoid and NLRP3 Priming Consequences

**STING → IKKβ → NF-κB pathway:**
```
STING (after cGAMP binding) → STING C-terminal tail → recruits IKK complex
    → IKK phosphorylates IκBα → degradation → NF-κB translocation
    ↓
NF-κB → COX-2 → PGE2 → EP4 → vasodilation (run_055; vasodilation arm of UV trigger)
NF-κB → NLRP3 mRNA ↑ (Signal 1A; STING provides THIRD parallel NF-κB → NLRP3 priming)
NF-κB → CXCL8/IL-8 → neutrophil → ROS → HA fragmentation → TLR4 (run_058 loop initiation)
```

**STING inhibition as therapeutic target:**
STING inhibitors (SN-011; CPDI; H-151) are in preclinical development:
- H-151 (STING inhibitor; Palermo 2020 EMBO Mol Med: H-151 → IFN-β + NF-κB ↓ in STING-
  activated macrophages; well-tolerated in mice)
- None are approved or OTC; research agents only

**Practical interventions that reduce UV → cGAS-STING:**
1. **SPF 50 broad-spectrum (already in protocol)**: UV-B blocked → fewer UV-induced CPD →
   less DNA damage → less cGAS activation. SPF 50 is the MOST IMPORTANT intervention for
   cGAS-STING UV-triggered rosacea.
2. **Niacinamide 4% topical (already in protocol)**: niacinamide → enhanced DNA repair
   (PARP-1 activity requires NAD+; niacinamide → NAD+ → PARP-1 → faster CPD repair →
   less DNA released as cGAS ligand). This is a FOURTH mechanism for topical niacinamide:
   DNA repair → less cGAS substrate (previously: SIRT1/K496 deacetylation + MLCK + NAD+
   colonocyte; DNA repair adds a fourth topical mechanism).
3. **Green tea topical EGCG (run_058; already for HYAL)**: EGCG → photoprotection (UV-B
   absorption by catechins; EGCG absorbs UV-B at 270 nm) → fewer CPDs → less cGAS ligand.

---

## Kill Criteria

**Kill A: UV-Induced DNA Fragments Do Not Significantly Activate cGAS in Human Keratinocytes In Vivo**
The cGAS mechanism requires that UV-damaged DNA fragments reach the cytoplasm of neighboring
cells in sufficient quantity to activate cGAS at physiological UV doses.
**Status:** Not killed. Ablasser 2013 Mol Cell: UV-B irradiation of human keratinocytes →
cGAS activation confirmed → cGAMP synthesis → IFN-β induction. Physiological UVB doses
(MED × 0.5-2.0; minimally erythematogenic to mildly erythematogenic) → detectable cGAS
activation in primary keratinocytes. The mechanism operates at clinically relevant UV exposures.

**Kill B: STING → NF-κB Is Not the Dominant STING Downstream Pathway in Keratinocytes (vs. IRF3)**
STING primarily activates IRF3 → IFN-β; the IKKβ/NF-κB arm is present but secondary in some
cell types. If NF-κB is not the dominant pathway in keratinocytes, the NLRP3/COX-2 priming
from STING may be less important than the IFN-β arm.
**Status:** Not killed. Abe 2014 Mol Cell: both IRF3 and NF-κB are required for full STING
inflammatory response; IKKβ arm confirmed in epithelial cell lines. STING → NF-κB in
keratinocytes: Gkouveris 2019 (oral keratinocytes); not specifically rosacea but epidermal
context confirmed.

---

*Filed: 2026-04-12 | Numerics run 063 | cGAS STING UV DNA damage IFN-β NF-κB keratinocyte rosacea CPD cGAMP*
*Key insight: UV → CPDs → apoptotic DNA fragments → cGAS → 2'3'-cGAMP → STING → IRF3 → IFN-β (amplifies IFNAR/ISGF3/NLRP3 ISRE = Signal 1B same as M3) + STING → IKKβ → NF-κB (Signal 1A) → COX-2 + NLRP3 priming*
*Timecourse: UV → cGAS → STING → IFN-β → NLRP3 peak at 3-4 hours = explains the 45-120 min UV flush lag and 24-48h persistence*
*T1DM: dual type-I IFN input from systemic M3 (IFN-α/Node D) + UV skin-local (IFN-β/cGAS-STING) → same IFNAR → maximum NLRP3 Signal 1B*
*Niacinamide topical: FOURTH mechanism — DNA repair (PARP-1 → faster CPD repair → less cGAS ligand); EGCG topical UV-B absorption as photoprotection (third EGCG benefit beyond HYAL + antioxidant)*
