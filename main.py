import pygame

# WINDOW PROPERTIES
pygame.init()
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# COLORS
BEIGE = (234, 218, 184)
RED = (242, 85, 96)
GREEN = (86, 174, 87)
BLUE = (69, 177, 232)
GRAY = (142, 135, 123)
BLACK = (100, 100, 100)

# GAME VARIABLES
ROWS = 6
COLS = 6
clock = pygame.time.Clock()
FPS = 60

class Wall():
    def __init__(self):
        self.width = WIDTH // COLS
        self.height = 50

    def create_wall(self):
        self.blocks = []
        block = []
        for row in range(ROWS):
            block_row = []
            for col in range(COLS):
                block_x = self.width * col
                block_y = self.height * row
                brick = pygame.Rect(block_x, block_y, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                block = [brick, strength]
                block_row.append(block)
            self.blocks.append(block_row)
    
    def draw_wall(self):
        for block_row in self.blocks:
            for block in block_row:
                if block[1] == 3:
                    block_color = BLUE
                elif block[1] == 2:
                    block_color = GREEN
                elif block[1] == 1:
                    block_color = RED
                pygame.draw.rect(WINDOW, block_color, block[0])
                pygame.draw.rect(WINDOW, BEIGE, block[0], 1)


class Paddle():
    def __init__(self):
        self.height = 20
        self.width = WIDTH / COLS
        self.x = WIDTH / 2 - self.width / 2
        self.y = HEIGHT - (self.height * 2)
        self.speed = 10
        self.paddle = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
    
    def move_paddle(self):
        self.direction = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] and self.paddle.x > 0:
            self.paddle.x -= self.speed
            self.direction = -1
        elif key_pressed[pygame.K_d] and self.paddle.x + self.width < WIDTH:
            self.paddle.x += self.speed
            self.direction = 1

    def draw_paddle(self):
        pygame.draw.rect(WINDOW, GRAY, self.paddle)
        pygame.draw.rect(WINDOW, BLACK, self.paddle, 3)


wall = Wall()
wall.create_wall()
paddle = Paddle()

run = True
while run:

    clock.tick(FPS)
    WINDOW.fill(BEIGE)
    wall.draw_wall()
    paddle.draw_paddle()
    paddle.move_paddle()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()