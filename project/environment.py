# environment for the snake game
from random import randint
from collections import deque

class Snake(object):
    def __init__(self, rows=10, cols=10, speed=5):
        self.rows = rows
        self.cols = cols
        self.speed = speed
        self.direction = "RIGHT"
        self.body = deque([(1, 3), (2, 3), (3, 3)])
        self.directions = {"RIGHT": (1, 0), "LEFT": (-1, 0), "UP": (0, -1), "DOWN": (0, 1)}
        self.food = self.random_food()
        self.alive = True

    def __str__(self):
        return f"Snake(body={self.body}, head={self.body[-1]}, food={self.food}, direction={self.direction})"

    def random_food(self):
        """Generate random food position."""
        x, y = (randint(0, self.cols - 1), randint(0, self.rows - 1))
        while (x, y) in self.body:
            (x, y) = (randint(0, self.cols - 1), randint(0, self.rows - 1))
        return x, y

    def reset(self):
        """Reset the snake to the initial state."""
        self.body = deque([(1, 3), (2, 3), (3, 3)])
        self.food = self.random_food()
        self.direction = "RIGHT"

        return self.state()

    def state(self):
        """Return the current state of the snake. ({body}, head, food, direction)"""
        return self.body, self.body[-1], self.food, self.direction

    def actions(self):
        """Return the possible actions --> 3 directions, all but opposite of current"""
        directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        idx = directions.index(self.direction)
        return [self.direction, directions[(idx + 1) % 4], directions[(idx + 3) % 4]]


    def step(self, action):
        """Apply an action to the snake."""
        x, y = tuple(map(sum, zip(self.body[-1], self.directions[action]))) # calculate new head position
        # (x, y) = self.head + self.directions[action] # calculate new head position

        # check if snake is inbounds or collides with itself
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows or (x, y) in self.body:
            self.alive = False
            return -1

        self.body.append((x, y))  # add new head position
        self.direction = action

        # check if snake at food
        if (x, y) == self.food:
            self.food = self.random_food()
        else:
            self.body.popleft() # remove tail if not eating food

    def h(self):
        """Heuristic function for the snake game. Returns manhattan distance to food."""
        head = self.body[-1]
        food = self.food
        return abs(head[0] - food[0]) + abs(head[1] - food[1])


    def display_snake(self):
        grid = [['.' for _ in range(self.cols)] for _ in range(self.rows)]

        # Place food
        fx, fy = self.food
        grid[fy][fx] = '*'

        # Place snake body
        for x, y in self.body:
            grid[y][x] = '#'

        # Print grid row by row
        for row in grid:
            print(' '.join(row))

