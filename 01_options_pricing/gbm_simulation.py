import numpy as np
import matplotlib.pyplot as plt

S0 = 100                    #starting stock price
r = 0.05                    #risk-free interest
sigma = 0.20                #volatility
T = 1                       #time, years

n_simulations = 100000      #number of simulations

Z = np.random.normal(0, 1, n_simulations)  #standard normal distribution

ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

print("Average future share price:", np.mean(ST))
print("Lowest future share price:", np.min(ST))
print("Highest future share price:", np.max(ST))

plt.hist(ST, bins=30, edgecolor="black")

plt.title("Distribution of Simulated Future Share Prices")
plt.xlabel("Share Price (£)")
plt.ylabel("Frequency")

plt.show()