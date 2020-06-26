import numpy as np

# Monte Carlo Integration
def sim_integrate(func, xmin, xmax, sims):
    x = np.random.uniform(xmin, xmax, sims)
    y = np.random.uniform(min(min(func(x)), 0), max(func(x)), sims)
    area = (max(y) - min(y))*(xmax - xmin)
    result = area * sum(abs(y) < abs(func(x)))/sims
    return result

result = sim_integrate(func = lambda x: x*np.exp(x), xmin = 0, xmax = 1, sims = 50)
print("Simulated answer = {}, Actual Answer = 1".format(result))

# Calculating the value of pi
sims, circle_points = 10000, 0

for i in range(sims):
    point = np.random.uniform(-1, 1, 2)

    within_circle = point[0]**2 + point[1]**2 <= 1
    if within_circle == True:
        circle_points += 1

pi_sim = 4*circle_points/sims
print('Simulated value of pi = {}'.format(pi_sim))