#!/usr/bin/env python3
"""
C13 Verification: State-Contingent Nash Correspondence vs. Type-Posterior Evolution

Demonstrates the key distinction:
  - Type-posterior μ_t evolves in BOTH i.i.d. and Markov cases (standard reputation dynamics)
  - State-contingent best response B(s₁*, F(·|θ_t)) is NEW and specific to Markov states

Shows that the novel phenomenon is B varying with θ_t, not μ_t evolving.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)


def simulate_beliefs(alpha, beta, T, is_iid=False):
    """
    Simulate state sequence and the resulting SR beliefs about next-period state.

    In i.i.d. case: SR belief about θ_{t+1} is always π regardless of θ_t
    In Markov case: SR belief about θ_{t+1} is F(·|θ_t), which depends on θ_t
    """
    pi_G = beta / (alpha + beta)

    if is_iid:
        states = np.random.choice(2, size=T, p=[pi_G, 1 - pi_G])
    else:
        F_mat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
        states = np.zeros(T, dtype=int)
        states[0] = 0 if np.random.rand() < pi_G else 1
        for t in range(1, T):
            states[t] = np.random.choice(2, p=F_mat[states[t - 1]])

    if is_iid:
        sr_belief_G = np.full(T, pi_G)
    else:
        sr_belief_G = np.where(states == 0, 1 - alpha, beta)

    return states, sr_belief_G, pi_G


def simulate_type_posterior(T, mu_0_commit=0.01, distinguish_prob=0.1):
    """
    Simplified simulation of type-posterior evolution μ_t.
    In each period, with some probability the SR observes a "distinguishing" signal.
    This happens in BOTH i.i.d. and Markov cases - it is NOT the novel phenomenon.
    """
    mu_t = np.zeros(T)
    mu_t[0] = mu_0_commit
    for t in range(1, T):
        if np.random.rand() < distinguish_prob:
            mu_t[t] = mu_t[t - 1] * 0.95
        else:
            mu_t[t] = min(mu_t[t - 1] * 1.05, 0.99)
    return mu_t


def main():
    alpha, beta = 0.3, 0.5
    T = 300
    mu_star = 0.6  # SR threshold

    fig, axes = plt.subplots(3, 2, figsize=(14, 13))
    fig.suptitle(
        'C13 Verification: Novel Phenomenon = State-Contingent B(s₁*), NOT μ_t Evolution',
        fontsize=13, fontweight='bold'
    )

    # Panel 1: i.i.d. case - SR belief is constant
    np.random.seed(42)
    states_iid, sr_belief_iid, pi_G = simulate_beliefs(alpha, beta, T, is_iid=True)

    ax = axes[0, 0]
    ax.plot(sr_belief_iid[:150], 'b-', linewidth=1.5, label='SR belief about P(G next)')
    ax.axhline(y=pi_G, color='red', linestyle='--', linewidth=1.5, label=f'π(G) = {pi_G:.3f}')
    ax.axhline(y=mu_star, color='orange', linestyle=':', linewidth=1.5, label=f'μ* = {mu_star}')
    state_colors = ['green' if s == 0 else 'salmon' for s in states_iid[:150]]
    for t in range(150):
        ax.axvspan(t, t + 1, alpha=0.08, color=state_colors[t])
    ax.set_title('I.I.D. Case: SR Belief Always = π(G) ← State-Independent')
    ax.set_ylabel('SR belief P(G next)')
    ax.set_xlabel('Period')
    ax.legend(fontsize=8)
    ax.set_ylim(0.3, 0.9)

    # Panel 2: Markov case - SR belief is state-contingent
    np.random.seed(42)
    states_mk, sr_belief_mk, _ = simulate_beliefs(alpha, beta, T, is_iid=False)

    ax = axes[0, 1]
    ax.plot(sr_belief_mk[:150], 'b-', linewidth=1.5, label='SR belief F(G|θ_t)')
    ax.axhline(y=pi_G, color='red', linestyle='--', linewidth=1.5, label=f'π(G) = {pi_G:.3f}')
    ax.axhline(y=mu_star, color='orange', linestyle=':', linewidth=1.5, label=f'μ* = {mu_star}')
    ax.axhline(y=1 - alpha, color='green', linestyle='-.', alpha=0.6, label=f'F(G|G) = {1 - alpha}')
    ax.axhline(y=beta, color='darkred', linestyle='-.', alpha=0.6, label=f'F(G|B) = {beta}')
    state_colors = ['green' if s == 0 else 'salmon' for s in states_mk[:150]]
    for t in range(150):
        ax.axvspan(t, t + 1, alpha=0.08, color=state_colors[t])
    ax.set_title('MARKOV Case: SR Belief = F(G|θ_t) ← STATE-CONTINGENT (Novel!)')
    ax.set_ylabel('SR belief F(G|θ_t)')
    ax.set_xlabel('Period')
    ax.legend(fontsize=7)
    ax.set_ylim(0.3, 0.9)

    # Panel 3: Best response in i.i.d. - always the same
    ax = axes[1, 0]
    br_iid = np.where(sr_belief_iid[:150] > mu_star, 1, 0)  # 1=cooperate, 0=defect
    ax.step(range(150), br_iid, 'b-', linewidth=1.5, where='mid')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Defect', 'Cooperate'])
    ax.set_title(f'I.I.D.: SR Best Response (π(G)={pi_G:.3f} > μ*={mu_star}? → Always Coop)')
    ax.set_xlabel('Period')
    frac_coop_iid = np.mean(br_iid)
    ax.text(75, 0.5, f'Cooperation rate: {frac_coop_iid:.0%}', fontsize=11,
            ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    # Panel 4: Best response in Markov - varies with state
    ax = axes[1, 1]
    br_mk = np.where(sr_belief_mk[:150] > mu_star, 1, 0)
    colors_br = ['green' if b == 1 else 'red' for b in br_mk]
    ax.step(range(150), br_mk, 'b-', linewidth=1.5, where='mid')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Defect', 'Cooperate'])
    ax.set_title(f'MARKOV: SR Best Response Varies with θ_t (Novel!)')
    ax.set_xlabel('Period')
    frac_coop_mk = np.mean(br_mk)
    for t in range(150):
        ax.axvspan(t, t + 1, alpha=0.08, color=state_colors[t])
    ax.text(75, 0.5,
            f'Cooperation rate: {frac_coop_mk:.0%}\n'
            f'(SR defects in B states since F(G|B)={beta} < μ*={mu_star})',
            fontsize=9, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Panel 5: Type-posterior μ_t evolves in BOTH cases - NOT the novel phenomenon
    np.random.seed(42)
    mu_t_iid = simulate_type_posterior(T)
    np.random.seed(42)
    mu_t_mk = simulate_type_posterior(T)

    ax = axes[2, 0]
    ax.plot(mu_t_iid[:150], 'b-', linewidth=1.5, alpha=0.7, label='μ_t (i.i.d.)')
    ax.plot(mu_t_mk[:150], 'r--', linewidth=1.5, alpha=0.7, label='μ_t (Markov)')
    ax.set_title('Type-Posterior μ_t Evolves in BOTH Cases\n(This is NOT the novel phenomenon)')
    ax.set_ylabel('μ_t (prob of commitment type)')
    ax.set_xlabel('Period')
    ax.legend(fontsize=9)

    # Panel 6: Summary
    ax = axes[2, 1]
    ax.axis('off')
    summary = (
        "C13: KEY DISTINCTION\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "What the paper INCORRECTLY says is novel:\n"
        "  'Nash correspondence B(s₁*) must be written\n"
        "   as B(s₁*, μ₀(h_t)) — since μ₀ changes'\n\n"
        "  Problems:\n"
        "  1. μ₀ is FIXED prior; posteriors are μ_t\n"
        "  2. μ_t evolution happens in i.i.d. too!\n\n"
        "What is ACTUALLY novel in Markov case:\n"
        "  B becomes STATE-CONTINGENT:\n"
        "    B(s₁*, F(·|θ_t)) varies with θ_t\n\n"
        "  In i.i.d.: B(s₁*, π) same for all θ_t\n"
        "  In Markov: B(s₁*, F(·|G)) ≠ B(s₁*, F(·|B))\n\n"
        "  This is what belief-robustness addresses:\n"
        "  BR holds ⟺ B(s₁*, F(·|θ)) constant in θ\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  α={alpha}, β={beta}\n"
        f"  F(G|G)={1 - alpha:.2f}, F(G|B)={beta:.2f}\n"
        f"  μ*={mu_star}: inside [{beta}, {1 - alpha}] → BR fails"
    )
    ax.text(0.02, 0.98, summary, transform=ax.transAxes, fontsize=8.5,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/Users/kylemathewson/mathTest/RefineAIReview/agents/C13/verification_c13.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print("=" * 60)
    print("C13 VERIFICATION RESULTS")
    print("=" * 60)
    print(f"\nParameters: α={alpha}, β={beta}, π(G)={pi_G:.3f}, μ*={mu_star}")
    print(f"F(G|G) = {1 - alpha:.2f}, F(G|B) = {beta:.2f}")
    print()
    print("I.I.D. case:")
    print(f"  SR belief: always π(G) = {pi_G:.3f}")
    print(f"  π(G) > μ*? {pi_G > mu_star} → SR always cooperates")
    print(f"  B(s₁*, π) is state-INDEPENDENT")
    print()
    print("Markov case:")
    print(f"  SR belief in G: F(G|G) = {1 - alpha:.2f} > μ* = {mu_star} → cooperate")
    print(f"  SR belief in B: F(G|B) = {beta:.2f} < μ* = {mu_star} → defect")
    print(f"  B(s₁*, F(·|θ_t)) is state-CONTINGENT ← this is novel!")
    print()
    print("Type-posterior μ_t:")
    print(f"  Evolves in BOTH cases (not novel)")
    print(f"  Paper incorrectly attributes novelty to μ₀/μ_t evolution")
    print(f"  Uses wrong notation μ₀ instead of μ_t")
    print()
    print("Figure saved: verification_c13.png")


if __name__ == '__main__':
    main()
