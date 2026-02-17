# Extending "Marginal Reputation" to Markov States: Critique, Testing & Correction

**Kyle Mathewson, University of Alberta | February 2026**

---

## The Critique — 3 Core Flaws Identified (Daniel Luo)

| # | Flaw | Evidence |
|---|------|----------|
| 1 | SR beliefs permanently deviate from stationary distribution | Mean TV distance = 0.47; gap = 2αβ\|1−α−β\|/(α+β)²; zero iff i.i.d. |
| 2 | Nash correspondence B(s₁) is dynamic, not static | B(s₁, μ₀(h_t)) varies with history; SR actions differ in 37.7% of periods |
| 3 | Commitment payoff overestimated by 14.7% | Stationary assumption: 0.64 vs filtered reality: 0.55 |

Plus 12 additional points addressed (lifting motivation, payoff structure, NBC claim, monotonicity, Stackelberg, Pei (2020) connection, and more).

---

## What Survived — Verified by 21 Scripts, 40 Figures

| Claim | Key Result |
|-------|------------|
| KL counting bound extends verbatim | Markov ≈ i.i.d. counts (N=1000 MC sims) |
| Filter stability (exponential forgetting) | λ ≈ \|1−α−β\|, R² > 0.99 |
| OT solution robust to belief perturbations | Stable in 94% of (α,β) space |
| Monotonicity extends for θ_t-only payoffs | First-coordinate order works |

---

## The Fix — Two Corrected Theorems

**Theorem 1' (Belief-Robust Games):** If SR best-response is unchanged when SR learns the state — formally, μ\* ∉ [β, 1−α] — then the original bound V(s₁\*) holds exactly.

**Theorem 1'' (General Corrected Bound):** V_Markov(s₁\*) ≤ V(s₁\*), with equality iff belief-robust. The gap is "the cost of persistence in reputation games."

---

## All 15 Critiques Addressed

10 fully accepted — including new §3 on belief-robustness. 1 partial (Stackelberg works for supermodular; persuasion remains open). 4 additional questions resolved.

**Deliverables:** 28-page revised paper · 10-page response letter · 8 figures · 7 scripts · `bash generate_paper.sh`
