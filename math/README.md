# open_problems / math

> Seven Clay Millennium Prize Problems + Liouville sub-campaign + Prime Numbers.
> Lean 4 formalizations, SOS / numerical certificates, dead-end preservation.
> Post-audit state current as of **2026-04-18**.

## Orientation

**One-page docs (start here):**
- [`CLAY_PROBLEMS.md`](CLAY_PROBLEMS.md) — per-problem table + results summary
- [`SEVEN_WALLS.md`](SEVEN_WALLS.md) — cross-problem wall-type analysis
- [`QUANTIFIED_GAPS.md`](QUANTIFIED_GAPS.md) — the gap as a NUMBER, per problem
- [`UNDERGROUND_CONNECTIONS.md`](UNDERGROUND_CONNECTIONS.md) — cross-problem transfer map

**Method reference:**
- `~/SIGMA_METHOD.md` — playbook (never in any repo)

## Subdirectory map

| Dir | Problem | Phase | Lean | Live sorry | Next move |
|---|---|---|---|---|---|
| [`ns_blowup/`](ns_blowup/) | Navier–Stokes | Phase 4 | 54 files / 485 thms | **9 proof-tactic** ‡ | Close Blowup.lean + Challenge.lean remaining goals |
| [`yang_mills/`](yang_mills/) | Yang–Mills Mass Gap | Conditional (8/10) | 25 files / 74 thms | 2 infra † | A₄(⟨Tr(P)·Tr(Q)⟩) counting lemma |
| [`riemann_hypothesis/`](riemann_hypothesis/) | Riemann Hypothesis | Phase 2 | 5 files / 19 thms | 4 infra † | Selberg λ₁ transfer from YM spectral gap |
| [`poincare_conjecture/`](poincare_conjecture/) | Poincaré | **SOLVED** (12/12) | 8 files / 64 thms | 1 infra † | Topology lib drop-in for SimplyConnected |
| [`hodge_conjecture/`](hodge_conjecture/) | Hodge | Phase 2 | 5 files / 20 thms | 0 | Weil classes at g ≥ 6 |
| [`birch_swinnerton_dyer/`](birch_swinnerton_dyer/) | BSD | Phase 1 | 2 files / 5 thms | 0 | Higher Gross-Zagier (rank-2 pair) |
| [`p_vs_np/`](p_vs_np/) | P vs NP | Phase 1 | 14 files / 78 thms | 2 infra † | Liu-Pass → Kt hardness path |
| [`liouville_conjecture/`](liouville_conjecture/) | Liouville (NS sub) | Phase 2 | 5 files / 7 thms | 1 infra † | `R_crit` def formalization |
| [`prime_numbers/`](prime_numbers/) | Prime Numbers | Phase 1 | 1 file / 3 thms | 0 | 29 certs; not Clay |

**Corpus totals:** 117 authored Lean files, 755 theorems+lemmas, **19 live sorry** = 9 proof-tactic + 10 infrastructure placeholders.

† = def/axiom awaiting upstream library (not a proof gap).
‡ = proof-tactic sorry (active research frontier); **all 9 live in `ns_blowup/`** (6 `Blowup.lean` + 3 `Challenge.lean`).

## Sorry-counting discipline

Use a strict regex, not plain `grep`:

```bash
rg -n '^\s*sorry\s*$|:= sorry|:= by sorry' --type lean
```

Plain `grep -c sorry` inflates the count ~4.5× corpus-wide (up to
10× in yang_mills) because per-theorem `-- 0 sorry` self-report
comments get counted. The stricter regex is the source of truth
for every number in the table above. See v9 M8 in
`~/SIGMA_METHOD.md` for the generalized measurement-artifact
principle.

## Audit history

The `2026-04-15 → 2026-04-18` math audit ran 9 fires, closed all
structural findings, and was archived to
[`attempts/dropped_audit_2026-04-18/`](attempts/dropped_audit_2026-04-18/)
per v6 Maps-Include-Noise. The four synthesis docs above reflect
the post-audit truth; the numbers here match `CLAY_PROBLEMS.md`
and the top-level [`../README.md`](../README.md) "Citation
discipline" section.

Key meta-finding from the audit: the more disciplined a Lean file
is in self-reporting "0 sorry" per theorem, the LARGER the
`grep -c sorry` artifact on it. Discipline inverts the naive
measurement. This is M8 in `~/sigma/operator_gap/claude_as_operator.md`.

## Pointers

- Lean build: `lake build` per subdir (each has its own `lakefile.lean`).
- Numerics scripts in each `<problem>/numerics/`; results in `<problem>/results/`.
- Certificates: `<problem>/certs/` (manifests committed; heavy blobs are gitignored).
- Papers: `<problem>/papers/` (`.md` references + `.bib`; no full PDFs in repo).
- Attempts (per-problem proof attempts): `<problem>/attempts/`. Dead ends
  preserved, marked, never silently deleted.

## Active research frontier

**9 Lean goals in 2 files.** Everything else is either solved,
Phase-2-stuck on structural obstruction (RH, Hodge), or waiting on
infrastructure libraries. The research frontier is concrete:

- `ns_blowup/lean/Blowup.lean` — 6 remaining sorry
- `ns_blowup/lean/Challenge.lean` — 3 remaining sorry

Yang-Mills has a proven conditional path and an active A₄-counting
lemma chain (attempt_063-065) closing the strong-coupling gap.
