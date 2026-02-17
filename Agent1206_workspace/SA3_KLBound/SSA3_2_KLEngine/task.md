# SSA3_2: KL Divergence Computation Engine

**Parent:** SA3_KLBound

## Task
Create `kl_engine.py` that:
1. Takes signal distributions from SSA3_1 and computes per-period KL divergences
2. Compute D(q_t ‖ p_t) for each period t
3. Compute cumulative KL: ∑_{t=0}^{T} D(q_t ‖ p_t)
4. Check: does cumulative KL stay below −log μ₀? (Use μ₀ = 0.01)
5. Also compute TV distances ‖q_t − p_t‖ at each period
6. Count distinguishing periods: #{t : ‖q_t − p_t‖ > η} for η ∈ {0.01, 0.05, 0.1, 0.2}

## Deliverables
- `kl_engine.py`
- `figures/cumulative_kl.png` — cumulative KL vs −log μ₀ bound
- `figures/tv_per_period.png` — TV distance time series  
- `report.md` with KL bound verification results
