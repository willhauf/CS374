# Environment for NvN peg puzzle

# generate start state for a puzzle with n pegs per color
def start_state(n):
    return tuple([1] * n + [0] + [2] * n + [n])


# Generates the available actions for a given state
def actions(state):
    empty = state[-1]
    # move tile two spaces away from empty space into it
    if empty > 1 and state[empty - 1] != state[empty - 2]:
        yield empty - 2
    if empty < len(state) - 3 and state[empty + 1] != state[empty + 2]:
        yield empty + 2

    # move tile on either side of empty space into it
    if empty > 0:
        yield empty - 1
    if empty < len(state) - 2:
        yield empty + 1

# Generates successor state from given state and action
def successor(state, action):
    s = list(state)
    empty = state[-1]
    s[empty] = s[action]
    s[action] = 0
    s[-1] = action
    return tuple(s)

# Checks if the state is the goal state
def is_goal(state):
    n = (len(state) - 2) // 2
    return state[:n] == (2,) * n and state[n] == 0

# Distance Heuristic
def h(state):
    n = (len(state) - 2) // 2
    ones, twos= n+1, 0
    moves = 0
    for i in range(2 * n + 1):
        peg = state[i]
        if peg == 1:
            moves += abs(i - ones) // 2 + abs(i - ones) % 2
            ones += 1
        elif peg == 2:
            moves += abs(i - twos) // 2 + abs(i - twos) % 2
            twos += 1

    return moves
