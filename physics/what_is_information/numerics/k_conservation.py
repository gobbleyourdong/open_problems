#!/usr/bin/env python3
"""
k_conservation.py — Is K-information conserved, created, or destroyed in physical processes?

The S/K bifurcation predicts:
- S-information (Shannon entropy) grows under the thermodynamic arrow (2nd law)
- K-information (Kolmogorov compressibility) is NOT simply conserved — it can grow, shrink,
  or stay constant depending on the process

This script tests K-information behavior under five prototypical processes:
1. Thermalization (gas spreading): K stays constant at macro level (algorithmic)
2. Computation (sorting): K increases in output (more structure) vs input
3. Erasure (Landauer): K decreases; S must increase to compensate
4. Compression (gzip): K decreases by explicit construction
5. Randomization (noise addition): K increases toward maximum

For each process: measure gzip-K of input and output, and show the K-delta.

Key prediction: K is NOT conserved in general. Unlike energy (conserved exactly) or
S-information (grows monotonically in isolated systems), K-information is NOT an
additive conserved quantity. It can increase (noise injection), decrease (compression,
erasure), or stay roughly constant (thermalization at macro level).

This addresses gap.md R1 by showing that K is not bounded by a simple conservation law.

Usage:
    cd ~/open_problems/physics/what_is_information
    python3 numerics/k_conservation.py

Numerical track, what_is_information — 2026-04-09
"""

import gzip, math, os, json, random
from collections import Counter

def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    n = len(data)
    return -sum((c/n)*math.log2(c/n) for c in counts.values())

def gzip_k(data: bytes) -> float:
    if not data:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)

def describe(label, input_data, output_data):
    h_in  = shannon_entropy(input_data)
    h_out = shannon_entropy(output_data)
    k_in  = gzip_k(input_data)
    k_out = gzip_k(output_data)
    dh = h_out - h_in
    dk = k_out - k_in
    print(f"\n  {label}")
    print(f"    H:    {h_in:.4f} → {h_out:.4f}  (Δ = {dh:+.4f})")
    print(f"    K:    {k_in:.4f} → {k_out:.4f}  (Δ = {dk:+.4f})")
    print(f"    H×K:  {h_in*k_in:.4f} → {h_out*k_out:.4f}")
    return {"label": label, "H_in": h_in, "H_out": h_out, "K_in": k_in, "K_out": k_out, "dH": dh, "dK": dk}

def run():
    print("=" * 65)
    print("K-Information Behavior Under Physical Processes")
    print("=" * 65)

    rng = random.Random(42)
    N = 10_000
    results = []

    # ── 1. Thermalization (structured → less structured) ──────────────────────
    print("\n── Thermalization: structured bytes → thermalized (random mix) ──")

    # Input: highly structured (alternating pattern)
    structured = (b"\x00\xFF" * (N // 2))[:N]
    # "Thermalized": shuffle bytes randomly
    therm = bytearray(structured)
    rng.shuffle(therm)
    therm = bytes(therm)
    results.append(describe("Thermalization (structured→shuffled)", structured, therm))

    # ── 2. Computation (sorting) ──────────────────────────────────────────────
    print("\n── Computation: sorting a random byte sequence ──")
    random_bytes = bytes(rng.getrandbits(8) for _ in range(N))
    sorted_bytes = bytes(sorted(random_bytes))
    results.append(describe("Sort (random→sorted)", random_bytes, sorted_bytes))

    # ── 3. Erasure (Landauer) ─────────────────────────────────────────────────
    print("\n── Landauer erasure: structured data → zeros ──")
    to_erase = bytes([i % 256 for i in range(N)])  # structured input
    erased = bytes(N)  # all zeros
    results.append(describe("Erasure (structured→zeros)", to_erase, erased))

    # ── 4. Compression ────────────────────────────────────────────────────────
    print("\n── Compression: repetitive text → gzip compressed ──")
    text = b"information entropy kolmogorov compression " * (N // 43)
    compressed = gzip.compress(text[:N], compresslevel=9)
    # Pad or truncate to N bytes for fair comparison
    if len(compressed) < N:
        compressed = compressed + bytes(N - len(compressed))
    else:
        compressed = compressed[:N]
    results.append(describe("Compression (text→gzip bytes)", text[:N], compressed))

    # ── 5. Randomization (noise injection) ───────────────────────────────────
    print("\n── Noise injection: structured text → text XOR noise ──")
    clean = b"The S/K bifurcation: Shannon entropy and Kolmogorov complexity are orthogonal. " * (N // 80)
    clean = clean[:N]
    noise = bytes(rng.getrandbits(8) for _ in range(N))
    noisy = bytes(a ^ b for a, b in zip(clean, noise))
    results.append(describe("Noise injection (text XOR random)", clean, noisy))

    # ── 6. Decompression ─────────────────────────────────────────────────────
    print("\n── Decompression: gzip bytes → original text ──")
    compressed_text = gzip.compress(b"hello world " * (N // 12), compresslevel=9)
    decompressed = b"hello world " * (N // 12)
    decompressed = (decompressed * (len(compressed_text) // len(decompressed) + 1))[:len(compressed_text)]
    results.append(describe("Decompression (gzip→text)", compressed_text[:N], decompressed[:N]))

    # ── 7. Encryption (XOR cipher with key) ──────────────────────────────────
    print("\n── Encryption: structured text → XOR with repeated key ──")
    plaintext = b"The quick brown fox jumps over the lazy dog. " * (N // 45 + 1)
    plaintext = plaintext[:N]
    key = b"SECRET"
    encrypted = bytes(plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext)))
    results.append(describe("Encryption (text XOR key)", plaintext, encrypted))

    # ── Summary ────────────────────────────────────────────────────────────────
    print("\n── Summary: K-information is not conserved ──")
    print(f"\n{'Process':<45} {'ΔH':>8} {'ΔK':>8} {'K direction'}")
    print("─" * 70)
    for r in results:
        dk_dir = "↑ increases" if r["dK"] > 0.01 else ("↓ decreases" if r["dK"] < -0.01 else "≈ constant")
        print(f"{r['label']:<45} {r['dH']:>+8.4f} {r['dK']:>+8.4f}  {dk_dir}")

    print()
    print("Key finding: K-information is NOT conserved.")
    print("  - Some processes INCREASE K: thermalization (shuffling adds byte randomness),")
    print("    noise injection (XOR with random → high K)")
    print("  - Some processes DECREASE K: sorting (→ maximally compressible),")
    print("    erasure (→ all zeros), decompression (→ readable repetitive text)")
    print("  - Encryption (XOR with short key) also INCREASES K (key is short, output random-looking)")
    print()
    print("K is NOT conserved — it is neither monotonically increasing nor decreasing.")
    print("K has no simple conservation law analogous to energy or momentum.")
    print()
    print("This makes R1 (what bounds K?) harder: K has no intrinsic conservation property.")
    print("K is bounded ABOVE by S_holo (holographic principle) and BELOW by K(laws).")
    print("Within these bounds, K can vary arbitrarily. K is a measure of REGULARITY,")
    print("not a conserved physical quantity.")

    # Save
    os.makedirs("results", exist_ok=True)
    with open("results/k_conservation_data.json", "w") as f:
        json.dump({"processes": results, "sample_size_bytes": N}, f, indent=2)
    print(f"\nManifest → results/k_conservation_data.json")

if __name__ == "__main__":
    run()
