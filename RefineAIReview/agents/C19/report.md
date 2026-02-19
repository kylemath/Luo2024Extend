# C19 Analysis Report: Imprecise Terminology Regarding Filter Stability

## Comment Summary
**Severity**: LOW  
**Location**: `app_A_kl_verification.tex`, paragraph after Proposition A.2 (line 36)  
**Reviewer claim**: The text "initial condition of the Markov chain is 'forgotten' exponentially fast" reads as if referring to θ₀ (chain mixing) rather than π₀ (prior forgetting). Proposition A.2 is about the filter's dependence on the initial prior.

## Diagnosis

### The Problematic Text
From `app_A_kl_verification.tex`, line 36:

> "This ensures that the initial condition of the Markov chain is 'forgotten' exponentially fast, so the per-period signal distribution converges to a limit determined by the observation process alone—the key property used in Step 3 of the proof."

### Why the Reviewer Is Correct

Proposition A.2 (`prop:filter_stability`) states:

$$\sup_{\pi_0, \pi_0'} \|\pi_t - \pi_t'\| \leq C \cdot \lambda^t$$

where π_t and π_t' are **filters** starting from priors π₀ and π₀'. This is a statement about the **filter** (the posterior distribution over states given observations) forgetting its **initial prior** π₀.

The phrase "initial condition of the Markov chain" is ambiguous:
- **Reading 1 (incorrect)**: θ₀, the initial state of the hidden Markov chain. Forgetting θ₀ is **chain mixing** — a property of the Markov chain itself, governed by its spectral gap. This is a different mathematical object.
- **Reading 2 (intended)**: π₀, the initial prior used to initialize the filter. Forgetting π₀ is **filter stability** — a property of the filtering recursion. This is what Proposition A.2 actually states.

The text uses the language of Reading 1 ("initial condition of the Markov chain") to describe the content of Reading 2 (filter stability). A reader familiar with HMM theory would likely parse this correctly from context, but the phrasing is genuinely imprecise and could confuse readers less familiar with the distinction.

### The Second Clause Is Also Imprecise
The continuation "so the per-period signal distribution converges to a limit determined by the observation process alone" is also loose. The per-period signal distribution is always determined by the current state θ_t and the observation channel — filter stability doesn't change what determines the signal. What filter stability ensures is that the **filter's prediction** of the signal distribution is insensitive to the initial prior π₀.

## Proposed Resolution

1. **Replace "initial condition of the Markov chain"** with "initial prior" or "initial filtering distribution"
2. **Clarify the second clause**: the filter's prediction, not the signal distribution itself, becomes insensitive to initialization
3. **Add parenthetical** distinguishing filter stability (prior forgetting) from chain mixing (state forgetting)

## Self-Assessment

- **Validity of reviewer comment**: ✅ Valid. The terminology is genuinely ambiguous.
- **Severity**: LOW is appropriate. This is a wording issue in the appendix, not a conceptual or mathematical error. The proposition itself is stated correctly.
- **Confidence in proposed fix**: HIGH. Simple rephrasing resolves the ambiguity.
- **Risk of over-correction**: LOW. A brief clarification is all that's needed.
- **Relationship to other comments**: Part of the filter stability cluster (C07, C11, C19). C07 and C11 target the conceptual error in Section 10.2; C19 targets the terminological imprecision in Appendix A. All three stem from imprecise treatment of what filter stability means.
