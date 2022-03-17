import pygame


class Unit:
    def __init__(self, img, pos, scale, screen):
        self.health = 800
        self.max_health = 800
        self.price = 100
        self.pos = pos
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        #self.castle50image = pygame.transform.scale(castle50_img, (int(width * scale), int(height * scale)))
        #self.castle25image = pygame.transform.scale(castle25_img, (int(width * scale), int(height * scale)))

        self.rect = self.castle100image.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
    def move(self, pos, goal_pos):
        self.pos = goal_pos
        self.rect = self.castle100image.get_rect()
        self.rect.x, self.rect.y = pos
    
    def train(self, img, scale):
        self.max_health += 200
        width = img.get_width()
        height = img.get_height()
        self.castle100image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        
    def heal(self):
        if (self.health+100)<=self.max_health:
            self.health += 100
        else:
            self.health = self.max_health
        
    def findPath(self, pos, game_map_data, castle_pos):
        pass
    
    def get_pos(self):
        return self.pos
    
    def delete(self):
        pass
    
    def reduceHealth(self, enemy):
        if self.health-enemy.damage>0:
            self.health -= enemy.damage;
        else:
            enemy.delete()
    """
    def draw(self, win):
       
        Draws the enemy with the given images
        :param win: surface
        :return: None
       
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))
        self.draw_health_bar(win)
        """

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface...enemy_position?
        :return: None
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0)

class UvsU(Unit):
    def __init__(self, img, pos, scale, screen):
        self.health = 800
        self.max_health = 800
        self.price = 100
        width = img.get_width()
        height = img.get_height()
        self.castle100image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.damage = 100
        self.range = 50
        
    def attack(self, pos, enemy):
        if (enemy.get_pos()-self.range)==self.pos:
            enemy.reduceHealth(self)
        
class UvsB(Unit):
    def __init__(self, img, pos, scale, screen):
        self.health = 800
        self.max_health = 800
        self.price = 100
        width = img.get_width()
        height = img.get_height()
        self.castle100image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.damage = 100
        self.range = 1
    def attack(self, pos, enemy):
        if (enemy.get_pos()-self.range)==self.pos:
            enemy.reduceHealth(self)
class UvsO(Unit):
    def __init__(self, img, pos, scale, screen):
        self.health = 800
        self.max_health = 800
        self.price = 100
        width = img.get_width()
        height = img.get_height()
        self.castle100image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.damage = 100
        self.range = 1
    def attack(self, pos, enemy):
        if (enemy.get_pos()-self.range)==self.pos:
            enemy.reduceHealth(self)