# Numerics Run 044 — H. pylori: M7 Gastric Extension with NLRP3 and NF-κB Activity
## Helicobacter pylori as the Oral-Gastric Dysbiosis Bridge to Rosacea/T1DM | 2026-04-12

> M7 currently covers the oral microbiome (P. gingivalis + red complex: T. denticola,
> T. forsythia). H. pylori (Helicobacter pylori) extends M7 to the GASTRIC MICROENVIRONMENT:
> H. pylori colonizes the gastric mucosa and, via CagA/VacA virulence factors, activates both
> NF-κB (TLR4 → NF-κB + CagA → EPIYA-SHP2 → NF-κB) and NLRP3 (IL-18/IL-1β secretion from
> gastric epithelial cells is NLRP3-dependent). The rosacea-H. pylori association has been
> studied for 30 years: two meta-analyses (Gravina 2015, Chen 2019) document significantly
> higher H. pylori seropositivity in rosacea vs. controls and H. pylori eradication → rosacea
> improvement. This run formalizes the mechanism and protocol implications.

---

## H. pylori Biology and Virulence Factors

**H. pylori colonization:**
- Gram-negative spiral bacterium; colonizes gastric antrum + corpus mucosa
- Global prevalence: 50% (developed world ~30-40%; developing world >70%)
- Transmission: oral-oral (saliva, vomit) or fecal-oral; acquired primarily in childhood
- Chronic infection: H. pylori evades immune clearance (urease → ammonia → pH buffering;
  LPS structure modified → low TLR4 affinity → reduced innate detection)

**Key virulence factors:**

CagA (Cytotoxin-associated gene A):
```
CagA-positive strains (~60% of H. pylori isolates) → type IV secretion system → injects
    CagA protein into gastric epithelial cells
    ↓
CagA → EPIYA tyrosines phosphorylated by Src/Abl kinases → activated CagA
    ↓
Phospho-CagA → SHP2 phosphatase binding → Ras/ERK pathway → NF-κB activation
CagA (unphosphorylated form) → E-cadherin disruption → β-catenin nuclear translocation
    → additional NF-κB target gene expression
    ↓
NF-κB → IL-8 ↑ (neutrophil recruitment), IL-6 ↑, TNF-α ↑, pro-IL-1β ↑ (NLRP3 priming Signal 1)
```

VacA (Vacuolating cytotoxin A):
```
VacA → binds gastric epithelial cell surface → oligomerizes into pore → membrane channel
    ↓
VacA channel → Cl⁻ efflux + K⁺ efflux → intracellular K⁺ ↓ (NLRP3 Signal 2 equivalent!)
    ↓
K⁺ efflux → NLRP3 oligomerization → ASC speck → caspase-1 activation
    ↓
Pro-IL-1β (Signal 1, via CagA/NF-κB) + VacA K⁺ efflux (Signal 2) → MATURE IL-1β secreted
    from gastric epithelium → local inflammation → gastric NLRP3-driven IL-1β
    AND: VacA → mitochondrial membrane disruption → mtROS → additional NLRP3 Signal 2
```

**This creates an H. pylori-specific NLRP3 activation circuit:**
- CagA → NF-κB → NLRP3 priming (Signal 1) — same as TLR4/LPS in gut
- VacA → K+ efflux → NLRP3 activation (Signal 2) — same logic as ATP/BHB
- The H. pylori CagA/VacA combination delivers BOTH NLRP3 signals simultaneously from a single pathogen

---

## H. pylori → Systemic Inflammation: The M7 Gastric Bridge

**H. pylori-derived LPS and bacterial translocation:**
H. pylori gastric colonization → chronic gastric inflammation → gastric barrier disruption →
H. pylori LPS + bacterial products → portal circulation → liver (Kupffer cells) → systemic
circulation → systemic NF-κB activation. This is the same gut-systemic bridge as M1 (intestinal
LPS) but from the GASTRIC compartment.

**H. pylori and rosacea — epidemiological evidence:**
- Gravina 2015 J Eur Acad Dermatol Venereol: meta-analysis 14 studies (N=2,346) → H. pylori
  seropositivity in rosacea patients: 65% vs. 38% controls (OR 2.47, 95% CI 1.82-3.35, p<0.001)
- Chen 2019 J Am Acad Dermatol: meta-analysis 8 studies → H. pylori eradication → rosacea
  improvement in 65-80% of cases (variable by study design; open-label and RCT)
- El-Khalawany 2004 J Eur Acad Dermatol: H. pylori eradication (triple therapy) × 2 weeks →
  rosacea remission at 6 months in 63% of H. pylori positive rosacea patients vs. 17% H. pylori
  negative controls (dermal flushing + papulopustular phenotype)

**Mechanistic explanation:**
H. pylori → gastric CagA/VacA → NLRP3 → IL-1β → systemic inflammatory tone ↑
H. pylori LPS → portal → systemic → TLR4 → NF-κB → HERV-W expression ↑ (Loop 3 priming)
H. pylori gastritis → gastric serotonin cell disruption → altered gut motility → M1 dysbiosis
    amplification (disrupted gastric emptying → bacterial overgrowth downstream)

---

## H. pylori and T1DM

**H. pylori in T1DM:**
T1DM prevalence of H. pylori: ~40-55% (comparable to general population but with higher risk
of atrophic gastritis progression due to T1DM immune dysregulation).

**H. pylori → insulin resistance / β cell relevance:**
- H. pylori CagA+ → IL-8, TNF-α, IL-6 → systemic low-grade inflammation → insulin resistance
  (adipose tissue TNF-α → insulin receptor substrate-1 serine phosphorylation → insulin
  resistance; same pathway as M1 LPS-driven insulin resistance)
- H. pylori eradication → improved insulin sensitivity (meta-analysis Tang 2019 World J
  Gastroenterol: H. pylori eradication → HOMA-IR reduced 0.31 [95% CI 0.13-0.49])
- In T1DM: H. pylori → systemic inflammation → NLRP3 priming (via IL-6/TNF-α → NF-κB →
  NLRP3 priming Signal 1) → lower threshold for β cell NLRP3 activation (run_043 bridge)

**H. pylori + PPI use (M7 oral-gut connection from run_030):**
PPI (proton pump inhibitor) use for H. pylori treatment → gastric acid suppression → P. gingivalis
(acid-sensitive anaerobe) can reach duodenum and colon → SECOND M7→M1 mechanism. H. pylori
treatment requires PPI (triple therapy: PPI + amoxicillin + clarithromycin or metronidazole).
The H. pylori treatment protocol ITSELF creates a temporary P. gingivalis gut colonization risk:
- During triple therapy (14 days): PPI → gastric pH 5-6 → P. gingivalis-friendly
- After H. pylori eradication: stop PPI promptly → gastric acid restored → P. gingivalis transit
  eliminated

**Protocol implication:** H. pylori triple therapy → LGG probiotic concurrent (during PPI course)
to prevent P. gingivalis/oral dysbiosis gut colonization during the acid-suppressed window.

---

## H. pylori Detection and Eradication Protocol

**Detection:**
- Stool H. pylori antigen test (sensitivity 94%, specificity 97%; less invasive than urea breath test)
- Urea breath test (13C-UBT): sensitivity 95%, specificity 96%; gold standard for non-endoscopic diagnosis
- Serum H. pylori IgG: sensitivity 85%, specificity 79% (lower specificity; false positives from past
  exposure; not ideal for current infection vs. past infection)

**Eradication:**
Standard first-line regimen (region-dependent on clarithromycin resistance rates):
- Low clarithromycin resistance (<15%): triple therapy:
  PPI + amoxicillin 1g BID + clarithromycin 500mg BID × 14 days
- High clarithromycin resistance (>15%) or penicillin allergy:
  Bismuth quadruple: PPI + bismuth subcitrate 120mg QID + tetracycline 500mg QID + metronidazole
  500mg TID × 10-14 days (more effective in resistant regions)

**Framework-specific additions to standard H. pylori protocol:**
1. **Concurrent LGG 10^10 CFU/day** (start Day 1 of triple therapy; continue 90 days post-eradication):
   - Prevents P. gingivalis gut colonization during PPI-induced acid suppression (M7 → M1 bridge)
   - Reduces clarithromycin-associated dysbiosis (Lactobacillus rhamnosus GG is clarithromycin-resistant)
2. **Stop PPI promptly** (14 days for triple therapy; stop on Day 15): gastric acid restoration
   → P. gingivalis transit window closed
3. **Confirm eradication**: UBT or stool antigen test at 4-6 weeks post-treatment (minimum 2 weeks
   after last PPI dose to avoid false negative)
4. **Test rosacea response**: rosacea flare frequency at 3 and 6 months post-eradication; expect
   improvement in 65-80% of H. pylori-positive rosacea patients per meta-analysis data

**Should H. pylori be screened in all rosacea/T1DM patients?**
Screening indication: rosacea (M8-dominant flushing + erythema; OR recalcitrant papulopustular
not responding to standard protocol) + dyspeptic symptoms (heartburn, bloating, nausea) OR
first-degree relative with gastric cancer/peptic ulcer. Universal screening in rosacea is not
evidence-based; symptom-guided screening is.

---

## Kill Criteria

**Kill A: H. pylori Eradication Improves Rosacea Via Placebo Effect or Antibiotic Mechanism, Not H. pylori Itself**
The improvement after H. pylori eradication could be due to the antibiotics (clarithromycin has
anti-inflammatory properties; metronidazole has anti-rosacea activity for other organisms)
rather than H. pylori eradication per se.
**Status:** Partially concerning. El-Khalawany 2004 compared H. pylori-positive vs. H. pylori-
negative rosacea patients given the same antibiotics → only H. pylori-positive patients improved
significantly. This is the most direct test of the H. pylori vs. antibiotic effect and supports
H. pylori causation over antibiotic bystander effect.

**Kill B: H. pylori LPS Is Too Low-Potency to Drive Systemic NF-κB in Rosacea at Clinical Infection Levels**
H. pylori LPS has modified lipid A (reduced TLR4 affinity vs. E. coli LPS). H. pylori is a GASTRIC
colonizer, not a bloodstream pathogen; bacteremia is rare. The systemic exposure to H. pylori
products may be too low to drive meaningful NF-κB outside the stomach.
**Status:** Partially concerning. CagA injection via type IV secretion system is intracellular and
local — not systemic. The systemic mechanism is more likely: H. pylori gastritis → gastric mucosal
inflammation → IL-8, IL-6, TNF-α ↑ in gastric tissue → systemic cytokine spillover rather than
H. pylori LPS directly. This is supported by the insulin resistance data (Tang 2019: HOMA-IR
improvement after eradication confirms systemic metabolic effect from a local gastric pathogen).

---

*Filed: 2026-04-12 | Numerics run 044 | H. pylori CagA VacA NLRP3 NF-κB rosacea T1DM M7 gastric*
*Key insight: H. pylori delivers BOTH NLRP3 signals simultaneously: CagA/NF-κB → NLRP3 priming (Signal 1) + VacA → K+ efflux → NLRP3 activation (Signal 2). Two meta-analyses document H. pylori → rosacea association (OR 2.47) and eradication → 65-80% rosacea improvement*
*M7 extended: oral (P. gingivalis + red complex) + gastric (H. pylori) dysbiosis as the dual M7 targets*
*Protocol: H. pylori eradication (triple/quadruple) + concurrent LGG (prevents P. gingivalis gut colonization during PPI window) + confirm eradication at 6 weeks + stop PPI promptly on Day 15*
*T1DM: H. pylori → insulin resistance (HOMA-IR, Tang 2019) + NLRP3 priming → eradication improves both insulin resistance and lowers NLRP3 floor*
*Kill A partially mitigated: H. pylori-positive vs. -negative rosacea same antibiotics → only H. pylori-positive improved (El-Khalawany 2004)*
