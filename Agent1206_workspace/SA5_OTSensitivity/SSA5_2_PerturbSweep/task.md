# SSA5_2: Marginal Perturbation Sweep

**Parent:** SA5_OTSensitivity

## Task
Create `perturb_sweep.py` that:
1. Starting from ρ̃, create parameterized perturbations:
   - Direction 1: increase weight on (G,G), decrease on (B,B) — "more persistent good"
   - Direction 2: increase weight on (G,B)+(B,G), decrease on diagonal — "more transitions"
   - Direction 3: toward F(·|G) marginal — what SR sees after state G revealed
   - Direction 4: toward F(·|B) marginal — what SR sees after state B revealed
2. For each direction, sweep ε from 0 to 0.3 in steps of 0.01
3. At each ε, solve the OT problem with perturbed marginal (1-ε)ρ̃ + ε·δ_direction
4. Record: (a) optimal coupling, (b) support of coupling, (c) objective value
5. Identify: critical ε* where the support changes (if it does)

## Key Question
For the GAME-RELEVANT perturbations (directions 3 and 4 — what SR actually sees after state revelation), does the OT support change?

## Deliverables
- `perturb_sweep.py`
- `figures/ot_objective_vs_epsilon.png` — for each direction
- `figures/support_change_threshold.png` — critical ε* per direction
- `report.md` with sweep results and analysis
