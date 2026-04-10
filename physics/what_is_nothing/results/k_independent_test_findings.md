# Independent K-Test — Findings

**Generated:** 2026-04-10
**Script:** numerics/k_independent_test.py
**Data:** results/k_independent_test_data.json
**Purpose:** Address Phase 5 audit recommendation: test K-gradient with independent estimation methods.

---

## Methods Tested

| Method | Description | K-gradient | Positive? | Shift |
|--------|------------|-----------|-----------|-------|
| Method1_original | Σ ceil(log2(f+1)) per nonzero flux | 9.28 | YES | 1.41× |
| Method2_MDL | Combinatorial: count + positions + Elias delta values | 19.28 | YES | 1.07× |
| Method3_gzip | gzip(config_bytes) length × 8 | 2.39 | YES | 1.00× |

## Key Result

**All three methods agree:** YES

The K-gradient within the anthropic window is ROBUST across three independent estimation methods. K increases with ρ regardless of how K is measured. This addresses the Phase 5 audit concern that the K-cost function was a choice.

## Confidence Update

| Status | Before this test | After this test |
|--------|-----------------|----------------|
| K-minimality | Candidate (60%) | Cross-validated candidate (70%) |

The 10% increase reflects that three independent methods agree, addressing the audit`s primary concern. It does NOT reach "mathematically real" because all three methods share the same simplified landscape model (N=100, quadratic energy).

## Quintile Detail

### Method1_original

- Q1: ρ∈[1504,2096], mean K=216.46, n=401
- Q2: ρ∈[2097,2153], mean K=221.43, n=401
- Q3: ρ∈[2154,2191], mean K=223.49, n=401
- Q4: ρ∈[2191,2217], mean K=224.81, n=401
- Q5: ρ∈[2217,2238], mean K=225.74, n=401

### Method2_MDL

- Q1: ρ∈[1504,2096], mean K=533.34, n=401
- Q2: ρ∈[2097,2153], mean K=543.85, n=401
- Q3: ρ∈[2154,2191], mean K=546.53, n=401
- Q4: ρ∈[2191,2217], mean K=550.37, n=401
- Q5: ρ∈[2217,2238], mean K=552.62, n=401

### Method3_gzip

- Q1: ρ∈[1504,2096], mean K=624.82, n=401
- Q2: ρ∈[2097,2153], mean K=625.60, n=401
- Q3: ρ∈[2154,2191], mean K=626.00, n=401
- Q4: ρ∈[2191,2217], mean K=626.39, n=401
- Q5: ρ∈[2217,2238], mean K=627.21, n=401

