# Report: SA6_NashDynamics (SA6_NashDynamics)

**Status:** completed
**Level:** Subagent
**Parent:** Agent1206
**Generated:** 2026-02-17T00:42:04.297717

## Task

# SA6: Nash Correspondence Dynamics

**Assigned to:** SA6_NashDynamics  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** MEDIUM-HIGH — tests whether B(s₁, μ₀) is effectively static

## Objective

Luo says "you need to write B(s₁, μ₀) as a function of player 2's belief about theta and also s₁... but this makes it impossible to get just deviations of the form we consider to work, since μ₀ will constantly be changing." Test this by computing the SR best response set as a function of beliefs.

## Sub-subagent Assignments

### SSA6_1_BestResponse
Compute SR player best response for each belief state in the deterrence game.

### SSA6_2_GameSim
Simulate the full game with belief-dependent SR responses and track how B(s₁, μ₀) moves.

### SSA6_3_BVisualization
Visualize the Nash correspondence as a function of SR beliefs.

## Deliverables
- `report.md` analyzing whether B(s₁, μ₀) varies substantively


## Sub-agent Reports

### SSA6_1_BestResponse

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


---

### SSA6_2_GameSim

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


---

### SSA6_3_BVisualization

# SSA6_3: Nash Correspondence Visualization — Report

## Setup
- Markov chain: α=0.3, β=0.5
- Stationary π(G) = 0.6250
- SR threshold: μ* = 0.6
- Simulation: T=5000

## Nash Correspondence B(s₁, μ)

The Nash correspondence maps beliefs to best responses:
- μ > 0.6: SR plays **C** (Cooperate)
- μ < 0.6: SR plays **D** (Defect)
- μ = 0.6: SR is indifferent (can mix)

## i.i.d. vs Markov Comparison

| Metric | i.i.d. | Markov |
|--------|--------|--------|
| Belief | Always π(G)=0.6250 | μ̄=0.6377 ± 0.4806 |
| Time in C | 100.0% | 63.8% |
| Time in D | 0.0% | 36.2% |
| BR changes | 0 | Frequent |

## Key Findings

1. Under i.i.d. states, the belief is a single point at π(G)=0.6250, which is in the C region. SR always cooperates.

2. Under Markov states, the filtered belief fluctuates substantially. SR spends 63.8% of time in the C region and 36.2% in the D region.

3. The belief distribution under Markov states has large variance (σ=0.4806), causing frequent BR threshold crossings. This is fundamentally different from the i.i.d. case.

4. **Implication for the paper**: The commitment payoff calculated using the stationary distribution assumes SR always cooperates (since π(G)>μ*). But with Bayesian filtering under Markov states, SR defects ~36% of the time, reducing LR's actual payoff.

## Figures
![Nash Correspondence](figures/nash_correspondence.png)

![Belief Histogram in BR Regions](figures/belief_histogram_in_BR_regions.png)


---
