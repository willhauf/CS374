# BFS puzzle solver
from environment import actions, successor, is_goal
from collections import deque

def breadth_first_search(puzzle):
    if is_goal(puzzle):
        return [puzzle]

    frontier = deque([puzzle])
    reached = {puzzle: None}

    while len(frontier) > 0:
        state = frontier.popleft()

        for action in actions(state):
            s = successor(state, action)

            if s not in reached:
                reached[s] = state
                frontier.append(s)

                # get path to solution and return it
                if is_goal(s):
                    path = [s]
                    while path[-1] != puzzle:
                        path.append(reached[path[-1]])
                    return path[::-1]



