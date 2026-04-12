# T-Index Component Interactions — Multiplicative vs Additive
## Run 003 | Numerical Instance | 2026-04-11

> Question from Run 002: do the 8 T-index proxies combine additively or multiplicatively?
> Finding: components are NOT independent — they form a network with two convergence nodes.

---

## Network Structure of T-Index Components

The 8 proxies are upstream inputs to two convergence nodes:

```
INPUT LAYER                    NODE A: Treg tone           NODE B: Inflammatory tone

Vitamin D ────────────────────┤ (FOXP3 induction,         │
F. prausnitzii ────butyrate───┤  Treg proliferation,      │
Akkermansia ──────mucin/LPS───┤  IL-10 production)        │
                               │                           │
Omega-3 (EPA/DHA) ────────────┼────────────────────────── ┤ (resolvin, NF-κB suppression,
hsCRP (inverse) ──────────────┼────────────────────────── ┤  NLRP3 tone, PGE2 balance)
Zinc ─────────────────────────┼────────────────────────── ┤
                               │                           │
NOD2/TLR4 genotype ─ sets the FLOOR for both nodes (constitutional baseline)

         THRESHOLD STATE = Node_A × Node_B × Genetic_Floor
```

The two nodes are not independent either — Treg tone (Node A) actively suppresses inflammatory tone (Node B) via IL-10 and TGF-β. Low Node A → less suppression of Node B → Node B rises. This creates a **multiplicative coupling** between the two nodes.

---

## Interaction 1: Vitamin D × F. prausnitzii (STRONG, multiplicative)

**Mechanism:**
- Vitamin D → VDR on intestinal epithelial cells → promotes tight junction integrity + antimicrobial peptide expression → maintains commensal-favorable niche
- Vitamin D → VDR on immune cells → FOXP3 expression → Treg expansion
- F. prausnitzii butyrate → HDAC inhibition → FOXP3 amplification (requires vitamin D's FOXP3 priming to work efficiently)
- Low D: both niche support and FOXP3 induction impaired
- Low F. prausnitzii: butyrate signal absent, FOXP3 amplification blocked
- **Both low: FOXP3 induction is doubly blocked — neither the VDR nor the butyrate-HDAC pathway is functional**

**Evidence for coupling:**
- VDR-KO mice have profoundly dysbiotic gut microbiome including F. prausnitzii depletion (Jin 2015)
- F. prausnitzii growth requires Paneth cell defensins partially regulated by VDR
- Vitamin D supplementation in IBD → partial restoration of F. prausnitzii (Zhao 2012 — observational)

**Interaction type:** MULTIPLICATIVE at threshold level. Individual deficiency = partial Treg impairment. Both deficient = near-total impairment of the butyrate-FOXP3 axis.

**User relevance:** If TinyHealth shows low F. prausnitzii AND user's D level is <40 ng/mL → doubly impaired Treg axis. Protocol already supplements D3. Confirm 25-OH-D is >60 ng/mL.

---

## Interaction 2: Zinc × Vitamin D (CRITICAL, often overlooked)

**Mechanism:**
- Zinc finger domain: VDR is a nuclear receptor with a zinc finger DNA-binding domain
- Low zinc → dysfunctional VDR → vitamin D cannot execute downstream gene programs
- Result: serum 25-OH-D may look NORMAL (or even optimal) while VDR function is impaired
- This makes zinc deficiency a "hidden amplifier" — it silently blocks D's effects without changing D's measured level

**Evidence:**
- VDR zinc finger coordination: biochemical, well-established
- Zinc deficiency → reduced VDR mRNA expression in intestinal cells (Sekler 1996)
- Clinical implication: supplementing D without adequate zinc may produce apparent D sufficiency (serum level OK) but functional D deficiency (VDR not working)

**Interaction type:** MULTIPLICATIVE — zinc deficiency renders vitamin D supplementation partially or fully ineffective. This is the most clinically impactful interaction in the T-index.

**Check:** Is serum zinc being monitored? Supplementing D3+K2 without zinc monitoring is incomplete.

---

## Interaction 3: Omega-3 × hsCRP (CORRELATED, not multiplicative)

**Mechanism:**
- Omega-3 deficiency IS a cause of elevated hsCRP (via less resolvin production → unresolved inflammation → CRP elevation)
- Therefore: low omega-3 and high hsCRP are measuring the same downstream state, not independent factors

**Implication for T-index:** These two components cannot both be counted as independent risk points. If hsCRP is elevated AND omega-3 is low → one inference (resolution pathway impaired), not two.

**How to handle:** In the T-index, treat omega-3 and hsCRP as a CLUSTER:
- Both low omega-3 AND high CRP: strongly confirms resolution pathway impaired → -3 pts (not -4)
- High CRP with normal omega-3: CRP from other source (infection, other inflammation) → -1 pt
- Low omega-3 with normal CRP: either resolution impaired but compensated, OR hsCRP hasn't caught up → -1 pt

---

## Interaction 4: NOD2 Variant × F. prausnitzii Abundance (MULTIPLICATIVE, genetic floor)

**Mechanism:**
- NOD2 detects muramyl dipeptide (MDP) from bacterial cell walls → triggers Paneth cell defensin secretion
- Paneth cell defensins shape commensal community (selective antimicrobial pressure)
- NOD2 variants (R702W, G908R, L1007fs) → reduced MDP sensing → less defensin → different commensal selection pressure
- In NOD2 wild-type: Paneth cell defensins help sustain F. prausnitzii community
- In NOD2 variant: commensal maintenance is compromised; F. prausnitzii is more vulnerable to depletion by dietary or antibiotic stress

**Evidence:**
- NOD2 variants: F. prausnitzii is among the taxa depleted in NOD2-variant IBD patients (Sokol 2009)
- NOD2-KO mice: altered intestinal defensin profile → dysbiotic gut microbiome

**Interaction type:** MULTIPLICATIVE. NOD2 variant = lower floor for how well F. prausnitzii can be maintained regardless of dietary optimization. You can supplement butyrate/tributyrin directly, but cannot fully compensate for the defensin maintenance deficit.

**User relevance:** NOD2 genotype determines whether F. prausnitzii restoration via dietary/probiotic means will be stable or will keep depleting. Cheap to test (23andMe covers R702W at minimum).

---

## Interaction 5: Akkermansia × Gut Barrier → hsCRP (SEQUENTIAL cascade)

```
Akkermansia present → mucin layer maintained
     ↓
Gut barrier intact → less LPS translocation
     ↓
Less systemic TLR4 activation → less NF-κB → lower hsCRP
     ↓
Lower systemic inflammatory priming → Node B stays low
```

**Interaction type:** SEQUENTIAL (chain), not parallel multiplicative. Akkermansia depletion ultimately shows up as elevated hsCRP if the barrier degrades far enough. But the timeline is weeks-months (barrier degradation is gradual).

**Measurement lag:** Akkermansia depletion may precede hsCRP elevation by 4-12 weeks. So T-index using TinyHealth + hsCRP together may detect the early signal (low Akkermansia) before the late signal (elevated hsCRP).

**Clinical implication:** If TinyHealth shows low Akkermansia BUT hsCRP is still normal → early warning state. Intervention before hsCRP elevates is higher ROI.

---

## Revised T-Index Structure

Based on the interaction analysis, the 8-component flat score is misleading. Restructured:

```
T-INDEX v2 (network-aware)

TREG NODE SCORE (Node A):
  Primary: F. prausnitzii (weighted x2 — butyrate-FOXP3 is the main pathway)
  Amplifier: Vitamin D × Zinc (D efficacy gated by zinc — must check together)
  Secondary: Akkermansia (barrier maintenance → less inflammatory depletion of Tregs)

INFLAMMATORY TONE SCORE (Node B):
  Primary: hsCRP + omega-3 index (treat as cluster, not independent)
  Secondary: Zinc (NLRP3 gate)

GENETIC FLOOR:
  NOD2 status (sets how stable Node A can be maintained)
  TLR4 D299G (sets LPS sensitivity baseline)

THRESHOLD = Node_A × Node_B × Genetic_Floor

LOW THRESHOLD (= vulnerable state):
  Node A < 50th percentile AND Node B elevated AND NOD2 variant present
  → Any microbial density increase likely crosses disease threshold

HIGH THRESHOLD (= resilient state):
  Node A > 75th percentile AND Node B low AND NOD2 wild-type
  → High microbial density tolerated without disease
```

**Key revision:** zinc must be measured before interpreting vitamin D level. A normal 25-OH-D in a zinc-deficient person is functionally low D.

---

## What Study Would Validate the T-Index?

Design: Cross-sectional
- Enroll 200 adults with documented high Demodex density (>100/cm² by dermoscopy), half with active rosacea, half asymptomatic
- Measure full T-index v2 in both groups
- Prediction: T-index v2 score is significantly lower in disease group vs tolerant group

If this study exists → T-index is validated. If not → it should exist. This is tractable (Dermatology + Microbiome collaboration). Estimated feasibility: 6 months, $150,000-300,000.

---
*Run 003 T-index interactions: flat additive model is wrong. Network model with two convergence nodes. Critical interaction: zinc × vitamin D (VDR function gate). Most actionable: test zinc before interpreting D supplementation.*
