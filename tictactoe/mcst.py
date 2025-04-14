# Monte Carloe Tree Search
from environment import utility, actions, max_successor, min_successor
from math import sqrt, log, inf
from random import choice
from time import time


# Represents a node in the game tree
class Node(object):
    def __init__(self, state, turn, parent=None):
        self.state = state
        self.turn = turn
        self.parent = parent
        self.utility = utility(state)
        self.children = dict() # action -> successor
        self.wins = 0
        self.playouts = 0

# computes UCB1 score for a node
def ucb1(node):
    if node.playouts == 0:
        return inf
    else:
        return (node.wins / node.playouts) + 2 * sqrt(log(node.parent.playouts) / node.playouts)

# Select a Node to expand
def select(node):
    if len(node.children) == 0:
        return node
    else:
        best_child = max(node.children.values(), key = ucb1)
        return select(best_child)

# Grows the game tree and randomly selects one of the new nodes
def expand(node):
    if node.utility is not None:
        return node

    for action in actions(node.state):
        if node.turn % 2 == 0:
            state = max_successor(node.state, action)
        else:
            state = min_successor(node.state, action)

        child = Node(state, node.turn + 1, node)
        node.children[action] = child

    return choice(list(node.children.values()))

# performs a random playout
def simulate(node):
    state = node.state
    outcome = node.utility
    turn = node.turn

    while outcome is None:
        action = choice(list(actions(state)))

        if node.turn % 2 == 0:
            state = max_successor(node.state, action)
        else:
            state = min_successor(node.state, action)

        outcome = utility(state)
        turn += 1

    return outcome

# Updates stats in the game tree
# NOTE: for tic-tac-toe we count ties as wins
def backpropagate(node, outcome):

    while node is not None:
        if node.turn % 2 == 0 and outcome <= 0:
            node.wins += 1
        elif node.turn % 2 == 1 and outcome >= 0:
            node.wins += 1

        node.playouts += 1
        node = node.parent

# chooses an action with MCTS
def mcts_action(state, turn, time_limit):
    root = Node(state, turn)
    start_time = time()

    while time() - start_time < time_limit:
         node = select(root)
         node = expand(node)
         outcome = simulate(node)
         backpropagate(node, outcome)

    return max(root.children.keys(), key=lambda a: root.children[a].playouts)