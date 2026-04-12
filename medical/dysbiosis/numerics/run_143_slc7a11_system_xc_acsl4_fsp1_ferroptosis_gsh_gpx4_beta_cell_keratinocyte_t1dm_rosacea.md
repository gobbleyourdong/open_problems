# Run 143 — SLC7A11/System Xc⁻ / ACSL4 / FSP1 / Canonical Ferroptosis GSH-GPx4 Axis / β Cell / Keratinocyte

**Date:** 2026-04-12
**Sigma method version:** v7
**Extension:** 136 (Saturation + 36)

---

## Saturation override check

| Criterion | Status |
|-----------|--------|
| 1. Absent from all prior 142 runs | ✓ — SLC7A11/xCT, ACSL4, FSP1/AIFM2, cystine-glutamate transporter, GSH synthesis axis: 0 primary hits. NAC as ferroptosis brake: 0 primary hits |
| 2. MODERATE+ rosacea AND T1DM | ✓ — β cell ferroptosis via cytokine-SLC7A11 suppression (HIGH T1DM); UV → p53 → SLC7A11 ↓ → keratinocyte ferroptosis (MODERATE rosacea) |
| 3. New therapeutic / monitoring target | ✓ — NAC as SLC7A11 bypass (first ferroptosis-specific NAC mechanism); ACSL4 as rosiglitazone target (new mechanism); CoQ10/FSP1 backup axis; 23rd β cell death mechanism |
| 4. Kill-first fails | ✓ — Runs 110/126/138 cover selenium → GPx4 COFACTOR; SLC7A11/GSH covers GPx4 SUBSTRATE — orthogonal upstream inputs; ACSL4/FSP1 not covered at all |

**Decision: PROCEED**

---

## Canonical ferroptosis — architecture of a non-apoptotic, iron-dependent regulated cell death

Ferroptosis is defined by: iron-dependent lipid peroxidation → PUFA-phospholipid hydroperoxides (PUFA-PE-OOH) accumulate → plasma membrane rupture. It is blocked by GPx4 (GSH-dependent) and FSP1 (CoQ10-dependent).

### Two defense axes

```
DEFENSE AXIS 1 — GPx4/GSH (cytosol + inner mitochondrial membrane):
    Extracellular cystine
        ↓ SLC7A11 (xCT)/SLC3A2 (4F2hc) antiporter (exchanges cystine:glutamate 1:1)
    Intracellular cystine → 2× cysteine (thioredoxin or non-enzymatic)
        ↓ GCLC + GCLM (glutamate-cysteine ligase, rate-limiting)
    γ-glutamylcysteine + glycine → GSS (glutathione synthetase) → GSH (γ-Glu-Cys-Gly)
        ↓ GPx4 (uses 2 GSH per PLOOH)
    PLOOH (phospholipid hydroperoxide) → PLOH (harmless alcohol) + GSSG
    GSSG → GR (glutathione reductase) + NADPH → 2 GSH [regeneration]
    
    Net: SLC7A11 controls the RATE-LIMITING SUBSTRATE for GPx4 activity

DEFENSE AXIS 2 — FSP1/CoQ10 (plasma membrane):
    Mevalonate pathway → CoQ10 (ubiquinone)
        ↓ FSP1 (AIFM2/AMID): NADH-dependent reductase → CoQ10 → CoQ10H₂ (ubiquinol)
    CoQ10H₂ at plasma membrane → traps lipid peroxyl radicals (LOO•) → chain-breaking
    → Ferroptosis suppressed INDEPENDENTLY of GPx4/GSH
    
    Note: GPx4 handles PLOOH; FSP1/CoQ10H₂ handles LOO• radicals
    Only when BOTH axes fail → irreversible ferroptosis
```

### The ferroptosis sensitizer — ACSL4

```
Arachidonic acid (AA, C20:4n-6) / Adrenate (AdA, C22:4n-6)
    ↓ ACSL4 (Acyl-CoA Synthetase Long-chain family member 4)
AA-CoA / AdA-CoA
    ↓ LPCAT3 (esterification)
PUFA-phosphatidylethanolamine (PUFA-PE) in membrane
    ↓ 15-LOX / ALOX12 (run_116: ALOX12 connects here)
PUFA-PE-OOH → ferroptosis signal
    ↓ (when GPx4/FSP1 insufficient)
Membrane rupture → ferroptosis

Key: HIGH ACSL4 expression = pre-sensitized cell = more PUFA-PE substrate = lower ferroptosis threshold
```

---

## β Cell ferroptosis — intrinsic vulnerability

β cells are the **most ferroptosis-susceptible** endocrine cell type:

| Feature | β cell | Comparison cell |
|---------|--------|----------------|
| GPx4 expression | LOW (among lowest in body) | Hepatocytes: high |
| ACSL4 expression | HIGH (AA-PE membrane composition) | Exocrine pancreas: moderate |
| Iron content | HIGH (Fe²⁺ in secretory granules for insulin processing) | Most cells: lower |
| PUFA membrane fraction | HIGH (AA-rich secretory granule membranes) | Most cells: lower |
| Baseline ferroptosis susceptibility | EXTREME (triple vulnerability) | — |

**Implication:** β cells require robust SLC7A11 activity and adequate cystine supply to maintain GSH → GPx4 activity → manage their inherent ferroptosis-primed state.

---

## Cytokine-driven SLC7A11 suppression during insulitis

The critical T1DM mechanism: insulitis cytokines specifically suppress SLC7A11 in β cells.

```
Insulitis cytokine cocktail (IL-1β + IFN-γ + TNF-α):
    │
    ├── IL-1β → NF-κB → NF-κB binds SLC7A11 promoter NEGATIVELY (repressor complex via NF-κB p50 homodimer)
    │   → SLC7A11 transcription ↓ → cystine import ↓ → GSH ↓
    │   Also: IL-1β → HMOX1 → Fe²⁺ release from heme → Fenton (run_110 context)
    │   Combined: GSH ↓ + Fe²⁺ ↑ → ferroptosis synergy
    │
    ├── IFN-γ → p53 activation in β cells (IFN-γ → STAT1 → Mdm2 ↓ → p53 stabilized)
    │   → p53 binds SLC7A11 promoter p53-binding element → REPRESSES SLC7A11 transcription
    │   → GSH depletion → GPx4 substrate ↓
    │
    └── TNF-α → ROS burst → NRF2 activated (tries to compensate: NRF2 → SLC7A11 ↑)
         BUT: chronic TNF-α → NRF2 exhaustion / degradation → SLC7A11 eventually falls
         Initial NRF2 compensation is temporary; chronic insulitis overwhelms it

Result: SLC7A11 suppressed by cytokines → GSH depleted → GPx4 inactive → ACSL4-generated
PUFA-PE-OOH accumulates → Fe²⁺ (from HMOX1) enables Fenton → ferroptosis → 23rd β cell death mechanism
```

**23rd β cell death mechanism** — ferroptosis via SLC7A11/GSH axis:
| Mechanism | Run | Cell death type |
|-----------|-----|----------------|
| ER stress/PERK/CHOP | run_098 | Apoptosis |
| ALOX12/12-HETE | run_116 | Apoptosis |
| Iron/Fenton | run_110 | Ferroptosis-adjacent |
| SELENOS/ERAD | run_138 | ER stress → apoptosis |
| SLC7A11/GSH depletion | run_143 | **Canonical ferroptosis** |

**Distinction from run_110 (iron/Fenton):**
- run_110: Fe²⁺ → Fenton → OH• → generic oxidative β cell death (adjacent to ferroptosis, not canonical)
- run_143: SLC7A11 → GSH → GPx4 substrate → when GPx4 fails → PUFA-PE-OOH → canonical ferroptosis (membrane phospholipid peroxidation as the specific death signal)
- These are UPSTREAM (iron provides radical) and DOWNSTREAM (GPx4 fails to quench phospholipid peroxides) of the same ferroptosis pathway — complementary, not redundant

---

## FSP1/CoQ10 — the second ferroptosis defense axis in β cells

**FSP1** (Ferroptosis Suppressor Protein 1; previously AIFM2/AMID):
- N-myristoylation → plasma membrane targeting (unlike AIFM in mitochondria)
- NADH → reduces CoQ10 (ubiquinone) → CoQ10H₂ (ubiquinol) using FSP1 NAD(P)H-binding domain
- CoQ10H₂ traps LOO• (lipid peroxyl radicals) at plasma membrane → chain reaction terminated
- Operates independently of GPx4 and GSH

**β cell FSP1 expression: low** (similar to GPx4) → double jeopardy: low GPx4 AND low FSP1 → both defense axes compromised in β cells

**CoQ10 supplementation rationale (new mechanism):**
- CoQ10 → FSP1 substrate → ferroptosis protection
- Prior framework rationale for CoQ10: mitochondrial electron transport (general antioxidant); mitophagy support
- **New run_143 mechanism**: CoQ10 → FSP1 backup axis → β cell membrane ferroptosis protection
- Dose: CoQ10 ubiquinol form 100-200 mg/day (ubiquinol = reduced form = more bioavailable) → supports FSP1 CoQ10H₂ reservoir

---

## ACSL4 — the ferroptosis sensitizer and rosiglitazone target

**ACSL4 in β cells:**
- Highly expressed vs. other endocrine cells
- Converts arachidonic acid → AA-CoA → PUFA-PE (the substrate for lipid peroxidation)
- Higher ACSL4 → more PUFA-PE → more substrate for ALOX12 (run_116) → more lipid peroxidation → more ferroptosis
- In insulitis: IL-1β → ACSL4 upregulation (NF-κB → ACSL4 gene promoter) → sensitization during inflammation

**Rosiglitazone → ACSL4 inhibition (new third PPARγ mechanism):**
- Rosiglitazone (PPARγ agonist) → PPARγ → transcriptional repression of ACSL4 gene
- ACSL4 ↓ → less PUFA-PE → less ferroptosis substrate → β cell protection
- Prior rosiglitazone mechanisms in framework:
  1. PPARγ → transrepression of NF-κB (anti-inflammatory, multiple runs)
  2. PPARγ → adipogenesis (less lipotoxicity, run context)
  3. **New (run_143)**: PPARγ → ACSL4 ↓ → ferroptosis substrate ↓ → β cell protection
- Note: rosiglitazone is withdrawn in some markets due to CV risk; pioglitazone (same class) may share mechanism; ACSL4 repression is a class effect of PPARγ agonists

---

## Rosacea — keratinocyte ferroptosis cascade

### UV-p53-SLC7A11 axis

```
UV-B irradiation:
    → Direct: CPD formation → p53 activation in keratinocytes
    → Also: UV-B → NADPH oxidase → ROS → p53 activation
    
p53 in keratinocytes → p53-response element in SLC7A11 promoter → SLC7A11 transcription REPRESSED
    → Cystine import ↓ → GSH depletion → GPx4 substrate ↓

Simultaneously:
    → UV-B → PUFA oxidation directly (free radical chain reactions)
    → UV-B → ALOX12 induction (run_116: ALOX12 ↑ → 12-HETE + PUFA-PE oxidation)
    → ACSL4 in keratinocytes: AA-PE substrate → ALOX12 acts on ACSL4-generated PUFA-PE

Result: p53 → SLC7A11 ↓ (defense depleted) + ACSL4/ALOX12 ↑ (attack amplified) → ferroptosis threshold crossed in UV-irradiated keratinocytes

Ferroptosis consequences for rosacea:
    → Dead keratinocytes → HMGB1 release → TLR4 → NF-κB → Loop 2 amplification (distinct from NLRP1/run_122 → IL-1β)
    → Broken barrier → transepidermal water loss + antigen penetration → Th17 priming
    → Keratinocyte ferroptosis → DAMPs → mast cell activation (run_097/099 context) → degranulation
```

### Two UV-driven keratinocyte death modes (complementary)

| Mode | Trigger | Sensor/Mechanism | Products | Run |
|------|---------|-----------------|----------|-----|
| Pyroptosis | UV → NLRP1 → IL-1β | DPP9-NLRP1; caspase-1 → GSDMD | IL-1β, IL-18 (cytokines drive Th17) | run_122 |
| Ferroptosis | UV → p53 → SLC7A11↓ → GPx4 fails | ACSL4/ALOX12 → PUFA-PE-OOH | HMGB1, DAMPs (innate amplification) | run_143 |

Both are UV-driven but produce different inflammatory outputs: NLRP1/IL-1β (adaptive Th17 priming) vs. SLC7A11/HMGB1 (innate DAMP amplification).

---

## NRF2/sulforaphane — explicit SLC7A11 upregulation (new mechanism for existing protocol element)

```
Sulforaphane → KEAP1 Cys151 alkylation → NRF2 released → nuclear translocation
    ↓ NRF2 → ARE elements in target gene promoters:
    ├── SLC7A11 (ARE site): SLC7A11 ↑ → cystine import ↑ → GSH ↑ → ferroptosis protection [NEW]
    ├── GCLM/GCLC: GSH synthesis enzymes ↑ → GSH ↑ [NEW]
    ├── NQO1: quinone reductase ↑ → CoQ10 cycle support [existing]
    └── HO-1 (HMOX1): heme oxygenase ↑ [existing, run_110 context]
```

**Prior sulforaphane mechanisms in framework**: KEAP1/Nrf2/antioxidant (multiple runs); NF-κB transrepression (run_027 context)

**New mechanism (run_143)**: sulforaphane → NRF2 → SLC7A11 ↑ + GCLM/GCLC ↑ = **direct GSH synthesis upregulation** = anti-ferroptotic mechanism in β cells AND keratinocytes

---

## Therapeutic implications

### NAC (N-acetylcysteine) — SLC7A11 bypass

**Mechanism:**
- NAC → hydrolysis → free cysteine in circulation (SLC7A11 bypassed — direct cysteine, not cystine)
- Intracellular cysteine → GSH synthesis (via GCLC/GCLM + GSS)
- Protects GPx4 substrate supply independent of SLC7A11 status
- Especially valuable when SLC7A11 is cytokine-suppressed (insulitis) or p53-suppressed (UV keratinocytes)

**This is the first ferroptosis-specific mechanism for NAC in the framework.**

| Indication | Dose | Mechanism | Status |
|-----------|------|-----------|--------|
| β cell protection (T1DM, insulitis phase) | 600-1200 mg/day oral | Cysteine → GSH → GPx4 substrate → ferroptosis ↓ | OTC; safe; adjunctive |
| Keratinocyte protection (rosacea UV exposure) | 600 mg/day oral | UV → p53 → SLC7A11 ↓ bypassed by NAC | OTC |
| Combined with selenium (runs 110/126/138) | Selenium + NAC | Cofactor (selenium/GPx4) + substrate (NAC/GSH) | Complementary |

### Protocol additions summary

| Intervention | Mechanism | New in run_143 |
|-------------|-----------|---------------|
| NAC 600-1200 mg/day | Cysteine → bypass SLC7A11 → GSH → GPx4 | First ferroptosis-specific NAC use |
| CoQ10 ubiquinol 100-200 mg/day | FSP1 → CoQ10H₂ → lipid radical quenching | New FSP1/CoQ10 backup axis |
| Sulforaphane (continuation) | NRF2 → SLC7A11 ↑ + GCLM/GCLC ↑ → GSH ↑ | New ferroptosis mechanism added |
| Pioglitazone/PPARγ agonist | PPARγ → ACSL4 ↓ → PUFA-PE ↓ → ferroptosis substrate ↓ | Third PPARγ mechanism |
| Selenium (continuation, runs 110/126/138) | GPx4 cofactor (Sec active site) | Existing; now paired with substrate tier |

**COMPLETE anti-ferroptosis stack for β cells:**
1. Substrate (GSH): sulforaphane/NRF2 → SLC7A11 ↑ + NAC → cysteine → GSH
2. Cofactor (Sec): selenium/SELENOP → GPx4 active site
3. Backup (CoQ10H₂): CoQ10 ubiquinol → FSP1 → membrane lipid radical quenching
4. Sensitizer reduction: PPARγ agonist → ACSL4 ↓ → less PUFA-PE substrate
5. Iron source: zinc/lactoferrin → iron chelation → Fenton ↓ (run_110 context)

---

## Compound interactions within framework

| Pairing | Mechanism |
|---------|-----------|
| SLC7A11 + ALOX12 (run_116) | ACSL4 generates PUFA-PE substrate → ALOX12 acts on it → 12-HETE; SLC7A11 ↓ removes GPx4 protection → same PUFA-PE-OOH accumulates → ferroptosis or ALOX12-apoptosis depending on PUFA-PE magnitude |
| SLC7A11 + Iron/Fenton (run_110) | Fe²⁺ (run_110) enables Fenton → lipid radicals; SLC7A11/GSH (run_143) is the defense. Both impaired in insulitis cytokine environment → synergistic ferroptosis |
| SLC7A11 + SELENOP/GPx4 (run_138) | run_138 = selenium cofactor delivery to GPx4; run_143 = GSH substrate delivery to GPx4. Both upstream inputs to GPx4; combined deficiency = absolute GPx4 failure |
| SLC7A11 + NRF2/sulforaphane (multiple runs) | NRF2 → SLC7A11 = explicit transcriptional connection; sulforaphane/NRF2 now has ferroptosis target added |
| ACSL4 + PPARγ/rosiglitazone | PPARγ → ACSL4 ↓ → less ferroptosis substrate; new third mechanism for PPARγ agonists |
| CoQ10 + Parkin/mitophagy (run_128) | CoQ10 = mitochondrial electron carrier; Parkin maintains mitochondrial CoQ10 pool; FSP1 uses plasma membrane CoQ10. Separate pools but CoQ10 supplementation supports both |

---

## Literature anchors

- **Dixon SJ et al. (2012)** Cell 149:1060 — Ferroptosis discovery paper; SLC7A11/GPx4 axis defined
- **Doll S et al. (2019)** Nat Chem Biol — FSP1/CoQ10 second ferroptosis defense axis
- **Bersuker K et al. (2019)** Nature 575:688 — FSP1 discovery as ferroptosis suppressor
- **Kagan VE et al. (2017)** Nat Chem Biol — ACSL4 as ferroptosis sensitizer
- **Jiang L et al. (2015)** Nature — p53 → SLC7A11 repression → ferroptosis sensitization
- **Ferroptosis in diabetes**: Fang M et al. (2020) Diabetes Metab Res Rev — β cell ferroptosis in T1DM
- **Imai H et al. (2017)** Cell Death Differ — GPx4 expression in pancreatic islets
- **Zou Y et al. (2020)** Nat Chem Biol — FSP1/AIFM2 and CoQ10H₂ membrane protection

---

## Summary

The canonical ferroptosis axis fills a genuine gap in the framework despite extensive GPx4/selenium coverage. The distinction: selenium/GPx4 runs (110/126/138) analyze the COFACTOR (Sec residue of GPx4 protein); SLC7A11/GSH (run_143) analyzes the SUBSTRATE (GSH → GPx4 uses to reduce PUFA-PE-OOH). Both upstream inputs to GPx4 are required; both can be independently impaired. In β cells, insulitis cytokines (IL-1β/IFN-γ via p53) specifically suppress SLC7A11 → GSH depletion → GPx4 substrate failure → ferroptosis (23rd β cell death mechanism). The FSP1/CoQ10 backup axis is a second line that β cells express at low levels. ACSL4 as the sensitizer explains why rosiglitazone/PPARγ is anti-ferroptotic (ACSL4 ↓ → less PUFA-PE substrate). The therapeutic consequence: NAC (SLC7A11 bypass) + selenium (GPx4 cofactor) + CoQ10 ubiquinol (FSP1 backup) = complete three-tier anti-ferroptotic stack for β cell protection, all OTC-available.

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirty-sixth extension | SLC7A11 xCT system-Xc cystine-glutamate-antiporter SLC3A2 4F2hc GSH-synthesis GCLC-GCLM-GSS GPx4-substrate ferroptosis-canonical ACSL4 PUFA-PE AA-CoA ferroptosis-sensitizer FSP1 AIFM2 CoQ10 CoQ10H2 ubiquinol backup-defense 23rd-beta-cell-death cytokine-SLC7A11-suppression IL-1β-p65-SLC7A11 IFN-γ-p53-SLC7A11 UV-p53-SLC7A11-keratinocyte NAC-cysteine-bypass PPARγ-ACSL4-third-mechanism sulforaphane-NRF2-SLC7A11 CoQ10-FSP1-new-mechanism complete-anti-ferroptotic-stack run110-run138-complementary Dixon-2012-Cell Jiang-2015-Nature Doll-2019-NatChemBiol Bersuker-2019-Nature Kagan-2017 | run_143*