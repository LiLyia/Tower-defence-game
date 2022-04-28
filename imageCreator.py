from __future__ import annotations
import pygame
from os import listdir
from os.path import isfile, join

DEFAULT_BACKGROUND_IMAGE_NUMBER: int = 5
DEFAULT_SCALE = 0.12

"""
    This document is created to create images and return them to required classes
    @author = Harun Eren MUTLU 
"""

class ImageCreator:
    @classmethod
    def createImageCreator(cls, filePath: str):
        return cls(filePath=filePath)

    def __init__(self, filePath: str):
        self._towerList: list[[[pygame.Surface]]] = [[[None for _ in range(3)] for _ in range(3)] for _ in range(2)]
        self._unitList: list[[pygame.Surface]] = [[None for _ in range(4)] for _ in range(2)]
        self._hurdleList: list[[pygame.Surface]] = [None for _ in range(5)]
        self._casteList: list[[pygame.Surface]] = [[None for _ in range(3)] for _ in range(2)]
        self._backGroundList: list[[pygame.Surface]] = [None for _ in range(DEFAULT_BACKGROUND_IMAGE_NUMBER)]
        self._createEverything(filePath)

    def setTowerList(self, healthLevel: int, towerType: int, playerNumber: int, image: pygame.Surface) -> None:
        self._towerList[playerNumber][towerType][healthLevel] = image

    def setHurdleList(self, index: int, image: pygame.Surface):
        self._hurdleList[index] = image

    def setCastleList(self, index: int, playerNumber: int, image: pygame.Surface):
        self._casteList[playerNumber][index] = image

    def setUnitList(self, unitType: int, playerNumber: int, image: pygame.Surface):
        self._unitList[playerNumber][unitType] = image

    def setBackgroundList(self, index: int, image: pygame.Surface):
        self._backGroundList[index] = image

    def _createEverything(self, filePath: str):
        self._createTowerImages(filePath)
        self._createHurdleImages(filePath)
        self._createUnitImages(filePath)
        self._createBackgroundImages(filePath)
        self._createCastleImages(filePath)

    def _createTowerImages(self, filePath: str, scale:float = DEFAULT_SCALE):
        towerImageNames: list[str] = [x for x in listdir(f'{filePath}/Towers') if
                                      isfile(join(f'{filePath}/Towers', x))]
        for towerImageName in towerImageNames:
            if 'png' in towerImageName:
                image: pygame.Surface = self.scaleImage(pygame.image.load(f'{filePath}/Towers/{towerImageName}').convert_alpha(), scale)
                if 'blue' in towerImageName:
                    if 'fire' in towerImageName:
                        if '1' in towerImageName:
                            self.setTowerList(0, 1, 1, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 1, 1, image)
                        else:
                            self.setTowerList(2, 1, 1, image)
                    elif 'slower' in towerImageName:
                        if '1' in towerImageName:
                            self.setTowerList(0, 2, 1, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 2, 1, image)
                        else:
                            self.setTowerList(2, 2, 1, image)
                    else:
                        if '1' in towerImageName:
                            self.setTowerList(0, 0, 1, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 0, 1, image)
                        else:
                            self.setTowerList(2, 0, 1, image)
                else:
                    if 'fire' in towerImageName:
                        if '1' in towerImageName:
                            self.setTowerList(0, 1, 0, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 1, 0, image)
                        else:
                            self.setTowerList(2, 1, 0, image)
                    elif 'slower' in towerImageName:
                        if '1' in towerImageName:
                            self.setTowerList(0, 2, 0, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 2, 0, image)
                        else:
                            self.setTowerList(2, 2, 0, image)
                    else:
                        if '1' in towerImageName:
                            self.setTowerList(0, 0, 0, image)
                        elif '2' in towerImageName:
                            self.setTowerList(1, 0, 0, image)
                        else:
                            self.setTowerList(2, 0, 0, image)

    def _createHurdleImages(self, filePath: str):
        hurdleImageNames: list[str] = [x for x in listdir(f'{filePath}/Hurdles') if
                                       isfile(join(f'{filePath}/Hurdles', x))]
        for hurdleImageName in hurdleImageNames:
            if 'png' in hurdleImageName:
                image: pygame.Surface = pygame.image.load(f'{filePath}/Hurdles/{hurdleImageName}').convert_alpha()
                if 'dirt' in hurdleImageName:
                    self.setHurdleList(0, image)
                else:
                    index: int = int(hurdleImageName.split('_')[1][0])
                    self.setHurdleList(index, image)

    def _createCastleImages(self, filePath: str, scale:float = 0.09):
        castleImageNames: list[str] = [x for x in listdir(f'{filePath}/Castle') if
                                       isfile(join(f'{filePath}/Castle', x))]
        for castleImageName in castleImageNames:
            if 'png' in castleImageName:
                image: pygame.Surface = self.scaleImage(pygame.image.load(f'{filePath}/Castle/{castleImageName}').convert_alpha(), scale)
                if 'castle1' in castleImageName:
                    if '25' in castleImageName:
                        self.setCastleList(2, 0, image)
                    elif '50' in castleImageName:
                        self.setCastleList(1, 0, image)
                    else:
                        self.setCastleList(0, 0, image)
                else:
                    if '25' in castleImageName:
                        self.setCastleList(2, 1, image)
                    elif '50' in castleImageName:
                        self.setCastleList(1, 1, image)
                    else:
                        self.setCastleList(0, 1, image)

    def _createUnitImages(self, filePath, scale:float = DEFAULT_SCALE):
        unitImageNames: list[str] = [x for x in listdir(f'{filePath}/Units') if
                                           isfile(join(f'{filePath}/Units', x))]
        for unitImageName in unitImageNames:
            if 'png' in unitImageName:
                #image: pygame.Surface = self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), scale)
                if 'red' in unitImageName:
                    if 'uvso' in unitImageName:
                        self.setUnitList(1, 1, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.28))
                    elif 'uvsu' in unitImageName:
                        self.setUnitList(2, 1, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.22))
                    elif 'basic' in unitImageName:
                        self.setUnitList(3, 1, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.28))
                    else:
                        self.setUnitList(0, 1, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.07))
                else:
                    if 'uvso' in unitImageName:
                        self.setUnitList(1, 0, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.28))
                    elif 'uvsu' in unitImageName:
                        self.setUnitList(2, 0, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.22))
                    elif 'basic' in unitImageName:
                        self.setUnitList(3, 0, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.28))
                    else:
                        self.setUnitList(0, 0, self.scaleImage(pygame.image.load(f'{filePath}/Units/{unitImageName}').convert_alpha(), 0.07))


    def _createBackgroundImages(self, filePath, scale:float = 1.0):
        backgroundImageNames: list[str] = [x for x in listdir(f'{filePath}/Background') if
                                       isfile(join(f'{filePath}/Background', x))]
        for backgroundImage in backgroundImageNames:
            if 'png' in backgroundImage:
                image: pygame.Surface = self.scaleImage(pygame.image.load(f'{filePath}/Background/{backgroundImage}').convert_alpha(), scale)
                self.setBackgroundList(int(backgroundImage.split('.')[0][-1])-1, image)

    def getTowerImage(self, healthLevel: int, towerType: int, playerNumber: int):
        """

        :param healthLevel: int -> 0..2| 0 for full 2 for full/4
        :param towerType: int -> 0 for basicTower 1 for fireTower 2 for slowingTower
        :param playerNumber: int -> 0 for red 1 for blue
        :return:
        """
        return self._towerList[playerNumber][towerType][healthLevel]

    def getUnitImage(self, unitType: int, playerNumber: int):
        """

        :param unitType: int -> 0 for soldier 1 for uvso 2 for uvsu 3 for basic
        :param playerNumber: int -> 0 for red 1 for blue
        :return:
        """
        return self._unitList[playerNumber][unitType]

    def getBackgroundImage(self, index: int):
        """

        :param index: int -> 0 for bg_1 and goes on
        :return:
        """
        return self._backGroundList[index]

    def getCastleImage(self, index: int, playerNumber: int):
        """

        :param index: int -> 0..2| 0 for full_health 2 for full/4
        :param playerNumber: int -> 0 for red 1 for blue
        :return:
        """
        return self._casteList[playerNumber][index]

    def getHurdleImage(self, index: int):
        """

        :param index: int -> 0..# 0 for dirt and so on
        :return:
        """
        return self._hurdleList[index]

    def scaleImage(self, img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        '''
        The function that scales images according to some scale
        :param img: pygame.Surface
        :param scale: float
        :return: pygame.Surface
        '''
        width = img.get_width()
        height = img.get_height()
        return pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def scaleWithWidthAndHeight(self, img, width, height) -> pygame.Surface:
        """
        The function that scales images according to given width and height
        :param img: pygame.Surface
        :param width: int
        :param height: int
        :return: pygame.Surface
        """
        return pygame.transform.scale(img, (width, height))


