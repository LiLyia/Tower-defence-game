import pygame
from pygame.locals import *


class GameMap:
    def __init__(self, data, tile_size, screen):
        # Creating the list storing the position of the tiles
        self.tiles_position_list = []
        self.screen = screen
        #         dirt and hurdles images
        dirt_img = pygame.image.load('Images/hurdles/dirt_0.png')
        hurdle1_img = pygame.image.load('Images/hurdles/hurdle_1.png')
        hurdle2_img = pygame.image.load('Images/hurdles/hurdle_2.png')
        hurdle3_img = pygame.image.load('Images/hurdles/hurdle_3.png')
        hurdle4_img = pygame.image.load('Images/hurdles/hurdle_4.png')
        # for storing row count
        row_cnt = 0
        for row in data:
            col_cnt = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_cnt * tile_size
                    img_rect.y = row_cnt * tile_size
                    tile = (img, img_rect)
                    self.tiles_position_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(hurdle1_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_cnt * tile_size
                    img_rect.y = row_cnt * tile_size
                    tile = (img, img_rect)
                    self.tiles_position_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(hurdle2_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_cnt * tile_size
                    img_rect.y = row_cnt * tile_size
                    tile = (img, img_rect)
                    self.tiles_position_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(hurdle3_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_cnt * tile_size
                    img_rect.y = row_cnt * tile_size
                    tile = (img, img_rect)
                    self.tiles_position_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(hurdle4_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_cnt * tile_size
                    img_rect.y = row_cnt * tile_size
                    tile = (img, img_rect)
                    self.tiles_position_list.append(tile)
                col_cnt += 1
            row_cnt += 1

    def draw_tiles(self):
        for tile in self.tiles_position_list:
            self.screen.blit(tile[0], tile[1])
