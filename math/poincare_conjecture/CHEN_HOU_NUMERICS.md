# Chen-Hou 2025 Part II: Rigorous Numerics — Key Findings

Source: arXiv:2305.05660 (Chen-Hou, "...Part II: Rigorous Numerics")
Extracted by: Gemini (some chain-of-thought leakage, content verified)

## 1. Interval Arithmetic: INTLAB (MATLAB)
- Uses INTLAB package in MATLAB
- Basic interval arithmetic (not fancy — just tracks round-off rigorously)
- Every floating-point operation returns an interval [lower, upper] instead of a point value
- This makes ALL numerical bounds rigorous, not approximate

## 2. Stability Lemma Inequalities (Lemma 2.1)
The computer-assisted proof verifies TWO inequalities for all x, z, t∈[0,T]:

**Inequality 1 (Damping dominates):**
  ι_ii(x,z,t)·E* - Σ_{j≠i} (|a_ij|·E* + |a_ij,2|·E*² + |a_ij,3(x,z,t)|) > ε₀

**Inequality 2 (Bounded coupling):**
  Σ_{j≠i} (|a_ij|·E* + |a_ij,2|·E*² + |a_ij,3(x,z,t)|) < M

If both hold with E(0) < E*, then E(t) < E* for all t∈[0,T].
→ The perturbation stays bounded → the self-similar profile is stable → blowup happens.

## 3. Grid Resolution

### Profile Mesh (Adaptive)
- N = 748 points
- Domain: [0, L]² where L = 10¹⁵ (massive — captures far-field decay)
- Near-origin: spacing = 1/256 ≈ 0.0039 (exact binary for round-off safety)
- Far-field: exponentially growing spacing
- Representation: piecewise 6th-order B-splines
- Refinement: 3× for linearized equations (3 points per interval)

### Integral Mesh (for Biot-Savart)
- h_x = 13·2⁻¹² ≈ 0.0032 (exact binary)
- h = 13·2⁻¹¹ ≈ 0.0064 (exact binary)
- x_c = 13·2⁻⁵ ≈ 0.4

Note: grid parameters chosen as exact binary fractions to eliminate
representation error in interval arithmetic.

## 4. Biot-Savart Integral Bounds (5-part strategy)

1. **Symmetrization**: Exploit odd/even symmetry to cancel leading singularities
   before integrating (K_sym kernels)
2. **Domain decomposition**: Split into near-field, bulk, far-field
3. **Rigorous quadrature (bulk)**: Trapezoidal rule with derived error bounds
   using L∞ norms of kernel second derivatives
4. **Analytic integration (singular core)**: Isolate K₀₀, K_ux0 parts near
   origin, integrate via Taylor expansion of weights/functions
5. **Asymptotic bounds (far-field)**: Known decay rates of functions/kernels

All operations wrapped in INTLAB interval arithmetic.

## 5. Error Tolerance

E* = 5 × 10⁻⁶

The bootstrap assumption: if E(0) < E* = 5e-6, then E(t) < E* for all time.
This is the threshold the computer-assisted bounds must verify.
The residual error from the approximate profile must be smaller than this.

## 6. MATLAB Verification Code

Available at: https://jiajiechen94.github.io/codes
Referenced as [10] in the paper.
Contains all computer-assisted proof computations.

## Our Implementation Plan

| Chen-Hou | Our Equivalent |
|----------|---------------|
| INTLAB (MATLAB) | Python `mpmath` or custom interval class |
| N=748 adaptive mesh | Our Chebyshev grid (different but equivalent purpose) |
| 6th-order B-splines | Chebyshev spectral (higher order, fewer points needed) |
| Lemma 2.1 inequalities | Lean theorem statements + computed bounds |
| E* = 5e-6 | PySR-discovered tolerance from our data |
| MATLAB verification | Python + Lean (reproducible, open) |

## Cross-Verification Status
- INTLAB: well-known library, not hallucination ✓
- N=748: specific, consistent with "up to 1536²" mention in framework ✓
- E*=5e-6: specific numerical value, plausible for blowup proof ✓
- MATLAB code link: verifiable URL ✓
- Grid parameters as binary fractions: clever trick, not obvious enough to hallucinate ✓
- Lemma 2.1 structure: consistent with Part I stability framework ✓
