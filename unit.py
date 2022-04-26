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
                 screen, game_map_data,color, image_path='Images/Units/soldier.png', scale=0.05, health=800, max_health=800, price=100):
        self.health = health
        self.max_health = max_health
        self.price = price
        self.color = color
        self.isStopped = False

        self.game_map_data = game_map_data
        self.pos = pos
        self.img = pygame.image.load(image_path)
        self.path = []
        self.moveList = []
        self.move_target = None

        # Scale the image
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(self.width * scale), int(self.height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
        self.hitbox = pygame.Rect(self.pos[0]+3, self.pos[1]+8, 100, 100) #Hitbox area for the units

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

        if self.path == [] or self.path[-1] != enemy_pos:
            self.path = []

            returned_path = self.findPath(enemy_pos,obstacles,block)

            if returned_path is None:
                return
            else:
                for i in returned_path:
                    self.path.append(create_coord(i[::-1]))

        goal_pos = self.path[0]
        if (self.pos[0] < goal_pos[0]):
            self.rect.x += 50
        elif(self.pos[0] > goal_pos[0]):
            self.rect.x -= 50
        if(self.pos[1] < goal_pos[1]):
            self.rect.y += 50
        elif(self.pos[1] > goal_pos[1]):
            self.rect.y -= 50
        self.pos = (self.rect.x, self.rect.y)
        self.path.pop(0)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 100, 100)

    def heal(self):
        """
        Extra feature that can be added afterwards
        """
        if (self.health + 100) <= self.max_health:
            self.health += 100
        else:
            self.health = self.max_health

    def get_pos(self):
        """
        :return pos: Current position of the unit
        """
        return self.pos

    def setStopped(self, bool):
        self.isStopped = bool

    def reduceHealth(self, damage):
        """
        Reduce health. If the health is not enough, delete.
        :param damage: enemy damage
        :return: None
        """
        if self.health - damage > 0:
            self.health -= damage
        else:
            self.health = 0

    def draw(self):
        """
        Draws the unit with the given images
        """
        self.screen.blit(self.img, self.rect)

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
        x,y,z = self.color
        draw_health_bar(self.screen, health_rect.topleft, health_rect.size,
                x,y,z, self.health/self.max_health)

    def remove(self):
        """
        Make the unit disappear from the game.
        """
        self.screen.fill((255, 255, 255))

    def findPath(self, castle_pos, obstacles, block):
        """
        Take the current position, calculate the shortest path possible to the enemy castle from the game map.
        :param castle_pos: the position of the enemy castle
        :return next available step's coordinates
        """

        unit_pos = (int(self.pos[0] / 50), int(self.pos[1] / 50))
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



    """"
    def train(self, img, scale):
        self.max_health += 200
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
    """


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
        self.pos = pos
        self.damage = damage
        self.attack_range = attack_range
        self.targetList = []
        self.attackList = []

        self.last_target = None
        self.current_target = None

        self.current_cd = 0
        self.cd = 150
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 50, 50)
        Unit.__init__(self, pos, screen, game_map_data, color, image_path, scale, health, max_health, price)

    def attack(self, type):
        """
        Attack and reduceHealth of the enemy if is in attack_range.
        :param enemy: is of type Unit.
        :return: None
        """
        for e in self.attackList:
            if e.target.health <= 0:
                self.attackList.remove(e)
                self.current_cd = -1
        if self.current_cd <= 0 and self.current_target != None:
            self.attackList.append(Projectile(self.pos[0],self.pos[1],self.current_target,self.damage))
            self.current_cd = self.cd
        else:
            self.current_cd -= 1
        for e in self.attackList:
            if type == UvsB:
                if self.current_target != None:
                    e.hitTower()
            else:
                if self.current_target != None:
                    e.hitEnemy()

    def move(self,obstacles, find=True, block = True):

        if(self.moveList == []):
            return

        if find:
            closest = None
            closest_num = 999999
            x, y = self.pos
            for k in self.moveList:
                q, w = k.pos
                num = abs(x - q) + abs(y - w)
                if (num < closest_num):
                    closest_num = num
                    closest = k
            self.move_target = closest


        super().move(self.move_target.pos, obstacles, block)



"""
 UvsU is subclass of AttackingUnit. Meaning UnitvsUnit, it can attack and destroy the enemy units.
"""

class UvsU(AttackingUnit):
    def __init__(self, pos, screen, game_map_data, color, image_path='Images/Units/uvsu.png', scale = 0.2):
        super().__init__(pos, screen, game_map_data, color, image_path, scale, 500,500,100,50,50)

    def move(self,obstacles, block = True):
        """
        Make the unit move only 1 block according to the path it has.
        """
        def create_coord(matrix):
            return (matrix[0] * 50, matrix[1] * 50)

        if(self.moveList == [] or self.isStopped):
            return

        closest = None
        closest_num = 999999
        x, y = self.pos
        for k in self.moveList:
            q, w = k.pos
            num = abs(x - q) + abs(y - w)
            if (num < closest_num):
                closest_num = num
                closest = k
        self.move_target = closest

        x,y = self.move_target.pos
        isTrue = ((x+30 >= self.pos[0] and x<= self.pos[0]) or (x-30 <= self.pos[0] and x>= self.pos[0])) and ( (y+30 >= self.pos[1] and y<= self.pos[1]) or (y-30 <= self.pos[1] and y>= self.pos[1]))
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

            if (self.pos[0] < goal_pos[0]):
                self.rect.x += 50
            elif(self.pos[0] > goal_pos[0]):
                self.rect.x -= 50
            if(self.pos[1] < goal_pos[1]):
                self.rect.y += 50
            elif(self.pos[1] > goal_pos[1]):
                self.rect.y -= 50
            self.pos = (self.rect.x, self.rect.y)



"""
 UvsB is subclass of AttackingUnit. Meaning UnitvsBuilding, it can attack and destroy enemy towers.
"""


class UvsB(AttackingUnit):
    def __init__(self, pos: tuple[int], screen, game_map_data, color, image_path='Images/Units/basic.png', scale=0.2):
        super().__init__(pos, screen, game_map_data, color, image_path, scale,800,800,150,50,50)

    def move(self,obstacles):
        if self.move_target == None:
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
        if self.move_target == None:
            super().move(obstacles, block=False)
        else:
            super().move(obstacles, find=False, block = False)
