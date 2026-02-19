# C14: Ambiguous Definition of Best-Response Set in Lemma 5.8

## Reviewer Comment
> B-hat_{xi(eta)}(s1*) appears without redefinition in the Markov extension. Readers may confuse it with state-dependent B(s1*,F(·|θ)). Need to recall B-hat is the static confirmed best-response set from Luo-Wolitzky.

## Analysis

### Current State
In `sec_05_proof.tex`, Lemma 5.8 (`lem:combining`, Section 5.4, lines 176–185):

```latex
(\sigma_0^*(h_t),\, \sigma_2^*(h_t)) \;\in\; \hat{B}_{\xi(\eta)}(s_1^*).
```

The notation $\hat{B}_{\xi(\eta)}(s_1^*)$ is used without being (re)defined in the Markov context. The paper introduces two distinct best-response objects:

1. **$B(s_1^*, F(\cdot|\theta))$** — the state-contingent Nash correspondence (Definition 4.2, used in Theorem 1'')
2. **$\hat{B}_{\xi(\eta)}(s_1^*)$** — the $\xi$-confirmed best-response set (from Luo-Wolitzky 2024)

The proof of Lemma 5.8 (lines 183–184) explains the logic correctly but does not explicitly disambiguate the two objects. A reader encountering $\hat{B}$ for the first time in the Markov proof sketch may reasonably confuse it with the state-dependent correspondence $B(s_1^*, F(\cdot|\theta))$.

### Where $\hat{B}$ Is Used
- Lemma 5.8 statement (line 179)
- Lemma 5.8 proof (line 184)
- Step 5 payoff bound (lines 196, 202)
- Remark on continuation value (line 72, referencing $B_\eta(s_1^*)$)

### Severity Assessment
**MEDIUM** — This is a notation clarity issue. The mathematical content is correct, but the reader must mentally track which best-response set is being used where. A short clarification would significantly improve readability.

## Proposed Resolution

Add a brief clarifying remark before Lemma 5.8 that:
1. Recalls that $\hat{B}_{\xi}(s_1^*)$ denotes the $\xi$-confirmed best-response set from Luo-Wolitzky (2024, Definition 3)
2. Distinguishes it from the state-contingent $B(s_1^*, F(\cdot|\theta))$ introduced in this paper
3. Notes that the two coincide under belief-robustness

## Self-Assessment
- **Confidence**: HIGH — This is a purely notational clarification with no risk to correctness.
- **Risk**: LOW — Text-only change; no mathematical content affected.
- **Verification needed**: Confirm that the term "confirmed best-response set" matches Luo-Wolitzky's terminology.
