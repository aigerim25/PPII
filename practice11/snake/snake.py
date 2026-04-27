import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
ORANGE = (255, 140, 0)
PURPLE = (160, 32, 240)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

score = 0
level = 1
speed = 8
foods_eaten = 0

FOOD_LIFETIME = 5000


def draw_snake():
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))


def generate_food():
    food_types = [
        {"color": RED, "weight": 1},
        {"color": ORANGE, "weight": 2},
        {"color": PURPLE, "weight": 3}
    ]

    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        position = (x, y)

        if position not in snake:
            food_type = random.choice(food_types)

            return {
                "position": position,
                "color": food_type["color"],
                "weight": food_type["weight"],
                "created_time": pygame.time.get_ticks()
            }


def draw_food(food):
    x, y = food["position"]
    pygame.draw.rect(screen, food["color"], (x, y, CELL_SIZE, CELL_SIZE))


def draw_text():
    text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(text, (20, 20))


def check_collision(head):
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    if head in snake[1:]:
        return True

    return False


def game_over_screen():
    screen.fill(BLACK)

    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)

    pygame.display.update()


food = generate_food()
running = True
game_over = False

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

            else:
                if event.key == pygame.K_r:
                    snake = [(100, 100), (80, 100), (60, 100)]
                    direction = "RIGHT"
                    score = 0
                    level = 1
                    speed = 8
                    foods_eaten = 0
                    food = generate_food()
                    game_over = False

                elif event.key == pygame.K_q:
                    running = False

    if not game_over:
        current_time = pygame.time.get_ticks()
        if current_time - food["created_time"] > FOOD_LIFETIME:
            food = generate_food()

        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= CELL_SIZE
        elif direction == "DOWN":
            head_y += CELL_SIZE
        elif direction == "LEFT":
            head_x -= CELL_SIZE
        elif direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if check_collision(new_head):
            game_over = True
        else:
            snake.insert(0, new_head)

            if new_head == food["position"]:
                score += food["weight"]
                foods_eaten += 1
                food = generate_food()

                if foods_eaten % 3 == 0:
                    level += 1
                    speed += 2
            else:
                snake.pop()

        screen.fill(BLACK)
        draw_snake()
        draw_food(food)
        draw_text()
        pygame.display.update()

    else:
        game_over_screen()

pygame.quit()