# GUI for the FrozenLake environment.
from environment import FrozenLake
from pickle import load
import pygame

# Game setup
env = FrozenLake()
state = env.reset()
intent = None

# Display setup
pygame.init()
display = pygame.display.set_mode([env.cols * 50, env.rows * 50])
font = pygame.font.SysFont("Segoe UI Symbol", 30)

# Agent setup
with open("saved_agent.pkl", "rb") as file:
    agent = load(file)

# Game loop
displaying = True
terminal = False
while displaying:
    action = -1

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            displaying = False
        elif event.type == pygame.KEYDOWN and not terminal:
            if event.key == pygame.K_SPACE:
                action = agent.choose(state, env.actions)
            elif event.key == pygame.K_UP:
                action = 0
            elif event.key == pygame.K_LEFT:
                action = 1
            elif event.key == pygame.K_DOWN:
                action = 2
            elif event.key == pygame.K_RIGHT:
                action = 3

    # State update
    if action in env.actions:
        intent = env.current, action
        _, state, terminal = env.step(action)

    # Lake drawing
    display.fill((255, 255, 255))
    for r in range(env.rows):
        for c in range(env.cols):
            pygame.draw.rect(display, (0, 0, 0), pygame.Rect(c * 50, r * 50, 50, 50), width=1)
            if (r, c) == env.goal:
                pygame.draw.rect(display, (0, 0, 0), pygame.Rect(c * 50, r * 50, 50, 50))
            if (r, c) in env.holes:
                pygame.draw.rect(display, (0, 0, 255), pygame.Rect(c * 50 + 1, r * 50 + 1, 48, 48))
            if (r, c) == env.current:
                pygame.draw.circle(display, (0, 255, 0), (c * 50 + 25, r * 50 + 25), 20)

    # Move arrow
    if intent is not None:
        (r, c), action = intent
        arrow = ["↑", "←", "↓", "→"]
        x = [c * 50 + 18, c * 50 + 10, c * 50 + 18, c * 50 + 10]
        y = [r * 50 + 3, r * 50, r * 50 + 3, r * 50]
        text = font.render(arrow[action], False, (0, 0, 0))
        display.blit(text, (x[action], y[action]))

    # Display update
    pygame.display.flip()

# Display close
pygame.quit()