import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
Portfolio Simulation - Part I
"""
np.random.seed(123)
def portfolio_return(yrs, avg_return, sd_of_return, principal):
    rates = np.random.normal(
        loc=avg_return,
        scale=sd_of_return,
        size=yrs
    )
    end_return = principal
    for x in rates:
        end_return *= (1+x)
    return end_return

res = []
for i in range(5000): # nums simulations
    result = portfolio_return(
        yrs=5,
        avg_return=.07,
        sd_of_return=.15,
        principal=1000  
    )  
    print('Portfolio return after 5 years (sumulation: {}) = {}'.format(i, result))
    res.append(result)

np_res = np.sort(np.array(res))
profit = np_res[np_res >= 1000]
loss = np_res[np_res < 1000]

n_max, n_min, n_mean, n_std = np_res.max(), np_res.min(), np_res.mean(), np_res.std()
lower_ci = np.percentile(np_res, 2.5)
upper_ci = np.percentile(np_res, 97.5)
u_75 = np.percentile(np_res, 75)
print('lower percentile :', lower_ci)
print('upper percentile :', upper_ci)
print('75% percentile   :', u_75)
# print('profit array:', profit)
# print('profit array:', loss)
print('profit count:', profit.shape[0])
print('loss count:', loss.shape[0])
print('max  :', n_max)
print('min  :', n_min)
print('mean :', n_mean)
print('std  :', n_std)

plt.axvline(x=lower_ci)
plt.axvline(x=upper_ci)
plt.axvline(x=u_75)
plt.plot(np_res, (norm.pdf(np_res, n_mean, n_std)), '-')
#plt.hist(np_res, bins=30)
plt.show()