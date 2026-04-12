# Implicit Kills Analysis — Dysbiosis Kill Matrix
## Theory Instance | 2026-04-11

> "Implicit kill" = a prediction in the kill matrix where existing published data already falsifies
> it, but numerics didn't call it out explicitly. Distinct from explicit kills (predictions that
> were tested and failed) and untested predictions (not yet engaged).
>
> Three categories: ASSAY KILLS (biology sound, measurement dead), TECHNICAL KILLS
> (hypothesis intact, detection method dead), MECHANISM KILLS (mechanism superseded or falsified).

---

## Category 1 — Assay Kills

### IK-1: P1.2 — Zonulin as gut permeability marker

**Prediction:** Zonulin elevation correlates with dysbiosis-linked disease.

**Kill source:** Zhang et al. 2021 — the Immundiagnostik commercial ELISA (most widely used) detects
**complement C3**, not the actual zonulin protein (FAM55B gene product). Published gut permeability
data using this kit likely measures a non-specific inflammatory marker.

**What this kills:** The specific biomarker P1.2 is built on. Not the underlying leaky gut hypothesis.

**What survives:**
- Gut permeability as a concept: biologically sound
- P1.3 (butyrate producers), P1.6 (LPS→TLR4): unaffected
- The L:M ratio test (gold standard functional test) still works
- FABP2 + LBP (blood-based alternatives) still valid

**Implicit kill score:** HIGH — this is already flagged 2/3 AGAINST in kill matrix (Run 001), but
the full extent (assay is entirely wrong, not just controversial) wasn't stated explicitly.

**Action:** Any previous "zonulin" results from Immundiagnostik kit should be disregarded as gut
permeability data. L:M ratio (Genova, ~$150) is the valid replacement.

---

### IK-2: Standard IgG Serology for CVB Persistence

**Prediction (implicit):** CVB IgG serology could indicate current viral persistence in islets.

**Kill source:** The nature of CVB serology + 5'UTR deletion biology.
- IgG = past exposure antibody. Persists for decades after acute-resolved infection.
- A positive CVB IgG titer in a T1DM patient means: they had CVB infection at some point.
  It does NOT mean CVB is currently persisting in islets.
- The 5'UTR-deleted variant that persists may have REDUCED immunogenicity (deleted 5'UTR
  affects IRES-based translation → possibly lower antigen production → blunted antibody response)
- Result: IgG positive = prior exposure (ubiquitous in adults); IgG negative = unlikely CVB
  involvement (useful only as exclusion); no IgG result can confirm active persistence.

**What this kills:** Serology as a monitoring tool for current CVB activity. This is NOT mentioned
in the kill matrix because numerics correctly focused on IFN-α2 Simoa as the proxy. But the
implicit assumption that "antibody titer correlates with active infection" — which appears in some
patient-facing literature — is dead.

**What survives:**
- M3 core hypothesis: entirely intact
- IFN-α2 Simoa: remains the best available proxy for ongoing viral replication
- ISG 4-gene panel (MX1/IFIT1/OAS1/RSAD2): intact
- CXCL10 screen: intact

**Implicit kill score:** MODERATE — not in the kill matrix but a common misuse of serology in
clinical translation of CVB research.

---

## Category 2 — Technical Kills

### IK-3: P3.5 — Virome-Enriched Sequencing of TinyHealth FASTQ for CVB

**Prediction:** Virome-enriched sequencing reveals disease-associated viral signatures missed by
standard shotgun metagenomics.

**Kill source:** CVB biology + stool metagenomics methodology (confirmed in Run 002 after
TinyHealth shot-gun metagenomics correction).

**Three independent reasons CVB is undetectable in TinyHealth FASTQ:**
1. **RNA virus, DNA assay**: CVB is a (+)ssRNA virus. Shotgun metagenomics is DNA-based.
   CVB genomic RNA is not captured without a specific RNA extraction + RT-PCR step.
2. **Organ-specific, not fecal**: CVB persists in pancreatic islet beta cells, not in the gut
   lumen. It is NOT shed in stool at detectable levels (unlike, e.g., gut-tropic enteroviruses
   acutely). The stool is looking in the wrong place.
3. **5'UTR deletion**: Even if RNA were captured, the standard CVB genome databases have the
   full 5'UTR sequence. The 5'UTR-deleted variant would match poorly or not at all, appearing
   as a partial/novel sequence rather than CVB.

**What this kills:** Using TinyHealth FASTQ to test M3 (CVB persistence hypothesis). This cannot
be done with the available assay.

**What survives:** P3.5 as a general prediction is NOT killed — virome-enriched sequencing FROM
ISLET TISSUE would reveal CVB signals (Krogvold 2015, Richardson 2021). The prediction
holds for the right tissue type with the right preparation.

**Collateral survival:** TinyHealth FASTQ CAN detect:
- CrAssphage (phageome proxy for Bacteroides density control)
- Caudovirales contigs (IBD phageome pattern, via VirSorter2)
- Gut-tropic viral elements (not islet-tropic)

**Implicit kill score:** HIGH — this was the primary correction made during the session (TinyHealth
is shotgun metagenomics, not virome-enriched; CVB still undetectable for all three reasons above).

---

### IK-4: P6.5 — Vaginal Seeding Normalizes Microbiome After C-Section

**Prediction:** Vaginal seeding after C-section normalizes microbiome trajectory.

**Kill source:** Dominguez-Bello 2016 follow-up data; subsequent independent replications.
- Partial transfer: some vaginal taxa do transfer, but the full composition is not restored
- Incomplete normalization: at age 1+ year, seeded infants still differ from vaginally-born
- GBS safety concern: if mother is GBS-positive (Group B Streptococcus, ~20% of pregnant women),
  vaginal seeding would transfer a pathogen — potentially dangerous
- Current regulatory status (2026): not FDA-approved, not standard of care in any country

**What this kills:** Vaginal seeding as a validated clinical intervention. Not as a hypothesis —
the principle (oral microbiome inoculates neonatal gut) is sound, but the specific method is
too imprecise and has safety constraints that limit implementation.

**What survives:** M6 core prediction (P6.1-P6.4 all unaffected). The early-life assembly
window hypothesis is robust; only the intervention method is technically limited.

**Implicit kill score:** MODERATE — already flagged as "contested" in kill matrix P6.5, but the
full extent of the safety constraint (GBS transfer risk affects ~20% of births) wasn't explicit.

---

## Category 3 — Mechanism Kills

### IK-5: M3+M7 Bridge — Systemic Th17 Mechanism (SUPERSEDED)

**Original mechanism (Phase 1 numerics construction):**
```
P. gingivalis (oral) → systemic Th17 elevation → IL-17 reaches islets via circulation
→ amplifies CVB-driven beta cell damage
```

**Kill source:** PMC7305306 (Graves lab 2020) — found during theory audit, missed by numerics.
P. gingivalis physically TRANSLOCATES to pancreatic islets in mice and humans, locating
intranuclearly in beta cells. Bihormonal cell emergence (beta cell dedifferentiation) correlates
with P. gingivalis presence in islets.

**What this kills:** The SYSTEMIC mechanism as the REQUIRED pathway. It is not that systemic
Th17 effects cannot occur — they likely do — but the LOCAL mechanism is now:
- Mechanistically stronger (no systemic dilution required)
- Empirically supported (PMC7305306 is data, not construction)
- More testable (nPOD dual IHC: same tissue sections can show co-localization)

**Precise statement of kill:** The claim that systemic Th17 elevation is the DOMINANT mechanism
linking P. gingivalis to CVB-T1DM bridge is superseded. The dominant mechanism is local islet
co-infection with direct TLR2 activation and local IL-17A production.

**What survives:** M7 (oral dysbiosis) as a mountain — strengthened, not killed.
The bridge M3+M7 — strengthened, not killed.
Two independent synergy mechanisms now confirmed (Th17 local + CAR upregulation).

**Implicit kill score:** HIGH — the original mechanism construction in attempt_002 was based
on the systemic model. That model is not published in the literature and is now secondary
to the local model which HAS empirical support.

---

### IK-6: P.gingivalis → CAR Degradation → Reduced CVB Entry (FALSIFIED)

**Potential kill tested:** Gingipain proteolysis of CAR (Coxsackievirus and Adenovirus Receptor)
might REDUCE CVB entry into beta cells → P. gingivalis and CVB would be ANTAGONISTIC →
bridge falsified.

**Kill source:** PMC5129002 — CAR expression is UPREGULATED by proinflammatory cytokines
(IL-1β, IFN-γ, TNF-α) in T1DM islets. Net effect:

| Effect | Direction |
|--------|-----------|
| Gingipain degrades CAR locally | ↓ CVB entry (spatially limited) |
| P. gingivalis LPS → IL-1β, TNF-α → CAR upregulation | ↑ CVB entry (diffuse, islet-wide) |

The indirect cytokine-driven upregulation is dominant (wider spatial reach, documented in T1DM).

**Result:** NOT a kill. The potential kill was FALSIFIED — the bridge is STRENGTHENED.
P. gingivalis likely INCREASES beta cell CVB susceptibility via CAR upregulation.

**Implicit kill score:** RESOLVED — this potential kill was explicitly tested (attempt_002_car_update.md).
Included here for completeness as the most important potential kill that was tested and failed.

---

## Summary Table

| Kill ID | Prediction | Kill Type | Kill Status | Biology Survives? |
|---------|------------|-----------|-------------|-------------------|
| IK-1 | P1.2 Zonulin as marker | Assay kill | CONFIRMED — kit measures C3 | Yes — L:M ratio is valid |
| IK-2 | CVB IgG serology = active persistence | Assay kill | CONFIRMED — serology measures past exposure | Yes — IFN-α2 Simoa is valid |
| IK-3 | P3.5 CVB in TinyHealth FASTQ | Technical kill | CONFIRMED — RNA virus, wrong tissue, 5'UTR deletion | Yes — ISG panel, Simoa still valid |
| IK-4 | P6.5 Vaginal seeding normalizes | Technical kill | PARTIAL — incomplete normalization, GBS safety constraint | Yes — M6 core intact |
| IK-5 | Systemic Th17 as dominant M3+M7 mechanism | Mechanism kill | SUPERSEDED by local islet model | Yes — bridge strengthened |
| IK-6 | P. gingivalis → CAR degradation → anti-CVB | Mechanism kill (potential) | FALSIFIED — CAR upregulated, not blocked | Yes — bridge strengthened |

---

## What the Implicit Kills Tell Us

**Pattern 1: Assay invalidation is concentrated in M1 and M3**
Both mountains have commonly-used assays that don't measure what they claim to measure.
Zonulin (M1) measures C3. CVB serology (M3) measures past exposure. This is not a coincidence —
both fields (functional gut medicine, viral autoimmunity) moved faster than assay validation.
The biology is real; the measurement tools are lagging.

**Pattern 2: Technical kills don't kill hypotheses**
CVB is undetectable in TinyHealth FASTQ. This says nothing about whether CVB persists in islets.
The kill is about the assay, not the biology. The right assay (Simoa, ISG panel) is available.

**Pattern 3: The M3+M7 bridge survives all tested potential kills**
Three potential kills were tested: (1) bridge not in literature → confirmed novel, (2) CAR
degradation → opposite effect found, (3) systemic mechanism required → local mechanism found
and is stronger. Each potential kill strengthened rather than killed the bridge. This pattern is
consistent with a robust finding, but also consistent with motivated reasoning — which is why
the nPOD co-localization test remains the decisive falsification target.

**Pattern 4: The real frontier is M4**
No implicit kills in M4. Nothing has been tested. No assay exists. This is not because M4 is
protected from falsification — it's because the methods don't exist yet. THE WALL is not an
implicit kill problem; it's a measurement invention problem.

---

## Revised Action Priorities (Post-Implicit-Kill)

1. **Discard any existing "zonulin" results** if from Immundiagnostik kit. Do not use as evidence
   for or against leaky gut. Order L:M ratio (Genova) if gut permeability is clinically relevant.

2. **Discard CVB IgG serology** as a monitoring tool for persistence. It answers "did this person
   ever have CVB" — not useful for the M3 question. CXCL10 → IFN-α2 Simoa is the monitoring
   cascade.

3. **Do not attempt CVB detection from TinyHealth FASTQ.** The phageome (CrAssphage, Caudovirales)
   IS detectable and is worthwhile. Viral profiling of the gut from this dataset is about gut
   phages, not islet-tropic enteroviruses.

4. **Treat M3+M7 local islet co-infection model as the working mechanism.** The systemic Th17
   narrative in attempt_002_m3m7_co_conspiracy.md is superseded. The local model in
   attempt_002_theory_audit.md is the current operative mechanism.

5. **The nPOD dual IHC test remains the decisive falsification.** No implicit kill analysis can
   substitute for the co-localization data. Graves + Richardson collaboration is the target.

---

## What Is NOT Killed

To be explicit about the boundaries:

- **M1 biology** (gut permeability → systemic LPS → inflammatory tone): Not killed. Assay is.
- **M3 core** (CVB persistence in T1DM islets drives IFN-α → beta cell destruction): Not killed.
- **M7** (P. gingivalis reaches islets, causes local damage): Strengthened by PMC7305306.
- **M3+M7 bridge**: Strengthened, not killed.
- **M4 threshold** (THE WALL): Cannot be killed yet — no assay exists to test it.
- **M5 substrate shift**: Strongest mountain. No implicit kills found.
- **T-index v2**: Not killed — the zinc×D interaction (VDR zinc finger) is a biological
  prediction from structure. Cannot be implicitly killed by existing literature.

---

*Theory instance: implicit kills analysis complete. Filed 2026-04-11.*
*Strongest implicit kills: zonulin assay (IK-1) and CVB stool detection (IK-3).*
*No predictions killed that affect the main mechanistic conclusions.*
*M3+M7 bridge survives all tested kills. nPOD dual IHC remains the decisive test.*
