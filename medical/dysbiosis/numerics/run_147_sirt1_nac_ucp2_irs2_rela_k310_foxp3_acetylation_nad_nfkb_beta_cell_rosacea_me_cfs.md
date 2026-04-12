# run_147 — SIRT1: Nuclear NAD⁺-Dependent Deacetylase, UCP2/IRS-2/RelA-K310 β Cell Protection, NF-κB Brake, FOXP3 Acetylation Dynamics, Rosacea UV/NAD⁺ Axis

## Identity

| Field | Value |
|-------|-------|
| Gene | SIRT1 (chromosome 10q21.3) |
| Protein | Sirtuin 1 (SIR2-like protein 1) |
| Class | Class III HDAC / NAD⁺-dependent protein deacetylase |
| Reaction | Acetyl-lysine + NAD⁺ → deacetylated lysine + nicotinamide + O-acetyl-ADP-ribose (OAADPr) |
| Primary location | Nucleus + cytoplasm (shuttles; primarily nuclear in unstimulated cells) |
| Key substrates | p53-K382, RelA/p65-K310, FOXO3a, PGC-1α, UCP2, IRS-2, FOXP3, H3K9ac, H4K16ac, LKB1 |
| Expression | Ubiquitous; high in β cells, neurons, liver, adipose, T cells |

---

## Structural Distinction from SIRT3 and SIRT6 (run_090)

run_090 covers SIRT3 (mitochondrial; deacetylates SOD2/IDH2/LCAD/acetyl-CoA enzyme) and SIRT6 (nuclear; DNA repair/telomere maintenance/H3K9ac/H3K56ac). SIRT1 is fundamentally different in:

| Feature | SIRT3 (run_090) | SIRT6 (run_090) | SIRT1 (run_147) |
|---------|----------------|----------------|----------------|
| Location | Mitochondrial matrix | Nuclear, chromatin-bound | Nuclear + cytoplasmic (shuttles) |
| Primary substrates | Mitochondrial metabolic enzymes (SOD2, IDH2, LCAD) | H3K9ac, H3K56ac, DNA-PK | p65/RelA-K310, PGC-1α, UCP2, IRS-2, FOXP3, p53 |
| Primary function | Mitochondrial redox balance, metabolic enzymes | DNA repair, telomere length | NF-κB signaling, insulin secretion, Treg function |
| Activators | PGC-1α upstream | SREBPs | Resveratrol, caloric restriction, fisetin, NMN/NR (via NAD⁺) |
| T1DM β cell role | Mitochondrial OXPHOS efficiency | Telomere/genomic stability | UCP2 deacylation → GSIS ↑; NF-κB ↓ |

These are distinct proteins with non-overlapping substrate spectra. SIRT1's dominant disease-relevant functions (NF-κB termination, insulin secretion, Treg FOXP3 dynamics) are not covered by SIRT3/6.

---

## SIRT1 Enzymatic Mechanism

```
Acetyl-lysine on substrate protein
    + NAD⁺ (required cofactor; Km ~50-100 μM)
         ↓ SIRT1 catalytic core (Ross domain; NAD⁺-binding + substrate binding)
    → Deacetylated lysine + nicotinamide + O-acetyl-ADP-ribose (OAADPr)
```

**NAD⁺ dependence:** SIRT1 cannot function without NAD⁺. NAD⁺ is consumed (not regenerated in the same reaction). This creates a direct metabolic-epigenetic coupling: when cellular NAD⁺ is low (fasting, mitochondrial dysfunction, PARP1 activation, aging), SIRT1 activity falls even if SIRT1 protein abundance is unchanged.

**Allosteric regulation:**
- Resveratrol: allosteric activator via SIRT1 N-terminal activation domain (STAC domain)
- Nicotinamide: product inhibitor (competitive with NAD⁺ binding)
- DBC1 (KIAA1967): endogenous inhibitor; binds SIRT1 catalytic domain; blocked by AMPK phosphorylation of DBC1
- AROS: endogenous activator; binds SIRT1 N-terminus

---

## β Cell SIRT1 Functions

### UCP2 Deacetylation → Insulin Secretion Coupling

**UCP2 (uncoupling protein 2)** is a mitochondrial inner membrane protein that allows proton leak → dissipates the proton gradient → reduces ATP synthesis. In β cells:

```
β cell basal state (fasting-like):
UCP2 active → proton uncoupling → ΔΨm partially dissipated → ATP/ADP ratio ↓
→ KATP channels remain open → β cell hyperpolarized → no insulin exocytosis

With SIRT1 activity (fed state, high NAD⁺):
SIRT1 → deacetylates UCP2-K222 → UCP2 ubiquitinated → proteasomal degradation
→ UCP2 protein level ↓ → proton coupling restored → ΔΨm ↑ → ATP/ADP ↑
→ KATP channel closed → membrane depolarized → Ca²⁺ influx → insulin exocytosis ↑

Without SIRT1 (low NAD⁺, SIRT1 inhibited):
UCP2 accumulates → uncoupling → ATP ↓ → KATP open → insulin secretion ↓
```

SIRT1 is thus a positive regulator of glucose-stimulated insulin secretion (GSIS) via UCP2 proteolytic control. β cell SIRT1 knockout mice → ~40% reduction in GSIS.

### IRS-2 Deacetylation → β Cell Survival Signaling

IRS-2 (insulin receptor substrate 2) is the primary PI3K/Akt survival signal in β cells (distinct from IRS-1 which is dominant in muscle/liver):

```
SIRT1 → deacetylates IRS-2-K1173 → IRS-2 interaction with IR/IGF-1R ↑
→ PI3K/Akt activation → FOXO1 nuclear export → β cell survival genes (Pdx1, insulin) maintained
→ mTORC1 ↑ (moderate) → β cell mass maintenance
```

Insulitis cytokines → IRS-2 serine phosphorylation (IRS-1/2 Ser307/Ser612 by JNK) → IRS-2 degradation. SIRT1 counteracts this by maintaining IRS-2 in a deacetylated/active conformation.

### NF-κB/RelA-K310 Deacetylation → Islet Inflammation Termination

```
TNF-α/IL-1β in islets → IKKβ → IκBα phosphorylation → RelA/p65 nuclear translocation
→ RelA-K310 acetylation by p300/CBP → NF-κB transcriptionally active (sustained)

SIRT1 counter-mechanism:
SIRT1 → deacetylates RelA-K310 → RelA transcriptional activity ↓
→ NF-κB target genes (iNOS, IL-6, IL-12, MCP-1) duration limited
→ islet inflammation auto-limited
```

**Distinction from SETD7-RelA-K314/315 (run_145):** SETD7 methylates RelA-K314/315 → proteasomal degradation of chromatin-bound RelA. SIRT1 deacetylates RelA-K310 → transcriptional activity ↓ without degradation. Two non-overlapping residues, two distinct mechanisms for NF-κB termination. Both converge to limit islet NF-κB-driven inflammation.

---

## FOXP3 Acetylation Dynamics — SIRT1 in Tregs

FOXP3 post-translational modification landscape (integrating prior runs):

| Modification | Enzyme | Effect | Run |
|--------------|--------|--------|-----|
| K302 methylation | SETD7 | Blocks GSK-3β → STUB1; stability ↑ | run_145 |
| K302 demethylation | LSD1/KDM1A | Removes protection | run_145 |
| Ser418 phosphorylation | GSK-3β | STUB1 recruitment → degradation | run_114 |
| K31/K263 acetylation | p300/CBP | Stabilizes FOXP3 activity; Treg function ↑ | — |
| K31/K263 deacetylation | **SIRT1** | Reduces acetylation → context-dependent | **run_147** |
| Ubiquitination | STUB1/ITCH | Proteasomal degradation | run_114 |

**The SIRT1/FOXP3 relationship is context-dependent:**
- In activated Tregs (high NAD⁺, high SIRT1 activity): SIRT1 → FOXP3 deacetylation → initially reduces FOXP3 stability BUT activates FOXO1/FOXO3a → Treg identity genes maintained via alternative FOXO pathway
- In inflammatory environments (low NAD⁺, PARP1-depleted): SIRT1 activity ↓ → FOXP3 hyper-acetylated by p300 → paradoxically, this may be protective (acetylated FOXP3 is more stable)
- Key: SIRT1 influences Treg function primarily through FOXO3a (SIRT1 deacetylates FOXO3a → nuclear localization → Treg-supportive gene transcription) rather than direct FOXP3 destabilization

**Practical implication:** In high-inflammation/low-NAD⁺ T1DM islet microenvironment → SIRT1 low → FOXO3a nuclear export impaired → Treg metabolic support genes ↓ → Treg dysfunction even without direct FOXP3 protein degradation. This is a metabolic gate on Treg function distinct from the kinase/methyltransferase gates.

---

## Rosacea — UV/PARP1/NAD⁺/SIRT1 Axis

### UV → PARP1 → NAD⁺ Depletion → SIRT1 Failure → NF-κB

```
UV radiation → DNA strand breaks in keratinocytes
    ↓
PARP1 (poly-ADP-ribose polymerase 1) activation
    ↓
PARP1 consumes NAD⁺ → poly-ADP-ribose synthesis (DNA repair signal)
    ↓
Cellular NAD⁺ pool depleted (PARP1 consumes 100-200 NAD⁺ per DNA break)
    ↓
SIRT1 activity ↓↓ (NAD⁺ substrate depleted)
    ↓
RelA-K310 not deacetylated → NF-κB sustained
    ↓
IL-6, IL-8, MMP-1, CXCL1 → inflammatory keratinocyte state
    ↓
Rosacea flare amplification loop
```

This UV → PARP1 → NAD⁺ → SIRT1 → NF-κB axis explains why UV triggers disproportionate inflammation in rosacea skin — the NAD⁺ pool is more easily depleted (possibly baseline lower in rosacea patients), and SIRT1 fails to terminate the NF-κB response normally.

### SIRT1 Activators in Rosacea Protocol Context

| Compound | SIRT1 Mechanism | Framework Status |
|----------|----------------|-----------------|
| NMN (nicotinamide mononucleotide) | NAD⁺ precursor → SIRT1 cofactor replenishment | New primary SIRT1 indication |
| NR (nicotinamide riboside) | NAD⁺ precursor (via NMNAT2) | New primary SIRT1 indication |
| Resveratrol | Allosteric SIRT1 activator (STAC domain) | Mentioned in framework for other reasons; SIRT1 now primary mechanism |
| Pterostilbene | Dimethyl resveratrol analog, better bioavailability, SIRT1 activator | New addition |
| Fisetin | Flavonoid; SIRT1 activator; also AMPK (existing); also senolytic (run_061) | Multiple mechanism compound |
| Nicotinamide (high dose) | PARADOX: nicotinamide is the SIRT1 reaction product → competitive inhibitor; low-dose niacinamide may be neutral; high-dose → SIRT1 inhibition | Framework alert: niacinamide (run_076) at high dose may reduce SIRT1 activity |

**Niacinamide/SIRT1 paradox (run_076 context):** Niacinamide (nicotinamide) at cosmetic doses (4% topical, 500 mg/day oral) is an NAD⁺ precursor via NAMPT → NMN pathway. But nicotinamide is also the product inhibitor of SIRT1 at >10 mM tissue concentrations. At therapeutic oral doses (500-1000 mg/day), tissue nicotinamide concentrations do not typically reach inhibitory levels. Systemic SIRT1 inhibition by supplemental niacinamide = low probability at standard dosing. Monitor at doses >2g/day.

---

## ME/CFS — NAD⁺ Depletion and SIRT1 Hypofunction

### The ME/CFS NAD⁺ Deficit Hypothesis

ME/CFS = chronic metabolic/mitochondrial dysfunction → multiple NAD⁺ depletion routes:

| Route | Mechanism | NAD⁺ effect |
|-------|-----------|------------|
| Chronic inflammation | PARP1 activation (DNA repair from oxidative stress) | NAD⁺ ↓↓ |
| Mitochondrial dysfunction | Impaired NADH → NAD⁺ regeneration via complex I | NAD⁺/NADH ratio ↓ |
| IDO1 activation (run_091) | Tryptophan → kynurenine → quinolinic acid → NAD⁺ (QPRT) vs. competing toxic metabolites | Net NAD⁺ synthesis ↓ (QPRT saturation) |
| CD38 upregulation | NAD⁺ consuming enzyme; IFN-β → CD38 ↑ in immune cells | NAD⁺ ↓ |

**Result:** SIRT1 activity ↓ → NF-κB (RelA-K310) not deacetylated → neuroinflammation sustained → FOXO3a nuclear export impaired → NK/T cell metabolic adaptation ↓ → fatigue compound.

### NMN/NR Supplementation in ME/CFS — SIRT1 Mechanistic Anchor

NMN (500-1000 mg/day) and NR (300-600 mg/day) are increasingly trialed in ME/CFS for mitochondrial/fatigue benefit. run_147 provides the mechanistic anchor:
- NMN/NR → NAD⁺ ↑ → SIRT1 activity restored → RelA-K310 deacetylated → neuroinflammation ↓
- NAD⁺ → Complex I substrate → OXPHOS efficiency ↑ → ATP ↑ → PEM reduction
- NAD⁺ → SIRT1 → PGC-1α deacetylation → PGC-1α activation → mitochondrial biogenesis → capacity ↑

**Connection to run_146 (PERK/ISR):** eIF2α-P → translation ↓ → NAMPT protein synthesis ↓ → NAD⁺ ↓ → SIRT1 ↓ → NF-κB ↑. Chronic ER stress (run_146) and NAD⁺ depletion (run_147) feed each other: translation attenuation from PERK reduces NAD⁺ biosynthetic enzyme levels, deepening SIRT1 dysfunction.

---

## AMPK/SIRT1 Axis — Metabolic Sensor Coupling

AMPK (run_085/existing framework element) and SIRT1 form a positive feedback loop:

```
Low energy (AMP/ATP ↑)
    ↓
AMPK activated
    ↓
AMPK → phosphorylates DBC1 → DBC1 cannot inhibit SIRT1
    ↓
SIRT1 activity ↑
    ↓
SIRT1 → deacetylates LKB1 → LKB1 active → AMPK activation maintained
    ↓ (positive feedback)
SIRT1 → PGC-1α deacetylation → mitochondrial biogenesis → more ATP → feedback eventually closes
```

This AMPK/SIRT1 circuit means metformin (AMPK activator, run_085) has a SIRT1-mediated component: metformin → AMPK → DBC1 release → SIRT1 ↑ → NF-κB ↓ in islets. Metformin's anti-inflammatory benefit partially operates through the AMPK → SIRT1 → RelA-K310 axis.

---

## Quantitative Parameters

| Parameter | Value | Context |
|-----------|-------|---------|
| SIRT1 Km (NAD⁺) | ~50-100 μM | Depends on substrate |
| SIRT1 Km (acetyl-peptide) | ~1-10 μM | Substrate-dependent |
| NAD⁺ concentration (normal cell) | ~200-500 μM | Tissue-dependent |
| NAD⁺ drop after UV (PARP1) | ~60-80% ↓ | Within 30-60 min in keratinocytes |
| SIRT1 activity threshold (NAD⁺) | Active at >100 μM | Below: activity falls steeply |
| β cell GSIS reduction (SIRT1-KO) | ~40% ↓ | Mouse islet perifusion |
| UCP2 protein level (SIRT1-KO) | ~3-5× ↑ | Protein half-life 2-3 h → accumulates |
| Resveratrol SIRT1 EC50 | ~1-5 μM | Depends on substrate/assay |
| NMN oral bioavailability (mouse) | ~90% | Oral NMN → plasma NAD⁺ in 15 min |
| NMN → NAD⁺ increase | ~2-fold | Metabolomics in blood |

---

## Framework Integration Points

| Prior Run | Connection |
|-----------|-----------|
| run_090 (SIRT3/SIRT6) | Same sirtuin family; orthogonal isoforms — SIRT1 nuclear/cytoplasmic vs SIRT3 mitochondrial vs SIRT6 chromatin |
| run_145 (SETD7/RelA-K314/315) | SIRT1 deacetylates RelA-K310; SETD7 methylates RelA-K314/315 → two orthogonal NF-κB termination mechanisms at adjacent residues |
| run_085 (metformin/AMPK) | Metformin → AMPK → DBC1 phosphorylation → SIRT1 derepression; metformin NF-κB effect partially SIRT1-mediated |
| run_091 (IDO1/kynurenine) | IDO1 → tryptophan → quinolinic acid → potentially NAD⁺ (QPRT); also: IDO1 depletes NAD⁺ precursor; bidirectional |
| run_069 (AMPK/NLRP3) | AMPK ↑ → SIRT1 ↑ → NF-κB ↓ → NLRP3 priming ↓ (Signal 1 suppression) |
| run_076 (niacinamide) | Niacinamide at high dose = SIRT1 product inhibitor; clinical alert for doses >2g/day |
| run_061 (senescence/SASP) | SIRT1 activity ↓ with aging (NAD⁺ depletion, DBC1 ↑) → SASP amplification; fisetin = senolytic (run_061) + SIRT1 activator (run_147) |
| run_146 (PERK/ISR) | eIF2α-P → NAMPT synthesis ↓ → NAD⁺ ↓ → SIRT1 ↓ → NF-κB ↑; ER stress (PERK) and NAD⁺ depletion (SIRT1) form vicious cycle |
| run_114 (GSK-3β/FOXP3) | Both GSK-3β/STUB1 (run_114) and SIRT1/FOXO3a (run_147) regulate Treg metabolic function; parallel Treg stability mechanisms |

---

## Saturation Override Checklist

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| 1. Absent from all prior runs as primary subject | PASS | SIRT1 appears in 37 files as context/mention; no file has SIRT1 as primary subject; run_090 = SIRT3/SIRT6 (different isoforms, different substrates/location) |
| 2. MODERATE+ rosacea + T1DM | PASS | T1DM: UCP2/GSIS ↑, IRS-2 survival, RelA-K310 islet NF-κB ↓, Treg FOXO3a metabolic support; Rosacea: UV/PARP1/NAD⁺ → SIRT1 failure → NF-κB sustained → inflammatory loop |
| 3. New therapeutic/monitoring target | PASS | NMN/NR as primary SIRT1/NAD⁺ supplementation rationale; resveratrol's primary mechanism now SIRT1 (prior mentions in passing); niacinamide SIRT1 paradox monitoring alert; pterostilbene/fisetin additions; AMPK/SIRT1 dual mechanism for metformin |
| 4. Kill-first fails | PASS | run_090 covers mitochondrial SIRT3/SIRT6 (non-overlapping substrates, non-overlapping functions); SIRT1 nuclear/cytoplasmic functions (RelA-K310, UCP2, IRS-2, FOXO3a) = zero coverage in prior runs |

---

*One-hundred-and-fortieth extension | SIRT1 sirtuin-1 NAD+-dependent deacetylase Class-III-HDAC UCP2-K222 GSIS-rescue IRS-2-deacetylation RelA-K310-NF-κB-termination FOXP3-FOXO3a-Treg-metabolic-gate UV-PARP1-NAD+-depletion NF-κB-sustained SIRT1-failure-rosacea NMN-NR-NAD+-supplementation resveratrol-STAC pterostilbene fisetin DBC1-AMPK-SIRT1-circuit metformin-SIRT1-mediated niacinamide-paradox ME/CFS-NAD+-deficit CD38-IDO1-NAD+ run090-SIRT3-SIRT6-orthogonal run145-RelA-K314-adjacent run085-AMPK-SIRT1 run146-PERK-ISR-NAMPT | run_147 | Framework at SATURATION + 36: 147 runs*
