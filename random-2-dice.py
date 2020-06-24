import numpy as np

die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
outcomes = np.random.choice(die, size=num_dice, p=probabilities)

if outcomes[0] == outcomes[1]:
    answer = 'win'
else:
    answer = 'lose'

print('The dice show {} and {}. You {}!'.format(outcomes[0], outcomes[1], answer))
