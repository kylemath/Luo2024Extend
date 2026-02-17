# SA1: Short-Run Player Belief Dynamics Under Markov States

**Assigned to:** SA1_SRBeliefs  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** HIGHEST — this addresses the fatal flaw identified by Daniel Luo

## Objective

Test whether SR player beliefs about θ_t remain close to the stationary distribution π or persistently deviate when states are Markov. This is the central empirical question: if beliefs are history-dependent in a non-vanishing way, the paper's reliance on ρ̃ as the OT marginal is fundamentally wrong.

## Sub-subagent Assignments

### SSA1_1_MarkovSim
Create the core Markov chain simulator. Generate long state sequences for various (α, β) parameters. Validate against theoretical stationary distribution.

### SSA1_2_BayesFilter  
Implement Bayesian filtering: given a commitment strategy s₁*(G)=A, s₁*(B)=F and observed signals, track the SR player's posterior belief about θ_t. Compare to the stationary distribution. Compute TV distance ‖posterior(θ_t | h_t) − π‖ at each time step.

### SSA1_3_BeliefViz
Produce publication-quality figures showing belief trajectories, TV distance over time, and distribution of TV distances across many simulations. Generate summary statistics.

## Deliverables
- `report.md` synthesizing all sub-subagent findings
- Figures in `figures/` directory
- Key statistic: mean and max TV distance between SR posterior and π over T=10,000 periods
