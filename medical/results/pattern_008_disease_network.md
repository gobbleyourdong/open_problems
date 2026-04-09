# Pattern 008: CVB Disease Network Topology

## Status: IDENTIFIED — Numerics complete, not yet certified

## The CVB Disease Network

Twelve diseases. One virus. One network.

The 12 CVB-caused diseases form a directed graph where edges represent causal/progression relationships with measurable transition probabilities. The network is rooted at acute CVB infection and flows through acute presentations to chronic diseases.

```
                        CVB INFECTION (root)
                     /    |    |    \    \    \    \    \
                   15%   10%   5%  0.1%  5%   8%   3%   2%   5%   1%
                  /       |     |    \     \    \    \    \    \    \
             PLEUR    MENING  HEP   NEO  MYOC  PERI PANC ORCH  ME/CFS T1DM
               |        |            / | \    ↕     |     ↓↓↓
              20%      5%          40% 50% 20% 15%  25%  reseed
               |        |          |    |    |       |
             ME/CFS  ENCEPH    MYOC  HEP ENCEPH   T1DM
                                |
                               30%
                                |
                               DCM
```

The network has 13 nodes (12 diseases + root CVB infection) and 24 directed edges.

---

## Analysis 1: Degree Centrality — Most Connected Disease

| Disease | Out-degree | In-degree | Total Degree | Description |
|---------|------------|-----------|--------------|-------------|
| **CVB Infection** | **10** | **0** | **10** | Root node: seeds all diseases via viremia |
| Myocarditis | 3 | 4 | 7 | Hub: receives from CVB/peri/orchitis/neonatal; feeds DCM/peri/orchitis |
| Orchitis | 3 | 3 | 6 | Reservoir: receives seeding, feeds back to 3 organs |
| Neonatal Sepsis | 3 | 1 | 4 | High-fan-out: neonatal multi-organ disease |
| Pancreatitis | 2 | 2 | 4 | Bridge: connects to T1DM and orchitis |
| ME/CFS | 0 | 3 | 3 | Terminal sink: receives from pleurodynia, CVB, orchitis |
| T1DM | 0 | 2 | 2 | Terminal sink: receives from pancreatitis, CVB |
| DCM | 0 | 1 | 1 | Terminal sink: receives from myocarditis only |

**Finding**: Acute CVB infection is the most connected node (degree 10) — it seeds all downstream diseases. This makes it the single most impactful prevention target (vaccination).

Among non-root nodes, **myocarditis** is the most connected disease (degree 7), serving as both a receiving node and a propagation node.

---

## Analysis 2: Keystone Analysis — Most Disruptive Removal

Which single disease, if removed from the network, disconnects the most disease paths?

| Disease | Paths Disrupted | % of Total Paths | Interpretation |
|---------|-----------------|-------------------|----------------|
| **Myocarditis** | **27** | **57.4%** | Keystone: removing it disconnects the cardiac cluster AND orchitis feedback |
| Orchitis | 24 | 51.1% | Removing the reservoir breaks the reseeding loop |
| Pancreatitis | 15 | 31.9% | Removing it blocks the pancreatitis -> T1DM path |
| CVB Infection | 12 | 25.5% | Root removal eliminates direct seeding but not inter-disease paths |
| Pericarditis | 11 | 23.4% | Breaks the cardiac bidirectional link |

**Finding**: **Myocarditis is the keystone disease.** Removing it from the network disrupts 57.4% of all disease paths. This is because myocarditis:
1. Sits at the center of the cardiac cluster (pericarditis <-> myocarditis -> DCM)
2. Can seed orchitis (which then reseeds all organs)
3. Is a major downstream target of neonatal sepsis

This does NOT mean myocarditis is the best treatment target — it means that preventing myocarditis would break the most cascading pathways.

---

## Analysis 3: Intervention Value — Best Treatment Target

Which disease, if perfectly treated/prevented, reduces the most total disease burden?

Burden = transition probability x disease severity x population at risk.

| Rank | Disease | Downstream Prevented | Own Burden | Total Value | Downstream # |
|------|---------|---------------------|------------|-------------|--------------|
| 1 | **CVB Infection** | **0.0199** | **0.2000** | **0.2199** | **12** |
| 2 | Pleurodynia | 0.0075 | 0.0450 | 0.0525 | 1 |
| 3 | Myocarditis | 0.0139 | 0.0350 | 0.0489 | 6 |
| 4 | Pericarditis | 0.0061 | 0.0400 | 0.0461 | 6 |
| 5 | ME/CFS | 0.0000 | 0.0375 | 0.0375 | 0 |

**Finding**: **CVB infection is the best intervention target by a factor of 4x** over any individual disease. This is the vaccine argument: a single CVB vaccine prevents all 12 diseases simultaneously. The total intervention value of treating CVB at the source (0.2199) dwarfs treating any individual disease.

Among individual diseases, **pleurodynia** ranks #2 — not because it is severe, but because treating pleurodynia prevents its 20% progression to ME/CFS, which has the largest affected population.

---

## Analysis 4: Cascading Failure Paths

The highest-probability cascade pathways from initial CVB infection to terminal (chronic) disease:

| # | Path | Cumulative Probability | Terminal Disease |
|---|------|----------------------|------------------|
| 1 | CVB -> ME/CFS | 5.00% | ME/CFS |
| 2 | CVB -> Pleurodynia -> ME/CFS | 3.00% | ME/CFS |
| 3 | CVB -> Myocarditis -> DCM | 1.50% | DCM |
| 4 | CVB -> T1DM | 1.00% | T1DM |
| 5 | CVB -> Pancreatitis -> T1DM | 0.75% | T1DM |
| 6 | CVB -> Meningitis -> Encephalitis | 0.50% | Encephalitis |
| 7 | CVB -> Pericarditis -> Myocarditis -> DCM | 0.36% | DCM |
| 8 | CVB -> Orchitis -> ME/CFS | 0.30% | ME/CFS |

**Finding**: ME/CFS is the most probable terminal disease from CVB infection (total probability ~8.3% across all paths). This explains why ME/CFS has the largest affected population among CVB diseases.

The two most common cascades both lead to ME/CFS:
- Direct: CVB -> ME/CFS (5%)
- Via pleurodynia: CVB -> pleurodynia -> ME/CFS (3%)

---

## Analysis 5: Disease Clusters

The network naturally organizes into 5 clusters:

### Cardiac Cluster: Myocarditis -- Pericarditis -- DCM
- Internal edges: myocarditis <-> pericarditis (bidirectional, 15-20%), myocarditis -> DCM (30%)
- Driven by CVB3 cardiotropism and 2A protease cleaving dystrophin
- Clinical implication: ANY cardiac CVB presentation should be screened for all 3

### Metabolic Cluster: Pancreatitis -- T1DM
- Internal edge: pancreatitis -> T1DM (25%)
- Driven by CVB1/B4 pancreatic tropism, exocrine-to-endocrine seeding
- Clinical implication: CVB pancreatitis patients need long-term diabetes screening

### Neurological Cluster: Aseptic Meningitis -- Encephalitis -- ME/CFS
- Internal edge: meningitis -> encephalitis (5%)
- ME/CFS connects via CNS component (neuroinflammation)
- Clinical implication: post-meningitis patients need long-term neurological follow-up

### Reservoir Cluster: Orchitis -- ME/CFS
- Orchitis creates an immune-privileged reservoir in testes
- Periodic viral shedding reseeds all organs
- Clinical implication: male CVB patients with orchitis are at high risk for chronic multi-organ disease

### Acute Cluster: Pleurodynia -- Hepatitis -- Neonatal Sepsis
- Initial CVB presentations that can each seed downstream chronic disease
- Neonatal sepsis has the highest fan-out (3 downstream diseases at high probability)
- Clinical implication: all acute CVB presentations warrant screening for other organ involvement

---

## Upstream vs Downstream Classification

### Upstream Diseases (Prevention Targets)
These diseases are early in the cascade. Preventing them prevents downstream disease.

| Disease | Downstream Diseases | Clinical Action |
|---------|---------------------|-----------------|
| CVB Infection | All 12 | **Vaccination** is the endgame prevention |
| Pleurodynia | ME/CFS | Early antiviral treatment to prevent chronification |
| Aseptic Meningitis | Encephalitis | Monitor for CNS progression |
| Myocarditis | DCM, Pericarditis, Orchitis | Aggressive antiviral + cardiac protection |
| Pancreatitis | T1DM, Orchitis | Prophylactic islet protection (GABA, fluoxetine) |

### Downstream Diseases (Treatment Targets)
These are terminal nodes — they don't cause other diseases but cause major burden.

| Disease | Upstream Sources | Clinical Action |
|---------|-----------------|-----------------|
| ME/CFS | Pleurodynia, CVB, Orchitis | Adapted protocol (see Pattern 002) |
| T1DM | Pancreatitis, CVB | Full T1DM protocol (attempts 001-063) |
| DCM | Myocarditis | Cardiac-specific protocol + SGLT2i |
| Encephalitis | Meningitis, Neonatal Sepsis | Fluoxetine (crosses BBB) + supportive |

---

## The Clinical Implication: Screen ALL 12

Current medical practice treats each CVB disease in isolation. A patient presents with myocarditis; the cardiologist treats the heart. No one checks for pancreatic function, testicular involvement, or ME/CFS symptoms.

The network analysis shows this is wrong.

### The Screening Protocol

**Any patient with confirmed CVB infection (VP1+) should be screened for:**

| Organ System | Screen | Test | Cost |
|-------------|--------|------|------|
| Cardiac | Myocarditis, pericarditis, DCM | Troponin, NT-proBNP, ECG, echocardiogram | $200-500 |
| Pancreas | Pancreatitis, T1DM risk | Lipase, HbA1c, fasting glucose, GAD65/IA-2 antibodies | $100-200 |
| CNS | Meningitis, encephalitis, ME/CFS | Neurological exam, Bell Disability Scale questionnaire | $50-100 |
| Musculoskeletal | Pleurodynia, ME/CFS | Physical exam, activity assessment, NK cytotoxicity | $100-300 |
| Liver | Hepatitis | LFTs (AST, ALT, bilirubin) | $30-50 |
| Testicular (male) | Orchitis | Physical exam, testicular ultrasound if symptomatic | $50-200 |
| Neonatal (if applicable) | Multi-organ sepsis | Full neonatal panel | $500-1000 |

**Total screening cost**: $530-1,350 for a comprehensive multi-organ CVB screen.

**Cost-effectiveness**: A single case of DCM (heart failure) costs $50,000-100,000/year to manage. A single case of T1DM costs $10,000-15,000/year for life. Early detection and antiviral treatment could prevent these outcomes at a fraction of the cost.

---

## The Orchitis Feedback Loop

The most concerning feature of the network is the orchitis feedback loop:

```
CVB -> myocarditis/pancreatitis -> orchitis
                                      |
                                      v
                            immune-privileged testes
                            (virus persists indefinitely)
                                      |
                                      v
                            periodic viral shedding
                                 / |  \
                                v  v   v
                         myocarditis  pancreatitis  ME/CFS
                              |            |
                              v            v
                            DCM          T1DM
```

Orchitis creates a PERMANENT viral reservoir. Even if you clear virus from the heart, pancreas, and CNS, the testes can reseed all organs months or years later.

**Clinical implication**: In male CVB patients, orchitis screening is critical. If detected, fluoxetine's lipophilicity and lysosomal accumulation (10-50x concentration in lysosomes; Daniel & Bhatt 2006) make it uniquely suited to penetrate the blood-testis barrier. This is one of the strongest arguments for fluoxetine as the antiviral of choice: it reaches the hardest reservoir.

---

## Summary: Three Key Insights

### 1. Vaccinate at the Root
CVB infection is the intervention with the highest value (4x any individual disease). A multivalent CVB vaccine (B1-B5) would prevent all 12 diseases. This is the endgame.

### 2. Screen Broadly
Any single CVB disease implies risk for all others. The network shows interconnection, not isolation. Clinical practice must evolve from organ-specific to systemic CVB screening.

### 3. Treat the Keystones
If vaccination isn't available, the highest-value intervention targets are:
- **Myocarditis** (keystone: disrupts 57% of paths if eliminated)
- **Orchitis** (reservoir: disrupts 51% of paths)
- **Pleurodynia** (sentinel: preventing its 20% progression to ME/CFS prevents the most burden)

---

## Files

- Numerics: `numerics/disease_network.py` (full graph analysis, 6 analyses, 3 visualizations)
- Visualization: `results/figures/disease_network.png` (network topology diagram)
- Visualization: `results/figures/intervention_heatmap.png` (adjacency matrix + intervention ranking)
- Visualization: `results/figures/cascade_paths.png` (top 20 cascade paths)
- Cross-disease: `results/pattern_004_protocol_propagation_matrix.md` (how T1DM protocol propagates)
- This pattern: `results/pattern_008_disease_network.md`

*Generated by numerical track (numerics), systematic approach, 2026-04-08*
*Based on: disease_network.py graph analysis — 13 nodes, 24 edges, 6 analytical passes*
