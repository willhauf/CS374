# Hill-Climbing puzzle solver
from environment import actions, h, take, take_back


def hill_climb(state):
    steps = 0

    while True:
        best_height = -h(state)
        best_action = None

        for action in actions(state):
            take(state, action)
            height = -h(state)

            if height > best_height:
                best_height = height
                best_action = action

            take_back(state, action)

        if best_action is not None:
            take(state, best_action)
            steps += 1
        else:
            return steps


