# SSA2_1: State-Revealing Strategy Simulation

**Parent:** SA2_StateRevealing

## Task
Create `revealing_sim.py` that:
1. Simulate deterrence game with s₁*(G)=A, s₁*(B)=F (this reveals the state)
2. After observing action at time t, SR player knows θ_t exactly
3. SR player's belief about θ_{t+1} is therefore F(·|θ_t), NOT π
4. Track: |F(·|θ_t) − π| at each time step
5. For (α,β)=(0.3,0.5): F(G|G)=0.7, F(G|B)=0.5, π(G)=0.625
   So after seeing A (state G), SR believes Pr(G next) = 0.7, not 0.625 — a gap of 0.075
   After seeing F (state B), SR believes Pr(G next) = 0.5, not 0.625 — a gap of 0.125
6. These gaps NEVER shrink because every period reveals the state anew
7. Simulate T=5000 steps, plot the belief and the gap

## Deliverables
- `revealing_sim.py`
- `figures/revealed_belief_trajectory.png`
- `figures/belief_gap_persistent.png` 
- `report.md` documenting the persistent gap
