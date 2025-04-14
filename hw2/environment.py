# Environment for n-queens puzzle
from random import shuffle, randint


# Print state in grid format
def display(state):
    for col in state:
        before = col
        after = len(state) - col - 1
        print(" :: "*before + " Q " + " :: "*after+"\n")

# generates list with numbers of conflicts each col in a row has
def get_conflicts(state, n):
    conflicts = [0] * n
    new_row = len(state) # row conflicts is being generated for

    for row in range(len(state)): # loop through all placed queen locations
        queen = state[row]

        if queen is None:
            return conflicts

        for col in range(n): # column loop
            if col in state or abs(new_row - row) == abs(queen - col):
                conflicts[col] += 1

def queens_conflicts(state):
    n = len(state)
    conflicts = [-1]*n

    for r1 in range(n):
        c1 = state[r1]

        for r2 in range(n):
            if r2 == r1:
                pass
            c2 = state[r2]

            if c1 == c2 or abs(c1 - c2) == abs(r1 - r2):
                conflicts[r1] += 1

    return conflicts

# generate random action with more efficiency
def rand_action(state):
    n = len(state)
    r1 = randint(0, n-1)
    r2 = randint(0, n - 1)
    while r2 == r1:
        r2 = randint(0, n - 1)
    return r1, r2



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




