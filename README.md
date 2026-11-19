# Quantitative Finance Portfolio

## Overview

This project explores the mathematical and computational methods used to price financial derivatives, with a particular focus on European options.

The aim is to implement and compare three approaches to option pricing:

1. **Black-Scholes Model** – an analytical solution providing a theoretical benchmark for European option prices.
2. **Monte Carlo Simulation** – a stochastic numerical method that estimates option prices by simulating possible future asset prices.
3. **Finite Difference Methods** – numerical techniques for solving the Black-Scholes partial differential equation.

The project combines financial mathematics, probability theory, numerical analysis and Python programming to investigate how different pricing methods work and how their accuracy and computational efficiency compare.

## Mathematical Background

The project focuses on European call options.

A European call option gives its holder the right, but not the obligation, to purchase an underlying asset at a predetermined strike price at the option's expiry date.

The payoff at expiry is:

$$
C_T = \max(S_T-K,0)
$$

where:

- $S_T$ is the underlying asset price at expiry.
- $K$ is the strike price.

The objective is to estimate the fair value of this payoff today.

The project uses the following market parameters:

| Symbol | Description |
|---|---|
| $S_0$ | Current underlying asset price |
| $K$ | Option strike price |
| $T$ | Time to expiry |
| $r$ | Risk-free interest rate |
| $\sigma$ | Asset price volatility |

## Methods

### 1. Black-Scholes Analytical Model

The Black-Scholes model provides a closed-form solution for pricing European options under a set of mathematical assumptions.

For a European call option on a non-dividend-paying asset:

$$
C = S_0N(d_1)-Ke^{-rT}N(d_2)
$$

where:

$$
d_1 =
\frac{\ln(S_0/K)+(r+\frac{1}{2}\sigma^2)T}
{\sigma\sqrt{T}}
$$

$$
d_2=d_1-\sigma\sqrt{T}
$$

This method will provide a benchmark against which the numerical methods can be evaluated.

### 2. Monte Carlo Simulation

Monte Carlo simulation estimates an option's value by generating a large number of possible future asset prices.

The project models asset prices using Geometric Brownian Motion (GBM):

$$
S_T=S_0\exp\left[
(r-\frac{1}{2}\sigma^2)T+\sigma\sqrt{T}Z
\right]
$$

where $Z$ is a standard normally distributed random variable.

For each simulation, the option payoff is calculated. The average payoff is then discounted to its present value:

$$
C \approx e^{-rT}\frac{1}{N}
\sum_{i=1}^{N}\max(S_{T,i}-K,0)
$$

where $N$ is the number of simulations.

### 3. Finite Difference Methods

The finite difference approach numerically solves the Black-Scholes partial differential equation:

$$
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2S^2
\frac{\partial^2V}{\partial S^2}
+rS\frac{\partial V}{\partial S}
-rV=0
$$

The aim is to investigate numerical methods for approximating the solution, including their stability, accuracy and convergence.

## Current Implementation

The following components have been implemented:

- Simulation of future asset prices using Geometric Brownian Motion.
- Generation and visualisation of individual simulated price paths.
- Generation of multiple simulated price paths.
- Monte Carlo estimation of European call option prices.

Further development will include the analytical Black-Scholes implementation, finite difference methods and a systematic comparison of the three approaches.

## Technologies

- **Python** – primary programming language.
- **NumPy** – numerical computation and random number generation.
- **SciPy** – statistical functions and mathematical calculations.
- **Matplotlib** – data visualisation.

## Project Structure

```text
quantitative-finance-portfolio/
│
├── README.md
│
├── 01_options_pricing/
│   ├── gbm_simulation.py
│   ├── gbm_paths.py
│   ├── multiple_gbm_paths.py
│   └── monte_carlo.py
│
├── 02_analysis/
│
└── requirements.txt
```

## Future Development

Planned extensions include:

- Implementing the Black-Scholes analytical pricing formula.
- Implementing finite difference methods to solve the Black-Scholes PDE.
- Investigating Monte Carlo convergence as the number of simulations increases.
- Analysing the effect of volatility, strike price and time to expiry on option prices.
- Comparing pricing accuracy and computational efficiency across all three methods.
- Producing visualisations of numerical results.

## Objective

The overall objective is to develop a deeper understanding of quantitative finance through the practical implementation of mathematical models and numerical methods, while producing a reproducible Python project demonstrating analytical problem-solving and computational skills.
