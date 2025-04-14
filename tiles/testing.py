# Testing for tile puzzle solvers
from environment import start_state
from bfs import breadth_first_search
from gh import greedy_search
from astar import astar_search
from time import time

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

def test(difficulty, search):
    print("Solving", difficulty, "puzzle...", end="")
    puzzle = start_state(difficulty)
    start_time = time()
    solution = search(puzzle)
    stop_time = time()
    solve_time = stop_time-start_time
    print("Found path of length", len(solution), "in", red(solve_time), "seconds.")


# print(bold("BFS Tests"))
# test("easy", breadth_first_search)
# test("medium", breadth_first_search)

print(blue(bold("GH Tests")))
test("easy", greedy_search)
test("medium", greedy_search)
test("hard", greedy_search)
brk()

print(blue(bold("A* Tests:")))
test("easy", astar_search)
test("medium", astar_search)
brk()

print(blue(bold("Weighted A* Tests:")))
test("easy", lambda s: astar_search(s, w=2))
test("medium", lambda s: astar_search(s, w=2))
test("hard", lambda s: astar_search(s, w=2))
brk()