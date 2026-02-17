# SSA2_3: Full Counterexample Construction

**Parent:** SA2_StateRevealing

## Task
Create `counterexample.py` that:
1. Sets up the OT problem for the deterrence game on lifted state space
2. Solves OT with marginal = ρ̃ (stationary distribution) — this is what the paper uses
3. Solves OT with marginal = actual filtering distribution F(·|θ_t) for each possible θ_t
4. Compare: do the OT solutions have the same support? Same coupling?
5. If the supports differ for ANY filtering distribution, then confound-defeating at ρ̃ does NOT imply confound-defeating at the actual per-period belief
6. Use scipy.optimize.linprog to solve the OT problems
7. Test for both supermodular (x+y<1) and non-supermodular (x+y>1) payoffs

## Key Question
For the SPECIFIC deterrence game with supermodular payoffs: does the OT solution change between ρ̃ and F(·|θ_t)? If yes, the paper's main worked example fails. If no, there may be a restricted class where the approach works.

## Deliverables
- `counterexample.py`
- `figures/ot_support_comparison.png` — visualization of OT supports at ρ̃ vs F(·|θ_t)
- `report.md` with clear verdict on whether the counterexample succeeds
