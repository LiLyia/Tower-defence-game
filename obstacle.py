from __future__ import annotations
import pygame
from imageCreator import ImageCreator

DEFAULT_HIT = 2

class Obstacle:
    @classmethod
    def createObstacle(cls, pos, screen, imager, tile_size, image_number=0, health=200, max_health=200):
        return cls(pos=pos, screen=screen, imager=imager, image_number=image_number,
                   tile_size=tile_size, health=health, max_health=max_health)

    def __init__(self, pos, screen, imager, image_number, tile_size, health, max_health):
        self.health = health
        self.max_health = max_health
        self.pos = pos
        self.imager = imager
        # Scale the image
        self.img = imager.scaleWithWidthAndHeight(imager.getHurdleImage(image_number), tile_size, tile_size)

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
        self.hitbox = pygame.Rect(self.pos[0] + 3, self.pos[1] + 8, 40, 40)  # Hitbox area for the units

    def setHealth(self, health):
        self.health = health

    def draw(self):
        """
        Draws the unit with the given images
        """
        self.screen.blit(self.img, self.rect)

    def remove(self):
        """
        Make the unit disappear from the game.
        """
        self.screen.fill((255, 255, 255))

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.pos = (x, y)
        self.updateRect()

    def updateRect(self):
        self.rect.x, self.rect.y = self.pos

    def getType(self):
        return "Hurdle"

    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        '''
        The function that makes tower take a hit
        :param reduce_amount: int
        :return:
        '''
        self.setHealth(self.health - reduce_amount)
        if self.isDead():
            self.remove()

    def isDead(self):
        return self.health <= 0

    def draw_health_bar(self):
        """
        draw health bar above unit
        :param win: surface
        :return: None
        """

        def draw_health_bar(screen, pos, size, borderC, backC, healthC, progress):
            pygame.draw.rect(screen, backC, (*pos, *size))
            pygame.draw.rect(screen, borderC, (*pos, *size), 1)
            innerPos = (pos[0] + 1, pos[1] + 1)
            innerSize = ((size[0] - 2) * progress, size[1] - 2)
            rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
            pygame.draw.rect(screen, healthC, rect)

        health_rect = pygame.Rect(0, 0, self.img.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        x, y, z = [(0, 0, 0), (0, 255, 0), (255, 255, 0)]
        draw_health_bar(self.screen, health_rect.topleft, health_rect.size,
                        x, y, z, self.health / self.max_health)