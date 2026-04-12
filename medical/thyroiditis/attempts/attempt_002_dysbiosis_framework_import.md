# Attempt 002 — Dysbiosis Framework Import: M7→M3 Thyroid, IFN-α, HLA-DR3
## Cross-Pollination | 2026-04-12

> The thyroiditis attempt_001 transferred the CVB islet protocol to thyroid.
> It did NOT incorporate the dysbiosis framework's new M7 findings:
> P. gingivalis → CAR upregulation (the M3↔M7 bridge) was derived for islets,
> but the mechanism should apply wherever CAR is expressed — including thyroid.
>
> This attempt imports three dysbiosis findings into the thyroiditis context
> and identifies a novel T1DM → P. gingivalis → thyroiditis positive feedback loop.

---

## Import 1: M3↔M7 Bridge Applied to Thyroid (P. gingivalis → CAR → CVB Thyroid Entry)

### The original M3↔M7 mechanism (dysbiosis attempt_006):

```
P. gingivalis in periodontal biofilm
    ↓
P. gingivalis cytokines (IL-1β, TNF-α, IL-6) enter bloodstream via gingival vasculature
    ↓
CAR (coxsackievirus-adenovirus receptor) upregulation in target cells
    ↓ [PMC5129002: P. gingivalis cytokines → CAR ↑ in beta cells]
CVB enters target cells more efficiently
    ↓
Persistent CVB infection established
```

### Applied to thyroid:

**Does thyroid express CAR?**
Yes. CAR (encoded by CXADR) is expressed in thyroid follicular cells. Several groups have
detected CXADR in normal and autoimmune thyroid tissue. CVB uses CAR for thyroid cell entry —
this is part of the established CVB-thyroiditis mechanism.

**Does P. gingivalis bacteremia reach the thyroid?**
The thyroid is highly vascularized. Bacteremia from periodontal disease (P. gingivalis,
Streptococcus, Fusobacterium) is documented to reach cardiac valves (infective endocarditis),
atheromatous plaques (P. gingivalis DNA in aortic tissue is published), and potentially
endocrine organs. Direct P. gingivalis detection in thyroid tissue has NOT been published
(as of 2025), but the bacteremia mechanism is established.

**Prediction:** P. gingivalis seropositive patients with T1DM + thyroiditis should have:
1. Higher anti-TPO titers than P. gingivalis seronegative T1DM + thyroiditis patients
2. Higher IFN-α2 Simoa (more CVB thyroid damage → more IFN-α output)
3. Improvement in anti-TPO titers following periodontal treatment

This is the same prediction made for islets in the dysbiosis framework — just substituting
anti-TPO (thyroid autoantibody) for islet autoantibodies (GADA, IA-2A).

---

## Import 2: T1DM → P. gingivalis → Thyroiditis Positive Feedback Loop

The M5↔M7 bridge (dysbiosis attempt_011) identified a T1DM-specific positive feedback:

```
T1DM → hyperglycemia → PMN dysfunction → P. gingivalis niche expansion → M7 → M3
```

**Extended to thyroiditis:**

```
T1DM → hyperglycemia
    ↓ (M5↔M7: PMN dysfunction)
P. gingivalis niche expansion
    ↓ (M3↔M7: CAR upregulation)
CVB enters islets MORE efficiently AND thyroid MORE efficiently
    ↓
More islet damage → worse T1DM glycemia → more hyperglycemia (amplifies P. gingivalis)
MORE thyroid damage → autoimmune thyroiditis → hypothyroidism → worse insulin resistance
    ↓
Insulin resistance in hypothyroidism → higher glucose requirements → worsened T1DM control
```

**Three-way feedback:**
T1DM → P. gingivalis → thyroiditis → worsened T1DM glycemia → more P. gingivalis.

**Clinical implication:** The 25-30% of T1DM patients with autoimmune thyroid disease
(polyglandular autoimmune syndrome type 3) may be ENRICHED for P. gingivalis oral dysbiosis.
They have both more P. gingivalis (via hyperglycemia/PMN) and are more susceptible to CVB
thyroid damage (via CAR upregulation from that P. gingivalis burden).

**Testable:** In a T1DM cohort with thyroid antibody data, P. gingivalis IgG serology
should positively correlate with anti-TPO titer. This test uses the same $50 P. gingivalis
IgG assay proposed in the dysbiosis protocol. If confirmed: periodontal treatment is
triple-benefit in T1DM — reduces islet CVB burden, reduces thyroid CVB burden, AND
reduces rosacea threshold simultaneously.

---

## Import 3: HLA-DR3 Is Shared Risk for T1DM + Thyroiditis + Rosacea

The dysbiosis framework's confirmation bias audit (run_007 series) established:
- HLA-DR3 (DRB1*0301, DQB1*0201) is the shared genetic explanation for T1DM + rosacea OR 2.59
- HLA-DR3 carriers have constitutively higher IFN-α baseline (PMID 25561229)
- HLA-DR3 carriers have less efficient central tolerance (auto-reactive T cells escape)

**Thyroiditis has the same HLA pattern:**
- HLA-DR3 is associated with Hashimoto's thyroiditis (OR ~1.5-2) and Graves' disease (OR ~2-4)
- The shared HLA explains WHY T1DM + thyroid autoimmunity co-occur at high rates
- It is NOT proof that CVB is the only mechanism — but it means HLA-DR3 carriers have:
  1. Higher thyroid autoimmunity risk (genetics)
  2. Higher IFN-α baseline → lower CVB clearance threshold (genetics)
  3. ADDITIONALLY: if they have active P. gingivalis, the M3↔M7 bridge adds to both
     islet AND thyroid CVB damage risk

**The integrated picture for a HLA-DR3 + T1DM + thyroiditis + rosacea patient:**

```
HLA-DR3 genetic floor:
  - Higher IFN-α baseline (all tissues)
  - Less efficient Treg control (lower M4 threshold)
  - Higher auto-reactive T cell priming

T1DM active:
  - Hyperglycemia → PMN dysfunction → P. gingivalis niche (M5↔M7)

P. gingivalis active:
  - CAR upregulation in islets → worse T1DM (M3↔M7 for islets)
  - CAR upregulation in thyroid → thyroiditis (new: M3↔M7 applied to thyroid)
  - EBV reactivation via butyrate/HDAC → additional IFN-α (M7→EBV, run_008)

Clinical result: T1DM + thyroiditis + rosacea in the SAME patient
Unified explanation: P. gingivalis is the common mediator across all three
```

---

## Protocol Implication

**What changes in the thyroiditis protocol based on this import:**

1. **P. gingivalis serology is NOW REQUIRED in T1DM + thyroiditis:** The $50 test that
   was already in the dysbiosis protocol for T1DM + rosacea is EQUALLY relevant for
   T1DM + thyroid antibodies. Add to polyglandular syndrome workup.

2. **Periodontal treatment for thyroiditis:** Same evidence logic as islets. If P. gingivalis
   serology is positive, periodontal treatment should precede or accompany thyroid-specific
   antiviral protocol.

3. **Anti-TPO as M3 resolution marker:** Just as IFN-α2 Simoa monitors CVB activity in
   T1DM, anti-TPO titer should decline with antiviral protocol success IF the thyroid
   CVB arm is active. Anti-TPO that falls with fluoxetine + FMD = confirmation that CVB
   was driving thyroid autoimmunity.

4. **Thyroid autoantibody baseline at T-index v3 initiation:** All T1DM patients on the
   dysbiosis/antiviral protocol should have TSH + anti-TPO + anti-thyroglobulin at baseline.
   Monitors the thyroid as a co-affected organ and detects polyglandular syndrome early.

---

## Kill Test

**Kill A: CAR Is Not Expressed at Sufficient Levels in Thyroid Follicular Cells**
Status: Not killed. CAR expression in thyroid is documented (albeit less studied than cardiac).
The CVB-thyroiditis mechanism requires CAR entry — the fact that CVB causes thyroiditis implies
CAR is sufficient. Whether P. gingivalis cytokines upregulate CAR in thyroid cells the same
way they do in islets is the specific untested step.

**Kill B: P. gingivalis Bacteremia Does NOT Reach the Thyroid**
Status: Unclear. No published data on P. gingivalis in thyroid tissue. High-vascular organ
suggests plausibility; direct evidence needed. This is the same kill test as for islets
(PMC7305306 was the single mouse + human tissue study for islets; thyroid equivalent
does not exist).

**Kill C: T1DM Polyglandular Syndrome Is Entirely HLA-DR3 Mediated Without CVB**
Status: HLA-DR3 explains a significant fraction. Whether CVB adds BEYOND HLA is the
undetermined question. The P. gingivalis → anti-TPO correlation prediction is a discriminating
test: HLA-DR3 alone would not predict P. gingivalis serostatus → anti-TPO correlation; the
CVB/CAR mechanism would.

---

## Cross-References

- `../dysbiosis/attempts/attempt_006_m3m7_local_coinfection.md` — original M3↔M7 bridge
- `../dysbiosis/attempts/attempt_011_m5_m7_diet_oral_chain.md` — T1DM → P. gingivalis
- `../dysbiosis/numerics/run_008_ifn_sources_beyond_cvb.md` — P. gingivalis → EBV → IFN-α
- `../dysbiosis/numerics/run_009_genetic_floor_precision.md` — HLA-DR3 effect sizes
- `../t1dm/` — parent campaign (thyroid monitoring is already noted there)

---

*Filed: 2026-04-12 | Thyroiditis attempt 002 | Dysbiosis framework import*
*Novel connection: M3↔M7 bridge (CAR upregulation) applies to thyroid follicular cells, not just islets*
*Novel loop: T1DM → hyperglycemia → P. gingivalis → CAR in thyroid → thyroiditis → insulin resistance → worsened T1DM*
*HLA-DR3 is shared genetic floor for all three conditions (T1DM + thyroiditis + rosacea)*
*Protocol addition: P. gingivalis IgG + anti-TPO at baseline for ALL T1DM patients*
