import pygame as pg
import sprites as sp


pg.init()
clock = pg.time.Clock()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_color = (255, 102, 0)

player = sp.Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
player_group = pg.sprite.GroupSingle()
player_group.add(player)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill(bg_color)

    player_group.draw(screen)
    player_group.update()

    clock.tick(60)
    pg.display.flip()
