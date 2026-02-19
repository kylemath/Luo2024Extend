#!/usr/bin/env python3
"""
C20 Verification: Cross-reference check for Stackelberg well-definedness
discussion between Section 9.5 and Section 10.2.

Confirms the cross-reference error: Section 9.5 claims the topic is
discussed in Section 10, but Section 10.2 omits it.
"""


def main():
    print("=" * 65)
    print("  C20: Cross-Reference Check — Stackelberg Well-Definedness")
    print("=" * 65)

    # Content from Section 9.5 (sec_09_methodology.tex, line 82)
    sec_9_5_claim = (
        'The partially accepted point concerns Stackelberg well-definedness '
        'for persuasion games, which is acknowledged as an open question '
        'in Section~\\ref{sec:discussion}.'
    )

    # Open questions listed in Section 10.2 (sec_10_discussion.tex)
    sec_10_2_topics = [
        "Belief-robustness landscape",
        "Computation of V_Markov",
        "epsilon-perturbed strategies",
        "Rate of convergence",
        "Continuous state spaces",
        "Non-revealing strategies / approximate belief-robustness",
    ]

    print(f"\nSection 9.5 claim:")
    print(f"  \"{sec_9_5_claim}\"")

    print(f"\nSection 10.2 open questions:")
    for i, topic in enumerate(sec_10_2_topics, 1):
        has_stackelberg = "stackelberg" in topic.lower() or "persuasion" in topic.lower()
        marker = " <-- MATCH" if has_stackelberg else ""
        print(f"  {i}. {topic}{marker}")

    print(f"\nResult: NO mention of Stackelberg well-definedness in Section 10.2")
    print(f"Cross-reference is BROKEN.")

    # The issue explained
    print(f"\n--- The Underlying Issue ---")
    print(f"  For persuasion games, the Stackelberg strategy is defined via")
    print(f"  concavification of the sender's value function.")
    print(f"  Under Markov dynamics, the receiver's prior is F(.|theta),")
    print(f"  which varies by state. Different priors may yield different")
    print(f"  optimal concavifications, so the 'Stackelberg strategy' may")
    print(f"  not be well-defined as a state-independent object.")
    print(f"\n--- Resolution ---")
    print(f"  Add a paragraph on Stackelberg well-definedness for persuasion")
    print(f"  games to Section 10.2, making the cross-reference accurate.")


if __name__ == "__main__":
    main()
