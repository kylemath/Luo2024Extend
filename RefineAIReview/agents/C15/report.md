# C15: Incorrect Claim About Confound-Defeating Conditions

## Assessment: GREEN

## Reviewer Comment
> "Persistence thus strengthens identification, making confound-defeating conditions easier to satisfy in the supermodular case."

The reviewer notes that Section 6 shows the supermodularity/monotonicity characterization of confound-defeating is UNCHANGED from i.i.d. So in what sense is it "easier to satisfy"?

## Location
`sec_08_interpolation.tex`, Section 8.6, line 41.

## Analysis

The reviewer correctly identifies an imprecision. Section 6 (Proposition 6.1) establishes that under the first-coordinate order on the lifted space θ̃, the confound-defeating ⟺ monotonicity equivalence is identical to the i.i.d. case. The **mathematical condition** is unchanged.

The paper's claim that persistence "makes confound-defeating conditions easier to satisfy" conflates two distinct concepts:

### 1. The Mathematical Condition (UNCHANGED)
The condition for confound-defeating in the supermodular case is:
- s₁* is monotone on θ̃ (equivalently, on θ_t under the first-coordinate order)

This is exactly the same condition as in Luo–Wolitzky (2024) — it depends on the payoff structure, not on the dynamics.

### 2. Empirical Verifiability (POTENTIALLY IMPROVED)
Persistence provides a richer data structure for TESTING whether the condition holds:
- Under i.i.d., actions are i.i.d. draws conditional on the type
- Under persistence, actions exhibit autocorrelation that reflects the state-contingent strategy
- Sequential patterns (e.g., "always fight after a bad outcome") are a stronger identifying feature than per-period frequencies
- This makes it potentially easier to VERIFY (not to SATISFY) the confound-defeating condition

### The Fix
Replace "easier to satisfy" with language distinguishing the mathematical condition from its empirical testability. The condition itself is the same; what changes is the richness of the identification channel.

## Resolution
Editorial fix to sec_08_interpolation.tex. Change "making confound-defeating conditions easier to satisfy" to something like "providing a richer identification channel for verifying confound-defeating conditions empirically, even though the mathematical characterization is unchanged."
