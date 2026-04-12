# Numerics Run 089 — PPAR-α: Primary Omega-3 Macrophage Nuclear Receptor → NF-κB Transrepression + Warburg Shift ↓
## EPA/DHA → PPAR-α (Not PPARγ) → p65 Coactivator Block + β-Oxidation → Succinate ↓ → HIF-1α ↓ | T1DM Retinopathy Benefit | 2026-04-12

> Three omega-3 mechanisms are in the framework: GPR120 (run_062: surface receptor → Th17 ↓),
> PPARγ (run_077: nuclear receptor → transrepression; omega-3 is a WEAK PPARγ agonist),
> and SPM/resolvins (run_020: bioactive lipid metabolites → resolution). A FOURTH mechanism
> has been overlooked: PPAR-ALPHA.
>
> EPA and DHA are strong endogenous PPAR-α agonists (EC50 ~1-10 µM) — this is the DOMINANT
> omega-3 nuclear receptor interaction, not PPARγ (for which omega-3 has EC50 ~50-100 µM,
> ~10-100x weaker). PPAR-α is the primary fatty acid-sensing nuclear receptor in macrophages,
> liver, and cardiac tissue.
>
> PPAR-α anti-inflammatory mechanism (macrophages):
> (a) TRANSREPRESSION: PPAR-α (ligand-activated) → sequesters CBP/p300 coactivator → p65/CBP
>     interaction ↓ → NF-κB transcriptional activity ↓ (distinct from PPARγ transrepression
>     mechanism, which involves Lys SUMO-ylation; run_077)
> (b) METABOLIC SHIFT: PPAR-α → β-oxidation gene expression ↑ (CPT1, ACOX1) → macrophage
>     metabolic shift AWAY from Warburg glycolysis → less succinate accumulation → PHD2
>     activity ↑ → HIF-1α degradation restored → IL-1β ↑ reversed (direct run_084 connection)
>
> T1DM-specific: ACCORD-Lipid 2010 trial (fenofibrate, the pharmacological PPAR-α agonist) →
> diabetic retinopathy progression ↓ in T2DM/T1DM-equivalent patients. The FIELD trial:
> fenofibrate → limb amputation ↓. These PPAR-α clinical benefits are independent of
> lipid-lowering and map to the anti-inflammatory/metabolic mechanisms above.

---

## PPAR-α Biology and Omega-3 Affinity

**PPAR family members and omega-3 ligand affinity:**
```
PPAR-α (NR1C1): expressed in liver >> heart/muscle >> macrophages/monocytes
    → Primary endogenous ligands: fatty acids (saturated, mono-, poly-unsaturated)
    → EPA/DHA affinity: EC50 ~1-10 µM (STRONG PPAR-α agonists)
    → Fenofibrate/fibrates: pharmacological PPAR-α agonists (prescription)
    → Function: fatty acid β-oxidation, anti-inflammatory transrepression
    
PPARγ (NR1C3): expressed in adipose >> macrophages > liver
    → Primary endogenous ligands: 15-deoxy-Δ12,14-PGJ2, oxylipins, thiazolidinediones
    → EPA/DHA affinity: EC50 ~50-100 µM (WEAK PPARγ agonists; run_077 basis)
    → Function: adipogenesis, insulin sensitivity, anti-inflammatory transrepression
    
PPARδ/β (NR1C2): expressed ubiquitously
    → EPA/DHA: intermediate affinity
    
CONCLUSION: When omega-3 activates nuclear receptors in macrophages, PPAR-α is the
DOMINANT interaction (10-100× stronger than PPARγ for same concentration).
The framework's run_077 analysis of omega-3/PPARγ captures the SECONDARY mechanism;
omega-3/PPAR-α was not analyzed.
```

**PPAR-α in macrophages — expression and activation:**
```
Macrophage PPAR-α expression:
    Resting macrophages: moderate PPAR-α mRNA (lower than liver, higher than T cells)
    M1 activation: PPAR-α expression ↓ (NF-κB + HIF-1α suppress PPAR-α; reciprocal antagonism)
    M2 activation: PPAR-α expression ↑ (IL-4, IL-13 → PPAR-α)
    → T1DM macrophages: M1-shifted → PPAR-α ↓ → less endogenous anti-inflammatory counter
    
Supplemental EPA → intracellular accumulation → PPAR-α re-activation:
    → Even in M1 macrophages, pharmacological EPA/DHA doses overcome M1-suppressed PPAR-α
    → EC50 ~1-10 µM: achievable at 3-4g/day omega-3 supplementation
    → Plasma EPA levels at 3g/day supplementation: ~100-200 µM total (free + esterified)
    → Intracellular free EPA: ~1-10 µM (after phospholipase A2 release from membranes)
    → IN RANGE for PPAR-α activation
```

---

## PPAR-α Mechanism 1: NF-κB Transrepression

**PPAR-α → CBP/p300 coactivator sequestration:**
```
Activated PPAR-α (+ RXRα heterodimer) interacts with:
    CBP (CREB-binding protein) / p300 co-activator complex
    → PPAR-α:RXRα:CBP/p300 complex formed → CBP/p300 sequestered
    
NF-κB (p65) requires CBP/p300 for full transcriptional activation:
    p65 + CBP/p300 → Lys310 acetylation of p65 (by p300 HAT) → p65 transcriptionally active
    → PPAR-α sequesters CBP/p300 → p65 Lys310 NOT acetylated → NF-κB target gene ↓
    
Evidence: Delerive 2001 Mol Endocrinol 15(8):1356-1369:
    PPAR-α → competitive coactivator displacement → IL-6, TNFα, NF-κB targets ↓ in macrophages
    → In vitro: EPA pre-treatment → PPAR-α activation → IL-1β ↓ 50-70% in LPS-stimulated macrophages
    
Distinct from PPARγ transrepression (run_077):
    PPARγ: SUMO-ylation of PPARγ LBD → recruits NCoR1/HDAC3 → maintains repressive chromatin at
           NF-κB target loci (active repression mechanism; requires SUMO E3 ligase PIAS1)
    PPAR-α: CBP/p300 sequestration → passive (competitive; no active chromatin remodeling)
    → Two distinct transrepression mechanisms; both suppress NF-κB but via different coactivator paths
    → Protocol: omega-3 provides BOTH PPAR-α AND PPARγ transrepression (additive, distinct mechanisms)
```

**IL-6 production specifically:**
```
PPAR-α → CBP/p300 sequestration → p65 Lys310 not acetylated → IL-6 promoter NF-κB site:
    IL-6 → STAT3 → RORγt → Th17 (run_062 context: omega-3 → less IL-6 → less Th17)
    
Previous framework: omega-3 → GPR120 → ERK1/2 ↓ → IL-6/IL-23 ↓ (surface receptor)
Now: omega-3 → PPAR-α → CBP/p300 sequestration → IL-6 ↓ (nuclear receptor; intracellular)
    → Two distinct mechanisms for omega-3 → IL-6 ↓:
        (1) GPR120 (cell surface → signal transduction)
        (2) PPAR-α (intracellular → transcription factor competition)
    → Both additive; explains why omega-3 has strong IL-6-suppressing effect in clinical studies
```

---

## PPAR-α Mechanism 2: Macrophage Warburg Shift ↓ → Succinate ↓ → HIF-1α ↓

**Direct connection to run_084 succinate/HIF-1α mechanism:**
```
Run_084: M1 macrophage → Warburg shift → succinate accumulation → PHD2 inhibition →
    HIF-1α stabilized at normoxia → IL-1β ↑ (Signal 1C metabolic route)

PPAR-α interrupts this chain at the Warburg shift:
    PPAR-α → activates CPT1a (carnitine palmitoyltransferase 1a) → fatty acid transport into
              mitochondria for β-oxidation
    PPAR-α → activates ACOX1, HADHA → peroxisomal + mitochondrial β-oxidation genes ↑
    PPAR-α → PPARγ coactivator 1α (PGC-1α) interaction → mitochondrial biogenesis ↑
    
Net metabolic effect:
    PPAR-α → β-oxidation dominant → macrophage less dependent on glycolysis for ATP
    → Less Warburg shift under LPS stimulation
    → Succinate does not accumulate to same extent
    → PHD2 activity maintained → HIF-1α hydroxylated → degraded → IL-1β ↑ prevented
    
Evidence: Varga T 2011 Immunity 34(5):706-718:
    PPAR-α ligands → macrophage metabolic shift toward oxidative phosphorylation
    → Less glycolytic Warburg reprogramming under inflammatory conditions
    → Succinate/fumarate ratio maintained (less broken Krebs cycle)
```

**PPAR-α + run_084 protocol integration:**
```
Protocol element → mechanism → run_084 succinate/HIF-1α benefit:
    BHB (ketogenic): acetyl-CoA → less Warburg (mentioned in run_084)
    Metformin: Complex I mild inhibition → less mROS → less HIF-1α (indirect)
    PPAR-α (omega-3): β-oxidation ↑ → less Warburg shift → less succinate (DIRECT, new)
    
PPAR-α is actually the MOST DIRECT pharmacological Warburg-shift antagonist in the protocol:
    → Activates the metabolic counter-program (β-oxidation) directly
    → Does not just inhibit the Warburg pathway; actively competes for metabolic substrate
```

---

## T1DM Clinical Evidence: PPAR-α Benefits Beyond Rosacea

**ACCORD-Lipid trial (fenofibrate; pharmacological PPAR-α agonist):**
```
ACCORD-Lipid 2010 NEJM 362:1563-1574:
    T2DM patients (metabolically similar to T1DM in many parameters)
    Fenofibrate (145mg/day) + simvastatin vs. placebo + simvastatin
    
    Diabetic retinopathy: DR progression ↓ 40% with fenofibrate (unexpected; not lipid-mediated)
    → This DR benefit is PPAR-α mediated: PPAR-α → retinal VEGF ↓ + NF-κB ↓ + ROS ↓
    → Connects to run_084: succinate → HIF-1α → VEGF in T1DM vasculature;
      PPAR-α → less HIF-1α → less VEGF → less DR progression
    → DR has same VEGF/HIF-1α pathology as rosacea Loop 4 VEGF + telangiectasia

FIELD trial (fenofibrate): fenofibrate → limb amputation ↓ in T2DM
    → Peripheral macrophage/endothelial PPAR-α → less NF-κB-driven vascular inflammation
```

**Omega-3 vs. fenofibrate:**
```
Fenofibrate: pharmacological PPAR-α agonist (prescription; clinical evidence strongest)
    → T1DM: consider fenofibrate for T1DM patients with:
        (a) High triglycerides (standard indication)
        (b) Retinopathy (ACCORD-Lipid mechanism; off-label)
        
Omega-3 supplementation (3-4g/day EPA+DHA): dietary PPAR-α activation
    → EPA intracellular concentrations at this dose: ~1-10 µM (PPAR-α EC50 range)
    → Already in protocol for run_020/GPR120/SPM mechanisms
    → PPAR-α = ADDITIONAL mechanism being delivered simultaneously
    → No new agents required; omega-3 dose is sufficient
```

---

## Framework Position: Fourth Omega-3 Mechanism

**Complete omega-3 mechanism map (post-run_089):**

| Mechanism | Target | Pathway | Run |
|-----------|--------|---------|-----|
| 1. GPR120 activation | Cell surface receptor | → ERK1/2 ↓ → IL-6/IL-23 ↓ → Th17 ↓ | run_062 |
| 2. SPM production | Bioactive lipid mediators | → Resolvin D/E + protectin → resolution pathways | run_020 |
| 3. PPARγ activation (weak) | Nuclear receptor | → SUMO-PPAR-γ/NCoR1/HDAC3 → NF-κB chromatin repression | run_077 |
| 4. PPAR-α activation (primary) | Nuclear receptor | → CBP/p300 sequestration → NF-κB ↓ + Warburg shift ↓ → succinate ↓ → HIF-1α ↓ | **run_089** |

**PPAR-α vs. PPARγ from omega-3:**
- PPAR-α: EC50 1-10 µM → activated by omega-3 doses in protocol
- PPARγ: EC50 50-100 µM → weakly activated; requires polyphenol co-agonists (quercetin + resveratrol + EGCG for full PPARγ effect; run_077)
- Conclusion: omega-3/PPAR-α is the dominant single-agent nuclear receptor mechanism; omega-3/PPARγ requires polyphenol amplification

---

## Protocol: No New Agents Required

```
Existing omega-3 protocol: 3-4g/day EPA+DHA (long-chain omega-3)
    → PPAR-α is an ADDITIONAL mechanism being delivered by the existing dose
    → No new agents, no dose change
    
What changes post-run_089:
    → Mechanism count for omega-3 increases from 3 → 4
    → run_084 succinate/HIF-1α mechanism now has an ADDITIONAL upstream counter:
      omega-3/PPAR-α → Warburg shift ↓ → less succinate (alongside BHB + metformin)
    → T1DM patients with retinopathy: consider ophthalmology referral discussion re: fenofibrate
      (pharmacological PPAR-α) as adjunct to omega-3 (ACCORD-Lipid evidence)
    
Fenofibrate as T1DM adjunct (specialist discussion):
    T1DM + retinopathy + elevated TG: fenofibrate 145mg/day (ACCORD-Lipid)
    T1DM + rosacea + Node D elevated: omega-3 PPAR-α (run_089) + HCQ TLR7/9 (run_088) = Signal 1B coverage
    Not a primary rosacea-specific add; T1DM vascular complication context
```

---

## Kill Criteria

**Kill A: PPAR-α Macrophage Expression Is Too Low for Meaningful Anti-Inflammatory Effect**
PPAR-α is expressed at highest levels in liver/cardiac tissue; macrophage expression is meaningful but lower. Omega-3 concentrations achievable in macrophage cytoplasm may be insufficient for PPAR-α activation in vivo (cell culture EC50 vs. in vivo concentrations differ).
**Status:** Acknowledged as quantitative uncertainty. The in vitro evidence (Delerive 2001; Varga 2011) is confirmed in macrophage cell lines. Omega-3 plasma concentrations at 3-4g/day supplementation (100-200 µM total; free EPA ~1-10 µM) are within the PPAR-α EC50 range. Clinical evidence (ACCORD-Lipid: macrophage-rich retinal vessels responding to fenofibrate) supports in vivo PPAR-α activation in macrophage-rich tissues. Not killed; quantitative uncertainty acknowledged.

**Kill B: The PPAR-α Mechanism Is Already Captured by Existing Protocol Documentation**
The GPR120 + PPARγ + SPM mechanisms already document omega-3 anti-inflammatory benefits sufficiently; adding PPAR-α is redundant documentation of the same net effect.
**Status:** Not killed as a conceptual mechanism. The PPAR-α mechanism is MECHANISTICALLY DISTINCT (different pathway, different coactivator, different metabolic effect). The practical importance is: (1) it explains the succinate/HIF-1α (run_084) connection that run_084 left as "omega-3 may help via metabolic shift but mechanism unanalyzed"; (2) it justifies the T1DM fenofibrate/retinopathy discussion; (3) it completes the omega-3 mechanism taxonomy.

**Kill C: ACCORD-Lipid DR Benefit Is Confounded by Lipid-Lowering**
The retinopathy benefit in ACCORD-Lipid may be due to TG-lowering rather than PPAR-α anti-inflammatory effects.
**Status:** Partially challenging. ACCORD-Lipid TG subgroup analysis showed the DR benefit was NOT restricted to patients with high TG at baseline (Chew 2014 JAMA Ophthalmol); the effect was seen in TG-normal patients too → suggests lipid-independent (anti-inflammatory) PPAR-α mechanism. Not killed; lipid-independent component supported.

---

*Filed: 2026-04-12 | Numerics run 089 | PPAR-α EPA DHA omega-3 primary nuclear receptor CBP p300 NF-κB transrepression macrophage Warburg shift succinate HIF-1α ACCORD-Lipid fenofibrate diabetic retinopathy T1DM*
*Key insight: EPA/DHA are STRONG PPAR-α agonists (EC50 1-10 µM) and WEAK PPARγ agonists (EC50 50-100 µM). The framework's run_077 analyzed the SECONDARY omega-3 nuclear receptor mechanism (PPARγ); this run identifies the PRIMARY one (PPAR-α). PPAR-α provides: (1) NF-κB transrepression via CBP/p300 coactivator competition (distinct from PPARγ's SUMO-mediated repression); (2) macrophage β-oxidation ↑ → Warburg shift ↓ → succinate ↓ → HIF-1α ↓ (direct run_084 connection). No new agents required — omega-3 3-4g/day already delivers PPAR-α activation.*
*T1DM: ACCORD-Lipid fenofibrate → DR progression ↓ 40% (PPAR-α → VEGF ↓ via HIF-1α pathway). Omega-3 protocol already provides dietary PPAR-α coverage. T1DM + retinopathy: consider fenofibrate discussion with ophthalmology.*
