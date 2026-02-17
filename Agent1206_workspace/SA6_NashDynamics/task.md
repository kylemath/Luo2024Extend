# SA6: Nash Correspondence Dynamics

**Assigned to:** SA6_NashDynamics  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** MEDIUM-HIGH — tests whether B(s₁, μ₀) is effectively static

## Objective

Luo says "you need to write B(s₁, μ₀) as a function of player 2's belief about theta and also s₁... but this makes it impossible to get just deviations of the form we consider to work, since μ₀ will constantly be changing." Test this by computing the SR best response set as a function of beliefs.

## Sub-subagent Assignments

### SSA6_1_BestResponse
Compute SR player best response for each belief state in the deterrence game.

### SSA6_2_GameSim
Simulate the full game with belief-dependent SR responses and track how B(s₁, μ₀) moves.

### SSA6_3_BVisualization
Visualize the Nash correspondence as a function of SR beliefs.

## Deliverables
- `report.md` analyzing whether B(s₁, μ₀) varies substantively
