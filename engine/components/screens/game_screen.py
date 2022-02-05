import sys

import pygame

from engine.C import WIDTH, FPS
from engine.components.Enemy import Enemy
from engine.components.background import Background
from engine.components.bullet import Bullet
from engine.components.engine_smoke import EngineSmoke
from engine.components.player import Player


class GameScreen:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.background = Background()
        self.font = pygame.font.Font(None, 50)
        self.clock = pygame.time.Clock()
        self.start_time = int(pygame.time.get_ticks() / 1000)
        self.score = 0

        self.engine_smoke = pygame.sprite.Group()
        self.engine_smoke.add(EngineSmoke(140, 335))
        self.engine_smoke.add(EngineSmoke(140, 365))

        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.engine_smoke, self.bullets))

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def menu_bar(self):
        pygame.draw.rect(self.display_surface, (64, 64, 64), (0, 0, WIDTH, 60))

    def display_score(self):
        score_surf = pygame.font.Font(None, 30).render(f'Score: {int(self.score)}', False, 'Lime')
        score_rect = score_surf.get_rect(center=(WIDTH / 2, 30))
        self.display_surface.blit(score_surf, score_rect)

    def display_fps(self):
        fps_surf = pygame.font.Font(None, 30).render(f'FPS: {int(self.clock.get_fps())}', False, 'Lime')
        fps_rect = fps_surf.get_rect(midleft=(15, 30))
        self.display_surface.blit(fps_surf, fps_rect)

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.enemys, False):
            print('player morreu')
            return False
        else:
            return True

    def collision_bullet(self):
        if pygame.sprite.groupcollide(self.enemys, self.bullets, True, True):
            return False
        else:
            return True

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.obstacle_timer:
                self.enemys.add(Enemy())

        self.score = int(pygame.time.get_ticks() / 1000) - self.start_time
        self.background.draw()

        self.collision_sprite()
        self.collision_bullet()
        self.menu_bar()
        self.display_score()
        self.display_fps()

        self.engine_smoke.draw(self.display_surface)
        self.engine_smoke.update()

        self.player.draw(self.display_surface)
        self.player.update()

        self.bullets.draw(self.display_surface)
        self.bullets.update()

        self.enemys.draw(self.display_surface)
        self.enemys.update()



        self.clock.tick(FPS)



