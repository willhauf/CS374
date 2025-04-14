# Standard Q-learning agent
from collections import defaultdict
from random import random, choice


class QLearner(object):
    def __init__(self, alpha, gamma, epsilon, decay):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.decay = decay
        self.q = defaultdict(float) # Values default 0

    def choose(self, s, actions):
        if random() < self.epsilon:
            return choice(actions)
        else:
            return max(actions, key = lambda a: self.q[(s, a)]) # chooses action with best q-value

    def update(self, s, a, r, sp, actions, terminal):
        if terminal:
            reward = r
            self.epsilon *= self.decay
        else:
            reward = r + self.gamma * max(self.q[(sp, ap)] for ap in actions)

        self.q[(s, a)] = self.alpha * reward + (1 - self.alpha) * self.q[(s, a)]
        
