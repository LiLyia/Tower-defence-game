import pygame

class GoldMine:
    def __init__(self, pos, screen, gold = 50, image_path='Images/Gold.png', scale=0.1, health=300, max_health=300, price=200):
        self.health = health
        self.max_health = max_health
        self.price = price
        self.pos = pos
        self.gold_amount = gold

        self.img = pygame.image.load(image_path)

        # Scale the image
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(self.width * scale), int(self.height * scale)))

        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen
        self.hitbox = pygame.Rect(self.pos[0]+3, self.pos[1]+8, 40, 40) #Hitbox area for the units

    def draw(self):
        """
        Draws the unit with the given images
        """
        self.screen.blit(self.img, self.rect)

    def remove(self):
        """
        Make the unit disappear from the game.
        """
        self.screen.fill((255, 255, 255))

    def addGold(self,player):
        player.gold += self.gold_amount