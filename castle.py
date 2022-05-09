import pygame
import math


class Castle:
    def __init__(self, imager, pos, screen, player_number, color):
        self.health = 1200
        self.max_health = self.health
        self.img = imager.getCastleImage(0, player_number)
        self.imager = imager
        self.player_number = player_number
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
        self.color = color
        self.pos = pos

    #         ----------Draw castle ------------------
    '''In draw_castle function when the health of castle decrease the images changes accordingly'''

    def draw_castle(self):
        # to check which image should be used when health dropped
        if self.health <= 600:
            self.img = self.imager.getCastleImage(1, self.player_number)
        elif self.health <= 300:
            self.img = self.imager.getCastleImage(2, self.player_number)
        else:
            self.img = self.imager.getCastleImage(0, self.player_number)

        self.screen.blit(self.img, self.rect)

    # ----------------------- Implementation of damage castle function

    def draw_health_bar(self):
        """
        draw health bar above unit
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
        x, y, z = self.color
        draw_health_bar(self.screen, health_rect.topleft, health_rect.size, x, y, z, self.health/self.max_health)

    def reduceHealth(self, hit_amount=50):
        """
        The function that makes castle take a hit
        :param reduce_amount: int
        :return: None
        """
        self.health -= hit_amount

    def isDead(self):
        """
        Checks if the castle does not have health.
        :return: bool
        """
        return self.health <= 0

    def collide(self, movingObject):
        """
        Checks if the objects collide or not.
        :return: bool
        """
        x2 = movingObject.pos[0]
        y2 = movingObject.pos[1]
        dis = math.sqrt((x2 - self.pos[0]) ** 2 + (y2 - self.pos[1]) ** 2)
        if dis >= 100:
            return False
        else:
            return True

    def updateRect(self):
        """
        Changes the _rect.
        :return: None
        """
        self.rect.x, self.rect.y = self.pos

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.pos = (x, y)
        self.updateRect()

    @property
    def isInappropriate(self) -> bool:
        """
        Checks if the position is correct.
        :return: bool
        """
        if self.pos[0] > 600 - 25 or self.pos[1] > 600 - 35 or self.pos[0] < 50 or self.pos[1] < 50:
            return True
        return False

    @staticmethod
    def getType():
        """
        Returns the class name.
        :return: string
        """
        return "Castle"
