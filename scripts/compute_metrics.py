import numpy as np

def calculate_var(returns):
    return np.percentile(returns.dropna(), 5)

def calculate_cvar(returns):
    var = calculate_var(returns)
    return returns[returns <= var].mean()

print("Metrics module loaded")