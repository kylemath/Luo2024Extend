# SSA6_3: Nash Correspondence Visualization

**Parent:** SA6_NashDynamics

## Task
Create `b_visualization.py` that:
1. Plot the Nash correspondence B(s₁, μ) as a function of μ ∈ [0,1]
2. For the deterrence game:
   - At each μ, compute the set of SR best responses (pure and mixed)
   - Plot the best response regions with belief thresholds
3. Overlay: the TIME SERIES of μ(h_t) from a simulation on the same plot
   - Show how the belief moves around and crosses BR boundaries
4. Compute: fraction of time the belief is in each BR region
5. Compare for i.i.d. (μ always equals π — single point) vs Markov (μ fluctuates)
6. Create animation-style panel: snapshots at t=10, 100, 500, 2000

## Deliverables
- `b_visualization.py`
- `figures/nash_correspondence.png` — B(s₁, μ) with trajectory overlay
- `figures/belief_histogram_in_BR_regions.png`
- `report.md` with interpretation
