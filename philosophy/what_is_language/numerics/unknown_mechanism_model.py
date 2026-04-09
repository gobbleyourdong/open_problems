"""
unknown_mechanism_model.py — Cycle 5
Numerical Track: what_is_language

Models three candidate mechanisms for the 200× residual compression gap
(the gap left after medium-evidence mechanisms are accounted for).

From result_004: medium-evidence mechanisms (grounding ×10, curriculum ×5,
RLHF ×30) provide only 10^3.2 = 1500× compression of a 10^5.52 gap.
Residual: 200×. This needs to come from somewhere.

Three candidates:
  M1. Bayesian word learning (cross-situational)
  M2. Social scaffolding (joint attention + adaptive input)
  M3. Structural prior (proto-syntax, object/causality knowledge)

For each, we build a simple quantitative model and estimate the compression
factor, then check whether any combination closes the 200× gap.
"""

import math

# ---------------------------------------------------------------------------
# M1: Cross-situational word learning
# ---------------------------------------------------------------------------

def m1_cross_situational(
    vocab_size: int = 60000,
    n_referents_per_scene: int = 10,
    n_scenes_per_word: int = 15,
    noise_rate: float = 0.2,
) -> dict:
    """
    Cross-situational word learning model (Yu & Smith 2007 framework).

    A child learning word w hears w in N scenes. Each scene has K referents.
    The correct referent is present in every scene; distractors vary randomly.
    By observing co-occurrence, the child can identify the correct referent
    via intersection of the referent sets across scenes.

    Compression estimate:
    - Naive (LLM-like): need ~N_exposures_total to learn all words
      N_LLM = vocab_size × mean_exposures_per_word_in_LLM_corpus
    - Cross-situational: need ~N_scenes × K observations total
      N_human = vocab_size × n_scenes_per_word × n_referents_per_scene

    The compression ratio is the reduction in exposures needed.

    Information-theoretic estimate:
    Each scene with K referents provides log2(K) bits of information about
    which referent w refers to (assuming w appears once per scene).
    After n_scenes_per_word scenes, information accumulated = n_scenes * log2(K) bits.
    Bits needed to identify correct referent = log2(vocab_size) bits.
    n_scenes_needed = log2(vocab_size) / log2(K)

    vs. LLM passive learning: needs ~C * vocab_size exposures per word,
    where C is the number of examples needed to learn a new word (roughly
    consistent with ~100-1000 examples per word in LLM scaling).
    """
    bits_per_scene = math.log2(n_referents_per_scene) * (1 - noise_rate)
    bits_to_identify = math.log2(vocab_size)
    n_scenes_needed = math.ceil(bits_to_identify / bits_per_scene)

    # Total human data needed (tokens):
    # ~n_scenes_needed scenes per word × ~20 words per scene × vocab_size words
    tokens_human = n_scenes_needed * 20 * vocab_size

    # LLM needs: empirically ~100-10000 examples per word × vocab_size words
    # Use ~1000 as central estimate (from scaling laws and distributional learning)
    llm_exposures_per_word = 1000
    tokens_llm = llm_exposures_per_word * vocab_size

    compression = tokens_llm / max(tokens_human, 1)

    return {
        "mechanism": "Cross-situational word learning (M1)",
        "bits_per_scene": round(bits_per_scene, 3),
        "bits_to_identify": round(bits_to_identify, 2),
        "n_scenes_needed": n_scenes_needed,
        "tokens_human": round(tokens_human, 0),
        "tokens_llm": round(tokens_llm, 0),
        "compression_factor": round(compression, 1),
        "log10_compression": round(math.log10(max(compression, 1)), 3),
    }


# ---------------------------------------------------------------------------
# M2: Social scaffolding (joint attention + adaptive input)
# ---------------------------------------------------------------------------

def m2_social_scaffolding(
    fraction_attended: float = 0.85,
    fraction_relevant: float = 0.7,
    baseline_fraction: float = 0.3,
) -> dict:
    """
    Social scaffolding compression estimate.

    Children learning with a caregiver who tracks their attention have
    dramatically better word learning than children exposed to the same words
    without joint attention (Tomasello & Farrar 1986, Baldwin 1993).

    Joint attention effect: when caregiver labels an object while child
    attends to it, the word-object mapping is unambiguous. Without joint
    attention, the child must infer which of K concurrent objects is being
    named.

    Compression factor:
    - With joint attention: P(correct referent) = fraction_attended ≈ 0.85
    - Without (LLM): P(correct referent) ≈ 1/K ≈ baseline_fraction

    Each labelling event provides:
    - With joint attention:  log2(1/fraction_attended) bits to close the word
      Wait, this is the other way. Let me think.

    Actually: cross-referent resolution.
    Without joint attention: need to see word in ~K different contexts to identify
    correct referent (where K = n_referents_per_scene ≈ 10).
    With joint attention: each instance is already ~1-referent-disambiguated.
    Compression = K (referents per scene) × fraction_attended.

    Literature: Baldwin 1993 shows children with joint attention acquire
    novel words in 1-2 exposures; without joint attention, need 5-10+.
    Compression factor: ~5-10×.
    """
    k_referents = 10
    compression_jt = k_referents * fraction_attended / max(baseline_fraction, 0.01)

    # Adaptive input (child-directed speech):
    # CDS has shorter sentences, higher repetition, acoustic emphasis on keywords.
    # Compression from CDS: ~2-5× (Bengio 2009 curriculum learning estimates)
    cds_compression = 3.0

    total = compression_jt * cds_compression

    return {
        "mechanism": "Social scaffolding (M2)",
        "joint_attention_compression": round(compression_jt, 1),
        "cds_compression": cds_compression,
        "total_compression": round(total, 1),
        "log10_compression": round(math.log10(max(total, 1)), 3),
    }


# ---------------------------------------------------------------------------
# M3: Structural prior (object permanence, causality, proto-syntax)
# ---------------------------------------------------------------------------

def m3_structural_prior(
    hypothesis_space_reduction: float = 0.001,
    redundancy_factor: float = 100,
) -> dict:
    """
    Structural prior compression estimate.

    Children arrive with prior knowledge that constrains the hypothesis space
    for word meaning and grammar:
    - Object permanence: words tend to name persistent entities, not events
    - Causality: verbs tend to describe causal relations
    - Whole-object bias: new words refer to whole objects, not parts/properties
    - Mutual exclusivity: each object has one name
    - Syntactic bootstrapping: grammatical category of word constrains meaning

    Together, these reduce the hypothesis space for each new word by a factor
    of roughly 1/hypothesis_space_reduction (e.g., 1000× if the true prior
    eliminates 99.9% of possible meanings).

    With a 1000× smaller hypothesis space, each observation provides
    log2(1000) ≈ 10 bits instead of ~0 bits (in the limit of uniform prior).
    Compression ≈ hypothesis_space_reduction × 1/baseline_learning_rate.

    Literature: Markman 1990 (whole-object bias), Carey 1978 (fast mapping),
    Quine 1960 (gavagai problem). Fast mapping: children can learn a word from
    1-3 exposures with a strong structural prior. LLMs need ~hundreds.

    Central estimate: 10-100× compression from structural prior.
    """
    fast_mapping_exposures = 2          # children: 1-3 exposures
    llm_exposures_per_word = 200        # rough estimate

    compression_fast_mapping = llm_exposures_per_word / fast_mapping_exposures
    compression_hypothesis = 1.0 / hypothesis_space_reduction
    total = math.sqrt(compression_fast_mapping * compression_hypothesis)

    return {
        "mechanism": "Structural prior (M3)",
        "fast_mapping_compression": round(compression_fast_mapping, 1),
        "hypothesis_space_compression": round(compression_hypothesis, 0),
        "total_compression": round(total, 1),
        "log10_compression": round(math.log10(max(total, 1)), 3),
    }


# ---------------------------------------------------------------------------
# Gap closure analysis
# ---------------------------------------------------------------------------

def run():
    CONFIRMED_COMPRESSION = 10 ** 3.2   # medium-evidence mechanisms
    RAW_GAP = 3.33e5                    # central estimate
    RESIDUAL = RAW_GAP / CONFIRMED_COMPRESSION  # ~200×

    print("=" * 72)
    print("UNKNOWN MECHANISM MODEL — what_is_language Cycle 5")
    print("=" * 72)
    print(f"\n  Confirmed mechanisms provide: 10^3.2 = {CONFIRMED_COMPRESSION:.0f}× compression")
    print(f"  Raw gap: {RAW_GAP:.1e}×")
    print(f"  Residual to explain: {RESIDUAL:.0f}× (= 10^{math.log10(RESIDUAL):.2f})")

    m1 = m1_cross_situational()
    m2 = m2_social_scaffolding()
    m3 = m3_structural_prior()

    print("\n  Candidate mechanisms:")
    print("-" * 72)
    for m in [m1, m2, m3]:
        print(f"\n  {m['mechanism']}")
        for k, v in m.items():
            if k != "mechanism":
                print(f"    {k:<35} {v}")

    # Gap closure analysis
    print("\n  Gap closure analysis:")
    print("-" * 72)
    total_candidates = m1["compression_factor"] * m2["total_compression"] * m3["total_compression"]
    residual_after = RESIDUAL / total_candidates

    print(f"  M1 (cross-situational):  ×{m1['compression_factor']:.0f}")
    print(f"  M2 (social scaffolding): ×{m2['total_compression']:.0f}")
    print(f"  M3 (structural prior):   ×{m3['total_compression']:.0f}")
    print(f"  Combined (independent):  ×{total_candidates:.0f}")
    print(f"  Residual after M1+M2+M3: {residual_after:.3f}× "
          f"({'over' if residual_after < 1 else 'under'}-explains by {1/residual_after:.0f}×)")

    # What if mechanisms overlap at 57% (result_004 finding)?
    # Use coverage model: log-effective = sum_log × (1 - r × sum_si_sj)
    log_factors = [
        math.log10(m1["compression_factor"]),
        math.log10(m2["total_compression"]),
        math.log10(m3["total_compression"]),
    ]
    total_log = sum(log_factors)
    scopes = [lf / total_log for lf in log_factors]
    r = 0.57
    from itertools import combinations
    sum_si_sj = sum(scopes[i] * scopes[j] for i, j in combinations(range(len(scopes)), 2))
    eff_fraction = max(0, total_log - r * sum_si_sj * total_log)  # simplified
    eff_comp = 10 ** min(eff_fraction, total_log)
    residual_overlap = RESIDUAL / eff_comp

    print(f"\n  With 57% overlap (from result_004):  x{eff_comp:.0f}  residual={residual_overlap:.2f}x")

    print("\n  Summary:")
    confirmed_plus = CONFIRMED_COMPRESSION * total_candidates
    log_confirmed_plus = math.log10(confirmed_plus)
    print(f"  Confirmed (med-evidence) + M1+M2+M3: {confirmed_plus:.2e}x  vs gap {RAW_GAP:.2e}x")
    if confirmed_plus >= RAW_GAP:
        excess = confirmed_plus / RAW_GAP
        print(f"  Result: GAP CLOSED (over-explains by {excess:.0f}× if all independent)")
    else:
        shortfall = RAW_GAP / confirmed_plus
        print(f"  Result: still {shortfall:.0f}× SHORT")


if __name__ == "__main__":
    run()
