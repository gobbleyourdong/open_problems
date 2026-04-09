# Attempt 002: Treg/Th2 Rebalance — The Immunological Core of Eczema

## The Insight

Eczema is fundamentally a Treg deficiency disease. Not "too much Th2" but "too few Tregs to suppress Th2."

```
HEALTHY:
  Naïve CD4+ → TGF-β + IL-2 → Treg (FOXP3+) → suppresses Th2
  Th2 cells exist but are HELD IN CHECK by Tregs
  Th1/Th2/Th17/Treg in balance

ECZEMA:
  Naïve CD4+ → IL-4 (from innate lymphoid cells, basophils) → Th2
  Tregs insufficient → Th2 runs unchecked
  IL-4/IL-13 → suppress filaggrin → barrier breaks → more antigen entry → more Th2
  VICIOUS CYCLE (analogous to ME/CFS vicious cycle but different variables)
```

## The Eczema Vicious Cycle (Formalized)

```
State variables:
  B(t) = barrier integrity (0 to 1, where 1 = intact)
  T2(t) = Th2 cell activity (cytokine production level)
  Tr(t) = Treg suppressive capacity
  S(t) = S. aureus colonization density
  I(t) = itch intensity (drives scratching → mechanical barrier damage)

Coupled dynamics:
  dB/dt = +k_repair × Emollients - k_scratch × I - k_cytokine × T2 × (IL-4 suppresses FLG)
  dT2/dt = +k_antigen × (1-B) × Allergens - k_suppress × Tr × T2 + k_staph × S
  dTr/dt = +k_butyrate × Butyrate + k_vitD × VitD - k_consume × T2 (Tregs consumed suppressing Th2)
  dS/dt = +k_colonize × (1-B) - k_antimicrobial × Cathelicidin - k_bleach × BleachBath
  dI/dt = +k_IL31 × T2 - k_antihistamine × Antihistamine - k_moisturize × Emollients

DISEASE STEADY STATE:
  B low, T2 high, Tr low, S high, I high → stable (self-reinforcing)

HEALTH STEADY STATE:
  B high, T2 low (suppressed), Tr adequate, S low, I low → stable

BISTABLE — same as ME/CFS. Must push multiple variables simultaneously.
```

## Why Single Interventions Fail

| Intervention alone | Why it fails |
|-------------------|-------------|
| Moisturizer only | Repairs barrier temporarily, but Th2 suppresses filaggrin → barrier breaks again |
| Topical steroid only | Suppresses local inflammation, but systemic Th2 skewing persists → flares when stopped |
| Probiotic only | Marginal Treg boost insufficient to overcome established Th2 dominance |
| Antihistamine only | Reduces itch but doesn't address Th2/barrier/S. aureus |
| Dupilumab only | Blocks IL-4/IL-13 → dramatic improvement, but $36K/year and doesn't fix Tregs |

## Why the Multi-Target Protocol Should Work

The protocol pushes ALL FIVE variables simultaneously:

| Variable | Intervention | Direction |
|----------|-------------|-----------|
| B (barrier) | Ceramide moisturizer + dilute bleach baths | B ↑ |
| T2 (Th2) | Tregs suppress Th2 (indirect) | T2 ↓ |
| Tr (Tregs) | Butyrate + vitamin D + BHB | Tr ↑↑ |
| S (S. aureus) | Vitamin D → cathelicidin + bleach baths | S ↓ |
| I (itch) | Barrier repair + Th2 suppression + moisturizer | I ↓ |

**Push all 5 → cross the threshold → system settles into health attractor.**

This is the SAME principle as the ME/CFS bistability model. Single interventions fail because the system snaps back. Multi-target intervention crosses the separatrix.

## The Treg Restoration Stack

The core of the approach — directly increasing Treg:Th2 ratio:

| Intervention | Treg mechanism | Expected magnitude |
|-------------|---------------|-------------------|
| Butyrate 300mg TID | HDAC inhibition → FOXP3 promoter derepression → Treg differentiation | Moderate (10-20% Treg increase in gut, systemic effect smaller) |
| Vitamin D 5,000 IU | VDR → direct Treg differentiation + IκBα upregulation | Moderate (especially if currently deficient) |
| BHB (fasting/exogenous) | HDAC inhibition → pro-Treg epigenetic state | Modest (sustained low-level effect) |
| GOS/FOS prebiotics | Feed Faecalibacterium → butyrate production → Tregs | Moderate (indirect, takes weeks) |
| L. rhamnosus GG | Modulates DC phenotype → promotes Treg induction | Modest-moderate (best data in prevention) |
| WHM → IL-10 | IL-10 → STAT3 → FOXP3 → Treg differentiation | Unknown magnitude for skin-specific Tregs |

**Combined**: estimated 30-50% increase in circulating Treg frequency over 3 months. Whether this is sufficient to tip the Treg/Th2 balance in skin depends on initial severity.

## The S. aureus Problem

S. aureus colonizes >90% of eczema skin. Its toxins are superantigens that polyclonally activate T cells (including Th2) → amplify flares.

Vitamin D → cathelicidin → kills S. aureus. This is a DIRECT antimicrobial effect, not immunomodulation.

```
Vitamin D deficient eczema patient:
  Low cathelicidin → S. aureus thrives → superantigen → Th2 flare → worse eczema

Vitamin D replete eczema patient:
  Cathelicidin adequate → S. aureus suppressed → fewer superantigen triggers → less Th2 → better skin
```

**Checking and correcting vitamin D is possibly the single highest-impact intervention in eczema.** It's the only intervention that simultaneously kills S. aureus (antimicrobial), induces Tregs (immune), and inhibits keratinocyte proliferation (direct skin effect).

## Status: IMMUNOLOGICAL MODEL — Treg/Th2 rebalance as core mechanism, multi-target approach required
