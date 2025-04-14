# Evaluation Function for tic-tac-toe
from environment import  actions, max_successor, min_successor, utility
from collections import Counter
from math import inf

def check_and_get_value(t):
    counts = Counter(x for x in t if x != 0)
    if len(counts) <= 1:
        return next(iter(counts), None)  # Return the single nonzero value or None
    return None

# returns a value from -1 to 1 to describe the state
def evaluation(state):
    # Number of possible winning lines (unblocked)
    f1 = 0 # MAX
    f2 = 0 # MIN
    # Number of rows 1 move away from winning
    f3 = 0  # MAX
    f4 = 0  # MIN

    lines = [
        state[0:3], state[3:6], state[6:9], # rows
        state[0:7:3], state[1:8:3], state[2:9:3], # columns
        state[0:9:4], state[2:7:2] # diagonals
    ]

    for line in lines:
        # val = sum(1 for x in line if x != 0) == 1
        val = sum(line)
        if val > 0 and 0 in line:
            f1 += 1
        elif val < 0 and 0 in line:
            f2 += 1
        if val == 2:
            f3 += 1
        elif val == -2:
            f4 += 1

    whos_turn = sum(state)
    min_wgt = 0
    max_wgt = 0
    if whos_turn == 0 or f3 > 1:
        # max goes next
        max_wgt = 3
    elif whos_turn == 1 or f4 > 1:
        # min goes next
        min_wgt = 3

    eval = (f1 - f2 + (max_wgt*f3) - (min_wgt*f4)) / 14

    if abs(eval) >= 1:
        print("Error: eval is greater than 1", eval)

    return eval

def max_value(state, alpha, beta, max_depth, min_depth):
    u = utility(state)
    if u is not None:
        return u, None

    if max_depth == 0 or min_depth == 0:
        return evaluation(state), None

    best_value, best_action = -inf, None
    for action in actions(state):
        value, _ = min_value(max_successor(state, action), alpha, beta, max_depth - 1, min_depth - 1)
        if value > best_value:
            best_value, best_action = value, action
            alpha = max(alpha, best_value)
        if best_value >= beta:
            break

    return best_value, best_action

def min_value(state, alpha, beta, max_depth, min_depth):
    u = utility(state)
    if u is not None:
        return u, None

    if max_depth == 0 or min_depth == 0:
        return evaluation(state), None

    best_value, best_action = +inf, None
    for action in actions(state):
        value, _ = max_value(min_successor(state, action), alpha, beta, max_depth - 1, min_depth - 1)
        if value < best_value:
            best_value, best_action = value, action
            beta = min(beta, best_value)
        if best_value <= alpha:
            break

    return best_value, best_action

# Return the  best action for the current player
def minimax_action(state, turn, max_depth, min_depth):
    if turn % 2 == 0:
        best_value, action = max_value(state, alpha=-inf, beta=+inf, max_depth=max_depth, min_depth=inf)
    else:
        best_value, action = min_value(state, alpha = -inf, beta = +inf, max_depth=inf, min_depth=min_depth)

    return best_value, action

def display(state):
    lines = [state[0:3], state[3:6], state[6:9]]
    for line in lines:
        p_line = []
        for char in line:
            if char < 0:
                p_line += 'O'
            elif char > 0:
                p_line += 'X'
            else:
                p_line += '-'
        print(p_line)

def testing():
    for i in range(1, 10):
        for j in range(1, 10):
            state = (0, 0, 0, 0, 0, 0, 0, 0, 0)
            displaying = True
            terminal = False
            turn = 0

            # print("\033[91mTrying Max Min combo \033[0m", i, j)

            while displaying:
                # Get player action (Replace this with your input method)
                _, action = minimax_action(state, turn, max_depth=i, min_depth=j)  # Assuming MCTS is used for moves

                # State update
                if action in actions(state):
                    if turn % 2 == 0:
                        state = max_successor(state, action)
                    else:
                        state = min_successor(state, action)

                    if utility(state) is not None:
                        terminal = True
                    else:
                        turn += 1

                # Exit if the game is over
                if terminal:
                    displaying = False

            # get utility of final state to see the outcome
            outcome = utility(state)
            # display(state)

            if outcome > 0:
                print("X won with depth ", i, "against depth ", j)
            elif outcome < 0:
                print("O won with depth ", j, "against depth ", i)
            elif outcome == 0:
                print("Tied with Max D", i, "and Min D", j)

testing()

# print(evaluation((-1, 1, 0, 0, 1,0, 1, -1, 0)))
# print(evaluation((-1, -1, 1, 0, 1, 1, 0, 0, 0)))
# print(evaluation((0, -1, -1, 0, 1, 0, 0, 1, 0)))