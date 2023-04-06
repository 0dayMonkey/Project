import pygame
import sys
import random

# Paramètres du jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 20
FPS = 10

# Couleurs
BLACK = (0, 0, 0)

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Charger les images
snake_head_img = pygame.image.load("snake_head.png")
food_img = pygame.image.load("food.png")

class Snake:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, -SQUARE_SIZE)

    def move(self):
        x, y = self.direction
        head_x, head_y = self.positions[0]
        new_head = (head_x + x, head_y + y)
        self.positions.insert(0, new_head)
        self.positions.pop()

    def change_direction(self, new_direction):
        self.direction = new_direction

    def eat(self, food):
        self.positions.append(self.positions[-1])

    def is_collision(self):
        head_x, head_y = self.positions[0]
        return (head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT
                or (self.positions[0] in self.positions[1:]))

class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // SQUARE_SIZE) - 1) * SQUARE_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // SQUARE_SIZE) - 1) * SQUARE_SIZE)

def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, SQUARE_SIZE):
                    snake.change_direction((0, -SQUARE_SIZE))
                if event.key == pygame.K_DOWN and snake.direction != (0, -SQUARE_SIZE):
                    snake.change_direction((0, SQUARE_SIZE))
                if event.key == pygame.K_LEFT and snake.direction != (SQUARE_SIZE, 0):
                    snake.change_direction((-SQUARE_SIZE, 0))
                if event.key == pygame.K_RIGHT and snake.direction != (-SQUARE_SIZE, 0):
                    snake.change_direction((SQUARE_SIZE, 0))

        snake.move()

        if snake.positions[0] == food.position:
            snake.eat(food)
            food = Food()

        if snake.is_collision():
            snake = Snake()
            food = Food()

        screen.fill(BLACK)

        screen.blit(food_img, food.position)
        for position in snake.positions:
          screen.blit(snake_head_img, position)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
