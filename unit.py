from __future__ import annotations
import pygame
from projectile import Projectile
import collections
import math


"""
Unit class, functions as a 'Basic Unit' and is the base class of all the units.
Only the position and the screen is required to create it.
"""


class Unit:
    def __init__(self, pos: tuple[int], 
                 screen, game_map_data,color, image_path='Images/Units/soldier.png', scale=0.05, health=500, max_health=500, price=100):
        self._health = health
        self._max_health = max_health
        self._price = price
        self._color = color
        self.isStopped = False

        self.game_map_data = game_map_data
        self._pos = pos
        self.img = pygame.image.load(image_path)
        self._path = []
        self._moveList = []
        self._move_target = None

        # Scale the image
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(self.width * scale), int(self.height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self._screen = screen
        self._hitbox = pygame.Rect(self.pos[0]+3, self.pos[1]+8, 100, 100) #Hitbox area for the units

    def move(self, enemy_pos, obstacles, block = True):
        """
        Make the unit move only 1 block according to the path it has.
        """
        def create_coord(matrix):
            return (matrix[0] * 50, matrix[1] * 50)

        if(self.isStopped):
            return

        x,y = enemy_pos
        x = x - (x % 50)
        y = y - (y % 50)
        enemy_pos = (x,y)


        if (enemy_pos == self.pos):
            return

        if self._path == [] or self._path[-1] != enemy_pos:
            self._path = []

            returned_path = self.findPath(enemy_pos,obstacles,block)

            if returned_path is None:
                return
            else:
                for i in returned_path:
                    self._path.append(create_coord(i[::-1]))

        goal_pos = self._path[0]
        if (self._pos[0] < goal_pos[0]):
            self.rect.x += 50
        elif(self._pos[0] > goal_pos[0]):
            self.rect.x -= 50
        if(self._pos[1] < goal_pos[1]):
            self.rect.y += 50
        elif(self._pos[1] > goal_pos[1]):
            self.rect.y -= 50
        self._pos = (self.rect.x, self.rect.y)
        self._path.pop(0)
        self._hitbox = pygame.Rect(self.pos[0], self.pos[1], 100, 100)

    @property
    def health(self) -> int:
        """
        Returns the health of unit
        :return: int
        """
        return self._health

    @property
    def maxHealth(self) -> int:
        """
        Returns the maximum health of unit
        :return: int
        """
        return self._max_health

    @property
    def screen(self) -> pygame.Surface:
        """
        Returns the screen of the game
        :return:
        """
        return self._screen

    @property
    def pos(self) -> tuple[int, int]:
        """
        Returns the position of unit
        :return: tuple[int]
        """
        return self._pos
    @property
    def hitbox(self):
        """
        Returns the hitbox
        :return: pygame.Rect
        """
        return self._hitbox

    @property
    def price(self) -> int:
        """
        Returns the price of unit
        :return: int
        """
        return self._price

    @property
    def move_target(self):
        """
        Returns the target for moving
        :return: object
        """
        return self._move_target

    @property
    def moveList(self):
        """
        Returns the list of targets for moving
        :return: array
        """
        return self._moveList

    def setMoveTarget(self, value):
        """
        Changes the _move_target.
        :param value: array
        :return: None
        """
        self._move_target = value

    def setMoveList(self, value):
        """
        Changes the _moveList.
        :param value: object
        :return: None
        """
        self._moveList = value

    def appendMoveList(self, value):
        """
        Appends a value to the _moveList.
        :param value: object
        :return: None
        """
        self._moveList.append(value)

    def setPos(self, value):
        """
        Changes the _pos.
        :param value: tuple
        :return: None
        """
        self._pos = value

    def get_pos(self):
        """
        :return pos: Current position of the unit
        """
        return self._pos

    def setStopped(self, bool):
        """
        Changes the isStopped.
        :param value: boolean
        :return: None
        """
        self.isStopped = bool

    def setHealth(self, value):
        """
        Changes the _health.
        :param value: int
        :return: None
        """
        self._health = value

    def reduceHealth(self, damage):
        """
        Reduce health. If the health is not enough, delete.
        :param damage: enemy damage
        :return: None
        """
        if self._health - damage > 0:
            self._health -= damage
        else:
            self._health = 0

    def draw(self):
        """
        Draws the unit with the given images
        """
        self._screen.blit(self.img, self.rect)

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
        x,y,z = self._color
        draw_health_bar(self._screen, health_rect.topleft, health_rect.size,
                x,y,z, self._health/self._max_health)

    def remove(self):
        """
        Make the unit disappear from the game.
        """
        self._screen.fill((255, 255, 255))

    def findPath(self, castle_pos, obstacles, block):
        """
        Take the current position, calculate the shortest path possible to the enemy castle from the game map.
        :param castle_pos: the position of the enemy castle
        :return next available step's coordinates
        """

        unit_pos = (int(self._pos[0] / 50), int(self._pos[1] / 50))
        end = (int(castle_pos[0] / 50), int(castle_pos[1] / 50))

        w, h = pygame.display.get_surface().get_size()
        w = int(w/50)
        h = int(h/50)

        queue = collections.deque([[unit_pos]])
        seen = set([unit_pos])
        noway = []

        if block:
            for obstacle in obstacles:
                x,y = obstacle.pos
                noway.append((int(x/50), int(y/50)))

        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (y,x) == end:
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < w and 0 <= y2 < h and (y2,x2) not in noway and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))


"""
AttackingUnit Class is a superclass for UvsU, UvsB and UvsO and also subclass of Unit. 
Includes attacking function.
"""
class AttackingUnit(Unit):
    
    def __init__(self, pos: tuple[int], screen, game_map_data, color, image_path, scale,
                 health=800,
                 max_health=800,
                 price=100,
                 damage=50,
                 attack_range=50):
        self._pos = pos
        self._damage = damage
        self._attack_range = attack_range
        self._targetList = []
        self._attackList = []
        self._moveList = []

        self.last_target = None
        self._current_target = None

        self.current_cd = 0
        self.cd = 150
        self._hitbox = pygame.Rect(self._pos[0], self._pos[1], 50, 50)
        Unit.__init__(self, pos, screen, game_map_data, color, image_path, scale, health, max_health, price)

    @property
    def targetList(self):
        
        return self._targetList

    @property
    def current_target(self):

        return self._current_target

    def setCurrentTarget(self, value):
        """
        Changes the _current_target.
        :param value: object
        :return: None
        """
        self._current_target = value

    def setTargetList(self, value):
        """
        Changes the _targetList.
        :param value: array
        :return: None
        """
        self._targetList = value

    def appendTargetList(self, value):
        """
        Appends a value to the _targetList.
        :param value: object
        :return: None
        """
        self._targetList.append(value)

    def removeTargetList(self, value):
        """
        Removes a value from the _targetList.
        :param value: object
        :return: None
        """
        self._targetList.remove(value)

    def setHitbox(self, value):
        """
        Changes the _hitbox.
        :param value: pygame.Rect
        :return: None
        """
        self._hitbox = value

    def attack(self):
        """
        Attack and reduceHealth of the enemy if is in attack_range.
        :return: None
        """
        for e in self._attackList:
            if e.target.health <= 0:
                self._attackList.remove(e)
                self.current_cd = -1
        if self.current_cd <= 0 and self._current_target != None:
            self._attackList.append(Projectile(self._pos[0],self._pos[1],self._current_target,self._damage))
            self.current_cd = self.cd
        else:
            self.current_cd -= 1
        for e in self._attackList:
            if self._current_target != None:
                e.hitEnemy()

    def move(self,obstacles, find=True, block = True):
        """
        Make the unit move only 1 block according to the path it has.
        """
        if(self._moveList == []):
            return
        if find:
            closest = None
            closest_num = 999999
            x, y = self._pos
            for k in self._moveList:
                q, w = k.pos
                num = abs(x - q) + abs(y - w)
                if (num < closest_num):
                    closest_num = num
                    closest = k
            self.setMoveTarget(closest)

        self._hitbox = pygame.Rect(self._pos[0], self._pos[1], 100, 100)
        super().move(self.move_target.pos, obstacles, block)

    

"""
 UvsU is subclass of AttackingUnit. Meaning UnitvsUnit, it can attack and destroy the enemy units.
"""
class UvsU(AttackingUnit):
    def __init__(self, pos, screen, game_map_data, color, image_path='Images/Units/uvsu.png', scale = 0.2):
        super().__init__(pos, screen, game_map_data, color, image_path, scale, 500,500,100,150,50)

    def move(self,obstacles, block = True):
        """
        Make the unit move only 1 block according to the path it has.
        """
        def create_coord(matrix):
            return (matrix[0] * 50, matrix[1] * 50)

        if(self._moveList == [] or self.isStopped):
            return

        closest = None
        closest_num = 999999
        x, y = self._pos
        for k in self._moveList:
            q, w = k.pos
            num = abs(x - q) + abs(y - w)
            if (num < closest_num):
                closest_num = num
                closest = k
        self.setMoveTarget(closest)

        x,y = self.move_target.pos
        isTrue = ((x+30 >= self._pos[0] and x<= self._pos[0]) or (x-30 <= self._pos[0] and x>= self._pos[0])) and ( (y+30 >= self._pos[1] and y<= self._pos[1]) or (y-30 <= self._pos[1] and y>= self._pos[1]))
        x = x - (x % 50)
        y = y - (y % 50)
        castle_pos = (x,y)

        if (isTrue):
            return

        returned_path = self.findPath(castle_pos,obstacles, block)
        if returned_path is None:
            return
        else:
            if (len(returned_path)<2):
                return

            goal_pos = create_coord(returned_path[1][::-1])

            if (self._pos[0] < goal_pos[0]):
                self.rect.x += 50
            elif(self._pos[0] > goal_pos[0]):
                self.rect.x -= 50
            if(self._pos[1] < goal_pos[1]):
                self.rect.y += 50
            elif(self._pos[1] > goal_pos[1]):
                self.rect.y -= 50
            self.setPos((self.rect.x, self.rect.y))
        self.setHitbox(pygame.Rect(self._pos[0], self._pos[1], 100, 100))



"""
 UvsB is subclass of AttackingUnit. Meaning UnitvsBuilding, it can attack and destroy enemy towers.
"""
class UvsB(AttackingUnit):
    def __init__(self, pos: tuple[int], screen, game_map_data, color, image_path='Images/Units/basic.png', scale=0.2):
        super().__init__(pos, screen, game_map_data, color, image_path, scale,800,800,150,50,50)

    def move(self,obstacles):
        """
        Make the unit move only 1 block according to the path it has.
        """
        if self.move_target == None or self.move_target not in self._moveList:
            super().move(obstacles)
        else:
            super().move(obstacles, find=False)


"""
 UvsO is subclass of AttackingUnit. Meaning UnitvsObstacle, it can attack and destroy the obstacles
"""
class UvsO(AttackingUnit):
    def __init__(self, pos, screen, game_map_data, color, image_path='Images/Units/uvso.png', scale=0.2):
        super().__init__(pos, screen,game_map_data, color, image_path, scale,400,400,100,100,50)

    def move(self,obstacles):
        """
        Make the unit move only 1 block according to the path it has.
        """
        self._hitbox = pygame.Rect(self._pos[0], self._pos[1], 100, 100)
        if self.move_target == None or self.move_target not in self._moveList:
            super().move(obstacles, block=False)
        else:
            super().move(obstacles, find=False, block = False)
            
