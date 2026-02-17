# SSA6_2: Full Game Simulation with Belief-Dependent SR Responses

**Parent:** SA6_NashDynamics

## Task
Create `game_sim.py` that:
1. Simulate the deterrence game over T=5000 periods:
   - State θ_t follows Markov chain (α=0.3, β=0.5)
   - LR player plays commitment strategy s₁*(G)=A, s₁*(B)=F
   - SR player observes action, updates belief about θ_t, and best-responds
2. Track: SR belief μ_t, SR action a₂_t, LR payoff u₁_t at each period
3. Compare two scenarios:
   - (a) SR uses STATIONARY belief (always π) — this is what the paper assumes
   - (b) SR uses FILTERED belief (Bayesian update from history) — this is reality
4. Compute: difference in LR average payoff between (a) and (b)
5. This difference measures how much the paper's assumption costs

## Key Question
Does using the filtered belief instead of the stationary belief change the SR player's actions? If the actions differ, it matters for the commitment payoff calculation.

## Deliverables
- `game_sim.py`
- `figures/payoff_comparison.png` — LR payoff under stationary vs filtered beliefs
- `figures/sr_action_disagreement.png` — fraction of periods where SR action differs
- `report.md` with comparative analysis
