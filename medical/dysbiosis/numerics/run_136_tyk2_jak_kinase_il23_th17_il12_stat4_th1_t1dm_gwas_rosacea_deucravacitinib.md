# Run 136 — TYK2: Pseudokinase Allosteric Regulation, IL-12R/IL-23R Axis, Th1/Th17, T1DM GWAS rs34536443, Rosacea Th17 Subtype

**Date:** 2026-04-12
**Framework position:** TYK2 mentioned 8× in prior runs ONLY as "JAK1/TYK2 pair at IFNAR" notation — never as primary subject. The TYK2 IL-12R/IL-23R arm (STAT4 → Th1; Th17 maintenance), the P1104A pseudokinase regulatory mechanism, and deucravacitinib (TYK2-specific allosteric inhibitor) are completely absent. TYK2 rs34536443 = one of the most widely protective autoimmune GWAS variants (T1DM, RA, SLE, MS, IBD). First TYK2-specific run.
**Saturation criteria:** (1) TYK2 as primary subject, rs34536443 P1104A, deucravacitinib absent from all 135 prior runs ✓ (2) T1DM HIGH (rs34536443 protective across T1DM + RA + SLE + MS + IBD; TYK2 → STAT4 → Th1 in islet autoimmunity) + rosacea HIGH (IL-23 → Th17 maintenance → rosacea papulopustular subtype; deucravacitinib for psoriasis = direct rosacea Th17 analog) ✓ (3) New: TYK2 pseudokinase allosteric regulation (P1104A mimicked by deucravacitinib); IL-12R/IL-23R TYK2 arm distinct from IFNAR; STAT4 → Th1 pathway not previously analyzed; 12th T1DM genetic stratification point; deucravacitinib as first TYK2-specific inhibitor in framework ✓ (4) Kill-first fails: JAK1/2 inhibitors (baricitinib, run_133 context) are pan-JAK; TYK2-specific allosteric mechanism and IL-23 axis are distinct from IFNAR JAK1/TYK2 notation in prior runs ✓

---

## 1. TYK2 Molecular Architecture

**TYK2 (Tyrosine kinase 2):** 134 kDa; JAK family member; gene at 19p13.2. Unlike JAK1/2/3, TYK2 has a functional pseudokinase (JH2) domain that allosterically regulates the kinase (JH1) domain — the structural basis for TYK2-specific drug design.

**JAK family members and receptor pairings:**
| JAK | Receptor partners | Key outputs |
|-----|------------------|-------------|
| JAK1 | IFNAR2, IL-2R, IL-4R, gp130 | STAT1/2 (IFN), STAT5 (IL-2), STAT6 (IL-4) |
| JAK2 | EpoR, GHR, IL-12Rβ2, IL-23R | STAT5 (Epo/GH), STAT4 (IL-12), STAT3 (IL-23) |
| JAK3 | γc chain (IL-2/4/7/9/15/21R) | STAT5 (lymphocyte development) |
| **TYK2** | **IFNAR1, IL-12Rβ1, IL-10Rβ** | **STAT1/2 (IFN), STAT4 (IL-12), STAT3 (IL-10/IL-23)** |

**Key TYK2 receptor pairings:**
```
IFNAR1/IFNAR2:
    TYK2 (IFNAR1) + JAK1 (IFNAR2) → STAT1/STAT2 → ISGF3 → ISGs
    [covered extensively: runs 006/040/063/130/133]

IL-12R (IL-12Rβ1/IL-12Rβ2):
    TYK2 (IL-12Rβ1) + JAK2 (IL-12Rβ2) → STAT4 → T-bet → Th1 differentiation
    [NOT previously analyzed]

IL-23R (IL-12Rβ1/IL-23R):
    TYK2 (IL-12Rβ1) + JAK2 (IL-23R) → STAT3/STAT4 → RORγt maintenance → Th17 persistence
    [NOT previously analyzed]

IL-10R (IL-10Rα/IL-10Rβ):
    JAK1 (IL-10Rα) + TYK2 (IL-10Rβ) → STAT3 anti-inflammatory
    [mentioned in run_080 context]
```

---

## 2. TYK2 Pseudokinase Domain and P1104A Protective Variant

**Pseudokinase (JH2) allosteric regulation:**
- TYK2 JH2 (pseudokinase) domain binds nucleotide → conformationally locks JH1 (kinase) in low-activity state
- When cytokine binds receptor → JH2 conformational change → releases JH1 lock → kinase active
- JH2 is therefore a NEGATIVE REGULATORY domain — provides intrinsic autoinhibition until cytokine activates

**P1104A variant (rs34536443):**
- Proline 1104 → Alanine in the JH2 pseudokinase domain
- Effect: enhanced autoinhibition → TYK2 JH1 stays more locked → reduced enzymatic activity under cytokine stimulation
- Consequence: LESS signaling from IL-12R and IL-23R → less STAT4 → less Th1; less RORγt maintenance → less Th17
- Selectivity: P1104A preferentially reduces TYK2 function at IL-12R/IL-23R arms relative to IFNAR arm (IFN signaling relatively preserved = why this variant doesn't cause severe viral susceptibility like complete TYK2 loss-of-function)
- Population frequency: ~5-7% European; heterozygote benefit; homozygous rare

**GWAS breadth (rs34536443):**
| Disease | Effect direction | Approx. OR |
|---------|-----------------|-----------|
| **T1DM** | **Protective** | **0.63-0.72** |
| RA | Protective | 0.70 |
| SLE | Protective | 0.68 |
| MS | Protective | 0.73 |
| IBD | Protective | 0.77 |
| Psoriasis | Protective (anti-IL-23) | 0.75 |
| Atopic dermatitis | Protective | 0.80 |

This is one of the most BROADLY protective GWAS variants across autoimmune/inflammatory diseases — confirms TYK2-IL-12/IL-23 axis as a central hub in autoimmune pathogenesis.

---

## 3. Deucravacitinib — TYK2-Specific Allosteric Inhibitor

**Mechanism:** Deucravacitinib binds the TYK2 JH2 (pseudokinase) domain — not the ATP-binding JH1 kinase domain. This is the SAME regulatory site as P1104A. JH2 binding → mimics P1104A → enhanced autoinhibition → TYK2 JH1 activity ↓ → IL-12/IL-23 signaling ↓.

**Selectivity advantage over pan-JAK inhibitors:**
- Baricitinib/tofacitinib = ATP-competitive JAK1/2 inhibitors → suppress all JAK-STAT signaling
- Deucravacitinib = JH2 allosteric → preferentially suppresses TYK2 at IL-23R (IL-23 → STAT3) + IL-12R (IL-12 → STAT4); IFNAR/JAK1 signaling (IFN, IL-2) relatively preserved
- Clinical consequence: less immunosuppression, maintained anti-viral IFN response, no thrombocytopenia, no lipid elevation (JAK1-independent effects preserved)

**Approvals and trials:**
- Psoriasis: FDA approved 2022 (POETYK PSO-1/2 trials); first TYK2 inhibitor approval
- SLE: Phase 2 trials positive
- T1DM: Phase 2 trials ongoing (NIMBLE-T1D)
- Rosacea: no dedicated trial yet — but psoriasis mechanism (IL-23 → Th17 ↓) directly maps to rosacea Th17 papulopustular subtype

---

## 4. IL-12R/TYK2 → STAT4 → Th1 (T1DM Insulitis)

**IL-12 → Th1 differentiation:**
```
Macrophage/DC (in pancreatic lymph nodes or islets):
    [activated by viral PAMP / β cell DAMP]
    → IL-12 (heterodimer: p35 + p40 → IL-12p70)
    ↓
CD4 Th0 cell:
    IL-12 → IL-12R (IL-12Rβ1 + IL-12Rβ2)
    → TYK2 (Rβ1) + JAK2 (Rβ2) → STAT4 phospho (Y693)
    → STAT4 → T-bet (TBX21) → IFN-γ production
    → IFN-γ → macrophage M1 → more IL-12 (amplification loop)
    ↓
Th1 cells → IFN-γ + TNF-α → β cell MHC-I ↑ → CD8 T cell killing
```

**TYK2 P1104A effect on insulitis:**
- P1104A → STAT4 ↓ → T-bet ↓ → IFN-γ ↓ → less macrophage M1 amplification → less IL-12 → less Th1 differentiation → less insulitis
- Loop break: TYK2 P1104A disrupts the macrophage-Th1-IFN-γ positive feedback loop that drives insulitis progression
- NK cells: TYK2/STAT4 also drives NK IFN-γ production (not just T cells); P1104A → NK IFN-γ ↓ → less β cell activation signal from NK arm

**T1DM 12th genetic stratification:**
- rs34536443: OR ~0.65 protective (T allele protective; C allele = risk)
- Population frequency of protective T allele: ~5-8%
- Testing: includes TYK2 rs34536443 in T1DM polygenic risk score
- Clinical implication: P1104A carriers → naturally less IL-12/IL-23 signaling → lower insulitis risk → deucravacitinib mimics this protection pharmacologically in non-carriers

---

## 5. IL-23R/TYK2 → Th17 Maintenance (Rosacea Th17 Subtype)

**IL-23 biology:**
```
Macrophage/DC (dermal, activated by TLR2/LL-37/UV-B):
    → IL-23 (heterodimer: p19 + p40 → IL-23p19/p40)
    ↓
Differentiated Th17 cells (requires prior IL-6 + TGF-β → RORγt for induction):
    IL-23 → IL-23R (IL-23R + IL-12Rβ1)
    → TYK2 (IL-12Rβ1) + JAK2 (IL-23R) → STAT3 → STAT4 phospho
    → RORγt maintained (IL-23 = survival/persistence signal, not induction signal)
    → IL-17A sustained + IL-17F + IL-22
    ↓
Keratinocytes → IL-17A/IL-22 → KLK5 ↑ → LL-37 ↑ → Loop 1 perpetuation
```

**Rosacea Th17 subtype distinction:**
- Induction signals (IL-6 + TGF-β + IL-21 → RORγt): prior runs (079/062/074) addressed these
- **MAINTENANCE signal (IL-23 → TYK2 → STAT3 → RORγt persistence)**: NOT previously analyzed
- Gap: even with Th17 induction blocked, chronically differentiated Th17 cells persist via IL-23 maintenance. TYK2 inhibition → IL-23 signal terminated → RORγt expression ↓ → IL-17A production ↓ in EXISTING Th17 cells
- Psoriasis/deucravacitinib direct analog: psoriasis = IL-23/Th17-dominant skin disease; deucravacitinib approval for psoriasis directly informs rosacea papulopustular Th17 subtype

**Rosacea TYK2 mechanisms:**
1. IL-23 maintenance signal → Th17 persistence → IL-17A → KLK5 → Loop 1 (MOST RELEVANT for papulopustular subtype)
2. IL-12 → Th1 → IFN-γ → Loop 3 amplification (TYK2 P1104A also reduces Th1 in skin DCs)
3. TYK2 at IFNAR in keratinocytes: TYK2 P1104A → slightly reduced cGAS/IFN-β response (mild, but rosacea keratinocytes already have IFN-β excess, run_063)

---

## 6. ME/CFS Connections

**IL-12/STAT4 → NK IFN-γ:**
- TYK2/STAT4 pathway required for NK cell IFN-γ production
- ME/CFS: elevated NK IFN-γ but impaired cytotoxicity (runs 127/132/134/135 Ca²⁺ + developmental + metabolic)
- TYK2/IL-12/STAT4 → NK IFN-γ arm: TYK2 overactivation could contribute to NK IFN-γ production without cytotoxicity improvement (STAT4 drives cytokine production, not perforin/granzyme)
- MODERATE ME/CFS angle: TYK2 inhibition → NK IFN-γ ↓ → may reduce IFN signature in ME/CFS (but risk: reduce already-limited antiviral response)

**IL-23/Th17 in ME/CFS:**
- ME/CFS has elevated IL-17 in some cohorts
- TYK2/IL-23 → Th17 maintenance → IL-17 contribution to ME/CFS inflammation
- Less robust than T1DM/rosacea angles; borderline

**IFN-α arm (TYK2/IFNAR) in ME/CFS:**
- Run_133 (USP18) + run_006/040/063 already cover IFNAR/IFN persistence
- TYK2 P1104A affects IFNAR less than IL-12R/IL-23R → ME/CFS IFN persistence mechanism not primarily driven by TYK2 IL-12R arm
- Deucravacitinib would NOT be the primary ME/CFS intervention given preserved IFN signaling is needed for antiviral defense

---

## 7. Framework Connection Map

```
TYK2 (run_136)
    ├── IL-12R arm: TYK2 + JAK2 → STAT4 → T-bet → IFN-γ (Th1)
    │       ↔ IFN-γ → β cell MHC-I ↑ (runs 006/040/133 context)
    │       ↔ STAT4 → Th1 → Loop 3 amplification (rosacea)
    │       ↔ runs 079/062/074: Th1/Th17 balance (TYK2 = upstream IL-12 signal)
    │
    ├── IL-23R arm: TYK2 + JAK2 → STAT3/4 → RORγt maintenance → IL-17A
    │       ↔ run_079 (PPARγ → RORγt ↓): same RORγt target, different upstream
    │       ↔ run_062 (omega-3 → Th17 ↓): induction; TYK2/IL-23 = maintenance
    │       ↔ run_107 (LTB4/CysLTs): Th17-mast cell crosstalk downstream
    │
    ├── IFNAR arm: TYK2 + JAK1 → STAT1/2 (covered, runs 006/040/133)
    │       [P1104A preferentially reduces IL-12/IL-23 arms; IFNAR relatively preserved]
    │
    ├── Genetic: rs34536443 (12th T1DM stratification; broadest protective variant)
    │       ↔ Deucravacitinib (JH2 allosteric) = pharmacological P1104A mimic
    │       ↔ Baricitinib (run_133 context): TYK2 allosteric vs JAK1/2 ATP-competitive
    │
    └── ME/CFS: NK IFN-γ arm (STAT4) + IL-17 (IL-23); moderate; don't compromise IFN
```

---

## 8. β Cell Death — TYK2 Context

**No new numbered β cell death mechanism** — TYK2's contribution to β cell death is via IL-12 → Th1 → IFN-γ → β cell MHC-I ↑ → CD8 T cell killing. This pathway (IFN-γ effect on β cells) is already embedded in run_006 (type I IFN/T1DM insulitis context) and runs 040/133.

TYK2 is the upstream cytokine receptor kinase that initiates Th1 → IFN-γ production — adding mechanistic depth to existing β cell death pathways rather than a new numbered mechanism.

---

## 9. Protocol Integration

**Genetic stratification update (12th point):**
```
rs34536443 TYK2 (T allele = protective; C allele = risk):
    T allele: ~0.65 OR → ~35% relative T1DM risk reduction
    C allele (risk): normal TYK2 activity → full IL-12/IL-23 signaling
    Testing: add to polygenic risk score panel

Compound protective: rs34536443 T + other protective variants (CTLA4, IL2RA)
→ consider DUCRAvacitinib or lower monitoring frequency
```

**Clinical therapeutics — deucravacitinib:**
- Approved: psoriasis (FDA 2022, POETYK PSO-1/2)
- In trials: SLE, T1DM (NIMBLE-T1D), PsA
- Rosacea: off-label rationale established (IL-23 → Th17 → papulopustular; same mechanism as psoriasis)
- Advantage over baricitinib (run_133): TYK2-selective → preserved IFN/JAK1 signaling → lower infection risk; no thrombocytopenia
- Precaution: not OTC; prescription; monitor for infections; active TB or hepatitis B rule-out

**OTC context:**
- No selective OTC TYK2 inhibitor
- Omega-3 EPA/DHA (run_062): reduces IL-23 production from macrophages (via GPR120/PPAR-α → less IL-23p19 transcription) → indirect TYK2/IL-23R burden reduction
- Quercetin (run_127): reduces DC activation threshold → less IL-12/IL-23 production; indirect
- These do not constitute TYK2-specific OTC mechanisms

**Th17 MAINTENANCE vs INDUCTION — therapeutic implications:**
```
Th17 INDUCTION (IL-6 + TGF-β + IL-21 → RORγt):
    PPARγ → RORγt ↓ (run_079)
    Omega-3 → STAT3 suppression (run_062)
    IS reduction → less AhR Th17 induction (run_074)

Th17 MAINTENANCE (IL-23 → TYK2/JAK2 → STAT3 → RORγt persistence):
    Deucravacitinib → TYK2 JH2 → STAT3 ↓ → RORγt not maintained (run_136)
    [NEW: first maintenance-specific intervention in framework]
```

**T1DM insulitis — therapeutic implications:**
```
IL-12 pathway blockade:
    TYK2 inhibition (deucravacitinib): → STAT4 ↓ → T-bet ↓ → IFN-γ ↓ → less Th1 amplification
    vs. baricitinib (run_133): → JAK1/2 → broader STAT1/2/4/5 suppression
    Deucravacitinib advantage: Th1/Th17-selective suppression; IFN response (antiviral) preserved
```

---

## 10. Key Literature

- Shuai K, Liu B. (2003) Regulation of JAK-STAT signalling in the immune system. *Nat Rev Immunol* — JAK family structure/function overview
- Burke JR et al. (2019) Autoimmune pathways in mice and humans are blocked by pharmacological stabilization of the TYK2 pseudokinase domain. *Sci Transl Med* — TYK2 JH2 allosteric inhibition mechanism; deucravacitinib preclinical
- Armstrong AW et al. (2023) Trial of deucravacitinib versus placebo and apremilast in moderate-to-severe plaque psoriasis. *N Engl J Med* — POETYK PSO-1 trial; TYK2 approval
- Dendrou CA et al. (2016) Resolving TYK2 locus genotype-to-phenotype differences in autoimmunity. *Sci Transl Med* — rs34536443 mechanistic analysis; P1104A functional characterization
- Cooper JD et al. (2012) Meta-analysis of genome-wide association study data identifies additional type 1 diabetes risk loci. *Nat Genet* — T1DM GWAS including TYK2 region

---

*Gap.md updated: 2026-04-12 | One-hundred-and-twenty-ninth extension | TYK2 tyrosine-kinase-2 JAK-family pseudokinase JH2 allosteric P1104A rs34536443 protective-variant IL-12R IL-23R STAT4 T-bet Th1 IFN-γ RORγt-maintenance Th17 IL-23-maintenance-signal deucravacitinib BMS-986165 TYK2-allosteric rosacea-Th17-subtype papulopustular psoriasis-analog 12th-T1DM-stratification ME/CFS-NK-STAT4 JAK1-TYK2-IFNAR-covered Th17-maintenance-vs-induction POETYK-PSO Dendrou-2016-Sci-Transl-Med Burke-2019-Sci-Transl-Med Cooper-2012-Nat-Genet | run_136*
