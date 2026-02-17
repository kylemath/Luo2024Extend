# SSA7_2: Supermodularity Checker — Report

## Objective
Check whether increasing differences (supermodularity) of payoffs extends
from the base 3-state game to the lifted state space Θ̃ = Θ × Θ (9 states)
under various total orderings.

## Payoff Variants
1. **θ_t-only:** u₁(θ̃, a) = 1.5 · θ_t · a
2. **Transition-dependent:** u₁(θ̃, a) = 1.5·θ_t·a + 0.5·(θ_t − θ_{t-1})·a
3. **Strong history:** u₁(θ̃, a) = θ_t·a + θ_{t-1}·a

## Canonical Order Results

| Order | θ_t only | Transition dep. | Strong history |
|-------|----------|-----------------|----------------|
| lexicographic | ✓ | ✗ (27 viol.) | ✗ (6 viol.) |
| first_coord | ✓ | ✗ (27 viol.) | ✗ (6 viol.) |
| reverse_lex | ✗ (27 viol.) | ✗ (54 viol.) | ✗ (6 viol.) |
| sum_order | ✗ (6 viol.) | ✗ (33 viol.) | ✓ |

## Exhaustive Enumeration (All 362,880 Orders)

| Payoff Type | Valid Orders | Fraction |
|-------------|-------------|----------|
| θ_t only | 216 | 0.000595 |
| Transition dep. | 1 | 0.000003 |
| Strong history | 24 | 0.000066 |

## Figures
![Supermodularity Fraction](figures/supermod_fraction_by_payoff.png)
![Canonical Order Results](figures/canonical_order_results.png)

## Key Findings

1. **θ_t-only payoff:** Supermodularity holds under 216 of 362,880 orders (0.0595%). Any order that respects the θ_t ranking preserves supermodularity, since the payoff ignores θ_{t-1}.

2. **Transition-dependent payoff:** Only 1 of 362,880 orders preserve supermodularity (0.0003%). The coupling between θ_t and θ_{t-1} makes it harder to find a consistent order.

3. **Strong history payoff:** 24 of 362,880 orders work (0.0066%). Since both coordinates contribute symmetrically, sum-based orders perform well.

4. **Implication for the paper:** Monotonicity/supermodularity does NOT automatically extend
   to the lifted state space for all payoff structures. The choice of order on Θ̃ is crucial.
   For payoffs depending only on θ_t, any θ_t-consistent order suffices; but for
   transition-dependent payoffs, valid orders may be rare or non-existent.