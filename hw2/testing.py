# Min-conflicts solver for n-queens puzzles.
from environment import h, display
from random import randint, choice


def greedy_conflicts(state, row):
    n = len(state)
    conflicts = [0]*n
    for i in range(row):
        queen = state[i]
        conflicts[queen] += 1
        d_left = queen - (row - i)
        d_right = queen + (row - i)

        if d_left >= 0:
            conflicts[d_left] += 1
        if d_right < n:
            conflicts[d_right] += 1

    return conflicts

# Constructs a greedy start state for n queens.
def greedy_state(n):
    state = [0]*n
    state[0] = randint(0, n-1)
    for i in range(1, n):
        conflicts = greedy_conflicts(state, i)
        choice = random_min_index(conflicts)
        state[i] = choice
    return state # Your answer

# returns an array with the number of conflicts each queen has
def get_conflicts(state):
    n = len(state)
    conflicts = [0] * n  # Initialize conflict count for each queen

    for row1 in range(n):
        col1 = state[row1]
        for row2 in range(n):
            if row2 == row1:
                continue  # Skip self-comparison
            col2 = state[row2]

            # Check for conflicts
            if col2 == col1 or abs(row2 - row1) == abs(col2 - col1):
                conflicts[row1] += 1  # Increase conflict count for this queen

    return conflicts

# returns the number of conflicts each possible location in a row has
def row_conflicts(state, row):
    n = len(state)
    conflicts = [0] * n
    for col in range(n):
        # queen state[row] = col
        for row2 in range(n):
            if row2 == row:
                continue
            col2 = state[row2]
            if col == col2 or abs(row2 - row) == abs(col2 - col):
                conflicts[col] += 1

    return conflicts



def random_min_index(lst):
    min_value = min(lst)  # Find the minimum value
    min_indices = [i for i, val in enumerate(lst) if val == min_value]  # Get all indices with min value
    return choice(min_indices)

# Attempts to minimize conflicts and returns the number of steps taken.
def minimize_conflicts(state, max_steps=100):
    steps = 0
    n = len(state)

    while h(state) > 0 and steps < max_steps:
        # choose queen with conflicts
        conflicts = get_conflicts(state)
        queen = max(range(n), key=lambda q: conflicts[q])

        # switch that queen to a location that produces the least conflicts
        # options1 = [0]*n
        # for col in range(n):
        #     state[queen] = col
        #     options1[col] = h(state)

        options = row_conflicts(state, queen)

        state[queen] = random_min_index(options)
        steps += 1

    return steps

# Repeats the min-conflicts algorithm until it arranges n queens.
def solve(n):
    while True:
        state = greedy_state(n)
        steps = minimize_conflicts(state)
        print("Size", n, "attempt stopped at", h(state), "conflicts after", steps, "steps.")
        if h(state) == 0:
            return state

# Tests
solve(16)
solve(32)
solve(64)
solve(128)
solve(256)

# grid = greedy_state(6)
# display(grid)
# minimize_conflicts(grid)

