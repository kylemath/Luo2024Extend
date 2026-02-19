# C10: Missing Content in Appendix A.3 — Monte Carlo Verification

## Reviewer Comment
> "A.3 Monte Carlo Verification" appears to be empty (header only). Main text (Section 5.4) relies on it.

## Analysis

### Current State
Appendix A.3 (in `app_A_kl_verification.tex`, lines 38–45) contains:
- A `\subsection{Monte Carlo Verification}` header
- A figure environment with `fig_kl_bound.png` and a caption
- **No explanatory text whatsoever**

The caption references N=`\KLMonteCarloN` (500) runs and T=`\KLMonteCarloPeriods` (5000) periods, but provides no details about the simulation methodology.

### Cross-References
The Monte Carlo verification is referenced in:
1. **Section 5.2 (Step 2: KL Counting Bound)**, line 136: "Monte Carlo verification ($N=\KLMonteCarloN$ simulations, $T=\KLMonteCarloPeriods$ periods) confirms that the empirical distribution of distinguishing-period counts is nearly identical for Markov and i.i.d.\ processes (Figure~\ref{fig:kl_bound})."
2. **Section 1.2 (Computational Verification)**, line 14: references the same Monte Carlo simulations.

### Severity Assessment
**HIGH** — The main text makes a quantitative claim (KL bound is identical for Markov and i.i.d.) supported by a figure whose methodology is not described. This is a clear gap in the paper's reproducibility.

## Proposed Resolution

Add a paragraph between the subsection header and the figure environment that:
1. Describes the simulation setup (two parallel processes: Markov chain with parameters α,β and an i.i.d. process with the same stationary distribution)
2. Explains the methodology (for each run: simulate signals, compute Bayesian posteriors, count distinguishing periods where ‖p_t − q_t‖ > η)
3. States the key comparison metric (empirical CDF of distinguishing-period counts)
4. Reports the numerical outcome (from stats.tex: i.i.d. mean count 8.1 vs. Markov mean count 12.7, both below the theoretical bound)

## Self-Assessment
- **Confidence**: HIGH — This is a clear omission requiring only text addition; the figure and statistics already exist.
- **Risk**: LOW — Adding explanatory text does not alter any results.
- **Verification needed**: The proposed text should be consistent with the statistics in `stats.tex` (specifically `\statIidMeanCount{8.1}` and `\statMarkovMeanCount{12.7}`).
