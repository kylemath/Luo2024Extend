# SSA7_2: Supermodularity Checker

**Parent:** SA7_Monotonicity

## Task
Create `supermod_check.py` that:
1. Given payoff u₁(θ̃, a₁) and a total order on Θ̃:
   Check whether u₁ has increasing differences in (θ̃, a₁)
   i.e., for θ̃' > θ̃ and a₁' > a₁: u₁(θ̃', a₁') - u₁(θ̃', a₁) ≥ u₁(θ̃, a₁') - u₁(θ̃, a₁)
2. Test with payoffs depending only on θ_t (ignoring θ_{t-1}):
   - Lexicographic order: (θ_t, θ_{t-1}) ordered lex → check supermodularity
   - First-coordinate order: ordered by θ_t, ties broken arbitrarily → check
3. Test with payoffs depending on both θ_t and θ_{t-1}:
   - Some natural payoff that depends on transitions → check supermodularity
4. Enumerate ALL possible total orders on 9 lifted states (9! = 362880 — sample 10000)
5. For each sampled order, check supermodularity
6. Report: fraction of orders where supermodularity holds

## Deliverables
- `supermod_check.py`
- `figures/supermod_fraction_by_payoff.png` — fraction of valid orders per payoff type
- `report.md` with results and interpretation
