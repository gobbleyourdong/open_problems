# Infertility — Published Statistics Summary

**Disease:** Infertility (Male + Female Factor)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Note:** Infertility is NOT a CVB disease per se, but CVB orchitis (campaign disease #11) is a known male fertility cause. Protocol components directly affect sperm and oocyte quality.

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Global affected couples | ~72 million | WHO 2023 |
| Prevalence (couples) | ~15% | WHO 2023 |
| Male factor only | ~40% | WHO 2023 |
| Female factor only | ~40% | WHO 2023 |
| Combined/unexplained | ~20% | WHO 2023 |
| Annual IVF cycles worldwide | ~2 million | ESHRE 2022 |
| IVF success rate per cycle (age <35) | ~30-40% | SART, CDC ART report 2021 |
| US annual cost of infertility treatment | ~$5 billion | ASRM |

## Male Factor Data

| Parameter | Normal | Infertile | Source |
|-----------|--------|-----------|--------|
| Sperm concentration | >16 million/mL | <16 million/mL | WHO 2021 criteria |
| Total motility | >42% | <42% | WHO 2021 |
| Progressive motility | >30% | <30% | WHO 2021 |
| Normal morphology | >4% | <4% | WHO/Kruger criteria |
| DNA fragmentation | <15% | >25% (borderline) | DFI |

## CVB Orchitis → Male Infertility Link

| Outcome | Prevalence After CVB Orchitis |
|---------|-------------------------------|
| Testicular atrophy (unilateral) | 30-50% (severe orchitis) |
| Oligospermia | ~30% (bilateral) |
| Azoospermia | 5-10% (bilateral severe) |
| CVB contribution to male infertility | ~5% |

Source: `orchitis/numerics/data_summary.md`, cross_disease_burden_results.json

## Protocol Components Relevant to Infertility

| Component | Sperm Effect | Oocyte Effect | Evidence |
|-----------|-------------|---------------|---------|
| FMD (caloric restriction) | Reduces oxidative stress in spermatogonia | Improves oocyte mitochondrial function | Mouse data; limited human data |
| Vitamin D (optimization) | Sperm motility improvement | Ovarian reserve marker | Meta-analysis: OR 2.0 for clinical pregnancy with adequate Vit D |
| Fluoxetine | CAUTION — SSRIs associated with DNA fragmentation (some data) | ? | Specific SSRI sperm effects contested |
| Anti-inflammatory diet | Reduces seminal cytokines | Reduces endometrial inflammation | Observational data |
| Colchicine | Anti-inflammatory in reproductive tract | ? | Anecdotal |

**Key caveat on fluoxetine:** Some data suggests SSRIs, including fluoxetine, may increase sperm DNA fragmentation. For male infertility specifically, the protocol's fluoxetine component needs careful evaluation against alternative antivirals.

## Female Factor Key Statistics

| Condition | Prevalence in Infertility |
|-----------|--------------------------|
| Ovulatory dysfunction (PCOS, hypothalamic) | ~25% |
| Tubal factor (PID, endometriosis) | ~20% |
| Uterine factor (fibroids, polyps) | ~10% |
| Diminished ovarian reserve | ~10% |
| Endometriosis | ~25-50% of infertile women (by laparoscopy) |
| Unexplained | ~30% |

## Cross-Reference

- `/home/jb/open_problems/medical/infertility/PROBLEM.md` — full analysis
- `/home/jb/open_problems/medical/orchitis/numerics/data_summary.md` — CVB orchitis data
- Campaign note: CVB orchitis prevention via vaccine would prevent ~5% of male infertility cases
