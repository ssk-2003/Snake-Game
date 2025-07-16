import pygame
import random
import sys

# Initialize
pygame.init()

# Screen setup
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Satish Snake Game")

# Colors
BG_COLOR = (220, 220, 220)
FOOD_COLOR = (255, 51, 51)
SNAKE_HEAD_COLOR = (0, 200, 0)
SNAKE_BODY_COLOR = (100, 255, 100)
SCORE_BAR_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (255, 0, 0)

# Snake block size
BLOCK_SIZE = 15

# Fonts
font = pygame.font.SysFont("Arial", 24)
admin_font = pygame.font.SysFont("Arial", 20, bold=True)
game_over_font = pygame.font.SysFont("Arial", 48, bold=True)

clock = pygame.time.Clock()

# Game reset logic
def reset_game():
    global snake_x, snake_y, change_x, change_y, snake_body, food_x, food_y, score
    snake_x, snake_y = width // 2, height // 5
    change_x, change_y = 0, 0
    snake_body = [(snake_x, snake_y)]
    food_x = random.randrange(0, width, BLOCK_SIZE)
    food_y = random.randrange(0, height, BLOCK_SIZE)
    score = 0

# Initialize game
reset_game()
game_over = False

def draw_game():
    screen.fill(BG_COLOR)
    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for i, (x, y) in enumerate(snake_body):
        color = SNAKE_HEAD_COLOR if i == len(snake_body) - 1 else SNAKE_BODY_COLOR
        pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    # Top bar
    pygame.draw.rect(screen, SCORE_BAR_COLOR, (0, 0, width, 40))
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    admin_text = admin_font.render("Satish - Admin", True, TEXT_COLOR)
    screen.blit(score_text, (10, 5))
    screen.blit(admin_text, (width - 180, 8))

    pygame.display.update()

def show_game_over():
    screen.fill(BG_COLOR)
    text1 = game_over_font.render("GAME OVER", True, GAME_OVER_COLOR)
    text2 = font.render("Press R to Restart", True, GAME_OVER_COLOR)
    screen.blit(text1, (width // 2 - text1.get_width() // 2, height // 2 - 50))
    screen.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 + 10))
    pygame.display.update()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT and change_x == 0:
                    change_x = -BLOCK_SIZE
                    change_y = 0
                elif event.key == pygame.K_RIGHT and change_x == 0:
                    change_x = BLOCK_SIZE
                    change_y = 0
                elif event.key == pygame.K_UP and change_y == 0:
                    change_x = 0
                    change_y = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and change_y == 0:
                    change_x = 0
                    change_y = BLOCK_SIZE
            elif event.key == pygame.K_r:
                reset_game()
                game_over = False

    if not game_over:
        snake_x = (snake_x + change_x) % width
        snake_y = (snake_y + change_y) % height

        # Self-collision check
        if (snake_x, snake_y) in snake_body[1:]:
            game_over = True

        snake_body.append((snake_x, snake_y))

        # Food collision
        if snake_x == food_x and snake_y == food_y:
            score += 1
            food_x = random.randrange(0, width, BLOCK_SIZE)
            food_y = random.randrange(0, height, BLOCK_SIZE)
        else:
            snake_body.pop(0)

        draw_game()
    else:
        show_game_over()

    clock.tick(15)
