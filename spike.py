from const import *
import pygame
import  random
from utils import resource_path

class Spike:

    def __init__(self):
        self.size = 48
        self.x = random.randint(10, SCREEN_WIDTH - self.size * 2)
        self.y = random.randint(10, SCREEN_HEIGHT - self.size * 2)

        self.speed = random.randint(5, 15)

        self.type = random.randint(0, 1)
        self.type2 = random.randint(0, 1)


        self.image = pygame.image.load(resource_path('assets/spike.png')).convert_alpha()

    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.get_rect())

    def update(self):

        if self.type2 == 0:
            if self.type == 0:
                if self.x < SCREEN_WIDTH + self.size:
                    self.x += self.speed
                else:
                    self.x = 0
            else:
                if self.y < SCREEN_HEIGHT + self.size:
                    self.y += self.speed
                else:
                    self.y = 0
        else:
            if self.type == 0:
                if self.x > 0 - self.size:
                    self.x -= self.speed
                else:
                    self.x = SCREEN_WIDTH
            else:
                if self.y > 0 - self.size:
                    self.y -= self.speed
                else:
                    self.y = SCREEN_HEIGHT


    def collison(self, other_rect):
        if self.get_rect().colliderect(other_rect):
            return True
        else:
            return False
