import pygame


class Unit:
    def __init__(self, unit_img, pos, scale, screen, health=600, speed=50, price=100):
        self.health = health
        self.speed = speed
        width = unit_img.get_width()
        height = unit_img.get_height()
        self.unit_img = pygame.transform.scale(unit_img, (int(width * scale), int(height * scale)))

        self.rect = self.unit_img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
        self.price = price

    def move(self):
        ...

    def train(self):
        ...

    def findPath(self):
        ...

