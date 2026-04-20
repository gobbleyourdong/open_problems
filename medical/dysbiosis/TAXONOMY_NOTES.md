# Taxonomy Notes — Dysbiosis Corpus

> **Purpose**: canonical location for organism-rename / taxonomy-update
> notes that affect citations across the dysbiosis numerics corpus.
> When literature reclassifies an organism (genus rename, species
> split, etc.), the per-run files written before the rename use the
> historical name. Rather than editing every per-run file when a
> rename is published, this file holds the canonical mapping and
> future readers/instances can grep here.
>
> **Maps to**: sigma v5 Convention Beats Instruction (this file is
> structural enforcement of taxonomy accuracy via single-source-of-
> truth + grep, rather than per-file propagation); CITATION_DISCIPLINE.md
> (companion structural-enforcement doc for citation accuracy).
>
> **Status**: Tier 1 framework doc per sigma v9.1 Method Mechanism
> Map. Created 2026-04-20 Fire 19 from cross-audit propagation work
> (Fires 17-18) that surfaced the Heyndrickxia rename.

---

## Active taxonomy corrections

### *Bacillus oleronius* → ***Heyndrickxia oleronia*** (Gupta 2020)

**Reclassification source**: Gupta RS, Patel S, Saini N, Chen S.
"Robust demarcation of 17 distinct *Bacillus* species clades, proposed
as novel Bacillaceae genera, by phylogenomics and comparative genomic
analyses: description of *Robertmurraya kyonggiensis* sp. nov. and
proposal for an emended genus *Bacillus* limiting it only to the
members of the Subtilis and Cereus clades of species."
**Int J Syst Evol Microbiol** 2020;70(11):5753–5798.
**PMID: 33112222** (with erratum PMID 33351742).

**Mapping**:
- **Old name**: *Bacillus oleronius* (Bacillaceae; widely used in
  clinical literature 2007-present, especially Lacey et al. work on
  Demodex endosymbiont mechanism)
- **New name**: ***Heyndrickxia oleronia*** (Bacillaceae;
  *Heyndrickxia* is the new genus, named after Karel Heyndrickx;
  -us → -a feminine ending)
- **Both names are still in active clinical literature use**; both
  refer to the same organism.

**Affected dysbiosis files** (per Fire 18 grep, 10 files total):
- `numerics/run_046_demodex_rosacea_nlrp3.md` (foundational Demodex/
  endosymbiont mechanism run; carries R-Heyndrickxia audit note)
- `numerics/run_028_topical_rapamycin_loop1.md`
- `numerics/run_048_gasdermin_keratinocyte_loop2.md`
- `numerics/run_058_hyaluronic_acid_tlr4_damp.md`
- `numerics/run_072_ceramide_barrier_tlr.md`
- `numerics/run_093_trpa1_4hne_loop4_m8.md`
- `attempts/attempt_021_audit_numerics_sample_046_100_170.md`
- `results/protocol_integration.md`
- `thewall_extensions_archive.md`
- `gap_extensions_archive.md`

**Affected files in other subdirs** (per Fire 17/18/20 cross-subdir grep):
- `medical/blepharitis/results/claim_audit_2026-04-15.md` (C27 entry —
  this is where the rename was first identified for this corpus)
- `medical/persistent_organisms/PROBLEM.md` (1 mention, secondary —
  lid-margin polymicrobial context, not load-bearing mechanistic claim)
- `biology/evolution/results/host_coevolution.md` (3 mentions in TLR
  variant context, secondary mentions)
- `biology/evolution/attempts/attempt_010_malassezia_cutibacterium
  _evolution.md` (1 mention, secondary)
- ✅ `biology/evolution/attempts/attempt_009_demodex_evolution.md`
  **already uses correct *Heyndrickxia oleronia* with Gupta 2020
  attribution** — best-practice example written by an instance with
  taxonomy-discipline; no correction needed. The cross-subdir reach
  for this rename is now exhaustively verified.

**Cross-subdir verification status (Fire 20)**: scope is now fully
mapped. Total ~14 files corpus-wide reference the organism. 1 file
(attempt_009) uses correct current naming. 13 files use legacy
*Bacillus oleronius* — all preserved per the no-mass-edit disposition.
Readers grep this TAXONOMY_NOTES file for current taxonomy.

**Disposition**: per Convention Beats Instruction, individual per-run
files are NOT being mass-edited with the rename. They preserve
historical naming for readability + commit-history clarity. Readers
encountering "*Bacillus oleronius*" in any dysbiosis file should
treat it as referring to *Heyndrickxia oleronia*. Future-written runs
should use "*Heyndrickxia oleronia* (formerly *Bacillus oleronius*)"
on first mention to maintain compatibility with both literatures.

**Mechanism claims unaffected**: the B. oleronius / H. oleronia
40 + 83 kDa protein fractions (Lacey 2007 *Br J Dermatol* PMID
17596156) and 73% rosacea vs 29% control PBMC stimulation findings
are unaffected by the rename — only the genus name has changed.

---

## Verified-clean taxonomy claims (no correction needed)

These are taxonomy-related claims in the corpus that have been
checked and are correct as written.

### *Demodex folliculorum* / *Demodex brevis* — names current

Both species names are current per LPSN (List of Prokaryotic Names
with Standing in Nomenclature) and standard arachnology references.
The "Demodex has no anus" claim that appears in some legacy
secondary literature was overturned by **Smith et al. 2022** (EM +
anus-development genes). Dysbiosis runs do NOT cite this refuted
claim (Fire 18 grep clean). Per blepharitis claim_audit C26.

### *Cutibacterium acnes* (formerly *Propionibacterium acnes*)

The 2016 reclassification (Scholz & Kilian 2016 *Int J Syst Evol
Microbiol* PMID 27006333) split *Propionibacterium* into multiple
new genera, with the human skin-associated species moving to
*Cutibacterium*. Dysbiosis runs (e.g., run_038
cutibacterium_acnes_loop4) use the current name. No correction needed.

---

## Future taxonomy-correction template

When a new rename / reclassification is identified, add an entry under
"Active taxonomy corrections" with:

1. Old name → New name
2. Reclassification source (author, year, journal, PMID)
3. Mapping notes (etymology if unusual, period of overlap)
4. Affected files list (run grep at time of discovery)
5. Disposition (mass-edit vs grep-and-find)
6. Mechanism-claim impact (does the rename affect any cited findings?)

Then optionally add cross-references to per-run audit notes. The
v5 Convention-Beats-Instruction discipline keeps this file
authoritative; per-run notes are for the highest-impact runs only.

---

## Cross-references

- `CITATION_DISCIPLINE.md` (Fire 88) — companion citation-accuracy doc
- `VERIFIED_REFS.md` (Fires 78-90 + Fires 17-18) — PMID-anchored
  references including the Phase 4b audit history
- `numerics/run_046_demodex_rosacea_nlrp3.md` — foundational Demodex
  run with full R-Forton + R-Heyndrickxia audit notes
- `medical/blepharitis/results/claim_audit_2026-04-15.md` — original
  source of C27 Heyndrickxia finding (cross-audit convergence event #3
  per Fire 18)
