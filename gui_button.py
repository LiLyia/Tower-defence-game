from pygame.locals import *
import pygame

'''
@ramzan
'''

class Button:

    # constructor of Button class(x,y at which position our button will start)
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont("Aguda", 32)
        self.clicked = False
        self.button_color = "#253e8a"
        self.hover_color = "#5480f0"
        self.mouse_clicked_color = "#0E6655"
        self.text_color = (0, 0, 0)
        self.btn_width, self.btn_height = 350, 60

    # function to draw the Button
    def draw_Button(self, screen):

        action = False

        # For getting the position of mouse
        position = pygame.mouse.get_pos()

        # For creating the Pygame rectangular area of the object (Button)
        button_rect = Rect(self.x, self.y, self.btn_width, self.btn_height)
        # For checking the Mouse over
        if button_rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(screen, self.mouse_clicked_color, button_rect)

            elif pygame.mouse.get_pressed()[0] == 0 and (self.clicked == True):
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, button_rect)

        # adding the shadow to the Button
        pygame.draw.line(screen, self.white, (self.x, self.y), (self.x + self.btn_width, self.y), 2)
        pygame.draw.line(screen, self.white, (self.x, self.y), (self.x, self.y + self.btn_height), 2)
        pygame.draw.line(screen, self.white, (self.x, self.y + self.btn_height),
                         (self.x + self.btn_width, self.y + self.btn_height), 2)
        pygame.draw.line(screen, self.white, (self.x + self.btn_width, self.y),
                         (self.x + self.btn_width, self.y + self.btn_height), 2)

        # add text to button
        text_img = self.font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.btn_width / 2) - int(text_len / 2), self.y + 25))
        return action
