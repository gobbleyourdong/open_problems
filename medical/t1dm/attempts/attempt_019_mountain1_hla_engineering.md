# Attempt 019: Mountain 1 Deep Dive — HLA Engineering Beyond Knockout

## Going Deeper on Mountain 1

Sana's approach (attempt 007) knocks out HLA entirely — makes cells invisible. But invisible cells have a problem: NK cells kill cells that LACK HLA (the "missing self" hypothesis). Sana compensates with CD47 ("don't eat me"), but this is a patch, not a solution.

## The Next Generation: Selective HLA Engineering

Instead of removing ALL HLA, what if you:
1. Keep HLA-E (inhibits NK cells naturally — no CD47 needed)
2. Remove only HLA-A/B/C classical class I (prevents CD8+ T cell recognition)
3. Remove HLA class II (prevents CD4+ T cell recognition)
4. Express only non-polymorphic HLA: HLA-E, HLA-G (placental tolerance molecule)

This is "hypoimmune 2.0" — cells that are invisible to adaptive immunity but visible enough to NK cells to avoid "missing self" killing.

## HLA-G: The Placental Solution

The fetus is a foreign body. Half its HLA comes from the father. The mother's immune system should reject it. It doesn't. Why?

**HLA-G.** Expressed on trophoblast cells at the maternal-fetal interface.
- Inhibits NK cell cytotoxicity
- Induces Treg differentiation
- Suppresses CD4+ and CD8+ T cell proliferation
- Creates LOCAL tolerance without systemic immunosuppression

**What if beta cells expressed HLA-G?**

The beta cell would create its own tolerogenic microenvironment. No drugs. No devices. The cell itself would say "don't attack me" in the language the immune system already understands — the same language the placenta uses.

## Status of HLA-G Engineering

- Preclinical proof-of-concept in islet transplant models (mouse): HLA-G-expressing islets survive longer without immunosuppression
- CRISPR delivery of HLA-G expression cassette into stem cell-derived beta cells: feasible (same gene editing pipeline as Sana)
- Not yet in human trials for any cell therapy
- Concern: HLA-G is expressed by some cancers to evade immunity. Need a kill switch.

## The Kill Switch

Every engineered cell therapy needs a safety valve:
- **iCasp9 (inducible caspase 9)**: A suicide gene. Administer a small molecule (AP1903/rimiducid) → all engineered cells die within hours. Already used in CAR-T therapy.
- **HSV-TK (thymidine kinase)**: Ganciclovir sensitivity. Older technology, proven in clinical use.

Engineering: HLA-KO + HLA-G expression + HLA-E retention + iCasp9 kill switch → a beta cell that:
- Is invisible to adaptive immunity (no HLA-A/B/C, no class II)
- Is tolerated by NK cells (HLA-E + HLA-G)
- Induces local Treg formation (HLA-G)
- Can be destroyed on command if anything goes wrong (iCasp9)

## What This Adds to Mountain 1

| Generation | Approach | Problem |
|-----------|----------|---------|
| 1st | Transplant + immunosuppression | Drugs forever |
| 2nd | HLA-KO + CD47 (Sana) | NK cell risk, no active tolerance |
| 3rd | HLA-KO + HLA-G + HLA-E + iCasp9 | Active local tolerance, kill switch |

3rd gen hasn't been built yet. It's the logical next step.

## The Gap on Mountain 1 (Refined)

Mountain 1's gap is no longer "can we protect cells from immunity?" (answered: yes, multiple ways). The gap is: **which immune evasion strategy is safest and most durable long-term?** This is a clinical validation gap, not a conceptual one. Multiple solutions exist. We need 10-year safety data on at least one.

## Status: CONCEPTUAL — 3rd gen HLA engineering not yet built, but all components exist
