import numpy as np

sims, lottery_ticket_cost = 3000, 0
grand_prize = 1000000
chance_of_winning = 1/1000


while True:
    outcomes = np.random.choice(
        [-lottery_ticket_cost, grand_prize - lottery_ticket_cost],
        size=sims,
        p=[1 - chance_of_winning, chance_of_winning],
        replace=True
        )

    if outcomes.mean() < 0:
        break
    else:
        lottery_ticket_cost += 1

answer = lottery_ticket_cost - 1
print(print("Average payoff from {} simulations = {}".format(size, answer)))
    
