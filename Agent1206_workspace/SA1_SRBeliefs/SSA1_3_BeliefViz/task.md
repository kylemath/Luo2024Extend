# SSA1_3: Belief Visualization and Summary Statistics

**Parent:** SA1_SRBeliefs

## Task
Create `belief_viz.py` that:
1. Runs the full SR belief simulation for multiple (α,β) parameter values
2. Across N=200 simulations of T=5000 steps each:
   - Compute distribution of TV distances at each time step
   - Compute time-averaged TV distance per simulation
   - Compare mean TV distance across (α,β) values
3. Generate publication-quality figures:
   - Heatmap: mean TV distance as function of (α, β)
   - Violin plot: distribution of time-averaged TV distances  
   - Comparison panel: low persistence vs high persistence belief trajectories

## Deliverables
- `belief_viz.py`
- `figures/tv_heatmap.png`
- `figures/tv_violin.png`
- `figures/persistence_comparison.png`
- `report.md` with summary statistics table and interpretation
