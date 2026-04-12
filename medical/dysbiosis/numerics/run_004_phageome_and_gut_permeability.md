# Phageome Dynamics + Gut Permeability Assay Landscape
## Run 004 | Numerical Instance | 2026-04-11

> Two Run 001/002 noise items addressed together (related: both affect M1).

---

# PART A: Phageome

## Why the Phageome Matters for Dysbiosis

Phages outnumber gut bacteria ~10:1 by particle count. They are the density governors of the bacterial community — the natural "population control" system. When phage community structure breaks down, bacterial density regulation fails → dysbiosis is harder to reverse.

```
Healthy phage-bacteria ecosystem:
  Phage predation ←→ Bacterial population
  (Lotka-Volterra oscillation, keeps populations in check)
  
Dysbiotic phage ecosystem (IBD):
  Lysogenic phage expansion (integrate into bacteria)
  → Horizontal gene transfer (virulence factors, toxins)
  → Bacterial clones with enhanced survival
  → Harder to displace with conventional probiotics
```

## CrAssphage — The Most Abundant Gut Phage

**Discovery:** 2014, Dutilh et al. — found by cross-assembly of metagenomic datasets that had been sitting in databases for years unrecognized as a virus. Named "crAss" for cross-assembly.

**Target:** Bacteroides species (primarily B. intestinalis, B. fragilis)

**Abundance:** Detectable in ~50-70% of gut metagenomes globally. When present: often the most abundant viral signal.

**Dysbiosis relevance:**
- Low CrAssphage → less predation pressure on Bacteroides → Bacteroides can over-expand
- But also: Bacteroides is generally beneficial (fiber fermentation, acetate production)
- CrAssphage dynamics are therefore complex — it maintains Bacteroides density at homeostatic levels, not zero

**In TinyHealth FASTQ:**
- Shotgun metagenomics: CrAssphage DNA reads detectable with Kraken2 (viral database required)
- Presence/absence + relative abundance is informative
- Absence of CrAssphage: could mean low Bacteroides, or could mean phageome is depleted

## IBD Phageome Pattern

**Expansion of Caudovirales (tailed phages, dsDNA):**
- 2-5× expansion in Crohn's disease vs healthy controls (Norman 2015, Cell Host & Microbe)
- These are predominantly TEMPERATE (lysogenic) phages, not lytic
- They integrate into bacterial genomes → facilitate horizontal gene transfer (HGT)
- More HGT → more toxin/virulence gene spread → more pathogenic bacterial clones

**Why this matters for treatment:**
- Standard probiotics add beneficial bacteria but can't address bacteriophage-mediated HGT
- If a patient has IBD-pattern phageome (Caudovirales expansion), the bacterial landscape is being actively modified by phage activity in a way probiotics can't counter

**Can TinyHealth FASTQ detect this?**
- CrAssphage: yes (with viral sequences in Kraken2 database)
- Caudovirales expansion: requires VirSorter2 on assembled contigs (advanced, Run 004 pipeline step 7)
- Simple proxy: if Kraken2 shows >5% viral reads in non-human fraction → unusual viral load, investigate

## Phage Therapy as Precision Dysbiosis Intervention

**Current state (2026):**
- FDA compassionate use: approved on case-by-case basis for drug-resistant infections
- Clinical trials: 
  - BioPhage PA (P. aeruginosa phage) — Phase 2 complete in CF lung infections
  - PHAGOBIOTIC studies (multi-drug resistant Staph) — Phase 1/2
  - Pherecydes PP921 for atopic derm Staph — Phase 1/2 (topical phage)
  - No approved gut-dysbiosis-targeted phage product

**The gut dysbiosis phage therapy gap:**
Eliminating one dysbiotic taxon (e.g., Klebsiella in IBD) with phage leaves an ecological vacuum. Unless something fills it:
- Related bacteria evolve resistance to phage (resistance mutations in phage receptor → rapid) 
- Other opportunists expand into the niche

**Combination strategy (emerging):**
- Phage cocktail (kills target bacteria) + probiotic (fills ecological niche) + prebiotic (sustains the probiotic)
- Phage resistance cycling: use 3-4 phages targeting different receptors, rotate to stay ahead of resistance

**Most relevant for user's context:**
- S. aureus phage therapy for skin dysbiosis (atopic derm component): Pherecydes PP921 topical — Phase 1 data shows safety and some efficacy signals. Not yet available commercially.
- No phage therapy relevant for Malassezia/Demodex (these are eukaryotes, not bacteria — phages don't infect them)
- Gut Klebsiella (histamine producer): if detected in TinyHealth FASTQ → no clinical phage option yet, but dietary intervention (low-histamine diet, DAO supplement) is the current route

## What to Watch in TinyHealth FASTQ for Phageome

```
Metric                     How to check          What it means
─────────────────────────  ────────────────────  ──────────────────────────────
CrAssphage presence        Kraken2 viral reads   Bacteroides density control active
Viral read % (total)       Kraken2 summary       >5% = elevated viral activity
Caudovirales contigs       VirSorter2            Elevated = IBD-pattern phageome
ssDNA Microviridae         VirSorter2            Common, usually benign
```

---

# PART B: Gut Permeability Assay Landscape

## The Zonulin Problem

Post-Zhang 2021, the standard "zonulin" assay is compromised:
- The Immundiagnostik commercial kit (most widely used, including by most functional medicine labs) detects **complement C3**, not the actual zonulin protein
- Actual zonulin: a protein encoded by the FAM55B gene, a role in tight junction regulation. The commercial assay doesn't specifically target it.
- Result: years of published data using "zonulin" as a gut permeability marker may be measuring C3, which is a non-specific inflammation marker

**Clinical implication:** Don't order the standard zonulin test from most labs. If you get a positive result, it may just mean systemic inflammation, not specifically gut permeability.

**If gut permeability is clinically relevant to investigate:** use alternative tests below.

---

## Alternative Gut Permeability Tests

### 1. Lactulose:Mannitol (L:M) Ratio — Gold Standard Functional Test

**Principle:** Two sugars, two routes of absorption
- **Mannitol** (monosaccharide, ~182 Da): absorbed via transcellular route (through enterocytes). Fraction absorbed reflects absorptive surface area.
- **Lactulose** (disaccharide, ~342 Da): normally cannot pass intact tight junctions. Elevated urinary lactulose = paracellular leak.

**Protocol:**
1. Overnight fast (8-12h)
2. Drink solution: 5g lactulose + 1g mannitol in 100mL water
3. Collect 5-hour urine (complete collection)
4. Lab: HPLC or enzymatic assay for both sugars
5. Calculate: lactulose/mannitol ratio

**Normal:** L:M < 0.07 (lactulose passes very little even with normal fasting transit time)
**Elevated (leaky):** L:M > 0.09-0.10

**What it actually measures:** Small intestinal permeability (jejunum and ileum). Does NOT measure colonic permeability.

**Advantages:**
- Functional test (directly measures permeability, not a biomarker)
- No antibody/assay controversy
- Published validation across 40 years
- Can be repeated to track changes over time

**Limitations:**
- 5-hour urine collection (patient burden)
- Confounded by delayed gastric emptying, renal impairment, gut transit time
- Not available at most hospital labs

**Lab availability (US):**
- Genova Diagnostics: "Intestinal Permeability Assessment" (~$150-200)
- Great Plains Laboratory: similar test
- Cyrex Array 2 is a DIFFERENT test (antibodies to barrier proteins, not functional)

---

### 2. Lactulose:Rhamnose (L:R) Ratio — More Precise

**Same principle but rhamnose is more precise than mannitol** for small intestinal absorption measurement. Published more recently. Some research groups prefer it.

**Not widely commercially available as a clinical test.**

---

### 3. Serum 4PB (4-phenylbutyrate) — Emerging

Not yet commercially available. Research stage. 4PB is a short-chain fatty acid that serves as a tracer for paracellular passage when given orally.

---

### 4. LPS-Binding Protein (LBP) Serum — Indirect

**What it measures:** LBP is an acute phase protein that binds LPS. Elevated LBP = increased LPS exposure.

**Advantages:**
- Standard clinical assay (ELISA, research/specialty labs)
- Reflects cumulative LPS burden
- Does not require sugar drink/urine collection

**Disadvantages:**
- Indirect (measures immune response to LPS, not gut permeability per se)
- Elevated in any gram-negative infection, not only gut LPS
- Also elevated by the acute phase response to any inflammation

**Reference:**
- Normal: ~3-10 µg/mL
- Metabolic syndrome patients: ~15-25 µg/mL
- Sepsis: >100 µg/mL
- Chronic gut dysbiosis: typically 10-20 µg/mL range (subtle elevation)

**Clinical availability:** Research specialty labs, some functional medicine panels. ~$50-100.

---

### 5. Fatty Acid-Binding Protein 2 (FABP2 / I-FABP) Serum — Emerging Clinical Use

**What it measures:** Intestinal FABP is released by enterocytes when they are damaged or have increased permeability. Serum FABP2 elevation = enterocyte injury/death.

**Advantages:**
- Direct enterocyte damage marker (more specific than LBP)
- Standard ELISA, increasingly available
- Elevation precedes clinical symptoms in gut damage models

**Limitations:**
- Reflects DAMAGE, not just permeability (e.g., could be elevated in celiac, IBD active disease, even with a high-fat meal that causes enterocyte stress)
- Not specific to chronic permeability — more useful for acute gut injury

**Clinical availability:** Specialty labs, some hospitals. ~$50-150.

---

## Summary: Which Permeability Test to Order

```
SITUATION                           RECOMMENDED TEST
────────────────────────────────    ─────────────────────────────────────────────
"I want to test if I have leaky      L:M ratio (Genova Diagnostics)
gut" — best functional evidence      (~$150, urine collection)

"I want a blood test, simpler"       FABP2 + LBP combination
                                     (~$100-200, single blood draw)

"I already have a 'zonulin' result   Discard if from Immundiagnostik kit.
from a standard lab"                 Re-test with L:M ratio.

"I want to monitor over time"        LBP (most standardized for serial measurement)
                                     Or L:M ratio at baseline + 6mo intervals
```

---

## Connection to M1 (gut dysbiosis → systemic inflammation)

Run 001 kill matrix: P1.2 (zonulin) had evidence AGAINST = 2/3 (marker controversy). With this data:

**Revised M1 P1.2 status:** 
- Zonulin as measured by commercial kit = measure of C3 (inflammation), not gut permeability. Invalidated as permeability marker.
- Replacement: L:M ratio (validated) or FABP2 + LBP (blood-based)
- The underlying P1.2 prediction (gut permeability correlates with systemic disease) remains biologically sound. The assay was just wrong.

---
*Run 004 phageome + permeability: CrAssphage visible in TinyHealth FASTQ with Kraken2 viral DB. Zonulin assay from commercial kit likely measures C3 (not zonulin). Replace with L:M ratio (Genova, ~$150) or FABP2+LBP blood panel. No clinical phage therapy yet for gut dysbiosis organisms.*
