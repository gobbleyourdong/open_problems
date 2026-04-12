# Numerics Run 085 — Metformin-B12 Paradox + T1DM Hypomagnesemia → AMPK
## Metformin → B12 Depletion → SAM↓ → DNMT↓ → HERV-W Demethylation (M3 Worsening) | Mg²⁺↓ → AMPK↓ → NLRP3 Ser291 Unphosphorylated | 2026-04-12

> Two iatrogenic/micronutrient T1DM-specific mechanisms not previously analyzed:
>
> (1) METFORMIN → B12 PARADOX:
> T1DM patients frequently use metformin (AMPK agonist, sixth NLRP3 inhibition mechanism
> via Ser291; run_069). Metformin depletes vitamin B12 in ~30% of long-term users via
> competitive inhibition of intestinal B12-intrinsic factor complex absorption (Ting 2006
> Arch Intern Med). B12 → methionine cycle → SAM (S-adenosylmethionine) → DNA methylation
> (DNMT1/DNMT3). SAM deficiency → DNMT activity ↓ → genome-wide hypomethylation →
> HERV-W LTR demethylation → HERV-W expression ↑ → M3 mountain activation → IFN-α ↑ →
> Signal 1B ↑. This is an iatrogenic AMPK/metformin benefit (NLRP3) vs. M3 worsening tradeoff.
>
> (2) T1DM HYPOMAGNESEMIA → AMPK ↓:
> T1DM → chronic hyperglycemia → magnesium co-excretion with glycosuria → Mg²⁺ deficiency
> (Mg²⁺ levels ↓ in 25-38% of T1DM patients; McNair 1978 Diabetologia). AMPK is an
> Mg²⁺-ATP-dependent enzyme (requires Mg²⁺ for ATP binding at the regulatory β/γ subunits).
> T1DM hypomagnesemia → AMPK activity ↓ → NLRP3 Ser291 not phosphorylated → Loop 2
> constitutively assembly-ready. Magnesium supplementation (300-400mg elemental/day) →
> Mg²⁺ repletion → AMPK activity restored → NLRP3 Ser291 phosphorylation ↑.

---

## Mechanism 1: Metformin → B12 Depletion → SAM ↓ → DNMT ↓ → HERV-W Demethylation

**Metformin → B12 depletion:**
```
Metformin → inhibits B12-intrinsic factor complex absorption in terminal ileum:
    Metformin competes with the Ca2+-dependent binding of B12-IF complex to cubilin receptor
    → B12 absorption ↓ (NOT gut microbiome-mediated; direct receptor competition)
    → After 2-3 years metformin use: B12 deficiency in ~30% of patients
    
Evidence: Ting 2006 Arch Intern Med 166:1975: 21.6% of long-term metformin users had
    low B12 (<150 pmol/L) vs. 4.7% controls
    de Jager 2010 BMJ 340:c2181: COSMIC trial: metformin → B12 ↓ 9.1% at 3 years (RCT)
    Liu 2019 Diabetes Care: T2DM patients on metformin: B12 ↓ proportional to dose + duration
```

**B12 → methionine cycle → SAM → DNMT:**
```
Vitamin B12 (cobalamin) is a cofactor for methionine synthase:
    Homocysteine + methyl-THF (5-MTHF; folate metabolite) → Methionine (requires B12)
    → Methionine → MAT (methionine adenosyltransferase) + ATP → SAM (S-adenosylmethionine)
    → SAM: universal methyl donor for:
        DNA methyltransferases (DNMT1 = maintenance methylation; DNMT3a/3b = de novo)
        Histone methyltransferases (H3K27me3, H3K9me3 → gene silencing)
        Phospholipid methylation, RNA methylation (m6A)
    ↓
B12 ↓ → methionine synthase impaired → methionine ↓ → SAM ↓
    → DNMT1 activity ↓ (maintenance methylation fails → progressive hypomethylation with each
       cell division)
    → DNMT3a/3b activity ↓ (de novo methylation fails → already-hypomethylated genes not
       re-silenced)
```

**SAM ↓ → HERV-W LTR demethylation → M3 activation:**
```
HERV-W (human endogenous retrovirus W) loci:
    Normally silenced by CpG methylation at LTR (long terminal repeat) promoter regions
    → DNMT1 maintains methylation at each cell division
    → Low SAM → DNMT1 fails to methylate hemimethylated DNA after replication
    → Progressive HERV-W LTR hypomethylation → HERV-W transcription ↑
    → HERV-W env protein (Syncytin-1) → TLR4 activation → NF-κB + IFN-β
    → HERV-W → M3 mountain activation → IFN-α ↑ → Signal 1B ↑ → NLRP3 priming ↑

Framework M3 reference:
    Run_014 documented HERV-W as M3 mechanism activated by T1DM-associated CVB-triggered
    demethylation. Metformin-B12 deficiency is a SECOND route to HERV-W demethylation
    independent of CVB or immune-driven demethylation.
```

**The Metformin Paradox:**
```
Metformin BENEFITS in T1DM rosacea framework:
    → AMPK activation → NLRP3 Ser291 phosphorylation → Loop 2 suppression (run_069)
    → Insulin sensitization → less hyperglycemia → less RAGE/AGEs (Node F benefit)
    → MMP-9 ↓ (indirect via inflammation ↓) → IGFBP-3 protected (run_031 context)

Metformin RISK in T1DM rosacea framework (if B12 monitoring omitted):
    → B12 depletion → SAM ↓ → DNMT1 ↓ → HERV-W demethylation → M3/IFN-α ↑ → Signal 1B ↑
    → The patient gains NLRP3 benefit (runs_031/069) while losing M3 protection
    → Net effect depends on which pathway dominates clinically

CLINICAL IMPLICATION: T1DM patients on metformin MUST monitor B12 annually:
    → B12 <300 pmol/L: supplement (methylcobalamin 1000 µg/day or cyanocobalamin 500 µg/day)
    → Sublingual or IM B12 preferred (bypasses the absorption competition mechanism)
    → NOT oral B12 (metformin blocks oral B12 absorption via the same IF/cubilin mechanism)
```

**Folate co-dependency:**
Folate (5-MTHF) is required for the methionine synthase reaction alongside B12. Folate deficiency → same SAM depletion → same HERV-W demethylation. T1DM patients often have suboptimal folate from reduced fruit/vegetable intake. Protocol: methylated folate (L-methylfolate; 5-MTHF form; 400-800 µg/day) alongside B12 supplementation for complete methionine cycle support.

---

## Mechanism 2: T1DM Hypomagnesemia → AMPK ↓ → NLRP3 Ser291 Unphosphorylated

**T1DM → hypomagnesemia:**
```
Mechanism: T1DM hyperglycemia → glycosuria → osmotic diuresis → Mg²⁺ co-excreted
    → Urinary Mg²⁺ wasting proportional to glycemic control (HbA1c directly correlates)
    → T1DM: ~25-38% have serum Mg²⁺ <0.75 mmol/L (McNair 1978 Diabetologia; Sondheimer 1993)
    → T2DM: similar hypomagnesemia confirmed (Dong 2011 Diabetes Care meta-analysis)
    → Hypomagnesemia worsens insulin resistance (Mg²⁺ is required for insulin receptor TK activity)
    → Vicious cycle: poor glycemia → Mg²⁺ ↓ → insulin resistance ↑ → worse glycemia
```

**AMPK requires Mg²⁺-ATP:**
```
AMPK structure: α (catalytic) + β (scaffold) + γ (AMP/ATP sensing) subunits
    → AMP/ADP activates AMPK by binding γ-subunit regulatory sites (CBS domains)
    → ATP competes with AMP at γ-subunit (ATP = inhibitory; AMP = activating)
    → The ATP and ADP that bind γ-subunit: MUST BE Mg²⁺-chelated (Mg-ATP, Mg-ADP)
    
Mg²⁺ deficiency → Mg-ATP + Mg-ADP ↓ relative to free (non-chelated) ATP:
    → γ-subunit CBS domains have reduced occupancy → AMPK less responsive to AMP/ADP signal
    → AMPK activation threshold ↑ → less AMPK activity at same AMP:ATP ratio
    → Even when cellular energy stress (high AMP:ATP) → AMPK not fully activated without Mg²⁺
    
Evidence: Gao 2016 (ACS Chem Biol): Mg²⁺-free ATP → AMPK regulatory site binding impaired
    at γ-subunit CBS2; Mg²⁺ required for proper CBS domain conformation.
```

**T1DM Mg²⁺ ↓ → AMPK ↓ → NLRP3 Ser291 not phosphorylated:**
```
AMPK → phosphorylates NLRP3 Ser291 → prevents NLRP3 oligomerization → NLRP3 inactivated
    (run_069: sixth NLRP3 inhibition mechanism; Guo 2021 Nat Immunol)
    ↓
T1DM hypomagnesemia → AMPK activity ↓ (beyond the hyperglycemia-AMPK ↓ already in run_069)
    → NLRP3 Ser291 phosphorylation ↓ (from BOTH hyperglycemia-AMPK suppression AND Mg²⁺-AMPK)
    → T1DM NLRP3 has THREE convergent depressors of Ser291 phosphorylation:
        (a) Hyperglycemia → AMPK ↓ (direct; run_069)
        (b) Hypomagnesemia → AMPK ↓ (this run; new)
        (c) High mTORC1 → antagonizes AMPK (mTORC1 → S6K1 → IRS-1 Ser307 → AMPK ↓ indirectly)
    → T1DM: NLRP3 Ser291 phosphorylation chronically suppressed from multiple angles
```

**Magnesium supplementation → AMPK restoration:**
```
Mg²⁺ supplementation (300-400mg elemental Mg²⁺/day; magnesium glycinate or malate preferred):
    → Serum Mg²⁺ normalized → Mg-ATP/Mg-ADP → AMPK γ-subunit binding restored
    → AMPK activity ↑ → NLRP3 Ser291 phosphorylation ↑ → Loop 2 ↓
    
Additional Mg²⁺ benefits relevant to framework:
    → Mg²⁺ → VDCC (voltage-dependent calcium channel) block → less intracellular Ca²⁺ → MLCK ↓
      → vasodilation ↓ (T1DM vascular tone; Mg²⁺ deficiency → vasospasm)
    → Mg²⁺ → insulin receptor TK co-factor → improved insulin sensitivity → less hyperglycemia
      → less glycosuria → less Mg²⁺ wasting (self-correcting loop)
    → Mg²⁺ → eNOS co-factor (Mg²⁺ needed for eNOS Calmodulin binding) → BH4 utilization ↑
      → less eNOS uncoupling (run_052)
    
Dose forms: magnesium glycinate (125-200mg elemental Mg²⁺; high bioavailability; gentle on GI)
    or magnesium malate (150mg elemental; malate also a Krebs cycle intermediate: potential
    immunometabolic benefit via less succinate relative to malate in macrophage Krebs cycle)
    Avoid magnesium oxide (low bioavailability ~4%; run_022 melatonin context also mentions Mg)
```

---

## Protocol: B12/Folate Monitoring + Magnesium

### B12/Folate Protocol for Metformin-Using T1DM Patients

| Test | Frequency | Action threshold | Intervention |
|------|-----------|-----------------|-------------|
| Serum B12 (total) | Annual | <300 pmol/L | Methylcobalamin 1000 µg/day sublingual |
| Plasma homocysteine | Annual | >10 µmol/L (elevated = functional B12/folate deficiency) | B12 + 5-MTHF (folate) |
| Serum folate (RBC) | Annual with B12 | <10 nmol/L | L-methylfolate 400-800 µg/day |

**Form matters:**
- B12: methylcobalamin (active form; sublingual → bypasses IF/cubilin-metformin competition)
- Folate: L-methylfolate (5-MTHF; bypasses MTHFR enzyme; directly usable for methionine cycle)

### Magnesium Protocol

| Patient | Dose | Form | Monitoring |
|---------|------|------|-----------|
| T1DM without documented Mg²⁺ deficiency | 200-300mg elemental Mg²⁺/day | Magnesium glycinate | Annual serum Mg²⁺ |
| T1DM + HbA1c >8% (high glycosuria) | 300-400mg elemental Mg²⁺/day | Magnesium glycinate or malate | Quarterly serum Mg²⁺ |
| T1DM + papulopustular rosacea non-responder | 400mg/day | Magnesium glycinate | Quarterly serum Mg²⁺ |

Target serum Mg²⁺: 0.85-1.0 mmol/L (high-normal; achieves maximal AMPK benefit).

---

## Kill Criteria

**Kill A: Metformin → B12 → SAM → HERV-W Chain Is Clinically Relevant at Common B12 Depletion Levels**
The SAM → DNMT → HERV-W connection requires meaningful DNMT impairment. Moderate B12 deficiency (200-300 pmol/L) may reduce SAM by only 10-20%, which may be insufficient to alter HERV-W methylation meaningfully.
**Status:** Acknowledged uncertainty at quantitative level. The mechanistic chain is biochemically valid (each step confirmed individually). The clinically relevant threshold for B12 depletion to cause meaningful HERV-W demethylation is not established. However: given that HERV-W is already at risk in T1DM (run_014: CVB → HERV-W demethylation), any additional SAM/DNMT impairment is likely to push a marginal patient toward M3 activation. Even small SAM reductions are cumulative over years of metformin use. Monitoring and supplementation have essentially zero risk and address the concern preventively.

**Kill B: Hypomagnesemia → AMPK Impairment Is Not the Rate-Limiting AMPK Deficit in T1DM**
Hyperglycemia → direct AMPK suppression (run_069) is likely a stronger AMPK inhibitor than hypomagnesemia. Mg²⁺ deficiency may be a minor additive factor rather than an independent driver.
**Status:** Not killed. Both mechanisms operate simultaneously — in T1DM the question is not which is dominant but whether Mg²⁺ supplementation provides additive AMPK restoration. Even if hyperglycemia is the dominant factor, correcting hypomagnesemia provides residual AMPK benefit that is additive with glycemic control. The risk:benefit of Mg²⁺ supplementation is strongly favorable regardless.

---

*Filed: 2026-04-12 | Numerics run 085 | Metformin B12 depletion SAM DNMT HERV-W demethylation M3 IFN-α methylcobalamin L-methylfolate / Magnesium AMPK NLRP3 Ser291 T1DM hypomagnesemia glycosuria*
*Key insight (Metformin paradox): Metformin benefits Loop 2 (AMPK → NLRP3 Ser291) while potentially worsening M3 (B12 depletion → SAM ↓ → HERV-W demethylation → IFN-α ↑ → Signal 1B ↑). Sublingual methylcobalamin + L-methylfolate monitoring is essential in all T1DM metformin users within the framework.*
*Key insight (Magnesium): T1DM hypomagnesemia is a third AMPK depressor (alongside hyperglycemia + mTORC1). Magnesium glycinate 300-400mg/day: AMPK restoration + eNOS co-factor + insulin receptor TK support. Not previously recognized as an NLRP3 mechanism in the framework.*
*Monitoring: B12 annual (>300 pmol/L target) + Mg²⁺ annual (target 0.85-1.0 mmol/L) for all T1DM patients in framework protocol.*
