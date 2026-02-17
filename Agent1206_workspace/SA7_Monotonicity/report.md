# Report: SA7_Monotonicity (SA7_Monotonicity)

**Status:** completed
**Level:** Subagent
**Parent:** Agent1206
**Generated:** 2026-02-17T00:42:04.297872

## Task

# SA7: Monotonicity in Higher-Dimensional Lifted Space

**Assigned to:** SA7_Monotonicity  
**Parent:** Agent1206 (Orchestrator)  
**Priority:** MEDIUM — tests whether supermodular characterization extends

## Objective

Luo says "our definition of monotonicity only works for one dimensional states and actions, which the 'lifting' technique here obviates." Test whether the monotonicity/supermodularity characterization survives the lifting to θ̃ = (θ_t, θ_{t-1}).

## Sub-subagent Assignments

### SSA7_1_GameSetup
Define a 3-state, 3-action game where supermodularity holds in (θ, a₁) but may fail in the lifted space.

### SSA7_2_SupermodCheck
Systematically check supermodularity of payoffs under various orderings of the lifted state space.

### SSA7_3_OTOrders
For each valid ordering, solve the OT problem and verify whether the co-monotone coupling is optimal.

## Deliverables
- `report.md` with clear answer: does monotonicity extend to the lifted space?


## Sub-agent Reports

### SSA7_1_GameSetup

# SSA7_1: Multi-State Game Setup — Report

## Base Game
- **States:** Θ = {L, M, H} with order L < M < H
- **Actions:** A₁ = {l, m, h} with order l < m < h
- **Payoff:** u₁(θ, a) = 1.5 · θ · a  (θ, a ∈ {0, 1, 2})
- **Supermodular:** True

### Payoff Matrix
| | l | m | h |
|---|---|---|---|
| L | 0.0 | 0.0 | 0.0 |
| M | 0.0 | 1.5 | 3.0 |
| H | 0.0 | 3.0 | 6.0 |

## Markov Chain
- **Persistence parameter:** α_stay = 0.6
- **Stationary distribution:** π = [0.2857, 0.4286, 0.2857]

## Lifted State Space
- **Θ̃ = Θ × Θ:** 9 states
- **States:** (L,L), (L,M), (L,H), (M,L), (M,M), (M,H), (H,L), (H,M), (H,H)

### Lifted Stationary Distribution
| State | ρ̃ |
|---|---|
| (L,L) | 0.171429 |
| (L,M) | 0.085714 |
| (L,H) | 0.028571 |
| (M,L) | 0.085714 |
| (M,M) | 0.257143 |
| (M,H) | 0.085714 |
| (H,L) | 0.028571 |
| (H,M) | 0.085714 |
| (H,H) | 0.171429 |

## Payoff Variants
1. **θ_t-only payoff:** u₁(θ̃, a) = 1.5 · θ_t · a (ignores θ_{t-1})
2. **Transition-dependent:** u₁(θ̃, a) = 1.5 · θ_t · a + 0.5 · (θ_t − θ_{t-1}) · a

## Figures
![Payoff Matrices](figures/payoff_matrices.png)
![Stationary Distributions](figures/stationary_distributions.png)
![Transition Matrix](figures/transition_matrix.png)

## Key Observations
- The base game is supermodular with increasing differences.
- The lifted state space has 9 states, making exhaustive order enumeration feasible (9! = 362,880).
- The θ_t-only payoff preserves the base game's structure for states grouped by θ_t.
- The transition-dependent payoff introduces interactions between θ_t and θ_{t-1}.
- These structures will be tested for supermodularity under various orders in SSA7_2.

---

### SSA7_2_SupermodCheck

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

---

### SSA7_3_OTOrders

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

---
