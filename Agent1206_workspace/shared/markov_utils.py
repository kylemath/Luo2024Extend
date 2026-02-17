"""
Shared utilities for the Markov reputation game simulation framework.
Used by all subagent scripts.
"""

import numpy as np
from typing import Tuple, Optional, Dict


class MarkovChain:
    """2-state Markov chain for the deterrence game."""

    def __init__(self, alpha: float = 0.3, beta: float = 0.5):
        """
        Parameters
        ----------
        alpha : float
            Pr(B | G) — probability of transitioning from Good to Bad
        beta : float
            Pr(G | B) — probability of transitioning from Bad to Good
        """
        self.alpha = alpha
        self.beta = beta
        self.states = ['G', 'B']
        self.n_states = 2

        # Transition matrix: T[i,j] = Pr(state j | state i)
        # Row 0 = G, Row 1 = B
        self.T = np.array([
            [1 - alpha, alpha],   # From G
            [beta, 1 - beta]      # From B
        ])

        # Stationary distribution
        self.pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])

        # Lifted state space: (theta_t, theta_{t-1})
        # Order: (G,G), (G,B), (B,G), (B,B)
        self.lifted_states = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.n_lifted = 4

        # Lifted stationary distribution
        self.rho_tilde = np.array([
            self.pi[0] * (1 - alpha),   # (G,G): pi(G) * Pr(G|G)
            self.pi[1] * beta,          # (G,B): pi(B) * Pr(G|B)
            self.pi[0] * alpha,         # (B,G): pi(G) * Pr(B|G)
            self.pi[1] * (1 - beta)     # (B,B): pi(B) * Pr(B|B)
        ])

    def simulate(self, T: int, theta_0: Optional[int] = None,
                 rng: Optional[np.random.Generator] = None) -> np.ndarray:
        """Simulate T steps of the Markov chain.

        Returns array of states (0=G, 1=B) of length T.
        """
        if rng is None:
            rng = np.random.default_rng()
        if theta_0 is None:
            theta_0 = rng.choice(2, p=self.pi)

        states = np.zeros(T, dtype=int)
        states[0] = theta_0
        for t in range(1, T):
            states[t] = rng.choice(2, p=self.T[states[t - 1]])
        return states

    def lifted_sequence(self, states: np.ndarray) -> np.ndarray:
        """Convert state sequence to lifted state indices.

        Lifted state index: (theta_t, theta_{t-1}) ->
          (G,G)=0, (G,B)=1, (B,G)=2, (B,B)=3
        Returns array of length len(states)-1 (starts at t=1).
        """
        lifted = np.zeros(len(states) - 1, dtype=int)
        for t in range(1, len(states)):
            lifted[t - 1] = states[t] * 2 + states[t - 1]
        return lifted


class DeterrenceGame:
    """The deterrence game from the paper's worked example."""

    def __init__(self, x: float = 0.3, y: float = 0.4):
        """
        Payoffs: u1(G, A) = 1, u1(G, F) = x, u1(B, A) = y, u1(B, F) = 0
        Supermodular when x + y < 1.
        """
        self.x = x
        self.y = y
        self.is_supermodular = (x + y < 1)

        self.actions = ['A', 'F']  # Acquiesce, Fight
        self.n_actions = 2

        # Payoff matrix: u1[state, action]
        # state: 0=G, 1=B; action: 0=A, 1=F
        self.u1 = np.array([
            [1.0, x],    # State G
            [y, 0.0]     # State B
        ])

    def stackelberg_strategy(self, state: int) -> int:
        """Deterministic Stackelberg: A in G, F in B."""
        return 0 if state == 0 else 1  # A=0, F=1


class BayesianFilter:
    """HMM Bayesian filter for SR player beliefs about the state."""

    def __init__(self, mc: MarkovChain, prior: Optional[np.ndarray] = None):
        self.mc = mc
        if prior is None:
            self.belief = mc.pi.copy()
        else:
            self.belief = prior.copy()

    def predict(self) -> np.ndarray:
        """One-step prediction: belief about theta_t given h_{t-1}."""
        return self.mc.T.T @ self.belief

    def update(self, signal: int, strategy_matrix: np.ndarray) -> np.ndarray:
        """
        Bayesian update given observed signal (action).

        Parameters
        ----------
        signal : int
            Observed action (0=A, 1=F)
        strategy_matrix : np.ndarray
            strategy_matrix[state, action] = Pr(action | state)

        Returns updated belief about theta_t.
        """
        # Predict
        predicted = self.predict()

        # Likelihood: Pr(signal | state) for each state
        likelihood = strategy_matrix[:, signal]

        # Update
        posterior = predicted * likelihood
        total = posterior.sum()
        if total > 0:
            posterior /= total
        else:
            posterior = self.mc.pi.copy()

        self.belief = posterior
        return posterior.copy()

    def reset(self, prior: Optional[np.ndarray] = None):
        if prior is None:
            self.belief = self.mc.pi.copy()
        else:
            self.belief = prior.copy()


def make_strategy_matrix(strategy_fn, n_states: int = 2,
                         n_actions: int = 2) -> np.ndarray:
    """Convert a deterministic strategy function to a probability matrix.

    Returns matrix[state, action] = Pr(action | state).
    """
    mat = np.zeros((n_states, n_actions))
    for s in range(n_states):
        a = strategy_fn(s)
        mat[s, a] = 1.0
    return mat


def tv_distance(p: np.ndarray, q: np.ndarray) -> float:
    """Total variation distance between two distributions."""
    return 0.5 * np.abs(p - q).sum()


def kl_divergence(p: np.ndarray, q: np.ndarray, eps: float = 1e-12) -> float:
    """KL divergence D(p || q) with numerical safeguard."""
    p_safe = np.clip(p, eps, 1.0)
    q_safe = np.clip(q, eps, 1.0)
    return np.sum(p_safe * np.log(p_safe / q_safe))


def save_figure(fig, path: str, dpi: int = 150):
    """Save matplotlib figure and close it."""
    fig.savefig(path, dpi=dpi, bbox_inches='tight')
    import matplotlib.pyplot as plt
    plt.close(fig)
    return path
