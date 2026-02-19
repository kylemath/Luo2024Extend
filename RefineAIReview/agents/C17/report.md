# C17: Confusing Motivation for Lifted State

## Reviewer Comment
> Section 1.1 says lifted state "provides a stationary distribution" which reads as if the original chain lacked one. Actually θ_t already has π; lifting creates a type space for Markov private info.

## Analysis

### Current State
In `sec_01_intro.tex`, Section 1.1, line 8:

> "We employ a *lifted state* construction $\tilde\theta_t = (\theta_t, \theta_{t-1})$, which provides a stationary distribution $\tilde\rho$ on the expanded space and allows the optimal transport framework to apply directly."

The reviewer's criticism is well-taken. The phrase "provides a stationary distribution" suggests that the original chain $\theta_t$ does not have a stationary distribution, which is false — the original chain has $\pi$ by Assumption 1(b) (sec_02_model.tex, line 14). The actual purpose of the lifting is:

1. To create a state space where the LR player's private information each period is the current transition $(\theta_t, \theta_{t-1})$, which captures the Markov structure.
2. To provide the appropriate type space for commitment types: a Markov strategy maps $\tilde\Theta \to \Delta(A_1)$.
3. To give the joint distribution $\gamma(s_1)$ the right structure for the OT framework.

Note: Remark 2.5 (`rem:key_property`, sec_02_model.tex, line 62) says: "The lifted state provides a Markov structure on which the optimal transport framework and cyclical monotonicity characterizations apply. The **key property** is that $\tilde\theta_t$ has a *fixed, known* stationary distribution $\tilde\rho$." This is clearer but still could be improved.

### Severity Assessment
**LOW** — This is a wording issue in the introduction. The model section (Section 2) is clear about the purpose.

## Proposed Resolution

Revise the sentence in Section 1.1 to clarify that:
1. The original chain already has a stationary distribution $\pi$
2. The lifting creates the appropriate type space for Markov private information
3. The distribution $\tilde\rho$ enables the OT framework on the expanded space

## Self-Assessment
- **Confidence**: HIGH — Simple wording fix.
- **Risk**: NONE — No mathematical content changes.
- **Verification needed**: None.
