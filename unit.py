import pygame
import collections
from projectile import *
import projectile

"""
Unit class, functions as a 'Basic Unit' and is the base class of all the units.
Only the position and the screen is required to create it.
"""


class Unit:
    def __init__(self, pos, screen,game_map_data, image_path='Images/basic.png', scale=0.3, health=800, max_health=800, price=100):
        self.health = health
        self.max_health = max_health
        self.price = price
        self.pos = pos
        self.img = pygame.image.load(image_path)
        self.game_map_data = game_map_data
        self.map_pos = (int(pos[0]/50), int(pos[1]/50))

        # Scale the image
        width = self.img.get_width()
        height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen

    def move(self, castle_pos):
        """
        Make the unit move only 1 block according to the path it has.
        """
        goal_pos = self.findPath(castle_pos)

        if goal_pos != self.pos:
            if (self.pos[0] < goal_pos[0]):
                self.rect.x += 10
            if(self.pos[0] > goal_pos[0]):
                self.rect.x -=10
            if(self.pos[1] < goal_pos[1]):
                self.rect.y += 10
            if(self.pos[1] > goal_pos[1]):
                self.rect.y -= 10
            self.pos = (self.rect.x, self.rect.y)
        print(self.pos)
        print(self.map_pos)
        if(self.pos[0]%50 == 0):
            x,y = self.map_pos
            x = int(self.pos[0]/50)
            self.map_pos = (x,y)
        if(self.pos[1]%50 == 0):
            x,y = self.map_pos
            y = int(self.pos[1]/50)
            self.map_pos = (x, y)


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

    def reduceHealth(self, enemy):
        """
        Reduce health. If the health is not enough, delete.
        :param enemy: type of Unit
        :return: None
        """
        if self.health - enemy.damage > 0:
            self.health -= enemy.damage
        else:
            self.delete()

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

        draw_health_bar(self.screen, health_rect.topleft, health_rect.size,
                (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health/self.max_health)

    def delete(self):
        """
        Make the unit disappear from the game.
        """
        pass

    def findPath(self, castle_pos):
        """
        Take the current position, calculate the shortest path possible to the enemy castle from the game map.
        :param castle_pos: the position of the enemy castle
        :param game_map : matrix of the map
        :return next available step's coordinates
        If its already at the final location, it again returns the final location. ( as (x,y). ve give matrix [y][x])
        """
        def create_coord(matrix):
            return (matrix[0] * 50, matrix[1] * 50)

        unit_pos = self.map_pos
        # cx, cy = castle_pos
        # cx = int(cx/50)
        # cy = int(cy/50)
        # end = (cx,cy)
        end = castle_pos

        w, h = pygame.display.get_surface().get_size()
        w = int(w/50)
        h = int(h/50)

        queue = collections.deque([[unit_pos]])
        seen = set([unit_pos])
        obstacle = 1

        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (y,x) == end:
                if (len(path) > 1 ):
                    return create_coord(path[1][::-1])
                else:
                    return create_coord(path[0][::-1])
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < w and 0 <= y2 < h and self.game_map_data[y2][x2] != obstacle and (x2, y2) not in seen:

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
    def __init__(self, pos, screen, image_path, scale, targetList, attackList,
                 health=800,
                 max_health=800,
                 price=100,
                 damage=100,
                 attack_range=50):

        self.damage = damage
        self.attack_range = attack_range
        self.targetList = []
        self.attackList = []
        self.current_cd = 0
        self.cd = 150
        self.hitbox = pygame.Rect(self._pos[0] - 35, self._pos[1] - 25, 80, 80)
        Unit.__init__(self, pos, screen, image_path, scale, health, max_health, price)

    def findTargetforUnits(unit_list, tower_list, obstacle_list):
        for u in unit_list:
            u.targetList = []
            if type(u) == UvsU:
                for m in unit_list:
                    if u.hitbox.colliderect(m.hitbox) == True:
                        u.targetList.append(m)
            if type(u) == UvsB:
                for m in tower_list:
                    if u.hitbox.colliderect(m.hitbox) == True:
                        u.targetList.append(m)
            if type(u) == UvsO:
                for m in obstacle_list:
                    if u.hitbox.colliderect(m.hitbox) == True:
                        u.targetList.append(m)
                    
    def currentUnitTarget(unit_list):
        for u in unit_list:
            if type(u) == UvsU or type(u) == UvsB or type(u) == UvsO:
                for t in u.targetList:
                    if u.current_target == None:
                        u.current_target = t
                        if u.current_target.health < 0:
                            #("Yes")
                            u.targetList.remove(t)
                    if u.current_target.pos[0] <= t.pos[0]:
                       u.current_target = t
            
            if len(u.targetList) == 0:
               u.current_target = None
             
    def shootUnits(unit_list):
        for u in unit_list:
            if type(u) == UvsU or type(u) == UvsB or type(u) == UvsO:
                if u.current_target != None:
                    u.attack()
                    if u.current_target.health <0:
                        u.current_target = None
    def attack(self):
        """
        Attack and reduceHealth of the enemy if is in attack_range.
        :param enemy: is of type Unit.
        :return: None
        """
        if self.current_cd <= 0 and self.current_target != None:
            self.attackList.append(Projectile(self.pos[0],self.pos[1],self.current_target,self.damage))
            self.current_cd = self.cd
        else:
            self.current_cd -= 1
        for e in self.attackList:
            if self.current_target != None :
                e.hitEnemy()


"""
 UvsU is subclass of AttackingUnit. Meaning UnitvsUnit, it can attack and destroy the enemy units.
"""


class UvsU(AttackingUnit):
    def __init__(self, pos, screen, image_path='Images/uvsu.png', scale=0.07):

        super().__init__(self, pos, screen, image_path, scale,
                         health=500,
                         max_health=500,
                         price=100,
                         damage=100,
                         attack_range=50)


"""
 UvsB is subclass of AttackingUnit. Meaning UnitvsBuilding, it can attack and destroy enemy towers.
"""


class UvsB(AttackingUnit):

    def __init__(self, pos, screen, image_path='Images/uvsb.png', scale=0.07):

        super().__init__(self, pos, screen, image_path, scale,
                         health=800,
                         max_health=800,
                         price=150,
                         damage=100,
                         attack_range=50)


"""
 UvsO is subclass of AttackingUnit. Meaning UnitvsObstacle, it can attack and destroy the obstacles
"""


class UvsO(AttackingUnit):
    def __init__(self, pos, screen, image_path='Images/uvso', scale=0.07):

        super().__init__(self, pos, screen, image_path, scale,
                         health=800,
                         max_health=400,
                         price=100,
                         damage=100,
                         attack_range=50)
