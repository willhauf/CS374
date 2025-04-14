# Environment for n-queens puzzle
from random import shuffle, randint

#returns a column permutation
def rand_state(n):
    state = list(range(n))
    shuffle(state)
    return state

# Print state in grid format
def display(state):
    for col in state:
        before = col
        after = len(state) - col - 1
        print(" :: "*before + "Q " + " :: "*after+"\n")


# Generates the actions for a given state
def actions(state):
    n = len(state)
    for r1 in range(n):
        for r2 in range(r1 + 1, n):
            yield r1, r2

# generate random action with more efficiency
def rand_action(state):
    n = len(state)
    r1 = randint(0, n-1)
    r2 = randint(0, n - 1)
    while r2 == r1:
        r2 = randint(0, n - 1)
    return r1, r2


# Move to next state
def take(state, action):
    r1, r2 = action
    state[r1], state[r2] = state[r2], state[r1]

def take_back(state, action):
    r1, r2 = action
    state[r1], state[r2] = state[r2], state[r1]

# Returns the number of attacking pairs (only considers diagonals)
def h(state):
    n = len(state)
    conflicts = 0

    for r1 in range(n):
        c1 = state[r1]

        for r2 in range(r1+1, n):
            c2 = state[r2]

            if c1 == c2 or abs(c1 - c2) == abs(r1 - r2):
                conflicts += 1

    return conflicts




