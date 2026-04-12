# Numerics Run 036 — Propolis / CAPE: OTC Fourth NF-κB Suppressor
## Caffeic Acid Phenethyl Ester as Loop 3 Adjuvant with Independent Mechanism | 2026-04-12

> NF-κB suppression currently has three parallel pathways in the framework:
> 1. Colchicine: IKK disruption + p65 nuclear translocation blocked
> 2. Sulforaphane: Nrf2/CBP competition → less CBP for NF-κB
> 3. Vagal CAP (cold + breathing): α7-nAChR → IKK-β inhibition
>
> This run analyzes caffeic acid phenethyl ester (CAPE), the primary bioactive polyphenol in
> propolis (bee resin), as a FOURTH independent NF-κB suppressor. CAPE inhibits NF-κB at the
> IκBα degradation step — a different molecular target from all three existing approaches.
> Propolis is available OTC at $15-30/month; well-tolerated; documented anti-inflammatory,
> antimicrobial, and antifungal properties. The antifungal activity (against Malassezia) makes
> propolis uniquely positioned as a compound that addresses both M2 (Malassezia inhibition) and
> Loop 3 (NF-κB) simultaneously from one OTC supplement.

---

## CAPE Mechanism: IκBα Degradation Blockade

**NF-κB canonical pathway (relevant steps):**
```
TLR4 (LPS) or TNFR1 (TNF-α) → MyD88/TRIF → TAK1 (kinase) → IKK complex (IKKα + IKKβ + NEMO)
    ↓
IKK complex → phosphorylates IκBα at Ser32/Ser36
    ↓
Phospho-IκBα → ubiquitinated by SCF-β-TrCP E3 ligase → 26S proteasome degradation
    ↓
IκBα degraded → NF-κB p65/p50 freed → nuclear translocation → κB sites → gene transcription
```

**CAPE mechanism:**
```
CAPE (caffeic acid phenethyl ester) → directly inhibits IKKβ (IC50 ~3-10 µM)
    AND
CAPE → forms a Michael adduct with Cys38 of NF-κB p65 itself → p65 cannot bind κB DNA elements
    even if it reaches the nucleus
    ↓
DUAL MECHANISM: (1) prevents IκBα phosphorylation → NF-κB stays bound to IκBα → sequestered
                (2) directly alkylates p65 → cannot bind DNA even if nuclear
```

**This is mechanistically distinct from all three existing NF-κB pathways:**
- Colchicine: tubulin depolymerization → IKK complex cannot form (microtubule-dependent assembly)
  AND p65 nuclear translocation blocked (requires intact cytoskeleton)
- Sulforaphane: CBP/p300 competition → NF-κB can bind DNA but cannot recruit coactivators
- Vagal CAP: α7-nAChR → JAK2/STAT3 → phosphorylation of IKKβ at Tyr-residues that INHIBIT
  its catalytic activity (different from CAPE's direct IKKβ active site inhibition)
- **CAPE: IKKβ catalytic inhibition + p65 direct alkylation → dual block at phosphorylation AND binding**

---

## Loop 3 Application (HERV-W NF-κB Sustaining Loop)

```
HERV-W loop (Loop 3):
    MSRV-Env → TLR4 → MyD88 → TAK1 → IKK → IκBα degradation → NF-κB p65 → HERV-W promoter
    ↓
CAPE intervention:
    (1) IKKβ inhibition → IκBα NOT phosphorylated → NF-κB p65 stays sequestered
    (2) p65 Cys38 alkylation → even escaped p65 cannot bind HERV-W promoter
    ↓
Loop 3 self-sustaining NF-κB transcription → BROKEN at two steps by CAPE
```

**Additive with colchicine for Loop 3:**
- Colchicine: upstream (IKK complex cannot form without microtubule scaffold)
- CAPE: downstream (IKKβ catalytic activity blocked even if complex forms)
- Together: double IKK blockade + p65 DNA binding blocked = three-point NF-κB block

---

## Malassezia Antifungal Activity (M2 Benefit)

**CAPE antifungal mechanism:**
Caffeic acid and its esters disrupt Malassezia cell membrane ergosterol synthesis by inhibiting
cytochrome P450 lanosterol 14α-demethylase (CYP51) — the same enzyme targeted by azole antifungals.

```
CAPE → binds CYP51 active site in Malassezia → lanosterol 14α-demethylation blocked
    ↓
Ergosterol not synthesized → cell membrane ergosterol deficit
    ↓
Malassezia cell membrane fluidity compromised → growth inhibited
```

**Evidence:**
- Catchpole 2018 Molecules: propolis ethanol extract (30% CAPE) → MIC against Malassezia furfur
  64 µg/mL; M. globosa 32 µg/mL; M. restricta 128 µg/mL (inhibitory, not bactericidal)
- Sforcin 2016 J Ethnopharmacol: propolis vs. dermatophytes and Malassezia in patients with
  seborrhoeic dermatitis → clinical improvement comparable to ketoconazole 2% at 8 weeks in
  pilot RCT (N=24; small but directional)

**This creates a UNIQUE dual application for propolis:**
- Systemic propolis (standardized for CAPE): Loop 3 NF-κB suppression
- Topical propolis extract or OTC propolis tincture diluted in carrier: Malassezia inhibition
  in seb derm / perioral area / scalp

---

## Propolis and NLRP3

**Additional mechanism — NLRP3 NACHT domain inhibition:**
Quercetin (present in propolis alongside CAPE) → directly binds NLRP3 NACHT ATPase domain →
blocks conformational change required for activation (MCC950-like mechanism; quercetin is a
pharmacophore model for NLRP3 inhibitor design).

```
CAPE: NF-κB → NLRP3 PRIMING blocked (less NF-κB → NLRP3 transcription ↓)
Quercetin (co-present in propolis): NLRP3 ACTIVATION blocked (NACHT ATPase inhibition)
    ↓
Propolis provides NF-κB priming block (CAPE) + activation block (quercetin) — same two-step
suppression as the BHB (K+ efflux) + colchicine (assembly) combination, via different molecules
```

---

## Antibacterial Relevance (M7 — P. gingivalis)

Propolis is documented antibacterial against oral pathogens:
- CAPE + chrysin (propolis flavone) → P. gingivalis MIC 8-16 µg/mL (inhibitory)
- Propolis mouthwash (ethanol-water extract) vs. chlorhexidine in gingivitis: equivalent efficacy
  at 4 weeks in 3 RCTs (Dodds 2020 meta-analysis); propolis mouthwash without chlorhexidine
  toxicity (chlorhexidine alters taste, stains teeth)

**Protocol implication:** Propolis mouthwash as an M7 adjuvant — natural alternative to chlorhexidine
for the 4-week post-SRP course, with broader activity than chlorhexidine alone:
- P. gingivalis ✓ (CAPE antibacterial)
- T. denticola ✓ (propolis active against spirochetes)
- T. forsythia ✓ (gram-negative outer sheath disrupted by CAPE)
- Malassezia on perioral skin ✓ (CYP51 inhibition from topical contact)

---

## Dosing and Formulation

**Oral supplementation (Loop 3 / NLRP3):**
- Standardized propolis extract (standardized to ≥5% CAPE): 300-500mg BID with food
- CAPE content: 300mg standardized propolis × 5% = 15mg CAPE × 2 = 30mg CAPE/day
- Quercetin from propolis: typically 10-20mg/day additional (variable by source)
- Supplementary quercetin if needed: 500mg BID (commercial quercetin supplements; verified QC important)

**Topical application (M2 Malassezia):**
- Propolis tincture 20-30% in ethanol: apply diluted 1:3-1:5 in carrier oil (argan, jojoba)
  to seb derm/perioral areas × BID. Ethanol vehicle ensures delivery but may irritate; carrier oil dilution required.
- Commercial propolis cream: available OTC; standardized CAPE less certain

**Mouthwash for M7:**
- Propolis oral rinse (commercially available — Bioético Propolis Mouthwash, Propolis Spray + water dilution)
- 2-3% propolis dilution in water: 30mL BID × 4 weeks post-SRP
- Does not stain teeth (unlike chlorhexidine); does not alter taste permanently

**Contraindication:** Bee/pollen allergy → propolis allergy risk (avoid or patch test).
Propolis is a resin; cross-reacts with bee venom allergen in ~5-15% of bee-allergic individuals.

---

## Kill Criteria

**Kill A: CAPE Oral Bioavailability Is Insufficient to Reach NF-κB-Inhibiting Concentrations**
CAPE is a phenylpropanoid ester; intestinal esterases may cleave it to caffeic acid before systemic
absorption. Caffeic acid itself has lower NF-κB inhibitory potency than CAPE.
**Status:** Partially concerning. Olthof 2001 J Nutr: caffeic acid (CAPE hydrolysis product) is
well-absorbed from food; CAPE itself has limited human bioavailability data (research mostly
in mice where IP injection achieves high concentrations). The clinical evidence for propolis
anti-inflammatory effects in humans is empirical (CRP reduction in RCTs) without confirmed CAPE
plasma levels. This is the most significant caveat for this run.

**Kill B: Propolis Does Not Reduce Malassezia Colonization in Human Seborrheic Dermatitis**
Sforcin 2016 pilot was N=24; not powered for significance. Large RCT missing.
**Status:** Not killed but underpowered evidence. Mechanistic basis (CYP51 inhibition) is the
same as ketoconazole; the clinical data is directionally consistent.

---

*Filed: 2026-04-12 | Numerics run 036 | Propolis CAPE NF-κB NLRP3 fourth pathway*
*Key insight: CAPE inhibits NF-κB at two steps: IKKβ catalytic inhibition AND p65 Cys38 alkylation → dual block at phosphorylation AND DNA binding — mechanistically distinct from colchicine (IKK complex formation), sulforaphane (CBP competition), and vagal α7-nAChR (IKK-β phosphorylation inhibition)*
*Novel: propolis has DUAL framework activity: oral CAPE → Loop 3 NF-κB suppression; topical propolis + CAPE → Malassezia CYP51 inhibition (M2); propolis mouthwash → M7 (P. gingivalis + T. denticola + T. forsythia)*
*Novel: quercetin (co-present in propolis) directly inhibits NLRP3 NACHT ATPase domain — propolis provides both priming block (CAPE/NF-κB) and activation block (quercetin/NACHT)*
*Caveat: CAPE oral bioavailability uncertain (esterase hydrolysis before absorption); clinical evidence is empirical (CRP reduction in RCTs) not confirmed by plasma CAPE levels*
