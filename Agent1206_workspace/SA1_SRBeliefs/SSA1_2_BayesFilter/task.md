# SSA1_2: Bayesian Filter for SR Player Beliefs

**Parent:** SA1_SRBeliefs

## Task
Create `bayes_filter.py` that:
1. Uses `shared/markov_utils.py` BayesianFilter class
2. Simulates the deterrence game with commitment strategy s₁*(G)=A, s₁*(B)=F
3. At each time step, the SR player observes the action (= signal) and updates beliefs about θ_t
4. Key: the SR player KNOWS the strategy s₁* (they're testing whether LR is commitment type)
5. Track: belief_t = Pr(θ_t = G | h_t) at each t
6. Compare to: (a) stationary π(G), (b) true state θ_t, (c) conditional F(·|θ_{t-1})
7. Compute TV distance ‖belief_t − π‖ over T=10,000 periods
8. Run for (α,β) = (0.3, 0.5) [baseline] and (0.1, 0.1) [high persistence]

## Key Question
Does ‖belief_t − π‖ converge to 0, stay bounded away, or fluctuate?
If it stays nonzero, the paper's OT characterization using ρ̃ is wrong for this game.

## Deliverables
- `bayes_filter.py`
- `figures/belief_trajectory.png` — belief vs time with π marked
- `figures/tv_distance_timeseries.png` — TV distance over time  
- `report.md` with findings and key statistics
