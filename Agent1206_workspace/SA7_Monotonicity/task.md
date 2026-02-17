# SA7: Monotonicity in Higher-Dimensional Lifted Space

**Assigned to:** SA7_Monotonicity  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** MEDIUM — tests whether supermodular characterization extends

## Objective

Luo says "our definition of monotonicity only works for one dimensional states and actions, which the 'lifting' technique here obviates." Test whether the monotonicity/supermodularity characterization survives the lifting to θ̃ = (θ_t, θ_{t-1}).

## Sub-subagent Assignments

### SSA7_1_GameSetup
Define a 3-state, 3-action game where supermodularity holds in (θ, a₁) but may fail in the lifted space.

### SSA7_2_SupermodCheck
Systematically check supermodularity of payoffs under various orderings of the lifted state space.

### SSA7_3_OTOrders
For each valid ordering, solve the OT problem and verify whether the co-monotone coupling is optimal.

## Deliverables
- `report.md` with clear answer: does monotonicity extend to the lifted space?
