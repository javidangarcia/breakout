import pygame
from constants import *
from wall import Wall
from paddle import Paddle
from ball import Ball

pygame.init()
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

# GAME OBJECTS
wall = Wall()
wall.create_wall()
paddle = Paddle()
ball = Ball(paddle.x + paddle.width // 2, paddle.y - paddle.height)

def main():
    run = True
    while run:

        clock.tick(FPS)
        WINDOW.fill(BEIGE)
        wall.draw_wall()
        paddle.draw_paddle()
        paddle.move_paddle()
        ball.draw_ball()
        ball.move_ball()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == "__main__":
    main()
pygame.quit()