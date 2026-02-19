# C16: Ambiguity in "Not Behaviorally Confounded" Application

## Reviewer Comment
> "Since s1* is not behaviorally confounded, any type with the same asymptotic signal distribution must be s1* itself" relies on an implicit identification between asymptotic conditional signal distributions and stationary p(α₀, s₁, α₂). Need to make explicit that filter stability + ergodicity ensure this.

## Analysis

### Current State
In `sec_05_proof.tex`, Part A of Lemma 5.7 (`lem:martingale`), lines 157–161:

```
Third, the KL bound from Lemma~\ref{lem:KL} (which holds unchanged) implies:
[equation for signal convergence]
$Q$-a.s., exactly as in the Luo--Wolitzky proof of Lemma~9 ... Since $s_1^*$ is not
behaviorally confounded, any type with the same asymptotic signal distribution must
be $s_1^*$ itself, hence $\mu_\infty(\{\omega^R, \omega_{s_1^*}\} | h) = 1$.
```

The logical chain is:
1. KL bound → signal distributions converge (equation 5.8)
2. "Not behaviorally confounded" → any type matching signal distribution must be s₁*
3. Therefore posterior concentrates on {ω^R, ω_{s₁*}}

The reviewer correctly identifies that step 2 contains an implicit leap. In the i.i.d. case, the asymptotic signal distribution equals the stationary signal distribution p(α₀, s₁, α₂) directly—there's no filtering. In the Markov case, the asymptotic per-period signal distribution depends on the filtering distribution π(θ_t | h_t, s₁), which converges to a limit determined by the observation process (by filter stability from Proposition A.2). The identification between "asymptotic signal distribution" and "stationary p(α₀, s₁, α₂)" requires two additional facts:

- **Filter stability** (Proposition A.2): π(θ_t | h_t, s₁) → π_∞(s₁) exponentially fast, regardless of initial condition
- **Ergodicity**: The limiting filter π_∞(s₁) under strategy s₁ determines a unique stationary signal distribution

Without stating these explicitly, the argument has a gap in the Markov case that doesn't exist in the i.i.d. case.

### Severity Assessment
**MEDIUM** — The mathematical tools to close the gap are already present in the paper (Proposition A.2 on filter stability). The issue is that the proof sketch doesn't invoke them at this critical juncture.

## Proposed Resolution

Expand the sentence at line 161 into a short paragraph that explicitly invokes:
1. Filter stability (Proposition A.2) to establish that the filtering distribution converges
2. Ergodicity to identify the limit as the unique stationary signal distribution
3. The "not behaviorally confounded" condition applied to the stationary distributions

## Self-Assessment
- **Confidence**: HIGH — The required tools are already in the paper; this is about making the argument explicit.
- **Risk**: LOW — This adds logical clarity without changing any mathematical content.
- **Verification needed**: None; this is a textual clarification of an existing argument.
