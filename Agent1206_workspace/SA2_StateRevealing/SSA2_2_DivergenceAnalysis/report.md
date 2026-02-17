# SSA2_2: Divergence Analysis — Report

## Summary

Analytical and numerical study of the permanent belief gap that arises under state-revealing
strategies in the Markov deterrence game.

## Analytical Formulas

For a 2-state Markov chain with Pr(B|G) = α and Pr(G|B) = β:

- **Stationary distribution**: π(G) = β/(α+β)
- **Belief after observing state G**: F(G|G) = 1 − α
- **Belief after observing state B**: F(G|B) = β
- **Gap after G**: |F(G|G) − π(G)| = α·|1−α−β| / (α+β)
- **Gap after B**: |F(G|B) − π(G)| = β·|1−α−β| / (α+β)
- **Expected gap**: π(G)·gap_G + π(B)·gap_B = 2αβ|1−α−β| / (α+β)²

## When is the Gap Zero?

Both gap_G and gap_B share the factor |1−α−β|, so:
- gap_G = 0 ⟺ α = 0 or |1−α−β| = 0
- gap_B = 0 ⟺ β = 0 or |1−α−β| = 0

For non-degenerate chains (α,β > 0), the gap is zero **if and only if α + β = 1** (the i.i.d. case).
The expected gap = 2αβ|1−α−β|/(α+β)² is zero iff |1−α−β| = 0, confirming this.

## Numerical Verification

- Maximum analytical-simulation discrepancy: 0.000000
- Gap at α = β = 0.5 (i.i.d.): 0.004949 (should be ≈ 0)
- Maximum gap along α = β diagonal: 0.4900 at α = β = 0.010

## Selected Parameter Values

| α | β | π(G) | Gap after G | Gap after B | Expected Gap |
|---|---|------|-------------|-------------|--------------|
| 0.1 | 0.1 | 0.5000 | 0.4000 | 0.4000 | 0.4000 |
| 0.3 | 0.5 | 0.6250 | 0.0750 | 0.1250 | 0.0937 |
| 0.5 | 0.5 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.9 | 0.9000 | 0.0000 | 0.0000 | 0.0000 |
| 0.05 | 0.05 | 0.5000 | 0.4500 | 0.4500 | 0.4500 |

## Key Finding

**The belief gap is zero if and only if the Markov chain is i.i.d. (α + β = 1).**

For ANY persistent chain (α + β ≠ 1), there exists a permanent, non-vanishing discrepancy
between what the SR player actually believes (based on last observation) and the stationary
distribution π. This gap cannot be eliminated by longer time horizons or more observations.

This is a fundamental structural property of the observation process, not a convergence issue.

## Figures

![Belief Gap Heatmap](figures/belief_gap_heatmap.png)
![Gap vs Persistence](figures/gap_vs_persistence.png)

## Implication for the Paper

The paper's OT characterization relies on the lifted stationary distribution ρ̃ as if it
represents the SR player's effective belief distribution. But the actual per-period belief
is F(·|θ_t), which differs from the marginal of ρ̃ by the gap computed here. This means
confound-defeating at ρ̃ does not imply confound-defeating at the actual belief distribution,
invalidating the paper's main extension from i.i.d. to Markov states.
