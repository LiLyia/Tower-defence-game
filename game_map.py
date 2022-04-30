from obstacle import *


class GameMap:
    def __init__(self, data, tile_size, screen, imager):
        # Creating the list storing the position of the tiles
        self.obstacles = []
        self.tiles_position_list = []
        self.screen = screen
        #         dirt and hurdles images
        # for storing row count
        row_cnt = 0
        for row in data:
            col_cnt = 0
            for tile in row:
                if tile != 0:
                    if tile == 1:
                        img = imager.scaleWithWidthAndHeight(imager.getHurdleImage(0), tile_size, tile_size)
                        img_rect = img.get_rect()
                        img_rect.x = col_cnt * tile_size
                        img_rect.y = row_cnt * tile_size
                        hurdle = (img, img_rect)
                        self.tiles_position_list.append(hurdle)

                    else:
                        pos = (col_cnt * tile_size, row_cnt * tile_size)
                        obj_obstacle = Obstacle.createObstacle(pos=pos, screen=screen, imager=imager,
                                                               tile_size=tile_size, image_number=tile-1)
                        self.obstacles.append(obj_obstacle)
                col_cnt += 1
            row_cnt += 1

    def getObstacles(self):
        return self.obstacles

    def draw_tiles(self):
        for tile in self.tiles_position_list:
            self.screen.blit(tile[0], tile[1])
