import numpy as np
import matplotlib.pyplot as plt

#Option parameters
S0 = 100        #Starting share price
r = 0.05        #Risk-free interest rate
sigma = 0.20    #Volatilty
T = 1           #Time in years

n_days = 252        #252 trading days in a year
dt = T / n_days     #252 time steps in a year

#Generates a random value for each day
Z = np.random.normal(0, 1, n_days)

#Creates a zero array
S = np.zeros(n_days + 1)

#Sets the initial value to the starting share price
S[0] = S0

#Simulates the share price one day at a time using GBM
for t in range(1, n_days + 1):
    #Calculates today's share price using yesterday's price and a daily random movement
    S[t] = S[t-1] * np.exp(
        (r - 0.5 * sigma**2) * dt           #Drift component
        + sigma * np.sqrt(dt) * Z[t-1])     #Volatility component

plt.plot(S)

plt.title("Simulated Share Price Path")
plt.xlabel("Trading Day")
plt.ylabel("Share Price (£)")

plt.show()