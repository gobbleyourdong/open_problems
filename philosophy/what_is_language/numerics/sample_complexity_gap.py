"""
sample_complexity_gap.py — Iteration 1
Numerical Track: what_is_language

Core claim under test: the sample-complexity gap between human and LLM language
acquisition is ~10^6 tokens. This tool:

1. Quantifies the gap from published scaling law data.
2. Models what compression multiplier each candidate mechanism (embodiment,
   curriculum learning, UG prior, active learning, instruction tuning)
   would need to contribute to close the full gap.
3. Identifies the residual gap after stacking all known mechanisms.
4. Produces a "gap budget" that informs what the LLM must still lack.

Data sources used:
- Chinchilla scaling laws (Hoffmann et al. 2022): loss ~ N^-0.076 * D^-0.095
- Human child input estimates (Hart & Risley 1995, Snow 1994, and follow-ups)
- LLM fluency thresholds inferred from capability emergence literature
- Mechanism compression estimates from the literature (rough orders of magnitude)

Usage:
    python sample_complexity_gap.py --report
    python sample_complexity_gap.py --sweep
    python sample_complexity_gap.py --budget
"""

import argparse
import json
import math

# ---------------------------------------------------------------------------
# Human acquisition parameters
# ---------------------------------------------------------------------------

# Hart & Risley 1995: professional-family children hear ~2100 words/hour
# Active hours (waking, language-exposed): ~10 hours/day
# Words heard per year: 2100 * 10 * 365 ≈ 7.7M
# By age 5 (60 months, counting from birth): ≈ 7.7M * 5 ≈ 38M
# But much is non-linguistic; linguistically relevant tokens: ~30% → 10M
# Other estimates (Snow 1994): ~10-50 million tokens by age 5
# Central estimate: 3e7 (30 million) words ≈ 3e7 tokens (tokens ≈ words at child vocab)
# Upper bound: 1e8
# Lower bound: 1e7

HUMAN_TOKENS_CENTRAL = 3e7       # 30 million tokens to fluency (age ~5)
HUMAN_TOKENS_LOW     = 1e7       # Conservative lower bound
HUMAN_TOKENS_HIGH    = 1e8       # Upper bound (heavy input environment)

# ---------------------------------------------------------------------------
# LLM acquisition parameters
# ---------------------------------------------------------------------------

# Training tokens for LLMs that achieve conversational fluency:
# - GPT-3 (2020): 300B tokens — early fluency
# - Chinchilla (2022): 1.4T tokens
# - LLaMA-2 (2023): 2T tokens
# - LLaMA-3 (2024): 15T tokens
# - Frontier 2025-26: ~10T-100T tokens
# Note: "fluency" benchmark differs from human; we use rough alignment

LLM_TOKENS = {
    "GPT-3 (2020)":        3.0e11,
    "Chinchilla (2022)":   1.4e12,
    "LLaMA-2 (2023)":      2.0e12,
    "LLaMA-3 (2024)":      1.5e13,
    "Frontier 2025-26":    1.0e13,   # median estimate
}

LLM_TOKENS_CENTRAL = 1.0e13   # frontier 2025-26 central

# ---------------------------------------------------------------------------
# Known compression mechanisms and literature estimates
# ---------------------------------------------------------------------------

# Each entry: (name, compression_factor, evidence_quality, source)
# compression_factor: how many times fewer tokens needed with this mechanism
# evidence_quality: 'strong', 'medium', 'weak', 'theoretical'

MECHANISMS = [
    {
        "name": "Multimodal grounding (vision+audio+action)",
        "factor": 10,
        "evidence": "medium",
        "source": "Flamingo-era VL bootstrap studies; 10× task-level compression",
        "notes": (
            "VL models like Flamingo show ~10× sample efficiency gains on visual "
            "tasks. Linguistic compression unclear. Probably domain-specific."
        ),
    },
    {
        "name": "Curriculum learning (easy-to-hard, child-directed speech)",
        "factor": 5,
        "evidence": "medium",
        "source": "Bengio 2009 curriculum learning; child-directed speech studies",
        "notes": (
            "Child-directed speech is simpler, shorter, more redundant than adult "
            "speech. LLMs train on filtered but not truly curated corpora. "
            "Conservative estimate: 5× from proper curriculum."
        ),
    },
    {
        "name": "Instruction tuning + RLHF feedback",
        "factor": 30,
        "evidence": "medium",
        "source": "RLHF literature; InstructGPT; 10-100× at task level",
        "notes": (
            "RLHF dramatically compresses task learning but much of the gain is "
            "post-training alignment, not pretraining sample efficiency. "
            "Central estimate: 30× on task performance, maybe 10× on core language."
        ),
    },
    {
        "name": "Active / curiosity-driven learning",
        "factor": 5,
        "evidence": "weak",
        "source": "Active learning literature; synthetic benchmarks; 2-10×",
        "notes": (
            "Children are active learners, asking questions, seeking clarification. "
            "Marginal gain on core language unclear."
        ),
    },
    {
        "name": "Universal Grammar / inductive bias",
        "factor": 100,
        "evidence": "theoretical",
        "source": "Chomsky 1965, Yang 2002; child language acquisition theory",
        "notes": (
            "If UG exists, the space of possible grammars is dramatically smaller. "
            "Yang 2002's variational learner acquires grammar in thousands of sentences. "
            "The factor is highly uncertain; could be 10-10000×. "
            "This is the PRIMARY candidate for closing the residual gap."
        ),
    },
    {
        "name": "Prior world knowledge (object permanence, causality, agency)",
        "factor": 20,
        "evidence": "weak",
        "source": "Spelke core knowledge; Bayesian cognitive models",
        "notes": (
            "Children arrive with extensive prior knowledge about physics, social "
            "dynamics, causality. This compresses language-learning by providing "
            "interpretive scaffolding. Estimate highly uncertain."
        ),
    },
]

# ---------------------------------------------------------------------------
# Gap analysis functions
# ---------------------------------------------------------------------------

def compute_gap(human_tokens=HUMAN_TOKENS_CENTRAL, llm_tokens=LLM_TOKENS_CENTRAL):
    """Compute the raw sample-complexity gap ratio."""
    return llm_tokens / human_tokens


def stacked_compression(mechanisms=None):
    """
    Compute the total compression from stacking all known mechanisms.
    Returns (total_factor, breakdown_list).
    """
    if mechanisms is None:
        mechanisms = MECHANISMS
    total = 1.0
    breakdown = []
    for m in mechanisms:
        total *= m["factor"]
        breakdown.append({
            "name": m["name"],
            "factor": m["factor"],
            "cumulative": total,
        })
    return total, breakdown


def residual_gap(human_tokens=HUMAN_TOKENS_CENTRAL,
                 llm_tokens=LLM_TOKENS_CENTRAL,
                 mechanisms=None):
    """
    Gap remaining after accounting for all known compression mechanisms.
    residual = raw_gap / stacked_compression
    """
    raw = compute_gap(human_tokens, llm_tokens)
    total_compression, _ = stacked_compression(mechanisms)
    return raw / total_compression


def gap_report(human_tokens=HUMAN_TOKENS_CENTRAL,
               llm_tokens=LLM_TOKENS_CENTRAL):
    """Print a full gap analysis report."""
    raw_gap = compute_gap(human_tokens, llm_tokens)
    total_comp, breakdown = stacked_compression()
    res = residual_gap(human_tokens, llm_tokens)

    print("=" * 72)
    print("SAMPLE-COMPLEXITY GAP ANALYSIS — what_is_language")
    print("=" * 72)
    print(f"\n  Human tokens to fluency:  {human_tokens:.2e}  (central estimate)")
    print(f"  LLM tokens to fluency:    {llm_tokens:.2e}  (frontier 2025-26)")
    print(f"  Raw gap (ratio):          {raw_gap:.2e}  (~10^{math.log10(raw_gap):.1f})")
    print()
    print("Known compression mechanisms (multiplicative stack):")
    print("-" * 72)
    for b in breakdown:
        print(
            f"  {b['name'][:50]:<50}  ×{b['factor']:<5}  "
            f"(cumulative: {b['cumulative']:.1e})"
        )
    print("-" * 72)
    print(f"  Total stacked compression:  {total_comp:.2e}  (~10^{math.log10(total_comp):.1f})")
    print()
    print(f"  Residual gap after known mechanisms:  {res:.2e}  (~10^{math.log10(max(res,1e-10)):.1f})")
    print()

    if res > 1:
        print(
            f"  CONCLUSION: Known mechanisms account for {total_comp:.1e}× compression,\n"
            f"  closing {math.log10(total_comp):.1f} of the {math.log10(raw_gap):.1f} log-orders.\n"
            f"  Residual gap of {res:.1e}× remains UNEXPLAINED.\n"
            f"  This is the compression the theory of language must account for."
        )
    else:
        print(
            f"  CONCLUSION: Known mechanisms MORE than close the gap.\n"
            f"  The gap could be explained by a subset of the mechanisms."
        )

    print()
    print("Sensitivity to human token estimate:")
    print("-" * 72)
    for label, ht in [
        ("Low (1e7)", HUMAN_TOKENS_LOW),
        ("Central (3e7)", HUMAN_TOKENS_CENTRAL),
        ("High (1e8)", HUMAN_TOKENS_HIGH),
    ]:
        g = compute_gap(ht, llm_tokens)
        r = residual_gap(ht, llm_tokens)
        print(
            f"  {label:<18}  raw gap={g:.1e}  "
            f"residual={max(r,1e-10):.2e}  (10^{math.log10(max(r,1e-10)):.1f})"
        )

    print()
    print("Sensitivity to LLM token estimate:")
    print("-" * 72)
    for label, lt in LLM_TOKENS.items():
        g = compute_gap(human_tokens, lt)
        r = residual_gap(human_tokens, lt)
        print(
            f"  {label:<22}  raw gap={g:.1e}  "
            f"residual={max(r,1e-10):.2e}  (10^{math.log10(max(r,1e-10)):.1f})"
        )


def budget_report():
    """
    Gap budget: what compression factor each mechanism needs to contribute to
    close the full gap.

    Computes required factor for each mechanism when all others contribute their
    literature estimate (holding-one-out analysis).
    """
    raw_gap = compute_gap()
    total_comp, _ = stacked_compression()
    res = residual_gap()

    print("=" * 72)
    print("GAP BUDGET — holding one mechanism out")
    print("How large must each factor be, given the others contribute as estimated?")
    print("=" * 72)
    print(f"\n  Raw gap: {raw_gap:.2e}  Total currently closed: {total_comp:.2e}  Residual: {res:.2e}")
    print()

    for i, m in enumerate(MECHANISMS):
        other_comp = total_comp / m["factor"]
        needed_factor = raw_gap / other_comp
        print(
            f"  {m['name'][:55]:<55}\n"
            f"    Current estimate: ×{m['factor']:<8}  "
            f"Needed to close gap alone: ×{needed_factor:.1e}  "
            f"(10^{math.log10(needed_factor):.1f})\n"
            f"    Evidence: {m['evidence']}\n"
        )


def sweep_report():
    """
    2D sweep: show residual gap over a grid of (human_token, llm_token) values.
    """
    print("=" * 72)
    print("RESIDUAL GAP SWEEP (residual = raw_gap / stacked_compression)")
    print("rows = human tokens, cols = LLM tokens")
    print("=" * 72)

    human_vals = [1e7, 3e7, 1e8]
    llm_vals = [3e11, 1e12, 1e13, 1e14]

    header = f"  {'Human↓ / LLM→':<20}" + "".join(f"  LLM={lt:.0e}" for lt in llm_vals)
    print(header)
    print("-" * 72)
    for ht in human_vals:
        row = f"  Human={ht:.0e}         "
        for lt in llm_vals:
            r = residual_gap(ht, lt)
            row += f"  {r:.1e}"
        print(row)
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Sample-complexity gap calculator (Odd track, what_is_language)"
    )
    parser.add_argument("--report", action="store_true",
                        help="Full gap report with sensitivity analysis")
    parser.add_argument("--budget", action="store_true",
                        help="Gap budget: how much each mechanism needs to contribute")
    parser.add_argument("--sweep", action="store_true",
                        help="2D sweep of human/LLM token estimates")
    parser.add_argument("--all", action="store_true",
                        help="Run all reports")
    args = parser.parse_args()

    if args.all or args.report:
        gap_report()
        print()
    if args.all or args.budget:
        budget_report()
        print()
    if args.all or args.sweep:
        sweep_report()

    if not any([args.report, args.budget, args.sweep, args.all]):
        parser.print_help()


if __name__ == "__main__":
    main()
