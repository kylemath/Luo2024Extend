# SSA4_1: HMM Filter Implementation

**Parent:** SA4_FilterStability

## Task
Create `hmm_filter.py` that:
1. Implements forward filtering for a 2-state HMM
2. Transition model: Markov chain with kernel F
3. Observation model: signal y_t depends on (θ_t, a_{1,t}) where a_{1,t} = s₁*(θ_t)
4. Since s₁* is deterministic and state-revealing, y_t = a_{1,t} perfectly reveals θ_t
5. Also implement a NOISY version where s₁ is stochastic: s₁(G) = 0.8A+0.2F, s₁(B) = 0.2A+0.8F
6. Compare: how does noise level affect filter convergence?
7. For the noisy case, the filter is non-trivial. For the deterministic case, the filter collapses to a point mass each period (no forgetting needed because each observation resets beliefs).

## Important Subtlety
When the strategy is deterministic and state-revealing, the filter is trivial (perfect state knowledge each period). Filter stability matters MORE when the strategy is stochastic and partially revealing. Test both.

## Deliverables
- `hmm_filter.py` 
- `figures/filter_deterministic_vs_noisy.png`
- `report.md` documenting both cases
