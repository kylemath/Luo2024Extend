# SSA6_1: SR Player Best Response — Report

## SR Payoff Structure

| State | Action C | Action D |
|-------|----------|----------|
| G     | 1.0      | 0.0      |
| B     | -1.0     | 0.5      |

## Expected Payoffs

- E[u₂(C)] = μ·1 + (1−μ)·(−1) = **2μ − 1**
- E[u₂(D)] = μ·0 + (1−μ)·0.5 = **0.5(1−μ)**

## Best Response Threshold

SR plays C iff 2μ−1 > 0.5(1−μ) ⟺ **μ > μ* = 0.6**

## Simulation Results

- Periods: 5000
- Threshold crossings: 1812
- Crossing rate: 0.3624/period
- Time in C region: 63.8%
- Time in D region: 36.2%
- Mean belief: 0.6377
- Stationary π(G): 0.6250

## Interpretation

The SR best-response threshold μ*=0.6 lies below the stationary belief π(G)=0.6250. This means that at stationarity, SR would cooperate (play C). However, with Bayesian filtering, the belief μ_t fluctuates around π(G) and crosses the threshold 1812 times in 5000 periods. Each crossing changes SR's action, which affects LR's actual payoff.

This confirms that the filtering distribution matters: even when the stationary belief is in one BR region, the actual beliefs can cross into the other.

## Figures
![Best Response vs Belief](figures/best_response_vs_belief.png)

![Threshold Crossings](figures/threshold_crossings.png)
