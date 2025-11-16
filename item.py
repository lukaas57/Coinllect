from const import *
import random
import pygame
from utils import *

class Item:

    # TODO:
    # mozno spravit inventar na itemy alebo budu insta use
    # PICKAXE pre znicenie nejakeho spiku
    # SHIELD prezije jeden naraz spiku
    # POTION na invulnerable, na speed, na slow spiky na chvilu
    # MAGNET na coiny
    # nejaka vec ktora vystreli po minci
    # LEGENDARY ITEM na reset spikov na 1

    def __init__(self):
        self.size = 48
        self.x = random.randint(24, SCREEN_WIDTH - self.size / 2)
        self.y = random.randint(24, SCREEN_HEIGHT - self.size / 2)

        self.timer = 0

        self.used = False

        self.spawn = False

        self.item = random.randint(0,0)

        # 0 speed potion
        if self.item == 0:
            self.image = pygame.image.load(resource_path('assets/potion.png')).convert_alpha()


    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.get_rect())

    def update(self, other_rect, player, items):
        if self.get_rect().colliderect(other_rect):
            self.used = True
            self.spawn = False
            player.speed = 12
            self.timer = FPS * 3

            self.x = 1000
            self.y = 1000
            return True

        if self.used:
            self.timerCountdown(player, items)

        return False


    def timerCountdown(self, player, items):
        self.timer -= 1

        if self.timer <= 0:
            player.speed = 8
            items.remove(self)
            self.used = False
            self.timer = 0