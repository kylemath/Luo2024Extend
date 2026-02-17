# SSA2_3: Full Counterexample Construction — Report

## Summary

Compared optimal transport (OT) solutions for the deterrence game when computed at:
1. The lifted stationary distribution ρ̃ (as the paper proposes)
2. The actual SR belief distribution F(·|θ_t) for each conditioning state

## Setup

The OT problem finds the optimal coupling between states and actions that minimizes
expected cost (negative payoff). The key question: does the OT solution (and hence the
implied strategy) change when using F(·|θ_t) instead of ρ̃?

## Results

### Supermodular, baseline (α=0.3,β=0.5)

- Parameters: α=0.3, β=0.5, x=0.3, y=0.4
- Supermodular: True
- Payoff at ρ̃: 0.7750
- Weighted avg payoff at F(·|θ): 0.7750
- Payoff difference: 0.000000
- **Do OT solutions differ? NO — strategies match**

Effective strategy from ρ̃:
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|G):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|B):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

### Supermodular, high persistence (α=0.1,β=0.1)

- Parameters: α=0.1, β=0.1, x=0.3, y=0.4
- Supermodular: True
- Payoff at ρ̃: 0.7000
- Weighted avg payoff at F(·|θ): 0.7000
- Payoff difference: 0.000000
- **Do OT solutions differ? NO — strategies match**

Effective strategy from ρ̃:
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|G):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|B):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

### Non-supermodular (α=0.3,β=0.5,x=0.6,y=0.6)

- Parameters: α=0.3, β=0.5, x=0.6, y=0.6
- Supermodular: False
- Payoff at ρ̃: 0.8500
- Weighted avg payoff at F(·|θ): 0.8500
- Payoff difference: 0.000000
- **Do OT solutions differ? NO — strategies match**

Effective strategy from ρ̃:
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|G):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|B):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

### Supermodular, i.i.d. (α=β=0.5)

- Parameters: α=0.5, β=0.5, x=0.3, y=0.4
- Supermodular: True
- Payoff at ρ̃: 0.7000
- Weighted avg payoff at F(·|θ): 0.7000
- Payoff difference: 0.000000
- **Do OT solutions differ? NO — strategies match**

Effective strategy from ρ̃:
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|G):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

Strategy from F(·|B):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | 1.0000 | 0.0000 |
| B | 1.0000 | 0.0000 |

## Overall Verdict

Out of 4 parameter configurations tested:
- **0 cases** where OT solutions differ between ρ̃ and F(·|θ_t)
- **4 cases** where OT solutions match

**In these specific test cases, the OT solutions happen to match.** However, this
does NOT validate the paper's approach because:
1. The deterministic Stackelberg strategy (A in G, F in B) trivially solves OT
   regardless of the belief distribution — it's state-by-state optimal.
2. The real issue is whether the OT characterization correctly captures the SR player's
   INCENTIVE CONSTRAINTS, not just the LR player's optimization.
3. The belief gap (documented in SSA2_1 and SSA2_2) means the SR player faces
   different incentives than what ρ̃ implies, even if the LR optimal strategy
   happens to be robust to the belief change.

## Figures

![OT Support Comparison](figures/ot_support_comparison.png)

## Interpretation

The fundamental issue is structural: under Markov dynamics with a state-revealing strategy,
the SR player's belief is F(·|θ_t), not the stationary distribution. Whether or not the
OT solution happens to be the same for a particular game, the paper's theoretical framework
incorrectly characterizes the SR player's belief formation process, which affects the
validity of the equilibrium construction.
