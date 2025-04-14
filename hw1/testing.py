# Testing for the PegSwap assignment.
from environment import start_state
from tiles.bfs import breadth_first_search
from tiles.astar import astar_search
from time import time

def solve(size, search):
    print("Solving size", size, "puzzle...", end="")
    puzzle = start_state(size)
    start_time = time()
    solution = search(puzzle)
    stop_time = time()
    solve_time = stop_time - start_time
    print("found path of length", len(solution), "in", solve_time, "seconds.")

print("BFS testing:")
for n in range(2, 12, 2):
    solve(n, breadth_first_search)

print("A* testing:")
for n in range(2, 24, 2):
    solve(n, astar_search)