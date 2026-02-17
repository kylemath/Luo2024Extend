# SSA4_2: Dual-Initialization Filter Comparison

**Parent:** SA4_FilterStability

## Task
Create `dual_init.py` that:
1. Generate one long state + observation sequence (T=5000)
2. Run HMM filter from π₀ = (1,0) — certain G
3. Run HMM filter from π₀' = (0,1) — certain B  
4. SAME observation sequence for both
5. Track ‖π_t − π_t'‖ at each time step
6. Test with NOISY strategy (s₁(G) = 0.8A+0.2F, s₁(B) = 0.2A+0.8F) since deterministic strategy makes filtering trivial
7. Also test with very noisy strategy (0.6/0.4) and barely noisy (0.95/0.05)
8. For each noise level, check if ‖π_t − π_t'‖ → 0

## Deliverables
- `dual_init.py`
- `figures/filter_divergence_over_time.png` — log-scale TV distance vs t
- `figures/noise_level_comparison.png` — convergence rate vs noise level
- `report.md` with convergence analysis
