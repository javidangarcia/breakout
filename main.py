import pygame
from constants import *
from wall import Wall
from paddle import Paddle
from ball import Ball

pygame.init()
pygame.display.set_caption("Breakout")
FONT = pygame.font.SysFont("comicsans", 30)
clock = pygame.time.Clock()
FPS = 60

def instructions(text, color, position_y):
    draw_text = FONT.render(text, 1, color, WHITE)
    WINDOW.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, position_y))

# GAME OBJECTS
wall = Wall()
wall.create_wall()
paddle = Paddle()
ball = Ball(paddle.x + paddle.width // 2, paddle.y - paddle.height)

def main():
    active = False
    game_over = 0
    run = True
    while run:

        clock.tick(FPS)
        WINDOW.fill(BEIGE)
        wall.draw_wall()
        paddle.draw_paddle()
        ball.draw_ball()

        if active:
            paddle.move_paddle()
            game_over = ball.move_ball(paddle, wall)
            if game_over != 0:
                active = False

        if active == False:
            if game_over == 0:
                instructions("CLICK ANYWHERE TO START", BLUE, HEIGHT // 2 + 100)
            elif game_over == 1:
                instructions("YOU WON", GREEN, HEIGHT // 2 + 50)
                instructions("CLICK ANYWHERE TO RESTART", GREEN, HEIGHT // 2 + 100)
            elif game_over == -1:
                instructions("YOU LOST", RED, HEIGHT // 2 + 50)
                instructions("CLICK ANYWHERE TO RESTART", RED, HEIGHT // 2 + 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and active == False:
                active = True
                ball.reset(paddle.x + paddle.width // 2, paddle.y - paddle.height)
                paddle.reset()
                wall.create_wall()

        pygame.display.update()


if __name__ == "__main__":
    main()
pygame.quit()