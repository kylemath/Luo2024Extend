# SSA5_1: OT Problem Setup — Report

## Parameters
- Markov chain: α=0.3, β=0.5
- Stationary distribution π: G=0.6250, B=0.3750
- Deterrence game: x=0.3, y=0.4, supermodular=True

## OT Problem Formulation
- **State space**: Lifted Θ̃ = {(G,G), (G,B), (B,G), (B,B)}
- **Action space**: A₁ = {A, F}
- **State marginal** μ = ρ̃ (lifted stationary distribution)
- **Action marginal** ϕ: A=0.6250, F=0.3750
- **Objective**: maximise Σ γ[θ̃, a₁] · u₁(θ̃, a₁)

## Results
- **Optimal objective value**: 0.625000
- **Co-monotone objective value**: 0.625000
- **Max difference from co-monotone**: 0.00e+00
- **Matches co-monotone**: True

## Support of Optimal Coupling
- ((G,G), A)
- ((G,B), A)
- ((B,G), F)
- ((B,B), F)

## Interpretation
The OT solution at the stationary distribution ρ̃ matches the co-monotone coupling, which is expected for a supermodular game. The support assigns:
- All lifted states with θ_t = G → action A (Acquiesce)
- All lifted states with θ_t = B → action F (Fight)

This confirms the Stackelberg strategy is OT-optimal at ρ̃. The key question (addressed in SSA5_2) is whether this remains true when μ ≠ ρ̃.

## Figures
![OT Coupling Heatmap](figures/ot_coupling_stationary.png)
