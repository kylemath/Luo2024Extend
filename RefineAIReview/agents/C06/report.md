# C06: Contradiction in One-Shot Deviation Argument

## Assessment: GREEN

## Reviewer Comment
> "the one-shot deviation argument is identical" followed by "adding this θ_t-dependent term can in principle change the OT solution"

## Location
`sec_05_proof.tex`, Lemma 5.1 proof (line 64) and subsequent discussion (lines 67–74).

## Analysis

The reviewer correctly identifies that two statements appear contradictory:

1. **Line 64** (end of Lemma 5.1 proof): "the one-shot deviation argument is identical"
2. **Line 69** (subsequent discussion): "adding this θ_t-dependent term can in principle change the OT solution"

### The Resolution

These statements are **not logically contradictory** once properly parsed, but the paper's exposition makes them appear so. The issue is one of imprecise scoping:

**Statement 1** ("argument is identical") refers to the **structure** of the proof: given an objective function w(θ̃, a₁), the one-shot deviation analysis proceeds by the same OT/cyclical-monotonicity logic as in Luo–Wolitzky. The combinatorial structure of the argument is unchanged. This is correct.

**Statement 2** ("can change the OT solution") refers to the **content** of the objective: in the Markov case, the effective objective is w = u₁ + g where g depends on θ_t. Since g changes the objective, the OT solution for w may differ from the OT solution for u₁ alone. This is also correct.

The contradiction is in the **juxtaposition**, not the logic. The paper needs to clearly distinguish:
- (i) **Structural claim**: Conditional on a given objective w, the OT argument has the same structure (one-shot deviation → cyclical monotonicity → confound-defeating). This carries over unchanged.
- (ii) **Content claim**: The objective w itself differs in the Markov case (w = u₁ + g instead of w = u₁), so confound-defeating with respect to u₁ does not automatically imply confound-defeating with respect to w.

### The Fix

Add a transitional sentence explicitly scoping the two claims. The structural claim should be stated first, then the content difference should be introduced with a clear signal that it's about a different aspect of the argument.

## Resolution

Editorial fix: restructure the paragraph to clearly delineate the structural vs. content claims. No mathematical changes needed—both statements are individually correct; only the juxtaposition is misleading.
