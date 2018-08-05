import sys
import pygame as pg
import time
import random

def run_game():

    def move(direction,level,delay):
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
        for wall in walls:
            if snake_head_rect.colliderect(wall):
                print("Hit Wall")
                run_game()
        for body in snake_bodies:
            if snake_head_rect.colliderect(body):
                print("Hit Body")
                run_game()
        for food in food_location:
            food_x, food_y = food
            if snake_head_rect.collidepoint(food_x, food_y):
                print("Ate Food")
                add_body()
                food_location.remove(food)
                delay -+ 0.01
                if food_location == []:
                    level += 1
                    for l in range(level):
                        place_food()
        return level, delay

    def add_body():
        snake_bodies.append(snake_bodies[-1])

    def place_food():
        food_location.append([random.randrange(15,1185,15) + 8, random.randrange(15,735,15) + 8])


    pg.init()
    screen = pg.display.set_mode((1200, 750))
    pg.display.set_caption("Snake")

    bg_color = (230,230,230)
    screen.fill(bg_color)

    #set up screen objects
    #(x, y, w, h)
    snake_head_rect = pg.Rect(600, 375, 15, 15)
    snake_bodies = [(snake_head_rect.x+3, snake_head_rect.y+3,10,10)]
    walls = [(0, 0, 1200, 15), (1185, 0, 15, 750), (0, 0, 15, 750), (0, 735, 1200, 15)]
    food_location = [(random.randrange(15,1185,15) + 8, random.randrange(15,735,15) + 8)]

    color = (100,100,100)

    current_time = time.time()
    direction = "RIGHT"
    delay = 1.0
    level = 1

    # Main Loop
    while True:
        # Even Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if direction == "LEFT":
                        pass
                    else:
                        direction = "RIGHT"
                elif event.key == pg.K_LEFT:
                    if direction == "RIGHT":
                        pass
                    else:
                        direction = "LEFT"
                elif event.key == pg.K_UP:
                    if direction == "DOWN":
                        pass
                    else:
                        direction = "UP"
                elif event.key == pg.K_DOWN:
                    if direction == "UP":
                        pass
                    else:
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
        for food in food_location:
            (x, y) = food
            pg.draw.circle(screen,(200,0,200),(x, y), 7)
        for w in range(0,1200,15):
            pg.draw.line(screen,(220,220,220),(w,0),(w,750),1)
        for h in range(0,800,15):
            pg.draw.line(screen,(220,220,220),(0,h),(1200,h),1)
        for body in snake_bodies:
            (x, y, w, h) = body
            pg.draw.rect(screen, color, pg.Rect(x, y, w, h))
        for wall in walls:
            (x, y, w, h) = wall
            pg.draw.rect(screen, (0, 0, 0),pg.Rect(x, y, w, h))
        if time.time() - current_time >= delay:
            current_time = time.time()
            current_level, current_delay = move(direction, level, delay)
            level, delay = current_level, current_delay

run_game()
