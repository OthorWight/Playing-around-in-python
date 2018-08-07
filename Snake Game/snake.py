import sys
import pygame as pg
import time
import random

def run_game():

    def move(direction,level,delay,score):
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
                score += 1
                delay -= delay/50
                if food_location == []:
                    level += 1
                    add_wall()
                    for l in range(level):
                        add_food()
        return level, delay, score

    def add_wall():
        wall_direction = random.randrange(0,2,1)
        if wall_direction == 0: #horizontal
            x = random.randrange(15, 1170, 15)
            y = random.randrange(15, 735, 15)
            w = random.randrange(15, 1185-x, 15)
            h = 15
            wall_collide = False
            for wall in walls:
                wl = pg.Rect(x,y,w,h)
                if wl.colliderect(wall):
                    wall_collide = True
            if not wall_collide:
                if w-15 < 30:
                    add_wall()
                else:
                    walls.append([x+15,y,w-15,h])
            else:
                add_wall()
        if wall_direction == 1: #vertical
            x = random.randrange(15, 1185, 15)
            y = random.randrange(15, 720, 15)
            w = 15
            h = random.randrange(15, 735-y, 15)
            wall_collide = False
            for wall in walls:
                wl = pg.Rect(x,y,w,h)
                if wl.colliderect((wall)):
                    wall_collide = True
            if not wall_collide:
                if h-15 < 30:
                    add_wall()
                else:
                    walls.append([x,y+15,w,h-15])
            else:
                add_wall()

    def add_food():
        x = random.randrange(15,1185,15) + 8
        y = random.randrange(15,735,15) + 8
        wall_collide = False
        for wall in walls:
            wl = pg.Rect(wall)
            if wl.collidepoint(x, y):
                wall_collide = True
        if not wall_collide:
            food_location.append([x, y])
        else:
            add_food()

    def add_body():
        snake_bodies.append(snake_bodies[-1])

    pg.init()
    screen = pg.display.set_mode((1200, 750))
    pg.display.set_caption("Snake")

    bg_color = (230,230,230)
    screen.fill(bg_color)

    myfont = pg.font.SysFont("monospace", 13, 1)

    #set up screen objects
    #(x, y, w, h)
    snake_head_rect = pg.Rect(600, 375, 15, 15)
    snake_bodies = [(snake_head_rect.x+3, snake_head_rect.y+3,10,10)]
    for l in range(9):
        add_body()
    walls = [(0, 0, 1200, 15), (1185, 0, 15, 750), (0, 0, 15, 750), (0, 735, 1200, 15)]
    for l in range(5):
        add_wall()
    food_location = [(random.randrange(15,1185,15) + 8, random.randrange(15,735,15) + 8)]

    color = (100,100,100)

    current_time = time.time()
    direction = "RIGHT"
    delay = 0.5
    level = 1
    score = 0

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
                    add_food()
                elif event.key == pg.K_3:
                    add_wall()

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
            current_level, current_delay, current_score = move(direction, level, delay, score)
            level, delay, score = current_level, current_delay, current_score
        scoretext = myfont.render("Score: " + str(score) + "        Level: " + str(level),1,(250,250,250))
        screen.blit(scoretext, (1,1))

run_game()
