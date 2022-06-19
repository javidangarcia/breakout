import pygame

# WINDOW PROPERTIES
pygame.init()
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# COLORS
BACKGROUND = (234, 218, 184)
RED = (242, 85, 96)
GREEN = (86, 174, 87)
BLUE = (69, 177, 232)

# GAME VARIABLES
ROWS = 6
COLS = 6

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
                pygame.draw.rect(WINDOW, BACKGROUND, block[0], 1)

wall = Wall()
wall.create_wall()

run = True
while run:

    WINDOW.fill(BACKGROUND)
    wall.draw_wall()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()