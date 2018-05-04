
import pygame
from bullet import Bullet


class Guy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('redneck.png')
        self.image = pygame.transform.scale(self.image, (100,75))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -25
        self.bullets = []
        self.x = x 
        self.y = y
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def shoot(self):
        bullet = Bullet(self.x, self.y) 
        self.bullets.append(bullet)
    def move(self, x):
        self.x = self.x + x