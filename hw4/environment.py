# THE FrozenLake RL environment
from random import random

class FrozenLake(object):
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.current = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)
        self.holes = self.random_holes()
        self.actions = [0, 1, 2, 3]

    def random_holes(self):
        # Randomly generate holes in the grid with a 10% chance of being a hole
        holes = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if random() < 0.1 and (r, c) != self.current and (r, c) != self.goal:
                    holes.add((r, c))
        return holes

    # Prepare the state for an episode
    def reset(self):
        self.current = (0, 0)
        self.holes = self.random_holes()
        return self.state()

    # Return the current state
    def state(self):
        (r, c) = self.current
        features = [1]*9
        neighbors = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]

        for i in range(len(neighbors)):
            if neighbors[i] in self.holes:
                features[i] = 0 # label all holes as 0's

        sides = [neighbors[0:3], neighbors[2:9:3], neighbors[6:9], neighbors[0:7:3]] # sides of the current state

        for side in sides:
            features += [1 if side[0] in self.holes else 0] # sum  sides to see how many holes.  larger number is safer

        return features + [1] # add constant feature to end

        # S HOLDS THE STATUS OF ALL NEIGHBORS

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

