# SSA7_1: Multi-State Game Setup — Report

## Base Game
- **States:** Θ = {L, M, H} with order L < M < H
- **Actions:** A₁ = {l, m, h} with order l < m < h
- **Payoff:** u₁(θ, a) = 1.5 · θ · a  (θ, a ∈ {0, 1, 2})
- **Supermodular:** True

### Payoff Matrix
| | l | m | h |
|---|---|---|---|
| L | 0.0 | 0.0 | 0.0 |
| M | 0.0 | 1.5 | 3.0 |
| H | 0.0 | 3.0 | 6.0 |

## Markov Chain
- **Persistence parameter:** α_stay = 0.6
- **Stationary distribution:** π = [0.2857, 0.4286, 0.2857]

## Lifted State Space
- **Θ̃ = Θ × Θ:** 9 states
- **States:** (L,L), (L,M), (L,H), (M,L), (M,M), (M,H), (H,L), (H,M), (H,H)

### Lifted Stationary Distribution
| State | ρ̃ |
|---|---|
| (L,L) | 0.171429 |
| (L,M) | 0.085714 |
| (L,H) | 0.028571 |
| (M,L) | 0.085714 |
| (M,M) | 0.257143 |
| (M,H) | 0.085714 |
| (H,L) | 0.028571 |
| (H,M) | 0.085714 |
| (H,H) | 0.171429 |

## Payoff Variants
1. **θ_t-only payoff:** u₁(θ̃, a) = 1.5 · θ_t · a (ignores θ_{t-1})
2. **Transition-dependent:** u₁(θ̃, a) = 1.5 · θ_t · a + 0.5 · (θ_t − θ_{t-1}) · a

## Figures
![Payoff Matrices](figures/payoff_matrices.png)
![Stationary Distributions](figures/stationary_distributions.png)
![Transition Matrix](figures/transition_matrix.png)

## Key Observations
- The base game is supermodular with increasing differences.
- The lifted state space has 9 states, making exhaustive order enumeration feasible (9! = 362,880).
- The θ_t-only payoff preserves the base game's structure for states grouped by θ_t.
- The transition-dependent payoff introduces interactions between θ_t and θ_{t-1}.
- These structures will be tested for supermodularity under various orders in SSA7_2.