#!/usr/bin/env python3
"""
gzip_lipschitz.py — Empirical measurement of gzip's Lipschitz constant on short inputs.

Theory track (attempt_006) reduces the histogram-stability conjecture to ONE axiom:
  gzip on fixed-length inputs of L bytes is Lipschitz with constant lambda <= 3.
  That is: changing k input bytes changes |gzip(x)| by at most lambda * k bytes.

This script measures lambda empirically:
  1. Random byte sequences of length L in {8, 16, 32, 64, 128}
  2. Histogram-like sequences (counts in 0-20, mimicking real NP proxies)
  3. For perturbation sizes d_H in {1, 2, 3, 4}:
       lambda = |gzip(original) - gzip(neighbor)| / d_H
  4. Reports max, mean, median, 99th percentile of lambda

Key question: Is lambda <= 3? Closer to 1? Depends on L?

Usage:
    cd ~/open_problems/physics/what_is_computation
    python3 numerics/gzip_lipschitz.py

Numerical track, what_is_computation — 2026-04-10
"""

import gzip
import json
import os
import random
import statistics
import sys
from collections import defaultdict

# ── Configuration ────────────────────────────────────────────────────────────

LENGTHS = [8, 16, 32, 64, 128]
PERTURBATION_SIZES = [1, 2, 3, 4]
N_SAMPLES = 10_000
COMPRESS_LEVEL = 9
SEED = 42

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")


# ── Core measurement ─────────────────────────────────────────────────────────

def compressed_size(data: bytes) -> int:
    """Return the length of gzip-compressed data."""
    return len(gzip.compress(data, compresslevel=COMPRESS_LEVEL))


def flip_k_bytes(data: bytearray, k: int, rng: random.Random) -> bytearray:
    """
    Create a neighbor at Hamming distance exactly k by flipping k distinct bytes.
    Each flipped byte is changed to a uniformly random DIFFERENT value.
    """
    result = bytearray(data)
    positions = rng.sample(range(len(data)), k)
    for pos in positions:
        old_val = result[pos]
        # Pick a new value that differs from the old one
        new_val = old_val
        while new_val == old_val:
            new_val = rng.randint(0, 255)
        result[pos] = new_val
    return result


def perturb_histogram(data: bytearray, k: int, rng: random.Random) -> bytearray:
    """
    Create a neighbor of a histogram-like sequence by perturbing k buckets.
    Each perturbed bucket is incremented or decremented by 1 (clamped to [0, 255]).
    This models how real NP proxy histograms change between search steps.
    """
    result = bytearray(data)
    positions = rng.sample(range(len(data)), k)
    for pos in positions:
        old_val = result[pos]
        if old_val == 0:
            result[pos] = 1
        elif old_val == 255:
            result[pos] = 254
        else:
            result[pos] = old_val + rng.choice([-1, 1])
    return result


def generate_random_bytes(L: int, rng: random.Random) -> bytearray:
    """Generate L uniformly random bytes."""
    return bytearray(rng.randint(0, 255) for _ in range(L))


def generate_histogram_like(L: int, rng: random.Random) -> bytearray:
    """
    Generate L bytes that look like histogram counts:
    values in 0-20, with ~30% zeros (sparse histograms, like real NP proxies).
    """
    data = bytearray(L)
    for i in range(L):
        if rng.random() < 0.30:
            data[i] = 0
        else:
            data[i] = rng.randint(0, 20)
    return data


def measure_lipschitz(
    L: int,
    n_samples: int,
    perturbation_sizes: list[int],
    generator,
    perturber,
    rng: random.Random,
    label: str,
) -> dict:
    """
    Measure the empirical Lipschitz constant of gzip on inputs of length L.

    Returns a dict:
      { d_H: { "max": ..., "mean": ..., "median": ..., "p99": ..., "ratios": [...] } }
    """
    results = {}

    for d_H in perturbation_sizes:
        if d_H > L:
            continue

        ratios = []
        for _ in range(n_samples):
            original = generator(L, rng)
            neighbor = perturber(original, d_H, rng)

            c_orig = compressed_size(bytes(original))
            c_neigh = compressed_size(bytes(neighbor))

            delta = abs(c_orig - c_neigh)
            lam = delta / d_H
            ratios.append(lam)

        results[d_H] = {
            "max": max(ratios),
            "mean": statistics.mean(ratios),
            "median": statistics.median(ratios),
            "p99": sorted(ratios)[int(0.99 * len(ratios))],
            "p999": sorted(ratios)[int(0.999 * len(ratios))],
            "frac_zero": sum(1 for r in ratios if r == 0.0) / len(ratios),
            "ratios": ratios,  # kept for JSON export, stripped for display
        }

    return results


# ── Display ───────────────────────────────────────────────────────────────────

def print_table(all_results: dict):
    """Print a nicely formatted summary table."""
    header = f"{'Input Type':<20} {'L':>4} {'d_H':>4} {'lambda_max':>10} {'lambda_p99':>10} {'lambda_p999':>11} {'lambda_mean':>11} {'lambda_med':>10} {'%zero':>7}"
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    for key in sorted(all_results.keys()):
        label, L = key
        data = all_results[key]
        for d_H in sorted(data.keys()):
            r = data[d_H]
            print(
                f"{label:<20} {L:>4} {d_H:>4} "
                f"{r['max']:>10.3f} {r['p99']:>10.3f} {r['p999']:>11.3f} "
                f"{r['mean']:>11.4f} {r['median']:>10.3f} {r['frac_zero']:>7.1%}"
            )
        print("-" * len(header))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    rng = random.Random(SEED)

    all_results = {}

    # Phase 1: Random byte sequences
    print(f"\n{'='*70}")
    print(f" Phase 1: Random byte sequences ({N_SAMPLES:,} samples per cell)")
    print(f"{'='*70}\n")

    for L in LENGTHS:
        sys.stdout.write(f"  L={L:>3} ... ")
        sys.stdout.flush()
        results = measure_lipschitz(
            L, N_SAMPLES, PERTURBATION_SIZES,
            generate_random_bytes, flip_k_bytes, rng,
            label="random",
        )
        all_results[("random", L)] = results
        sys.stdout.write(f"done (lambda_max @ d_H=1: {results[1]['max']:.3f})\n")
        sys.stdout.flush()

    # Phase 2: Histogram-like sequences (with byte-flip perturbation)
    print(f"\n{'='*70}")
    print(f" Phase 2: Histogram-like sequences, byte-flip perturbation")
    print(f"{'='*70}\n")

    for L in LENGTHS:
        sys.stdout.write(f"  L={L:>3} ... ")
        sys.stdout.flush()
        results = measure_lipschitz(
            L, N_SAMPLES, PERTURBATION_SIZES,
            generate_histogram_like, flip_k_bytes, rng,
            label="histogram_flip",
        )
        all_results[("hist_flip", L)] = results
        sys.stdout.write(f"done (lambda_max @ d_H=1: {results[1]['max']:.3f})\n")
        sys.stdout.flush()

    # Phase 3: Histogram-like sequences with increment/decrement perturbation
    # This is the most realistic model: changing one histogram count by +/-1
    print(f"\n{'='*70}")
    print(f" Phase 3: Histogram-like sequences, +/-1 count perturbation")
    print(f"{'='*70}\n")

    for L in LENGTHS:
        sys.stdout.write(f"  L={L:>3} ... ")
        sys.stdout.flush()
        results = measure_lipschitz(
            L, N_SAMPLES, PERTURBATION_SIZES,
            generate_histogram_like, perturb_histogram, rng,
            label="histogram_pm1",
        )
        all_results[("hist_pm1", L)] = results
        sys.stdout.write(f"done (lambda_max @ d_H=1: {results[1]['max']:.3f})\n")
        sys.stdout.flush()

    # ── Summary table ─────────────────────────────────────────────────────────

    print(f"\n\n{'='*70}")
    print(f" SUMMARY TABLE")
    print(f"{'='*70}\n")
    print_table(all_results)

    # ── Key findings ──────────────────────────────────────────────────────────

    # Find the global max lambda across everything
    global_max = 0
    global_max_info = ""
    for key, data in all_results.items():
        for d_H, r in data.items():
            if r["max"] > global_max:
                global_max = r["max"]
                global_max_info = f"{key[0]}, L={key[1]}, d_H={d_H}"

    # Check if lambda <= 3 holds everywhere
    axiom_holds = global_max <= 3.0

    print(f"\n{'='*70}")
    print(f" KEY FINDINGS")
    print(f"{'='*70}")
    print(f"\n  Global maximum lambda observed: {global_max:.3f}")
    print(f"  Achieved at: {global_max_info}")
    print(f"\n  Axiom (lambda <= 3) holds: {'YES' if axiom_holds else 'NO'}")

    # lambda_max at d_H=1 across L for random inputs
    print(f"\n  lambda_max at d_H=1 (random inputs) by L:")
    for L in LENGTHS:
        r = all_results[("random", L)][1]
        print(f"    L={L:>3}: max={r['max']:.3f}, p99={r['p99']:.3f}, mean={r['mean']:.4f}")

    print(f"\n  lambda_max at d_H=1 (histogram +/-1) by L:")
    for L in LENGTHS:
        r = all_results[("hist_pm1", L)][1]
        print(f"    L={L:>3}: max={r['max']:.3f}, p99={r['p99']:.3f}, mean={r['mean']:.4f}")

    # ── Save results ──────────────────────────────────────────────────────────

    os.makedirs(RESULTS_DIR, exist_ok=True)

    # JSON data (strip the full ratio lists for sanity, keep summary stats)
    json_data = {}
    for key, data in all_results.items():
        json_key = f"{key[0]}_L{key[1]}"
        json_data[json_key] = {}
        for d_H, r in data.items():
            json_data[json_key][str(d_H)] = {
                "max": r["max"],
                "mean": r["mean"],
                "median": r["median"],
                "p99": r["p99"],
                "p999": r["p999"],
                "frac_zero": r["frac_zero"],
                "n_samples": N_SAMPLES,
            }

    json_path = os.path.join(RESULTS_DIR, "gzip_lipschitz_data.json")
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)
    print(f"\n  Data saved to: {json_path}")

    # Findings markdown
    findings_path = os.path.join(RESULTS_DIR, "gzip_lipschitz_findings.md")
    with open(findings_path, "w") as f:
        f.write("# gzip Lipschitz Constant: Empirical Measurement\n\n")
        f.write(f"**Date:** 2026-04-10\n")
        f.write(f"**Samples per cell:** {N_SAMPLES:,}\n")
        f.write(f"**Compress level:** {COMPRESS_LEVEL}\n")
        f.write(f"**Seed:** {SEED}\n\n")

        f.write("## Context\n\n")
        f.write("attempt_006_histogram_stability.md reduces the histogram-stability conjecture ")
        f.write("to one axiom: gzip on fixed-length inputs of L bytes is Lipschitz with constant ")
        f.write("lambda <= 3. This script measures lambda empirically.\n\n")

        f.write("## Results\n\n")
        f.write("### Global maximum\n\n")
        f.write(f"- **lambda_max = {global_max:.3f}** (at {global_max_info})\n")
        f.write(f"- **Axiom (lambda <= 3) holds: {'YES' if axiom_holds else 'NO'}**\n\n")

        f.write("### Summary table (d_H = 1, the critical case)\n\n")
        f.write("| Input type | L | lambda_max | lambda_p99 | lambda_mean | %zero |\n")
        f.write("|:-----------|---:|-----------:|-----------:|------------:|------:|\n")

        for key in sorted(all_results.keys()):
            label, L = key
            if 1 in all_results[key]:
                r = all_results[key][1]
                f.write(
                    f"| {label} | {L} | {r['max']:.3f} | "
                    f"{r['p99']:.3f} | {r['mean']:.4f} | {r['frac_zero']:.1%} |\n"
                )

        f.write("\n### Full table (all d_H values)\n\n")
        f.write("| Input type | L | d_H | lambda_max | lambda_p99 | lambda_p999 | lambda_mean | lambda_median | %zero |\n")
        f.write("|:-----------|---:|----:|-----------:|-----------:|------------:|------------:|--------------:|------:|\n")

        for key in sorted(all_results.keys()):
            label, L = key
            data = all_results[key]
            for d_H in sorted(data.keys()):
                r = data[d_H]
                f.write(
                    f"| {label} | {L} | {d_H} | {r['max']:.3f} | "
                    f"{r['p99']:.3f} | {r['p999']:.3f} | {r['mean']:.4f} | "
                    f"{r['median']:.3f} | {r['frac_zero']:.1%} |\n"
                )

        f.write("\n## Interpretation\n\n")
        if axiom_holds:
            f.write("The Lipschitz axiom (lambda <= 3) is **empirically confirmed** across all ")
            f.write(f"{len(LENGTHS)} input lengths and {len(PERTURBATION_SIZES)} perturbation sizes, ")
            f.write(f"for {N_SAMPLES:,} random samples per cell.\n\n")
            if global_max <= 2.0:
                f.write(f"The actual maximum lambda ({global_max:.3f}) is well below 3, suggesting ")
                f.write("the conservative bound lambda <= 3 has significant headroom. ")
                f.write("A tighter bound might be achievable.\n\n")
            if global_max <= 1.0:
                f.write("In fact, lambda_max <= 1.0, meaning gzip on short inputs is a ")
                f.write("**contraction** (or at worst non-expansive) in absolute output size.\n\n")
        else:
            f.write(f"**WARNING:** The axiom lambda <= 3 is **violated** (max lambda = {global_max:.3f}). ")
            f.write("The theory in attempt_006 may need a larger constant or a refined statement.\n\n")

        f.write("## Connection to histogram-stability\n\n")
        f.write("For the 10 fixed-length NP proxy families (L in {8, 16}), the theorem states:\n\n")
        f.write("    |Delta K| <= lambda * epsilon / L\n\n")
        f.write("where epsilon is the number of histogram buckets that change per search step.\n")
        f.write("On hard instances (frozen core), epsilon -> 0, giving slope -> 0.\n")
        f.write("On easy instances, epsilon > 0, giving detectable negative slope.\n\n")
        f.write("The empirical lambda measured here determines how tight this bound is.\n")

    print(f"  Findings saved to: {findings_path}")
    print()


if __name__ == "__main__":
    main()
