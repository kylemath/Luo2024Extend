# C11 Analysis Report: Incorrect Inference from Filter Stability

## Comment Summary
**Severity**: HIGH  
**Location**: `sec_10_discussion.tex`, Section 10.2, same ε-perturbed strategies paragraph  
**Reviewer claim**: Same core issue as C07. The phrase "filter stability (SA4) suggests that beliefs may converge to the stationary distribution" conflates two distinct notions: (1) forgetting of the initial prior, and (2) convergence of the posterior to π.

## Diagnosis

### Relationship to C07
This comment targets the same sentence as C07 but emphasizes the *inference structure* rather than the conceptual definition. Where C07 identifies the conceptual error ("filter stability ≠ belief convergence to π"), C11 identifies the logical error ("filter stability does not *imply* belief convergence to π").

### The Invalid Inference
The paper's logic chain in the ε-perturbed paragraph is:
1. Strategy s₁^ε is not state-revealing (✓ correct)
2. Filter stability (SA4) holds for the resulting HMM (✓ correct)
3. Therefore beliefs may converge to π (✗ invalid inference)

The gap: filter stability is a statement about the *operator norm* of the filter update map — it contracts initial conditions. But the *fixed point* of the filter (what it converges to regardless of initialization) is determined by the observation channel, not by the stationary distribution of the hidden chain. Specifically:

- If observations are perfectly informative (ε = 0): fixed point tracks θ_t exactly
- If observations are partially informative (small ε): fixed point is a smoothed version of the indicator on θ_t, still far from π
- If observations are uninformative (ε → 1): fixed point approaches π

The inference "filter stability → beliefs converge to π" is structurally analogous to saying "a contraction mapping has a fixed point, therefore the fixed point is zero." The contraction property tells you the fixed point exists and is unique; it tells you nothing about *where* the fixed point is.

### What Would Be Needed for Belief Convergence to π
For the posterior to converge to π, one would need:
- The observation channel to lose all state-discriminating power (ε → 1), OR
- The conditional observation distributions g(·|θ) to be identical across θ (trivial observations), OR
- An infinite-memory averaging effect that doesn't exist in finite-state HMMs with informative channels

### Impact Assessment
Like C07, this affects only the speculative discussion in Section 10.2, not the formal results. However, the invalid inference pattern could propagate to future work if uncorrected. The reviewer is flagging a reasoning error, not just a wording issue.

## Proposed Resolution
The fix for C11 is subsumed by the fix for C07 — the rewritten paragraph correctly states what filter stability provides (prior forgetting) and does not make the invalid inference to belief convergence. The proposed edit for C07 includes a footnote explicitly distinguishing the three concepts.

Additional suggestion: add one sentence making the inference gap explicit, e.g., "Filter stability guarantees that the filter's fixed point is unique, but does not determine its location; for informative channels, the fixed point tracks the current state."

## Self-Assessment

- **Validity of reviewer comment**: ✅ Fully valid. The inference is logically unsound.
- **Severity**: HIGH is appropriate. The error reflects a misunderstanding of what filter stability implies.
- **Confidence in proposed fix**: HIGH. The C07 edit resolves this simultaneously.
- **Overlap with C07**: SUBSTANTIAL. Both target the same sentence. The joint fix addresses both.
- **Relationship to other comments**: Related to C19 (similar imprecision in Appendix A).
