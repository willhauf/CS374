# Greedy Heuristic puzzle solver
from environment import actions, successor, is_goal, h
from heapdict import heapdict

def greedy_search(puzzle):
    priority = heapdict({puzzle: h(puzzle)})
    reached = {puzzle: None}
    path_cost = {puzzle: 0}

    while len(priority) > 0:
        state, value = priority.popitem()

        if is_goal(state):
            path = [state]
            while path[-1] != puzzle:
                path.append(reached[path[-1]])
            return path[::-1]

        for action in actions(state):
            s = successor(state, action)
            pc = path_cost[state] + 1 # assuming equal cost actions

            if s not in reached or pc < path_cost[s]:
                path_cost[s] = pc
                reached[s] = state
                priority[s] = h(s)
