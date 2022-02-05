import pygame

from engine.components.bullet import Bullet
from engine.components.engine_smoke import EngineSmoke


class Player(pygame.sprite.Sprite):
    def __init__(self, engine_smoke, bullets):
        super().__init__()
        self.engine_smoke = engine_smoke
        self.bullets = bullets
        self.image = pygame.image.load('assets/gfx/ship/Ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(200, 350))
        self.can_shoot = True

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y > 40:
            for engine_smoke in self.engine_smoke:
                engine_smoke.rect.y -= 5
            self.rect.y -= 5

        if keys[pygame.K_DOWN] and self.rect.y < 600:
            for engine_smoke in self.engine_smoke:
                engine_smoke.rect.y += 5
            self.rect.y += 5

        if keys[pygame.K_SPACE]:
            if self.can_shoot:
                self.bullets.add(Bullet(self.rect.right + 30, self.rect.centery - 5))
                self.can_shoot = False

        if not keys[pygame.K_SPACE] and not self.can_shoot:
            self.can_shoot = True

    def update(self):
        self.player_input()
