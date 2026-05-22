# Cutting-Edge Tools for the P0 Metagenome (scan 2026-05-22)

GitHub repos cloned to `~/tools/metagenomics/`, ranked by how directly they answer P0's *open*
questions — and notably, the top two **bypass the DIAMOND/ARM block** that stopped HUMAnN.

| Tool | Repo | What it is (why cutting-edge) | Answers for P0 | ARM status |
|------|------|-------------------------------|----------------|------------|
| **sylph** ⭐ | [bluenote-1577/sylph](https://github.com/bluenote-1577/sylph) | ANI/k-mer profiler, *Nat Biotech* Aug 2025; CAMI2 winner; **30× more gut viral** than RefSeq; <1 min / 16 GB | **Fixes the 8% classification ceiling** → tight 6-metric numbers + a vastly better phageome/CrAssphage quantification | installing (Rust/cargo — ARM-safe) |
| **MICOM** ⭐ | [micom-dev/micom](https://github.com/micom-dev/micom) | Community metabolic modeling; predicts **personalized SCFA flux from abundance alone** (no gene search) | **THE elegant unblock** — answers the H₂S-vs-butyrate question directly from our taxonomy, *no DIAMOND/HUMAnN needed*. Predicts butyrate/propionate/acetate flux (and H₂S given sulfate-reducer models). Note: it predicted ↓butyrate in diabetics, restored by metformin | installing (pip — feasible) |
| **inStrain** | [MrOlm/inStrain](https://github.com/MrOlm/inStrain) | Strain-level SNV/microdiversity from read alignments | The *definitive* word on E. coli vs Shigella (SNV-level, beyond our reads+contigs agreement) | python (feasible) |
| **geNomad** | [apcamargo/genomad](https://github.com/apcamargo/genomad) | Virus + plasmid ID, *Nat Methods* 2023; supersedes VirSorter2 for many uses | Refines the 2,008-phage virome; flags **plasmid-borne AMR** (antibiotic-history link) | python (feasible) |
| **BugSigDB** | [waldronlab/BugSigDBStats](https://github.com/waldronlab/BugSigDBStats) | Curated differential-abundance signatures across host-microbiome studies (*Nat Biotech* 2023) | **Cross-reference P0's profile against published T1DM/dysbiosis signatures** — does P0 match the known disease signature? | R/Bioconductor (heavier) |

**Not cloned but noted** for the AMR→antibiotic-history question (why Akkermansia is 0%):
**AMRFinderPlus** (NCBI) / **RGI-CARD** — call resistance genes + their drug classes from the assembly.

## The two highest-value moves
1. **sylph re-profile** — re-run taxonomy with sylph against its GTDB+viral DB. This both *fixes the
   8% caveat* (the main limitation of our Kraken2 run) and gives a much deeper phageome. Single
   highest-leverage upgrade to the existing analysis.
2. **MICOM SCFA modeling** — feed our abundance table into MICOM → predicted butyrate/propionate/
   H₂S flux. This is the *functional answer we were going to get from HUMAnN* (butyrate axis), but
   from community modeling instead of DIAMOND gene search — so it runs natively on the Spark.

Together these close both gaps the Spark pipeline left open (classification depth + functional layer)
without needing the x86 offload.

## Run plan (once installed)
- `sylph sketch` the trimmed reads → `sylph profile` vs GTDB-r220 + sylph viral DB → re-derive 6 metrics + CrAssphage.
- MICOM: taxonomy table (from sylph/Bracken) + AGORA2 model DB → `micom.workflows.build` + `grow` → SCFA/H₂S fluxes.
- inStrain: map reads to the E. coli reference → SNV profile → E. coli vs Shigella call.
- BugSigDB: pull T1DM/dysbiosis signatures → score P0's profile against them.

## Install status (2026-05-22)
- **sylph 0.9.0** ✅ installed & runs native aarch64 (conda; Rust binary has a real ARM build). Env `sylph`.
- **MICOM 0.39.0** ✅ installed native aarch64 (pip; bundled HiGHS solver — no CPLEX/Gurobi). Env `micom`.
- sylph **GTDB-R220 DB** (~13 GB) + **viral DB** downloading → enables the re-profile.
- inStrain / geNomad / BugSigDB: cloned, not yet installed.

*Cloned 2026-05-22 to ~/tools/metagenomics/ (outside the repo).*
