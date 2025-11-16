import pygame
from utils import resource_path
class Counter:

    def __init__(self):
        self.count = 0
        self.x = 10
        self.y = 10
        self.size = 30

        self.font = pygame.font.Font(resource_path('assets/fonts/PressStart2P.ttf'), self.size)
        self.surface = self.font.render(f'{self.count}', False, 'goldenrod2')

    def update(self):
        self.count += 1
        self.surface = self.font.render(f'{self.count}', False, 'goldenrod2')

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def reset(self):
        self.count = 0
        self.surface = self.font.render(f'{self.count}', False, 'goldenrod2')

