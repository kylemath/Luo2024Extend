# SA5: Optimal Transport Solution Sensitivity

**Assigned to:** SA5_OTSensitivity  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** HIGH — tests whether confound-defeating is robust to belief perturbations

## Objective

The paper's confound-defeating condition is checked at the stationary distribution ρ̃. But the actual per-period marginal is the filtering distribution π(θ̃_t | h_t), which differs from ρ̃. Test whether the OT solution is stable under these perturbations.

## Sub-subagent Assignments

### SSA5_1_OTSetup
Set up the OT problem for the deterrence game on the lifted state space using scipy.optimize.linprog.

### SSA5_2_PerturbSweep
Solve OT for a systematic sweep of marginal perturbations away from ρ̃.

### SSA5_3_SupportStability
Analyze the support of the OT solution: does it change under perturbation? At what perturbation size does it change?

## Deliverables
- `report.md` with stability analysis
- Figures showing OT solution robustness
