import numpy as np

#Option parameters
S0 = 100        #Starting share price
K = 100         #Strike price
r = 0.05        #Risk-free interest rate, 5%
sigma = 0.20    #Volatility, 20%
T = 1           #Time in years

n_simulations = 100_000     #Number of simulations

Z = np.random.normal(0, 1, n_simulations)   #Generates a random value for each simulation

#Simulates the share price one day at a time using GBM
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T    #Drift component
    + sigma * np.sqrt(T) * Z)   #Volatility component

#Calculating option payoffs
payoffs = np.maximum(ST - K, 0)
average_payoff = np.mean(payoffs)

#Discounting the payoff to today's value
option_price = np.exp(-r * T) * average_payoff

print("Average future share price:", round(np.mean(ST), 4))
print("Average option payoff:", round(average_payoff, 4))
print("Monte Carlo option price:", round(option_price, 4))