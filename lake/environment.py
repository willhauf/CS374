# THE FrozenLake RL environment
from random import random

class FrozenLake(object):
    def __init__(self):
        self.rows = 4
        self.cols = 4
        self.current = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)
        self.holes = {(1, 1), (1, 3), (2, 3), (3, 0)}
        self.actions = [0., 1, 2, 3]

    # Prepare the state for an episode
    def reset(self):
        self.current = (0, 0)
        return self.state()

    # Return the current state
    def state(self):
        (r, c) = self.current
        return self.cols * r + c

    # apply an action
    def step(self, a):
        # Slipping
        p = random()
        if p < .15:
            a = (a + 1) % len(self.actions) # adding one is going counter-clockwise
        elif p < .30:
            a = (a - 1) % len(self.actions) # subtracting on eins going clockwise

        # Movement
        reward = 0
        (r, c) = self.current
        if a == 0 and r > 0:
            self.current = (r - 1, c) # up
            reward = -1
        elif a == 1 and c > 0:
            self.current = (r, c - 1) # left
            reward = -1
        elif a == 2 and r < self.rows - 1:
            self.current = (r + 1, c) # down
            reward = 1
        elif a == 3 and c < self.cols - 1:
            self.current = (r, c + 1) # right
            reward = 1

        # Endings
        terminal = False
        if self.current in self.holes:
            reward = -10
            terminal = True
        elif self.current == self.goal:
            reward = 10
            terminal = True

        # Results
        return reward, self.state(), terminal