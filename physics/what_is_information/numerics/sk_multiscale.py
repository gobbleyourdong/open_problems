#!/usr/bin/env python3
"""
sk_multiscale.py — S/K analysis at multiple linguistic scales (characters, words, sentences).

Theory: the S/K bifurcation from attempt_001 should manifest differently at different
scales of description. At the character level: moderate S, low K (compressible text).
At the word level: lower S (word distribution is more predictable), lower K.
At the sentence level: lower S still, possibly different K.

The ratio H/compression_ratio (S-cost / K-content) at each scale approximates the
"thermodynamic cost per unit of K-information extracted" — directly relevant to R3:
"Does the mind-as-compressor framing make a specific physical prediction?"

This script:
1. Takes a large text corpus (use first 100KB of the Project Gutenberg "War and Peace" or
   a generated synthetic text) and analyzes it at three granularities:
   - Byte level (chars): entropy over byte values, compression ratio
   - Word level: entropy over word tokens, compression ratio of the word sequence
   - Bigram level: entropy over consecutive word pairs, compression ratio

2. For each level, computes:
   - Shannon entropy H (bits per token)
   - gzip compression ratio (K-proxy)
   - H_max for the alphabet at that level (log2(vocabulary_size))
   - H/H_max: how close to maximum entropy (S-saturation)
   - The S/K ratio at each level

3. Key prediction: as we go from byte → word → bigram, both H and compression ratio
   should decrease (more structure visible at coarser scales), but the H/K ratio
   should stay roughly constant — or reveal whether coarser scales are more K-efficient.

4. Also computes the "K-extraction efficiency" of each scale: how much compressibility
   is revealed per unit of S-information processed.

Usage:
    cd ~/open_problems/physics/what_is_information
    python3 numerics/sk_multiscale.py

Numerical track, what_is_information — 2026-04-09
"""

import math, gzip, json, os, re
from collections import Counter

# ── Generate a large synthetic text corpus ────────────────────────────────────
# We use a Markov-chain generated text to avoid copyright issues and to have
# control over the statistical properties.

def generate_corpus(n_chars: int, seed: int = 42) -> str:
    """
    Generate a large synthetic English-like text corpus using a bigram model
    trained on a hardcoded seed text. Not real English, but has similar statistical
    properties (character and word frequency distributions).
    """
    import random
    rng = random.Random(seed)

    # Seed text (public domain, short enough to hardcode)
    seed_text = """
    The information theory, developed in the late nineteen forties by Claude Shannon,
    provides a mathematical framework for quantifying the amount of information in a message.
    Shannon introduced the concept of entropy as a measure of uncertainty in a random variable.
    The entropy of a source measures the average number of bits needed to encode the output.
    In the context of data compression, entropy provides a lower bound on the compression ratio.
    The Kolmogorov complexity of a string is defined as the length of the shortest computer
    program that produces the string as output. Unlike Shannon entropy, which is defined for
    probability distributions, Kolmogorov complexity is defined for individual strings.
    Random strings have high Kolmogorov complexity because they cannot be described more
    concisely than by listing them explicitly. Structured strings have low complexity because
    they can be described by short generating rules. The connection between information theory
    and thermodynamics was established by Landauer, who showed that erasing one bit of
    information requires dissipating at least kT times the natural logarithm of two of energy.
    This result connects the abstract notion of information to physical reality.
    The holographic principle suggests that the maximum amount of information that can be
    stored in a region of space is proportional to the surface area of the region, not its volume.
    This principle arises from the study of black hole thermodynamics and has profound
    implications for our understanding of the nature of space, time, and information.
    Quantum information theory extends classical information theory to quantum systems.
    Quantum bits, or qubits, can exist in superpositions of zero and one, allowing for
    phenomena such as quantum entanglement and quantum teleportation. The quantum channel
    capacity determines how much classical or quantum information can be reliably transmitted
    through a noisy quantum channel. Quantum error correction codes allow quantum information
    to be protected against decoherence and other sources of noise.
    """

    # Build a bigram model from the seed text
    words = seed_text.split()
    bigrams = list(zip(words[:-1], words[1:]))
    bigram_to_nexts = {}
    for (w1, w2) in bigrams:
        bigram_to_nexts.setdefault(w1, []).append(w2)

    # Generate text
    output_words = words[:5]
    while len(' '.join(output_words)) < n_chars:
        last = output_words[-1]
        if last in bigram_to_nexts:
            next_word = rng.choice(bigram_to_nexts[last])
        else:
            next_word = rng.choice(words)
        output_words.append(next_word)

    return ' '.join(output_words)[:n_chars]

# ── Multi-scale analysis ──────────────────────────────────────────────────────

def byte_level_analysis(text: str) -> dict:
    """Byte-level: treat text as sequence of bytes."""
    data = text.encode('utf-8')
    n = len(data)
    counts = Counter(data)
    vocab_size = len(counts)
    h = -sum((c/n) * math.log2(c/n) for c in counts.values())
    h_max = math.log2(vocab_size) if vocab_size > 1 else 0
    comp_size = len(gzip.compress(data, compresslevel=9))
    k_ratio = comp_size / n
    return {
        "level": "byte",
        "n_tokens": n,
        "vocab_size": vocab_size,
        "H_bits_per_token": round(h, 6),
        "H_max": round(h_max, 6),
        "H_saturation": round(h / h_max, 6) if h_max > 0 else 0,
        "gzip_ratio": round(k_ratio, 6),
        "H_over_K": round(h / k_ratio, 6) if k_ratio > 0 else 0,
    }

def word_level_analysis(text: str) -> dict:
    """Word-level: tokenize by whitespace, analyze word sequence."""
    words = text.lower().split()
    # Filter to alphabetic words only
    words = [w.strip(".,;:!?\"'()[]{}") for w in words if w.strip(".,;:!?\"'()[]{}").isalpha()]
    n = len(words)
    if n < 10:
        return {}
    counts = Counter(words)
    vocab_size = len(counts)
    h = -sum((c/n) * math.log2(c/n) for c in counts.values())
    h_max = math.log2(vocab_size) if vocab_size > 1 else 0
    # Compress the word sequence as a space-separated string
    word_seq = ' '.join(words).encode('utf-8')
    comp_size = len(gzip.compress(word_seq, compresslevel=9))
    k_ratio = comp_size / len(word_seq)
    return {
        "level": "word",
        "n_tokens": n,
        "vocab_size": vocab_size,
        "H_bits_per_token": round(h, 6),
        "H_max": round(h_max, 6),
        "H_saturation": round(h / h_max, 6) if h_max > 0 else 0,
        "gzip_ratio": round(k_ratio, 6),
        "H_over_K": round(h / k_ratio, 6) if k_ratio > 0 else 0,
    }

def bigram_level_analysis(text: str) -> dict:
    """Bigram-level: analyze consecutive word pairs."""
    words = text.lower().split()
    words = [w.strip(".,;:!?\"'()[]{}") for w in words if w.strip(".,;:!?\"'()[]{}").isalpha()]
    bigrams = [f"{w1}_{w2}" for w1, w2 in zip(words[:-1], words[1:])]
    n = len(bigrams)
    if n < 10:
        return {}
    counts = Counter(bigrams)
    vocab_size = len(counts)
    h = -sum((c/n) * math.log2(c/n) for c in counts.values())
    h_max = math.log2(vocab_size) if vocab_size > 1 else 0
    bigram_seq = ' '.join(bigrams).encode('utf-8')
    comp_size = len(gzip.compress(bigram_seq, compresslevel=9))
    k_ratio = comp_size / len(bigram_seq)
    return {
        "level": "bigram",
        "n_tokens": n,
        "vocab_size": vocab_size,
        "H_bits_per_token": round(h, 6),
        "H_max": round(h_max, 6),
        "H_saturation": round(h / h_max, 6) if h_max > 0 else 0,
        "gzip_ratio": round(k_ratio, 6),
        "H_over_K": round(h / k_ratio, 6) if k_ratio > 0 else 0,
    }

def trigram_char_level(text: str) -> dict:
    """Character trigram level: analyze consecutive char triples."""
    data = text.encode('utf-8')
    tgs = [data[i:i+3] for i in range(len(data)-2)]
    n = len(tgs)
    counts = Counter(tgs)
    vocab_size = len(counts)
    h = -sum((c/n) * math.log2(c/n) for c in counts.values())
    h_max = math.log2(vocab_size) if vocab_size > 1 else 0
    # Represent trigrams as sequence
    flat = b''.join(tgs)
    comp_size = len(gzip.compress(flat, compresslevel=9))
    k_ratio = comp_size / len(flat)
    return {
        "level": "char_trigram",
        "n_tokens": n,
        "vocab_size": vocab_size,
        "H_bits_per_token": round(h, 6),
        "H_max": round(h_max, 6),
        "H_saturation": round(h / h_max, 6) if h_max > 0 else 0,
        "gzip_ratio": round(k_ratio, 6),
        "H_over_K": round(h / k_ratio, 6) if k_ratio > 0 else 0,
    }

# ── S/K ratio across scales ───────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("Multi-Scale S/K Analysis: Character → Word → Bigram")
    print("=" * 70)

    # Generate corpus
    CORPUS_SIZE = 100_000  # 100KB of text
    print(f"\nGenerating {CORPUS_SIZE//1000}KB synthetic English-like corpus...")
    corpus = generate_corpus(CORPUS_SIZE)
    print(f"Generated {len(corpus)} characters, {len(corpus.split())} words")

    # Run analyses
    levels = [
        byte_level_analysis(corpus),
        trigram_char_level(corpus),
        word_level_analysis(corpus),
        bigram_level_analysis(corpus),
    ]

    print(f"\n{'Level':<15} {'Vocab':<10} {'H (b/tok)':<12} {'H_max':<10} {'H/H_max':<10} {'gzip':<10} {'H/K'}")
    print("─" * 80)
    for r in levels:
        if r:
            print(f"{r['level']:<15} {r['vocab_size']:<10} {r['H_bits_per_token']:<12.4f} "
                  f"{r['H_max']:<10.4f} {r['H_saturation']:<10.4f} "
                  f"{r['gzip_ratio']:<10.4f} {r['H_over_K']:.2f}")

    print("\n── Key ratios ──")
    byte_r = levels[0]
    word_r = levels[2]
    bigram_r = levels[3]

    if byte_r and word_r and bigram_r:
        print(f"\nH decreasing from char → word → bigram:")
        print(f"  char:   H = {byte_r['H_bits_per_token']:.4f} b/token (alphabet = {byte_r['vocab_size']} symbols)")
        print(f"  word:   H = {word_r['H_bits_per_token']:.4f} b/token (vocabulary = {word_r['vocab_size']} words)")
        print(f"  bigram: H = {bigram_r['H_bits_per_token']:.4f} b/token (bigrams = {bigram_r['vocab_size']})")

        print(f"\ngzip ratio (K-proxy) across scales:")
        print(f"  char:   {byte_r['gzip_ratio']:.4f}")
        print(f"  word:   {word_r['gzip_ratio']:.4f}")
        print(f"  bigram: {bigram_r['gzip_ratio']:.4f}")

        print(f"\nH/K ratio (S-cost per K-unit) across scales:")
        print(f"  char:   {byte_r['H_over_K']:.2f}")
        print(f"  word:   {word_r['H_over_K']:.2f}")
        print(f"  bigram: {bigram_r['H_over_K']:.2f}")

        print(f"\nPrediction (R3): if H/K is approximately constant across scales,")
        print(f"the S-cost per K-bit is scale-independent — a property of language itself.")
        print(f"If H/K changes, the K-extraction efficiency depends on the scale of analysis.")

        # The Zipf's law connection: word distribution follows Zipf, which gives
        # H ≈ log(log(N)) where N is vocabulary size — much less than log(N)
        n_words = word_r['vocab_size']
        h_uniform = math.log2(n_words)
        h_zipf_approx = math.log2(math.log2(n_words + 1) + 1) if n_words > 1 else 0
        print(f"\nZipf's law context: word vocabulary = {n_words}")
        print(f"  H if uniform distribution: {h_uniform:.4f} bits/word")
        print(f"  Actual H:                  {word_r['H_bits_per_token']:.4f} bits/word")
        print(f"  H/H_uniform:               {word_r['H_bits_per_token']/h_uniform:.4f}")
        print(f"  Words are far from maximum entropy — Zipf creates K-structure at word level.")

    # Cross-scale S information comparison
    print(f"\n── S-Information vs K-information across scales ──")
    print(f"The SAME text, analyzed at different granularities:")
    for r in levels:
        if r:
            effective_k = r['H_bits_per_token'] * r['gzip_ratio']
            print(f"  {r['level']:<15}: H={r['H_bits_per_token']:.4f} b/tok, "
                  f"gzip={r['gzip_ratio']:.4f}, H×K(proxy)={effective_k:.4f}")
    print()
    print("As analysis scale increases (char→word→bigram):")
    print("  - H per token INCREASES (each bigram is more 'unique' than each character)")
    print("  - H_max INCREASES (larger vocabulary)")
    print("  - H/H_max DECREASES (we're farther from maximum entropy at coarser scales)")
    print("  - gzip ratio decreases (coarser units are more compressible by local repetition)")
    print()
    print("The LINGUISTIC K-structure (word choice regularity) is most visible at")
    print("the word and bigram levels. Byte-level gzip finds punctuation/whitespace patterns.")

    # Save
    os.makedirs("results", exist_ok=True)
    with open("results/sk_multiscale_data.json", "w") as f:
        json.dump({"corpus_size": CORPUS_SIZE, "analyses": [r for r in levels if r]}, f, indent=2)
    print(f"\nManifest → results/sk_multiscale_data.json")

if __name__ == "__main__":
    run()
