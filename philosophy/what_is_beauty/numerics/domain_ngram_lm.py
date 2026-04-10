"""
domain_ngram_lm.py — Cycle 21
Numerical Track: what_is_beauty

Build a simple domain-specific n-gram language model trained on mathematical
vocabulary, then compare its NLL to GPT-2's NLL on compressed math stimuli.

Theory: the compression-beauty prediction should hold MORE STRONGLY under a
domain-specific prior than under GPT-2's generic prior.

Test: if the domain LM gives better within-register correlation than GPT-2,
this confirms that the signal IS in the domain-specific compression, not
just generic prior novelty.

Domain training corpus: mathematical text samples from classic theorems,
definitions, and proofs (manually curated to represent the domain structure
without memorising the evaluation stimuli).
"""

import math
import re
from collections import Counter, defaultdict
from scipy.stats import spearmanr
import numpy as np


# ---------------------------------------------------------------------------
# Training corpus: mathematical text NOT including the evaluation stimuli
# ---------------------------------------------------------------------------

MATH_CORPUS = """
A prime number is a natural number greater than one that has no positive divisors other than one and itself.
The fundamental theorem of arithmetic states that every integer greater than one is either prime or a product of primes in a unique way.
The sum of an infinite geometric series with first term a and ratio r converges to a divided by one minus r when the absolute value of r is less than one.
The binomial coefficient n choose k equals n factorial divided by k factorial times n minus k factorial.
An injective function maps distinct inputs to distinct outputs while a surjective function maps to every element of the codomain.
The Cauchy sequence of rational numbers has terms that become arbitrarily close together.
The intermediate value theorem guarantees that a continuous function on a closed interval attains every value between its endpoint values.
Taylor's theorem approximates differentiable functions by polynomials centered at a point.
A metric space consists of a set and a distance function satisfying non-negativity symmetry and triangle inequality.
The spectral theorem for symmetric matrices guarantees a basis of orthogonal eigenvectors.
If a function is differentiable then it is continuous but the converse is not necessarily true.
The Bolzano-Weierstrass theorem states that every bounded sequence in real numbers has a convergent subsequence.
The fundamental theorem of calculus connects differentiation and integration as inverse operations.
A group homomorphism preserves the group structure by mapping products to products.
The axiom of choice is equivalent to Zorn's lemma and the well-ordering theorem.
Cantor showed that the set of real numbers is uncountable using his diagonal argument.
The completeness axiom of real numbers states that every nonempty set bounded above has a least upper bound.
Fermat's little theorem states that if p is prime then a to the power p minus a is divisible by p.
The Pythagorean theorem relates the sides of a right triangle by the equation a squared plus b squared equals c squared.
A topological space is connected if it cannot be partitioned into two disjoint nonempty open sets.
The Heine-Borel theorem characterizes compact subsets of real numbers as closed and bounded sets.
Complex numbers extend the real numbers by including the imaginary unit i satisfying i squared equals negative one.
The fundamental group of a topological space captures information about loops up to continuous deformation.
Linear independence means no vector in the set can be expressed as a linear combination of the others.
The determinant of a square matrix equals zero if and only if the matrix is singular.
An eigenvalue of a linear transformation is a scalar by which an eigenvector is scaled.
The chain rule states that the derivative of a composite function is the product of the derivatives.
Integration by parts is the product rule for integrals involving two functions.
A convergent series has partial sums approaching a finite limit as the number of terms grows.
Rolle's theorem implies the mean value theorem for differentiable functions on closed intervals.
"""


# ---------------------------------------------------------------------------
# Simple word-level trigram model
# ---------------------------------------------------------------------------

def tokenize(text):
    """Simple word tokenizer."""
    return re.findall(r"[a-zA-Z0-9']+|[.,;:!?()]", text.lower())


def train_ngram(text, n=3):
    """Train n-gram model, return (unigram, bigram, trigram) counts."""
    tokens = ["<BOS>", "<BOS>"] + tokenize(text) + ["<EOS>"]
    unigrams  = Counter(tokens)
    bigrams   = Counter(zip(tokens, tokens[1:]))
    trigrams  = Counter(zip(tokens, tokens[1:], tokens[2:]))
    return unigrams, bigrams, trigrams


def ngram_nll(text, unigrams, bigrams, trigrams, smooth=0.1):
    """
    Compute mean NLL per token under trigram model with Laplace smoothing.
    P(w3 | w1, w2) = (count(w1,w2,w3) + smooth) / (count(w1,w2) + smooth * V)
    """
    tokens = ["<BOS>", "<BOS>"] + tokenize(text) + ["<EOS>"]
    V = len(unigrams) + 1
    nll = 0.0
    n_tokens = max(len(tokens) - 2, 1)
    for i in range(2, len(tokens)):
        w1, w2, w3 = tokens[i-2], tokens[i-1], tokens[i]
        c_tri  = trigrams.get((w1, w2, w3), 0) + smooth
        c_bi   = bigrams.get((w1, w2), 0) + smooth * V
        p = c_tri / c_bi
        nll += -math.log(p)
    return nll / n_tokens


# ---------------------------------------------------------------------------
# Evaluation stimuli (the n=14 compressed math statements from Cycle 10)
# ---------------------------------------------------------------------------

STIMULI = [
    ("Euler identity",         "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",            9.5),
    ("Ramanujan sum",          "1 + 2 + 3 + 4 + ... = -1/12. The zeta function at -1 assigns a finite value to a divergent sum.", 8.0),
    ("Euler's formula",        "e^(ix) = cos(x) + i*sin(x). Complex exponentials are rotations.",           8.5),
    ("Euler's polyhedral",     "V - E + F = 2 for any convex polyhedron. Vertices minus edges plus faces equals two.",             8.5),
    ("Fermat's Last Theorem",  "x^n + y^n = z^n has no positive integer solutions for n > 2.",             8.0),
    ("Cantor's theorem",       "|P(S)| > |S| for any set S. Every set is strictly smaller than its power set.", 8.5),
    ("Stirling approximation", "n! is approximately sqrt(2*pi*n) * (n/e)^n for large n.",                  6.0),
    ("Gaussian integral",      "The integral of e^(-x^2) from -infinity to infinity equals sqrt(pi).",      7.0),
    ("AM-GM inequality",       "The arithmetic mean of positive numbers is always at least as large as their geometric mean: (a+b)/2 >= sqrt(ab).", 5.5),
    ("Euler-Mascheroni",       "The harmonic series minus ln(n) converges to gamma = 0.5772...",            6.0),
    ("Distance formula",       "The distance between (x1,y1) and (x2,y2) is sqrt((x2-x1)^2 + (y2-y1)^2).", 3.5),
    ("Slope formula",          "The slope of a line through (x1,y1) and (x2,y2) is (y2-y1)/(x2-x1).",    2.5),
    ("Trig identities (list)", "sin^2(x) + cos^2(x) = 1. tan(x) = sin(x)/cos(x). sin(a+b) = sin(a)cos(b) + cos(a)sin(b).", 3.0),
    ("Circle area formula",    "The area of a circle is pi*r^2, where r is the radius.",                    2.0),
]

# Pre-computed GPT-2 NLL from Cycle 10
GPT2_NLL = {
    "Euler identity":         5.042, "Ramanujan sum":          3.754,
    "Euler's formula":        4.012, "Euler's polyhedral":     4.879,
    "Fermat's Last Theorem":  3.928, "Cantor's theorem":       5.211,
    "Stirling approximation": 4.064, "Gaussian integral":      4.260,
    "AM-GM inequality":       3.756, "Euler-Mascheroni":       5.198,
    "Distance formula":       1.633, "Slope formula":          2.219,
    "Trig identities (list)": 2.021, "Circle area formula":    3.678,
}


def run():
    # Train domain n-gram model
    unigrams, bigrams, trigrams = train_ngram(MATH_CORPUS, n=3)
    print(f"Domain LM vocabulary: {len(unigrams)} unique tokens")
    print(f"Domain LM corpus: {len(tokenize(MATH_CORPUS))} tokens")

    print("=" * 72)
    print("DOMAIN N-GRAM LM vs GPT-2 — what_is_beauty Cycle 21")
    print("=" * 72)

    domain_nlls = []
    gpt2_nlls   = []
    ratings     = []

    print(f"\n  {'Label':<35} {'domain_nll':>11} {'gpt2_nll':>10} {'rating':>7}")
    print("-" * 66)
    for label, text, rating in STIMULI:
        d_nll = ngram_nll(text, unigrams, bigrams, trigrams)
        g_nll = GPT2_NLL.get(label, None)
        domain_nlls.append(d_nll)
        ratings.append(rating)
        if g_nll:
            gpt2_nlls.append(g_nll)
        g_str = f"{g_nll:10.3f}" if g_nll else "      N/A"
        print(f"  {label:<35} {d_nll:11.3f} {g_str} {rating:7.1f}")

    rho_d, p_d = spearmanr(domain_nlls, ratings)
    rho_g, p_g = spearmanr(gpt2_nlls, ratings)

    print(f"\n  Domain n-gram NLL:  r={rho_d:+.3f}  p={p_d:.4f}")
    print(f"  GPT-2 NLL:          r={rho_g:+.3f}  p={p_g:.4f}")
    print()
    if rho_d > rho_g:
        print(f"  Domain LM OUTPERFORMS GPT-2: {rho_d:.3f} > {rho_g:.3f}")
        print(f"  Theory prediction CONFIRMED: richer domain prior → better correlation")
    else:
        print(f"  GPT-2 outperforms domain LM: {rho_d:.3f} < {rho_g:.3f}")
        print(f"  Possible reasons: domain LM too small (single paragraph corpus)")


if __name__ == "__main__":
    run()
