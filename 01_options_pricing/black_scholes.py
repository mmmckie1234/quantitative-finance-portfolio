import numpy as np
from scipy.stats import norm

#Option parameters
S0 = 100        #Starting share price
K = 100         #Strike price
r = 0.05        #Risk-free interest rate, 5%
sigma = 0.20    #Volatitiy, 20%
T = 1           #Time in years

# Calculate d1 and d2
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

# Calculate the Black-Scholes European call price
call_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# Print the theoretical option price
print("Black-Scholes Call Price:", round(call_price, 4))
