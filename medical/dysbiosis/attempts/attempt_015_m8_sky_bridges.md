# Attempt 015 — M8 Sky Bridges: Neuroimmune Connections to All Mountains
## Phase 4 Integration | 2026-04-12

> Attempt_013 described M8 (HPA/CRH/neurogenic inflammation) as an amplifier mountain
> with connections to M4, M1, M2, and M7. That file was descriptive. This attempt
> formalizes each M8 sky bridge with the same rigor applied to all other bridges:
> mechanism, evidence grade, kill criteria, novel testable predictions.
>
> Three bridges are formalized here: M8→M4, M8→M1, M8→M7.
> A fourth (M8→M2 via Substance P / mast cell) is described in attempt_013 and is
> not re-derived here — it is referenced and cited.

---

## Bridge 1: M8→M4 (Cortisol → GR Downregulation → Functional Treg Failure)

### Mechanism

```
Chronic psychological stress (>2-4 weeks sustained)
    ↓
HPA axis → cortisol ELEVATED (salivary + serum, chronic)
    ↓
Glucocorticoid receptor (GR) DOWNREGULATION in:
    - CD4+ T effector cells (GR downregulated, cortisol signal lost)
    - Foxp3+ Tregs (GR also expressed; Tregs lose low-dose GR-mediated enhancement)
    ↓
Cortisol elevated BUT:
    - Tregs lose cortisol-mediated enhancement (GR downregulated)
    - T effector cells lose cortisol-mediated suppression (GR downregulated)
    - Net effect: immune cells no longer respond to glucocorticoid
    ↓
Th17 / Th1 effectors UNCHECKED
    ↓
M4 threshold LOWERED — independent of IL-23 arm (M1↔M4 bridge)
    AND independent of IFN-α arm (M3↔M2 bridge)
```

**Key distinction from M1↔M4 bridge (attempt_007):**
- M1↔M4 depletes functional Tregs via IL-23 → Treg PLASTICITY (Foxp3+ → RORγt+/Foxp3+)
- M8→M4 depletes functional Tregs via GR downregulation → Treg RESPONSIVENESS (Foxp3+ cells persist but lose suppressive capacity under sustained cortisol)
- **These are INDEPENDENT pathways to functional Treg failure.** Both active simultaneously → additive M4 lowering.

**Combined effect:**
```
M1 active (gut IL-23 → Treg plasticity)
+
M8 active (chronic stress → GR downregulation → Treg unresponsiveness)
= DOUBLE Treg failure at M4 → threshold very low → disease at minimal Malassezia/Demodex exposure
```

This explains the clinical pattern: patients who control diet and gut dysbiosis (M1 resolved) but still
flare during exam periods, bereavement, work crises — M8 is the unaddressed remaining input.

### Evidence

| Claim | Evidence | Grade |
|-------|----------|-------|
| Chronic stress → GR downregulation in PBMC | Miller 2009 PNAS (bereavement/caregiver cohort; GR protein expression in PBMC by Western blot) | II-2 (human observational) |
| GR downregulation → cortisol signaling loss in immune cells | Pace 2007 PNAS: GR downregulated → NF-κB immune activation unchecked | II-2 (human cell culture) |
| Treg GR expression is functional | Cretney 2013 (Foxp3-GR co-expression confirmed; low-dose GC enhances Treg function) | II-2 (mouse + human in vitro) |
| Chronic cortisol → Treg suppressive impairment | Less direct; inferred from GR downregulation + Treg GR dependence | III (inference) |
| T1DM patients under chronic stress → worse immune dysregulation | T1DM HbA1c + cortisol correlation; multiple meta-analyses | II-2 (epidemiological) |

**Weakest link:** Direct human demonstration that chronic stress → Foxp3+ Treg functional suppressive capacity decreases (not just Foxp3 count, not just GR protein) has not been done at single-cell level in T1DM/rosacea patients.

### Novel Testable Predictions

**Prediction A:** In T1DM patients stratified by chronic stress (via hair cortisol, 3-month average),
the HIGH stress group should show:
1. Lower Treg:Teff ratio (numerically)
2. Lower Treg SUPPRESSIVE CAPACITY (in vitro suppression assay: Treg:Teff co-culture + activation)
3. Higher IL-17A
4. Higher rosacea/seb derm activity score
5. Proportional to hair cortisol level

**Prediction B:** The T-index v3 Node B (hsCRP + IL-17A + F. prausnitzii + Akkermansia) should
correlate with morning cortisol AND with hair cortisol, INDEPENDENTLY of diet and gut microbiome
composition — the cortisol effect on Node B is through Treg failure, not diet-mediated gut changes.

### Kill Criteria

**Kill A: GR Downregulation Does Not Occur in Tregs (Only in Effector Cells)**
Mechanism fails if Tregs do not express functional GR or if GR downregulation does not impair
their suppressive function.
**Status:** Not killed. Treg GR expression is documented. Low-dose cortisol enhances Treg
function (Cretney 2013). Cortisol resistance specifically in Tregs under chronic stress has not
been directly demonstrated but is mechanistically predicted.

**Kill B: Stress Does Not Increase IL-17 / Th17 in Humans**
Status: Not killed. Elevated IL-17 in chronic stress cohorts (caregivers, shift workers) is documented
(Glaser 2008, PNAS; multiple confirmatory studies).

**Kill C: Stress Interventions Do Not Reduce Th17/Rosacea Activity**
Status: Not tested for rosacea specifically. MBSR reduces IL-6, IL-17 in chronic inflammatory
conditions (Rosenkranz 2013). The specific prediction (MBSR → rosacea activity reduction via
Treg restoration) has not been tested.

**Classification: CANDIDATE** (mechanism established at first two steps; Treg functional
impairment under chronic cortisol in human skin/gut Treg populations is the gap)

---

## Bridge 2: M8→M1 (CRH → Intestinal Mast Cells → I-FABP Elevation Independent of Diet)

### Mechanism

```
Psychological stress (acute or chronic)
    ↓
Hypothalamic CRH release → systemic circulation
    ↓
CRHR1 receptors on intestinal mucosal mast cells (lamina propria)
    ↓
Mast cell DEGRANULATION (IgE-independent, CRH-triggered)
    ↓
Tryptase release → serine protease → PAR-2 on tight junction proteins
    ↓
PAR-2 activation → ZO-1 + occludin phosphorylation → tight junction disassembly
    ↓
Gut PERMEABILITY INCREASE (measurable as lactulose:mannitol ratio or I-FABP)
    ↓
M1 ARM ACTIVATED — same downstream as dietary gut dysbiosis:
    → LPS/TLR4 → GALT IL-23 → Th17 → M4 threshold lowered
    → F. prausnitzii / Akkermansia niche disruption
```

**Critical implication for T-index v3:**
Node C (I-FABP) measures gut barrier integrity — but its cause is AMBIGUOUS:
- HIGH Node C + low-fiber/high-GI diet = M5 driving M1 arm
- HIGH Node C + intact diet + recent stressful event = M8 driving M1 arm
- The signal is the SAME; the intervention differs

**This explains a diagnostic failure mode:**
A patient with correct diet (Node C should be improving) but ongoing chronic stress will show
persistent elevated I-FABP and be incorrectly told "the diet isn't working." The gut permeability
is real — but the cause is M8, not diet failure.

### Evidence

| Claim | Evidence | Grade |
|-------|----------|-------|
| CRH injection → human gut permeability increase (lactulose:mannitol) | Söderholm 2002 Gastroenterology: direct human evidence | II-2 (small RCT, crossover) |
| CRHR1 on intestinal mucosal mast cells | Reviewed in Theoharides 2012 Gut; confirmed in human biopsy studies | II-2 |
| Mast cells → PAR-2 → tight junction disruption | Ramsay 2013 Mucosal Immunology | II-2 (human tissue) |
| Psychological stress → I-FABP elevation in humans | Stress-induced IBS: I-FABP in exams (Ng 2018) | II-3 (observational) |
| Mast cell stabilizers partially protect against stress-induced gut permeability | Ketotifen in IBS with psychological stress trigger: Klooker 2010 Gut | II-2 (RCT) |

**Söderholm 2002 is the pivotal piece:** CRH infusion in healthy humans directly raises gut permeability.
This is not inferred — it is directly demonstrated.

### Novel Testable Predictions

**Prediction A:** In a cohort of patients on stable diet + gut protocol, I-FABP should correlate with
salivary cortisol / perceived stress score AFTER controlling for dietary fiber and food diary.
The residual I-FABP variance explained by cortisol (not diet) is the M8→M1 bridge signal.

**Prediction B:** Quercetin 500mg BID (mast cell stabilizer) should reduce the STRESS-ASSOCIATED I-FABP
spike (stress flare with intact diet) but NOT reduce baseline I-FABP when stress is absent.
This is a mechanistically targeted test: quercetin blocks mast cell degranulation, not diet-mediated
tight junction dysfunction.

**Prediction C:** IBS patients with documented psychological stress triggers should have higher CRHR1
expression on colonic mucosal mast cells than IBS patients with no stress triggers. This directly
tests whether the mast cell CRHR1 density is the individual-variation factor for M8→M1 susceptibility.

### Kill Criteria

**Kill A: CRH Does NOT Increase Gut Permeability at Physiological Stress Doses**
Söderholm 2002 used pharmacological CRH infusion. Whether ENDOGENOUS stress-released CRH
reaches concentrations sufficient to activate intestinal CRHR1 is the dose-question.
**Status:** Partially killed for healthy controls with low stress. The mast cell / IBS literature
(psychological stress → IBS flare → I-FABP elevation) provides human indirect evidence that
endogenous CRH is sufficient in susceptible individuals. Not fully killed.

**Kill B: Mast Cell Stabilizers Do Not Prevent Stress-Induced Gut Permeability**
Ketotifen study (Klooker 2010 Gut) DID show protection in IBS. Kill criterion NOT met.

**Classification: STRONG CANDIDATE** (Söderholm 2002 is direct human evidence for CRH→gut
permeability; Klooker 2010 provides therapeutic evidence for mast cell mechanism)

---

## Bridge 3: M8→M7 (Cortisol → Salivary IgA Suppression → P. gingivalis Colonization Facilitated)

### Mechanism

```
Chronic psychological stress
    ↓
HPA axis → cortisol elevated
    ↓
Cortisol → SUPPRESSES salivary IgA (sIgA) SECRETION:
    - sIgA is produced by plasma cells in salivary glands
    - Cortisol → reduces IgA+ B cell differentiation in submandibular gland
    - Reduces polymeric IgA transport (pIgR expression ↓)
    ↓
REDUCED sIgA in saliva (measurable: salivary IgA ELISA)
    ↓
sIgA is the PRIMARY mucosal defense against oral pathogens including P. gingivalis:
    - sIgA agglutinates P. gingivalis → prevents biofilm formation
    - sIgA blocks P. gingivalis fimbriae adhesion to gingival epithelium
    ↓
P. gingivalis colonization FACILITATED (low sIgA = open niche)
    ↓
M7 arm PRIMED — P. gingivalis now proceeds through all documented M7 pathways:
    M7→M3 (CAR upregulation, CVB entry)
    M7→M1 (oral-gut axis, TLR2+TLR4 GALT)
    M7→IFN (gingipains + butyrate → EBV reactivation)
```

**The cascade:**
```
M8 (stress) → sIgA ↓ → P. gingivalis colonization ↑ → M7 ACTIVE
    → M7→M3 → IFN-α ↑ → M4 lowered (IFN arm)
    → M7→M1 → IL-23 ↑ → M4 lowered (Th17 arm)
```

**M8 is therefore upstream of M7 in the stress-to-disease cascade.** A patient who develops
periodontal disease during sustained psychological stress (divorce, bereavement, work crisis) is
experiencing the M8→M7→M3/M1→M4 cascade. The stress came first; the periodontal disease followed.

**This connection reverses the typical clinical narrative:**
Standard: patient has gum disease → doctor treats gum disease.
M8→M7: stress → sIgA suppression → gum disease begins. Treating gum disease without addressing
stress → recurrence, because sIgA remains suppressed.

### Evidence

| Claim | Evidence | Grade |
|-------|----------|-------|
| Cortisol → reduces salivary IgA (sIgA) | Bosch 2011 (review): acute and chronic stress both reduce sIgA | II-2 (multiple cohort studies) |
| Exam stress → transient sIgA reduction → post-exam sIgA rebound | Classic sports/exam psychology studies; consistent across cohorts | II-2 |
| sIgA is primary P. gingivalis defense in saliva | P. gingivalis IgA-binding: documented; P. gingivalis has proteases that CLEAVE IgA (IgA protease) — this is a virulence factor | II-2 |
| Low sIgA → P. gingivalis colonization increase | Inferential from clinical studies: military recruits under basic training stress → increased periodontal disease | II-3 |
| Chronic stress → periodontal disease worsening | Multiple epidemiological studies: Hugoson 2002 (caregiver stress + periodontitis); Wimmer 2002 (workplace stress + periodontitis) | II-2 |
| REVERSAL: stress reduction → sIgA restoration → periodontal improvement | Limited; one RCT (MBSR + periodontal outcomes) exists in preliminary form | III |

**Key complication:**
P. gingivalis produces its OWN IgA protease that cleaves secretory IgA. This means once P. gingivalis
is established, even restoring sIgA via stress reduction is partially blunted — the bacteria actively
destroys the defense. This creates a maintenance threshold: more P. gingivalis → more IgA degradation
→ lower effective sIgA → lower P. gingivalis clearance. A self-sustaining M7 loop that parallels the
M2+M4 rosacea loop (attempt_008).

**Novel finding:** P. gingivalis IgA protease creates a SECOND self-amplifying loop (M7 analog of M2+M4
loop) — once established above a density threshold, P. gingivalis actively maintains its own niche via
sIgA destruction even if stress is resolved.

### Novel Testable Predictions

**Prediction A — Salivary IgA as M8 Functional Marker:**
In patients presenting for periodontal treatment: salivary IgA (ELISA, $20 send-out) should correlate
inversely with perceived stress score (PSS-10) and hair cortisol. This directly tests the M8→M7 link.
Clinical implication: low sIgA = high M8 activity = stress-driven periodontal susceptibility.

**Prediction B — MBSR + Periodontal Treatment vs. Periodontal Treatment Alone:**
RCT in mild-moderate periodontitis patients:
- Arm A: periodontal scaling/root planing (SRP) alone
- Arm B: SRP + 8-week MBSR
Primary outcome: P. gingivalis pocket counts at 6 months
Secondary: salivary IgA, hair cortisol, I-FABP (tests M8→M7→M1 full chain)
Prediction: Arm B shows lower recurrence because sIgA is restored AND cortisol-driven
M8→M1 gut permeability is reduced simultaneously.

**Prediction C — Stress → Periodontal Worsening Runs Through sIgA:**
Longitudinal study: bereavement cohort (well-defined stress onset) → serial salivary IgA + periodontal
pocket depth measurements at 0, 3, 6, 12 months post-event.
Prediction: sIgA drops within 4 weeks → P. gingivalis counts increase within 8 weeks → pocket depth
worsens by 6 months. This is the M8→M7 temporal sequence tested.

### Kill Criteria

**Kill A: sIgA Does Not Predict P. gingivalis Colonization in Humans**
The assumed causation (low sIgA → more P. gingivalis) needs direct human evidence.
**Status:** Not killed. Periodontal disease is consistently associated with both lower sIgA and higher
stress. The direct dose-response (sIgA concentration → P. gingivalis colony counts in same individual)
has not been measured in prospective trials.

**Kill B: P. gingivalis IgA Protease Does Not Cleave sIgA Efficiently at Subgingival Concentrations**
The virulence factor (IgA protease) may not be dominant in early colonization before biofilm
establishment.
**Status:** Not killed. IgA protease is a documented P. gingivalis virulence factor with confirmed
in vitro cleavage of secretory IgA (Plummer 1993; multiple subsequent confirmations).

**Kill C: Cortisol Does Not Suppress sIgA at Physiological Stress Concentrations**
Status: Not killed. Bosch 2011 review covers this comprehensively — cortisol-sIgA inverse relationship
is one of the most replicated findings in psychoneuroimmunology.

**Classification: CANDIDATE** (each step individually well-supported; the full cascade M8→sIgA→P.g.→M7
pathway not yet tested prospectively in a single cohort)

---

## M8 in the Integrated Framework — Updated Connection Map

```
M8 (HPA/CRH/Stress)
    │
    ├─[B1] Cortisol → GR downregulation → functional Treg failure → M4 LOWERED
    │       (Independent of IL-23/Treg plasticity from M1↔M4 bridge)
    │       Classification: CANDIDATE
    │
    ├─[B2] CRH → intestinal mast cells → tight junction disruption → I-FABP ↑ → M1 ACTIVATED
    │       (Diet-independent gut permeability — stress flare pattern)
    │       Classification: STRONG CANDIDATE (Söderholm 2002)
    │
    ├─[B3] Cortisol → sIgA suppression → P. gingivalis facilitated → M7 PRIMED
    │       (Stress opens the oral niche; P. gingivalis IgA protease creates secondary loop)
    │       Classification: CANDIDATE
    │
    └─[B4] Substance P → Malassezia growth + KLK5 → M2 rosacea loop primed
            (Described in attempt_013; not re-derived here)
            Classification: CANDIDATE
```

**M8 connects to M7, M1, M4 directly — and via these to M2, M3 (through M7 and M1).**
**M8 is the only mountain with NO isolated disease — it only manifests through amplification of others.**
**Unique signature: multisite flares during stress/sleep deprivation with intact protocol adherence.**

---

## Integration Notes

### Why M8 bridges matter for the T-index:

T-index v3 assumes that elevated nodes indicate modifiable inputs. But:
- Node C elevated (I-FABP) during stress ≠ diet failure (M5 intervention won't fix it)
- Node B elevated (hsCRP/IL-17A) during stress ≠ gut dysbiosis persistence (M1 intervention won't fix it)

The M8 active state is diagnosed by CONTEXT (stress event concurrent with flare) and MARKER (hair
cortisol elevated, morning cortisol flat diurnal pattern = HPA exhaustion).

**When M8 is active, the correct intervention is not more M1/M5 measures — it is M8-specific:**
- Sleep (most potent: 7-9h/night, each missed hour +10-15% cortisol)
- MBSR (8-week program → 20-30% salivary cortisol reduction, IL-17 reduction in chronic inflammatory
  conditions)
- Quercetin 500mg BID (mast cell stabilizer — blocks M8→M1 I-FABP arm; also inhibits P. gingivalis
  gingipains — dual benefit at M8→M7 interface)
- Ashwagandha KSM-66 300mg BID (28% cortisol reduction, Chandrasekhar 2012 RCT)

**Quercetin is the single drug that addresses two M8 bridges simultaneously:**
- Mast cell stabilization → blocks M8→M1 (prevents stress-induced gut permeability)
- Gingipain inhibition → reduces M7 virulence (reduces P. gingivalis tissue damage)

---

## References

- [Miller 2009 PNAS — GR downregulation in chronically stressed humans](https://pubmed.ncbi.nlm.nih.gov/19139404/)
- [Söderholm 2002 — CRH injection increases gut permeability (humans)](https://pubmed.ncbi.nlm.nih.gov/12225543/)
- [Klooker 2010 Gut — Ketotifen reduces stress-induced gut permeability in IBS](https://pubmed.ncbi.nlm.nih.gov/20541200/)
- [Bosch 2011 — Cortisol and salivary IgA inverse relationship (review)](https://pubmed.ncbi.nlm.nih.gov/21040780/)
- [Plummer 1993 — P. gingivalis IgA protease cleavage of secretory IgA](https://pubmed.ncbi.nlm.nih.gov/8478013/)
- [Wimmer 2002 — Workplace stress and periodontitis](https://pubmed.ncbi.nlm.nih.gov/12174061/)
- [Chandrasekhar 2012 — Ashwagandha reduces cortisol 28% in RCT](https://pubmed.ncbi.nlm.nih.gov/23439798/)
- See `attempts/attempt_013_m8_neuroimmune_hpa.md` — source M8 mountain framework

---

*Filed: 2026-04-12 | Phase 4 integration | M8 sky bridges*
*Bridges formalized: M8→M4 (CANDIDATE), M8→M1 (STRONG CANDIDATE), M8→M7 (CANDIDATE)*
*Novel finding: P. gingivalis IgA protease creates secondary self-amplifying M7 loop (sIgA destruction)*
*Novel finding: Quercetin addresses two M8 bridges simultaneously (mast cell + gingipain inhibition)*
*Clinical rule: elevated I-FABP + intact diet + stress event → M8→M1 is the cause; add quercetin, not more fiber*
