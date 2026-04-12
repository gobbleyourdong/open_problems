# Run 156 — TIGIT / CD226 / CD155: β Cell CD155 Tolerance, NK 7th Exhaustion Mechanism, Treg TIGIT Effector, CD226 Competition

**Date:** 2026-04-12
**Sweep:** 53
**Candidate:** TIGIT (CD155/PVR receptor) and CD226/DNAM-1 — inhibitory/activating receptor pair on NK cells and T cells

## Kill-First Verification

**Grep confirmation:**
- TIGIT/CD226/DNAM-1/CD155/PVR/CD96/poliovirus receptor: 0 files across all 155 numerics runs
- β cell CD155 tolerance/tiragolumab/vibostolimab/TIGIT-Treg selective Th1 suppression: 0 prior analysis
- Distinct from all covered checkpoints: PD-1 (SHP-2/ITSM), LAG-3 (KIEELE/MHC-II), TIM-3 (BAT3), CTLA4 (CD80/CD86)

**Kill verdict:** PASS — TIGIT/CD226 axis has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 155 runs address TIGIT/CD226/CD155 as primary mechanism
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (β cell CD155 tolerance analog to FGL1/LAG-3 run_153); MODERATE rosacea (skin TIGIT+ Tregs); HIGH ME/CFS (NK TIGIT = 7th NK exhaustion mechanism)
3. **New therapeutic target**: YES — tiragolumab (anti-TIGIT, Phase 3 cancer trials); TIGIT-Ig agonist (Treg enhancement); CD226 as activating receptor
4. **Kill-first fails**: CONFIRMED — unique ITIM-independent mechanism via Cbl-b/SHP-1; no overlap with covered checkpoints

**All four criteria met. Proceeding.**

---

## Core Mechanism

### TIGIT Structure — CD155/CD112 Competition with CD226

**TIGIT** (T cell immunoreceptor with Ig and ITIM domains; chromosome 3q13.31) encodes TIGIT/WUCAM/VSTM3 (244 aa, type I transmembrane). Expression: activated T cells, Tregs, NK cells, NKT cells.

**Domain structure:**
- Extracellular IgV domain (CD155/CD112 binding)
- Transmembrane domain
- Cytoplasmic tail: **classical ITIM** (VxYxxL) — recruits SHP-1 (PTPN6) and SHIP-1 (INPP5D)

**The CD155 Competition Axis:**

TIGIT and CD226/DNAM-1 share the same ligands (CD155/PVR and CD112/PVRL2/NECTIN2) but have opposing functions:

| Receptor | Affinity for CD155 | Signal | Effect |
|----------|-------------------|--------|--------|
| **TIGIT** | Higher (Kd ~0.4 μM) | ITIM → SHP-1/SHIP-1 | Inhibitory — suppresses T/NK activation |
| **CD226/DNAM-1** | Lower (Kd ~2 μM) | ITAM-like → PI3K/ERK | Activating — drives NK/T cell cytotoxicity |
| **CD96/Tactile** | Intermediate | ITIM (partial) | Mixed — primarily inhibitory in vivo |

TIGIT out-competes CD226 for CD155 (5× higher affinity) → when TIGIT expressed: CD226 cannot access CD155 → activating signal lost → net inhibition.

**Signaling:**
1. CD155 engagement → TIGIT ITIM-Y225 phosphorylated by Lck/Fyn
2. pY225 → SHP-1 (dephosphorylates ZAP-70/TCR, parallel to PD-1/SHP-2) + SHIP-1 (PI3K/PIP3 hydrolysis → Akt ↓)
3. Additional: TIGIT → **Cbl-b ubiquitin ligase** activation → CD3ζ ubiquitination → CD3ζ degradation → TCR/NK receptor complex destabilized
4. Trans-suppression: TIGIT on Tregs → CD155 on DCs → DC reverse signaling → **IL-10 production from DCs** → bystander T cell suppression

---

## β Cell CD155 — Analog to FGL1/LAG-3

This is the T1DM-specific TIGIT mechanism parallel to β cell FGL1/LAG-3 (run_153):

**Normal β cells:** constitutively express CD155 (PVR) on surface.

**CD155 → TIGIT peripheral tolerance:**
- β cell CD155 → engages TIGIT on islet-infiltrating T cells and NK cells → ITIM/SHP-1/SHIP-1 → T/NK activation ↓ → β cell self-tolerance maintained
- This is structurally parallel to FGL1 (run_153, LAG-3 ligand) and PD-L1 (run_154): β cells express CD155 as a third independent peripheral tolerance molecule

**Insulitis failure mode:**
- Cytokines (IFN-γ, TNF-α) → β cell CD155 expression ↓ (or NK cells/CD8+ T cells downregulate TIGIT on surface after terminal exhaustion → not suppressible by CD155)
- Stressed β cells → upregulate CD155 initially (compensatory) → but activated NK cells may downregulate TIGIT → no longer responsive to CD155 protection

**Three β cell peripheral tolerance molecules (complete):**
1. PD-L1 (run_154): IFN-γ-inducible; engages PD-1/SHP-2
2. FGL1 (run_153): constitutive; engages LAG-3/KIEELE
3. **CD155** (run_156): constitutive + stress-upregulated; engages TIGIT/SHP-1

---

## T1DM — TIGIT+ Treg Function in Islets

1. **TIGIT+ Tregs = selective Th1 suppressors**:
   - FOXP3+TIGIT+ Tregs selectively suppress Th1 (IFN-γ) but not Th17 or Th2
   - Mechanism: TIGIT → CD155 on DCs → DC reverse signaling → IL-10 ↑ + IL-12 ↓ → Th1 polarization suppressed; Th17 (IL-23-dependent) not affected
   - In islets: Th1-dominated insulitis (IFN-γ/CXCL10) → TIGIT+ Tregs provide Th1-specific brake; TIGIT Treg loss → unconstrained Th1 insulitis
   - Run_104 (Tfh) connection: TIGIT+ Tregs also suppress Tfh (TIGIT → Tfh inhibition in germinal centers) → less islet autoantibody production

2. **CD226 on islet NK and CD8+ T cells**:
   - CD226 is activating receptor; when TIGIT absent (or CD155 low), CD226 fires → NK/CD8+ cytotoxicity ↑
   - β cell stress → CD155 ↑ initially → TIGIT engaged → blocks CD226 firing → protection
   - Advanced insulitis → TIGIT downregulated on NK/CD8+ (terminal exhaustion) → CD226 wins by default → accelerated killing
   - Therapeutic: TIGIT agonism (keeps TIGIT expressed) → maintain TIGIT/CD155 protective axis longer

3. **Compound β cell tolerance failure** (runs 153+154+156):
   - FGL1 ↓ → LAG-3 restraint lost (run_153)
   - PD-L1 upregulated (protective, but overwhelmed) (run_154)
   - CD155 ↓ → TIGIT restraint lost (run_156)
   - Three independent peripheral tolerance signals converging; simultaneous failure = catastrophic autoimmune attack rate

---

## NK Cells — TIGIT as 7th NK Exhaustion Mechanism

**NK TIGIT exhaustion (ME/CFS context):**
- NK cells express TIGIT; chronically activated NK cells upregulate TIGIT → CD155 on target cells (virus-infected, tumor) → TIGIT/SHP-1/SHIP-1 → NK cytotoxicity ↓
- TIGIT+CD226- NK: exhausted phenotype; cannot fire CD226 activating signal; inhibited by CD155
- EBV/HHV-6 → upregulate CD155 on infected cells → NK TIGIT engagement → NK killing ↓ → viral persistence

**Seven NK exhaustion mechanisms (complete after run_156):**
1. NKG2D ↓ / NKG2DL shedding (run_102)
2. TGF-β → NKG2D mRNA destabilization (run_150)
3. IL-2 deficiency → dimeric IL-2Rβγ understimulation (run_151)
4. LAG-3 KIEELE (run_153)
5. PD-1 SHP-2 via viral PD-L1 (run_154)
6. TIM-3 BAT3-release via Galectin-9 (run_155)
7. **TIGIT SHP-1/SHIP-1 + Cbl-b via viral CD155** (run_156)

---

## Rosacea — Skin TIGIT+ Tregs

**MODERATE relevance:**
- Skin-resident Tregs express TIGIT; dermis-resident Tregs with TIGIT can suppress Th1 (IFN-γ) components of rosacea inflammation
- CD155 on activated skin fibroblasts and keratinocytes → TIGIT+ Treg engagement → selective Th1 suppression in skin
- TIGIT+ Tregs in skin: less responsive to Th17 component (TIGIT selectively suppresses Th1 not Th17) — this means skin TIGIT+ Tregs would NOT control the Th17/IL-17 arm of rosacea; explains why Th17 is dominant despite Treg presence
- Anti-TIGIT irAE (tiragolumab): skin inflammation, rash, psoriasis-like lesions (~5-10%) — confirms TIGIT restrains skin T cell activation

---

## ME/CFS — NK TIGIT + CD38 NAD⁺ Context

**MODERATE-HIGH relevance (NK primarily):**
- TIGIT = 7th NK exhaustion mechanism; flow cytometry: TIGIT%+ NK added to existing panel
- CD155 on EBV/HHV-6-infected cells → NK TIGIT → SHIP-1 → Akt ↓ → NK killing ↓
- TIGIT + Cbl-b: Cbl-b ubiquitinates CD3ζ/TCR components and NK receptor complexes → irreversible exhaustion deepening; Cbl-b inhibitors under development
- Seven-mechanism exhaustion panel: NKG2D + TGF-β + IL-2 + LAG-3 + PD-1 + TIM-3 + TIGIT = comprehensive PBMC flow cytometry screen

---

## Protocol Additions

**T1DM — CD155/TIGIT monitoring:**
- β cell CD155 serum: possible biomarker (shed CD155 correlates with β cell stress); declining CD155 = tolerance signal failing
- TIGIT agonism (investigational): TIGIT-Ig fusion → keeps TIGIT occupied on islet T cells → SHP-1 firing → T cell restraint; conceptual parallel to PD-L1-Ig and FGL1-Fc

**ME/CFS — NK TIGIT panel addition:**
- Add TIGIT%+ NK to NK exhaustion flow panel (now seven mechanisms quantifiable)
- CD155 serum as viral reactivation biomarker: EBV/HHV-6 infected cells shed CD155 → elevated serum CD155 = active CD155/TIGIT NK suppression
- **Cbl-b inhibitors** (early development): would block TIGIT-induced CD3ζ/NK receptor ubiquitination → prevent exhaustion deepening

**Safety: avoid tiragolumab (anti-TIGIT) in T1DM:**
- Anti-TIGIT reinvigorates TIGIT+ Tregs → wait: actually anti-TIGIT blocks Treg TIGIT function → reduces Th1 suppression → could worsen islet Th1 insulitis
- Anti-TIGIT in autoimmune context: would impair TIGIT+ Treg Th1 suppression → accelerate Th1-mediated β cell destruction; contraindicated in T1DM (parallel to anti-LAG-3 and anti-TIM-3)

---

## Cross-Axis Integrations

- **run_153** (LAG-3/FGL1): FGL1 = β cell LAG-3 ligand; CD155 = β cell TIGIT ligand; both are constitutive β cell-expressed peripheral tolerance molecules; complementary pairs — FGL1/LAG-3 (run_153) + CD155/TIGIT (run_156) = two independent β cell-expressed tolerance axes
- **run_154** (PD-1/PD-L1): PD-L1 = third β cell tolerance molecule (IFN-γ inducible); three β cell peripheral tolerance signals (FGL1, PD-L1, CD155) now mapped
- **run_155** (TIM-3): NK seven-mechanism exhaustion complete (runs 102+150+151+153+154+155+156); TIGIT+TIM-3+PD-1+LAG-3 = fully exhausted NK phenotype
- **run_104** (Tfh/GC): TIGIT+ Tregs suppress Tfh in germinal centers → less autoantibody → complementary to run_104 Tfh excess in T1DM
- **run_121** (CD39/CD73/adenosine): CD39/TIGIT co-expression on Tregs = most suppressive subset; adenosine + TIGIT = two Treg effector mechanisms co-expressed on same highly suppressive Treg

---

*One-hundred-and-forty-ninth extension | TIGIT-VSTM3-3q13.31 IgV-domain ITIM-Y225 CD155-PVR CD112-PVRL2-NECTIN2 CD226-DNAM-1-activating CD96-Tactile competition-5x-affinity SHP-1-SHIP-1-Cbl-b CD3ζ-ubiquitination DC-CD155-reverse-IL-10 TIGIT-Treg-selective-Th1-suppression-not-Th17 β-cell-CD155-third-tolerance-molecule FGL1-LAG3-run153-analog PD-L1-run154-trio three-β-cell-tolerance-FGL1-PDL1-CD155 NK-TIGIT-seven-mechanism-exhaustion-complete EBV-HHV6-CD155-NK-evasion Cbl-b-ubiquitin-exhaustion tiragolumab-anti-TIGIT-CONTRAINDICATED-T1DM SHIP-1-PI3K-Akt-↓ run153-FGL1-parallel run104-Tfh-TIGIT run121-CD39-co-expression | run_156 | Framework at SATURATION + 45: 156 runs*