import pygame as pg
from pygame.math import Vector2


class Sheet():
    def __init__(self, image, scale_factor=1):
        self.image = pg.image.load(f'images/sheet.png').convert_alpha()
        self.scale_factor = scale_factor
        if self.scale_factor != 1:
            self.size = self.image.get_rect().size
            self.target_size = (self.size[0] * self.scale_factor, self.size[1] * scale_factor)
            self.image = pg.transform.scale(self.image, self.target_size)


    def get_image(self, x, y, width, height):
        """Return an image cut out from the object's spritesheet."""
        image = self.image.subsurface(x, y, width, height)
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, spritesheet, pos):
        super().__init__()
        self.current_image = 0
        self.image = spritesheet.get_image(0, 0, 64, 64)
        self.rect = self.image.get_rect()
        self.load_images(spritesheet)
        self.velocity = Vector2(0, 0)

        self.frame = 0
        self.last_update = 0
        self.animation_cycle = self.up_move

    def load_images(self, spritesheet):
        self.right_move = []
        self.left_move = []
        self.up_move = []
        self.down_move = []

        w, h = 128, 128
        for x in range(0, 512, 128):
            self.down_move.append(spritesheet.get_image(x, 0, w, h))
            self.left_move.append(spritesheet.get_image(x, 128, w, h))
            self.right_move.append(spritesheet.get_image(x, 256, w, h))
            self.up_move.append(spritesheet.get_image(x, 384, w, h))


    def animate(self, frame_length=100):
        now = pg.time.get_ticks()   # Получаем время с инициализации pygame
        if now - self.last_update >= frame_length:
            self.last_update = now

            if self.velocity.x > 0:
                self.animation_cycle = self.right_move
            if self.velocity.x < 0:
                self.animation_cycle = self.left_move
            if self.velocity.y > 0:
                self.animation_cycle = self.down_move
            if self.velocity.y < 0:
                self.animation_cycle = self.up_move
            if self.velocity == Vector2(0, 0):
                self.frame = -1

            # self.frame += 1
            # if self.frame >= len(self.animation_cycle):
            #     self.frame = 0
            self.frame = (self.frame + 1) % len(self.animation_cycle)
            self.image = self.animation_cycle[self.frame]

    def move(self):
        self.velocity = Vector2(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.velocity.x = 1
        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_s]:
            self.velocity.y = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        self.rect.center += self.velocity * 5
