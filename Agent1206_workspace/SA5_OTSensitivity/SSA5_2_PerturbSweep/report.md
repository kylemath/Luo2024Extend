# SSA5_2: Marginal Perturbation Sweep — Report

## Parameters
- Markov chain: α=0.3, β=0.5
- Game: x=0.3, y=0.4, supermodular=True
- Perturbation range: ε ∈ [0, 0.30], step=0.01

## Perturbation Directions
- **More persistent good**: [ 0.5  0.   0.  -0.5]
- **More transitions**: [-0.25  0.25  0.25 -0.25]
- **Toward F(·|G)**: [ 0.35  0.15 -0.25 -0.25]
- **Toward F(·|B)**: [-0.35 -0.15  0.25  0.25]

## Results Summary

| Direction | Critical ε* | Objective Range | Status |
|-----------|------------|-----------------|--------|
| More persistent good | N/A | [0.6250, 0.7750] | Stable |
| More transitions | N/A | [0.6250, 0.6250] | Stable |
| Toward F(·|G) | N/A | [0.6250, 0.7750] | Stable |
| Toward F(·|B) | N/A | [0.4750, 0.6250] | Stable |

## Key Findings

- **Toward F(·|G)**: OT support remains STABLE across all tested ε. The OT solution is robust to this perturbation.
- **Toward F(·|B)**: OT support remains STABLE across all tested ε. The OT solution is robust to this perturbation.

## Interpretation

The game-relevant perturbation directions (Toward F(·|G) and Toward F(·|B)) represent the actual belief distributions that SR players condition on after observing specific states. If the OT support changes under these perturbations, it validates the critique that checking OT only at ρ̃ is insufficient.

## Figures
![OT Objective vs Epsilon](figures/ot_objective_vs_epsilon.png)

![Support Change Threshold](figures/support_change_threshold.png)
