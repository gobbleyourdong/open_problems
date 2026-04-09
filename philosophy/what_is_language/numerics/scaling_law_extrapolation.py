"""
scaling_law_extrapolation.py — Cycle 2
Numerical Track: what_is_language

Uses the Chinchilla scaling laws (Hoffmann et al. 2022) to:
1. Extrapolate what training token count D achieves human-equivalent
   language performance on a benchmark.
2. Compute the gap as a function of model size N and performance threshold.
3. Check whether the "optimal" Chinchilla compute point already accounts
   for the efficiency gap, or whether the gap is a fixed offset.

Chinchilla scaling law:
  L(N, D) = E + A/N^alpha + B/D^beta
  where:
    E = 1.69   (irreducible entropy floor, nats)
    A = 406.4
    B = 410.7
    alpha = 0.336
    beta  = 0.283

Human language performance on BLiMP (grammatical acceptability):
  Adults: ~94% accuracy (Warstadt et al. 2019)
  GPT-2 (1.5B): ~67%
  GPT-3 (175B): ~86%
  GPT-Neo 20B: ~89%
  Frontier models ~2024: ~96-98% (surpassing adult average)

This script:
  - Plots L(N, D) for fixed N (frontier scale) as a function of D
  - Finds D such that L(N_frontier, D) matches the loss implied by human
    performance (using a rough perplexity-accuracy mapping)
  - Computes the ratio D_human_equivalent / D_human_actual to quantify
    whether humans are more efficient than predicted by the scaling law
    alone (i.e., whether the gap is in the scaling law or beyond it)

Usage:
    python scaling_law_extrapolation.py --report
    python scaling_law_extrapolation.py --sweep-N
    python scaling_law_extrapolation.py --human-D
"""

import argparse
import json
import math

# ---------------------------------------------------------------------------
# Chinchilla constants (Hoffmann et al. 2022, Table A1)
# ---------------------------------------------------------------------------

E     = 1.69    # irreducible loss floor (nats)
A     = 406.4
B     = 410.7
ALPHA = 0.336
BETA  = 0.283


def chinchilla_loss(N: float, D: float) -> float:
    """
    Predicted cross-entropy loss (nats) for a transformer of N parameters
    trained on D tokens.
    """
    return E + A / (N ** ALPHA) + B / (D ** BETA)


def loss_to_ppl(loss: float) -> float:
    """Convert nats loss to perplexity (base-e)."""
    return math.exp(loss)


def ppl_to_loss(ppl: float) -> float:
    return math.log(ppl)


# ---------------------------------------------------------------------------
# Human-equivalent performance calibration
# ---------------------------------------------------------------------------

# BLiMP accuracy → rough loss calibration.
# BLiMP is a forced-choice task; accuracy maps to loss via:
#   accuracy ~ P(correct_choice) = exp(-L_correct) / (exp(-L_correct) + exp(-L_wrong))
# For a balanced 2-choice task: accuracy = sigmoid(L_wrong - L_correct)
# At accuracy=0.94: sigmoid(delta) = 0.94 → delta = logit(0.94) ≈ 2.75 nats
# This delta is the gap between the correct and incorrect sentence's loss.
# It's a model-level property, not directly the training loss L(N,D).
# We use a rough empirical mapping from published numbers instead.

# Published (N, D, BLiMP_accuracy) data points:
# GPT-2 small (117M params, 40B tokens): ~67%
# GPT-3 6.7B (~6.7e9 params, 300e9 tokens): ~81%
# GPT-3 175B (175e9 params, 300e9 tokens): ~86%
# GPT-Neo 20B (20e9 params, 400e9 tokens): ~89%
# Human adults: ~94%

EMPIRICAL_POINTS = [
    {"name": "GPT-2-small", "N": 1.17e8, "D": 4e10, "blimp": 0.67},
    {"name": "GPT-3-6.7B",  "N": 6.7e9,  "D": 3e11, "blimp": 0.81},
    {"name": "GPT-3-175B",  "N": 1.75e11, "D": 3e11, "blimp": 0.86},
    {"name": "GPT-Neo-20B", "N": 2.0e10,  "D": 4e11, "blimp": 0.89},
]

HUMAN_BLIMP   = 0.94   # adult average
HUMAN_TOKENS  = 3.0e7  # central estimate (30M words)


def fit_loss_blimp_mapping() -> tuple[float, float]:
    """
    Fit a simple linear mapping: blimp = a * L + b
    from the empirical data points (using Chinchilla loss as x).

    Returns (a, b) such that blimp ~ a * L(N, D) + b.
    """
    xs = [chinchilla_loss(p["N"], p["D"]) for p in EMPIRICAL_POINTS]
    ys = [p["blimp"] for p in EMPIRICAL_POINTS]
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    a = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / \
        sum((x - mean_x) ** 2 for x in xs)
    b = mean_y - a * mean_x
    return a, b


def blimp_to_loss(blimp: float, a: float, b: float) -> float:
    """Invert the linear mapping: loss = (blimp - b) / a."""
    return (blimp - b) / a


def find_D_for_loss(target_loss: float, N: float,
                    D_min: float = 1e6, D_max: float = 1e20,
                    tol: float = 1e-6) -> float:
    """
    Binary search for D such that chinchilla_loss(N, D) = target_loss.
    Only valid when target_loss > E (loss floor).
    """
    if target_loss <= E:
        return float("inf")
    for _ in range(200):
        D_mid = math.exp((math.log(D_min) + math.log(D_max)) / 2)
        loss_mid = chinchilla_loss(N, D_mid)
        if abs(loss_mid - target_loss) < tol:
            return D_mid
        if loss_mid > target_loss:
            D_min = D_mid
        else:
            D_max = D_mid
    return D_mid


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

def main_report():
    a, b = fit_loss_blimp_mapping()

    print("=" * 72)
    print("CHINCHILLA SCALING LAW EXTRAPOLATION — what_is_language")
    print("=" * 72)
    print()
    print("Empirical calibration: BLiMP accuracy ~ a*L + b")
    print(f"  a = {a:.4f}  b = {b:.4f}")
    print()
    print("Predicted vs actual BLiMP accuracy:")
    for p in EMPIRICAL_POINTS:
        L = chinchilla_loss(p["N"], p["D"])
        predicted = a * L + b
        print(
            f"  {p['name']:<15}  L={L:.3f}  "
            f"predicted={predicted:.3f}  actual={p['blimp']:.3f}  "
            f"err={abs(predicted - p['blimp']):.3f}"
        )

    print()
    target_loss = blimp_to_loss(HUMAN_BLIMP, a, b)
    print(f"Human BLiMP target: {HUMAN_BLIMP:.2f} → target loss: {target_loss:.4f} nats")
    print(f"Chinchilla floor E = {E:.2f} nats")
    print()

    if target_loss <= E:
        print("  WARNING: Target loss is AT OR BELOW the irreducible floor.")
        print("  Human-equivalent performance exceeds what any LLM can reach")
        print("  by just scaling N and D (floor limited).")
        print("  This means the gap is fundamental, not a compute-scaling issue.")
        return

    print("D required to reach human-equivalent BLiMP at various model sizes:")
    print("-" * 72)
    Ns = [1e8, 1e9, 1e10, 1e11, 7e10, 4e11, 1e12]
    for N in Ns:
        D_req = find_D_for_loss(target_loss, N)
        gap_ratio = D_req / HUMAN_TOKENS
        chinchilla_D = 20 * N  # Chinchilla optimal: D = 20N
        print(
            f"  N={N:.0e}  D_required={D_req:.2e}  "
            f"ratio_to_human={gap_ratio:.1e}  "
            f"(Chinchilla D={chinchilla_D:.0e}, {'over' if chinchilla_D >= D_req else 'under'}-serves)"
        )

    print()
    print("Summary:")
    print(f"  Human tokens to BLiMP-94%: ~{HUMAN_TOKENS:.0e}")
    N_frontier = 7e10  # ~70B (representative frontier model)
    D_frontier = find_D_for_loss(target_loss, N_frontier)
    print(f"  LLM tokens for same BLiMP (N=70B): ~{D_frontier:.2e}")
    if D_frontier != float("inf"):
        print(f"  Gap: {D_frontier/HUMAN_TOKENS:.1e}×  (~10^{math.log10(D_frontier/HUMAN_TOKENS):.1f})")
    else:
        print("  Gap: unreachable (target below floor)")


def sweep_N():
    a, b = fit_loss_blimp_mapping()
    target_loss = blimp_to_loss(HUMAN_BLIMP, a, b)

    if target_loss <= E:
        print(f"Target loss {target_loss:.4f} is at or below floor {E}. Gap is fundamental.")
        return

    print("=" * 72)
    print("N SWEEP: D required to match human BLiMP across model scales")
    print("=" * 72)
    print(f"Target loss = {target_loss:.4f}  (human BLiMP={HUMAN_BLIMP:.2f})")
    print(f"Human tokens = {HUMAN_TOKENS:.0e}\n")

    log_Ns = range(7, 14)   # 10^7 to 10^13 parameters
    for log_N in log_Ns:
        N = 10 ** log_N
        D_req = find_D_for_loss(target_loss, N)
        ratio = D_req / HUMAN_TOKENS if D_req < 1e30 else float("inf")
        print(
            f"  N=10^{log_N}  D_required={D_req:.2e}  "
            f"gap_ratio={ratio:.2e}  "
            f"log_gap={math.log10(max(ratio,1)):.1f}"
        )


def human_D_analysis():
    """
    Key analysis: where does 3e7 (human tokens) land on the Chinchilla curve?
    What BLiMP accuracy would a model trained on 3e7 tokens achieve?
    This tells us whether the gap is in scaling law terms or beyond it.
    """
    a, b = fit_loss_blimp_mapping()

    print("=" * 72)
    print("WHERE DOES HUMAN TOKEN COUNT LAND ON THE SCALING CURVE?")
    print("=" * 72)
    print()

    for N in [1e8, 1e9, 1e10, 1e11]:
        L = chinchilla_loss(N, HUMAN_TOKENS)
        blimp_pred = a * L + b
        print(
            f"  N={N:.0e}, D=3e7 (human):  L={L:.3f}  "
            f"predicted_BLiMP={blimp_pred:.3f}"
        )

    print()
    print("  Comparison: LLM trained on same 3e7 tokens as a human child")
    print("  would predict BLiMP accuracy of ~?? — compare to human 0.94")
    print()
    print("  If predicted << 0.94: the gap is in the SCALING LAW (LLMs need more D for same N)")
    print("  If predicted ~= 0.94: humans are efficient for other reasons (prior/embodiment)")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--sweep-N", action="store_true")
    parser.add_argument("--human-D", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.all or args.report:
        main_report(); print()
    if args.all or args.sweep_N:
        sweep_N(); print()
    if args.all or args.human_D:
        human_D_analysis()
    if not any([args.report, args.sweep_N, args.human_D, args.all]):
        parser.print_help()
