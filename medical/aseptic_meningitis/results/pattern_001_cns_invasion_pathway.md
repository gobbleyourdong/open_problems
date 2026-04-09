# Pattern 001: CVB CNS Invasion -- How Coxsackievirus Crosses the Blood-Brain Barrier

## The Pattern

CVB crosses the blood-brain barrier (BBB) during high-titer viremia to cause aseptic meningitis -- the most common CVB CNS manifestation. The invasion route involves both direct receptor-mediated transcytosis (via DAF/CD55 on endothelial cells) and Trojan horse transport within infected monocytes. The disease is usually self-limiting because meningeal inflammation recruits a robust adaptive immune response that clears the virus. Progression to encephalitis occurs only when specific host/viral factors align.

## Evidence

### Receptor-mediated BBB crossing

- **Bergelson et al., 1997:** CVB primary receptor is CAR (Coxsackievirus and Adenovirus Receptor). CAR is expressed on tight junctions of epithelial and endothelial cells -- including BBB endothelium.
- **Coyne & Bhering, 2006:** CVB also uses DAF (decay-accelerating factor, CD55) as an initial attachment receptor. DAF is expressed on the LUMINAL surface of brain endothelial cells (accessible from blood).
- **Mechanism:** CVB binds DAF on the apical surface of BBB endothelium -> receptor clustering -> signaling cascade (Src kinase, Rho GTPase) -> virus internalization -> transcytosis to the abluminal (brain) side.
- **Coyne et al., 2007:** In vitro BBB model -- CVB crosses polarized brain endothelial monolayers WITHOUT disrupting tight junction integrity. This is NOT inflammatory BBB breakdown; it is active transcytosis.

### Trojan horse mechanism

- **Tabor-Godwin et al., 2010:** CVB-infected monocytes/macrophages can cross the BBB by diapedesis (normal immune cell trafficking). The virus hitchhikes inside immune cells.
- **This explains delayed CNS invasion:** The Trojan horse route requires prior monocyte infection during systemic viremia, so CNS symptoms appear 3-7 days after initial infection.

### Why usually self-limiting

- **Rotbart, 2000:** CVB meningitis triggers vigorous meningeal inflammation: lymphocytic pleocytosis in CSF (100-1000 WBC/microL), elevated protein, normal glucose.
- **Immunocompetent host:** The inflammatory response WORKS. T cells, NK cells, and antibodies clear viral infection from the meninges within 7-14 days.
- **Key principle:** The meninges are NOT immunologically privileged (unlike brain parenchyma). They have robust lymphatic drainage (via dural sinuses), MHC expression, and dendritic cell patrols.
- **Self-limitation rate:** >95% of CVB meningitis resolves completely without sequelae (Rotbart 2000, Romero 2014).

### When it progresses to encephalitis

- **Age < 1 year:** Immature BBB, immature immune response, higher viral loads reach brain parenchyma.
- **High viremia:** Viral load in blood determines BBB crossing probability. Higher load = more crossing events = more parenchymal seeding.
- **Immunodeficiency:** Agammaglobulinemia patients get chronic CVB meningoencephalitis (no antibodies to clear virus).
- **Viral fitness:** Some CVB strains have enhanced neurotropism (point mutations in VP1 that increase DAF binding affinity).

## Quantitative Estimates

| Parameter | Estimate | Source |
|-----------|----------|--------|
| CVB as cause of aseptic meningitis | 30-50% of identified viral meningitis | Romero 2014 |
| Incidence of CVB meningitis | 75,000-150,000 cases/year (US estimate) | CDC enterovirus surveillance |
| CSF WBC count in CVB meningitis | 100-1000 cells/microL (lymphocyte-predominant) | Rotbart 2000 |
| Duration of illness | 5-14 days (median 7 days) | Clinical series |
| Complete resolution rate | >95% | Romero 2014 |
| Progression to encephalitis | <2% in immunocompetent | Rotbart 2000 |
| Progression to encephalitis (neonates) | 10-20% | Verboon-Maciolek 2005 |
| Viral load threshold for BBB crossing | ~10^5-10^6 TCID50/mL blood (estimated) | Animal model data |
| BBB transcytosis time (in vitro) | 2-6 hours | Coyne 2007 |

### BBB Crossing Model

```
P(CNS_invasion) = f(viral_load_blood) * g(DAF_expression_BBB) * h(BBB_integrity)

Where:
  f(V) = 1 - e^(-V/V_threshold)     [sigmoidal, threshold ~10^5 PFU/mL]
  g(DAF) ~= constant in healthy BBB  [DAF constitutively expressed]
  h(BBB) = 1 in adults, 1.5-2.0 in neonates [immature tight junctions]

At peak viremia (day 3-5 of infection):
  Adult, healthy BBB:    P(CNS) ~= 0.05-0.10 (5-10%)
  Neonate, immature BBB: P(CNS) ~= 0.15-0.30 (15-30%)
  Immunodeficient:       P(CNS) ~= 0.30-0.60 (viral load stays high)
```

## Connection to T1DM Protocol

1. **CNS invasion proves CVB reaches immunologically complex sites:** If CVB can cross the BBB, it can certainly reach (and persist in) pancreatic islets, which have a much less formidable barrier.
2. **Autonomic neuropathy in T1DM:** CVB CNS invasion during the initial infection may damage autonomic ganglia, contributing to the gastroparesis and orthostatic hypotension common in long-standing T1DM. The T1DM protocol's anti-inflammatory stack (BHB, omega-3) would help.
3. **ME/CFS overlap:** Brain fog and cognitive symptoms in T1DM patients may have a neuroinflammatory component from prior CVB CNS invasion. Worth screening for.
4. **Fluoxetine crosses the BBB:** Importantly, fluoxetine (proposed CVB antiviral in T1DM protocol) is designed to cross the BBB. If persistent CVB exists in CNS tissue, fluoxetine can reach it -- unlike many antivirals that cannot cross the BBB.

## What's Needed Next (theory track)

1. **Formalize the BBB crossing probability model** -- proper ODE system for viral load dynamics vs BBB transcytosis rate, with age-dependent parameters.
2. **Lean proof target:** "Self-limitation of CVB meningitis requires functional adaptive immunity" -- provable from agammaglobulinemia case series (they get chronic disease, proving the adaptive immune system is necessary for clearance).
3. **Quantify the dual-route contribution** -- what fraction of CNS invasion is transcytosis vs Trojan horse? This determines whether BBB-tightening interventions would help.
4. **Map the DAF/CAR expression gradient** across different CNS regions -- this predicts which brain areas are most vulnerable if meningitis progresses to encephalitis.
5. **Connect to the encephalitis pattern** -- formalize the branching point: what measurable parameters at meningitis presentation predict progression to encephalitis?
