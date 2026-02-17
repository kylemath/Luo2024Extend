# SSA2_1: State-Revealing Strategy Simulation — Report

## Summary

When the LR player uses the commitment strategy s₁*(G)=A, s₁*(B)=F, the action at each
period reveals the state θ_t to the SR player. Therefore, the SR player's belief about
θ_{t+1} is the conditional distribution F(·|θ_t), NOT the stationary distribution π.

## Analytical Results

For a 2-state Markov chain with parameters (α, β):
- F(G|G) = 1 − α, F(G|B) = β
- π(G) = β/(α+β)
- Gap after state G: |F(G|G) − π(G)| = |(1−α) − β/(α+β)| = α·|1−α−β|/(α+β)
- Gap after state B: |F(G|B) − π(G)| = |β − β/(α+β)| = α·β/(α+β)
- Expected gap: π(G)·gap_G + π(B)·gap_B

## Numerical Results

| α | β | π(G) | F(G|G) | F(G|B) | Gap after G | Gap after B | Expected Gap | Empirical Mean Gap |
|---|---|------|--------|--------|-------------|-------------|--------------|-------------------|
| 0.3 | 0.5 | 0.6250 | 0.7000 | 0.5000 | 0.0750 | 0.1250 | 0.0937 | 0.0938 |
| 0.1 | 0.1 | 0.5000 | 0.9000 | 0.1000 | 0.4000 | 0.4000 | 0.4000 | 0.4000 |
| 0.05 | 0.05 | 0.5000 | 0.9500 | 0.0500 | 0.4500 | 0.4500 | 0.4500 | 0.4500 |
| 0.5 | 0.5 | 0.5000 | 0.5000 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Key Finding

**The belief gap is PERMANENT.** Under a state-revealing strategy:
- Every period, the SR player learns the current state exactly.
- Their belief about the next state is F(·|θ_t), not π.
- The gap |F(·|θ_t) − π| never shrinks because new observations always override
  any convergence toward π.
- This gap is zero ONLY when α + β = 1 (i.e., the chain is i.i.d.).

This directly contradicts the paper's implicit assumption that SR beliefs can be
characterized by the stationary distribution on the lifted state space.

## Figures

![Revealed Belief Trajectory](figures/revealed_belief_trajectory.png)
![Persistent Gap](figures/belief_gap_persistent.png)
