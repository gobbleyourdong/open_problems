# Model: Maternal Antibody Threshold — The Binary Switch

## The Core Model

Neonatal CVB outcome is almost entirely determined by ONE variable: maternal anti-CVB IgG titer at delivery.

```
Let T = maternal anti-CVB neutralizing antibody titer (transferred transplacentally)
Let V₀ = neonatal CVB exposure dose
Let T_crit = critical titer needed to neutralize V₀

IF T ≥ T_crit:
  Maternal antibodies neutralize virus before significant replication
  Neonate clears infection → SURVIVAL, no sequelae
  
IF T < T_crit:
  Insufficient neutralization → unchecked viral replication
  Immature immune system cannot compensate
  Exponential viral growth → multi-organ infection → sepsis
  Mortality: 30-50%

IF T = 0 (seronegative mother):
  No protection → WORST outcome
  Every CVB particle that reaches neonate can replicate freely
  This is where nearly all neonatal CVB deaths occur
```

## The Titer-Outcome Curve

```
Neonatal
Outcome
(survival)
  100% ├────────────────────────────╮
       │                            │
       │        SAFE ZONE           │
       │                            │
   90% │                            ╰──────
       │                                   ╲
       │                                    ╲  
   70% │                             TRANSITION
       │                                      ╲
   50% │                                       ╲
       │                            DANGER ZONE  ╲
       │                                          ╲
    0% ├──────────────────────────────────────────╴╲──
       0        1:8      1:32     1:128    1:512
                Maternal anti-CVB IgG titer

T_crit ≈ 1:32 to 1:128 (estimated from clinical data)
Sharp transition: above threshold → fine; below → disaster
This is a BINARY SWITCH, not a gradient
```

## Factors Modifying T_crit

```
T_crit depends on:

1. Viral exposure dose (V₀)
   ├── Higher V₀ → need higher T to neutralize
   ├── Nursery outbreak: high V₀ (many infected infants shedding)
   ├── Single exposure: low V₀
   └── Breastfeeding adds mucosal IgA → effectively raises T by protecting gut entry

2. CVB serotype
   ├── Need serotype-SPECIFIC antibodies
   ├── Mother seropositive for CVB1 but seronegative for CVB3 → vulnerable to CVB3
   └── Must check ALL 5 serotypes (B1-B5)

3. Gestational age at delivery
   ├── IgG transfer is maximal in third trimester (32-40 weeks)
   ├── Preterm (<32 weeks): reduced transplacental transfer → lower T
   └── Premature neonates need LOWER T_crit (less body mass to protect)
       but RECEIVE less antibody → double jeopardy

4. Neonatal immune maturation
   ├── Term neonates have some innate immunity (NK cells, IFN)
   ├── Preterm: even innate immunity is immature
   └── IFN response in neonates: ~50% of adult capacity (variable)
```

## The Intervention Map

```
INTERVENTION                              EFFECT ON MODEL

Maternal vaccination                      T → 1:512+ for all serotypes (PERMANENT)
                                         T >> T_crit → guaranteed protection

Maternal IVIG (3rd trimester)            T → 1:64-256 (TEMPORARY, 3-6 months)
                                         T > T_crit for neonatal period

Neonatal IVIG (at birth)                 T → supplemented postnatally
                                         Effective even if maternal T was 0

Breastfeeding                            Adds mucosal IgA → reduces effective V₀
                                         Equivalent to lowering T_crit

NICU infection control                   Reduces V₀ (fewer exposure events)
                                         Effective at population level

Maternal CVB screening                   IDENTIFIES who needs IVIG
                                         Turns unknown risk → known → actionable
```

## The Population Math

```
US births: ~3.6M/year
CVB seroprevalence in adults: ~60-80% (varies by serotype and geography)

Seronegative for ALL 5 serotypes: ~5-10% of mothers
Seronegative for ≥1 serotype: ~20-40% of mothers

Neonatal CVB exposure rate: ~1-2% of neonates in first 28 days
  (higher during summer/fall, during outbreaks)

Neonatal CVB sepsis (hospitalized): ~300-500/year (US)
Neonatal CVB deaths: ~100-200/year (US)

WITH universal maternal screening + targeted IVIG:
  Identify 720K-1.4M seronegative mothers
  ~1-2% of their neonates exposed to CVB = 7,200-28,000
  IVIG coverage would prevent essentially ALL severe neonatal CVB
  Deaths prevented: ~100-200/year
  Cost: screening $180M + IVIG ~$50M = $230M/year
  
  Cost per neonatal death prevented: ~$1.1-2.3M
  (Compare: NICU stay for severe CVB sepsis: $200K-500K)
  Net cost savings if including NICU cost avoidance: BREAK EVEN or POSITIVE
```

## The Breastfeeding Factor

Breast milk contains secretory IgA that neutralizes enteroviruses at the gut mucosa:
- Breastfed neonates have significantly lower enteroviral infection rates
- IgA doesn't enter blood but prevents gut-to-blood viral entry
- This LOWERS T_crit — a breastfed neonate needs less circulating IgG
- **Breastfeeding is the cheapest, most accessible neonatal CVB protection**
- Formula feeding removes this protection (one of the hits in T1DM attempt 035)
