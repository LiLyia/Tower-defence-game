from __future__ import annotations
import pygame
import unit
from projectile import *
import projectile
# -------FireTower Basic Features-------------------------#
'''
@Elbir Erberk
'''

DEFAULT_TOWER_PRICE: int = 150
DEFAULT_TOWER_HEALTH: int = 600
DEFAULT_HIT: int = 1
DEFAULT_UPGRADE_PERCENT: float = 0.15
DEFAULT_LEVEL: int = 0
DEFAULT_SCALE = 0.09

# -----------------Extra features for FireTower-------------------------------#
DEFAULT_RANGE = 40
DEFAULT_DAMAGE = 40
DEFAULT_DAMAGE_UPGRADE_PERCENT: float = 0.27
DEFAULT_RANGE_UPGRAGE_PERCENT: float = 0.02

"""
Implementing FireTower
"""


class FireTower:
    '''
    The function that creates the tower
     without the need for other constant values
    '''

    @classmethod
    def createTower(cls, pos: tuple[int], image_list: list[[pygame.Surface]], screen: pygame.Surface) -> FireTower:
        return cls(pos=pos, image_list=image_list, screen=screen)

    def __init__(self, pos: tuple[int],
                 image_list: list[[pygame.Surface]],
                 screen: pygame.Surface,
                 damage: int = DEFAULT_DAMAGE,
                 range: int = DEFAULT_RANGE,
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

        self._pos: tuple[int] = pos
        self._rect = self.towerImage.get_rect()
        self._rect.x, self._rect.y = pos

        self._range = range
        self._damage = damage
        self.hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        self.targetList = []
        self.bulletList = []
        self.current_target = None
        self.current_cd = 0
        self.cd = 150
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
    def setRange(self, range) -> None:
        self._range = range

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
        return self._screen

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
        return self._rect

    # ---------Extras for Attack Tower---------#
    @property
    def damage(self) -> int:
        return self._damage

    @property
    def range(self) -> int:
        return self._range

    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        self.setHealth(self.health - reduce_amount)
        self.declareHealthLevel()

    def isDead(self) -> bool:
        return not self.health > 0

    # According to the percentages given, the tower's health, range, level, and
    # level-appropriate picture are determined here.

    def upgrade(self, upgrade_percent: float = DEFAULT_UPGRADE_PERCENT):
        self.setDamage(self.damage * (1 + DEFAULT_DAMAGE_UPGRADE_PERCENT))
        self.setRange(self.range * (1 + DEFAULT_RANGE_UPGRAGE_PERCENT))
        self.setLevel(self.level + 1)
        self.setMaxHealth(self.maxHealth * (1 + upgrade_percent))
        self.setHealth(self.health * (1 + upgrade_percent))
        self.declareHealthLevel()

    def remove(self):
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

    '''
    Adds the tower to the Map
    '''

    def draw_tower(self):
        self.screen.blit(self.towerImage, self.rect)
        self.hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 1)

    # Functions to be used for attack.
    # Extra features will be added for Shooting and Hitbox

    '''
    reduceHealth function defined to reduce the enemy's health
    or kill enemys
    '''

    def reduceHealthEnemy(self, enemy: unit):
        if (enemy.health - self.damage) < 0:
            enemy.health = 0
        else:
            enemy.health -= self.damage


    def check_cd(self):
        if self.current_cd > 0:
            return False
        return True

    
    def shoot(self):
        if self.check_cd() and self.current_target != None:
            self.bulletList.append(Projectile(self.pos[0],self.pos[1],self.current_target,self.damage))
            self.current_cd = self.cd
        else :
            self.current_cd -= 1
        for i in self.bulletList:
            if self.current_target != None :
                i.drawToTarget()
                i.hitEnemy()








