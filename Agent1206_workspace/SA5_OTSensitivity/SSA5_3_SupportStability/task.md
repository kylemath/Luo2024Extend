# SSA5_3: Support Stability Analysis

**Parent:** SA5_OTSensitivity

## Task
Create `support_stability.py` that:
1. Take the results from SSA5_2 and analyze support stability
2. For the deterrence game (supermodular, 2 states × 2 actions):
   - The co-monotone coupling has support {(G,*,A), (B,*,F)} — both lifted states with θ_t=G map to A, both with θ_t=B map to F
   - Under perturbation, does ANY (θ̃, a₁) pair enter or leave the support?
3. Visualize: for each (θ̃, a₁) pair, plot γ[θ̃, a₁] as function of ε
4. For the FULL 2D analysis: sweep (α, β) and for each, compute the stability margin (how much perturbation before support changes)
5. Create a phase diagram: regions of (α, β) space where the OT solution is robust vs fragile

## Deliverables
- `support_stability.py`
- `figures/coupling_weights_vs_epsilon.png`
- `figures/stability_margin_heatmap.png` — stability margin over (α,β)
- `report.md` with conclusions about OT robustness
