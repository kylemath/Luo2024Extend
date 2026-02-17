# SSA7_3: OT Under Various Orders

**Parent:** SA7_Monotonicity

## Task
Create `ot_orders.py` that:
1. For the 3-state game with supermodular u₁(θ, a₁):
2. For each total order on Θ̃ where supermodularity holds:
   - Compute the co-monotone coupling (sort both marginals and pair them)
   - Solve the general OT problem (linprog)
   - Check: does co-monotone coupling = OT solution?
3. For orders where supermodularity FAILS:
   - Solve OT anyway
   - Check: is the OT solution still unique? Is its support "monotone" in any sense?
4. Key test: with payoffs depending only on θ_t, does the first-coordinate order give the correct OT solution even though the lifted space is 2D?

## Deliverables
- `ot_orders.py`
- `figures/ot_solutions_by_order.png`
- `report.md` with analysis of which orders work
