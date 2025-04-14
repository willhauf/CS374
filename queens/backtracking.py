# Backtracking solver for queens puzzle
from environment import h

# Finishes arrangement of n queens with backtracking
def complete(state, options, popularity):
    # base case
    if len(options) == 0:
        return state

    # assign a row
    r1 = min(options, key=lambda r: len(options[r]))
    columns = options.pop(r1)

    # Try options from least to most popular
    for c1 in sorted(columns, key=lambda c: popularity[c]):
        state[r1] = c1

        # Collect the conflicting options for other rows
        conflicts = {r: set() for r in options}
        for r2 in options:
            for c2 in [c1, (r2 - r1 + c1), (c1 - r2 + r1)]:
                if c2 in options[r2]:
                    conflicts[r2] .add(c2)

        # Remove conflicting options
        for r2 in options:
            for c2 in conflicts[r2]:
                options[r2].remove(c2)
                popularity[c2] -= 1

        # Try to complete the solution from here
        solution = complete(state, options, popularity)

        if solution is not None:
            return solution

        # undo the column choice before trying the next one
        state[r1] = None
        for r2 in options:
            for c2 in conflicts[r2]:
                options[r2].add(c2)
                popularity[c2] += 1

    # Undo row assignment to backtrack
    options[r1] = columns

# Begins an arrangements of n queens with backtracking
def solve(n):
    state = [None] * n
    options = {r: set(range(n)) for r in range(n)}
    popularity = {c: n for c in range(n)}
    complete(state, options, popularity)
    print("Size", n, "puzzle solved with", h(state), "conflicts.")




# tests
solve(16)
solve(32)
solve(64)
solve(128)