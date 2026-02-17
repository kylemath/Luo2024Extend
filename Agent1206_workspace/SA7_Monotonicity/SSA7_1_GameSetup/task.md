# SSA7_1: Multi-State Game Setup

**Parent:** SA7_Monotonicity

## Task
Create `game_setup.py` that:
1. Define a 3-state game: Θ = {L, M, H} (Low, Medium, High) with order L < M < H
2. Actions: A₁ = {l, m, h} with order l < m < h
3. Supermodular payoff: u₁(θ, a₁) with increasing differences
   Example: u₁(θ, a) = θ·a + 0.5·θ·a (so u₁(i,j) = i*j + 0.5*i*j for i,j ∈ {0,1,2})
4. Markov chain on {L,M,H}: transition matrix with α parameters
5. Lifted state space: Θ̃ = Θ × Θ has 9 states
6. Lifted stationary distribution ρ̃
7. Output: all matrices and distributions needed for OT analysis

## Deliverables
- `game_setup.py`
- `report.md` describing the game and lifted state space
