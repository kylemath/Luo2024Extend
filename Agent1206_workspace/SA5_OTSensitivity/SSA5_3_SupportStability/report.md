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
