# Numerics Run 084 — Macrophage Immunometabolism: Succinate/HIF-1α vs. Itaconate/IRG1
## T1DM LPS → Warburg Shift → Succinate ↑ → HIF-1α → IL-1β ↑ | Itaconate → Nrf2 + p65 Cys38 → Counter-regulation | 2026-04-12

> Macrophage immunometabolism has not been analyzed in the framework. Classical M1 macrophage
> activation involves a metabolic shift (Warburg-like) that has pro-inflammatory consequences
> through two metabolites: succinate (pro-inflammatory) and itaconate (endogenous counter-
> regulatory). Both are Krebs cycle-derived. Both are relevant to T1DM gut dysbiosis where
> chronic LPS exposure forces macrophages into persistent M1 metabolic states.
>
> Succinate → HIF-1α mechanism (Tannahill 2013 Nature 496:238-242): M1 macrophages
> accumulate succinate via "broken Krebs cycle" → succinate → inhibits PHD2 (prolyl
> hydroxylase domain 2) → HIF-1α not hydroxylated → not degraded → HIF-1α ↑ → IL-1β
> mRNA stability + transcription ↑. This is a METABOLIC ROUTE to Signal 1A/NLRP3 priming.
>
> Itaconate → IRG1 counter-regulation (Lampropoulou 2016 Cell Metab 24:158): activated
> macrophages produce itaconate via IRG1 (immunoresponsive gene 1; cis-aconitate
> decarboxylase) → itaconate is an endogenous anti-inflammatory metabolite with TWO mechanisms:
> (a) electrophilic alkylation of KEAP1 → Nrf2 activation → anti-oxidant + anti-inflammatory
> (b) alkylation of p65 Cys38 → NF-κB transrepression (same Cys38 site as CAPE/propolis, run_004)

---

## Succinate → HIF-1α → IL-1β: The Pro-Inflammatory Immunometabolic Circuit

**M1 macrophage metabolic reprogramming:**
```
Resting macrophage: oxidative phosphorylation (OXPHOS) → ATP efficient
LPS/IFN-γ activation → M1 polarization → METABOLIC SHIFT:
    Glycolysis ↑ (Warburg effect: rapid ATP from glucose → pyruvate → lactate)
    Krebs cycle becomes "broken" at two points:
        (1) Citrate accumulates (exits to cytoplasm → lipid synthesis + itaconate)
        (2) Succinate accumulates (cannot proceed to fumarate efficiently)
    ↓
Succinate accumulates in M1 macrophage cytoplasm/mitochondria
```

**Succinate → HIF-1α → IL-1β (Tannahill 2013 Nature):**
```
Succinate ↑ → competitively inhibits PHD2 (prolyl hydroxylase domain 2):
    PHD2 normally: hydroxylates HIF-1α Pro402/Pro564 → VHL E3 ubiquitin ligase recognition
    → HIF-1α ubiquitinated → proteasomal degradation (rapid; t½ <5 min at normoxia)
    ↓
Succinate blocks PHD2 → HIF-1α NOT hydroxylated → NOT degraded by VHL
    → HIF-1α stabilized at NORMOXIA (pseudo-hypoxic state)
    → HIF-1α → IL-1β gene transcription ↑ (HRE in IL-1β promoter; confirmed in macrophages)
    → HIF-1α → VEGF ↑ (VEGF → telangiectasia; Loop 4 connection from run_061: SASP → VEGF)
    ↓
Result: LPS → M1 → succinate ↑ → HIF-1α stabilized → IL-1β ↑ + VEGF ↑
    = Metabolic amplification of Signal 1A (IL-1β → NLRP3 priming) via HIF-1α
```

**T1DM context — chronic LPS exposure → sustained succinate ↑:**
```
T1DM M1 gut dysbiosis → chronic low-grade LPS from gut → portal → systemic:
    → Macrophages (dermal + hepatic + circulating) chronically exposed to sub-threshold LPS
    → Persistent low-level M1 activation → "trained immunity" metabolic state
    → Succinate chronically elevated (not just during acute LPS spikes)
    → HIF-1α chronically semi-stabilized → IL-1β constitutively elevated
    → NLRP3 Signal 1A (IL-1β-mediated priming) from immunometabolic mechanism
    
Tannahill 2013 confirmed: succinate is elevated in LPS-stimulated macrophages by 6-fold.
In T1DM: plasma succinate elevated (Ferrannini 2013 Diabetes Care: succinate ↑ in T2DM;
    analogous T1DM metabolic changes). Also: HIF-1α (Signal 1C; run_050) is independently
    elevated by OSA/reoxygenation in T1DM → COMPOUNDED HIF-1α from metabolic + hypoxic sources.
```

---

## Itaconate → IRG1: The Endogenous Anti-Inflammatory Counter-Regulation

**IRG1 (immunoresponsive gene 1; gene: ACOD1):**
```
M1 macrophage activation → transcription factor NF-κB + HIF-1α → IRG1 gene expression ↑
    → IRG1 protein: cis-aconitate decarboxylase
    → Converts cis-aconitate (Krebs intermediate between citrate and isocitrate)
        → Itaconate (methylenesuccinic acid; a C5 unsaturated dicarboxylic acid)
    → Itaconate ACCUMULATES in M1 macrophages (up to mM concentrations intracellularly)
    → Itaconate is THE MOST HIGHLY INDUCED metabolite in LPS-activated macrophages
```

**Itaconate mechanism 1: KEAP1 alkylation → Nrf2 → anti-oxidant gene expression:**
```
Itaconate → electrophilic alkylation of KEAP1 Cys151/Cys273/Cys288 (same sites as sulforaphane!)
    → KEAP1 conformational change → cannot ubiquitinate Nrf2
    → Nrf2 stabilized → nuclear translocation → ARE binding → HO-1, NQO1, GCLM ↑
    → Anti-oxidant defense ↑ → ROS ↓ → NLRP3 Signal 2 ↓ + NF-κB Cys38 ↓

Comparison: sulforaphane (run_014 context: second NF-κB suppressor) → also KEAP1 alkylator
    Itaconate is an ENDOGENOUS sulforaphane-like compound: same KEAP1/Nrf2 mechanism
    Sulforaphane is the dietary version; itaconate is the macrophage's self-produced version
```

**Itaconate mechanism 2: p65 Cys38 alkylation → NF-κB transrepression:**
```
Itaconate → alkylates p65 Cys38 (Michael addition to electrophilic itaconate)
    → p65 Cys38 alkylation → p65 cannot bind DNA → NF-κB target gene ↓
    
This is the SAME Cys38 site targeted by:
    CAPE (caffeic acid phenethyl ester; run_004: fourth NF-κB suppressor)
    Propolis polyphenols
    Now: itaconate (endogenous)
    
Lampropoulou 2016 Cell Metab 24:158: itaconate → p65 Cys38 alkylation confirmed by
    mass spectrometry; NF-κB target gene ↓ in LPS-stimulated macrophages
    IRG1 knockout macrophages → MORE inflammatory (confirms itaconate's endogenous
    counter-regulatory role: without itaconate, LPS → uncontrolled NF-κB)
```

**Itaconate circuit in T1DM — potential impairment:**
```
Normal: LPS → M1 macrophage → (1) NF-κB → IL-1β ↑ SIMULTANEOUSLY WITH (2) IRG1 → itaconate → NF-κB ↓ (self-limiting)
    → Itaconate is the BRAKE on NF-κB activation; limits duration of inflammatory response

T1DM chronic dysbiosis → macrophages under chronic (not acute) LPS stimulation:
    Acute LPS: strong IRG1 induction → high itaconate → strong self-braking
    Chronic sub-threshold LPS: weaker IRG1 induction → less itaconate per LPS unit
    → T1DM macrophages: less itaconate-mediated self-braking → NF-κB runs longer per episode
    → Sustained IL-1β and NF-κB output despite moderate LPS stimulus
    
Evidence basis: Chronic LPS tolerance phenomenon (macrophages chronically exposed → reduced
    acute response to LPS). The itaconate arm may be differentially affected from the
    pro-inflammatory arm in chronically stimulated macrophages. Direct T1DM data not available;
    this is mechanistic inference.
```

---

## Framework Integration: Immunometabolic Amplification of Signal 1A

**New mechanistic chain:**
```
T1DM gut dysbiosis → LPS (TLR4) → M1 macrophage → Warburg shift:
    Pro-inflammatory arm: succinate ↑ → PHD2 ↓ → HIF-1α ↑ → IL-1β ↑ → NLRP3 priming ↑
    Counter-regulatory arm: itaconate ↑ (IRG1) → p65 Cys38 + KEAP1/Nrf2 → NF-κB ↓ + ROS ↓
    
In T1DM chronic dysbiosis: balance tilts toward pro-inflammatory
    (succinate elevation is sustained; itaconate braking is insufficient)
    
T1DM specific: HIF-1α from BOTH sources:
    Metabolic: succinate → PHD2 inhibition → HIF-1α ↑
    Hypoxic: OSA/reoxygenation (Signal 1C; run_050) → HIF-1α ↑ directly
    COMPOUNDED HIF-1α: higher IL-1β + VEGF in T1DM than non-T1DM same LPS level
```

**Connection to Signal 1C (HIF-1α, run_050):**
Signal 1C was documented as OSA (oxygen desaturation) → HIF-1α → NLRP3 NLRC4 priming.
Now: succinate → PHD2 → HIF-1α is a SECOND, non-hypoxic route to Signal 1C.
Any condition that elevates succinate (LPS, ischemia, high glucose) → pseudo-hypoxic HIF-1α → Signal 1C activation WITHOUT oxygen desaturation.

---

## Protocol: Addressing Macrophage Immunometabolism

**Existing protocol elements that affect succinate/HIF-1α axis:**
```
1. BHB (run_031 context):
    BHB → HCAR2 → cAMP → PKA → inhibits NLRP3 (established mechanism)
    ALSO: BHB enters Krebs cycle as acetyl-CoA → bypasses the glycolysis/succinate accumulation
    → Ketogenic diet → less macrophage Warburg shift → less succinate accumulation
    → HIF-1α less stabilized → IL-1β ↑ attenuated

2. Metformin (via AMPK, run_069):
    AMPK → Complex I inhibition (mild) → less mROS → less HIF-1α stabilization from ROS source
    AMPK → also mildly inhibits Warburg glycolysis → less metabolic reprogramming severity

3. Sulforaphane (second NF-κB suppressor, run_014):
    Sulforaphane → KEAP1 alkylation → Nrf2 → same pathway as itaconate mechanism 1
    Exogenous sulforaphane (dietary: broccoli sprouts) mimics endogenous itaconate/Nrf2 arm
    → Compensates for potentially reduced itaconate production in T1DM macrophages

4. CAPE/propolis (fourth NF-κB suppressor, run_004):
    CAPE → p65 Cys38 alkylation → same site as itaconate mechanism 2
    Exogenous CAPE mimics endogenous itaconate/p65 arm
    → Propolis BID compensates for itaconate self-braking deficit
```

**New protocol insight:**
Sulforaphane (broccoli sprouts) + CAPE (propolis) = DIETARY MIMICS of the two itaconate mechanisms. The protocol already delivers both itaconate effector mechanisms via two separate dietary agents — providing the functional equivalent of sustained itaconate production even in T1DM macrophages with reduced IRG1 response.

**Pharmacological succinate reduction (speculative):**
No approved agent specifically targets macrophage succinate accumulation. Potential targets:
- Dimethyl malonate (SDH inhibitor → less succinate → less HIF-1α? No — SDH converts succinate to fumarate; inhibiting SDH would increase succinate, not decrease it)
- Actually: reducing upstream glycolysis would reduce succinate. 2-DG (2-deoxyglucose) inhibits glycolysis → less Warburg → less succinate. But 2-DG is not clinically used for rosacea.
- Metformin via Complex I → reduces Warburg glycolytic drive indirectly.

---

## Kill Criteria

**Kill A: Succinate → HIF-1α Is Not Demonstrated in Dermal Macrophages Specifically**
Tannahill 2013 is in bone marrow-derived macrophages (BMDMs) from mice. Dermal macrophages (tissue-resident) may have different metabolic profiles and less Warburg shift capacity.
**Status:** Partially concerning for dermal-specific application. Resident tissue macrophages do show M1 reprogramming under LPS but may have different metabolic plasticity than BMDMs. The mechanism is confirmed in macrophages broadly; tissue-resident dermis-specific confirmation is lacking. Framework position: primary relevance is in circulating monocytes/macrophages (systemic) + any tissue macrophages recuited to lesional dermis; resident dermis macrophages are secondary.

**Kill B: Itaconate Impairment in T1DM Is Inferred, Not Measured**
The claim that T1DM macrophages have reduced itaconate production under chronic LPS is mechanistic inference without direct T1DM itaconate measurement data.
**Status:** Not killed as mechanism, but acknowledged as inference. The framework connection is that sulforaphane + CAPE provide functional compensation regardless of whether itaconate is truly reduced. The protocol benefit is independent of the inference being correct.

---

*Filed: 2026-04-12 | Numerics run 084 | Macrophage immunometabolism succinate HIF-1α IL-1β PHD2 itaconate IRG1 KEAP1 Nrf2 p65 Cys38 Tannahill 2013 Lampropoulou 2016 T1DM Warburg*
*Key insight: Succinate → PHD2 inhibition → HIF-1α stabilization at NORMOXIA = metabolic (non-hypoxic) activation of Signal 1C. T1DM macrophages under chronic LPS → sustained succinate elevation → constitutive partial HIF-1α → chronically elevated IL-1β.*
*Protocol elegance: sulforaphane (broccoli sprouts) + CAPE (propolis) = dietary mimics of the two itaconate anti-inflammatory mechanisms (KEAP1/Nrf2 + p65 Cys38). The protocol already delivers functional itaconate compensation without knowing this is what it was doing.*
*BHB (ketogenic): additional metabolic benefit — reduces macrophage Warburg shift → less succinate accumulation → less HIF-1α pseudo-stabilization.*
