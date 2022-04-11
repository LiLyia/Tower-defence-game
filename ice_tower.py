


from __future__ import  annotations
import pygame
import unit
from projectile import *
'''
'''
# -------FireTower Basic Features-------------------------#
DEFAULT_TOWER_PRICE: int = 150
DEFAULT_TOWER_HEALTH: int = 600
DEFAULT_UPGRADE_PERCENT: float = 0.15
DEFAULT_LEVEL: int = 0
DEFAULT_SCALE = 0.09
DEFAULT_HIT : int = 20

# -----------------Extra features for Ice Tower-------------------------------#
DEFAULT_SLOW_RATE = 0.3
DEFAULT_SLOW_RATE_UPGRADE_PERCENT : float = 0.3

class IceTower:
    '''
        The function that creates the tower
         without the need for other constant values
        '''

    @classmethod
    def createTower(cls, pos: tuple[int], image_list: list[[pygame.Surface]], screen: pygame.Surface) -> IceTower:
        return cls(pos=pos, image_list=image_list, screen=screen)

    def __init__(self, pos: tuple[int],
                 image_list: list[[pygame.Surface]],
                 screen: pygame.Surface,
                 slowRate : float = DEFAULT_SLOW_RATE,
                 scale: float = DEFAULT_SCALE,
                 price: int = DEFAULT_TOWER_PRICE,
                 health: int = DEFAULT_TOWER_HEALTH,
                 max_health: int = DEFAULT_TOWER_HEALTH,
                 level: int = DEFAULT_LEVEL,
                 ):
        self.image_list = image_list  # List for images to use
        self.screen = screen

        self.price: int = price
        self.health: int = health
        self.max_health: int = max_health

        self.level: int = level
        self.health_level: int = 0

        temp_image: pygame.Surface = image_list[self.level][self.healthLevel]  # How the Tower will look is determined by its Level and Health.
        self.towerImage: pygame.Surface = self.scaleImage(temp_image, scale)

        self.pos: tuple[int] = pos
        self.rect = self.towerImage.get_rect()
        self.rect.x, self._rect.y = pos
        self.hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)

        self.slowRate = slowRate


    def setHealth(self, health) -> None:  # Sets the health
        self._health = health

    def setMaxHealth(self, max_health) -> None:  # Sets the max health
        self._max_health = max_health

    def setPrice(self, price) -> None:  # Sets the price of Tower
        self._price = price

    def setLevel(self, level) -> None:  # Sets the level
        self._level = level

    def setHealthLevel(self, health_level) -> None:  # Set the health level for image
        self._health_level = health_level

    def setDamage(self, damage) -> None:  # Set damage of Attack Tower
        self._damage = damage

    def setSlowRate(self,slow_rate):
        self.slowRate = self.slowRate * (1+slow_rate)



    def setPos(self, pos):
        self._pos = pos

    @property
    def health(self) -> int:  # Returns the Health
        return self._health

    @property
    def maxHealth(self) -> int:  # Returns the Max Health
        return self._max_health

    @property
    def price(self) -> int:  # Return the Price
        return self._price

    @property
    def level(self) -> int:  # Returns the Level
        return self._level

    @property
    def healthLevel(self) -> int:  # Returns the Health Level for image of Tower
        return self._health_level

    @property
    def screen(self) -> pygame.Surface:
        return self.screen

    @property
    def towerList(self) -> list[[pygame.Surface]]:
        return self.image_list

    @property
    def towerImage(self) -> pygame.Surface:
        return self.scaleImage(self.towerList[self.level][self.healthLevel])

    @property
    def pos(self) -> tuple[int]:
        return self._pos

    '''
    rect function returns the position of the tower
    '''

    @property
    def rect(self) -> pygame.Rect:
        return self.rect

    @property
    def slowRate(self):
        return self.slowRate


    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        self.setHealth(self.health - reduce_amount)
        self.declareHealthLevel()

    def isDead(self) -> bool:
        return not self.health > 0

    def upgrade(self, upgrade_percent: float = DEFAULT_UPGRADE_PERCENT):
        self.setSlowRate(DEFAULT_SLOW_RATE_UPGRADE_PERCENT)
        self.setLevel(self.level + 1)
        self.setMaxHealth(self.maxHealth * (1 + upgrade_percent))
        self.setHealth(self.health * (1 + upgrade_percent))
        self.declareHealthLevel()

    def remove(self):
        self.screens.fill((255, 255, 255))


    """
    --------------------------------------------
    """


    def declareHealthLevel(self) -> int:
        if self.health > self.maxHealth / 2:
            self.setHealthLevel(0)
        elif self.health > self.maxHealth / 4:
            self.setHealthLevel(1)
        else:
            self.setHealthLevel(2)

    def scaleImage(self, img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        width = img.get_width()
        height = img.get_height()
        return pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def draw_tower(self):
        self.screen.blit(self.towerImage, self.rect)
        self.hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 1)

    def reduceEnemySpeed(self,enemy:unit):
        """
        The function that reduces the enemy speed according to the slow rate
        :param enemy:unit
        if self.hitbox.colliderect(enemy.hitbox):
            enemy.speed = enemy.speed * (1-  self.slowRate)
            return NULL
        """