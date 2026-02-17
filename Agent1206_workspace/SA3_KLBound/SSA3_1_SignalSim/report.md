# SSA3_1: Signal Process Simulator — Report

## Setup
- **Markov chain**: 2-state with alpha=0.3 (G->B), beta=0.5 (B->G)
- **Stationary distribution**: pi(G)=0.625, pi(B)=0.375
- **Simulation length**: T=2000

## Signal Processes
- **Q (commitment type)**: Deterministic Stackelberg — A in state G, F in state B
- **P (confused type)**: Mixed — s(G)=0.7A+0.3F, s(B)=0.4A+0.6F

## Key Finding
Since the commitment type plays deterministically, each signal perfectly reveals the state.
The confused type plays mixed strategies, so signals only partially reveal the state.
This creates an information asymmetry that the KL bound quantifies.

## Signal Distribution Statistics
| Metric | Value |
|--------|-------|
| Mean TV(q_t, p_t) | 0.1004 |
| Mean D(q_t \|\| p_t) | 0.021824 |
| Cumulative KL at T=2000 | 43.6479 |

## Distinguishing Periods
| Threshold eta | Count | Fraction |
|---------------|-------|----------|
| 0.01 | 2000 | 1.000 |
| 0.05 | 1999 | 1.000 |
| 0.10 | 1256 | 0.628 |
| 0.20 | 0 | 0.000 |

## Figures
- ![Signal Distributions](figures/signal_distributions.png)
- ![TV Distance Preview](figures/tv_distance_preview.png)

## Notes
The q_t distribution for the commitment type fluctuates with the SR player's belief
about the state. When the filter has high confidence in G, q_t(A) is close to 1.
The p_t distribution is smoother because the mixed strategy blurs state information.
