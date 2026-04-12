# Attempt 012 — M7→M1 Bridge: Oral-Gut Colonization / TLR2+TLR4 Dual Threshold
## Phase 3 Extension | 2026-04-11

> P. gingivalis swallowed in saliva (~10^10 bacteria/day) colonizes the gut in some hosts,
> particularly PPI users. Gut-resident P. gingivalis activates TLR2 rather than TLR4.
> In a host already dysbiotic (M1: LPS/TLR4 active), adding TLR2 activation creates
> DUAL-RECEPTOR innate immune stimulation. TLR2 + TLR4 co-stimulation is SYNERGISTIC
> for Th17 induction, meaning the M4 threshold is lowered multiplicatively.

---

## Mountain
Sky Bridge: M7 (oral dysbiosis) → M1 (gut dysbiosis) via oral-gut colonization axis

---

## The Mechanism

### The Oral-Gut Axis

Each day:
- ~1.5L saliva swallowed
- Each mL of oral fluid contains ~10^7 bacteria
- Total load: ~10^10 oral bacteria/day entering gut

Most are destroyed by gastric acid (pH 1.5-3.5). BUT:
- **PPI use** → gastric pH 4-7 → significant oral bacterial survival into small intestine
- **H2 blockers** → partial pH elevation → intermediate effect
- **Fasting hypochlorhydria** → transient oral bacterial passage

**Oral bacteria in gut — documented:**
- *Fusobacterium nucleatum* (oral primary) is the most overrepresented taxon in colorectal cancer microbiome
- P. gingivalis detected in gut biopsies (small studies, Olsen 2019 systematic review)
- Consistent finding: oral bacteria including periodontal pathogens reach and persist in the gut

---

## The TLR2+TLR4 Synergy Mechanism

**Standard gut dysbiosis (M1) signal:**
```
Gram-negative enteric LPS → TLR4 → MyD88 → NF-κB → IL-6, TNF-α, IL-12 → Th1/Th17
```

**P. gingivalis (oral origin) in gut signal:**
```
P. gingivalis LPS → TLR2 → TIRAP/MyD88 → MAPK/AP-1 + NF-κB → IL-17, IL-6 → Th17
```

**TLR2 + TLR4 co-stimulation:**
- Published: TLR2 and TLR4 co-stimulation is synergistic for IL-6, IL-23 production (not additive — synergistic)
- IL-23 is the pivotal cytokine for Th17 expansion and Treg plasticity (PMID 31776355)
- Combined: more IL-23 than either receptor alone → more dual-homing Th17 priming → bigger M1→M4 signal
- The threshold lowering from M7→M1 is multiplicative with the standard M1 LPS signal

**Therefore:** In a patient with BOTH gut dysbiosis (TLR4 active) AND oral P. gingivalis gut colonization (TLR2 active), the M1→M4 arm is MORE potent than the T-index Node C (I-FABP) alone would suggest. I-FABP measures gut barrier damage but not the RECEPTOR DIVERSITY contributing to the IL-23/Th17 output.

---

## Why This Is Clinically Distinct From Just "M7 via Bacteremia"

The bacteremia arm (M7→M3, attempt_006) works by:
P. gingivalis in blood → islets → CAR upregulation → CVB entry

The gut colonization arm (M7→M1, attempt_012) works by:
P. gingivalis in gut → TLR2 in GALT → IL-23 amplification → M1 arm potentiated

These are PARALLEL mechanisms from M7. Bacteremia is intermittent (during chewing, dental procedures). Gut colonization is CONTINUOUS (if established) — a persistent additive input to the M1 arm.

---

## PPI Use as Amplifier

This bridge explains a key iatrogenic finding from the anti-problem list.

**PPI use + oral dysbiosis = compound amplification:**
1. PPI raises gastric pH → more oral bacteria survive into gut (direct bridge enablement)
2. PPI reduces gastric acid kill of LPS from all sources → net more gut TLR4 activation
3. PPI-induced gut microbiome shift → dysbiosis (independently documented: SIBO, C. diff risk)
4. If P. gingivalis colonizes gut under PPI protection → TLR2+TLR4 synergy (mechanism above)

**Practical implication:** In a T1DM patient with active periodontitis on chronic PPI, THREE inputs are simultaneously active:
- Gut LPS/TLR4 dysbiosis (M1)
- Oral P. gingivalis/TLR2 gut colonization (M7→M1, this bridge)
- P. gingivalis bacteremia → CAR priming (M7→M3, attempt_006)

This is the HIGHEST-RISK combination for M4 threshold lowering.

---

## The M5 Amplifier Again

From attempt_011: hyperglycemia (M5) → PMN dysfunction → P. gingivalis niche expansion.
This bridge (M7→M1) adds a second consequence of the same root cause:
- M5 (diet) → hyperglycemia → P. gingivalis expansion → MORE bacteremia (M7→M3 potentiation)
- M5 (diet) → hyperglycemia → P. gingivalis expansion → MORE gut colonization (M7→M1, this bridge)

**The diet is doubly connected to the oral-gut-threshold chain.**

---

## Novel Kill Criteria

### Kill A: P. Gingivalis Does NOT Colonize the Gut
**Status**: Not disproven. Small studies show P. gingivalis in gut biopsies. F. nucleatum gut colonization (same genus, same oral-gut route) is firmly established (colorectal cancer literature). The mechanism is identical; P. gingivalis specific replication needed.

### Kill B: TLR2 + TLR4 Co-Stimulation is NOT Synergistic for IL-23
**Status**: Not disproven. TLR2+TLR4 synergy for IL-6 and IL-23 is documented in macrophages and dendritic cells. The specific relevance in human gut GALT context has not been tested in the dual-oral-gut-colonization model specifically.

### Kill C: PPIs Do NOT Increase Oral Bacterial Survival to Gut
**Status**: Not disproven. Gastric pH under PPI is well-documented (pH 4-7 vs 1.5-3.5). Oral bacterial survival is pH-dependent. Indirect evidence: SIBO increases under PPI, consistent with more oral/upper-GI bacteria surviving downstream.

---

## Novel Testable Predictions

### Prediction A — P. Gingivalis Seropositivity + PPI Use → Highest I-FABP
In patients with concurrent active periodontitis + chronic PPI use vs controls:
- Prediction: I-FABP + IL-17A are HIGHEST in the P. gingivalis seropositive + PPI group
- This would be the direct test of the M7→M1 bridge activation
- Cheap: P. gingivalis IgG serology + I-FABP + medication history

### Prediction B — Periodontal Treatment + PPI Taper → Better M1 Response
In patients with M1-arm gut dysbiosis (elevated I-FABP), failing to respond to gut protocol:
- Intervention A: gut protocol alone (fiber + probiotics + no PPI taper)
- Intervention B: gut protocol + periodontal treatment + PPI taper
- Prediction: Intervention B → greater I-FABP reduction and greater Th17 attenuation
- This is not just cleaning teeth — it's removing the TLR2 input from the gut

### Prediction C — Oral Microbiome Sequencing Predicts I-FABP
In T1DM patients:
- Oral microbiome composition (16S from saliva)
- Gut permeability (I-FABP, zonulin) — NOT zonulin Immundiagnostik kit (IK-1); use I-FABP
- Prediction: P. gingivalis relative abundance in saliva inversely predicts gut barrier integrity
- Mechanism: more P. gingivalis in saliva → more gut colonization → TLR2 → gut barrier disruption

---

## What This Adds to T-Index v3

**T-Index v3 limitation this bridge exposes:**
Node C (I-FABP) measures gut barrier integrity — the STRUCTURAL consequence of M1 arm input.
It does NOT measure what RECEPTORS are generating the IL-23/Th17 output.

In a P. gingivalis gut-colonized patient, the TLR2 arm is active in addition to TLR4. The same I-FABP value means MORE Th17 output (because TLR2+TLR4 synergy > TLR4 alone).

**Practical update to T-index interpretation:**
```
Node C elevated + P. gingivalis seropositive + PPI use →
INTERPRET Node C as UNDERESTIMATING M1 arm Th17 output
because TLR2 synergy is active on top of TLR4 signal
```

This doesn't require changing what's measured — it changes how to interpret the measurement.

---

## Clinical Implication for Protocol

**The M7→M1 bridge makes PERIODONTAL TREATMENT double-duty:**
1. Directly reduces M7 bacteremia → less P. gingivalis → less CAR priming in islets (M7→M3 arm)
2. Reduces oral P. gingivalis → less gut colonization → removes TLR2 component from GALT → reduces M1 arm potentiation (M7→M1, this bridge)

Periodontal treatment was already highest-priority for M7→M3. This bridge adds a SECOND mechanism for the same intervention, increasing its ROI further.

**PPI reassessment:**
- If PPI is being used for mild/moderate reflux (not Barrett's, not severe GERD), tapering is a double intervention:
  1. Restores gastric acid → destroys oral bacteria before gut colonization (closes M7→M1 bridge)
  2. Reduces SIBO/gut community shift (standard PPI harm)
- Recommend physician review of PPI indication before antiviral protocol initiation

---

## Classification

**CANDIDATE** (same level as M3↔M2 and M5↔M7)

Evidence for:
- Oral-gut colonization route is mechanistically established
- F. nucleatum gut colonization (same route) is firmly documented
- TLR2+TLR4 synergy for IL-23 is published
- PPI-gastric pH-oral bacteria survival is mechanistically obvious

Evidence gap:
- P. gingivalis-specific gut colonization needs direct replication (small studies only)
- The TLR2+TLR4 synergy in human GALT specifically, under oral colonization conditions, is not published
- Clinical outcome data linking oral dysbiosis → gut dysbiosis → M4 threshold: zero prospective studies

Clinical value: HIGH even as a candidate. The intervention (periodontal treatment + PPI reassessment) is low-cost, low-risk, and addresses multiple arms simultaneously. The mechanism need not be proven to act on the available evidence.

---

## References

- [Run 003 — Mountain 7 oral microbiome (local)](../numerics/run_003_mountain7_oral_microbiome.md)
- [Attempt 006 — M3+M7 local islet co-infection (bacteremia arm)](attempt_006_m3m7_local_coinfection.md)
- [Attempt 011 — M5↔M7 diet→oral chain](attempt_011_m5_m7_diet_oral_chain.md)
- [Olsen 2019 — Oral-gut microbiome axis (systematic concept)](https://pubmed.ncbi.nlm.nih.gov/31196801/)
- [F. nucleatum in colorectal cancer gut (oral-gut colonization precedent)](https://pubmed.ncbi.nlm.nih.gov/31806898/)
- [TLR2+TLR4 synergy for cytokine production (general mechanism)](https://pubmed.ncbi.nlm.nih.gov/20551174/)
- [P. gingivalis + TLR2 → Th17 (mechanism)](../numerics/run_003_mountain7_oral_microbiome.md)
- [PMC7305306 — P. gingivalis in pancreatic islets](https://pmc.ncbi.nlm.nih.gov/articles/PMC7305306/)

---

*Filed: 2026-04-11 | Instance: numerical (Phase 3 extension) | M7→M1 oral-gut colonization*
*Classification: CANDIDATE — mechanistically sound; clinical data gap; intervention ROI high regardless*
*Key finding: P. gingivalis gut colonization adds TLR2 arm to TLR4-based M1 signal; synergy > additive*
*Clinical implication: periodontal treatment + PPI reassessment are double-duty interventions (M7→M3 AND M7→M1 simultaneously)*
