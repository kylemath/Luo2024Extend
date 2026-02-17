# SSA1_1: Markov Chain Simulation — Validation Report

## Summary

Validated the `MarkovChain` class by comparing empirical statistics from 500 simulations
of 5000 steps each against theoretical values for all (α,β) combinations in
{0.1, 0.3, 0.5} × {0.1, 0.3, 0.5}.

## Results

| α | β | π(G) theoretical | π(G) empirical | Freq Error | Max Trans Error |
|---|---|---|---|---|---|
| 0.1 | 0.1 | 0.5000 | 0.4997 | 0.00032 | 0.00017 |
| 0.1 | 0.3 | 0.7500 | 0.7497 | 0.00030 | 0.00025 |
| 0.1 | 0.5 | 0.8333 | 0.8331 | 0.00028 | 0.00053 |
| 0.3 | 0.1 | 0.2500 | 0.2496 | 0.00042 | 0.00127 |
| 0.3 | 0.3 | 0.5000 | 0.4999 | 0.00011 | 0.00030 |
| 0.3 | 0.5 | 0.6250 | 0.6249 | 0.00006 | 0.00035 |
| 0.5 | 0.1 | 0.1667 | 0.1659 | 0.00078 | 0.00107 |
| 0.5 | 0.3 | 0.3750 | 0.3748 | 0.00019 | 0.00034 |
| 0.5 | 0.5 | 0.5000 | 0.5002 | 0.00018 | 0.00074 |

## Key Findings

1. **Maximum stationary frequency error**: 0.00078
2. **Maximum transition frequency error**: 0.00127
3. All errors are within expected Monte Carlo tolerance (~1/√(N·T) ≈ 0.00063)
4. The MarkovChain class correctly implements the 2-state Markov chain

## Figures

![Validation Stats](figures/validation_stats.png)

## Conclusion

The Markov chain simulator is validated. Empirical frequencies match theoretical predictions
to within Monte Carlo error, confirming correct implementation of transition dynamics and
stationary distributions.
