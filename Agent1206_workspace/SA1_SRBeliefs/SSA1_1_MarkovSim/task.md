# SSA1_1: Markov Chain Simulator

**Parent:** SA1_SRBeliefs

## Task
Create `markov_sim.py` that:
1. Uses `shared/markov_utils.py` MarkovChain class
2. Simulates state sequences for parameter grids: α ∈ {0.1, 0.3, 0.5}, β ∈ {0.1, 0.3, 0.5}
3. For each (α,β), runs N=500 simulations of T=5000 steps
4. Computes empirical state frequencies and compares to theoretical π
5. Computes empirical transition frequencies and compares to theoretical T
6. Saves validation stats to `figures/validation_stats.png`

## Deliverables
- `markov_sim.py` — self-contained, runnable script
- `figures/validation_stats.png` — heatmap of (empirical − theoretical) frequencies
- `report.md` — summary of validation results
