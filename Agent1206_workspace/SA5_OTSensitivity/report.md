# Report: SA5_OTSensitivity (SA5_OTSensitivity)

**Status:** completed
**Level:** Subagent
**Parent:** Agent1206
**Generated:** 2026-02-17T00:42:04.297568

## Task

# SA5: Optimal Transport Solution Sensitivity

**Assigned to:** SA5_OTSensitivity  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** HIGH — tests whether confound-defeating is robust to belief perturbations

## Objective

The paper's confound-defeating condition is checked at the stationary distribution ρ̃. But the actual per-period marginal is the filtering distribution π(θ̃_t | h_t), which differs from ρ̃. Test whether the OT solution is stable under these perturbations.

## Sub-subagent Assignments

### SSA5_1_OTSetup
Set up the OT problem for the deterrence game on the lifted state space using scipy.optimize.linprog.

### SSA5_2_PerturbSweep
Solve OT for a systematic sweep of marginal perturbations away from ρ̃.

### SSA5_3_SupportStability
Analyze the support of the OT solution: does it change under perturbation? At what perturbation size does it change?

## Deliverables
- `report.md` with stability analysis
- Figures showing OT solution robustness


## Sub-agent Reports

### SSA5_1_OTSetup

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


---

### SSA5_2_PerturbSweep

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


---

### SSA5_3_SupportStability

# SSA5_3: Support Stability Analysis — Report

## Parameters
- Baseline Markov chain: α=0.3, β=0.5
- Game: x=0.3, y=0.4, supermodular=True
- Phase diagram grid: α,β ∈ [0.05, 0.95], 30×30

## Coupling Weight Analysis

The coupling weights γ(θ̃, a₁) are plotted as a function of perturbation strength ε in the direction toward F(·|B). For the supermodular deterrence game:

- States with θ_t=G retain their coupling to action A across perturbations
- States with θ_t=B retain their coupling to action F across perturbations
- The support structure (which pairs have positive weight) is the key stability indicator

## Phase Diagram Results

The stability margin ε* measures how much the marginal distribution can be perturbed (toward the F(·|B) conditional) before the OT support changes.

- **Minimum stability margin**: 0.100
- **Maximum stability margin**: 0.500
- **Mean stability margin**: 0.474
- **Fragile regions** (ε*<0.1): 0.0% of parameter space
- **Robust regions** (ε*≥0.3): 94.0% of parameter space
- **Baseline** (α=0.3, β=0.5): ε* = 0.500

## Interpretation

The OT support is broadly robust across the (α, β) parameter space. For the 2-state supermodular deterrence game, the co-monotone structure is inherently stable because the payoff ordering (G→A, B→F) is strong.

However, this does NOT mean the OT *value* is unchanged — only that the support (which state-action pairs are used) remains the same. The coupling weights do shift, which can affect equilibrium payoffs.

## Figures
![Coupling Weights vs Epsilon](figures/coupling_weights_vs_epsilon.png)

![Stability Margin Heatmap](figures/stability_margin_heatmap.png)


---
