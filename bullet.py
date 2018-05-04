
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cat.png')
        self.image = pygame.transform.scale(self.image, (75,60))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -2
        
        print('bullet created')
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.rect.x, self.rect.y))
        print(self.rect.x, self.rect.y)