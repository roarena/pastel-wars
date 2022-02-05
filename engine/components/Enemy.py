import pygame

from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/gfx/pastel.png').convert_alpha()
        self.rect = self.image.get_rect(center=(randint(1300, 2000), randint(100, 680)))

    def move_enemy(self):
        self.rect.x -= 7

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.move_enemy()
        self.destroy()
