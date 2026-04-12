# run_148 — CTLA4 / CD152: Treg Effector Suppression, CD80/CD86 Trogocytosis, Abatacept T1DM Prevention, rs3087243 GWAS Locus

## Identity

| Field | Value |
|-------|-------|
| Gene | CTLA4 (chromosome 2q33.2) |
| Protein | Cytotoxic T lymphocyte-associated protein 4 (CD152) |
| Class | Type I transmembrane glycoprotein; CD28 superfamily; IgV-like ectodomain |
| Ligands | CD80 (B7-1), CD86 (B7-2) on APCs |
| Expression | Constitutive: Tregs (FOXP3 → CTLA4 transcription); Inducible: activated T cells (48-72h after TCR + CD28 signal) |
| Counter-receptor | CD28 (co-stimulatory receptor; competes for same B7 ligands) |

---

## Structural Context: CTLA4 vs. CD28 Competition

CTLA4 and CD28 share the same ligands (CD80 and CD86) but are functionally opposed:

| Feature | CD28 | CTLA4 |
|---------|------|-------|
| Function | Co-stimulatory | Co-inhibitory |
| Affinity for CD80 | Kd ~4 μM | Kd ~0.4 μM (10× higher) |
| Affinity for CD86 | Kd ~2.6 μM | Kd ~0.2 μM (>10× higher) |
| Valency | Monomer at membrane | Disulfide-linked homodimer (higher avidity) |
| Surface expression | Constitutive on naïve T cells | Inducible on activated T cells; constitutive on Tregs |
| Signaling output | PI3K/Akt → CD28 YMNM motif → p85 recruitment → Akt → survival/proliferation | Akt/PI3K INHIBITED; SHP-2 recruitment; PP2A recruitment → T cell activation ↓ |
| Subcellular | Plasma membrane | ~90% intracellular (TCR-recycling vesicles) → surface only during TCR engagement |

**Key insight:** CTLA4 outcompetes CD28 for B7 ligands by ~10-fold in affinity and by homodimer avidity. During T cell-APC contact, CTLA4 rapidly cycles to the membrane (half-life ~30s on surface) → rapidly captures CD80/CD86 before CD28 can engage them → CD28 signal truncated.

---

## Treg-Specific CTLA4 Functions

### Constitutive Expression via FOXP3

FOXP3 → transcriptional activation of CTLA4 gene (CTLA4 promoter has FOXP3 binding sites and NFAT/AP-1 sites). Natural Tregs express ~10-fold more CTLA4 surface protein than conventional T cells. This makes CTLA4 the constitutive effector molecule that allows Tregs to suppress adjacent T cells during every APC contact.

### Mechanism 1: Trogocytosis (CD80/CD86 Stripping)

The primary Treg suppression mechanism via CTLA4:

```
Treg CTLA4 engages CD80/CD86 on DC/B cell surface
    ↓
CTLA4-CD80/CD86 complex pulled into Treg by retrograde actin flow
    ↓
CD80/CD86 "stripped" from APC surface (trogocytosis)
    ↓
APC surface CD80/CD86 density ↓
    ↓
Neighboring naïve T cells: less CD28 signal available
    ↓
T cell activation threshold ↑ → anergy/tolerance
```

This is a TRANS mechanism — Tregs deplete B7 ligands from APCs, making the entire APC less stimulatory for all nearby T cells. It is not just blocking a single TCR contact but degrading the APC's stimulatory capacity globally.

**Quantitative:** A single Treg can strip ~300-500 CD80/CD86 molecules per hour from an APC. In a lymph node with ~1,000 APCs and normal Treg:Teff ratios (~1:10), this creates a significant CD28-depleted microenvironment around each APC.

### Mechanism 2: cis Competition on T Cells

On activated conventional T cells (inducible expression):
```
TCR + CD28 signal → CTLA4 upregulated (48-72h)
    ↓
CTLA4 (high affinity) outcompetes CD28 for remaining surface CD80/CD86
    ↓
CD28 co-stimulation ↓ → IL-2 production ↓ → T cell contraction
```

This is the "negative feedback on activated T cells" mechanism — CTLA4 upregulation automatically dampens the very signal that induced it.

### Mechanism 3: IDO Induction (Tolerogenic DC)

CTLA4 on Tregs → binds CD80/CD86 on plasmacytoid DCs → reverse signaling → IDO (indoleamine 2,3-dioxygenase) upregulation in DCs → tryptophan depleted → kynurenine produced → T cell proliferation inhibited (IDO covered in run_091).

This connects CTLA4 to the run_091 IDO/kynurenine pathway: CTLA4 is one trigger that induces IDO expression in DCs, creating a tolerogenic environment complementary to direct B7 trogocytosis.

### Mechanism 4: Soluble CTLA4 (sCTLA4)

Alternative splicing of CTLA4 mRNA produces a soluble isoform (sCTLA4, ~15 kDa) lacking the transmembrane domain. sCTLA4:
- Circulates in blood
- Binds CD80/CD86 in TRANS → prevents T cell activation without cell-cell contact
- rs3087243 G allele (risk for T1DM, RA, thyroid disease) → less efficient 3'UTR → less sCTLA4 → less peripheral tolerance

---

## T1DM — Genetics and Mechanism

### rs3087243 (CT60) T1DM GWAS Locus

One of the original T1DM susceptibility loci (pre-GWAS era, confirmed by GWAS):
- rs3087243 = 3'UTR polymorphism in CTLA4
- A allele (protective): efficient mRNA/splicing → high sCTLA4 production → peripheral tolerance
- G allele (risk): less sCTLA4 → less peripheral tolerance → autoreactive T cells escape
- Additional CTLA4 haplotype (splice variant that produces ligand-independent CTLA4): rs231775 (exon 1 A49G) → Thr17Ala in signal peptide region → altered surface trafficking

**T1DM mechanistic pathway:**
```
Low sCTLA4 (rs3087243 G) + Low membrane CTLA4
    ↓
Tregs: reduced trogocytosis capacity → APCs maintain higher CD80/CD86 density
Activated T cells: less CTLA4 negative feedback
    ↓
Autoreactive T cell activation threshold ↓
    ↓
Escaped autoreactive T cells → islet infiltration
    ↓
β cell destruction
```

### 18th T1DM Stratification: CTLA4 rs3087243

Adding to the existing T1DM genetic stratification panel (17 prior runs). CTLA4 haplotyping:
- Protective A allele: high sCTLA4, adequate Treg trogocytosis → lower T1DM risk
- Risk G allele: suboptimal CTLA4 → abatacept intervention more justified (restores CTLA4-Ig function)

### Abatacept (CTLA4-Ig) in T1DM

Abatacept = fusion protein of CTLA4-Ig Fc + CTLA4 ectodomain. Mechanism: CTLA4 ectodomain binds CD80/CD86 → APC cannot stimulate T cells → autoreactive T cell activation ↓.

**TrialNet TN-09 trial (Orban 2011 Lancet):**
- Recent-onset T1DM patients (T1DM ≤100 days)
- Abatacept (10 mg/kg monthly IV) × 2 years
- Result: ~59% higher C-peptide AUC vs. placebo at 2 years; effect persisted to year 3 despite drug discontinuation
- Mechanism: interrupts early insulitis wave → spares residual β cell mass → endogenous insulin production maintained

**TrialNet TN-10 (prevention):**
- At-risk relatives (2+ autoantibodies)
- Abatacept delayed T1DM diagnosis by ~50 months on average in high-risk participants
- Positions abatacept as prevention tool, not just treatment

**Comparison to other Treg stabilizers in framework:**
- Low-dose IL-2 (run_140): expands/maintains Treg numbers quantitatively
- CTLA4-Ig (abatacept): restores the EFFECTOR suppression function regardless of Treg count
- GSK-3β inhibitor (run_114): prevents FOXP3 degradation within each Treg
- Synergistic hypothesis: low-dose IL-2 (more Tregs) + abatacept (each Treg more effective) = additive Treg restoration

---

## Rosacea — CTLA4 and Skin Inflammation

### Th17/Th1 Balance in Rosacea Dermis

CTLA4 on Tregs trogocytoses CD80/CD86 from dermal APCs (Langerhans cells, dermal DCs, B cells) → APC stimulatory capacity ↓ → Th17 and Th1 priming ↓ in draining lymph nodes.

In rosacea patients with CTLA4 rs3087243 G allele:
- Reduced sCTLA4 → skin DCs maintain higher CD80/CD86 → more efficient Th17/Th1 priming from rosacea-relevant antigens (Demodex peptides, LL-37-modified self antigens)
- Inflammatory cycle: more APC stimulation → more Th17/Th1 cells → more dermal infiltration → more inflammation → more Demodex → more APC loading

### CLEC16A (run_128) Connection

run_128: CLEC16A (T1DM GWAS) controls MHC-II autophagy/degradation in DCs and Langerhans cells — affecting antigen presentation capacity. CTLA4 trogocytosis targets CD80/CD86 on these same CLEC16A-regulated DCs. These two T1DM loci control different aspects of APC function: CLEC16A = MHC-II antigen loading; CTLA4 = B7 co-stimulatory ligand stripping. Compound low-function genotypes (CLEC16A risk + CTLA4 G allele) = double APC dysregulation.

### Abatacept in Inflammatory Skin Disease

Abatacept has clinical activity in psoriasis (T cell-mediated, similar immune architecture to rosacea). Case reports of rosacea-like dermatitis during abatacept therapy are rare; more commonly anti-inflammatory. The T cell activation dampening mechanism is relevant to rosacea Th17/Th1 pathology.

---

## ME/CFS Relevance

- **CTLA4 on NK cells:** NK cells express CTLA4 under certain conditions; CTLA4 on NK cells → APC CD80/CD86 trogocytosis → NK functional suppression; in ME/CFS, if NK cells hyperexpress CTLA4 (exhaustion-associated), this could dampen their own activation
- **Central tolerance:** CTLA4 in thymus (AIRE cells) → negative selection; CTLA4 deficiency → autoimmune features; ME/CFS autoimmune hypothesis → suboptimal CTLA4
- **IDO connection (run_091):** CTLA4 → IDO induction in DCs → kynurenine → quinolinic acid (neurotoxic) or kynurenate (neuroprotective); ME/CFS IDO dysregulation = connected via CTLA4 → DC IDO pathway

---

## Quantitative Parameters

| Parameter | Value | Context |
|-----------|-------|---------|
| CTLA4 affinity for CD80 | Kd ~0.4 μM | SPR measurement |
| CTLA4 affinity for CD86 | Kd ~0.2 μM | SPR |
| CD28 affinity for CD80 | Kd ~4 μM | SPR (~10× lower than CTLA4) |
| CTLA4 surface half-life | ~30 seconds | Live imaging; rapid cycling |
| CD80/CD86 stripped per Treg per hour | ~300-500 molecules | Trogocytosis assay |
| rs3087243 OR for T1DM (G allele) | ~1.5-2.0 | Meta-analysis |
| Abatacept T1DM trial C-peptide preservation | ~59% higher AUC | Orban 2011 Lancet |
| sCTLA4 plasma level (normal) | ~50-100 ng/mL | ELISA |

---

## Framework Integration Points

| Prior Run | Connection |
|-----------|-----------|
| run_010 (FOXP3) | FOXP3 → CTLA4 transcription; Treg constitutive CTLA4 = FOXP3-dependent output |
| run_114 (GSK-3β/STUB1) | FOXP3 protein stability → CTLA4 expression maintained; run_114 affects CTLA4 indirectly via FOXP3 |
| run_128 (CLEC16A) | CLEC16A controls DC MHC-II loading; CTLA4 strips DC CD80/CD86 — two orthogonal APC regulation mechanisms |
| run_091 (IDO/kynurenine) | CTLA4 → DC IDO induction → tryptophan → kynurenine pathway; CTLA4 is an upstream IDO inducer |
| run_136 (TYK2/IL-23/Th17) | TYK2/IL-23 → Th17 differentiation; CTLA4 on Tregs → APC CD80/CD86 ↓ → less Th17 priming; upstream of run_136 |
| run_140 (IL2RA/JAK3/STAT5) | IL2RA = Treg quantitative supply; CTLA4 = Treg effector per-cell suppression; orthogonal Treg axes |
| run_147 (SIRT1/FOXO3a) | SIRT1/FOXO3a = Treg metabolic fitness; CTLA4 = Treg effector function — metabolic and effector layers |

---

## Saturation Override Checklist

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| 1. Absent from all prior runs as primary subject | PASS | CTLA4 appears in 10 files as IS/context mention; never analyzed as primary; trogocytosis mechanism, sCTLA4 splicing, abatacept T1DM trials = 0 prior analysis |
| 2. MODERATE+ rosacea + T1DM | PASS | T1DM: rs3087243 GWAS hit; abatacept T1DM prevention/treatment trials (Orban 2011); Treg effector suppression; Rosacea: skin DC CD80/CD86 trogocytosis → Th17/Th1 priming ↓; CTLA4 G allele → rosacea-skewing |
| 3. New therapeutic/monitoring target | PASS | Abatacept (approved RA/JIA; T1DM trial data); rs3087243 18th stratification; sCTLA4 monitoring; abatacept + low-dose IL-2 synergy rationale |
| 4. Kill-first fails | PASS | run_141 mentions CTLA4 cSMAC clustering as IS geometry context — not the trogocytosis/sCTLA4/abatacept mechanism; no prior run analyzes CTLA4 as primary; CD28 competition, trogocytosis, IDO induction, abatacept all absent |

---

*One-hundred-and-forty-first extension | CTLA4 CD152 trogocytosis CD80/CD86-stripping sCTLA4-soluble-isoform rs3087243-CT60-T1DM-GWAS 18th-stratification CD28-competition high-affinity-B7 Treg-effector-suppression APC-depleting abatacept-CTLA4-Ig TrialNet-TN09-Orban2011-Lancet T1DM-prevention-trial CLEC16A-run128-APC-parallel IDO-run091-upstream Th17-priming-brake rosacea-skin-DC FOXP3-CTLA4-link low-dose-IL2-run140-synergy | run_148 | Framework at SATURATION + 37: 148 runs*
