import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Fonts
font_title = pygame.font.SysFont("couriernew", 50, bold=True)
font_score = pygame.font.SysFont("couriernew", 25)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE), 1)

def draw_food(position):
    pygame.draw.rect(screen, RED, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    score_text = font_score.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

def game_over_screen(score):
    screen.fill(BLACK)
    title_text = font_title.render("GAME OVER", True, RED)
    score_text = font_score.render(f"Final Score: {score}", True, WHITE)
    screen.blit(title_text, [WIDTH//2 - title_text.get_width()//2, HEIGHT//2 - 50])
    screen.blit(score_text, [WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10])
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = "RIGHT"
    change_to = direction
    score = 0

    food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
    food_spawn = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        direction = change_to

        if direction == "UP":
            snake_pos[1] -= CELL_SIZE
        elif direction == "DOWN":
            snake_pos[1] += CELL_SIZE
        elif direction == "LEFT":
            snake_pos[0] -= CELL_SIZE
        elif direction == "RIGHT":
            snake_pos[0] += CELL_SIZE

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
        food_spawn = True

        # Game Over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            game_over_screen(score)
            main()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over_screen(score)
                main()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_pos)
        show_score(score)
        pygame.display.update()

        clock.tick(10)  # Speed

if __name__ == "__main__":
    main()
