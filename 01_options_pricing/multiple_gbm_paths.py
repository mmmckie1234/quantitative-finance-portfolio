import numpy as np
import matplotlib.pyplot as plt

S0 = 100
r = 0.05
sigma = 0.20
T = 1

n_days = 252
n_simulations = 1000

dt = T / n_days

Z = np.random.normal(0, 1, (n_simulations, n_days))

S = np.zeros((n_simulations, n_days + 1))

S[:, 0] = S0

for t in range(1, n_days + 1):
    S[:, t] = S[:, t-1] * np.exp(
        (r - 0.5 * sigma**2) * dt
        + sigma * np.sqrt(dt) * Z[:, t-1])

plt.plot(S.T)

plt.title("10 Simulated Share Price Paths")
plt.xlabel("Trading Day")
plt.ylabel("Share Price (£)")

plt.show()
