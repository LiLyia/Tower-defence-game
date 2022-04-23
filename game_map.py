import pygame
# @ramzan


class GameMap:
    def __init__(self, data, tile_size, screen):
        # Creating the list storing the position of the tiles
        self.tiles_position_list = []
        self.screen = screen
        # Different images for game map
        dirt_img = pygame.image.load('Images/hurdles/dirt_0.png')
        hurdle1_img = pygame.image.load('Images/hurdles/hurdle_1.png')
        hurdle2_img = pygame.image.load('Images/hurdles/hurdle_2.png')
        hurdle3_img = pygame.image.load('Images/hurdles/hurdle_3.png')
        hurdle4_img = pygame.image.load('Images/hurdles/hurdle_4.png')
        # creating dictionary for storing images
        TITLE_IMAGE_MAP = {
                        "1": dirt_img,
                        "2": hurdle1_img,
                        "3": hurdle2_img,
                        "4": hurdle3_img,
                        "5": hurdle4_img,
                    }

        # for storing row count
        row_cnt = 0
        for row in data:
            col_cnt = 0
            for tile in row:
                if tile in TITLE_IMAGE_MAP.keys():
                    raw_img = TITLE_IMAGE_MAP[tile]
                    img = pygame.transform.scale(raw_img, (tile_size, tile_size))
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
