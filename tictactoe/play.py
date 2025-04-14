# GUI for the game of tic-tac-toe
import pygame

from environment import start_state, actions, utility, min_successor, max_successor
from minimax import minimax_action
from tictactoe.minimax import rand_color
from mcst import mcts_action

# Game setup
state = start_state()
turn = 0


# Display setup
pygame.init()
display = pygame.display.set_mode([300, 300])

# Game loop
displaying = True
terminal = False
x_color = rand_color()
o_color = rand_color()

while displaying:
    action = -1

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            displaying = False
        elif event.type == pygame.KEYDOWN and not terminal:
            # action = minimax_action(state, turn)
            action = mcts_action(state, turn, 3)

        elif event.type == pygame.MOUSEBUTTONDOWN and not terminal:
            x, y = pygame.mouse.get_pos()
            action = (y // 100) * 3 + (x // 100)

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

    # Line drawing
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (100, 0), (100, 300), width=5)
    pygame.draw.line(display, (0, 0, 0), (200, 0), (200, 300), width=5)
    pygame.draw.line(display, (0, 0, 0), (0, 100), (300, 100), width=5)
    pygame.draw.line(display, (0, 0, 0), (0, 200), (300, 200), width=5)

    # Mark drawing
    for i in range(9):
        color = rand_color()
        x, y = (i % 3) * 100, (i // 3) * 100
        if state[i] == 1:
            pygame.draw.line(display, x_color, (x+10, y+10), (x+90, y+90), width=5)
            pygame.draw.line(display, x_color, (x+90, y+10), (x+10, y+90), width=5)
        elif state[i] == -1:
            pygame.draw.circle(display, o_color, (x+50, y+50), 40, width=5)

    # Display update
    pygame.display.flip()

# Display close
pygame.quit()