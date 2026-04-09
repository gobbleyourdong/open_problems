# Model: IL-23/Th17 Amplification Loop in Psoriasis

## The Core Loop

```
INITIATION (one-time trigger):
  Trigger (strep, trauma, stress) → keratinocyte stress → LL-37 release
  LL-37 + self-DNA → complex activates pDCs → IFN-α
  IFN-α → activates myeloid DCs → IL-23 production
  IL-23 → Th17 differentiation from naïve CD4+

AMPLIFICATION (self-sustaining — this is psoriasis):
  
  ┌─── Th17 cells ◄──── IL-23 (from DCs) ◄──── TNF-α (from keratinocytes) ───┐
  │         │                                              ▲                    │
  │         ▼                                              │                    │
  │    IL-17A/F + IL-22                                    │                    │
  │         │                                              │                    │
  │         ▼                                              │                    │
  │    Keratinocytes:                                      │                    │
  │    ├── Hyperproliferate (3-5 day turnover)             │                    │
  │    ├── Produce TNF-α ─────────────────────────────────►┘                    │
  │    ├── Produce CXCL1/CXCL8 → neutrophil recruitment                        │
  │    ├── Produce CCL20 → recruit more DCs → more IL-23 ──────────────────────┘
  │    └── Release LL-37 → more DC activation (inner loop)
  │
  │    NF-κB IN KERATINOCYTES:
  │    TNF-α → NF-κB → more TNF-α + more IL-1β + more chemokines
  │    This is the AMPLIFIER within the amplifier
  │
  │    NLRP3 IN KERATINOCYTES:
  │    Stress → NLRP3 → IL-1β → promotes Th17 differentiation (TGF-β + IL-1β → Th17)
  │    AND: IL-1β → NF-κB → more TNF-α → feeds the main loop
  │
  └─── LOOP CLOSES: more Th17 → more IL-17 → more keratinocyte activation → more TNF-α → more IL-23 → more Th17

  THREE BRAKES that can stop the loop:
  ├── BRAKE 1: Tregs suppress Th17 (Tr × T17 suppression term)
  ├── BRAKE 2: A20/TNFAIP3 degrades NF-κB signaling components
  └── BRAKE 3: IL-10 deactivates DCs → less IL-23
  
  All three brakes must fail for psoriasis to persist.
```

## The Equations

```
State variables:
  T17(t) = Th17 cell activity
  DC(t) = activated dendritic cell IL-23 production
  K(t) = keratinocyte activation state (proliferation + cytokine production)
  NF(t) = NF-κB activity in keratinocytes
  Tr(t) = Treg suppressive capacity

dT17/dt = k_IL23 × DC × IL23                           [IL-23 drives Th17]
        + k_IL1b × NLRP3 × IL1b                        [IL-1β promotes Th17 differentiation]
        - k_Treg × Tr × T17                             [Tregs suppress Th17]
        - k_apop × T17                                  [natural T cell turnover]

dDC/dt = k_CCL20 × K × CCL20                            [keratinocyte CCL20 recruits DCs]
       + k_LL37 × K × LL37                              [LL-37/DNA activates pDCs]
       - k_IL10 × IL10 × DC                             [IL-10 deactivates DCs]

dK/dt = k_IL17 × T17 × IL17                             [IL-17 activates keratinocytes]
      + k_TNF × NF × TNFa                               [TNF-α from NF-κB activates keratinocytes]
      - k_resolve × Resolvins × K                       [resolvins (omega-3) resolve activation]

dNF/dt = k_TNF_NF × TNFa                                [TNF-α → NF-κB (positive feedback)]
       + k_IL1b_NF × IL1b                               [IL-1β → NF-κB]
       - k_A20 × A20 × NF                               [A20 negative regulator]
       - k_IkBa × IkBa × NF                             [IκBα sequesters NF-κB]
       - k_barr × BetaArrestin2 × IKK                   [β-arrestin-2 from WHM → IKK sequestration]
       - k_BHB × BHB × p65                              [BHB deacetylates p65]

dTr/dt = k_butyrate × [Butyrate]                        [butyrate → FOXP3]
       + k_vitD × [VitD]                                 [vitamin D → Tregs]
       + k_IL10_Tr × IL10                                [IL-10 → FOXP3]
       - k_consume × T17 × Tr                            [consumed suppressing Th17]
```

## The Three Brakes → Three Protocol Arms

| Brake | What restores it | Protocol component |
|-------|-----------------|-------------------|
| **Treg suppression of Th17** | Increase Tr | Butyrate, vitamin D, BHB, WHM→IL-10 |
| **A20/NF-κB regulation** | Reduce NF activity | WHM→β-arrestin-2, BHB→p65 deacetylation, ALA→IKK, colchicine |
| **IL-10 DC deactivation** | Increase IL-10 | WHM→IL-10, apremilast→cAMP→CREB→IL-10 |

**The protocol restores all three brakes.** No single brake restoration is sufficient (the other two loops compensate). All three together can collapse the amplification.

## Comparison to Biologics

| Biologic | What it blocks | Where in the loop | Strength |
|----------|---------------|-------------------|----------|
| Secukinumab | IL-17A | T17 → K link | Very strong (PASI-90 in 50%+) |
| Guselkumab | IL-23 | DC → T17 link | Very strong (PASI-90 in 50%+) |
| Adalimumab | TNF-α | K → NF → K feedback | Strong (PASI-75 in 70%) |
| Apremilast | Multiple (PDE4) | IL-10 ↑, TNF-α ↓, IL-17 ↓ | Moderate (PASI-75 in 33%) |
| **The protocol** | NF-κB, NLRP3, Tregs | All three brakes | **Unknown — predicted moderate** |

Biologics cut SPECIFIC links in the loop. The protocol restores the NATURAL BRAKES. Different strategy, potentially complementary.

## The Prediction

For mild psoriasis (BSA <3%, few thin plaques):
- The three brakes may be sufficient to collapse the loop
- Prediction: 50-70% PASI improvement over 3-6 months
- Residual: occasional thin plaques at trauma-prone sites (Koebner)

For moderate psoriasis (BSA 3-10%):
- Brakes slow the loop but may not collapse it
- Prediction: 30-50% improvement; add apremilast for additional 15-20%
- May need topical therapy for persistent plaques

For severe psoriasis (BSA >10%):
- Loop too strong for brake restoration alone
- Need direct loop interruption (biologic) + protocol for maintenance
- Protocol may allow biologic dose reduction or extended intervals
