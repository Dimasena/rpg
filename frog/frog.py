import pygame as pg
import sys


class Frog(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.current_image = 0
        self.animating = False
        for i in range(1, 11):
            self.sprites.append(pg.image.load(f'frog/attack_{i}.png'))
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()

    def update(self):
        if self.animating:
            if self.current_image >= len(self.sprites)-1:
                self.current_image = 0
                self.animating = False
            self.current_image += 0.25
            self.image = self.sprites[int(self.current_image)]



pg.init()
clock = pg.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Sprite Animation")

# Creating the sprites and groups
frog_group = pg.sprite.Group()
frog = Frog()
frog_group.add(frog)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                frog.animating = True

    # Drawing
    screen.fill((255,255,255))
    frog_group.draw(screen)
    frog_group.update()
    pg.display.flip()
    clock.tick(60)
