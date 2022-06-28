import pygame
from constants import *

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

