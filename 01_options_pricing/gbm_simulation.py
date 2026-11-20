import numpy as np
import matplotlib.pyplot as plt

#Optiom parameters
S0 = 100        #Starting share price 
r = 0.05        #Risk-free interest rate, 5%             
sigma = 0.20    ##Volatility, 20%            
T = 1           #Time in years                 

n_simulations = 100000  #Number of simulations

Z = np.random.normal(0, 1, n_simulations)   #Generates a random value for each simulation  

#Simulating future share prices
ST = S0 * np.exp((r - 0.5 * sigma**2) * T   #Drift component
                  + sigma * np.sqrt(T) * Z) #Volatility component


plt.hist(ST, bins=30, edgecolor="black")

plt.title("Distribution of Simulated Future Share Prices")
plt.xlabel("Share Price (£)")
plt.ylabel("Frequency")

plt.show()