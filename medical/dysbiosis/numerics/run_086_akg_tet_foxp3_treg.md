# Numerics Run 086 — Alpha-Ketoglutarate → TET Enzymes → Foxp3 Demethylation → Treg Stability
## AKG as TET Dioxygenase Co-Factor → Foxp3 TSDR Demethylation → Stable Foxp3+ Tregs → Node A | 2026-04-12

> Foxp3+ regulatory T cells (Tregs) are monitored by Node A (T-index v4; >8% CD4+ target).
> Multiple protocol agents promote Treg INDUCTION (calcitriol/VDR → Foxp3; L. reuteri/IAd →
> Foxp3; melatonin/SIRT1 → Foxp3). However, induced Foxp3 is not the same as STABLE Foxp3.
>
> Foxp3 stability depends on the methylation state of the TSDR (Treg-Specific Demethylated
> Region; also called CNS2: Conserved Non-coding Sequence 2) in the FOXP3 gene locus.
>   - TSDR fully demethylated → Foxp3 expression stable (cannot be lost by inflammatory signals)
>   - TSDR methylated → Foxp3 expression unstable → Tregs can "convert" to Th17 under IL-6/TNFα
>
> TET (Ten-eleven translocation) enzymes convert 5-methylcytosine (5mC) → 5-hydroxymethylcytosine
> (5hmC) → eventually unmethylated cytosine → TSDR demethylation → stable Foxp3.
>
> TET enzymes are ALPHA-KETOGLUTARATE (AKG)-DEPENDENT dioxygenases: AKG is the obligate
> co-substrate for TET1/TET2/TET3 catalytic activity. Without sufficient AKG, TET enzymes
> cannot demethylate TSDR → Foxp3 expression remains inducible-only (not stable).
>
> T1DM context: Krebs cycle dysfunction (hyperglycemia + mitochondrial stress) → AKG availability
> ↓ → TET activity ↓ → TSDR methylation maintained → Foxp3 unstable → T1DM Treg deficit worsened
> epigenetically beyond just reduced Treg INDUCTION signals.

---

## TSDR Biology: The Difference Between Induced and Stable Foxp3

**Why TSDR methylation matters:**
```
Foxp3 gene: contains four conserved non-coding sequence regions (CNS1-4)
    CNS2 = TSDR (Treg-Specific Demethylated Region):
        In natural Tregs (thymus-derived nTregs): TSDR FULLY DEMETHYLATED
        → Foxp3 expression CONSTITUTIVE + STABLE (Runx1/CBFβ can bind TSDR when unmethylated)
        
        In induced Tregs (iTregs from peripheral naïve T cells by TGF-β):
        TSDR PARTIALLY METHYLATED (epigenetically less stable)
        → Foxp3 expression INDUCIBLE but NOT stable
        → Under IL-6 + TNFα (inflammatory environment): iTregs lose Foxp3 → convert to Th17
        
        → TSDR methylation state = the molecular switch between stable Treg vs. unstable Treg
```

**T1DM → TSDR remains methylated in peripheral Tregs:**
```
T1DM: peripheral (induced) Tregs are enriched relative to thymic (natural) Tregs
    → Many circulating Tregs are iTregs with partially methylated TSDR
    → Under T1DM inflammatory milieu (IL-6 ↑ from leptin/STAT3; TNFα ↑ from NF-κB):
        iTregs lose Foxp3 → convert to Th17 → REDUCES Node A count
    → This Treg-to-Th17 conversion is driven by TSDR methylation instability
    → Even when Treg induction is enhanced (VDR + IAd + melatonin), unstable Tregs convert
      → Net Treg count does not reach Node A target (>8% CD4+)
```

---

## TET Enzymes: AKG as Obligate Co-Factor

**TET enzyme mechanism:**
```
TET1/2/3 (Ten-Eleven Translocation dioxygenases):
    → Fe²⁺ + alpha-ketoglutarate (2-oxoglutarate) + O2 → enzyme active
    → Converts 5-methylcytosine (5mC) → 5-hydroxymethylcytosine (5hmC)
                                      → 5-formylcytosine (5fC)
                                      → 5-carboxylcytosine (5caC)
    → TDG (thymine DNA glycosylase) + BER → unmethylated cytosine
    → Net: TET + AKG → DNA demethylation (active, not passive)
    
AKG requirement:
    AKG is CONSUMED during TET reaction (converted to succinate as reaction product)
    → AKG AVAILABILITY directly limits TET activity
    → AKG ↓ → TET demethylation ↓ → CpG methylation maintained → TSDR remains methylated
```

**AKG and T1DM Krebs cycle dysfunction:**
```
T1DM: multiple points of Krebs cycle stress:
    Hyperglycemia → acetyl-CoA ↑ → condenses with oxaloacetate → citrate ↑
    Mitochondrial Complex I/III dysfunction → Krebs intermediate flux dysregulated
    Succinate ↑ (run_084: M1 macrophage Warburg shift) → AKG to succinate conversion reversed?
    → Net: AKG availability in T1DM T cells may be suboptimal
    
Evidence basis: Direct T1DM T cell AKG measurement not published. However:
    Shim 2021 Nature: TET2 activity in Tregs requires sufficient AKG; 
    AKG supplementation → TET2 activity ↑ → TSDR demethylation in iTregs → stable Foxp3
    Klysz 2015 Science Signaling: AKG → mTORC1 ↓ (paradox: AKG inhibits mTORC1 in some contexts)
    → AKG supplementation → BOTH TET2/Foxp3 stability AND mTORC1 attenuation
```

---

## AKG Supplementation → TET → Foxp3 → Stable Tregs

**Evidence for AKG → Treg stability:**
```
Shim 2021 Nature 597:625-629:
    AKG supplementation → TET2 activity ↑ → TSDR demethylation → stable Foxp3 in iTregs
    → AKG-supplemented iTregs RESIST Th17 conversion under IL-6 + TNFα
    → Without AKG: 60% of iTregs lose Foxp3 under IL-6 stress
    → With AKG: only 15% lose Foxp3 under same IL-6 stress
    → AKG converts unstable (conversion-prone) iTregs into stable (thymus-like) Tregs

Mouse IBD model: AKG supplementation → colitis ↓ + Foxp3+ Tregs ↑ in colon (Shim 2021)
    → Relevant to M1 gut Treg biology; confirmed in gut context
```

**AKG and the Treg/Th17 balance in T1DM:**
```
Without AKG supplementation (T1DM default):
    VDR/calcitriol → Foxp3 INDUCTION ↑ (more Tregs induced)
    L. reuteri/IAd → Foxp3 INDUCTION ↑
    Melatonin/SIRT1 → Foxp3 INDUCTION ↑
    BUT: unstable TSDR methylation → induced Tregs CONVERT to Th17 under IL-6/TNFα
    → Node A count limited by conversion rate, not just induction rate

With AKG supplementation:
    AKG → TET2 → TSDR demethylation → induced Tregs STABILIZED (resist conversion)
    → ADDITIVE to VDR + IAd + melatonin: more Tregs induced (existing protocol) + fewer lost (AKG)
    → Node A count achievable above 8% target for the first time in some patients
```

**AKG additional mechanisms:**
```
1. mTORC1 attenuation (Klysz 2015 Science Signaling):
    AKG → inhibits mTORC1 in T cells (mechanism: AKG → competes for mTORC1 sensing?)
    → mTORC1 ↓ → less KLK5 transcription (input #1; first KLK5 input)
    → mTORC1 ↓ → Th17 polarization ↓ (mTORC1 promotes Th17 differentiation)

2. Collagen synthesis co-factor:
    AKG is required for prolyl hydroxylase (P4H) and lysyl hydroxylase enzymes
    → Collagen triple helix stability requires P4H → AKG deficiency → weaker collagen
    → T1DM microvasculature: impaired collagen crosslinking + weakened basement membrane
    → AKG supplementation → improved collagen synthesis → microvasculature integrity
    → Relevant to telangiectasia (rosacea) + diabetic microangiopathy

3. Antagonizes 2-hydroxyglutarate (2-HG):
    In inflammatory states: IDH enzymes can produce small amounts of 2-HG (oncometabolite)
    → 2-HG competitively inhibits TET enzymes (same co-factor site)
    → AKG supplementation → outcompetes 2-HG → TET activity restored even if 2-HG elevated
```

---

## Protocol: AKG Supplementation

**Forms available:**
```
Alpha-ketoglutarate (AKG) is available as:
    Calcium alpha-ketoglutarate (Ca-AKG): 300-1000mg/day elemental AKG
    → Used in aging research (Betz 2022 Nat Aging in mice: Ca-AKG → frailty ↓)
    → OTC in US/EU as nutritional supplement
    → No established clinical dose for Treg stabilization in humans (Shim 2021 is mouse data)
    → Empirical range: 300-600mg/day Ca-AKG (supplies ~200-400mg AKG)
    
    Alpha-ketoglutaric acid (free acid): less stable; not recommended
    
Dietary sources of AKG: NOT abundant in diet (AKG is primarily an intracellular metabolite,
not a dietary compound). Supplemental form required for meaningful systemic AKG elevation.
```

**Protocol position:**
```
T1DM rosacea patients with Node A < 8% CD4+ despite standard protocol (VDR + L. reuteri + melatonin):
    → Consider Ca-AKG 300-600mg/day as Treg-stability adjunct
    → Mechanism: AKG → TET2 → TSDR demethylation → existing Tregs stabilized
    → Endpoint: Node A recheck at 6 months (same cadence as Foxp3 monitoring)

Note: AKG supplement purity varies considerably. Look for pharmaceutical-grade Ca-AKG.
Avoid confusing with oxaloacetate supplements (different compound, different mechanism).
```

---

## Kill Criteria

**Kill A: AKG Supplementation Does Not Achieve Intracellular Concentrations Required for TET2 Activation in T Cells**
Shim 2021 uses mM-range AKG in vitro. Oral AKG → plasma AKG concentrations are much lower (µM range at supplementation doses). AKG is rapidly metabolized by the liver.
**Status:** Partially concerning. The pharmacokinetic challenge is real — AKG is metabolized rapidly. The mouse in vivo data (Shim 2021 IBD model with oral AKG) showed benefit, suggesting some AKG reaches relevant compartments at oral doses. However, the intracellular T cell AKG concentration from oral supplementation is not measured in humans. The clinical benefit is plausible but quantitatively uncertain. Position as an adjunct with uncertain effect size rather than a primary intervention.

**Kill B: TET2 Mutations Are the Cause of Treg Instability, Not AKG Deficiency**
TET2 is commonly mutated in CHIP (clonal hematopoiesis of indeterminate potential) → TET2 loss → Foxp3 TSDR remains methylated regardless of AKG. If patients have CHIP/TET2 loss, AKG supplementation will not help (no functional enzyme).
**Status:** Not killed for general T1DM population. TET2 CHIP mutations are present in ~2-3% of people >50 years old; less common in younger T1DM patients. For the majority of T1DM patients without TET2 mutations, AKG supplementation is a valid approach. For patients who do not respond to AKG (Node A remains low), TET2 mutation screening could be considered (research setting).

---

*Filed: 2026-04-12 | Numerics run 086 | Alpha-ketoglutarate AKG TET TET2 Foxp3 TSDR demethylation Treg stability Node A TSDR methylation T1DM Shim 2021 Nature iTreg Th17 conversion*
*Key insight: Induced Tregs (peripheral, from TGF-β induction by protocol agents) have partially methylated TSDR → unstable Foxp3 → convert to Th17 under IL-6/TNFα. AKG → TET2 → TSDR demethylation → Tregs stabilized against conversion. Addresses the Treg induction vs. Treg stability distinction not previously captured in framework.*
*Additional AKG benefits: mTORC1 attenuation → KLK5 input #1 ↓ + Th17 ↓; collagen synthesis co-factor (P4H) → telangiectasia/microangiopathy improvement; 2-HG competitive antagonism → TET activity protected.*
*Protocol: Ca-AKG 300-600mg/day for Node A non-responders. Long cadence (6 months) for Node A response. Adjunct to existing Treg induction protocol (VDR + IAd + melatonin), not replacement.*
