import pygame
from constants import *

class Ball():
    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y
        self.ball = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.game_over = 0

    def move_ball(self):
        if self.ball.left < 0 or self.ball.right > WIDTH:
            self.speed_x *= -1
        if self.ball.top < 0:
            self.speed_y *= -1
        if self.ball.bottom > HEIGHT:
            self.game_over = -1
        self.ball.x += self.speed_x
        self.ball.y += self.speed_y
        return self.game_over

    def draw_ball(self):
        pygame.draw.circle(WINDOW, GRAY, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius)
        pygame.draw.circle(WINDOW, BLACK, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius, 3)