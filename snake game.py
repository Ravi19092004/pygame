import pygame
import random

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
INITIAL_SPEED = 5
SNAKE_SIZE = 20
FPS = 40

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 55)
        self.snake_body = []
        self.snake_length = 1
        self.score = 0
        self.high_score = self.load_high_score()
        self.food_x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
        self.food_y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)
        self.snake_x = 45
        self.snake_y = 55
        self.velocity_x = 0
        self.velocity_y = 0
        self.game_over = False

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def text_screen(self, text, color, x, y):
        screen_text = self.font.render(text, True, color)
        self.screen.blit(screen_text, [x, y])

    def plot_snake(self, snake_body, color, snake_size):
        for x, y in snake_body:
            pygame.draw.rect(self.screen, color, [x, y, snake_size, snake_size])

    def welcome(self):
        exit_game = False
        while not exit_game:
            self.screen.fill((233, 210, 229))
            self.text_screen("Welcome to Snake", BLACK, 260, 250)
            self.text_screen("Press Space Bar to Play", BLACK, 232, 290)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_loop()
            pygame.display.update()
            self.clock.tick(60)

    def game_loop(self):
        exit_game = False
        while not exit_game:
            if self.game_over:
                self.screen.fill(WHITE)
                self.text_screen("Game Over! Press Enter to Continue", RED, 100, 250)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.snake_body = []
                            self.snake_length = 1
                            self.score = 0
                            self.snake_x = 45
                            self.snake_y = 55
                            self.velocity_x = 0
                            self.velocity_y = 0
                            self.game_over = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.velocity_x = INITIAL_SPEED
                            self.velocity_y = 0
                        if event.key == pygame.K_LEFT:
                            self.velocity_x = -INITIAL_SPEED
                            self.velocity_y = 0
                        if event.key == pygame.K_UP:
                            self.velocity_y = -INITIAL_SPEED
                            self.velocity_x = 0
                        if event.key == pygame.K_DOWN:
                            self.velocity_y = INITIAL_SPEED
                            self.velocity_x = 0
                self.snake_x += self.velocity_x
                self.snake_y += self.velocity_y
                if abs(self.snake_x - self.food_x) < 6 and abs(self.snake_y - self.food_y) < 6:
                    self.score += 1
                    self.food_x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
                    self.food_y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)
                    self.snake_length += 5
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()
                self.screen.fill(WHITE)
                self.text_screen("Score: " + str(self.score), RED, 5, 5)
                pygame.draw.rect(self.screen, RED, [self.food_x, self.food_y, SNAKE_SIZE, SNAKE_SIZE])
                head = []
                head.append(self.snake_x)
                head.append(self.snake_y)
                self.snake_body.append(head)
                if len(self.snake_body) > self.snake_length:
                    del self.snake_body[0]
                if head in self.snake_body[:-1]:
                    self.game_over = True
                if self.snake_x < 0 or self.snake_x > SCREEN_WIDTH or self.snake_y < 0 or self.snake_y > SCREEN_HEIGHT:
                    self.game_over = True
                self.plot_snake(self.snake_body, BLACK, SNAKE_SIZE)
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()
        quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.welcome()