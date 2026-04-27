import pygame
import random
from db import save_result, get_top_scores, get_personal_best
from config import load_config, save_config


WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
DARK_RED = (120, 0, 0)
ORANGE = (255, 140, 0)
PURPLE = (160, 32, 240)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
CYAN = (0, 220, 220)
YELLOW = (255, 220, 0)
GRAY = (90, 90, 90)
GRID_COLOR = (40, 40, 40)


class SnakeGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.big_font = pygame.font.SysFont(None, 36)

        self.settings = load_config()
        self.snake_color = tuple(self.settings["snake_color"])
        self.grid_enabled = self.settings["grid"]
        self.sound_enabled = self.settings["sound"]

        self.state = "menu"
        self.username = ""
        self.personal_best = 0

        self.reset_game()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

        self.score = 0
        self.level = 1
        self.speed = 8
        self.base_speed = 8
        self.foods_eaten = 0

        self.food_lifetime = 5000
        self.poison_lifetime = 7000

        self.obstacles = []

        self.food = self.generate_food()
        self.poison_food = self.generate_poison_food()

        self.power_up = self.generate_power_up()
        self.power_up_lifetime = 8000

        self.active_power_up = None
        self.power_up_start_time = 0
        self.power_up_duration = 5000

        self.has_shield = False
        self.result_saved = False

    def is_position_free(self, position):
        return position not in self.snake and position not in self.obstacles

    def generate_food(self):
        food_types = [
            {"color": RED, "weight": 1},
            {"color": ORANGE, "weight": 2},
            {"color": PURPLE, "weight": 3}
        ]

        while True:
            position = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )

            if self.is_position_free(position):
                food_type = random.choice(food_types)

                return {
                    "position": position,
                    "color": food_type["color"],
                    "weight": food_type["weight"],
                    "created_time": pygame.time.get_ticks()
                }

    def generate_poison_food(self):
        while True:
            position = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )

            if self.is_position_free(position) and position != self.food["position"]:
                return {
                    "position": position,
                    "color": DARK_RED,
                    "created_time": pygame.time.get_ticks()
                }

    def generate_power_up(self):
        power_types = [
            {"type": "speed", "color": BLUE},
            {"type": "slow", "color": CYAN},
            {"type": "shield", "color": YELLOW}
        ]

        while True:
            position = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )

            if (
                self.is_position_free(position)
                and position != self.food["position"]
                and position != self.poison_food["position"]
            ):
                power = random.choice(power_types)

                return {
                    "position": position,
                    "type": power["type"],
                    "color": power["color"],
                    "created_time": pygame.time.get_ticks()
                }

    def generate_obstacles(self):
        self.obstacles = []

        if self.level < 3:
            return

        head = self.snake[0]

        safe_positions = [
            head,
            (head[0] + CELL_SIZE, head[1]),
            (head[0] - CELL_SIZE, head[1]),
            (head[0], head[1] + CELL_SIZE),
            (head[0], head[1] - CELL_SIZE)
        ]

        obstacle_count = self.level + 2

        while len(self.obstacles) < obstacle_count:
            position = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )

            if (
                position not in self.snake
                and position not in self.obstacles
                and position not in safe_positions
                and position != self.food["position"]
                and position != self.poison_food["position"]
            ):
                self.obstacles.append(position)

    def draw_grid(self):
        if not self.grid_enabled:
            return

        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw_snake(self):
        for part in self.snake:
            pygame.draw.rect(
                self.screen,
                self.snake_color,
                (part[0], part[1], CELL_SIZE, CELL_SIZE)
            )

    def draw_food(self):
        x, y = self.food["position"]
        pygame.draw.rect(
            self.screen,
            self.food["color"],
            (x, y, CELL_SIZE, CELL_SIZE)
        )

    def draw_poison_food(self):
        x, y = self.poison_food["position"]
        pygame.draw.rect(
            self.screen,
            self.poison_food["color"],
            (x, y, CELL_SIZE, CELL_SIZE)
        )

    def draw_power_up(self):
        if self.power_up is not None:
            x, y = self.power_up["position"]
            pygame.draw.rect(
                self.screen,
                self.power_up["color"],
                (x, y, CELL_SIZE, CELL_SIZE)
            )

    def draw_obstacles(self):
        for block in self.obstacles:
            pygame.draw.rect(
                self.screen,
                GRAY,
                (block[0], block[1], CELL_SIZE, CELL_SIZE)
            )

    def draw_text_center(self, text, y, color=WHITE, big=False):
        font = self.big_font if big else self.font
        rendered_text = font.render(text, True, color)
        rect = rendered_text.get_rect(center=(WIDTH // 2, y))
        self.screen.blit(rendered_text, rect)

    def draw_game_info(self):
        text = self.font.render(
            f"Player: {self.username}   Score: {self.score}   Level: {self.level}",
            True,
            WHITE
        )
        self.screen.blit(text, (20, 20))

        best_text = self.font.render(
            f"Personal Best: {self.personal_best}",
            True,
            WHITE
        )
        self.screen.blit(best_text, (20, 50))

        if self.has_shield:
            power_text = "Power-up: Shield"
        elif self.active_power_up == "speed":
            power_text = "Power-up: Speed Boost"
        elif self.active_power_up == "slow":
            power_text = "Power-up: Slow Motion"
        else:
            power_text = "Power-up: None"

        rendered_power = self.font.render(power_text, True, WHITE)
        self.screen.blit(rendered_power, (20, 80))

    def check_collision(self, head):
        wall_collision = (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        )

        self_collision = head in self.snake[1:]
        obstacle_collision = head in self.obstacles

        if obstacle_collision:
            return True

        if wall_collision or self_collision:
            if self.has_shield:
                self.has_shield = False
                return False

            return True

        return False

    def save_game_result_once(self):
        if not self.result_saved:
            save_result(self.username, self.score, self.level)
            self.result_saved = True

    def activate_power_up(self, power_type):
        if power_type == "speed":
            self.active_power_up = "speed"
            self.power_up_start_time = pygame.time.get_ticks()
            self.speed = self.base_speed + 6

        elif power_type == "slow":
            self.active_power_up = "slow"
            self.power_up_start_time = pygame.time.get_ticks()
            self.speed = max(4, self.base_speed - 4)

        elif power_type == "shield":
            self.has_shield = True

    def update_power_up_effects(self):
        current_time = pygame.time.get_ticks()

        if self.active_power_up in ["speed", "slow"]:
            if current_time - self.power_up_start_time > self.power_up_duration:
                self.active_power_up = None
                self.speed = self.base_speed

    def draw_menu(self):
        self.screen.fill(BLACK)

        self.draw_text_center("SNAKE GAME", 120, GREEN, big=True)
        self.draw_text_center("Enter your username:", 220)

        username_text = self.font.render(self.username, True, WHITE)
        username_rect = username_text.get_rect(center=(WIDTH // 2, 270))
        self.screen.blit(username_text, username_rect)

        self.draw_text_center("Press ENTER to start", 340)
        self.draw_text_center("Press L to see leaderboard", 380)
        self.draw_text_center("Press S for settings", 420)

        pygame.display.update()

    def draw_settings(self):
        self.screen.fill(BLACK)

        self.draw_text_center("SETTINGS", 100, GREEN, big=True)
        self.draw_text_center("1 - Change Snake Color", 200)
        self.draw_text_center(f"2 - Grid: {'ON' if self.grid_enabled else 'OFF'}", 250)
        self.draw_text_center(f"3 - Sound: {'ON' if self.sound_enabled else 'OFF'}", 300)

        color_text = f"Current Color: {self.snake_color}"
        self.draw_text_center(color_text, 360)

        self.draw_text_center("Press B to go back", 460)

        pygame.display.update()

    def draw_leaderboard(self):
        self.screen.fill(BLACK)

        self.draw_text_center("TOP 10 SCORES", 60, GREEN, big=True)

        scores = get_top_scores()

        if not scores:
            self.draw_text_center("No scores yet", 160)
        else:
            y = 120

            for index, row in enumerate(scores, start=1):
                username, score, level, played_at = row
                text = f"{index}. {username} | Score: {score} | Level: {level}"

                rendered_text = self.font.render(text, True, WHITE)
                self.screen.blit(rendered_text, (80, y))

                y += 40

        self.draw_text_center("Press B to go back", 540)
        pygame.display.update()

    def draw_game_over(self):
        self.screen.fill(BLACK)

        self.draw_text_center("GAME OVER", HEIGHT // 2 - 100, RED, big=True)
        self.draw_text_center(f"Final Score: {self.score}", HEIGHT // 2 - 30)
        self.draw_text_center(f"Level Reached: {self.level}", HEIGHT // 2 + 20)
        self.draw_text_center("Press R to Restart or Q to Quit", HEIGHT // 2 + 90)

        pygame.display.update()

    def handle_menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.username.strip() != "":
                    self.personal_best = get_personal_best(self.username)
                    self.reset_game()
                    self.state = "game"

            elif event.key == pygame.K_BACKSPACE:
                self.username = self.username[:-1]

            elif event.key == pygame.K_l:
                self.state = "leaderboard"

            elif event.key == pygame.K_s:
                self.state = "settings"

            elif event.unicode.isprintable():
                if len(self.username) < 50:
                    self.username += event.unicode

    def handle_settings_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.snake_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

                self.settings["snake_color"] = list(self.snake_color)
                save_config(self.settings)

            elif event.key == pygame.K_2:
                self.grid_enabled = not self.grid_enabled
                self.settings["grid"] = self.grid_enabled
                save_config(self.settings)

            elif event.key == pygame.K_3:
                self.sound_enabled = not self.sound_enabled
                self.settings["sound"] = self.sound_enabled
                save_config(self.settings)

            elif event.key == pygame.K_b:
                self.state = "menu"

    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != "DOWN":
                self.direction = "UP"
            elif event.key == pygame.K_DOWN and self.direction != "UP":
                self.direction = "DOWN"
            elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                self.direction = "RIGHT"

    def handle_game_over_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.personal_best = get_personal_best(self.username)
                self.reset_game()
                self.state = "game"

            elif event.key == pygame.K_q:
                pygame.quit()
                exit()

    def handle_leaderboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                self.state = "menu"

    def update_game(self):
        current_time = pygame.time.get_ticks()

        self.update_power_up_effects()

        if current_time - self.food["created_time"] > self.food_lifetime:
            self.food = self.generate_food()

        if current_time - self.poison_food["created_time"] > self.poison_lifetime:
            self.poison_food = self.generate_poison_food()

        if self.power_up is not None:
            if current_time - self.power_up["created_time"] > self.power_up_lifetime:
                self.power_up = self.generate_power_up()

        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if self.check_collision(new_head):
            self.save_game_result_once()
            self.state = "game_over"
            return

        self.snake.insert(0, new_head)

        if new_head == self.food["position"]:
            self.score += self.food["weight"]
            self.foods_eaten += 1
            self.food = self.generate_food()

            if self.foods_eaten % 3 == 0:
                self.level += 1
                self.base_speed += 2
                self.speed = self.base_speed

                self.generate_obstacles()

                self.food = self.generate_food()
                self.poison_food = self.generate_poison_food()
                self.power_up = self.generate_power_up()

        elif new_head == self.poison_food["position"]:
            for _ in range(2):
                if len(self.snake) > 1:
                    self.snake.pop()

            self.poison_food = self.generate_poison_food()

            if len(self.snake) <= 1:
                self.save_game_result_once()
                self.state = "game_over"
                return

        elif self.power_up is not None and new_head == self.power_up["position"]:
            self.activate_power_up(self.power_up["type"])
            self.power_up = self.generate_power_up()

        else:
            self.snake.pop()

    def draw_game(self):
        self.screen.fill(BLACK)

        self.draw_grid()
        self.draw_obstacles()
        self.draw_snake()
        self.draw_food()
        self.draw_poison_food()
        self.draw_power_up()
        self.draw_game_info()

        pygame.display.update()

    def run(self):
        running = True

        while running:
            self.clock.tick(self.speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == "menu":
                    self.handle_menu_events(event)

                elif self.state == "settings":
                    self.handle_settings_events(event)

                elif self.state == "game":
                    self.handle_game_events(event)

                elif self.state == "game_over":
                    self.handle_game_over_events(event)

                elif self.state == "leaderboard":
                    self.handle_leaderboard_events(event)

            if self.state == "menu":
                self.draw_menu()

            elif self.state == "settings":
                self.draw_settings()

            elif self.state == "game":
                self.update_game()
                self.draw_game()

            elif self.state == "game_over":
                self.draw_game_over()

            elif self.state == "leaderboard":
                self.draw_leaderboard()

        pygame.quit()