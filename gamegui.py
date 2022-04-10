import pygame
from pygame import mixer
from game_instructions import game_instruction
# @ramzan
# from pygame.locals import *
from gui_button import Button
from gameEngine import game_start

pygame.init()
screen = pygame.init()
SCREEN_HEIGHT, SCREEN_WIDTH = 650, 650
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("Defence Tower")
#  -----------Adjusting the Frame of the Game------------#
clock = pygame.time.Clock()
FPS = 60
# -----------BG Image---------------------#
bg_img = pygame.image.load("Images/BG/bg1.png")
bg_img = pygame.transform.scale(bg_img, (SCREEN_HEIGHT, SCREEN_WIDTH))
# ----------------Background music--------------
mixer.music.load('Music/background.wav')
mixer.music.play(-1)
# Using Button class
Start_game = Button(75,100, "Start")
instruction = Button(75,175,"Instruction")
save_game = Button(75,250,"Save")
quit_button = Button(75,325,"Quit")

is_game = True
while is_game:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))
    if Start_game.draw_Button(screen):
        # print("Play Again")
        pass
    if instruction.draw_Button(screen):
        # print("instruction")
        game_instruction()
    if save_game.draw_Button(screen):
        print('Save game')
    if quit_button.draw_Button(screen):

        is_game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
    pygame.display.update()
# pygame.quit()
