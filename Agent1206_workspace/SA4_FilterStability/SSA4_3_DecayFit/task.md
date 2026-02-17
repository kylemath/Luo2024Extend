# SSA4_3: Exponential Decay Fitting

**Parent:** SA4_FilterStability

## Task
Create `decay_fit.py` that:
1. For each (α,β) ∈ grid and each noise level:
   - Run dual-init filter comparison (N=100 simulations)
   - Compute mean ‖π_t − π_t'‖ across simulations at each t
2. Fit model: log(‖π_t − π_t'‖) = log(C) + t·log(λ) via linear regression
3. Extract: C (initial constant) and λ (forgetting rate)
4. Plot: λ as function of (α,β) — heatmap
5. Plot: λ as function of noise level
6. Compare to theoretical bound: for full-support observations, λ should be related to the second-largest eigenvalue of the transition matrix

## Theory Check
For a 2-state chain with transition matrix T, eigenvalues are 1 and (1−α−β). The second eigenvalue |1−α−β| governs mixing time. Does the fitted λ match |1−α−β|?

## Deliverables
- `decay_fit.py`
- `figures/forgetting_rate_heatmap.png` — λ vs (α,β)
- `figures/lambda_vs_theory.png` — fitted λ vs |1−α−β|
- `report.md` with fitted parameters and comparison to theory
