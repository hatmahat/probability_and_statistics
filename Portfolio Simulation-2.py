import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
Portfolio Simulation - Part I
"""

def portfolio_return(yrs, avg_return, volatility, principal):
    rates = np.random.normal(
        loc=avg_return,
        scale=volatility,
        size=principal
    )

    end_return = principal
    for x in rates:
        end_return *= (1+x)
    return end_return
    

sims, rets = 1000, []
for i in range(sims):
    rets.append(portfolio_return(
        yrs=10,
        avg_return=.07,
        volatility=.3,
        principal=10000
    ))

lower_ci = np.percentile(rets, 2.5) 
upper_ci = np.percentile(rets, 97.5)
u_795 = np.percentile(rets, 75)
print("95% CI of Returns: Lower = {}, Upper = {}".format(lower_ci, upper_ci))