# Model: Blood-Brain Barrier Crossing — How CVB Reaches the CNS

## The Routes

CVB is a non-enveloped RNA virus (~30nm). It has three potential routes across the BBB:

```
ROUTE 1: PARACELLULAR (between endothelial cells)
  Tight junctions (claudins, occludin, ZO-1) seal gaps between BBB endothelial cells
  Normally impermeable to virions
  BUT: high-titer viremia → inflammatory cytokines (TNF-α, IL-1β) → tight junction disruption
  "Open door" — virus passes between cells

  When: high viremia + systemic inflammation (neonates, severe acute infection)
  Evidence: TNF-α loosens tight junctions (demonstrated in multiple models)

ROUTE 2: TRANSCELLULAR (through endothelial cells)
  CVB binds CAR receptor on luminal (blood-facing) surface of BBB endothelium
  Endocytosed → transcytosed → released on abluminal (brain-facing) side
  Requires CAR expression on BBB endothelium

  When: CAR is expressed on BBB endothelium (debated — low expression in adults, higher in neonates)
  Evidence: CAR expression documented on brain endothelium in developing brain

ROUTE 3: TROJAN HORSE (inside immune cells)
  CVB infects circulating monocytes → monocytes traffic across BBB (normal immune surveillance)
  → infected monocyte enters CNS → releases virus
  
  When: monocyte infection established (evasion mechanism in T1DM attempt 054)
  Evidence: CVB infects monocytes (demonstrated); monocytes cross BBB (demonstrated)
  This route BYPASSES the BBB entirely — it uses normal immune cell trafficking
```

## The Quantitative Model

```
P(CNS_invasion) = P(route1) + P(route2) + P(route3) - overlaps

Where:
  P(route1) ≈ f(viremia × TNF_α_level × BBB_maturity)
  P(route2) ≈ f(viremia × CAR_expression_on_BBB)  
  P(route3) ≈ f(monocyte_infection_rate × monocyte_BBB_crossing_rate)

IN ADULTS:
  Route 1: low probability (tight junctions mature, inflammation moderate)
  Route 2: low probability (CAR expression low on adult BBB)
  Route 3: MOST LIKELY route in adults (monocytes always traffic across BBB)
  Combined: ~1-5% of infections → CNS invasion

IN NEONATES:
  Route 1: HIGH probability (tight junctions immature + high viremia → high TNF-α)
  Route 2: MODERATE probability (CAR expression higher on neonatal BBB)
  Route 3: HIGH probability (high monocyte infection rate due to immature clearance)
  Combined: >>5% → explains why neonatal CVB encephalitis is much more common
```

## Protocol Implications

| Route | How protocol reduces risk |
|-------|--------------------------|
| Route 1 (paracellular) | Fluoxetine reduces viremia → less TNF-α → tight junctions maintained. Omega-3 DHA supports BBB endothelial membrane integrity. |
| Route 2 (transcellular) | Fluoxetine reduces viremia → fewer virions available for transcytosis. |
| Route 3 (Trojan horse) | Fluoxetine blocks CVB replication IN monocytes → monocytes carry less/no virus. GABA may reduce monocyte activation. |

**Fluoxetine addresses all three routes** by reducing systemic viremia and blocking replication inside Trojan horse monocytes. This is why fluoxetine during acute viremia (not just chronic persistence) has value for CNS protection.

## The Neonatal Implication

Neonates can't take fluoxetine. Their CNS protection relies entirely on:
- Maternal anti-CVB IgG (neutralizes virus before it reaches BBB)
- IVIG (provides antibodies if maternal absent)
- Breastfeeding IgA (reduces gut viral load → lower viremia → lower BBB pressure)

**This circles back to the neonatal sepsis model: maternal antibodies are the neonatal BBB's first line of defense.**
