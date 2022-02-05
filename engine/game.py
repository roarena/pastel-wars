import pygame
import sys

from engine.C import WIDTH, HEIGHT, GAME_NAME, FPS
from engine.components.screens.game_screen import GameScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)

        self.font = pygame.font.Font(None, 50)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.x = 400
        self.clock = pygame.time.Clock()
        self.game_screen = GameScreen()

    def run(self):
        while True:
            self.screen.fill('black')

            self.game_screen.run()

            pygame.display.update()
