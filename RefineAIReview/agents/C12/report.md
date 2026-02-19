# C12: Contradiction Between Figure 6 Caption and Content

## Severity: MEDIUM
## Self-Assessment: GREEN

## Reviewer Concern

The caption for the KL bound figure (Figure 6 / fig_kl_bound) and the remark in Section 5.2 both describe the Markov and i.i.d. distributions of distinguishing-period counts as "nearly identical," but the means are 8.1 (i.i.d.) vs 12.7 (Markov). Both are far below 921, so the bound holds, but "nearly identical" overstates the similarity.

## Independent Verification

### The claimed similarity:
```
i.i.d. mean count:  8.1
Markov mean count:  12.7
Difference:         4.6
Relative difference: 4.6 / 8.1 = 56.8%
```

A 57% difference in means is **not** "nearly identical." The distributions may have similar shapes (both concentrated well below the bound), but their locations differ substantially.

### The bound validity:
```
Analytical bound: T̄ = -2·log(0.01) / 0.1² = 921 periods
i.i.d. mean:     8.1  (0.88% of bound)
Markov mean:     12.7 (1.38% of bound)
```

Both means are less than 1.4% of the theoretical bound. The bound holds overwhelmingly in both cases, with a margin exceeding two orders of magnitude.

## Root Cause

The word "nearly identical" conflates two properties:
1. **Both well below the bound** — TRUE (8.1 and 12.7 are both << 921)
2. **Similar to each other** — FALSE (57% difference in means)

The important mathematical point is (1), not (2). The caption should emphasize that the bound holds for both processes, not that they are similar to each other.

## Proposed Resolution

### Fix 1: Revise the Figure caption (app_A_kl_verification.tex)
Change "nearly identical in both settings" to language that accurately describes the relationship.

### Fix 2: Revise the remark in sec_05_proof.tex
Change "nearly identical for Markov and i.i.d. processes" to more precise language.

### Suggested replacement phrasing:
"both well below the analytical bound of 921 periods (i.i.d. mean: 8.1; Markov mean: 12.7), confirming that the bound holds with large margin in both settings despite differing distributional means"

## What Is NOT Wrong

- The KL bound formula is correct
- The bound T̄ = 921 is correctly computed
- The Monte Carlo simulation methodology is sound
- The fundamental claim (KL bound extends without modification) is correct
- The mean values 8.1 and 12.7 are from computational results (not independently verifiable without running simulations, but plausible)
