import sys
import pygame as pg
import time

def run_game():
    def add_body():
        snake_bodies.append(snake_bodies[-1])

    def move(direction):
        snake_bodies.insert(0,[snake_head_rect.x+3, snake_head_rect.y+3, 10, 10])
        del snake_bodies[-1]
        if direction == "RIGHT":
            snake_head_rect.x += 15
        elif direction == "LEFT":
            snake_head_rect.x -= 15
        elif direction == "UP":
            snake_head_rect.y -= 15
        elif direction == "DOWN":
            snake_head_rect.y += 15

    def place_food():
        pg.draw.circle(screen,(200,0,200),(30,30), 5)


    pg.init()
    screen = pg.display.set_mode((1200, 750))
    pg.display.set_caption("Snake")

    bg_color = (230,230,230)
    screen.fill(bg_color)

    #screen_rect = screen.get_rect()

    snake_head_rect = pg.Rect(600, 375, 15, 15)
    snake_bodies = [(snake_head_rect.x+3, snake_head_rect.y+3,10,10)]

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
                elif event.key == pg.K_1:
                    add_body()
                elif event.key == pg.K_2:
                    place_food()

        # Refresh
        pg.display.flip()
        screen.fill(bg_color)
        pg.draw.rect(screen, color, snake_head_rect)
        pg.draw.circle(screen,(200,0,200),(8,8), 7)
        for w in range(0,1200,15):
            pg.draw.line(screen,(220,220,220),(w,0),(w,750),1)
        for h in range(0,800,15):
            pg.draw.line(screen,(220,220,220),(0,h),(1200,h),1)
        for body in snake_bodies:
            (x, y, w, h) = body
            pg.draw.rect(screen, color, pg.Rect(x, y, w, h))
        if time.time() - current_time >= delay:
            current_time = time.time()
            move(direction)

run_game()
