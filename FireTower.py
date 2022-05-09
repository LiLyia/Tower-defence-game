from __future__ import annotations
import unit
from projectile import *
import math
# -------FireTower Basic Features-------------------------#
'''
@Elbir Erberk
'''

DEFAULT_TOWER_PRICE: int = 150
DEFAULT_TOWER_HEALTH: int = 600
DEFAULT_HIT: int = 20
DEFAULT_UPGRADE_PERCENT: float = 0.15
DEFAULT_LEVEL: int = 0
DEFAULT_SCALE = 0.09

# -----------------Extra features for FireTower-------------------------------#
DEFAULT_RANGE = 60
DEFAULT_DAMAGE = 110
DEFAULT_DAMAGE_UPGRADE_PERCENT: float = 0.27
DEFAULT_RANGE_UPGRAGE_PERCENT: float = 0.02

"""
Implementing FireTower
"""


class FireTower:
    """
    The function that creates the tower
     without the need for other constant values
    """

    @classmethod
    def createTower(cls, pos: tuple[int, int], image_list: list[[pygame.Surface]],
                    screen: pygame.Surface, color) -> FireTower:
        return cls(pos=pos, image_list=image_list, screen=screen, color=color)

    def __init__(self, pos: tuple[int, int],
                 image_list: list[[pygame.Surface]],
                 screen: pygame.Surface,
                 color: list[tuple[int, int, int]],
                 damage: int = DEFAULT_DAMAGE,
                 tower_range: int = DEFAULT_RANGE,
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

        self._range = tower_range
        self._damage = damage
        self._hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        self.targetList = []  # for the enemies
        self.bulletList = []  # for the bullets
        self.current_target = None
        self.current_cd = 0
        self.cd = 300  # post-shot standby cooldown
        self.color = color
    # Constructors

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

    # Ramge for Attacking
    def setRange(self, range_tower) -> None:
        self._range = range_tower

    def setPos(self, pos): #Changes the position of the tower
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
    def screen(self) -> pygame.Surface: # Returns the pygame screen
        return self._screen

    @property
    def towerList(self) -> list[[pygame.Surface]]: #Returns the list of tower images
        return self.image_list

    @property
    def towerImage(self) -> pygame.Surface: # Returns the image of the tower
        return self.scaleImage(self.towerList[self.level][self.healthLevel])

    @property
    def pos(self) -> tuple[int, int]: # Returns the current position of the tower
        return self._pos

    @property
    def rect(self) -> pygame.Rect: # Returns the current rectangle position of the tower
        return self._rect

    # ---------Extras for Attack Tower---------#
    @property
    def damage(self) -> int: # Returns the damage of the tower
        return self._damage

    @property
    def range(self) -> int: # Returns the damage range of the tower
        return self._range

    @property
    def hitbox(self) -> int:  # Returns the hitbox
        return self._hitbox

    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        """
        Reduces the amount of health.
        :param: reduce_amount - damage
        :return: None
        """
        self.setHealth(self.health - reduce_amount)
        self.declareHealthLevel()

    def isDead(self) -> bool:
        """
        Checks if the tower does not have health.
        :return: bool
        """
        return not self.health > 0

    # According to the percentages given, the tower's health, range, level, and
    # level-appropriate picture are determined here.

    def remove(self):
        """
        Removes the tower from the screen
        :return: None
        """
        self._screen.fill((255, 255, 255))

    '''
    "DeclareHealthLevel" function written to select pictures according to the health of the tower
    '''

    '''
    e.g : Tower -> Max Health = 100

    Tower = 100 HP -> healthLevel = 0
    Tower = 25HP<x<50  HP -> healthLevel = 1
    Tower = <25HP -> healthLevel = 2
    '''

    def declareHealthLevel(self) -> None:
        if self.health > self.maxHealth / 2:
            self.setHealthLevel(0)
        elif self.health > self.maxHealth / 4:
            self.setHealthLevel(1)
        else:
            self.setHealthLevel(2)

    @staticmethod
    def scaleImage(img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        """
        Scales the image size of the tower.
        :param: img - tower image, scale - the scales for image.
        :return: pygame.image
        """
        width = img.get_width()
        height = img.get_height()
        return pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def draw_tower(self):
        """
        Draws the tower to the map.
        :return: None
        """
        self.screen.blit(self.towerImage, self.rect)
        self._hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self._hitbox, 1)

    # Functions to be used for attack.
    # Extra features will be added for Shooting and Hitbox
    def reduceHealthEnemy(self, enemy: unit):
        """
        reduceHealth function defined to reduce the enemy's health
        or kill enemys
        """
        if (enemy.health - self.damage) < 0:
            enemy.health = 0
        else:
            enemy.health -= self.damage

    def check_cd(self):
        """
        Checks if the current cd is positive.
        :return: None 
        """
        if self.current_cd > 0:
            return False
        return True
    
    def shoot(self):
        """
        Attacks the current target
        :return: None
        """
        if self.check_cd() and self.current_target is not None:
            self.bulletList.append(Projectile(self.pos[0], self.pos[1], self.current_target, self.damage))
            self.current_cd = self.cd
        else:
            self.current_cd -= 1
        for i in self.bulletList:
            if self.current_target is not None:
                i.drawToTarget()
                i.hitEnemy()
                if self.current_target.health - self.damage < 0:
                    self.current_target = None
                    self.bulletList = []  # reset enemy

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self._pos = (x, y)
        self.updateRect()

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

    def updateRect(self):
        """
        Changes the _rect.
        :return: None
        """
        self.rect.x, self.rect.y = self.pos

    @staticmethod
    def getType():
        """
        Returns the class name.
        :return: string
        """
        return "FireTower"

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
