import pygame


class Unit:
    def __init__(self, img, pos, scale, screen, health=800, max_health=800, price=100):
        self.health = health
        self.max_health = max_health
        self.price = price
        self.pos = pos

        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen

    def move(self, pos, goal_pos):
        self.pos = goal_pos
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos

    def train(self, img, scale):
        self.max_health += 200
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))

    def heal(self):
        if (self.health + 100) <= self.max_health:
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
        if self.health - enemy.damage > 0:
            self.health -= enemy.damage
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

        pygame.draw.rect(win, (255, 0, 0), (self.rect.x - 30, self.rect.y - 75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.rect.x - 30, self.rect.y - 75, health_bar, 10), 0)


class AttackingUnit(Unit):
    def __init__(self, img, pos, scale, screen, health=800, max_health=800, price=100, damage=100, attack_range=50):
        self.damage = damage
        self.attack_range = attack_range
        Unit.__init__(self, img, pos, scale, screen, health, max_health, price)

    def attack(self, pos, enemy):
        if (enemy.get_pos() - self.attack_range) == self.pos:
            enemy.reduceHealth(self)


class UvsU(AttackingUnit):
    def __init__(self, img, pos, scale, screen):
        AttackingUnit.__init__(self, img, pos, scale, screen, health=800,
                               max_health=800, price=100, S
        damage = 100, attack_range = 50)

        class UvsB(AttackingUnit):
            def __init__(self, img, pos, scale, screen):
                AttackingUnit.__init__(self, img, pos, scale, screen, health=800,
                                       max_health=800, price=100, damage=100, attack_range=50)

        class UvsO(AttackingUnit):
            def __init__(self, img, pos, scale, screen):
                AttackingUnit.__init__(self, img, pos, scale, screen, health=800,
                                       max_health=800, price=00, damage=100, attack_range=50)