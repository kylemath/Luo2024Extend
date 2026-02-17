# SSA6_1: SR Player Best Response Computation

**Parent:** SA6_NashDynamics

## Task
Create `best_response.py` that:
1. In the deterrence game, the SR player chooses a₂ ∈ {C, D}
2. SR payoffs depend on their belief μ = Pr(θ=G):
   - Define SR payoff matrix u₂(θ, a₁, a₂) for some reasonable parameterization
   - For simplicity, assume SR payoff: u₂ = 1 if (θ=G, a₂=C), u₂ = 0 if (θ=G, a₂=D), u₂ = -1 if (θ=B, a₂=C), u₂ = 0.5 if (θ=B, a₂=D)
3. SR expected payoff from C: μ·1 + (1-μ)·(-1) = 2μ - 1
4. SR expected payoff from D: μ·0 + (1-μ)·0.5 = 0.5(1-μ)
5. SR plays C iff 2μ - 1 > 0.5(1-μ) iff μ > 3/5 = 0.6
6. So B(s₁, μ) changes at μ = 0.6: C for μ > 0.6, D for μ < 0.6
7. Plot: best response as function of μ
8. Compute: how often does μ(h_t) cross the threshold 0.6 in the Markov game?

## Deliverables
- `best_response.py`
- `figures/best_response_vs_belief.png`
- `figures/threshold_crossings.png` — how often beliefs cross the BR threshold
- `report.md` with analysis
