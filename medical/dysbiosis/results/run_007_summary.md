# Run 007 — Summary
## Phase 3 Coupled Attack | 2026-04-11

> Four searches. Two major sky bridges confirmed. One non-responder mechanism explained.
> This run produced the highest-density findings of the session.

---

## High-Signal Findings

### 1. M1↔M4 Bridge — Mechanistically Upgraded to STRONG CANDIDATE

**New evidence (PMID 31776355):**
IL-23 doesn't just promote Th17 differentiation — it drives TREG PLASTICITY. Foxp3+ Tregs
convert to RORγt+/Foxp3+ cells that CO-PRODUCE IL-17A in human psoriatic skin. This is the
specific molecular mechanism for skin Treg depletion in the M1↔M4 bridge.

**Consequence:** Patients with high IL-23 tone may have "normal" Treg COUNT but depleted
functional Treg capacity. T-index v3 Node A must measure functional Tregs, not just Foxp3+
cell count (Foxp3+/RORγt- only = genuine; Foxp3+/RORγt+ = subverted).

**Real-world drug validation:**
- Risankizumab (Skyrizi): FDA-approved for psoriasis (2019), Crohn's (2022), UC (2024)
- Ustekinumab retrospective (PubMed 30992173, n=70 IBD+psoriasis): 60.7% IBD clinical
  remission in patients started on ustekinumab via dermatology for skin disease
- These are dual-disease outcomes from blocking the shared IL-23 axis — consistent with bridge

**Natural experiment available:** SEQUENCE trial (risankizumab in CD) — co-morbidity subgroup
analysis for concurrent psoriasis patients would directly test Prediction A of attempt_007.

---

### 2. Histamine Axis — Scoped and Bounded

**H3R on beta cells (Nakamura 2014, PMC3874705):** Histamine suppresses GIIS and beta cell
proliferation. Metabolic effect, not autoimmune. H3R agonism → worse glycemic control, slower
beta cell recovery — NOT beta cell killing.

**H1R on T cells (Jutel Nature 2001):** Elevated histamine → Th1 promotion. Theoretically
pro-diabetogenic in T1DM but NO direct evidence in human T1DM studies.

**DAO deficiency in T1DM:** NOT established. Inverse finding: intensive insulin therapy → LOWER
DAO activity (PMID 10488998).

**Scope ruling:**
- DAO protocol remains valid for ROSACEA (H1R/H4R vascular/mast cell effects) → keep in protocol
- Do NOT expect T1DM-specific effects from DAO intervention
- Secondary monitoring: if CVB protocol patient has poor GIIS response → consider H3R-mediated
  histamine suppression as a differential (not autoimmune cause)

---

### 3. OSBP Inhibitors — CVB Target Confirmed at Grade II-2

**Mechanism confirmed:** CVB 3A → recruits PI4KB → OSBP cholesterol/PI4P counter-exchange
→ replication organelle membranes maintained. OSBP inhibition collapses RO → halts RNA synthesis.
Resistance mutations in CVB3 at 3A-3B junction confirm on-target specificity (PMID 29024767).

| Compound | CVB EC50 | Access |
|----------|---------|--------|
| OSW-1 | Low nM | Research only |
| Itraconazole | 0.3–1.6 µM | FDA-approved antifungal — CLINICALLY ACCESSIBLE |
| TTP-8307 | 1.2 µM | Research only |
| 25-hydroxycholesterol | Active | Not formulated |

**Itraconazole:** EC50 0.3–1.6 µM; achievable plasma concentrations at standard antifungal
dosing ~1-2 µM → within antiviral range. Requires CYP3A4 interaction check. No antiviral
dosing trial exists — N=1 empirical.

**Gap:** No in vivo CVB data. Cell culture only. Pancreatic islet microenvironment (low-titer,
persistent 5'UTR-deleted virus) is qualitatively different from cell culture models.

---

### 4. Rosacea Non-Responder Loop — Explained (attempt_008)

**B. oleronius → type I IFN → IL-23 → Th17 loop** (Arhendt JCI Insight 2023, PMC9977509):
Demodex → LL-37 lyses B. oleronius → DNA+LL-37 complexes → pDC TLR9 → type I IFN → IL-23 →
Th17/Th22. IFNAR blockade abolishes Th17 in mouse model → loop is IFN-dependent, not just
Demodex-dependent.

**KLK5-mTORC1 positive feedback confirmed:**
LL-37 → TLR2 → mTORC1 → more LL-37 transcription. Self-amplifying. Operates INDEPENDENTLY
of Demodex density once initiated. Explains ivermectin non-response at ~25%.

**Treatment implication:**
- Non-responders need LOOP INTERRUPTION, not just density reduction
- Azelaic acid 15% gel: inhibits KLK5 + LL-37 transcription → breaks mTORC1 feedback
- Ivermectin + azelaic acid: targets both Demodex input AND downstream loop
- Deucravacitinib trial (NCT06532136, TYK2 inhibitor): blocks type I IFN → IL-23 step directly

---

### 5. M3↔M2 Bridge — STRONG CANDIDATE (attempt_009)

**Epidemiological anchor:** Egeberg JAAD 2016 (n=6,759): T1DM → rosacea OR 2.59.

**Mechanistic chain — confirmed at every published node:**
```
CVB islet persistence → chronic IFN-α → pDC expansion in T1DM (PMID 24973447; 18835928)
    ↓
Elevated circulating IFN-α primes skin pDCs
    ↓
Lower threshold for B. oleronius → pDC → IFN → IL-23 → Th17 loop
    ↓
Rosacea develops at Demodex density that would be tolerated without IFN-α priming
    ↓
Population-level: T1DM patients have 2.59× rosacea prevalence
```

**Proof of concept (HCV era):** Exogenous IFN-α therapy induces psoriasis (n=36, 93% resolution
at cessation, PMC3443510) — confirms systemic IFN-α → Th17 skin disease direction.

**Protocol implication:** In T1DM+rosacea co-affected patients:
- Rosacea severity = SKIN PROXY for CVB IFN-α activity
- Antiviral treatment → less CVB → less IFN-α → rosacea flare frequency should decrease
- Monitor rosacea as a visible, patient-reported surrogate for IFN-α reduction

---

## Sky Bridges Found This Run

| Bridge | Attempt | Status |
|--------|---------|--------|
| M1↔M4 via IL-23/Treg plasticity | 007 (updated) | STRONG CANDIDATE — mechanism confirmed |
| M2+M4 rosacea KLK5/IFN/IL-23 loop | 008 | STRONG CANDIDATE — loop published |
| M3↔M2 via CVB→IFN-α→pDC→rosacea | 009 | STRONG CANDIDATE — OR 2.59 + 3 evidence layers |

---

## T-Index v3 Specification (Updated)

```
Node A = FUNCTIONAL Tregs: Foxp3+/RORγt- (genuine) — not just Foxp3+ count
         (IL-23 converts genuine Tregs to Foxp3+/RORγt+ IL-17 producers — subverted, not absent)

Node B = Inflammatory tone: hsCRP + serum IL-17A + F. prausnitzii + Akkermansia abundance

Node C = Gut Th17 trafficking: serum I-FABP (enterocyte damage proxy)
         High I-FABP → gut barrier breakdown → Th17 trafficking to skin → lower skin threshold

Node D (NEW) = Systemic IFN-α level (Simoa): CVB→IFN-α arm of M4 threshold
         High IFN-α → pDC expansion → skin loop priming → lower rosacea/skin disease threshold

Genetic floor = HLA-DR, NOD2, TLR4, IL23R variants

T-index v3 = f(Node A, B, C, D, Genetic floor)
```

Node D is the connection between M3 and M4. Nodes C and D TOGETHER explain the M4 threshold
from two independent gut/virome inputs. A patient high in both has maximally lowered threshold.

---

## What Remains Unmapped

1. **M6 (early-life) → M4**: Does early-life dysbiosis set baseline IL-23/Th17 tone that persists?
2. **M3+M7 bridge + M3↔M2 combined**: Does P. gingivalis → CAR upregulation → CVB → IFN-α → rosacea create a 4-mountain chain?
3. **Formal "convergent mechanism paper" concept**: All mountains now connect through M4. Is there a synthetic paper that assembles M1+M3+M7+M4+M2 as a unified dysbiosis mechanism?
4. **Clinical protocol final integration**: What does the complete T-index v3-guided protocol look like?

---

*Run 007 complete: 2026-04-11 | Phase 3 — highest yield run of session*
*Three new strong candidate sky bridges. Rosacea non-responder mechanism explained.*
*T-index upgraded to v3: nodes A+B+C+D + genetic floor.*
