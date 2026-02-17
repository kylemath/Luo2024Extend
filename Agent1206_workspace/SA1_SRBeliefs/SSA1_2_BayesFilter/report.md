# SSA1_2: Bayesian Filter for SR Player Beliefs — Report

## Summary

Simulated the deterrence game with commitment strategy s₁*(G)=A, s₁*(B)=F for T=10000
periods. The SR player uses a Bayesian filter (HMM forward algorithm) to update beliefs
about the current state θ_t after observing each action.

## Results

| Setting | α | β | π(G) | Mean TV | Median TV | Min TV | Max TV | Converges to π? |
|---------|---|---|------|---------|-----------|--------|--------|-----------------|
| Baseline | 0.3 | 0.5 | 0.6250 | 0.4661 | 0.3750 | 0.0000 | 0.6250 | NO |
| High persistence | 0.1 | 0.1 | 0.5000 | 0.5000 | 0.5000 | 0.0000 | 0.5000 | NO |

## Key Findings

### Baseline (α=0.3, β=0.5)

- Mean TV distance over full run: **0.4661**
- Mean TV distance in last 1000 steps: **0.4640**
- The commitment strategy s₁*(G)=A, s₁*(B)=F **fully reveals** the state to the SR player.
- After observing action at time t, the SR player knows θ_t exactly.
- Therefore, the SR player's belief about θ_{t+1} is F(·|θ_t), NOT π.
- The TV distance ‖F(·|θ_t) − π‖ does NOT converge to zero — it fluctuates around a nonzero value.

### High persistence (α=0.1, β=0.1)

- Mean TV distance over full run: **0.5000**
- Mean TV distance in last 1000 steps: **0.5000**
- The commitment strategy s₁*(G)=A, s₁*(B)=F **fully reveals** the state to the SR player.
- After observing action at time t, the SR player knows θ_t exactly.
- Therefore, the SR player's belief about θ_{t+1} is F(·|θ_t), NOT π.
- The TV distance ‖F(·|θ_t) − π‖ does NOT converge to zero — it fluctuates around a nonzero value.

## Interpretation

The Bayesian filter with a state-revealing strategy does NOT produce beliefs that converge
to the stationary distribution π. Instead, each period's observation reveals the state,
and the belief about the NEXT period is the conditional distribution F(·|θ_t), which
differs from π whenever the chain has persistence (α + β ≠ 1).

This is the fundamental issue: the paper's OT characterization assumes SR beliefs are
well-approximated by the stationary distribution ρ̃ on the lifted space, but in practice,
SR beliefs track F(·|θ_t) and never "forget" the last observation.

## Figures

![Belief Trajectory](figures/belief_trajectory.png)
![TV Distance](figures/tv_distance_timeseries.png)
