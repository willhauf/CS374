# Testing for the queens puzzler solvers>
from environment import rand_state, h
from queens.annealing import sim_anneal
from queens.climbing import hill_climb

def bold(s):
    return "\033[1m" + s + "\033[0m"

def brk():
    print("_"*75)

def red(text):
    return f"\033[31m{text}\033[0m"

def green(text):
    return f"\033[32m{text}\033[0m"

def yellow(text):
    return f"\033[33m{text}\033[0m"

def blue(text):
    return f"\033[34m{text}\033[0m"

def solve(n, search):
    while True:
        state = rand_state(n)
        steps= search(state)
        print("Size", n, "attempt stopped at", green(h(state)), "conflicts after", red(steps), "steps.")
        if h(state) == 0:
            return state

print(blue(bold("Hill Climbing tests:")))
solve(16, hill_climb)
solve(32, hill_climb)
solve(64, hill_climb)
# solve(128, hill_climb)
brk()

print(blue(bold("Simulated annealing tests:")))
solve(16, sim_anneal)
solve(32, sim_anneal)
solve(64, sim_anneal)
# solve(128, sim_anneal)
brk()

