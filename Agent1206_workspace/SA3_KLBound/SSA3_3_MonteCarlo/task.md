# SSA3_3: Monte Carlo Bound Verification

**Parent:** SA3_KLBound

## Task
Create `monte_carlo.py` that:
1. Run N=1000 simulations of T=5000 periods each
2. For each simulation, count distinguishing periods for each η
3. Compare empirical distribution of #{distinguishing periods} to theoretical T̄ = −2 log(μ₀)/η²
4. Compute: fraction of simulations where count exceeds T̄ (should be 0 if bound holds)
5. Plot: histogram of counts with T̄ marked as vertical line
6. Separate analysis for i.i.d. chain vs Markov chain — do they differ?
7. Assess bound tightness: ratio of mean empirical count to T̄

## Deliverables
- `monte_carlo.py`
- `figures/count_histogram.png` — histogram with bound line
- `figures/iid_vs_markov_comparison.png` — side-by-side comparison
- `report.md` with bound verification statistics
