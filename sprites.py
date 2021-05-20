import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('Mage Idle (1).png')
        self.image = pg.transform.scale(self.image, (50, 52))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += 2
        if keys[pg.K_w]:
            self.rect.y -= 2
        if keys[pg.K_s]:
            self.rect.y += 2
        if keys[pg.K_a]:
            self.rect.x -= 2
