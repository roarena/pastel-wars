import pygame


class EngineSmoke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        engine_smoke_1 = pygame.image.load('assets/gfx/ship/exhaust1.png').convert_alpha()
        engine_smoke_2 = pygame.image.load('assets/gfx/ship/exhaust2.png').convert_alpha()
        engine_smoke_3 = pygame.image.load('assets/gfx/ship/exhaust3.png').convert_alpha()
        engine_smoke_4 = pygame.image.load('assets/gfx/ship/exhaust4.png').convert_alpha()

        self.engine_animation = [engine_smoke_1, engine_smoke_2, engine_smoke_3, engine_smoke_4]
        self.animation_index = 0

        self.image = self.engine_animation[self.animation_index]
        self.rect = self.image.get_rect(center=(x, y))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.engine_animation): self.animation_index = 0
        self.image = self.engine_animation[int(self.animation_index)]

    def update(self):
        self.animation_state()
