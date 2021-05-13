import pygame as pg


pg.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_color = 'white'

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill(bg_color)




    pg.display.flip()
