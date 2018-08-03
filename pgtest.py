import sys
import pygame as pg

def run_game():
    # init screen
    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("Alien Invasion")

    bg_color = (230,230,230)
    screen.fill(bg_color)

    screen_rect = screen.get_rect()

    bullet_rect = pg.Rect(100,100,3,15)
    color = (100,100,100)
    pg.draw.rect(screen, color, bullet_rect)

    ship = pg.image.load('ship.png')
    ship_rect = ship.get_rect()
    ship_rect.midbottom = screen_rect.midbottom
    # draw ship
    screen.blit(ship, ship_rect)

    # Main Loop
    while True:
        # Even Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    ship_rect.x += 1
                elif event.key == pg.K_LEFT:
                    ship_rect.x -= 1
                elif event.key == pg.K_SPACE:
                    ship.fire_bullet()
                elif event.key == pg.K_q:
                    sys.exit()

        # Refresh
        pg.display.flip()

def blitme(self):
    self.screen.blit(self.image, self.rect)



run_game()