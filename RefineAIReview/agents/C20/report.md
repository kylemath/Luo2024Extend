# C20: Missing Discussion of Stackelberg Well-Definedness

## Reviewer Comment
> Section 9.5 says Stackelberg well-definedness for persuasion games is "acknowledged as an open question in Section 10." But Section 10.2 doesn't mention it. Need to either add it to Section 10.2 or fix the cross-reference.

## Analysis

### Current State

**Section 9.5 (sec_09_methodology.tex, line 82):**
> "The partially accepted point concerns Stackelberg well-definedness for persuasion games, which is acknowledged as an open question in Section~\ref{sec:discussion}."

This references `\ref{sec:discussion}`, which resolves to Section 10.

**Section 10 (sec_10_discussion.tex):**
- Section 10.1 (Summary): No mention of Stackelberg well-definedness.
- Section 10.2 (Open Questions): Lists six open questions:
  1. Belief-robustness landscape
  2. Computation of V_Markov
  3. ε-perturbed strategies
  4. Rate of convergence
  5. Continuous state spaces
  6. Non-revealing strategies

**None of these mention Stackelberg well-definedness for persuasion games.**

The cross-reference is broken. Section 9.5 claims the topic is discussed in Section 10, but Section 10.2 omits it entirely.

### Context
Stackelberg well-definedness for persuasion games refers to the issue (raised by Luo in the review) that for persuasion games, the Stackelberg strategy involves solving a concavification problem, and different priors (which arise under Markov dynamics) may yield different optimal concavifications. This means the "Stackelberg strategy" may not be well-defined in the Markov setting, because the prior changes with each state.

### Severity Assessment
**MEDIUM** — This is a concrete cross-reference error. The paper makes a claim ("acknowledged as an open question in Section 10") that is factually incorrect about the paper's own content. Two valid fixes exist:
1. Add the open question to Section 10.2 (preferred, since it IS a legitimate open question)
2. Fix the cross-reference in Section 9.5 to acknowledge it's not discussed and note it as future work

## Proposed Resolution

**Option 1 (Recommended):** Add a paragraph to Section 10.2 discussing Stackelberg well-definedness:
- For persuasion games, the Stackelberg strategy is defined via Bayesian persuasion (concavification)
- Under Markov dynamics, the prior changes state-by-state via filtering
- The optimal persuasion scheme may differ across states
- Whether a state-independent Stackelberg strategy exists (and when) is an open question

## Self-Assessment
- **Confidence**: HIGH — This is a verified cross-reference error with a clear fix.
- **Risk**: LOW — Adding an open question paragraph is straightforward.
- **Verification needed**: Confirmed by reading both sections. The word "Stackelberg" does not appear in sec_10_discussion.tex, and "persuasion" does not appear there either.
