import numpy as np 

lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000
chance_of_winning = 1/num_tickets
size = 2000 # simulation sze

# antara hilang 10 usd atau menang dikurang 10 usd
payoffs = [-lottery_ticket_cost, grand_prize - lottery_ticket_cost]
# probabilitas kalah dan menang
probs = [1 - chance_of_winning, chance_of_winning]

outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

answer = outcomes.mean()
print("Average payoff from {} simulations = {}".format(size, answer))
print(outcomes.count(-10))
print(outcomes.count(grand_prize-lottery_ticket_cost))