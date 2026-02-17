# SSA2_2: Divergence Analysis for State-Revealing Strategies

**Parent:** SA2_StateRevealing

## Task  
Create `divergence_analysis.py` that:
1. For a range of (α,β) values, compute the PERMANENT belief gap
2. Analytical formula: when state is revealed, SR belief about θ_{t+1} is F(·|θ_t)
   - Gap after G: |F(G|G) − π(G)| = |(1-α) − β/(α+β)| = |α(1-α-β)|/(α+β)
   - Gap after B: |F(G|B) − π(G)| = |β − β/(α+β)| = |αβ|/(α+β)
3. Expected gap = π(G)·gap_after_G + π(B)·gap_after_B
4. Plot: heatmap of expected gap over (α,β) ∈ [0.01, 0.99]²
5. Identify when gap = 0 (only when α+β=1, i.e., essentially i.i.d.)
6. Compare to simulated gaps from SSA2_1

## Key Finding to Report
The gap is ZERO if and only if the chain is i.i.d. For any persistent chain (α+β ≠ 1), there is a permanent, non-vanishing discrepancy between SR beliefs and the stationary distribution.

## Deliverables
- `divergence_analysis.py`
- `figures/belief_gap_heatmap.png`
- `figures/gap_vs_persistence.png` (1D slice along α=β)
- `report.md` with analytical formulas and numerical verification
