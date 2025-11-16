from const import *
import pygame
import random
from utils import resource_path

class Coin:

    def __init__(self):
        self.size = 48
        self.x = random.randint(24 , SCREEN_WIDTH - self.size/2)
        self.y = random.randint(24 , SCREEN_HEIGHT - self.size/2)

        self.image = pygame.image.load(resource_path('assets/coin.png')).convert_alpha()

    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.get_rect())

    def update(self, other_rect, counter):
        if self.get_rect().colliderect(other_rect):
            self.respawn()
            counter.update()
            return True
        return False

    def respawn(self):
        self.x = random.randint(10, SCREEN_WIDTH - self.size * 2)
        self.y = random.randint(10, SCREEN_HEIGHT - self.size * 2)