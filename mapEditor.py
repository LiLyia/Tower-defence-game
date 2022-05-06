import menu
from tower import *
from FireTower import *
from ice_tower import *
from goldmine import *
from game_map import *
from castle import *
from pygame.locals import *
from datetime import datetime


class MapEditor:
    def __init__(self, imager, screen, turn, player1, player2, tower_images,
                 fire_tower_images, ice_tower_images, tile_size, clock, bg_img, count, limit):
        self.__createMapData()
        self.tile_size = tile_size
        self.imager = imager
        self.count = count
        self.limit = limit
        self.screen = screen
        self.turn = turn
        self.player1 = player1
        self.player2 = player2
        self.obstacles = []
        self.tower_images = tower_images
        self.fire_tower_images = fire_tower_images
        self.ice_tower_images = ice_tower_images
        self.game_map = GameMap(self.game_map_data, tile_size, screen, imager=imager)
        self.clock = clock
        self.bg_img = bg_img
        self.towers = []
        self.moving_object = None
        self.side_menu = menu.VerticalMenu(750, 120, pygame.transform
                                           .scale(pygame.image.load('Images/menu.png').convert_alpha(), (200, 650)))
        self.mainButtons()

    def __createMapData(self):
        self.game_map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def buttons(self, side_menu_button, player):
        # Parameters: side_menu_button - the name of the button from the side menu; player - the current player.
        # Vertical menu implementation, draws and clears the buttons.
        if side_menu_button == "Castle":
            self.add_castle(self.screen)
        elif side_menu_button == "Hurdle": #type(side_menu_button) == str and "hurdle" in side_menu_button:
            self.addObstacle(self.screen)
        elif side_menu_button == "Turn":
            if self.turn == self.player1:
                return self.player2
            else:
                return self.player1
        elif side_menu_button == "Save":
            return "MAIN"

    def mainButtons(self):
        self.side_menu.add_btn(pygame.transform.scale(self.imager.getCastleImage(0, 0), (120, 80)), "Castle", 0)
        self.side_menu.add_btn(pygame.transform.scale(pygame.image.load('Images/turn.png')
                                                      .convert_alpha(), (120, 50)), "Turn", 0)
        self.side_menu.add_btn(
            pygame.transform.scale(pygame.image.load('Images/Hurdles/hurdle_1.png').convert_alpha(), (100, 80)), "Hurdle", 0)
        self.side_menu.add_btn(
            pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)), "Save", 0)

    def clearMainButtons(self):
        self.side_menu.clear_btn("Castles")
        self.side_menu.clear_btn("Turn")
        self.side_menu.clear_btn("Obstacles")
        self.side_menu.clear_btn("Save")

    def addObstacle(self, screen):
        x, y = pygame.mouse.get_pos()
        try:
            self.moving_object = Obstacle.createObstacle(pos=(x, y), screen=screen, imager=self.imager, tile_size=self.tile_size, image_number=1)
            self.moving_object.moving = True
        except Exception as e:
            print(str(e) + "Cannot create an obstacle")

    def add_castle(self, screen):
        x, y = pygame.mouse.get_pos()
        try:
            obj = self.__create_castle(x, y, screen)
            if obj is not None:
                self.moving_object = obj
                self.moving_object.moving = True
        except Exception as e:
            print(str(e) + " NOT VALID NAME")

    def __create_castle(self, x, y, screen):
        # Parameters: name - name of the button; x - x position; y - y position; screen - the screen.
        # Creates a tower object and adds it to tower list.
        if self.turn == self.player1:
            color = self.player1.color
            castle = Castle(self.imager, (x, y), screen, 0, color)
        else:
            color = self.player2.color
            castle = Castle(self.imager, (x, y), screen, 1, color)
        return castle

    def save(self):
        if self.player1.castle != None and self.player1.castle != None and self.limit <= 5:
            file_name = "map_" + str(self.count)
            print(str(datetime.now()))
            new_file = open(file_name, "w+")
            new_file.write(str(self.player1.castle_pos[0])+" "+str(self.player1.castle_pos[1]))
            new_file.write('\n')
            new_file.write(str(self.player2.castle_pos[0])+" "+str(self.player2.castle_pos[1]))
            new_file.write('\n')
            new_file.write(str(len(self.obstacles)))
            new_file.write('\n')
            for obstacle in self.obstacles:
                new_file.write(str(obstacle.pos[0])+" "+str(obstacle.pos[1]))
                new_file.write('\n')
            new_file.close()
            print(self.count)
            return file_name
        return None

    @staticmethod
    def upgrade_tower(turn):
        # Parameters: turn - the current player.
        # The function upgrades the first ready to be upgraded basic tower.
        for tower in turn.getTowers():
            if type(tower) != FireTower and type(tower) != IceTower:
                if tower.maxUp == 0:
                    break
                tower.upgrade()

    def updateObstacles(self, obstacle):
        x = obstacle.pos[0] // self.tile_size
        y = obstacle.pos[1] // self.tile_size
        self.game_map_data[x][y] = obstacle.image_number
        self.obstacles.append(obstacle)
        self.player1.setGameMap(game_map_data=self.game_map_data)
        self.player2.setGameMap(game_map_data=self.game_map_data)

    def run(self):
        self.player1.deleteCastle()
        self.player2.deleteCastle()
        self.player1.deleteTowers()
        self.player2.deleteTowers()
        is_game = True
        while is_game:
            self.clock.tick(60)
            self.screen.blit(self.bg_img, (0, 0))
            self.side_menu.draw(self.screen)
            if self.turn == self.player1:
                next_turn = "TURN OF Player 1"
            else:
                next_turn = "TURN OF Player 2"
            pygame.font.init()
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render(next_turn, False, (0, 0, 0))
            self.screen.blit(text_surface, (0, 0))  # It displays just for a moment.
            self.game_map.draw_tiles()
            castle_list = [self.player1.castle, self.player2.castle]
            for castle in castle_list:
                if castle is not None:
                    castle.draw_castle()
                    castle.draw_health_bar()
            for obs in self.obstacles:
                obs.draw()
                obs.draw_health_bar()
            pos = pygame.mouse.get_pos()
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
            for event in pygame.event.get():
                if event.type == QUIT:
                    return #self.player1, self.player2, self.turn, self.towers, self.obstacles, None
                elif event.type == MOUSEBUTTONUP:
                    if self.moving_object is not None:
                        not_allowed = False
                        check_list = self.towers + self.obstacles + self.player1.getGoldMines() + self.player2.\
                            getGoldMines() + [self.player1.castle, self.player2.castle]
                        while None in check_list:
                            check_list.remove(None)
                        if len(check_list) != 0:
                            for mov_obj in check_list:
                                if mov_obj.collide(self.moving_object) or self.moving_object.isInappropriate:
                                    not_allowed = True
                                    break
                        else:
                            if self.moving_object.isInappropriate:
                                not_allowed = True
                        if not not_allowed:
                            if "Hurdle" == self.moving_object.getType():
                                self.updateObstacles(self.moving_object)
                            else:
                                if self.turn == self.player1:
                                    if "castle" in self.moving_object.getType().lower():
                                        self.player1.setCastle(self.moving_object)
                                else:
                                    if "castle" in self.moving_object.getType().lower():
                                        self.player2.setCastle(self.moving_object)
                            self.moving_object.moving = False
                            self.moving_object = None
                # draw images at positions
                elif event.type == MOUSEBUTTONDOWN:
                    side_menu_button = self.side_menu.get_clicked(event.pos[0], event.pos[1])
                    if self.turn == self.player1:
                        rt = self.buttons(side_menu_button, self.player1)
                    else:
                        rt = self.buttons(side_menu_button, self.player2)
                    if rt == "MAIN":
                        result = MapEditor.save(self)
                        return self.player1, self.player2, self.turn, self.towers, self.obstacles, result
                    if rt is not None:
                        self.turn = rt
            pygame.display.flip()
            pygame.display.update()

