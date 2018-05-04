import pygame
import math
from gamepy import guy
black = (255, 0, 0)
class Bullet(pygame.sprite.Sprite):

    def __init__(self, mouse, player):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 10])
        self.image.fill(black)

        self.mouse_x, self.mouse_y = mouse[0], mouse[1]
        self.player = player

        self.rect = self.image.get_rect()
    def update(self):

        speed = 4.
        range = 200
        distance = [self.mouse_x - self.player[0], self.mouse_y - self.player[1]]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]
        bullet_vector = [direction[0] * speed, direction[1] * speed]


        self.rect.x -= bullet_vector[0]
        self.rect.y -= bullet_vector[1]

    bullet = Bullet(pygame.mouse.get_pos(), [guyImg.rect.x, guyImg.rect.y])