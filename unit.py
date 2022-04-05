import pygame
import collections

"""
Unit class, functions as a 'Basic Unit' and is the base class of all the units.
Only the position and the screen is required to create it.
"""


class Unit:
    def __init__(self, pos, screen, image_path='Images/basic.png', scale=0.07, health=800, max_health=800, price=100):
        self.health = health
        self.max_health = max_health
        self.price = price
        self.pos = pos
        self.img = pygame.image.load(image_path)

        # Scale the image
        width = self.img.get_width()
        height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen

    def move(self):
        """
        Make the unit move only 1 block according to the path it has.
        """
        #TODO: how to move player without filling the background? / animate
        goal_pos = self.findPath(self.pos)
        if goal_pos != self.pos:
            self.pos = goal_pos
            self.rect = self.img.get_rect()
            self.rect.x, self.rect.y = self.pos

            position = self.get_rect()
            for x in range(100):  # animate 100 frames
                self.screen.blit(background, position)  # erase
                self.position = goal_pos[::-1] # move player
                self.screen.blit(self.img, position)  # draw new unit
                pygame.display.update()

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

    def draw_health_bar(self, win):
        """
        draw health bar above unit
        :param win: surface...unit_position?
        :return: None
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255, 0, 0), (self.rect.x - 30, self.rect.y - 75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.rect.x - 30, self.rect.y - 75, health_bar, 10), 0)

    def delete(self):
        """
        Make the unit disappear from the game.
        """
        pass

    def findPath(self, castle_pos, game_map):
        """
        Take the current position, calculate the shortest path possible to the enemy castle from the game map.
        :param castle_pos: the position of the enemy castle
        :param game_map : matrix of the map
        :return next available step's coordinates
        If its already at the final location, it again returns the final location. ( as (x,y). ve give matrix [y][x])
        """
        w, h = pygame.display.get_surface().get_size()
        unit_pos = self.pos
        obstacle = 1 #Change this to the obstacle's number in game map matrix.

        queue = collections.deque([[unit_pos]])
        seen = set([unit_pos])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (y, x) == castle_pos:
                return path[1]
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x2 < w and 0 <= y2 < h and game_map[y2][x2] != obstacle and (x2, y2) not in seen:
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
    def __init__(self, pos, screen, image_path, scale,
                 health=800,
                 max_health=800,
                 price=100,
                 damage=100,
                 attack_range=50):

        self.damage = damage
        self.attack_range = attack_range
        Unit.__init__(self, pos, screen, image_path, scale, health, max_health, price)

    def attack(self, enemy, game_map, selfDigit):
        """
        Attack and reduceHealth of the enemy if is in attack_range.
        :param enemy: is of type Unit.
        :return: None
        """
        if (enemy.get_pos() - self.attack_range) <= self.pos:
            enemy.reduceHealth(self)


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
