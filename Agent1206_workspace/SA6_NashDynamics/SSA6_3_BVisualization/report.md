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
