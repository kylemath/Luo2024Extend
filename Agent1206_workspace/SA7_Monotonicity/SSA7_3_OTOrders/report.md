# SSA7_3: OT Under Various Orders — Report

## Objective
Solve the optimal transport problem under various total orderings of the lifted
state space and verify whether the co-monotone coupling is optimal when
supermodularity holds.

## Setup
- Lifted states: 9 states (Θ × Θ)
- Marginals: μ = lifted stationary distribution, ν = Stackelberg action distribution
- Cost: -u₁(θ̃, a) (minimize negative payoff = maximize payoff)

## Canonical Order Results

| Order | Payoff | Supermod? | OT Payoff | Como Payoff | Como=OT? | OT Monotone? |
|-------|--------|-----------|-----------|-------------|----------|--------------|
| lexicographic | theta_t_only | ✓ | 2.3571 | 2.3571 | ✓ | ✓ |
| lexicographic | transition_dep | ✗ | 2.5000 | 2.5000 | ✓ | ✓ |
| reverse_lex | theta_t_only | ✗ | 2.3571 | 1.9286 | ✗ | ✗ |
| reverse_lex | transition_dep | ✗ | 2.5000 | 1.7857 | ✗ | ✗ |
| sum_order | theta_t_only | ✗ | 2.3571 | 2.2714 | ✗ | ✗ |
| sum_order | transition_dep | ✗ | 2.5000 | 2.3286 | ✗ | ✗ |

## Random Order Analysis (500 samples, θ_t-only payoff)

- Orders with supermodularity: 1
  - Co-monotone = OT: 1
  - Co-monotone ≠ OT: 0
- Orders without supermodularity: 499
  - OT monotone: 0
  - OT not monotone: 499

**P(co-monotone = OT | supermod) = 1.0000**
**P(OT monotone | ¬supermod) = 0.0000**

## Key Test: First-Coordinate Order

- Supermodular under first-coordinate order: True
- Co-monotone coupling matches OT: True

**Interpretation:** The first-coordinate order correctly recovers the OT solution for θ_t-only payoffs, confirming that the lifting technique preserves the essential monotonicity structure when payoffs depend only on the current state.

## Figures
![OT Solutions by Order](figures/ot_solutions_by_order.png)
![OT Analysis Summary](figures/ot_analysis_summary.png)

## Key Findings

1. **Supermodularity implies co-monotone optimality:** When increasing differences hold
   under a given order, the co-monotone coupling is (typically) the OT solution.

2. **Order choice is critical:** Different orderings of the lifted space lead to
   different supermodularity and OT results. Not all orders work.

3. **θ_t-only payoffs are well-behaved:** For payoffs depending only on θ_t,
   the first-coordinate order (natural extension of the base order) suffices.

4. **Transition-dependent payoffs are harder:** When payoffs depend on (θ_t, θ_{t-1}),
   the choice of order becomes non-trivial and may require problem-specific analysis.

5. **Implication for the paper's claims:** The paper's lifting technique works for
   monotonicity when payoffs have appropriate structure (θ_t-only), but does NOT
   automatically extend to all payoff functions on the lifted space.