# T-Index v3 Decision Tree — Measurements to Actions
## 2026-04-12

> The T-index v3 specifies WHAT to measure. This document specifies WHAT TO DO
> based on the pattern of results. The goal: route the patient to the highest-ROI
> intervention arm before initiating the full protocol stack.
>
> Prerequisite: read results/protocol_integration.md for measurement details.
> This document assumes measurements have been obtained.

---

## The T-Index v3 Inputs (Recap)

```
Node C = I-FABP (gut barrier / M1 arm input to M4)
Node D = IFN-α2 Simoa (CVB arm / M3 input to M4)
Node B = hsCRP + IL-17A (inflammatory tone)
P.g.   = P. gingivalis IgG serology (M7 input to M3 + M1)
M6     = Early-life risk factors (structural floor modifier)
Genetic = HLA-DR3, history of T1DM family
```

---

## The Decision Tree

```
START: All measurements obtained
              │
              ▼
     P. gingivalis seropositive?
     ┌─────YES──────┐──────NO──────┐
     │              │              │
     ▼              │              │
STEP 1: PERIODONTAL TREATMENT FIRST
Scaling + chlorhexidine + xylitol
DO NOT add OSBP inhibitors (itraconazole)
or intensify antiviral protocol until
P. gingivalis load is addressed.
Rationale: active P.g. → CAR priming →
any CVB reduction is undermined.
Re-assess at 6 weeks.
     │              │              │
     └──────────────┘              │
                    │              │
                    ▼              │
            Node C (I-FABP) elevated? (>200 pg/mL or >150% of lab ref range)
            ┌─────YES──────────────┼──────NO──────┐
            │                      │              │
            ▼                      │              │
STEP 2a: M1 ARM IS ACTIVE          │              │
Priority intervention:             │              │
- Gut protocol intensification     │              │
  (fiber 35g+/day, LGG probiotic,  │              │
  butyrate 600mg/day, glutamine)   │              │
- Low-glycemic diet (M5 → M1)      │              │
- Check PPI use → taper if present │              │
Node D (IFN-α) still matters —     │              │
check it in parallel (see right)   │              │
Repeat I-FABP at 3 months         │              │
            │                      │              │
            └──────────────────────┘              │
                                   │              │
                                   ▼              │
                         Node D (IFN-α2 Simoa) elevated?
                         ┌─────YES───────────────NO──────┐
                         │                               │
                         ▼                               ▼
              STEP 2b: M3 ARM ACTIVE         STEP 2c: LOW BOTH ARMS
              IFN-α elevation confirmed      Neither gut nor IFN-α arm
              CVB arm is likely operational  elevated.
                                             
              Priority intervention:         Consider:
              - Antiviral protocol core      - M6 structural floor (if M6 risk
                (Vitamin D3/K2, omega-3,       high, may still benefit from
                IF for autophagy/NLRP3)       anti-inflammatory protocol even
              - Check CXCL10 if not done      without acute elevation)
              - OSBP consideration           - M2 arm only (skin protocol)
                (itraconazole — medication     without systemic intensification
                review required)             - Recheck Node D in 3 months if
              - Active rosacea present +       clinical rosacea progresses
                T1DM → presume IFN-α arm    - Node B (hsCRP) elevated?
                operational regardless         → anti-inflammatory foundation
                of Simoa absolute value        still warranted
```

---

## The Pattern Matrix (All Combinations)

| Node C | Node D | P.g. | Action Priority |
|--------|--------|------|-----------------|
| HIGH | HIGH | POS | 1. Periodontal → 2. Gut protocol → 3. Antiviral simultaneously |
| HIGH | HIGH | NEG | 1. Gut protocol (M1 dominant) + Antiviral (M3 arm) simultaneously |
| HIGH | LOW | POS | 1. Periodontal → 2. Gut protocol (M1 primary driver); monitor IFN-α |
| HIGH | LOW | NEG | 1. Gut protocol alone (M1 dominant; M3 arm quiescent); dietary focus |
| LOW | HIGH | POS | 1. Periodontal → 2. Antiviral (M3 primary driver); gut protocol supportive |
| LOW | HIGH | NEG | 1. Antiviral (M3 primary driver); gut protocol supportive |
| LOW | LOW | POS | 1. Periodontal (M7 — prevents cascade even if not active currently) |
| LOW | LOW | NEG | 1. Skin protocol (M2) + anti-problem list + anti-inflammatory foundation |

**Key rule: If BOTH Node C and Node D are LOW and P.g. is NEGATIVE:**
The systemic threshold arms are quiescent. Focus shifts to:
- M2 skin protocol (ketoconazole, ivermectin if rosacea, azelaic acid if non-responder)
- Anti-problem list removal (the highest-ROI intervention when threshold arms are not active)
- M6 structural floor: if M6 risk factors present, lower vigilance threshold for future re-testing

---

## M6 Modifier Rules

**M6 risk factors: C-section, ≥2 antibiotic courses before age 2, formula-fed**

| M6 risk score | Interpretation modifier |
|--------------|------------------------|
| 0-1 risk factors | Standard T-index interpretation applies |
| 2-3 risk factors | Downward-adjust "normal" Node A-D thresholds by ~20%; what looks borderline-normal IS functionally low |
| 3 risk factors (all) | Structural floor very low; maximize anti-problem avoidance; any acute trigger (antibiotic course, viral infection, dietary change) may push below threshold disproportionately |

---

## Monitoring Trigger Rules

**When to re-test Node C (I-FABP) sooner than scheduled:**
- New GI symptoms (cramping, bloating, change in stool pattern)
- Introduction of new NSAID (gut barrier disruption)
- Antibiotic course (gut community disruption → barrier compromise)
- Skin flare despite protocol adherence (may indicate M1 arm re-activation)

**When to re-test Node D (IFN-α2) sooner than scheduled:**
- New viral infection (cold/flu → transiently elevated IFN; wait 4 weeks post-infection before interpreting)
- Worsening rosacea despite ivermectin + azelaic acid (suggests IFN-α arm re-activation)
- Starting itraconazole (re-test at 8 weeks to confirm IFN-α attenuation)

**When to re-test P. gingivalis IgG sooner than scheduled:**
- Dental procedure with bacteremia (wait 3 months post-procedure for re-test)
- New dental symptoms (pain, bleeding gums, swelling)
- 6 months after periodontal scaling (confirm bacterial load reduced)

---

## The "Why Is the Skin Not Improving?" Algorithm

If skin disease (rosacea/seb derm) is not responding to standard topical therapy:

```
Is the KLK5-mTORC1 loop established?
→ Ivermectin non-response after 3 months = YES
→ Add azelaic acid 15-20%

Is the IFN-α arm driving despite topical therapy?
→ Check Node D (IFN-α2 Simoa)
→ Elevated = YES → intensify antiviral protocol

Is the gut Th17 arm driving despite topical therapy?
→ Check Node C (I-FABP)
→ Elevated = YES → intensify gut protocol, check PPI use, check P.g. serology

Is the structural floor the limiting factor?
→ Check M6 history
→ ≥2 risk factors + all Nodes borderline = YES
→ Cannot rescue to "normal" — maximize anti-problem avoidance
→ Maintenance therapy rather than remission targeting

Is a comedogenic product continuing the M2 substrate supply?
→ Check all skincare/haircare ingredients for fatty acid esters, oleic acid
→ Patient using heavy oil near sebaceous zones? → Remove first before adding treatments
```

---

## The Single Most Informative First Test

If only ONE measurement is available today and nothing else:

**P. gingivalis IgG serology (~$50)**

Reason: the result bifurcates the entire protocol.
- Positive → periodontal treatment is PRECONDITION; all other interventions deferred until M7 arm addressed
- Negative → skip to Node C + D for arm-specific protocol routing

If TWO measurements:
**P. gingivalis IgG + I-FABP** — covers M7 and M1 arms simultaneously; these are the two modifiable arms most immediately addressable (periodontal treatment + gut protocol are available today without physician prescription for most components).

If THREE measurements:
**P. gingivalis IgG + I-FABP + IFN-α2 Simoa** — all three modifiable threshold inputs mapped; full T-index v3 routing available.

---

*Filed: 2026-04-12 | Phase 4 sigma method | T-index v3 clinical decision tree*
*Converts framework measurements into protocol routing*
*Highest-ROI first test: P. gingivalis IgG serology (~$50)*
