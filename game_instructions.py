import pygame
import sys
from gui_button import Button
# @ramzan

def game_instruction():
    pygame.init()
    screen = pygame.init()
    SCREEN_HEIGHT, SCREEN_WIDTH = 650, 650
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    pygame.display.set_caption("Defence Tower")
    #  -----------Adjusting the Frame of the Game------------#
    # clock = pygame.time.Clock()
    # FPS = 60
    bg_img = pygame.image.load("Images/Background/bg_3.png")
    back_button = Button(140,525,"Back")
    is_game = True
    while is_game:
        # clock.tick(FPS)
        screen.blit(bg_img, (0, 0))
        if back_button.draw_Button(screen):
            screen = pygame.display.set_mode((850,650))
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# game_instruction()
