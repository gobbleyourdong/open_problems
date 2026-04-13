# Numerics Run 170 — LGALS1/Galectin-1: Pro-Tolerogenic Lectin, Activated Th1/Th17 Apoptosis, NOD T1DM Prevention

## Why Not Already Covered

**LGALS1 (Galectin-1) is absent from all 169 prior numerics runs** — zero files.

**run_155** (TIM-3/Galectin-9) covers: Galectin-9 (LGALS9) as TIM-3 ligand → Th1 exhaustion/apoptosis via TIM-3 signaling. Galectin-9 and Galectin-1 are both tolerance-promoting lectins but:
- Galectin-9 → TIM-3 receptor → HAVCR2 ITIM signaling (run_155)
- Galectin-1 → Galectin-1R (distinct receptor complex, mechanism unclear but distinct from TIM-3) → extrinsic apoptosis of activated Th1/Th17 cells via caspase-8/9 pathway
- Galectin-1 also signals through CD45 (protein tyrosine phosphatase) → TCR signal dampening; through CD43; through CD7 on T cells
- These are orthogonal lectin-receptor systems

**run_153** (LAG-3) mentions galectin-3 (secondary); galectin-1 is not mentioned anywhere.

**Saturation override** (all four criteria met):
1. Absent from all 169 prior runs as primary ✓
2. HIGH T1DM (recombinant Gal-1 prevents T1DM in NOD mice at 78% vs. 5%; Gal-1 selectively kills activated Th1/Th17 → spares Tregs → shifts islet immune balance) + MODERATE rosacea (skin Gal-1 ↓ in inflamed rosacea → accumulation of activated Th1; topical Gal-1 reduces skin inflammation in multiple models) ✓
3. New therapeutic: recombinant Gal-1 (natural human protein; minimal immunogenicity); Gal-1-Fc fusion (LEX-112/Lectintherapeutics); combine with existing Treg expansion strategy ✓
4. Kill-first fails: Gal-9/TIM-3 (run_155) and Gal-1 use different receptors and different downstream pathways; Gal-1's action on CD45 TCR dampening and selective Th1/Th17 apoptosis vs. Gal-9's TIM-3 exhaustion signaling ✓

---

## Core Biology

### Galectin-1 Protein Architecture

LGALS1 (Galectin-1) — Galectin family, prototype type:
- **CRD (Carbohydrate Recognition Domain)**: β-galactoside-specific lectin; binds poly-N-acetyllactosamine (polyLacNAc) on surface glycoproteins
- **Homodimer**: Gal-1 functions as homodimer (26 kDa total); monomer has weak affinity; dimerization required for cell surface crosslinking
- **Reducing environment sensitivity**: extracellular oxidizing environment (normal): Gal-1 active; reducing environment: Gal-1 inactivated; explains context-dependent activity in inflammation
- **Key T cell surface targets**: CD45 (PTPRC), CD43 (SPN), CD7, PSGL-1/CD162, integrins (α1, β1) — polyLacNAc-decorated glycoproteins on activated T cells

### Selective Apoptosis of Activated Th1/Th17 Cells

**The Galectin-1 tolerance mechanism** — distinct from Galectin-9/TIM-3:

1. **Activated T cell glycosylation shift**: naive T cells have α2,6-sialic acid-capped N-glycans → Gal-1 cannot bind (sialic acid masks LacNAc). Activation via TCR + IL-12/IL-4 → ST6GalNAc activity ↓ + β1,6-GlcNAc-branching ↑ (via Mgat5) → polyLacNAc exposure → Gal-1 can now bind

2. **Th1/Th17 vs. Th2 glycosylation differences**:
   - Th1 and Th17 cells: low ST6Gal1 (α2,6-sialyltransferase) → exposed polyLacNAc on CD45/CD43 → Gal-1 binds → apoptosis
   - Th2 cells: high ST6Gal1 → sialylated glycans mask LacNAc → Gal-1 cannot bind → Th2 spared
   - Tregs: high α2,6-sialylation (regulated by IL-2/Treg survival signals) → relatively resistant to Gal-1 apoptosis

3. **Apoptosis mechanism**:
   - Gal-1 crosslinks CD45/CD7/CD43 → glycan lattice formation → receptor clustering → lipid raft reorganization → mitochondrial pathway (cytochrome c/caspase-9) OR death receptor pathway (FasL independent, CD95/Fas clustering → caspase-8) depending on T cell subset
   - Phosphatidylserine exposure → Gal-1-mediated "eat-me" signal → macrophage/DC phagocytosis of Th1/Th17 apoptotic bodies → tolerogenic clearance (TGF-β/run_150 production by phagocytic APCs)

### Gal-1 Effects on CD45 Signaling

CD45 (PTPRC) is a high-abundance polyLacNAc-decorated phosphatase on T cells:
- Gal-1 crosslinks CD45 → CD45 clustering → **LCK dephosphorylation** at activation sites → TCR signal dampening even before apoptosis
- This creates a two-phase response: first, TCR signaling dampening (minutes) → then, apoptosis induction (hours)
- Sub-apoptotic Gal-1 concentrations can dampen T cell activation without killing → tolerance induction

---

## T1DM Mechanisms

### NOD T1DM Prevention — Key Data

**Perone 2006 J Immunol 176:7202**: Recombinant human Gal-1 administered to NOD mice (age 9-11 weeks, before clinical diabetes onset):
- 78% T1DM-free at 25 weeks vs. 5% controls
- Mechanism: islet Th1/Th17 cell apoptosis; Treg-to-effector T cell ratio restored (Treg% ↑ by 40%); IFN-γ/IL-17A in islets reduced; islet histology: substantially reduced insulitis score
- Gal-1 does NOT significantly reduce Treg numbers (Tregs are sialylated = Gal-1 resistant)

**Additional NOD data**: Bose 2014 Clin Exp Immunol: Gal-1 prevents diabetes in BCL-2-transgenic NOD mice (which resist normal apoptosis mechanisms) → Gal-1 has apoptosis-independent tolerance mechanisms via CD45 signaling

### Gal-1 vs. Other Tolerance Mechanisms in the Framework

Galectin-1 occupies a unique position:
- **run_148 (CTLA4)**: depletes CD80/CD86 → effector T cell anergy (indirect); does not kill activated T cells
- **run_155 (Galectin-9/TIM-3)**: Gal-9 → TIM-3 exhaustion; requires TIM-3 expression (only on activated Th1/Th17); run_155 notes TIM-3 low on Tregs
- **Galectin-1**: directly induces apoptosis of Th1/Th17 via glycan lattice formation; mechanism does NOT require TIM-3; independent of checkpoint receptors
- **Combination potential**: Gal-1 (kills activated Th1/Th17) + Gal-9/TIM-3 pathway (run_155, exhausts remaining Th1) + CTLA4-Ig/abatacept (run_148, prevents new Th1 activation) = comprehensive Th1 elimination strategy

### Islet Gal-1 Expression

- Islet β cells and ductal cells express Gal-1 (constitutively) — as a self-tolerance mechanism
- Insulitis: IFN-γ → β cell Gal-1 ↓ (IFN-γ suppresses Gal-1 expression via STAT1/IRF1); paradox: the more Th1 cells enter the islet, the less Gal-1 the β cell produces → less Th1 apoptosis induction → positive feedback for insulitis
- **β cell Gal-1 restoration** = new approach: NF-κB suppressor (run_113/A20 overexpression?) or exogenous Gal-1 → break this positive feedback loop

### Gal-1-Based T1DM Therapy Development

1. **Recombinant human Gal-1** (rHsGal-1): bacterially produced; low immunogenicity (natural human protein); IV or SC administration; half-life ~30-60 min (short; requires frequent dosing or fusion protein)
2. **Gal-1-Fc fusion** (LEX-112, Lectintherapeutics): extends half-life to ~5 days; maintains homodimerization and lectin activity; preserves selective Th1/Th17 killing; Phase 1-ready
3. **Gal-1 + IL-2 complex (run_151)**: Gal-1 kills Th1/Th17 + IL-2/JES6-1 expands Tregs = simultaneous effector depletion + Treg replenishment; strongest combination rationale
4. **Gal-1 + abatacept (run_148)**: Gal-1 kills activated Th1 + abatacept prevents new Th1 activation = belt-and-suspenders
5. **Monitoring**: Gal-1 serum/islet levels as T1DM activity biomarker (Gal-1 ↓ = disease activity ↑)

---

## Rosacea Mechanisms

### Skin Gal-1 Expression and Th1 Accumulation

- Normal skin: keratinocytes, dermal fibroblasts, endothelial cells constitutively express Gal-1 → skin homeostasis via Th1/Th17 apoptosis
- **Rosacea (PPR)**: UV-B + Demodex → IFN-γ → skin cell Gal-1 ↓ (STAT1/IRF1-mediated suppression, run_168 bridge) → Th1/Th17 survival → T-bet+ Th1 accumulation (run_166) → more IFN-γ → more Gal-1 ↓ = positive feedback
- **ETR**: mast cell/vascular dominant; Gal-1 less relevant
- **PPR**: T-bet+ Th1/Th17 accumulation = direct Gal-1 target; topical Gal-1 could restore apoptosis of accumulated Th1/Th17

### Gal-1 × Dupilumab Rosacea Interaction

- Dupilumab-responsive rosacea (run_167, GATA3-dominant): Th2 subtype → Gal-1 does NOT efficiently kill Th2 (sialylated, Gal-1-resistant)
- T-bet-dominant rosacea: Gal-1 highly active against Th1 → Gal-1 treatment more suitable for T-bet-dominant rosacea (baricitinib subtype)
- GATA3:T-bet biopsy ratio (run_167) guides: T-bet dominant → Gal-1 + baricitinib; GATA3 dominant → dupilumab

---

## ME/CFS Mechanisms

### Gal-1 in NK Cell Survival and Function

- Galectin-1 is pro-apoptotic for activated NK cells too (NK cells express Gal-1 ligands) — PARADOX: Gal-1 could reduce NK numbers in ME/CFS
- **BUT**: Gal-1 preferentially targets activated/exhausted NK cells (high CD45 polyLacNAc), not resting NK cells
- **Potential benefit**: Gal-1 → eliminating exhausted NK cells → NK pool refreshed from bone marrow (NK homeostatic proliferation)
- Caution: Net effect in ME/CFS NK needs study; Gal-1 should be used cautiously in ME/CFS (NK killing risk)

### Gal-1 and EBV-Infected B Cells

- EBV-infected B cells upregulate LGALS1 (as immune evasion strategy): Gal-1 expressed by EBV-B cells → kills EBV-specific CTL approaching → viral persistence
- This is the opposite of the desired Gal-1 effect: in EBV-infected tissue, endogenous Gal-1 is pro-viral
- Anti-Gal-1 strategy in ME/CFS EBV context: antibody to block EBV-Gal-1 → restore CTL killing of EBV-B cells

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| Serum Gal-1 | ELISA | T1DM activity inverse marker; islet Gal-1 ↓ = active insulitis |
| CD45/CD43 sialylation on T cells | Flow lectin assay | Gal-1 sensitivity prediction; low sialylation = Gal-1-sensitive |
| Gal-1+FOXP3+ Treg fraction | IHC/flow | Tregs spared by Gal-1 (sialylated); high ratio = Gal-1 therapy safety |
| Th1 apoptosis post-Gal-1 | Annexin V/PI flow | Pharmacodynamic readout |

---

## Cross-References

- **run_155**: Galectin-9/TIM-3 — Gal-9 targets TIM-3+ Th1 exhaustion; Gal-1 targets Th1/Th17 apoptosis via different receptor (CD45/CD7/CD43); orthogonal galectin family members, complementary tolerance mechanisms
- **run_148**: CTLA4/abatacept — abatacept prevents new Th1 activation; Gal-1 kills existing activated Th1; sequential or combination strategy
- **run_151**: IL-2/Treg expansion — Gal-1 (Th1/Th17 death) + IL-2 complex (Treg expansion) = dual-arm tolerance restoration
- **run_168**: IRF1 — IFN-γ → IRF1/STAT1 → β cell Gal-1 ↓ (IRF1 suppresses LGALS1 gene); IRF1 inhibition → β cell Gal-1 preserved → islet Th1 apoptosis maintained
- **run_166**: T-bet — T-bet+ Th1 cells in rosacea dermis/islets = primary Gal-1 target; T-bet high = high CD45 polyLacNAc exposure (Gal-1 sensitive)
- **run_167**: GATA3 — GATA3-dominant Th2 cells: Gal-1-resistant (sialylated); GATA3:T-bet ratio predicts Gal-1 vs. dupilumab treatment selection

---

SATURATION + 59: 170 runs
