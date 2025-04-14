# Environment for our nxn tile puzzles
from math import sqrt


# Provides some test puzzles
def start_state(difficulty):
    if difficulty == "easy": # Shortest path length is 32
        return 8, 0, 6, 5, 4, 7, 2, 3, 1, 1
    elif difficulty == "medium": # Shortest path length is 24
        return 4, 1, 2, 3, 0, 9, 7, 6, 8, 5, 10, 11, 12, 13, 14, 15, 4
    elif difficulty == "hard": # Shortest path length is 81
        return 15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 5, 1, 3, 7, 4, 0, 15


# Generates the available actions for a given state
def actions(state):
    n = int(sqrt(len(state)))

    empty = state[-1]
    row = empty // n
    col = empty % n

    if row > 0:
        yield empty - n # index of tile above us
    if row < n - 1:
        yield empty + n # index of tile below us
    if col > 0:
        yield empty - 1 # index of tile to the left of us
    if col < n - 1:
        yield empty + 1 # index of tile to the right of us

# Creates the next state
def successor(state, action):
    s = list(state)
    empty = state[-1]
    s[empty] = s[action]
    s[action] = 0
    s[-1] = action
    return tuple(s)

def is_goal(state):
    for i in range(len(state) - 1):
        if i != state[i]:
            return False
    return True


# manhattan distance heuristic
def h(state):
    total = 0
    n = int(sqrt(len(state)))

    for i in range(len(state)-1):
        if state[i] != 0:
            this_row = i // n
            goal_row = state[i] // n
            total += abs(goal_row - this_row)

            this_col = i % n
            goal_col = state[i] % n
            total += abs(goal_col- this_col)
            
    return total
