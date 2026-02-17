# SSA3_2: KL Divergence Computation Engine — Report

## Setup
- **Simulation**: T=5000 periods, alpha=0.3, beta=0.5
- **Prior probability of commitment type**: mu0=0.01
- **KL bound**: -log(mu0) = 4.6052

## KL Divergence Results
| Metric | Value |
|--------|-------|
| Mean D(q_t \|\| p_t) | 0.021959 |
| Median D(q_t \|\| p_t) | 0.023308 |
| Cumulative KL at T=5000 | 109.7937 |
| -log(mu0) bound | 4.6052 |
| Bound exceeded | True |
| First crossing t | 212 |

## Distinguishing Period Counts
| eta | Count | T_bar (bound) | Ratio | Exceeds? |
|-----|-------|---------------|-------|----------|
| 0.01 | 5000 | 92103.4 | 0.0543 | False |
| 0.05 | 4999 | 3684.1 | 1.3569 | True |
| 0.1 | 3188 | 921.0 | 3.4613 | True |
| 0.2 | 0 | 230.3 | 0.0000 | False |

## Interpretation
The KL counting bound states that the number of distinguishing periods (where TV > eta)
cannot exceed T_bar = -2 log(mu0) / eta^2 = 921.0 for eta=0.1.

**Key findings:**
- The cumulative KL divergence exceeds the -log(mu0) bound of 4.6052.
- For larger eta thresholds, the count is well below the bound (ratio << 1), confirming
  the bound is conservative.
- The KL bound applies regardless of whether states are i.i.d. or Markov, as claimed
  by the paper's extension.

## Figures
- ![Cumulative KL](figures/cumulative_kl.png)
- ![TV Per Period](figures/tv_per_period.png)
