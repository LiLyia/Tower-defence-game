import menu
from tower import *
from FireTower import *
from ice_tower import *
from goldmine import *
from game_map import *
from castle import *
from pygame.locals import *


class MapEditor:
    def __init__(self, imager, screen, turn, player1, player2, tower_images,
                 fire_tower_images, ice_tower_images, tile_size, clock, bg_img):
        self.__createMapData()
        self.tile_size = tile_size
        self.imager = imager
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
        if side_menu_button == "BackT":
            self.side_menu.clear_btn("BasicTower")
            self.side_menu.clear_btn("FireTower")
            self.side_menu.clear_btn("SlowingTower")
            self.side_menu.clear_btn("UpgradeTower")
            self.side_menu.clear_btn("BackT")
            self.mainButtons()
        elif side_menu_button == "BackG":
            self.side_menu.clear_btn("GoldMine")
            self.side_menu.clear_btn("BackG")
            self.side_menu.clear_btn("hurdle1")
            self.side_menu.clear_btn("hurdle2")
            self.side_menu.clear_btn("hurdle3")
            self.mainButtons()
        elif side_menu_button == "BackC":
            self.side_menu.clear_btn("Castle")
            self.side_menu.clear_btn("BackC")
            self.mainButtons()
        elif side_menu_button == "Towers":
            self.clearMainButtons()
            self.side_menu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png')
                                                          .convert_alpha(), (50, 50)), "BackT", 0)
            self.side_menu.add_btn(self.imager.getTowerImage(0, 0, 0), "BasicTower", 0)
            self.side_menu.add_btn(self.imager.getTowerImage(0, 1, 0), "FireTower", 0)
            self.side_menu.add_btn(self.imager.getTowerImage(2, 2, 0), "SlowingTower", 0)
            self.side_menu.add_btn(self.imager.getTowerImage(1, 1, 0), "UpgradeTower", 0)
        elif side_menu_button == "Obstacles":
            self.clearMainButtons()
            self.side_menu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png')
                                                          .convert_alpha(), (50, 50)), "BackG", 0)
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (60, 60)), "GoldMine",
                0)
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/Hurdles/hurdle_1.png')
                                       .convert_alpha(), (60, 60)), "hurdle1", 0)
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/Hurdles/hurdle_2.png').convert_alpha(), (60, 60)),
                "hurdle2",
                0)
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/Hurdles/hurdle_3.png').convert_alpha(), (60, 60)),
                "hurdle3",
                0)
        elif side_menu_button == "Castles":
            self.clearMainButtons()
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)),
                "BackC", 0)
            self.side_menu.add_btn(
                pygame.transform.scale(pygame.image.load('Images/Castle/castle1_100.png')
                                       .convert_alpha(), (120, 80)), "Castle", 0)
        elif side_menu_button in ["BasicTower", "FireTower", "SlowingTower"]:
            self.add_tower(side_menu_button, self.screen)
        elif side_menu_button == "Castle":
            self.add_castle(self.screen)
        elif side_menu_button == "UpgradeTower":
            self.upgrade_tower(player)
        elif side_menu_button == "GoldMine":
            self.add_gold_mine(self.screen)
        elif type(side_menu_button) == str and "hurdle" in side_menu_button:
            self.addObstacle(side_menu_button, self.screen)
        elif side_menu_button == "Turn":
            if self.turn == self.player1:
                return self.player2
            else:
                return self.player1
        elif side_menu_button == "Menu":
            return self.main_menu()

    def mainButtons(self):
        self.side_menu.add_btn(self.imager.getTowerImage(0, 0, 0), "Towers", 0)
        self.side_menu.add_btn(pygame.transform.scale(self.imager.getCastleImage(0, 0), (120, 80)), "Castles", 0)
        self.side_menu.add_btn(pygame.transform.scale(pygame.image.load('Images/turn.png')
                                                      .convert_alpha(), (120, 50)), "Turn", 0)
        self.side_menu.add_btn(
            pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Obstacles", 0)
        self.side_menu.add_btn(
            pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)), "Menu", 0)

    def clearMainButtons(self):
        self.side_menu.clear_btn("Towers")
        self.side_menu.clear_btn("Castles")
        self.side_menu.clear_btn("Turn")
        self.side_menu.clear_btn("Obstacles")
        self.side_menu.clear_btn("Menu")

    def addObstacle(self, side_menu_button, screen):
        x, y = pygame.mouse.get_pos()
        try:
            self.moving_object = self.create_obstacle(side_menu_button, x, y, screen)
            self.moving_object.moving = True
        except Exception as e:
            print(str(e) + "Cannot create an obstacle")

    def create_obstacle(self, name, x, y, screen):
        if "hurdle" in name:
            return Obstacle.createObstacle(pos=(x, y), screen=screen, imager=self
                                           .imager, tile_size=self.tile_size, image_number=int(name[-1]))
        else:
            return None

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

    def add_tower(self, name, screen):
        # Parameters: name - the name of the clicked button; screen - the screen.
        # Checks if the tower can be created. If yes, calls create_tower function. If no, prints an error
        x, y = pygame.mouse.get_pos()
        try:
            obj = self.__create_tower(name, x, y, screen)
            if obj is not None:
                self.moving_object = obj
                self.moving_object.moving = True
        except Exception as e:
            print(str(e) + " NOT VALID NAME")

    def __create_tower(self, name, x, y, screen):
        # Parameters: name - name of the button; x - x position; y - y position; screen - the screen.
        # Creates a tower object and adds it to tower list.
        if self.turn == self.player1:
            color = self.player1.color
        else:
            color = self.player2.color
        if name == "BasicTower":
            return Tower.createTower((x, y), self.tower_images, screen, color)
        elif name == "FireTower":
            return FireTower.createTower((x, y), self.fire_tower_images, screen, color)
        elif name == "SlowingTower":
            return IceTower.createTower((x, y), self.ice_tower_images, screen, color)
        else:
            return None

    def add_gold_mine(self, screen):
        # Parameters: screen - the screen.
        # Checks if the gold mine can be created. If yes, creates it. If no, prints the error.
        x, y = pygame.mouse.get_pos()
        if self.turn == self.player1:
            color = self.player1.color
        else:
            color = self.player2.color
        try:
            self.moving_object = GoldMine((x, y), screen, color)
            self.moving_object.moving = True
        except Exception as e:
            print(str(e) + " Gold Mine Cannot Be Created")

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
                    return self.player1, self.player2, self.turn, self.towers, self.obstacles
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
                                    if "tower" in self.moving_object.getType().lower():
                                        self.player1.tower_list.append(self.moving_object)
                                    elif "castle" in self.moving_object.getType().lower():
                                        self.player1.setCastle(self.moving_object)
                                    else:
                                        self.player1.getGoldMines().append(self.moving_object)
                                else:
                                    if "tower" in self.moving_object.getType().lower():
                                        self.player2.tower_list.append(self.moving_object)
                                    elif "castle" in self.moving_object.getType().lower():
                                        self.player2.setCastle(self.moving_object)
                                    else:
                                        self.player2.getGoldMines().append(self.moving_object)
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
                        return self.player1, self.player2, self.turn, self.towers, self.obstacles
                    if rt is not None:
                        self.turn = rt
            # Find possible targets for units and towers
            towers = self.player1.getTowers() + self.player2.getTowers()
            for tower in towers:
                tower.draw_tower()
                tower.draw_health_bar()
            for mine in self.player1.getGoldMines():
                mine.draw()
                mine.draw_health_bar()
            for mine in self.player2.getGoldMines():
                mine.draw()
                mine.draw_health_bar()
            pygame.display.flip()
            pygame.display.update()

    @staticmethod
    def main_menu():
        return "MAIN"
