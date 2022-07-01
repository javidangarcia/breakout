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
        self.max_speed = 5
        self.game_over = 0

    def move_ball(self, paddle, wall):

        threshold = 5
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for brick in row:
                if self.ball.colliderect(brick[0]):
                    if abs(self.ball.bottom - brick[0].top) < threshold and self.speed_y > 0:
                        self.speed_y *= -1
                    if abs(self.ball.top - brick[0].bottom) < threshold and self.speed_y < 0:
                        self.speed_y *= -1
                    if abs(self.ball.right - brick[0].left) < threshold and self.speed_x > 0:
                        self.speed_x *= -1
                    if abs(self.ball.left - brick[0].right) < threshold and self.speed_x < 0:
                        self.speed_x *= -1
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                if wall.blocks[row_count][item_count][0] != (0,0,0,0):
                    wall_destroyed = 0

                item_count += 1
            row_count += 1

        if wall_destroyed == 1:
            self.game_over = 1

        if self.ball.left < 0 or self.ball.right > WIDTH:
            self.speed_x *= -1 
        if self.ball.top < 0:
            self.speed_y *= -1
        if self.ball.bottom > HEIGHT:
            self.game_over = -1

        if self.ball.colliderect(paddle.paddle):
            if abs(self.ball.bottom - paddle.paddle.top) < threshold and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += paddle.direction
                if self.speed_x > self.max_speed:
                    self.speed_x = self.max_speed
                elif self.speed_x < 0 and self.speed_x < -self.max_speed:
                    self.speed_x = -self.max_speed
            else:
                self.speed_x *= -1

        self.ball.x += self.speed_x
        self.ball.y += self.speed_y
        return self.game_over

    def draw_ball(self):
        pygame.draw.circle(WINDOW, GRAY, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius)
        pygame.draw.circle(WINDOW, BLACK, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius, 3)