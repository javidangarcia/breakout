import pygame
from constants import *

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
                    block_color = RED
                elif block[1] == 2:
                    block_color = GREEN
                elif block[1] == 1:
                    block_color = BLUE
                pygame.draw.rect(WINDOW, block_color, block[0])
                pygame.draw.rect(WINDOW, BEIGE, block[0], 1)