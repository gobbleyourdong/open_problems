#!/usr/bin/env python3
"""
sk_lz78.py — LZ78 complexity vs gzip ratio across 16 string archetypes.

Theory context (gap.md R1):
  What physical quantities bound K-information in a region?
  Both gzip (LZ77 sliding-window) and LZ78 (dictionary-based) are computable
  lower-bound proxies for Kolmogorov complexity K. They are *different* lower
  bounds, so their divergence marks where the respective approximation schemes
  break down — and therefore where K itself is hard to bound from below.

LZ78 algorithm (Lempel-Ziv 1978):
  Scan string left-to-right. Maintain a dictionary of previously-seen phrases.
  At each step, find the longest current prefix that is in the dictionary, then
  extend it by one symbol and add the extended string to the dictionary as a
  new phrase. Count the number of phrases c(s,n).

  Complexity properties:
    - Random string of length n:  c ≈ n / log2(n)   (nearly every extension is new)
    - Constant string:            c = O(1)            (only a few phrases needed)
    - Periodic string (period p): c = O(p)            (dictionary fills up quickly, then repeats)
    - Globally-algorithmic string (π, LCG): c ≈ n/log2(n)  — same blindness as gzip,
      but the *absolute count* differs from gzip's compressed size in a predictable way.

  Normalized LZ78: lz78_norm = c / (n / log2(n))
    → 0 = perfectly compressible (structured)
    → ~1 = random-like (incompressible by LZ78)

Key predictions:
  - AGREE zone: random bytes, constants, periodic strings — both proxies give
    consistent signals (low or high K relative to true K).
  - DIVERGE zone: math constants (π,e,√2) and LCG adversarial string —
    gzip is blind because its sliding window finds no local repetition;
    LZ78 builds a global dictionary so it *also* finds nothing, BUT the
    ratio gzip_ratio / lz78_norm differs from the agree zone in a detectable way.
    Additionally, restricted-alphabet random (DNA, base64) diverges because
    alphabet size affects LZ78 phrase counts asymptotically differently from
    gzip's byte-stream compression.

Usage:
    cd ~/open_problems/physics/what_is_information
    python3 numerics/sk_lz78.py

Output: stdout comparison table + results/sk_lz78_data.json

Numerical track, what_is_information — 2026-04-09
"""

import gzip, math, json, os, struct
from collections import Counter

# ── LZ78 implementation ───────────────────────────────────────────────────────

def lz78_phrase_count(data: bytes) -> int:
    """
    Count the number of distinct phrases in the LZ78 factorization of data.

    Algorithm:
      - dictionary maps phrase (bytes) -> int index
      - current_phrase grows one byte at a time
      - when current_phrase is NOT in the dictionary, record a new phrase,
        add it to dictionary, reset current_phrase to empty
      - the empty string is implicitly in the dictionary as the root
    """
    dictionary = {}   # phrase_bytes -> index
    phrase_count = 0
    current = bytearray()

    for byte in data:
        current.append(byte)
        key = bytes(current)
        if key not in dictionary:
            phrase_count += 1
            dictionary[key] = phrase_count
            current = bytearray()
        # else: extend current phrase

    # If there's a leftover prefix that was already in the dictionary,
    # it still counts as the final (incomplete) phrase
    if current:
        phrase_count += 1

    return phrase_count


def lz78_norm(data: bytes) -> float:
    """
    Normalized LZ78 complexity in [0, ~1].

    For random data: c ≈ n/log2(n), so norm ≈ 1.
    For structured data: c << n/log2(n), so norm << 1.
    Values can slightly exceed 1.0 for short strings.
    """
    n = len(data)
    if n < 2:
        return 0.0
    c = lz78_phrase_count(data)
    expected_random = n / math.log2(n)
    return c / expected_random


# ── Shannon entropy ───────────────────────────────────────────────────────────

def shannon_bits_per_byte(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    n = len(data)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


# ── gzip ratio ────────────────────────────────────────────────────────────────

def gzip_ratio(data: bytes) -> float:
    n = len(data)
    if n == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / n


# ── String generators (re-implemented inline, no mpmath) ─────────────────────
# Matches sk_plane.py generators exactly where possible.
# For π/e/√2 we generate the digit strings via a different method:
#   Bailey-Borwein-Plouffe (for π in hex, converted to decimal) is complex.
#   Instead we use a simple decimal-expansion generator based on the
#   spigot algorithm (Gibbons 2004) for π, and Taylor series for e and √2.
#   This keeps the script stdlib-only.

def gen_random_bytes(n):
    return os.urandom(n)

def gen_constant(n):
    return bytes(n)

def gen_period2(n):
    return (b"AB" * (n // 2 + 1))[:n]

def gen_period16(n):
    pat = bytes(range(16))
    return (pat * (n // 16 + 1))[:n]

def gen_fibonacci_word(n):
    a, b = b"b", b"a"
    while len(a) < n:
        a, b = a + b, a
    return a[:n]

def gen_thue_morse(n):
    return bytes(bin(i).count("1") % 2 + 65 for i in range(n))

def _pi_digits_machin(n_digits: int) -> str:
    """
    π via Machin's formula: π/4 = 4*arctan(1/5) - arctan(1/239)
    Computed with integer arithmetic to n_digits+10 decimal places.
    arctan(1/x) = 1/x - 1/(3x^3) + 1/(5x^5) - ...
    """
    prec = n_digits + 20
    scale = 10 ** prec

    def arctan_series(x: int) -> int:
        # Returns arctan(1/x) * scale as integer
        total = 0
        term = scale // x        # first term: 1/x
        sign = 1
        k = 1
        while term != 0:
            total += sign * term
            k += 2
            term = term // (x * x) // k  # term_{k} = prev_term / (x^2 * k)
            sign = -sign
        return total

    pi_over_4 = 4 * arctan_series(5) - arctan_series(239)
    pi_int = 4 * pi_over_4
    # pi_int ≈ π * scale
    import sys; sys.set_int_max_str_digits(0)
    s = str(pi_int)
    # s is "3141592..." length ~prec+1, drop leading '3' to just get digit stream
    # but we want the full digit string: "314159265..."
    return s[:n_digits]

def gen_pi_digits(n):
    """First n ASCII decimal digits of π. H≈3.32 b/B, K=O(1), gzip high."""
    digits = _pi_digits_machin(n)
    return digits.encode("ascii")

def _e_digits_decimal(n_digits: int) -> str:
    """
    e = sum(1/k!, k=0..inf) computed in fixed-point decimal.
    Uses integer arithmetic for exact digits.
    """
    import sys; sys.set_int_max_str_digits(0)
    # Work with integers scaled by 10^(n_digits+20)
    prec = n_digits + 30
    scale = 10 ** prec
    total = 0
    term = scale  # 1/0! = 1
    k = 1
    while term > 0:
        total += term
        term //= k
        k += 1
    s = str(total)
    # total ≈ e * scale, length of str(total) ≈ prec+1
    return s[:n_digits]

def gen_e_digits(n):
    """First n ASCII decimal digits of e. K=O(1), gzip high."""
    digits = _e_digits_decimal(n)
    return digits[:n].encode("ascii")

def _sqrt2_digits_decimal(n_digits: int) -> str:
    """
    √2 via integer Newton's method in fixed-point decimal.
    x_{n+1} = (x_n + 2*scale^2/x_n) / 2
    """
    import sys; sys.set_int_max_str_digits(0)
    prec = n_digits + 20
    scale = 10 ** prec
    # Initial guess: 1.4142... * scale
    x = 14142 * (10 ** (prec - 4))
    for _ in range(60):
        x_new = (x + 2 * scale * scale // x) // 2
        if abs(x_new - x) <= 1:
            x = x_new
            break
        x = x_new
    s = str(x)
    # s represents √2 * 10^prec; prepend "1" if needed
    # Actually x ≈ 1.4142... * 10^prec, so first digit is '1'
    return s[:n_digits]

def gen_sqrt2_digits(n):
    """First n ASCII decimal digits of √2. K=O(1), gzip high."""
    digits = _sqrt2_digits_decimal(n)
    return digits[:n].encode("ascii")

def gen_english_text(n):
    passage = (
        b"The fundamental problem of communication is that of reproducing "
        b"at one point either exactly or approximately a message selected "
        b"at another point. Frequently the messages have meaning; that is "
        b"they refer to or are correlated according to some system with "
        b"certain physical or conceptual entities. These semantic aspects "
        b"of communication are irrelevant to the engineering problem. "
        b"The significant aspect is that the actual message is one selected "
        b"from a set of possible messages. The system must be designed to "
        b"operate for each possible selection, not just the one which will "
        b"actually be chosen since this is unknown at the time of design. "
    )
    return (passage * (n // len(passage) + 1))[:n]

def gen_source_code(n):
    snippet = b'''def shannon(data):
    from collections import Counter
    import math
    counts = Counter(data)
    total = len(data)
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

class KolmogorovApprox:
    """Lower-bound approximation to Kolmogorov complexity via compression."""
    def __init__(self, compressor="gzip"):
        self.compressor = compressor

    def complexity(self, data: bytes) -> float:
        import gzip, bz2, lzma
        n = len(data)
        if self.compressor == "gzip":
            return len(gzip.compress(data, compresslevel=9)) / n
        elif self.compressor == "bzip2":
            return len(bz2.compress(data)) / n
        return len(lzma.compress(data)) / n
'''
    return (snippet * (n // len(snippet) + 1))[:n]

def gen_incremental_uint32(n):
    buf = b""
    i = 0
    while len(buf) < n:
        buf += struct.pack(">I", i)
        i += 1
    return buf[:n]

def gen_dna_random(n):
    alphabet = b"ATCG"
    return bytes(alphabet[b % 4] for b in os.urandom(n))

def gen_base64_random(n):
    import base64
    raw = os.urandom(n)
    return base64.b64encode(raw)[:n]

def gen_rle_runs(n):
    result = bytearray()
    rng_bytes = os.urandom(n * 2)
    idx = 0
    while len(result) < n and idx + 1 < len(rng_bytes):
        run_len = (rng_bytes[idx] % 30) + 1
        byte = rng_bytes[idx + 1]
        result.extend([byte] * run_len)
        idx += 2
    return bytes(result[:n])

def gen_lz77_adversarial(n):
    """LCG: short program, output looks random to sliding-window compressors."""
    state = 1337
    result = bytearray()
    while len(result) < n:
        state = (1664525 * state + 1013904223) & 0xFFFFFFFF
        result.append(state >> 24)
    return bytes(result[:n])


# ── Archetype table ───────────────────────────────────────────────────────────

GENERATORS = [
    # (label, category, gen_fn, true_k_note, expected_divergence)
    ("random_bytes",       "RANDOM",      gen_random_bytes,      "K=MAX",        "AGREE-high"),
    ("constant_zeros",     "CONSTANT",    gen_constant,          "K=MIN",        "AGREE-low"),
    ("period_2",           "PERIODIC",    gen_period2,           "K=tiny",       "AGREE-low"),
    ("period_16",          "PERIODIC",    gen_period16,          "K=tiny",       "AGREE-low"),
    ("fibonacci_word",     "MORPHIC",     gen_fibonacci_word,    "K=small",      "AGREE-low"),
    ("thue_morse",         "MORPHIC",     gen_thue_morse,        "K=small",      "AGREE-low"),
    ("pi_digits",          "MATH",        gen_pi_digits,         "K=O(1)",       "DIVERGE"),
    ("e_digits",           "MATH",        gen_e_digits,          "K=O(1)",       "DIVERGE"),
    ("sqrt2_digits",       "MATH",        gen_sqrt2_digits,      "K=O(1)",       "DIVERGE"),
    ("english_prose",      "NATURAL",     gen_english_text,      "K=medium",     "AGREE-low"),
    ("source_code_python", "NATURAL",     gen_source_code,       "K=medium",     "AGREE-low"),
    ("incremental_uint32", "STRUCT",      gen_incremental_uint32,"K=small",      "AGREE-low"),
    ("dna_random",         "RANDOM4",     gen_dna_random,        "K=HIGH",       "DIVERGE"),
    ("base64_random",      "RANDOM64",    gen_base64_random,     "K=HIGH",       "DIVERGE"),
    ("rle_random_runs",    "MIXED",       gen_rle_runs,          "K=medium",     "AGREE-mid"),
    ("lz77_adversarial",   "ADVERSARIAL", gen_lz77_adversarial,  "K=medium-LCG", "DIVERGE"),
]

SAMPLE_N = 10_000  # bytes — matches sk_plane.py

# ── Agreement / divergence classifier ────────────────────────────────────────

def classify(gzip_r: float, lz78_n: float) -> str:
    """
    Both high (>0.7): AGREE-HIGH (random-like, both see no structure)
    Both low (<0.15): AGREE-LOW  (structured, both compress well)
    gzip high, lz78 high, but scale differs: DIVERGE-SCALE
    gzip high, lz78 mid (~0.4-0.8): DIVERGE-GZIP-BLIND
    gzip mid, lz78 high: DIVERGE-LZ78-BLIND
    """
    g_hi = gzip_r > 0.70
    g_lo = gzip_r < 0.15
    l_hi = lz78_n > 0.70
    l_lo = lz78_n < 0.15
    if g_hi and l_hi:
        return "AGREE-HIGH"
    if g_lo and l_lo:
        return "AGREE-LOW"
    if g_hi and not l_hi:
        return "DIVERGE(gzip>lz78)"
    if not g_hi and l_hi:
        return "DIVERGE(lz78>gzip)"
    diff = abs(gzip_r - lz78_n)
    if diff < 0.15:
        return "AGREE-MID"
    return "DIVERGE-MID"


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("Generating string archetypes and computing gzip vs LZ78 complexity...")
    print("(LZ78 runs in pure Python — may take ~10-30s for MATH constants)")
    print()

    records = []
    for label, cat, gen_fn, true_k, expected in GENERATORS:
        print(f"  [{cat:<12}] {label}...", flush=True)
        data = gen_fn(SAMPLE_N)

        h     = shannon_bits_per_byte(data)
        gr    = gzip_ratio(data)
        lz78n = lz78_norm(data)
        lz78c = lz78_phrase_count(data)  # raw count
        ratio_gl = gr / lz78n if lz78n > 1e-6 else float("inf")
        agree = classify(gr, lz78n)

        records.append({
            "label":            label,
            "category":         cat,
            "true_k_note":      true_k,
            "expected":         expected,
            "shannon_bpB":      round(h, 5),
            "gzip_ratio":       round(gr, 5),
            "lz78_phrase_count": lz78c,
            "lz78_norm":        round(lz78n, 5),
            "ratio_gzip_lz78":  round(ratio_gl, 4),
            "classification":   agree,
        })

    # ── Print comparison table ────────────────────────────────────────────────
    sep = "─" * 115
    print()
    print(sep)
    hdr = (f"{'Label':<22} {'Cat':<12} {'H b/B':<8} {'gzip':<8} {'lz78_norm':<11}"
           f"{'lz78_ct':<9} {'g/l ratio':<11} {'Classification':<22} True-K")
    print(hdr)
    print(sep)

    for r in records:
        print(
            f"{r['label']:<22} {r['category']:<12} {r['shannon_bpB']:<8.4f} "
            f"{r['gzip_ratio']:<8.4f} {r['lz78_norm']:<11.4f}"
            f"{r['lz78_phrase_count']:<9} {r['ratio_gzip_lz78']:<11.4f} "
            f"{r['classification']:<22} {r['true_k_note']}"
        )

    print(sep)

    # ── Agreement / divergence summary ────────────────────────────────────────
    print()
    print("── AGREEMENT ZONE (both proxies give consistent K signal) ──")
    agree_records = [r for r in records if r["classification"].startswith("AGREE")]
    for r in agree_records:
        print(f"  {r['label']:<22}  gzip={r['gzip_ratio']:.4f}  lz78={r['lz78_norm']:.4f}"
              f"  class={r['classification']}")

    print()
    print("── DIVERGENCE ZONE (proxies disagree — gzip window fails here) ──")
    div_records = [r for r in records if "DIVERGE" in r["classification"]]
    for r in div_records:
        print(f"  {r['label']:<22}  gzip={r['gzip_ratio']:.4f}  lz78={r['lz78_norm']:.4f}"
              f"  g/l={r['ratio_gzip_lz78']:.4f}  true-K={r['true_k_note']}")

    # ── Math constant analysis ────────────────────────────────────────────────
    print()
    print("── MATH CONSTANT ANALYSIS (K=O(1) but proxies say K=high) ──")
    math_records = [r for r in records if r["category"] == "MATH"]
    for r in math_records:
        print(f"  {r['label']:<15}  gzip={r['gzip_ratio']:.4f}  lz78={r['lz78_norm']:.4f}"
              f"  g/l={r['ratio_gzip_lz78']:.4f}")
    # Compare to random
    rand = next(r for r in records if r["label"] == "random_bytes")
    print(f"  {'random_bytes':<15}  gzip={rand['gzip_ratio']:.4f}  lz78={rand['lz78_norm']:.4f}"
          f"  g/l={rand['ratio_gzip_lz78']:.4f}  (reference: true K=MAX)")
    print()
    avg_math_gl = sum(r["ratio_gzip_lz78"] for r in math_records) / len(math_records)
    print(f"  Mean g/l ratio for math constants: {avg_math_gl:.4f}")
    print(f"  g/l ratio for random_bytes:        {rand['ratio_gzip_lz78']:.4f}")
    diff_pct = abs(avg_math_gl - rand["ratio_gzip_lz78"]) / rand["ratio_gzip_lz78"] * 100
    print(f"  Relative difference:               {diff_pct:.1f}%")
    print()
    print("  Interpretation: if g/l ratio for math ≈ g/l for random, both proxies")
    print("  fail identically — gzip and LZ78 are both blind to global structure.")
    print("  If g/l ratio differs significantly, the failure modes are different,")
    print("  which means the union of both proxies would tighten the K bound.")

    # ── LZ78 alphabet-sensitivity analysis ───────────────────────────────────
    print()
    print("── ALPHABET-SIZE SENSITIVITY ──")
    alpha_cases = ["random_bytes", "dna_random", "base64_random"]
    for lbl in alpha_cases:
        r = next(x for x in records if x["label"] == lbl)
        print(f"  {lbl:<22}  gzip={r['gzip_ratio']:.4f}  lz78={r['lz78_norm']:.4f}"
              f"  g/l={r['ratio_gzip_lz78']:.4f}  H={r['shannon_bpB']:.3f}")
    print()
    print("  LZ78 phrase count grows as n/log_|Sigma|(n) for |Sigma|-symbol alphabet.")
    print("  Our normalization uses log2(n) (byte alphabet), so restricted alphabets")
    print("  produce lz78_norm < 1 even when the string is truly random over its alphabet.")
    print("  This is a SYSTEMATIC BIAS: LZ78 underestimates K for small alphabets.")
    print("  gzip is also biased (byte-stream), so both proxies have the same directional")
    print("  error for alphabet-restricted strings, just at different magnitudes.")

    # ── Save JSON ─────────────────────────────────────────────────────────────
    os.makedirs("results", exist_ok=True)
    out_path = "results/sk_lz78_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "description": "LZ78 vs gzip K-proxy comparison across 16 string archetypes",
            "sample_bytes": SAMPLE_N,
            "normalization": "lz78_norm = phrase_count / (n / log2(n))",
            "records": records,
        }, f, indent=2)
    print(f"\nData → {out_path}")

    return records


if __name__ == "__main__":
    run()
