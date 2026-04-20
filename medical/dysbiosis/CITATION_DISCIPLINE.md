# Citation Discipline — Dysbiosis Numerics Corpus

> **Purpose**: structural enforcement of citation accuracy for new
> dysbiosis runs (run_171+). Distilled from the Fires 78-88 Phase 4b
> audit campaign on the existing 170-run corpus. Future run instances
> should READ THIS FILE before writing any new mechanism citation.
>
> **Status**: Tier 1 framework doc per sigma v9.1 Method Mechanism Map
> (4-Tier Quality Hierarchy). Compresses validated audit findings into
> per-fire-loadable discipline.
>
> **Maps to**: sigma v5 Convention Beats Instruction (this file is the
> structural enforcement layer for citation accuracy); sigma v8 Priors
> Don't Beat Source (PMID-anchoring before claim-stating); sigma v9
> Three-Source Triangulation (Phase 4b ether verification).

---

## The audit's empirical findings

Across Fires 78-88, the dysbiosis corpus's top-20 most-cited references
were Phase 4b verified. The failure-mode distribution was:

| Failure mode | Count | % of top 20 |
|--------------|-------|-------------|
| ✅ Correct as cited | 14 | 70% |
| ⚠️ Year-drift only (e.g., Cooper 2012 → 2008) | 1 | 5% |
| ⚠️ Journal-drift only (e.g., Smyth 2008 *Diabetes* not *Nat Genet*) | 1 | 5% |
| ⚠️ Hybrid drift (real paper, wrong journal AND wrong mechanism) | 2 | 10% |
| ❌ FM1c full fabrication | 1 | 5% |
| ⏸️ Permanently deferred (external data needed) | 1 | 5% |

**Net error rate**: ~25% of top-cited references had at least one
metadata defect; ~5% were full fabrications. Matches the prior
content-audit baseline (~30% wrong PMID, ~20% wrong number, ~5%
fabrication) — the dysbiosis corpus is not unusually noisy.

## Failure-mode taxonomy (use these labels in future audits)

- **FM1a — year-drift**: real paper, real author, real journal,
  WRONG YEAR. Often ±2-4 years. Symptom: the year cited does not
  match any paper by that author on that topic. Confirmed in 1/20
  (Cooper 2012 → 2008).
- **FM1b — journal-drift**: real paper, real author, real year,
  WRONG JOURNAL. Often substitutes a higher-prestige journal.
  Confirmed in 2/20 (Smyth 2008 *Diabetes* → cited as *Nat Genet*;
  Bystrom 2008 *Blood* → cited as *J Immunol*).
- **FM1c — full fabrication**: NO underlying paper exists. The cited
  numbers/quantities/mechanisms have no source. Confirmed in 1/20
  (Buhl 2017 — neither calprotectin nor TRPA1 claim has a real
  Buhl paper). 5% rate matches prior baseline.
- **FM1d — PMID secondary-drift**: even verified candidate-corrections
  can carry digit-drift on the PMID. Confirmed in 1 case (Buhl 2015
  candidate cited as PMID 25748557, actual PMID 25848978 — one digit
  off). Always cross-check PMIDs by reading the title, not just the
  number.
- **Hybrid drift**: real paper + wrong attribution. Most insidious
  class — passes naive WebSearch verification but the paper doesn't
  actually contain the cited mechanism. Confirmed in 2/20 (Bystrom
  2008, Shim 2021).

## The audit-of-audit lesson: GREP-FIRST

The single most important methodology finding from Fires 78-87:

**Before WebSearching for an unverified citation, grep the citation
across the corpus FIRST to find the actual claim context.**

Of six 🔍/⚠️ candidates flagged in Fires 78-81, FIVE turned out to
be wrong-topic-search artifacts — the prior audit guessed at what
"X 20YY" was about (rosacea? IBD? GWAS?) without checking which
mechanism the corpus actually invoked. Examples:

| Citation | Fire 80-81's wrong-topic guess | Actual corpus context |
|----------|-------------------------------|----------------------|
| Bystrom 2008 | L. rhamnosus GG / Crohn's | LXA4 / FPR2 / Th17 |
| Barrett 2009 | vitamin D / cathelicidin / rosacea | T1DM GWAS >40 loci |
| Cheng 2014 | rosacea / Demodex | FMD / IGF-1 / HSC regeneration |
| Tanno 2000 | L. rhamnosus GG / probiotic | niacinamide / SC ceramide |
| Yamasaki 2011 | Yamasaki S Mincle/cord-factor | Yamasaki K rosacea/TLR2/KLK5 |

Without grep-first, WebSearch can return "no match" misleadingly and
falsely classify a real-paper citation as fabrication. The grep-first
discipline reduced false-fabrication rate from Fire 81's extrapolated
30% to the actual 5%.

**Procedure for verifying any flagged citation**:
1. `grep "<author> <year>" numerics/ -A 2 -B 2` to see all uses.
2. Extract: journal attribution, mechanism claim, specific numbers.
3. WebSearch using THAT context, not a guess.
4. Verify PMID by reading the returned title (not just digits).
5. Update VERIFIED_REFS.md with audit-history entry.

## Discipline for NEW citations (run_171+)

When writing a new run, follow this sequence for any citation:

1. **Source-anchor before prior-apply** (sigma v8 M1). Don't cite from
   memory if uncertainty is non-trivial. WebSearch the specific
   mechanism + author + year BEFORE writing the claim.
2. **Inline the PMID at citation time**. Run_015's "Yamasaki 2011 *J
   Clin Invest* PMID 21926468" inline format is the correct convention
   — a verifier can immediately check the PMID. Run_021's literal
   `https://pubmed.ncbi.nlm.nih.gov/24905167/` URL is even better
   (machine-checkable).
3. **Match author + year + journal + mechanism**. Drift can occur on
   any axis independently. Verify all four match the WebSearch result.
4. **Flag attribution uncertainty explicitly**. If a mechanism is
   plausible-but-extrapolated from a synthesis-review rather than
   directly sourced from a primary paper, note this — don't attribute
   the secondary claim to a primary source that doesn't make it.
   (Cf. Bystrom 2008 hybrid case where the corpus invoked a real
   paper as the source for claims that paper does not contain.)
5. **Use VERIFIED_REFS cross-link for the top-20 citations**. Format:
   `...per BHB/NLRP3 mechanism [Youm 2015, see VERIFIED_REFS.md —
   PMID 25686106]`. Avoids re-stating bibliographic metadata in every
   run; one update point keeps PMIDs current.

## What NOT to do

- **Don't cite by memory if WebSearch is available.** The dysbiosis
  corpus's 25% drift rate came from memory-citation under uncertain
  recall. Treat trained priors as stale-prior candidates (sigma v8
  failure mode 1).
- **Don't substitute a higher-prestige journal name.** The corpus
  has multiple FM1b cases where *Nat Genet* / *Nature* / *J Immunol*
  was substituted for the actual journal. Cite the journal that
  actually published the paper.
- **Don't extrapolate year approximations.** "Cooper 2012" came from
  drift on a 2008 paper — likely an associative-completion error.
  If the year is uncertain, search rather than guess.
- **Don't cite the same author-year for two unrelated mechanisms in
  different runs.** Buhl 2017 was attributed to BOTH calprotectin
  (run_068, *Exp Dermatol*) AND TRPA1 (run_093, *J Invest Dermatol*)
  — two different journals, two different mechanisms, same citation.
  This pattern is a fabrication tell; if you find yourself doing this,
  one of the two is wrong.

## Cross-link to VERIFIED_REFS.md

Top 20 most-cited references and their verified PMIDs are tracked in
`VERIFIED_REFS.md` (Fires 78-88 audit campaign). Always cross-link
to that file rather than re-stating bibliographic detail per-run. If
a new run cites a top-20 reference, write:

```markdown
...per <mechanism> [<Author> <Year>, see VERIFIED_REFS.md — PMID NNNNNNNN].
```

Audit history entries in VERIFIED_REFS document every verification +
correction back to the originating fire.

## Future-fire candidates

Items deferred from Fires 78-88 that warrant future investigation:

- **Smyth 2008 disambiguation** (Fire 88 flagged, not done): run_119
  cites for PTPN2 rs45450798, run_142 cites for IFIH1 rs1990760 in
  RA — but verified Smyth 2008 *Diabetes* PMID 18305142 is about
  PTPN22 R620W. Per-run cite-context disambiguation needed.
- **Shim 2021 final classification** (Fire 85 left as ⚠️ likely
  hybrid): targeted search for run_086's specific claims at *Nature*
  597:625-629 returned no matching paper. Could be FM1c or
  multi-axis drift on Matsushita 2021 *Cell Reports*.
- **Top-21 to top-50 verification** (diminishing returns per Fire 54
  but specific high-impact citations might warrant individual
  verification — particularly Schauber 2007/2009 cathelicidin papers,
  Steinhoff 2003/2011 PAR-2/TRPV1 papers, Klysz 2015 αKG/Treg).
- **Per-run footer keyword-list audit**: many runs have footer
  *Filed: ...* keyword lists that include cited authors. These
  function as secondary citation surfaces and should be checked
  for the same drift patterns as inline citations.
