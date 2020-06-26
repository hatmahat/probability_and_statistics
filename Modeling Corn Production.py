"""
Suppose that you manage a small corn farm and are interested in optimizing your costs. In this exercise, we will model the production of corn.

For simplicity, let's assume that corn production depends on only two factors: rain, which you don't control, and cost, which you control. Rain is normally distributed with mean 50 and standard deviation 15. For now, let's fix cost at 5,000. Corn produced in any season is a Poisson random variable while the average corn production is governed by the equation:

100×(cost)^0.1×(rain)^0.2
Let's model this production function and simulate one outcome.
"""
import numpy as np

# init var
cost = 5000
rain = np.random.normal(50, 15) # normal distributin mean = 50 abd std = 15

def corn_produced(rain, cost):
    mean_corn = 100*(cost**.1)*(rain**.2) # average corn production is governed by eq.
    corn = np.random.poisson(mean_corn)
    return corn

def corn_demand(price):
    mean_corn = 1000 - 8*price # average corn demand is giverned by eq.
    corn = np.random.poisson(abs(mean_corn))
    return corn

def profits(cost):
    rain = np.random.normal(50, 15)
    price = np.random.normal(40, 10)
    supply = corn_produced(rain, cost)
    demand = corn_demand(price)
    equil_short = demand >= supply
    if equil_short == True: # kalau untung
        tmp = supply*price - cost
        return tmp
    else:
        tmp2 = demand*price - cost
        return tmp2

corn_result = corn_produced(rain, cost)
print('Simulated Corn Production = {}'.format(corn_result))

result = profits(cost)
print('Simulated profit = {}'.format(result))

'''
Optimizing Costs
'''

# init
sims, results = 1000, {}
cost_levels = np.arange(100, 5100, 100)

for cost in cost_levels:
    tmp_profits = []
    for i in range(sims):
        tmp_profits.append(profits(cost))
    results[cost] = np.mean(tmp_profits)

cost_max = [x for x in results.keys() if results[x] == max(results.values())][0]
print('Average profit is maximized when cost = {}'.format(cost_max))