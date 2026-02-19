# C09: Arithmetic Error and Variable Confusion in Cost of Persistence

## Severity: HIGH
## Self-Assessment: RED

## Reviewer Concern

Section 8.5 states: "the cost equals 0.777 − 0.628 = 0.094" but `0.777 − 0.628 = 0.149`, not `0.094`. Also, `23.7%` is `0.149/0.628`, not "of the i.i.d. payoff."

## Independent Verification

### Error 1: Arithmetic
```
Paper:   0.777 - 0.628 = 0.094
Correct: 0.777 - 0.628 = 0.149
```
This is unambiguously wrong. The paper's LaTeX expands:
`\PayoffStationary - \PayoffFiltered = \PayoffGapAbsolute`
→ `0.777 - 0.628 = 0.094`

### Error 2: Conflation of two different "gaps"
The value 0.094 comes from the **belief gap formula**:
```
2αβ|1-α-β| / (α+β)²
= 2(0.3)(0.5)(0.2) / (0.8)²
= 0.06 / 0.64
= 0.09375 ≈ 0.094
```
This is the expected total variation distance between filtering beliefs and the stationary distribution — a **belief-space** quantity.

The value 0.149 is the **payoff gap** — the difference in LR expected payoffs between the i.i.d. and Markov scenarios.

These are related but distinct: the belief gap (0.094) measures how much SR beliefs differ; the payoff gap (0.149) measures how much LR payoffs differ. The payoff gap depends on the game's payoff structure (which amplifies the belief gap), while the belief gap is a pure probability quantity.

### Error 3: Percentage base
The paper states: "representing 23.7% of the i.i.d. payoff"

Verification:
- `0.149 / 0.777 = 0.1917 ≈ 19.2%` (percentage of i.i.d. payoff) ← NOT 23.7%
- `0.149 / 0.628 = 0.2372 ≈ 23.7%` (percentage of Markov payoff) ← MATCHES

So 23.7% is the overestimation **relative to the filtered (Markov) payoff**, meaning: "the i.i.d. payoff exceeds the Markov payoff by 23.7% of the Markov payoff." The phrasing "of the i.i.d. payoff" is incorrect.

## Root Cause

The `\PayoffGapAbsolute` macro in stats.tex is set to 0.094 (the belief gap), but Section 8.5 uses it in a context where the payoff gap (0.149) is needed. The macro name "PayoffGapAbsolute" is itself misleading — it stores a belief gap, not a payoff gap.

## Proposed Resolution

### Fix 1: Add a new macro for the payoff gap
In stats.tex:
```
\newcommand{\PayoffGapPayoff}{0.149}
```

### Fix 2: Correct Section 8.5 text
Replace: "the cost equals \PayoffStationary − \PayoffFiltered = \PayoffGapAbsolute"
With: "the cost equals \PayoffStationary − \PayoffFiltered = \PayoffGapPayoff"

### Fix 3: Correct the percentage phrasing
Replace: "representing \PayoffOverestimation\% of the i.i.d. payoff"
With: "a \PayoffOverestimation\% overestimation relative to the Markov payoff"

### Fix 4: Clarify the belief gap vs payoff gap distinction
Add a sentence explaining: "The analytical belief gap $2\alpha\beta|1-\alpha-\beta|/(\alpha+\beta)^2 = 0.094$ measures the expected TV distance in beliefs; the payoff gap of 0.149 reflects the economic amplification of this belief difference through the game's payoff structure."

## What Is NOT Wrong

- The belief gap formula and its value (0.094) are correct
- The payoff values (0.777 and 0.628) are correct
- The 23.7% figure is correctly computed (just mislabeled)
- The conceptual point about the "cost of persistence" is valid
