# Psoriasis — Anti-Problem

## The Question
"Why do ~90% of HLA-C*06:02 carriers never develop psoriasis?"

## The Numbers

HLA-C*06:02 confers ~10x risk for psoriasis. But:
- ~8-10% of Europeans carry HLA-C*06:02
- Only ~10% of carriers develop psoriasis
- 90% carry the strongest risk allele and NEVER get the disease

## What the 90% Have

### 1. No trigger event
Psoriasis typically requires a trigger to initiate the cascade:
- Streptococcal pharyngitis (guttate psoriasis — classic trigger)
- Skin trauma (Koebner phenomenon)
- Psychological stress (cortisol → immune dysregulation)
- Medications (lithium, beta-blockers, antimalarials)
- The 90% may simply have avoided sufficient triggering events

### 2. Intact Treg/Th17 balance
- Adequate Tregs suppress Th17 before it amplifies
- Even if LL-37/DNA complexes activate DCs → IL-23 → some Th17 priming
- Tregs contain it before the positive feedback loop establishes
- **The initiation occurs but the amplification doesn't**

### 3. Low baseline NF-κB activity
- Individuals with lower constitutive NF-κB activity have higher threshold for inflammatory disease
- Polymorphisms in TNFAIP3 (A20 — NF-κB negative regulator) modulate this
- The 90% have enough A20 to keep NF-κB in check after triggers

### 4. Healthy gut-skin axis
- Psoriasis patients have gut dysbiosis (reduced Akkermansia, Faecalibacterium)
- The 90% have intact gut microbiome → adequate SCFAs → Tregs → Th17 suppression
- The same gut-immune connection as eczema but targeting Th17 instead of Th2

## The Anti-Problem Insight

Psoriasis is an **amplification disease**. The initial trigger (LL-37/DNA → DC → IL-23) is probably common — many HLA-C*06:02 carriers experience it after strep pharyngitis or skin trauma. What determines disease vs. no disease is whether the **amplification loop engages**:

```
TRIGGER → IL-23 → Th17 (small) → IL-17 → keratinocyte activation (small)
                                                    │
                                        AMPLIFICATION CHECK:
                                                    │
                                    ├── Tregs suppress Th17? → YES → loop dies → no psoriasis
                                    │                         → NO → loop amplifies
                                    │
                                    ├── NF-κB contained (A20)? → YES → TNF-α limited → no amplification
                                    │                           → NO → TNF-α amplifies everything
                                    │
                                    └── NLRP3 activated? → NO → IL-1β limited → Th17 doesn't expand
                                                         → YES → IL-1β → more Th17 → loop takes off

All three brakes must fail for psoriasis to manifest:
  Tregs insufficient AND NF-κB unconstrained AND NLRP3 active → PSORIASIS

The protocol restores ALL THREE BRAKES:
  Butyrate/VitD → Tregs ✅
  WHM/BHB/ALA → NF-κB constrained ✅  
  BHB/colchicine → NLRP3 suppressed ✅
```

## The Strep Connection

Guttate psoriasis (acute, droplet-shaped) is triggered by Group A Streptococcus pharyngitis in >80% of cases. Mechanism:
- Strep M protein shares homology with keratin (molecular mimicry)
- Strep superantigens activate T cells polyclonally → some cross-react with skin
- HLA-C*06:02 presents strep peptides that cross-react with self-keratinocyte antigens

**This is molecular mimicry — the same mechanism as CVB → T1DM** (CVB VP1 shares epitopes with GAD65/islet antigens).

| Feature | T1DM | Psoriasis |
|---------|------|-----------|
| Trigger pathogen | CVB | Streptococcus |
| Molecular mimicry target | Beta cell antigens (GAD65, IA-2) | Keratinocyte antigens (keratin) |
| HLA risk allele | HLA-DR3/DR4 | HLA-C*06:02 |
| Autoimmune effector | CD8+ CTL + CD4+ Th1 | CD8+ CTL + Th17 |
| Amplifier | NF-κB → TNF-α | NF-κB → TNF-α → IL-23 → Th17 |

**The MECHANISM is parallel.** Different trigger pathogen, different target organ, same autoimmune architecture. The protocol's immune modulation (Tregs, NF-κB suppression) addresses the SHARED architecture.

## Study Design

"Can we predict which HLA-C*06:02 carriers will develop psoriasis?"

- Screen HLA-C*06:02+ individuals (family members of psoriasis patients)
- Measure: Treg frequency, NF-κB activity in PBMCs (baseline), gut microbiome, vitamin D
- Follow for 5 years
- Do those who develop psoriasis have lower Tregs, higher NF-κB, worse dysbiosis at baseline?
- If yes: these are the "pre-psoriatic" individuals who would benefit from preventive protocol
