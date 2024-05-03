import pygame
from pygame import rect
import sys

class Button:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = (x, y)

    def resize(self, scale):
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def change_pos(self, x, y):
        self.pos = (x, y)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


    def displayButton(self, screen):
        screen.blit(self.image, self.pos)

    def checkCollision(self, screen, pos):
        if self.rect.collidepoint(pos):
            return True

        return False
