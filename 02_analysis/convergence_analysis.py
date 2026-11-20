
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Option parameters
S0 = 100        #Starting share price
K = 100         #Strike price
r = 0.05        #Risk-free interest rate, 5%
sigma = 0.20    #Volatility, 20%
T = 1           #Time in years

#Number of simulations
N = 1_000_000

#Generate reproducible random numbers
rng = np.random.default_rng(42)
Z = rng.standard_normal(N)

#Simulate future share prices
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z)

#Calculate option payoffs
payoffs = np.maximum(ST - K, 0)

#Discount individual payoffs
discounted_payoffs = np.exp(-r * T) * payoffs

#Calculate Black-Scholes benchmark FIRST
d1 = (
    np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

bs_price = (
    S0 * norm.cdf(d1)
    - K * np.exp(-r * T) * norm.cdf(d2))

#Simulation sizes
simulation_sizes = [100, 1_000, 10_000, 100_000, 1_000_000]

#Store Monte Carlo prices
mc_prices = []

print("Black-Scholes price:", round(bs_price, 4))
print()

#Calculate convergence results
for n in simulation_sizes:

    sample = discounted_payoffs[:n]

    price = np.mean(sample)

    mc_prices.append(price)

    se = np.std(sample, ddof=1) / np.sqrt(n)

    lower = price - 1.96 * se
    upper = price + 1.96 * se

    error = abs(price - bs_price)

    print(
        f"N: {n:>10,} | "
        f"Price: £{price:.4f} | "
        f"SE: £{se:.4f} | "
        f"95% CI: [{lower:.4f}, {upper:.4f}] | "
        f"Error: £{error:.4f}"
    )

plt.figure(figsize=(10, 6))

plt.plot(
    simulation_sizes,
    mc_prices,
    marker="o",
    label="Monte Carlo estimate"
)

plt.axhline(
    y=bs_price,
    linestyle="--",
    label="Black-Scholes benchmark"
)

plt.xscale("log")
plt.xlabel("Number of simulations")
plt.ylabel("Option price (£)")
plt.title("Monte Carlo Convergence")
plt.legend()
plt.grid(True)

plt.show()
