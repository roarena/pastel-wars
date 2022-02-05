import pygame
from random import randint

stars_group = pygame.sprite.Group()


class Star(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()

        self.start_x = x or randint(0, 1280)
        self.start_y = y or randint(0, 1280)
        self.x = self.start_x
        self.y = self.start_y

        self.image = pygame.image.load('assets/gfx/star.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
            stars_group.add(Star(x=randint(1200, 1380)))


class Background:

    def __init__(self):
        max_stars = 300

        while len(stars_group) < max_stars:
            stars_group.add(Star())

    def draw(self):
        stars_group.draw(pygame.display.get_surface())
        stars_group.update()
