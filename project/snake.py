import pygame
import sys
import random

# Constants
CELL_SIZE = 30
GRID_SIZE = 12
MARGIN = 50  # Space at the top for score display
SCREEN_SIZE = CELL_SIZE * GRID_SIZE
TOTAL_HEIGHT = SCREEN_SIZE + MARGIN  # Include margin at the top

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 20, 222)
RED = (200, 0, 0)
LIGHT_GREEN = (48, 199, 84)
DARK_GREEN = (36, 166, 67)
DARKEST_GREEN = (6, 79, 6)
BORDER_COLOR = (0, 0, 0)
SNAKE_SPEED = 6

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, TOTAL_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

directions = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
current_direction = "RIGHT"

# Example state representation
snake_state = [(3, 3), (1, 3), [(1, 3), (2, 3), (3, 3)], (7, 7)]


def show_start_screen(snake_state):
    """Wait for key press before starting the game."""
    draw_board()
    draw_score(0)
    draw_snake(snake_state)
    text = font.render("Press any key to start", True, BLACK)
    screen.blit(text, (SCREEN_SIZE // 4, TOTAL_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False  # Exit loop when key is pressed


def draw_board():
    """Draw the checkerboard pattern for the game grid."""
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE),
            )


def draw_snake(state, game_over=False):
    """Draw the snake with googly eyes that turn into X's when the game is over."""
    head, _, body, _ = state

    for segment in body:
        pygame.draw.rect(
            screen,
            BLUE,
            (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE),
        )

    # Draw googly eyes on the head
    head_x, head_y = head
    head_x_pixel = head_x * CELL_SIZE
    head_y_pixel = head_y * CELL_SIZE + MARGIN

    eye_radius = CELL_SIZE // 6

    # Default eye positions (for RIGHT direction)
    eye1_offset = (CELL_SIZE // 4, -CELL_SIZE // 4)
    eye2_offset = (CELL_SIZE // 4, CELL_SIZE // 4)

    # Adjust eyes based on current direction
    if current_direction == "UP":
        eye1_offset = (-CELL_SIZE // 4, -CELL_SIZE // 3)
        eye2_offset = (CELL_SIZE // 4, -CELL_SIZE // 3)
    elif current_direction == "DOWN":
        eye1_offset = (-CELL_SIZE // 4, CELL_SIZE // 3)
        eye2_offset = (CELL_SIZE // 4, CELL_SIZE // 3)
    elif current_direction == "LEFT":
        eye1_offset = (-CELL_SIZE // 3, -CELL_SIZE // 4)
        eye2_offset = (-CELL_SIZE // 3, CELL_SIZE // 4)

    # Compute final eye positions
    eye1 = (head_x_pixel + CELL_SIZE // 2 + eye1_offset[0], head_y_pixel + CELL_SIZE // 2 + eye1_offset[1])
    eye2 = (head_x_pixel + CELL_SIZE // 2 + eye2_offset[0], head_y_pixel + CELL_SIZE // 2 + eye2_offset[1])

    # Draw eyes
    pygame.draw.circle(screen, WHITE, eye1, eye_radius)
    pygame.draw.circle(screen, WHITE, eye2, eye_radius)

    if game_over:
        # Draw X pupils
        draw_x_pupil(eye1)
        draw_x_pupil(eye2)
    else:
        # Draw regular pupils
        pygame.draw.circle(screen, BLACK, eye1, eye_radius // 2)
        pygame.draw.circle(screen, BLACK, eye2, eye_radius // 2)


def draw_x_pupil(center):
    """Draw an X instead of a circular pupil for dead eyes."""
    size = CELL_SIZE // 8
    x, y = center

    pygame.draw.line(screen, BLACK, (x - size, y - size), (x + size, y + size), 5)
    pygame.draw.line(screen, BLACK, (x - size, y + size), (x + size, y - size), 5)


def draw_food(state):
    """Draw food as a red circle."""
    food = state[3]
    pygame.draw.circle(
        screen,
        RED,
        (food[0] * CELL_SIZE + CELL_SIZE // 2, food[1] * CELL_SIZE + MARGIN + CELL_SIZE // 2),
        CELL_SIZE // 3,
    )

def draw_score(score):
    """Display the current score at the top margin."""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.fill(DARKEST_GREEN, (0, 0, SCREEN_SIZE, MARGIN))  # Clear the top margin area
    screen.blit(text, (10, 10))


def move_snake(state, direction):
    """Update the snake's position based on movement."""
    head, tail, body, food = state
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head == food:  # Eat food, grow snake
        body.append(new_head)
        new_food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        while new_food in body or new_food == head:
            new_food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        return [new_head, body[0], body, new_food]

    body.append(new_head)
    body.pop(0)  # Remove the old tail

    return [new_head, body[0], body, food]


def game_over_screen(score):
    """Display game over screen with score and wait for key press."""
    # screen.fill(WHITE)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (SCREEN_SIZE // 4, TOTAL_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     waiting = False  # Exit loop on key press


def main():
    """Main game loop."""
    global current_direction, snake_state
    show_start_screen(snake_state)  # Wait for key press to start
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        draw_board()
        # draw_border()  # Draw the border
        draw_snake(snake_state)
        draw_food(snake_state)
        draw_score(score)  # Display score

        old_snake_state = snake_state

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and current_direction != "DOWN":
                    current_direction = "UP"
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    current_direction = "DOWN"
                elif event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    current_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    current_direction = "RIGHT"

        old_food = snake_state[3]
        snake_state = move_snake(snake_state, directions[current_direction])

        if old_food != snake_state[3]:  # If food changes, the snake ate it
            score += 1


        x, y = snake_state[0]

        if (x, y) in snake_state[2][:-1] or x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            print(f"Game Over! Score: {score}")
            draw_snake(old_snake_state, game_over=True)
            game_over_screen(score)
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
