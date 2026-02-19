# C07 Analysis Report: Conceptual Error Regarding Filter Stability

## Comment Summary
**Severity**: HIGH  
**Location**: `sec_10_discussion.tex`, paragraph on ε-perturbed strategies (line 16)  
**Reviewer claim**: Section 10.2 suggests that ε-perturbed strategies cause beliefs to "converge to the stationary distribution." Filter stability means the initial *prior* is forgotten, not that the posterior converges to π. For small ε, signals remain very informative, so μ_t tracks θ_t rather than settling at π.

## Diagnosis

### Problematic Text
The exact passage is:

> "filter stability (SA4) suggests that beliefs may converge to the stationary distribution"

### Why the Reviewer Is Correct

Filter stability (Proposition A.2 / `prop:filter_stability`) establishes:

$$\sup_{\pi_0, \pi_0'} \|\pi_t - \pi_t'\| \leq C \cdot \lambda^t$$

This says: two filters initialized at *different priors* π₀ and π₀' converge to each other exponentially fast. The initial prior is "forgotten." It does **not** say the posterior converges to the stationary distribution π.

For ε-perturbed strategies with small ε:
- The commitment type plays s₁^ε(θ) = (1−ε)s₁*(θ) + ε·uniform
- Signals are still highly informative about the current state θ_t (Fisher information ∝ 1/ε for small ε)
- The posterior μ_t will therefore *track* θ_t via approximately F(·|θ_t), not settle at π
- Only in the limit ε → 1 (completely uninformative signals) would μ_t → π

The conflation arises because filter stability and chain mixing are related but distinct:
1. **Chain mixing**: θ_t's marginal distribution converges to π regardless of θ₀ (property of the Markov chain itself)
2. **Filter stability**: the filter π_t(·|y₀,...,y_t) forgets its initial prior π₀ (property of the filtering process)
3. **Belief convergence to π**: the posterior concentrates on π (would require uninformative observations)

The paper incorrectly infers (3) from (2).

### Impact on Paper Claims
This is a conceptual error in the discussion section (Section 10.2), not in the formal results. The ε-perturbed strategy discussion is speculative ("suggests," "may"), and no theorem depends on this claim. However, it misrepresents filter stability to the reader and could mislead follow-up work.

## Proposed Resolution

1. **Correct the characterization** of what filter stability implies for ε-perturbed strategies
2. **Distinguish explicitly** between:
   - Prior forgetting (filter stability guarantees this)
   - Posterior tracking θ_t (happens when signals are informative, i.e., small ε)
   - Posterior converging to π (requires signals to be uninformative)
3. **Reframe the ε-perturbation discussion**: the benefit of ε-perturbation is not that beliefs converge to π, but that the strategy is no longer perfectly state-revealing, so the filtering belief F(·|θ_t) is replaced by a smoothed version that may reduce the belief gap

## Self-Assessment

- **Validity of reviewer comment**: ✅ Fully valid. The reviewer correctly identifies a conceptual conflation.
- **Severity**: HIGH is appropriate. While it doesn't affect formal theorems, it demonstrates a misunderstanding of a key technical tool used in the proof.
- **Confidence in proposed fix**: HIGH. The distinction between filter stability and belief convergence is mathematically unambiguous.
- **Risk of over-correction**: LOW. The fix clarifies without changing any formal results.
- **Relationship to other comments**: Directly related to C11 (same passage, same core issue) and C19 (similar conflation in Appendix A).
