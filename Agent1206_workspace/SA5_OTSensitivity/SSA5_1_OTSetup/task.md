# SSA5_1: OT Problem Setup

**Parent:** SA5_OTSensitivity

## Task
Create `ot_setup.py` that:
1. Define the OT problem for the deterrence game:
   - State space: lifted Θ̃ = {(G,G), (G,B), (B,G), (B,B)} (4 states)
   - Action space: A₁ = {A, F} (2 actions)
   - Joint distribution: γ ∈ R^{4×2}, γ[θ̃, a₁] ≥ 0
   - Marginal constraint 1: ∑_{a₁} γ[θ̃, a₁] = μ(θ̃) for each θ̃
   - Marginal constraint 2: ∑_{θ̃} γ[θ̃, a₁] = ϕ(a₁) for each a₁
   - Objective: max ∑ γ[θ̃, a₁] · u₁(θ̃, a₁)
2. Implement as a linear program using scipy.optimize.linprog
3. Solve at μ = ρ̃ with the Stackelberg strategy's action marginal ϕ
4. Verify the solution matches the co-monotone coupling (since the game is supermodular)
5. Output the optimal coupling and its support

## Deliverables
- `ot_setup.py`
- `figures/ot_coupling_stationary.png` — heatmap of optimal coupling at ρ̃
- `report.md` documenting the OT problem formulation and solution
