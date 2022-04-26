from unit import *
from goldmine import *

DEF_BASIC_UNIT_PRICE = 100
DEF_UVSU_PRICE = 100
DEF_UVSO_PRICE = 100
DEF_UVSB_PRICE = 150

DEF_GOLDMINE_PRICE = 100
DEF_BASICTOWER_PRICE = 200
DEF_FIRINGTOWER_PRICE = 200
DEF_SLOWINGTOWER_PRICE = 200
DEF_UPGRADETOWER_PRICE = 200
DEF_ICETOWER_PRICE = 200

class Player:
    def __init__(self, screen, map_data, castle, color, gold = 500):
        self.screen = screen
        self.map_data = map_data
        self.castle = castle
        self.castle_pos = (castle.rect.x, castle.rect.y)
        self.gold = gold
        self.color = color

        self.unit_list = []
        self.tower_list = []
        self.goldmines_list = []

        self.unit_pos = []
        self.tower_pos = []
        self.goldmines_pos = []

    def addUnit(self, type="BasicUnit"):
        pos = self.castle_pos
        x,y = self.__coord_to_index(pos)
        #self.map_data[y][x] = type

        buy = False
        if type == "BasicUnit":
            if(self.gold >= DEF_BASIC_UNIT_PRICE):
                soldier = Unit(pos, self.screen, self.map_data, self.color)
                self.gold -= DEF_BASIC_UNIT_PRICE
                buy = True
        elif type == "vsObstacles":
            if(self.gold >= DEF_UVSO_PRICE):
                soldier = UvsO(pos, self.screen, self.map_data, self.color)
                self.gold -= DEF_UVSO_PRICE
                buy = True
        elif type == "vsTowers":
            if (self.gold >= DEF_UVSB_PRICE):
                soldier = UvsB(pos, self.screen, self.map_data, self.color)
                self.gold -= DEF_UVSB_PRICE
                buy = True
        elif type == "vsUnits":
            if (self.gold >= DEF_UVSU_PRICE):
                soldier = UvsU(pos, self.screen, self.map_data, self.color)
                self.gold -= DEF_UVSU_PRICE
                buy = True

        if (buy):
            self.unit_pos.append(soldier.pos)
            self.unit_list.append(soldier)

    def addGoldMine(self, pos):

        if (self.gold >= DEF_GOLDMINE_PRICE):
            x,y = self.__coord_to_index(pos)
            self.map_data[y][x] = type

            mine = GoldMine(pos, self.screen)
            self.goldmines_list.append(mine)
            self.goldmines_pos.append(pos)
            self.gold -= DEF_GOLDMINE_PRICE

    def checkCost(self, type):
        cost = 0
        if type == "BasicTower":
            cost = DEF_BASICTOWER_PRICE
        elif type == "FireTower":
            cost = DEF_FIRINGTOWER_PRICE
        elif type == "UpgradeTower":
            cost = DEF_UPGRADETOWER_PRICE
        elif type == "SlowingTower":
            cost = DEF_ICETOWER_PRICE
        elif type == "GoldMine":
            cost = DEF_GOLDMINE_PRICE
        if self.gold - cost >=0:
            self.gold -= cost
            return True
        else:
            return False

    def remove(self, pos):
        x,y = self.__coord_to_index(pos)
        self.map_data[y][x] = "0"

    def __coord_to_index(self, coord):
        return ( int(coord[0] / 50), int(coord[1] / 50))

    def getData(self):
        return self.map_data

    def getCastlePos(self):
        return self.castle_pos

    def getUnitPos(self):
        return self.unit_pos

    def getTowerPos(self):
        return self.tower_pos

    def getGoldMinePos(self):
        return self.goldmines_pos

    def getUnits(self):
        return self.unit_list

    def getTowers(self):
        return self.tower_list

    def getGoldMines(self):
        return self.goldmines_list
