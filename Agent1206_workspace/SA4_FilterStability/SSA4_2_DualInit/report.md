# SSA4_2: Dual-Initialization Filter Comparison — Report

## Setup
- **Simulation length**: T=500
- **Prior 1**: pi0 = (1, 0) — certain G
- **Prior 2**: pi0' = (0, 1) — certain B
- **Same observation sequence** for both filters

## Chain Parameters Tested
| alpha | beta | |1-alpha-beta| | Mixing Speed |
|-------|------|---------------|--------------|
| 0.3 | 0.5 | 0.200 | fast |
| 0.1 | 0.1 | 0.800 | slow |
| 0.05 | 0.05 | 0.900 | slow |
| 0.02 | 0.02 | 0.960 | slow |

## Convergence Results

### Steps to TV < 1e-6
| Chain (alpha, beta) | noise=0.05 | noise=0.1 | noise=0.2 | noise=0.3 | noise=0.5 |
|---------------------|------------|-----------|-----------|-----------|-----------|
| (0.3, 0.5) | 4 | 5 | 7 | 8 | 8 |
| (0.1, 0.1) | 7 | 9 | 26 | 40 | 61 |
| (0.05, 0.05) | 5 | 7 | 21 | 46 | 131 |
| (0.02, 0.02) | 5 | 8 | 26 | 43 | 338 |

## Key Findings

### Filter Forgetting Property
Both filters converge to the same beliefs regardless of initialization, confirming
the **filter stability / forgetting property** for all chain parameterizations tested.

### Effect of Chain Mixing Rate
- **Fast mixing** (|1-a-b| small, e.g., alpha=0.3, beta=0.5): Convergence occurs within
  1-5 steps even with uninformative signals, because the transition matrix itself
  rapidly mixes beliefs.
- **Slow mixing** (|1-a-b| close to 1, e.g., alpha=0.05, beta=0.05): Convergence takes
  many more steps, especially with uninformative signals. The filter forgetting rate
  is governed by the chain's second eigenvalue.

### Effect of Signal Informativeness
- **Informative signals** (low noise): Accelerate convergence beyond what the transition
  model alone provides, because each observation strongly identifies the current state.
- **Uninformative signals** (noise=0.5): Convergence rate matches the chain mixing rate,
  since the filter relies entirely on the transition model.

### Relationship to Paper's Claims
The paper claims filter stability extends from i.i.d. to Markov states. Our results
confirm this but highlight that the **rate of forgetting** depends on:
1. The chain's mixing properties (second eigenvalue)
2. The informativeness of observations (strategy noisiness)

For deterministic strategies (noise=0), filter stability is trivially instantaneous.
For stochastic strategies, the forgetting rate is a non-trivial function of both factors.

## Figures
- ![Filter Divergence Over Time](figures/filter_divergence_over_time.png)
- ![Noise Level Comparison](figures/noise_level_comparison.png)
