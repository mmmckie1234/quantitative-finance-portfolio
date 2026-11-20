import numpy as np
from scipy.stats import norm

#Option parameters
S0 = 100
K = 100
r = 0.05
sigma = 0.20
T = 1

n_simulations = 100_000

#Calculate d1 and d2 for the Black-Scholes formula
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

#Calculate the theoretical Black-Scholes call price
bs_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

#Generate random shocks from a standard normal distribution
Z = np.random.normal(0, 1, n_simulations)

#Simulate future share prices using GBM
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z)

#Calculate the payoff of the call option at maturity
payoffs = np.maximum(ST - K, 0)

#Calculate the average simulated payoff
average_payoff = np.mean(payoffs)

#Discount the expected payoff to today's value
mc_price = np.exp(-r * T) * average_payoff

#Calculate the absolute difference between the two prices
absolute_error = abs(mc_price - bs_price)

print("Black-Scholes price:", round(bs_price, 4))
print("Monte Carlo price:", round(mc_price, 4))
print("Absolute error:", round(absolute_error, 4))
