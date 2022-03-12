import pygame


class Castle:
    def __init__(self, castle100_img,castle50_img,castle25_img, pos, scale, screen):
        self.health = 1200
        self.max_health = self.health
        width = castle100_img.get_width()
        height = castle100_img.get_height()
        self.castle100image = pygame.transform.scale(castle100_img, (int(width * scale), int(height * scale)))
        self.castle50image = pygame.transform.scale(castle50_img, (int(width * scale), int(height * scale)))
        self.castle25image = pygame.transform.scale(castle25_img, (int(width * scale), int(height * scale)))

        self.rect = self.castle100image.get_rect()
        self.rect.x, self.rect.y = pos
        self.screen = screen

    #         ----------Draw castle ------------------
    '''In draw_castle function when the health of castle decrease the images changes accordingly'''

    def draw_castle(self):
        # to check which image should be used when health dropped
        if self.health <= 600:
            self.image = self.castle50image
        elif self.health <= 300:
            self.image = self.castle25image
        else:
            self.image = self.castle100image

        self.screen.blit(self.image, self.rect)

    # ----------------------- Implementation of damage castle function
