from collections import defaultdict
from random import random, choice
import numpy as np


class QLearner(object):
    def __init__(self, alpha, gamma, epsilon, decay, feature_size=14):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.decay = decay
        self.feature_size = feature_size # may change later if feature size changes.  mine is 13 as of now
        self.action_size = 4 # up down left right
        self.weights = np.zeros(self.feature_size * self.action_size)  # one weight per state-action pair

    def q_value(self, s, a):
        # compute Q-value for a given state s and action a
        feature_vector = self.feature_vector(s, a)

        # computes dot product of weights and feature vector giving us the Q-value for the state-action pair
        return np.dot(self.weights, feature_vector)

    def choose(self, s, actions):
        if random() < self.epsilon: # exploration by trying new actions
            return choice(actions)
        else:   # exploitation using known Q-values
            return max(actions, key=lambda a: self.q_value(s, a))

    def update(self, s, a, r, sp, actions, terminal):
        if terminal:
            reward = r
            self.epsilon *= self.decay
        else:
            reward = r + self.gamma * max(self.q_value(sp, ap) for ap in actions)  # Max Q-value for next state

        # calculate the temporal difrerence error and update weights
        delta = reward - self.q_value(s, a)
        self.weights += self.alpha * delta * self.feature_vector(s, a)

    def feature_vector(self, s, a):
        # initialize vector of length feature_size * action_size to zeros
        features = np.zeros(self.feature_size * self.action_size)

        # calculate offset for the action's section in the feature vector
        index = a * self.feature_size

        # Encode the state features in the feature vector
        features[index:index + self.feature_size] = s  # Encode state features in the action's section

        return features