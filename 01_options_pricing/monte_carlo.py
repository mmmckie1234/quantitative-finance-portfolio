import numpy as np

S0 = 100
K = 100
r = 0.05
sigma = 0.20
T = 1

n_simulations = 100_000

Z = np.random.normal(0, 1, n_simulations)

ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z)

payoffs = np.maximum(ST - K, 0)

average_payoff = np.mean(payoffs)

option_price = np.exp(-r * T) * average_payoff

print("Average future share price:", round(np.mean(ST), 4))
print("Average option payoff:", round(average_payoff, 4))
print("Monte Carlo option price:", round(option_price, 4))