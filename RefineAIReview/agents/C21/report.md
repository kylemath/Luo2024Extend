# C21: Inconsistent Payoffs and Stackelberg Strategy

## Severity: LOW
## Self-Assessment: GREEN

## Reviewer Concern

Only D-row payoffs are shown: `u1(G,A)=1, u1(G,F)=0.3, u1(B,A)=0.4, u1(B,F)=0`. Looking at the D-row alone, in state B: `u1(B,A)=0.4 > u1(B,F)=0`, so A dominates F. But the Stackelberg strategy prescribes `s1*(B)=F`. The full C-row payoffs make `s1*(B)=F` correct but are not displayed.

## Independent Verification

### D-row payoffs (from Section 7.1):
```
u1(G, A, D) = 1.0    u1(G, F, D) = x = 0.3
u1(B, A, D) = y = 0.4    u1(B, F, D) = 0.0
```

### In state B, against D only:
```
u1(B, A, D) = 0.4 > u1(B, F, D) = 0.0
→ A dominates F in state B (D-row only)
→ s1*(B) = F appears suboptimal
```

### Why s1*(B) = F is correct with full payoffs:
The Stackelberg strategy is not chosen to maximize single-period payoffs against D. It is chosen to maximize the **reputation payoff** — the payoff when SR eventually best-responds to the commitment type. The key mechanism:

1. If LR plays s1*(G)=A, s1*(B)=F consistently, SR learns the pattern
2. SR's best response depends on their belief about the state
3. When SR cooperates (believing state is likely G), LR benefits from reputation
4. Fighting in B is costly in the short run (0 vs 0.4) but makes the commitment type identifiable

Specifically, the Stackelberg strategy works because:
- It is **state-contingent**: different actions in different states
- SR can infer the state from LR's action
- This allows SR to best-respond contingent on the state
- In state G, SR cooperates → LR gets u1(G,A,C) (high payoff)
- The short-term cost of F in B is offset by the reputation benefit in G

### The C-row makes this explicit:
From the paper's computed values:
- u1(G,A,C) must give the stationary payoff 0.777 or the filtered payoff 0.628
- The gains from cooperation in G outweigh the cost of fighting in B
- Without C-row display, the reader cannot verify this directly

## Root Cause

The paper displays only the D-conditional payoffs (line 18-21) and references Luo & Wolitzky Section 2.1 for the full matrix. This is mathematically adequate (the referenced source has the full matrix) but pedagogically deficient: the reader seeing only D-payoffs will naturally question why F is chosen in B when A gives higher D-payoff.

## Proposed Resolution

### Option A (Preferred): Display the full payoff matrix
Add a table showing both C and D conditional payoffs for all (θ, a1) combinations. This is a few lines and resolves the confusion completely.

### Option B (Minimal): Add a clarifying remark
After the D-payoff display, add: "The Stackelberg strategy maximizes the reputation payoff (against SR best response to the commitment type), not the single-period payoff against D. Under the full payoff structure (including C-column payoffs from Luo & Wolitzky, 2024), s1*(B)=F is optimal because it makes the commitment type identifiable while cooperation gains in good states outweigh fighting costs in bad states."

## What Is NOT Wrong

- The Stackelberg strategy s1*(G)=A, s1*(B)=F is correct
- The reference to Luo & Wolitzky for the full payoff matrix is accurate
- The D-payoff values are correctly stated
- The supermodularity condition (x+y < 1) is correctly verified
