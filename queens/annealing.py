# Simulated annealing puzzle solver
from environment import h, rand_action, take, take_back
from math import exp
from random import random


def sim_anneal(state, max_temp = 100.0, min_temp = 0.01, cooling_rate = 0.999):
    current_height = -h(state)
    temperature = max_temp
    steps = 0

    while temperature > min_temp and current_height < 0:
        action = rand_action(state)
        take(state, action)

        height = -h(state)
        probability = exp((height - current_height) / temperature)
        temperature *= cooling_rate

        if height > current_height or random() < probability:
            current_height = height
            steps += 1
        else:
            take_back(state, action)

    return steps