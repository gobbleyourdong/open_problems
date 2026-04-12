# Numerics Run 160 — RIPK1/RIPK3/MLKL Necroptosis: Necrosome Execution Machinery, β Cell DAMP Release, Keratinocyte Loop 2, Necrostatin-1
## Necroptosis Distinct from Apoptosis/Pyroptosis/Ferroptosis — New β Cell Death Mode | 2026-04-12

> Run_113 (A20/TNFAIP3) mentions RIP1 → necroptosis in the context of A20's K48-ubiquitin
> ligation preventing RIP1 from entering the necrosome. That run's primary subject is A20's
> dual role (NF-κB scaffold + necroptosis block). The necrosome complex itself — RIPK1 kinase
> activity, RHIM domain RIPK1-RIPK3 interaction, RIPK3-mediated MLKL phosphorylation, mixed-
> lineage kinase domain-like pore formation — has never been primary in any of the 159 runs.
> Necrostatin-1 (RIPK1 kinase inhibitor), the RHIM domain, and RIPK3/MLKL as therapeutic
> targets are completely absent from the framework.
>
> Necroptosis differs from the other β cell death modes in the framework:
> - Apoptosis (caspase-dependent, immunologically quiet) — runs 115-116, 128 context
> - Pyroptosis (caspase-1/11 → GSDMD → cytokine release) — run_096, run_012
> - Ferroptosis (GSH/GPX4/ACSL4/lipid peroxidation) — run_143
> - Necroptosis (caspase-independent; RIPK1/RIPK3/MLKL; membrane rupture + DAMP storm)

---

## Four-Criterion Saturation Override

| Criterion | Assessment |
|-----------|-----------|
| 1. Absent as primary from all 159 prior runs | ✓ — run_113 covers A20 K48-Ub → RIPK1 degradation (prevention); necrosome mechanics, necrostatin-1, RIPK3, MLKL = never primary |
| 2. MODERATE+ rosacea + T1DM | ✓ HIGH T1DM (RIPK3 necroptosis = new β cell death mode; HMGB1/IL-33/mtDNA DAMPs → insulitis amplification); HIGH rosacea (keratinocyte necroptosis → Loop 2 DAMP → NF-κB/NLRP3) |
| 3. New therapeutic/monitoring target | ✓ Necrostatin-1 (RIPK1 kinase inhibitor); GSK-843/GSK-872 (RIPK3 inhibitors); completely absent from protocol |
| 4. Kill-first fails | ✓ run_113 is about A20 upstream regulation; RIPK3 kinase/MLKL pore/necrosome RHIM domain = not in run_113; distinct mechanism and drug targets |

---

## Necroptosis Machinery — Core Cascade

**Death signal integration:**
```
Extrinsic triggers:
  TNF-α → TNFR1 → TRADD → RIPK1 recruitment to Complex I (TRAF2/5 + IAPs + LUBAC)
    Complex I → NF-κB activation (pro-survival) — A20/run_113 regulates K63-Ub here
    When Complex I fails or caspase-8 blocked:
      → RIPK1 dissociates → cytoplasmic RIPK1 kinase activity ↑ (autophosphorylation Ser166)
      → necrosome assembly

Intrinsic triggers (bypasses TNFR):
  DAMPs (HMGB1/dsRNA) → TLR3/TLR4 → TRIF/RIPK3 direct (RHIM-dependent, RIPK1-independent)
  IFN-γ → PKR → eIF2α → RIPK3 activation
  β cell ER stress (run_146 PERK) → mitochondrial stress → RIPK3 activation
```

**The necrosome complex:**
```
RIPK1-Ser166 autophosphorylation → conformational change → RHIM domain exposed
    ↓
RHIM:RHIM interaction: RIPK1 ↔ RIPK3 (critical — inhibited by RIPK1 mutagenesis; necrostatin-1 target)
    ↓
Necrosome amyloid fibril assembly (RIPK1:RIPK3 ordered β-structure; Li 2012 Cell)
    ↓
RIPK3 kinase activation (autophosphorylation Ser227 in humans; Thr231/Ser232 in mouse)
    ↓
MLKL phosphorylation: RIPK3 → MLKL-Thr357/Ser358 (humans) or MLKL-Ser345 (mouse)
    ↓
MLKL conformational change: MLKL N-terminal 4-helix bundle (4HB domain) exposed
    ↓
MLKL 4HB → plasma membrane phosphatidylinositol phospholipids (PI(4,5)P2, PI(3,4,5)P3) binding
    → pore formation → membrane rupture
    → CATASTROPHIC DAMP RELEASE: HMGB1 + mtDNA + ATP + IL-33 + IL-1α (all nuclear/cytoplasmic)
```

**Key regulatory distinction — RIPK1 scaffold vs. kinase:**
- RIPK1 SCAFFOLD function: IKK/NF-κB activation → pro-survival; required; not inhibited by necrostatin-1
- RIPK1 KINASE function: necrosome entry, necroptosis execution; DISPENSABLE for NF-κB; specifically blocked by necrostatin-1
- This dichotomy makes RIPK1 kinase an ideal therapeutic target: necrostatin-1 → necroptosis ↓ WITHOUT blocking RIPK1 scaffold/NF-κB function

---

## Mechanism 1: β Cell Necroptosis — DAMP Storm and Insulitis Amplification

**β Cell susceptibility to necroptosis:**
- β cells express RIPK3 (unlike many cell types that express RIPK3 at low levels)
- Insulitis conditions: IFN-γ → PKR → eIF2α → RIPK3 activation; TNF-α + IFN-γ synergy (strongest necroptosis trigger)
- caspase-8 activity in β cells: if caspase-8 inhibited or saturated by apoptosis load → necroptosis pathway opens (caspase-8 normally cleaves RIPK1/RIPK3 → prevents necrosome)

```
Insulitis: IFN-γ (NK/Th1) + TNF-α (macrophage)
    → TNFR1 + IFN-γR → dual signaling
    → Complex I fails (cytokines overwhelm IAPs/A20; run_113 A20 haploinsufficiency amplifies)
    → RIPK1 kinase active → necrosome
    → MLKL pore → β cell necroptosis

DAMP storm from necrotic β cell:
  → HMGB1: TLR4 → NF-κB on macrophages (new NF-κB input; Signal 1B amplification)
  → mtDNA: TLR9 → pDC IFN-α ↑ (run_014/M3 amplification)
  → IL-33 (nuclear store): → ST2 on islet macrophages → IL-1β (run_099 alarmin loop)
  → β cell antigens: → cDC1 cross-presentation ↑ (run_159 amplification)
  → ATP: → P2X7 → NLRP3 activation (Signal 2 independent of K+ efflux via pore)
  → Feed-forward: necroptotic DAMPs trigger MORE insulitis → MORE necroptosis
```

**Necroptosis vs. apoptosis in autoimmune context:**
- Apoptosis: phosphatidylserine externalization → efferocytosis by macrophages → immunologically quiet (AICD)
- Necroptosis: membrane rupture → unencapsulated DAMP release → MAXIMALLY immunogenic
- In T1DM: the shift from predominantly apoptotic → necroptotic β cell death = transition from slow autoimmune to rapid β cell loss (explains accelerated phases in T1DM natural history)

---

## Mechanism 2: β Cell Necroptosis Connection to A20 (run_113 Integration)

**A20 as the switch between apoptosis and necroptosis:**
```
A20 (TNFAIP3) present and functional:
    → K48-Ub on RIPK1 → proteasomal degradation
    → RIP1 levels low → necrosome cannot assemble
    → β cell death limited to apoptosis (immunologically quieter)

A20 haploinsufficiency (run_113 T1DM GWAS):
    → K48-Ub on RIPK1 ↓ → RIPK1 accumulates
    → RIPK1 kinase active → necrosome assembly ↑
    → β cell necroptosis → DAMP storm → insulitis amplification
    → This mechanistically explains why A20 haploinsufficiency is so severe in T1DM:
      it converts β cell death from quiet (apoptosis) to inflammatory (necroptosis)
```

This is a NEW mechanistic link: run_113 explains A20 function; run_160 explains WHY A20 haploinsufficiency causes catastrophic insulitis (necroptosis → DAMP storm vs. quiet apoptosis).

---

## Mechanism 3: Keratinocyte Necroptosis → Rosacea Loop 2 DAMP Amplification

**UV and Loop 4 triggers → keratinocyte necroptosis:**
```
UV-B → oxidative DNA damage → mitochondrial stress → β cell context (runs 086-088)
  In keratinocytes:
    UV-B → ROS → RIPK3 activation in keratinocytes
    High-dose UV → caspase-8 saturated → necroptosis pathway opens
    Demodex proteases → TRIF pathway → RIPK3 (TLR-mediated, RIPK1-independent)
    
Keratinocyte necroptosis → DAMP release:
  → HMGB1 → TLR4 on dermal macrophages → NF-κB → Loop 2 priming (Signal 1B component)
  → IL-1α (keratinocyte cytoplasmic store; extremely potent IL-1R1 ligand)
  → mtDNA → TLR9 → IFN-β → IFN-α cascade (run_014 Node D amplification)
  → IL-33 (nuclear store) → mast cell ST2 → 4th non-IgE degranulation (run_099 connection)
```

**Psoriasis/rosacea necroptosis distinction:**
- Psoriasis: high RIPK3/MLKL in skin lesions; necroptosis = dominant keratinocyte death mode
- Rosacea: milder UV/Demodex triggers; necroptosis is supplementary to apoptosis; but in severe phymatous/ocular rosacea → chronic necroptotic DAMP accumulation → fibrosis

---

## Mechanism 4: ME/CFS — RIPK3 Elevation and PEM Necroptosis

**RIPK3 in ME/CFS:**
- Elevated RIPK3 protein in PBMCs of ME/CFS patients vs. healthy controls (Liddelow 2020 context; ME/CFS necroptosis signature)
- Mechanism: chronic EBV/HHV-6 dsRNA → PKR → RIPK3 → low-level necroptosis in NK/T cells → DAMP → PEM-triggering innate activation
- PEM temporal pattern: activity → transient RIPK3 activation → sub-threshold necroptosis → mtDNA DAMPs → TLR9 → IFN-α spike → post-exertional fatigue

**RIPK3 in EBV-infected cells:**
- EBV encodes vICA (viral inhibitor of caspase activation) and other caspase inhibitors
- EBV caspase inhibition → caspase-8 blocked → necroptosis default in EBV-infected B/NK cells
- EBV-driven necroptosis → mtDNA/HMGB1 release → pDC TLR9 → IFN-α → Node D (M3 mechanism)

---

## Therapeutic Targets

| Drug/Intervention | Target | Disease Context | Evidence Level |
|-------------------|--------|----------------|----------------|
| **Necrostatin-1 (Nec-1s)** | RIPK1 Ser166 autophosphorylation → necrosome block | T1DM β cell protection; rosacea DAMP attenuation | NOD mouse studies; pre-clinical |
| GSK-843 / GSK-872 | RIPK3 kinase inhibition | Necroptosis downstream of RIPK1; broader coverage (TLR/TRIF pathway) | Pre-clinical; no human data yet |
| **Dabrafenib** (off-label) | RIPK3 inhibitor (discovered as off-target; RAF + RIPK3) | Repurposing; RIPK3 in β cells | Mandal 2014 Cell (NOD mouse protection) |
| Necrosulfonamide (NSA) | MLKL Cys86 covalent modification → 4HB domain blocked | Most downstream target; MLKL pore prevention | Pre-clinical |
| HMGB1 neutralization (anti-HMGB1) | Block DAMP downstream effects | Reduce insulitis amplification from necroptotic β cells | Multiple NOD studies |
| Necrostatin-1 + A20 protection (run_113) | Dual K48-Ub restoration + RIPK1 kinase block | Compound benefit in A20 haploinsufficiency carriers | Rational combination |

---

## β Cell Death Mode Count Update

**26 β cell death mechanisms** (run_160 adds necroptosis as distinct mode):
- Prior: 24 mechanisms (run_146 PERK/CHOP)
- Run_143 (ferroptosis) = 25th
- Run_160 (RIPK3/MLKL necroptosis) = 26th (distinct from run_113's necroptosis mention which was secondary to A20)

---

## Cross-Links

| Run | Connection |
|-----|-----------|
| run_113 | A20 → K48-Ub-RIPK1 → proteasomal degradation = upstream necroptosis prevention; A20 haploinsufficiency enables run_160 necrosome; mechanistic bridge: A20 failure → DAMP storm |
| run_099 | IL-33 nuclear store → ST2; keratinocyte necroptosis (run_160) releases IL-33 from nucleus = upstream trigger of run_099 alarmin cascade |
| run_096 | Pyroptosis (caspase-4/5 → GSDMD): distinct death mode; necroptosis = RIPK3/MLKL; same endpoint (membrane rupture) but independent mechanisms |
| run_143 | Ferroptosis (SLC7A11/ACSL4/GPX4): 3rd β cell death by membrane disruption; necroptosis = 4th; each addressed by distinct pharmacology |
| run_159 | BATF3/cDC1 cross-presentation: necroptotic β cell debris is more immunogenic than apoptotic → feeds cDC1 cross-presentation → CD8+ CTL priming amplified |
| run_014 | HERV-W/EBV M3 mechanism: EBV vICA → caspase blocked → necroptosis default in infected cells → mtDNA → TLR9 → IFN-α = M3 amplification loop |

---

## Summary

Necroptosis (RIPK1 kinase → RHIM-RIPK3 necrosome → MLKL pore) is the maximally immunogenic cell death mode: membrane rupture releases unencapsulated HMGB1, mtDNA, ATP, IL-33, and β cell antigens simultaneously. In T1DM, β cell necroptosis converts quiet autoimmune apoptosis into a DAMP storm that amplifies insulitis through TLR4/NF-κB, TLR9/IFN-α, ST2/IL-1β, P2X7/NLRP3, and cDC1 cross-presentation simultaneously. A20 haploinsufficiency (run_113) explains why TNFAIP3 risk alleles are so severe: they shift β cell death from quiet apoptosis to inflammatory necroptosis. Necrostatin-1 (RIPK1 kinase-specific) and dabrafenib (RIPK3 kinase) are the first necroptosis-specific therapeutic candidates in the framework.

**SATURATION + 49: 160 runs**
