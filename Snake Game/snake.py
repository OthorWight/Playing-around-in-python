import sys
import pygame as pg
import time

def run_game():
    def add_body(x,y):
        snake_bodies.insert(0,[x, y, 10, 10])

    def move(direction):
        snake_bodies.insert(0,[snake_head_rect.x+2, snake_head_rect.y+2, 10, 10])
        del snake_bodies[-1]
        if direction == "RIGHT":
            snake_head_rect.x += 15
        elif direction == "LEFT":
            snake_head_rect.x -= 15
        elif direction == "UP":
            snake_head_rect.y -= 15
        elif direction == "DOWN":
            snake_head_rect.y += 15


    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("Snake")

    bg_color = (230,230,230)
    screen.fill(bg_color)

    #screen_rect = screen.get_rect()

    snake_head_rect = pg.Rect(600, 400, 15, 15)
    snake_bodies = []
    add_body(snake_head_rect.x+2, snake_head_rect.y+2)

    color = (100,100,100)
    #pg.draw.rect(screen, color, snake_head_rect)
    #pg.draw.rect(screen, color, snake_body_rect)

    current_time = time.time()
    direction = "RIGHT"
    delay = 1.0

    # Main Loop
    while True:
        # Even Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pg.K_LEFT:
                    direction = "LEFT"
                elif event.key == pg.K_UP:
                    direction = "UP"
                elif event.key == pg.K_DOWN:
                    direction = "DOWN"
                elif event.key == pg.K_q:
                    sys.exit()

        # Refresh
        pg.display.flip()
        screen.fill(bg_color)
        pg.draw.rect(screen, color, snake_head_rect)
        for body in snake_bodies:
            (x, y, w, h) = body
            pg.draw.rect(screen, color, pg.Rect(x, y, w, h))
        if time.time() - current_time >= delay:
            current_time = time.time()
            move(direction)

run_game()