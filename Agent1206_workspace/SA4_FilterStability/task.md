# SA4: HMM Filter Stability Verification

**Assigned to:** SA4_FilterStability  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** HIGH — paper's Proposition A.2 claims exponential forgetting

## Objective

Verify that the HMM filter (SR player's posterior about θ_t given history) "forgets" its initial condition exponentially fast. This is claimed in the paper's Appendix (filter stability) and is critical for the martingale convergence argument in Lemma 3.

## Sub-subagent Assignments

### SSA4_1_HMMFilter
Implement HMM filtering from arbitrary initial conditions. This is the Bayesian filter but starting from non-stationary priors.

### SSA4_2_DualInit
Run HMM filtering from two extreme initial conditions (π₀=(1,0) and π₀'=(0,1)) on the SAME observation sequence. Track ‖π_t − π_t'‖ over time.

### SSA4_3_DecayFit
Fit exponential decay model C·λ^t to the filter divergence. Vary (α,β) and characterize how λ depends on chain parameters.

## Deliverables
- `report.md` confirming or refuting filter stability
- Figures showing exponential decay with fitted parameters
