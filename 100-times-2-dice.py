import numpy as np

#np.random.seed(42)
die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
num_simulation, wins = 100, 0

for i in range(num_simulation):
    outcomes = np.random.choice(die, size=num_dice, p=probabilities)
    if outcomes[0] == outcomes[1]:
        wins += 1

print('In {} games, you win {} times'.format(num_simulation, wins))
