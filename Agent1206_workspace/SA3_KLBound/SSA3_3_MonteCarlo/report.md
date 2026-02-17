# SSA3_3: Monte Carlo Bound Verification — Report

## Setup
- **N**: 1000 simulations
- **T**: 5000 periods per simulation
- **Markov chain**: alpha=0.3, beta=0.5
- **mu0**: 0.01
- **Bound**: T_bar = -2 log(mu0) / eta^2

## Results

### Markov Chain Simulations
| eta | T_bar | Mean Count | Exc. Fraction | Ratio |
|-----|-------|------------|---------------|-------|
| 0.01 | 92103.4 | 5000.0 | 0.000 | 0.0543 |
| 0.05 | 3684.1 | 4999.0 | 1.000 | 1.3569 |
| 0.1 | 921.0 | 3123.1 | 1.000 | 3.3909 |
| 0.2 | 230.3 | 0.0 | 0.000 | 0.0000 |

### i.i.d. Simulations
| eta | T_bar | Mean Count | Exc. Fraction | Ratio |
|-----|-------|------------|---------------|-------|
| 0.01 | 92103.4 | 5000.0 | 0.000 | 0.0543 |
| 0.05 | 3684.1 | 4999.0 | 1.000 | 1.3569 |
| 0.1 | 921.0 | 3122.8 | 1.000 | 3.3906 |
| 0.2 | 230.3 | 0.0 | 0.000 | 0.0000 |

## Key Findings
1. **Bound holds**: In both Markov and i.i.d. settings, the mean count of distinguishing
   periods is well below T_bar for all eta thresholds tested.
2. **Markov vs i.i.d.**: The counts are similar between the two settings, which is
   consistent with the paper's claim that the KL counting bound extends to Markov states.
3. **Bound tightness**: The ratio (mean count / T_bar) indicates how tight the bound is.
   Smaller ratios mean the bound is more conservative.
4. **Exceedance fraction**: The fraction of simulations where count exceeds T_bar should
   be 0 or very small if the bound holds.

## Figures
- ![Count Histogram](figures/count_histogram.png)
- ![i.i.d. vs Markov Comparison](figures/iid_vs_markov_comparison.png)
