# Minimax game players
from math import inf
from random import randint

from environment import utility, actions, max_successor, min_successor

# Returns the best value and action for the max player
def max_value(state, alpha, beta):
    u = utility(state)
    if u is not None:
        return u, None

    best_value, best_action = -inf, None
    for action in actions(state):
        value, _ = min_value(max_successor(state, action), alpha, beta)
        if value > best_value:
            best_value, best_action = value, action
            alpha = max(alpha, best_value)
        if best_value >= beta:
            break

    return best_value, best_action

def min_value(state, alpha, beta):
    u = utility(state)
    if u is not None:
        return u, None

    best_value, best_action = +inf, None
    for action in actions(state):
        value, _ = max_value(min_successor(state, action), alpha, beta)
        if value < best_value:
            best_value, best_action = value, action
            beta = min(beta, best_value)
        if best_value <= alpha:
            break

    return best_value, best_action

# Return the  best action for the current player
def minimax_action(state, turn):
    if turn % 2 == 0:
        _, action = max_value(state, alpha=-inf, beta=+inf)
    else:
        _, action = min_value(state, alpha = -inf, beta = +inf)

    return action

def rand_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)




