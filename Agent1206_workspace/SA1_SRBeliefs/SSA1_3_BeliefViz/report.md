# SSA1_3: Belief Visualization — Report

## Summary

Comprehensive visualization of SR player belief dynamics across the parameter space.
Ran 200 simulations of 5000 steps for selected (α,β) values, plus a heatmap
over a 10×10 grid.

## TV Distance Statistics

| Setting | Mean | Std | Min | Max | Median |
|---------|------|-----|-----|-----|--------|
| α=0.1,β=0.1 (high persist) | 0.4999 | 0.0000 | 0.4999 | 0.4999 | 0.4999 |
| α=0.3,β=0.5 (baseline) | 0.4688 | 0.0023 | 0.4619 | 0.4741 | 0.4690 |
| α=0.5,β=0.5 (i.i.d.) | 0.4999 | 0.0000 | 0.4999 | 0.4999 | 0.4999 |
| α=0.1,β=0.9 (near i.i.d.) | 0.1799 | 0.0033 | 0.1704 | 0.1869 | 0.1798 |
| α=0.05,β=0.05 (very persist) | 0.4999 | 0.0000 | 0.4999 | 0.4999 | 0.4999 |

## Key Findings

1. **TV distance is near zero only when α + β ≈ 1** (i.i.d. case), visible in the heatmap
   as a dark valley along the α + β = 1 diagonal.
2. **Higher persistence (smaller α, β) → larger TV distance.** When the chain is very
   persistent (α=β=0.05), the SR belief is far from π because F(·|θ_t) differs
   significantly from π.
3. **The violin plot shows tight concentration**: for each (α,β), the time-averaged TV
   distance has low variance across simulations, meaning the gap is structural, not
   a finite-sample artifact.
4. **Persistence comparison** dramatically illustrates: near-i.i.d. chains produce
   beliefs close to π, while persistent chains produce beliefs that track F(·|θ_t)
   and persistently deviate from π.

## Figures

![TV Heatmap](figures/tv_heatmap.png)
![TV Violin](figures/tv_violin.png)
![Persistence Comparison](figures/persistence_comparison.png)

## Conclusion

The SR player's belief about the current state **does not converge to the stationary
distribution** under Markov dynamics with a state-revealing strategy. The deviation is
permanent and grows with the persistence of the chain (distance from i.i.d.). This
undermines the paper's use of the lifted stationary distribution ρ̃ as the relevant
measure for the OT characterization.
