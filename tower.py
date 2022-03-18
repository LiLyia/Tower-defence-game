from __future__ import annotations
import pygame

DEFAULT_TOWER_PRICE: int = 100
DEFAULT_TOWER_HEALTH: int = 100
DEFAULT_HIT: int = 1
DEFAULT_UPGRADE_PERCENT: float = 0.15
DEFAULT_LEVEL: int = 0
DEFAULT_SCALE = 0.09


class Tower:

    @classmethod
    def createTower(cls, pos: tuple[int], image_list: list[[pygame.Surface]],screen: pygame.Surface) -> Tower:
        return cls(pos=pos, image_list=image_list, screen= screen)

    def __init__(self, pos: tuple[int],
                 image_list: list[[pygame.Surface]],
                 screen: pygame.Surface,
                 scale: float = DEFAULT_SCALE,
                 price: int = DEFAULT_TOWER_PRICE,
                 health: int = DEFAULT_TOWER_HEALTH,
                 max_health: int = DEFAULT_TOWER_HEALTH,
                 level: int = DEFAULT_LEVEL
                 ):
        self.image_list = image_list
        self._screen = screen
        self._price: int = price
        self._health: int = health
        self._max_health: int = max_health
        self._level: int = level
        self._health_level: int = None
        self.declareHealthLevel()
        temp_image: pygame.Surface = image_list[self.getLevel][self.getHealthLevel]
        self._towerImage: pygame.Surface = self.scaleImage(temp_image, scale)

        self._rect = self.getTowerImage.get_rect()
        self._rect.x, self._rect.y = pos

    def setHealth(self, health) -> None:
        self._health = health

    def setMaxHealth(self, max_health) -> None:
        self._max_health = max_health

    def setPrice(self, price) -> None:
        self._price = price

    def setLevel(self, level) -> None:
        self._level = level

    def setHealthLevel(self, health_level) -> None:
        self._health_level = health_level

    @property
    def getHealth(self) -> int:
        return self._health

    @property
    def getMaxHealth(self) -> int:
        return self._max_health

    @property
    def getPrice(self) -> int:
        return self._price

    @property
    def getLevel(self) -> int:
        return self._level

    @property
    def getHealthLevel(self) -> int:
        return self._health_level

    @property
    def getScreen(self) -> pygame.Surface:
        return self._screen

    @property
    def getTowerList(self) -> list[[pygame.Surface]]:
        return self.image_list

    @property
    def getTowerImage(self) -> pygame.Surface:
        return self.scaleImage(self.getTowerList[self.getLevel][self.getHealthLevel])

    @property
    def getRect(self) -> pygame.Rect:
        return self._rect

    def reduceHealth(self, reduce_amount: int = DEFAULT_HIT) -> None:
        self.setHealth(self.getHealth - reduce_amount)
        self.declareHealthLevel()

    def isDead(self) -> bool:
        return not self.getHealth > 0

    def upgrade(self, upgrade_percent: float = DEFAULT_UPGRADE_PERCENT):
        self.setLevel(self.getLevel + 1)
        self.setMaxHealth(self.getMaxHealth * (1 + upgrade_percent))
        self.setHealth(self.getHealth * (1 + upgrade_percent))
        self.declareHealthLevel()

    def remove(self):
        pass

    def declareHealthLevel(self) -> int:
        if self.getHealth > self.getMaxHealth/2:
            self.setHealthLevel(0)
        elif self.getHealth > self.getMaxHealth/4:
            self.setHealthLevel(1)
        else:
            self.setHealthLevel(2)

    def scaleImage(self, img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        width = img.get_width()
        height = img.get_height()
        return  pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def draw_tower(self):
        self.getScreen.blit(self.getTowerImage, self.getRect)
