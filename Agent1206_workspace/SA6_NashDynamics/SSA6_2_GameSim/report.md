# SSA6_2: Full Game Simulation — Report

## Setup
- Markov chain: α=0.3, β=0.5
- Game: x=0.3, y=0.4
- Periods: T=5000, Runs: 20
- LR strategy: Stackelberg (A in G, F in B)
- SR threshold: μ* = 0.6
- Stationary π(G) = 0.6250

## Two Scenarios

| Scenario | Description |
|----------|-------------|
| (a) Stationary | SR always believes μ = π(G) — paper's assumption |
| (b) Filtered | SR uses Bayesian filter on observed actions — reality |

## Key Results

| Metric | Value |
|--------|-------|
| LR avg payoff (stationary) | 0.6378 |
| LR avg payoff (filtered) | 0.5472 |
| Mean payoff difference | 0.0940 ± 0.0016 |
| Mean SR disagreement rate | 0.3772 ± 0.0075 |

## Analysis

The SR player's action differs between stationary and filtered scenarios in **37.7%** of periods on average. This means the paper's assumption (that SR always uses π) leads to incorrect SR actions a non-trivial fraction of the time.

The stationary assumption gives LR a higher average payoff by 0.0940, which suggests the paper's commitment payoff calculation is optimistic.

## Figures
![Payoff Comparison](figures/payoff_comparison.png)

![SR Action Disagreement](figures/sr_action_disagreement.png)
