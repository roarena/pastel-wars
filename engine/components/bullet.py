import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        bullet_1 = pygame.image.load('assets/gfx/ship/shot5_1.png').convert_alpha()
        bullet_2 = pygame.image.load('assets/gfx/ship/shot5_2.png').convert_alpha()
        bullet_3 = pygame.image.load('assets/gfx/ship/shot5_3.png').convert_alpha()
        bullet_4 = pygame.image.load('assets/gfx/ship/shot5_4.png').convert_alpha()
        bullet_5 = pygame.image.load('assets/gfx/ship/shot5_5.png').convert_alpha()
        bullet_stand = pygame.image.load('assets/gfx/ship/shot_stand.png').convert_alpha()

        self.engine_animation = [bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_stand]
        self.animation_index = 0

        self.image = self.engine_animation[self.animation_index]
        self.rect = self.image.get_rect(center=(x, y))

    def animation_state(self):
        self.animation_index += 0.3
        if self.animation_index >= len(self.engine_animation) - 1: self.animation_index = 5
        self.image = self.engine_animation[int(self.animation_index)]

    def move_bullet(self):
        self.rect.x += 5

    def destroy(self):
        if self.rect.x >= 1300:
            self.kill()

    def update(self):
        self.animation_state()
        self.move_bullet()
        self.destroy()
