# C08: Arithmetic Error in Belief-Robust Condition

## Severity: HIGH
## Self-Assessment: RED

## Reviewer Concern

Section 7.4 states: `μ* = 0.60 < β = 0.5`, but `0.60 > 0.5`. With `(α,β) = (0.3, 0.5)`, belief-robustness requires `μ* < β`, which `0.60` violates.

## Independent Verification

### The claimed inequality:
```
Paper: μ* = BRThreshold = 0.60 < β = BaseBeta = 0.50
Truth: 0.60 > 0.50  ← FALSE
```

### Belief-robust condition requires:
For SR to cooperate in ALL states, we need `μ* ≤ min_θ F(G|θ)`.

The filtering beliefs are:
- `F(G|G) = 1 - α = 0.70`
- `F(G|B) = β = 0.50`
- `min F(G|θ) = 0.50`

So belief-robustness requires `μ* ≤ 0.50`. With `μ* = 0.60 > 0.50`, SR defects after bad states, and the game is NOT belief-robust.

### Additional error — BRPayoff:
Section 7.4 states `V(s1*) = BRPayoff = 0.60`, but the Proposition gives `V(s1*) = β/(α+β) = 0.625`. So `BRPayoff` is also wrong.

## Root Cause

Two errors in stats.tex:
1. `BRThreshold = 0.60` should be `< 0.50` for belief-robustness
2. `BRPayoff = 0.60` should be `0.625` (matching `β/(α+β)`)

These may have originated from the same source: both happen to be 0.60, suggesting a copy-paste or conflation of the SR threshold (Version 2, μ* = 0.60 for the non-belief-robust case) with the belief-robust threshold (Version 1, which needs μ* < β = 0.50).

## Proposed Resolution

### Fix 1: Change `BRThreshold` to 0.40
With `μ* = 0.40`:
- `μ* = 0.40 < β = 0.50` ✓
- `F(G|G) = 0.70 ≥ 0.40` ✓
- `F(G|B) = 0.50 ≥ 0.40` ✓
- SR cooperates in all states → belief-robust ✓

### Fix 2: Change `BRPayoff` to 0.625
Under belief-robustness, the formal bound from Proposition 1 is:
`V(s1*) = β/(α+β) = 0.625`

### Required file changes:
1. **stats.tex**: `\BRThreshold{0.60}` → `\BRThreshold{0.40}`, `\BRPayoff{0.60}` → `\BRPayoff{0.625}`
2. **sec_07_example.tex, Section 7.4**: text automatically updates via macros, but verify the surrounding prose still reads correctly

## What Is NOT Wrong

- The concept of belief-robustness is correctly defined
- The formal theorems (belief-robust and general) are correctly stated
- Version 2 (non-belief-robust, μ* = SRThreshold = 0.60) is correct
- The filtering belief formulas `F(G|G) = 1-α` and `F(G|B) = β` are correct
