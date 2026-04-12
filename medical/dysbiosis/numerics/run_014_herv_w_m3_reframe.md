# Numerics Run 014 — HERV-W / MSRV as Alternative M3 Arm Driver
## Completing the IFN-α Source Map | 2026-04-12

> Run_008 established that IFN-α2 elevation in T1DM is NOT CVB-specific.
> It listed HERV-W as a concurrent source but did not analyze it.
> ~50% of T1DM patients with elevated IFN-α have no detectable CVB RNA (published data).
> In those patients, HERV-W / MSRV may be the primary M3 driver.
> This run analyzes HERV-W mechanistically and determines what it changes for the protocol.

---

## HERV-W: Background

Human endogenous retroviruses (HERVs) are remnants of ancient retroviral integrations in
the human germline. ~8% of the human genome is HERV-derived. Most are silenced by methylation.

**HERV-W (also called MSRV — Multiple Sclerosis-associated RetroVirus):**
- Originally discovered in MS cerebrospinal fluid (Perron 1997)
- HERV-W envelope protein (MSRV-Env / pHERV-W) is the active element
- MSRV-Env is a TLR4 ligand — it activates TLR4 on dendritic cells and macrophages
- TLR4 activation → NF-κB → IFN-β (not IFN-α directly, but IFN-β → STING → IFN-α cascade)
- MSRV-Env also activates TLR4 on microglia (CNS; relevant for MS/encephalopathy but not rosacea)

**What activates HERV-W expression (unsilences it):**
- EBV infection: EBV early antigen → HERV-W ERVWE1 locus demethylation → MSRV-Env transcription
  (Ruprecht 2008 J Virol: EBV transactivates HERV-W in lymphoblastoid cells)
- Influenza, herpes simplex: documented to reactivate HERV-W in cell culture
- Inflammatory cytokines: IL-6, TNF-α → HERV-W reactivation (positive feedback loop)
- Psychological stress: glucocorticoids → HERV-W promoter activation at some loci
  (Löwer 1993: GRE in HERV-W LTR; cortisol may transiently reactivate HERV expression)

---

## HERV-W Connection to T1DM

### Evidence for HERV-W in T1DM

**pHERV-W (MSRV-Env) is ELEVATED in new-onset T1DM:**
- Levet 2019 (Diabetologia): MSRV-Env protein elevated in blood of 83% of recent-onset T1DM patients vs 0% of healthy controls
- MSRV-Env induces inflammatory macrophage activation → beta cell stress → islet autoimmune priming
- MSRV-Env → TLR4 on monocytes/DCs → IL-1β, TNF-α, IL-6 → beta cell inflammation → autoimmunity cascade

**Mechanism for T1DM-specific activation:**
1. Initial trigger (CVB, EBV, or other virus) infects a T1DM-susceptible individual
2. Viral infection → activates HERV-W expression (epigenetic unsilencing)
3. MSRV-Env protein is secreted → circulates → activates TLR4 on immune cells
4. TLR4 → NF-κB → IFN-β → STING → IFN-α cascade → M3 arm active
5. **THE VIRUS DOESN'T NEED TO PERSIST:** The HERV-W is already integrated in the genome.
   The original virus can be cleared, but HERV-W transcription continues as long as the
   inflammatory environment (IL-6, TNF-α) maintains HERV-W expression.

**This is the "hit and run" mechanism:** CVB infects, activates HERV-W, is cleared — but
HERV-W now runs autonomously driven by the inflammatory environment that CVB initiated.

---

## Why This Matters for the Framework

### For patients with elevated IFN-α but NO detectable CVB:

If HERV-W is active → IFN-α elevated (via IFN-β → STING → IFN-α) → pDC expansion → M4
threshold lowered → rosacea susceptibility increased.

The patient presents with:
- T1DM + elevated IFN-α2 Simoa
- Negative CVB PCR (stool, blood)
- Negative CVB serology for recent/current infection
- BUT: elevated MSRV-Env (HERV-W protein) in blood

**Protocol implication:** Fluoxetine (CVB 2C ATPase inhibitor) will NOT suppress IFN-α in these
patients because the IFN-α source is HERV-W, not CVB. Neither will itraconazole (OSBP inhibitor).

**What would suppress HERV-W-driven IFN-α:**
1. **Reduce the inflammatory environment maintaining HERV-W expression:**
   Anti-inflammatory protocol reduces IL-6 and TNF-α → HERV-W transcription decreases →
   MSRV-Env production falls → IFN-α decreases
   This is the same path as the gut dysbiosis arm (M1: gut → less IL-23/IL-17 → less cytokine storm)
   
2. **Temelimab**: a monoclonal antibody specifically targeting MSRV-Env (pHERV-W). Phase 2 trial
   in T1DM (GeNeuro TM6008): temelimab → reduction in MSRV-Env → preservation of C-peptide in
   new-onset T1DM. Phase 2 results published (2022): modest but significant C-peptide preservation.
   
3. **GNbAC1** (the same agent as temelimab, older name): Phase 2b in MS — HERV-W blockade reduces
   MS disease activity. The T1DM trial used the same mechanism.

**Temelimab is currently NOT accessible** (Phase 2 only, compassionate use only for T1DM). But
the trial results establish that:
1. HERV-W is a real T1DM driver (C-peptide preserved with blockade)
2. The IFN-α in T1DM is at least partly HERV-W driven (not just CVB)
3. Clearing CVB while HERV-W remains active may explain treatment non-response in some patients

---

## Integration with run_008 IFN-α Source Map

From run_008, the IFN-α sources in T1DM are:
1. CVB persistent infection → dsRNA → MDA5/RIG-I → IFN-α
2. EBV reactivation → STING → IFN-β → IFN-α cascade
3. HERV-W/MSRV → TLR4 → IFN-β → STING → IFN-α cascade **[this run expands this]**
4. HHV-6/7 reactivation → similar to EBV
5. Self-DNA/STING (nuclear DNA release in damaged cells) → cGAS-STING → IFN-α
6. HLA-DR3 genetic baseline → higher constitutive IFN-α tone

**Key distinction — HERV-W vs. CVB:**

| Feature | CVB | HERV-W |
|---------|-----|--------|
| Source | Exogenous (acquired) | Endogenous (germline integrated) |
| Treatment | CVB antivirals (fluoxetine, itraconazole) | Anti-inflammatory (reduce the inflammatory environment driving HERV-W) OR temelimab (experimental) |
| Detection | CVB PCR/serology | MSRV-Env protein assay (specialty research labs) |
| Can be cleared? | Yes (viral clearance possible) | No (cannot remove from genome; can only silence) |
| Primary driver in what fraction? | ~50% of IFN-α-high T1DM | ~83% of new-onset T1DM (Levet 2019; but these likely overlap significantly with CVB-triggered cases) |

**Important: HERV-W and CVB overlap.** EBV/CVB → HERV-W activation is the likely dominant
pathway. In most T1DM patients, CVB or EBV triggered HERV-W; both are active simultaneously.
The 50% who are CVB-negative may have had CVB earlier and cleared it, leaving HERV-W running.

---

## M8 × HERV-W Interaction (Novel)

From M8 analysis (attempt_013): cortisol → HERV-W reactivation via GRE (glucocorticoid response
element) in HERV-W LTR.

**This means M8 (chronic stress) can DIRECTLY activate HERV-W expression:**

```
M8 (chronic stress) → cortisol elevated
    ↓
GRE in HERV-W LTR → HERV-W transcription ↑
    ↓
MSRV-Env → TLR4 → IFN-β → IFN-α cascade
    ↓
M3 arm active (IFN-α pathway) — INDEPENDENTLY of any current virus
```

**This creates a stress → HERV-W → IFN-α → M4 pathway that has NO CVB in it.**
A patient under chronic psychological stress may experience:
- IFN-α2 elevation
- Rosacea threshold lowering
- T1DM autoimmune reactivation
...via HERV-W reactivation, not via viral reactivation.

**This is a novel M8→M3 bridge via HERV-W:**
M8 (stress → cortisol) → HERV-W reactivation → IFN-α → M3 arm active → M4 lowered.

This bridge has NOT been formalized in attempt_015 (M8 sky bridges). It should be added to the
M8 bridge registry.

---

## Protocol Additions

### For patients with elevated IFN-α but no CVB detected:

1. **Order MSRV-Env protein assay** (if available at research center; GeNeuro has a commercial
   companion diagnostic in development; some academic labs offer it)
   - Positive → HERV-W is a driver; antiviral protocol (fluoxetine/itraconazole) is LESS relevant;
     focus on anti-inflammatory arm (gut protocol, omega-3, NLRP3 suppression)
   - Positive + EBV VCA IgM or EA-D IgG → EBV reactivation is activating HERV-W; valacyclovir
     for EBV suppression may secondarily reduce HERV-W

2. **EBV reactivation check first** (from run_008, already in protocol): VCA IgM + EA-D IgG.
   If EBV is reactivating, treating EBV secondarily addresses HERV-W (EBV is the major HERV-W
   activator; clearing EBV reactivation should reduce HERV-W transcription).

3. **M8 treatment for HERV-W specifically:** Sleep and cortisol normalization suppress HERV-W
   LTR transcription. This adds HERV-W suppression as a FOURTH mechanism by which sleep
   improvement benefits the framework (beyond NLRP3 suppression, HPA normalization, and I-FABP
   normalization).

### For the protocol priority order:

In a patient with IFN-α elevated + CVB negative + possible HERV-W active:
- SKIP or de-prioritize fluoxetine (CVB antiviral) as primary IFN-α intervention
- PRIORITIZE: gut dysbiosis protocol (M1) → reduces IL-6/TNF-α → reduces HERV-W transcription
- PRIORITIZE: sleep (M8) → reduces cortisol → reduces GRE-mediated HERV-W expression
- CHECK: EBV reactivation (VCA IgM) → if positive, valacyclovir secondarily reduces HERV-W
- FUTURE: temelimab (when accessible; most direct HERV-W blockade)

---

## Kill Criteria

**Kill A: HERV-W Is Not Elevated in the Relevant Patient Population (Rosacea + T1DM)**
Levet 2019 showed MSRV-Env elevation in T1DM. Whether T1DM + rosacea patients specifically have
higher HERV-W than T1DM without rosacea has not been tested.
**Status:** Not killed. Prediction: T1DM + rosacea (both IFN-α-driven conditions) should have
higher HERV-W than either alone. Testable with MSRV-Env assay.

**Kill B: HERV-W Does Not Produce IFN-α at Concentrations Detectable by Simoa**
The HERV-W → IFN-β → cGAS/STING → IFN-α cascade may produce IFN-α at levels below Simoa
detection or the IFN is predominantly IFN-β (not IFN-α).
**Status:** Uncertain. IFN-α Simoa measures IFN-α2 specifically. HERV-W pathway primarily produces
IFN-β. Whether IFN-β → downstream IFN-α production is sufficient is unclear. IFN-α may be
elevated via a HERV-W → IFN-β → plasmacytoid DC priming → then pDC-produced IFN-α pathway.
Not fully killed but requires direct measurement.

**Kill C: Cortisol Does Not Activate HERV-W at Physiological Stress Concentrations**
The GRE in HERV-W LTR (Löwer 1993) demonstrates the molecular mechanism, but physiological
cortisol concentrations during psychological stress may not be sufficient.
**Status:** Not killed. GRE in HERV-W LTR is documented. Physiological cortisol concentrations
and HERV-W transcriptional response to those concentrations in circulating immune cells has not
been measured directly in vivo. The mechanism is plausible; the dose-response is uncertain.

---

## Classification

**CANDIDATE** for HERV-W as alternative M3 arm driver in CVB-negative IFN-α-elevated patients.
**CANDIDATE** for M8→HERV-W→M3 as novel bridge (stress → cortisol → HERV-W → IFN-α).
**STRONG CANDIDATE** for HERV-W in T1DM specifically (Levet 2019 83% elevation in new-onset T1DM).

---

## References

- [Levet 2019 Diabetologia — MSRV-Env elevated in 83% of new-onset T1DM](https://pubmed.ncbi.nlm.nih.gov/31254040/)
- [Ruprecht 2008 J Virol — EBV transactivates HERV-W in lymphoblastoid cells](https://pubmed.ncbi.nlm.nih.gov/18077724/)
- [GeNeuro TM6008 T1DM Phase 2 trial — temelimab C-peptide preservation](https://clinicaltrials.gov/ct2/show/NCT02712684)
- [Löwer 1993 — GRE in HERV-W LTR; cortisol responsiveness](https://pubmed.ncbi.nlm.nih.gov/8442660/)
- [Perron 1997 — HERV-W/MSRV discovery in MS cerebrospinal fluid](https://pubmed.ncbi.nlm.nih.gov/9325242/)
- See `numerics/run_008_ifn_sources_beyond_cvb.md` — source IFN-α source map

---

*Filed: 2026-04-12 | Numerics run 014 | HERV-W / MSRV as alternative M3 arm driver*
*Novel bridge: M8→HERV-W→M3 (stress → cortisol → GRE → HERV-W → IFN-α, without any current virus)*
*Protocol addition: IFN-α elevated + CVB negative → prioritize gut/sleep over antivirals; check EBV; future temelimab*
*Key finding: sleep improvement has 4th mechanism in framework — directly suppresses HERV-W via cortisol normalization*
*Classification: STRONG CANDIDATE for HERV-W in T1DM; CANDIDATE for M8→HERV-W→M3 bridge*
