from const import *
import pygame
from utils import resource_path


class Player:

    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.size = 48
        self.speed = 8

        self.dashing = False

        self.invulnerable = False
        self.invuln_timer = 0

        self.normal_image = pygame.image.load(resource_path('assets/player.png')).convert_alpha()
        self.invuln_image = pygame.image.load(resource_path('assets/player_invulnerable.png')).convert_alpha()

        self.image = self.normal_image

    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.get_rect())

    def update(self):

        if self.invulnerable:
            self.image = self.invuln_image
            self.invuln_timer -= 1
            if self.invuln_timer <= 0:
                self.invulnerable = False
                self.image = self.normal_image

        if self.dashing:
            speed = 8 * 30
        else:
            speed = self.speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0 + self.size/2:
                self.y -= speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.size/2:
                self.y += speed
        if keys[pygame.K_LEFT] and self.x > 0 + self.size/2:
                self.x -= speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.size/2:
                self.x += speed

        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.size/2
        if self.x < 0 + self.size/2:
            self.x = self.size/2

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.size/2
        if self.y < 0:
            self.y = self.size/2

        self.dashing = False


