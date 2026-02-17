# SA2: State-Revealing Strategy Counterexample

**Assigned to:** SA2_StateRevealing  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** HIGHEST — tests Luo's specific counterexample

## Objective

Daniel Luo's key example: "suppose s₁ just takes an action that reveals the state. In the iid case, this won't affect SR beliefs. But in the Markov case, this can cause beliefs to never settle into the stationary distribution."

NOTE: The paper's OWN deterrence Stackelberg strategy s₁*(G)=A, s₁*(B)=F IS state-revealing (each state maps to a unique action). So this critique applies directly to the worked example.

## Sub-subagent Assignments

### SSA2_1_RevealingSim
Simulate the deterrence game where s₁* reveals the state. Track what SR players learn: after observing action A, they know θ_t=G and can predict θ_{t+1} ~ F(·|G) = (1-α, α). Show this differs from π.

### SSA2_2_DivergenceAnalysis
Quantify HOW MUCH SR beliefs deviate from π when the strategy is state-revealing. Compute the belief trajectory and show it tracks F(·|θ_t) rather than π. This is the smoking gun.

### SSA2_3_Counterexample
Construct the full counterexample: show that using ρ̃ as the OT marginal gives a different OT solution than using the actual filtering distribution F(·|θ_t). If the solutions differ, confound-defeating at ρ̃ does NOT imply confound-defeating at the actual belief.

## Deliverables
- `report.md` with clear yes/no: does the state-revealing strategy break the paper's argument?
- Figures showing belief trajectories vs stationary distribution
- Quantitative measure of the gap
