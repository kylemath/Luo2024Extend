# C01: Incorrect Scaling of Continuation Values

## Assessment: GREEN

## Reviewer Comment
> "Combined with δ→1 (which makes the continuation value perturbation small relative to the stage-game payoff)"

## Location
`sec_05_proof.tex`, Remark 5.4 (`rem:continuation`), line 74.

## Analysis

The reviewer is **correct**. Under the standard discounted payoff normalization:

$$W = (1-\delta)\sum_{t=0}^{\infty} \delta^t u_t$$

the Bellman equation for a one-shot deviation at period $t$ is:

$$V = (1-\delta)u_1(\theta_t, a_1, \alpha_2) + \delta \mathbb{E}[V(\theta_{t+1})]$$

As $\delta \to 1$:
- The stage-game payoff weight $(1-\delta) \to 0$
- The continuation value weight $\delta \to 1$

So continuation values become **MORE** important relative to the stage-game payoff, not less. The paper's claim is backwards.

## What the Paper Actually Needs

The paper's argument in Remark 5.4 conflates two distinct mechanisms:

1. **Filter stability**: The filtering distribution $\pi_t(h_t)$ converges to the stationary distribution $\tilde{\rho}$ exponentially fast. This makes the $\theta_t$-dependent perturbation of the continuation value small for large $t$, because the filtering beliefs settle down and the continuation value's dependence on $\theta_t$ diminishes.

2. **Front-loading via $\delta \to 1$**: As $\delta \to 1$, any finite number of initial "bad" periods (where filter stability hasn't kicked in) become negligible in the discounted sum. This is the standard front-loading argument used in Step 5.

These are **separate** effects that work together:
- Filter stability handles the *asymptotic* regime (large $t$): the perturbation g(θ_t, a₁, h_t) becomes small.
- $\delta \to 1$ handles the *transient* regime (small $t$): the initial periods where filter stability hasn't yet kicked in become negligible.

The paper incorrectly attributes the smallness of the perturbation to $\delta \to 1$ (the Bellman weight), when it's actually filter stability that makes the perturbation small, and $\delta \to 1$ that makes the transient period irrelevant.

## Resolution

Replace the incorrect sentence with a corrected explanation that properly attributes each effect. The correction is straightforward and does not affect any formal results—only the informal explanation in the remark.

## Verification

The formal proof in Subsections 5.5 (Step 5) does not use this incorrect claim. The formal argument proceeds via the front-loading argument directly and is sound. Only the intuitive explanation in Remark 5.4 contains the error.
