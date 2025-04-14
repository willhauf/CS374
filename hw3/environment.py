# Environment for the game of tic-tac-toe

def start_state():
    return 0, 0, 0, 0, 0, 0, 0, 0, 0

# Generate the available actions
def actions(state):
    for i in range(9):
        if state[i] == 0:
            yield i

# Returns the state reached by placing x and o
def max_successor(state, action):
    s = list(state)
    s[action] = 1
    return tuple(s)

def min_successor(state, action):
    s = list(state)
    s[action] = -1
    return tuple(s)

# returns the minimax utility
def utility(state):
    # 1 if X wins
    # -1 if O wins
    #0 if tie
    # None if still playing
    lines = {
        state[0:3], state[3:6], state[6:9], # rows
        state[0:7:3], state[1:8:3], state[2:9:3], # columns
        state[0:9:4], state[2:7:2] # diagonals
    }

    if (1, 1, 1) in lines:
        return 1 # X wins
    elif (-1, -1, -1) in lines:
        return -1 # O wins
    elif 0 not in state:
        return 0 # tie
    else:
        return None # still playing

utility((1, -1, 1, -1, -1, 1, 1, -1, 1))

