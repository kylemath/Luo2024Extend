# SSA3_1: Signal Process Simulator

**Parent:** SA3_KLBound

## Task
Create `signal_sim.py` that:
1. Simulates two processes on the SAME Markov state sequence:
   - Q process: commitment type plays s₁*(G)=A, s₁*(B)=F deterministically
   - P process: "confused" type plays s₁'(G)=0.7A+0.3F, s₁'(B)=0.4A+0.6F (mixed)
2. At each time step, compute signal distributions:
   - q_t(y|h_t) = Pr(signal | commitment type, history)
   - p_t(y|h_t) = Pr(signal | confused type, history)
3. Note: for the commitment type, since the strategy is deterministic and state-revealing, q_t is degenerate (one signal has probability 1). For the mixed type, p_t depends on the SR player's belief about θ_t.
4. Store per-period signal distributions for KL computation

## Deliverables
- `signal_sim.py`
- `report.md` describing the signal process structure
