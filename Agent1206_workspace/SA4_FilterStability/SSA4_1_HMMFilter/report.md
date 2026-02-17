# SSA4_1: HMM Filter Implementation — Report

## Setup
- **Markov chain**: alpha=0.3, beta=0.5
- **Stationary distribution**: pi(G)=0.625, pi(B)=0.375
- **Simulation length**: T=2000

## Filter Performance by Noise Level

| Noise Level | MAE | Mean Belief(G) | Std Belief(G) |
|-------------|-----|----------------|---------------|
| 0.00 | 0.0000 | 0.6280 | 0.4833 |
| 0.05 | 0.0955 | 0.6315 | 0.4318 |
| 0.10 | 0.1749 | 0.6320 | 0.3828 |
| 0.20 | 0.3011 | 0.6278 | 0.2872 |
| 0.30 | 0.3933 | 0.6295 | 0.1921 |
| 0.40 | 0.4465 | 0.6264 | 0.0965 |
| 0.50 | 0.4680 | 0.6250 | 0.0000 |

## Key Findings

### Deterministic Strategy (noise=0)
When the strategy is deterministic (A in G, F in B), each signal perfectly reveals
the current state. The filter collapses to a point mass after each observation.
**Filter stability is trivially satisfied** because there is no information to "forget" —
each period provides complete state knowledge.

### Noisy Strategy (noise > 0)
When the strategy is stochastic, signals only partially reveal the state. The filter
maintains non-degenerate beliefs that evolve smoothly. **This is where filter stability
becomes non-trivial** — the filter must combine prior beliefs (from the transition model)
with new noisy evidence.

### Uninformative Strategy (noise=0.5)
When noise = 0.5, signals are independent of the state (pure noise). The filter
relies entirely on the Markov transition structure. Beliefs converge toward the
stationary distribution and vary only due to the transition model predictions.

### Implication for the Paper
The paper's extension claims filter stability holds for Markov states. This is
**trivially true for deterministic strategies** (which the paper focuses on) but
**substantively important for stochastic strategies**. The critique may be pointing
out that the interesting case (stochastic strategies) deserves more attention.

## Figures
- ![Deterministic vs Noisy](figures/filter_deterministic_vs_noisy.png)
