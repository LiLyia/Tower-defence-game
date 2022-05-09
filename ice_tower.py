from __future__ import annotations
from projectile import *
import math

# -------FireTower Basic Features-------------------------#
DEFAULT_TOWER_PRICE: int = 200
DEFAULT_TOWER_HEALTH: int = 600
DEFAULT_UPGRADE_PERCENT: float = 0.15
DEFAULT_LEVEL: int = 0
DEFAULT_SCALE: float = 0.09
DEFAULT_HIT: int = 20
DEFAULT_SLOW_RATE_UPGRADE_PERCENT: float = 0.15


class IceTower:
    """
        The function that creates the tower
         without the need for other constant values
    """

    @classmethod
    def createTower(cls, pos: tuple[int, int], image_list: list[[pygame.Surface]],
                    screen: pygame.Surface, color) -> IceTower:
        return cls(pos=pos, image_list=image_list, screen=screen, color=color)

    def __init__(self, pos: tuple[int, int],
                 image_list: list[[pygame.Surface]],
                 screen: pygame.Surface,
                 color: list[tuple[int, int, int]],
                 scale: float = DEFAULT_SCALE,
                 price: int = DEFAULT_TOWER_PRICE,
                 health: int = DEFAULT_TOWER_HEALTH,
                 max_health: int = DEFAULT_TOWER_HEALTH,
                 level: int = DEFAULT_LEVEL,
                 ):
        self.image_list = image_list  # List for images to use
        self._screen = screen

        self._price: int = price
        self._health: int = health
        self._max_health: int = max_health

        self._level: int = level
        self._health_level: int = 0

        temp_image: pygame.Surface = image_list[self.level][self.healthLevel]  # How the Tower will look is determined by its Level and Health.
        self._towerImage: pygame.Surface = self.scaleImage(temp_image, scale)

        self._pos: tuple[int, int] = pos
        self._rect = self.towerImage.get_rect()
        self._rect.x, self._rect.y = pos
        self._hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        self.color = color

    def setHealth(self, health) -> None:  # Sets the health
        self._health = health

    def setMaxHealth(self, max_health) -> None:  # Sets the max health
        self._max_health = max_health

    def setPrice(self, price) -> None:  # Sets the price of Tower
        self._price = price

    def setLevel(self, level) -> None:  # Sets the level
        self._level = level

    def setHealthLevel(self, health_level) -> None:  # Sets the health level for image
        self._health_level = health_level

    def setPos(self, pos): # Sets the position of the tower
        self._pos = pos

    @property
    def health(self) -> int:  # Returns the Health
        return self._health

    @property
    def maxHealth(self) -> int:  # Returns the Max Health
        return self._max_health

    @property
    def price(self) -> int:  # Returns the Price
        return self._price

    @property
    def level(self) -> int:  # Returns the Level
        return self._level

    @property
    def healthLevel(self) -> int:  # Returns the Health Level for image of Tower
        return self._health_level

    @property
    def screen(self) -> pygame.Surface: # Returns the pygame screen
        return self._screen

    @property
    def towerList(self) -> list[[pygame.Surface]]: # Returns the list of images
        return self.image_list

    @property
    def towerImage(self) -> pygame.Surface: # Returns the image of the tower
        return self.scaleImage(self.towerList[self.level][self.healthLevel])

    @property
    def pos(self) -> tuple[int, int]: # Returns the position of the tower
        return self._pos

    @property
    def hitbox(self): # Returns the hitbox
        return self._hitbox

    @property
    def rect(self) -> pygame.Rect: # Return the rect
        return self._rect

    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        """
        The function that makes tower take a hit
        :param reduce_amount: int
        :return: None
        """
        self.setHealth(self.health - reduce_amount)

    def isDead(self) -> bool:
        """
        The function that checks if the tower is that or not
        :return: bool
        """
        return not self.health > 0

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self._pos = (x, y)
        self.updateRect()
        self.updateHitbox()

    def updateRect(self):
        """
        Changes the _rect.
        :return: None
        """
        self.rect.x, self.rect.y = self.pos

    def updateHitbox(self):
        """
        Changes the _hitbox.
        :return: None
        """
        self._hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)

    @staticmethod
    def getType():
        """
        Returns the class name.
        :return: string
        """
        return "SlowingTower"

    def collide(self, otherTower):
        """
        Checks if the towers collide or not.
        :return: bool
        """
        x2 = otherTower.pos[0]
        y2 = otherTower.pos[1]
        dis = math.sqrt((x2 - self.pos[0]) ** 2 + (y2 - self.pos[1]) ** 2)
        if dis >= 100:
            return False
        else:
            return True

    def remove(self):
        """
        Function that removes the tower
        :return:
        """
        self.screen.fill((255, 255, 255))

    @staticmethod
    def scaleImage(img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        """
        The function that scales tower image according to some scale
        :param img: pygame.Surface
        :param scale: float
        :return: pygame.Surface
        """
        width = img.get_width()
        height = img.get_height()
        return pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def draw_tower(self):
        """
        The function for drawing the tower to the map
        :return: None
        """
        self.screen.blit(self.towerImage, self.rect)
        self._hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self._hitbox, 1)

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

        health_rect = pygame.Rect(0, 0, self.towerImage.get_width()*3, 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        x, y, z = self.color
        draw_health_bar(self.screen, health_rect.topleft, health_rect.size, x, y, z, self.health/self.maxHealth)

    @property
    def isInappropriate(self) -> bool:
        """
        Checks if the position is correct.
        :return: bool
        """
        if self.pos[0] > 600 - 25 or self.pos[1] > 600 - 35 or self.pos[0] < 50 or self.pos[1] < 50:
            return True
        return False
