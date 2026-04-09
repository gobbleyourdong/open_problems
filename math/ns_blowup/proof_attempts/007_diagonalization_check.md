---
test: Does Q diagonalize in Fourier space for divergence-free fields?
result: NO — diagonalization FAILS
implication: Nemotron's proof (004) is invalid. Use Manus (005) or ChatGPT (006).
---

## Test
Computed Q = ω·S·ω - ν|∇ω|² for a random div-free field at N=4.

## Result
- Nemotron's predicted integral (Σ |k|²|ω̂|²) = 9320
- Actual integral of stretching = -0.23
- They don't match. The formula is WRONG pointwise.

## Why It Fails
Nemotron's equation (1) confuses the spatial AVERAGE with the pointwise value.
- The spatial average of Q can be written as a sum over modes (Parseval)
- The POINTWISE value Q(x) involves triadic convolutions (three Fourier modes interacting)
- The convolution does NOT reduce to per-mode terms

## Consequence
- Nemotron's clean 6-step proof is invalid
- The proof must handle the trilinear structure
- Manus's Latala inequality or ChatGPT's alignment-rarity argument are the correct approaches
- The ranking changes: Manus #1, ChatGPT #2, Grok #3

## Updated Ranking
1. **Manus (005)** — correctly trilinear, Latala's inequality, two proof tracks
2. **ChatGPT (006)** — best intuition, alignment rarity, explains TG plateau
3. **Grok (002)** — spectral convergence fallback, doesn't need diagonalization
4. **Nemotron (004)** — INVALID (wrong about diagonalization)
5. **Gemini (001)** — framework only
6. **Mistral (003)** — supporting ideas
