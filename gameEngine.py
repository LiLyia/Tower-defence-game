from pygame import mixer
from game_instructions import game_instruction
from gui_button import Button
from pygame.locals import *
from castle import Castle
from game_map import GameMap
from tower import *
from FireTower import *
from imageCreator import *
from player import *
from ice_tower import *
from obstacle import *
from mapEditor import *
import menu
import random
import sys


class Main:
    moving_object = None
    # -----------Colors------------------------#
    WHITE = (255, 255, 255)
    # ------------------game------------------#
    screen = pygame.init()
    SCREEN_HEIGHT, SCREEN_WIDTH = 650, 850
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Defence Tower")
    #  -----------Adjusting the Frame of the Game------------#
    clock = pygame.time.Clock()
    FPS = 60
    # -----------BG Image---------------------#
    bg_img = pygame.image.load("Images/Background/bg_1.png")
    # --------------SideMenu--------------------
    imager = ImageCreator.createImageCreator('Images')
    # creating towers
    tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                     pygame.image.load('Images/Towers/tower2.png'),
                     pygame.image.load('Images/Towers/tower3.png')]]
    fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),
                          pygame.image.load('Images/Towers/firetower.png'),
                          pygame.image.load('Images/Towers/firetower.png')]]
    ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')]]
    # randomly picking the position of castle 1 position
    castle1_pos = [(150, 100), (200, 100), (250, 100), (300, 100), (350, 100), (400, 100), (450, 100)]
    position_castle1 = random.choice(castle1_pos)
    # randomly picking the position of castle 2 position
    castle2_pos = [(150, 450), (200, 450), (250, 450), (300, 450), (350, 450), (400, 450), (450, 450)]
    position_castle2 = random.choice(castle2_pos)
    castle1 = Castle(imager, position_castle1, screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
    castle2 = Castle(imager, position_castle2, screen, 1, [(0, 0, 0), (0, 0, 255), (255, 0, 0)])
    tile_size = 50
    # -----------------Game Map---------------------
    game_map_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
        [1, 0, 2, 2, 0, 0, 0, 0, 0, 3, 2, 0, 1],
        [1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    game_map = GameMap(game_map_data, tile_size, screen, imager=imager)
    player1 = Player(screen, game_map_data, castle1, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
    player2 = Player(screen, game_map_data, castle2, [(0, 0, 0), (0, 0, 255), (255, 0, 0)])
    obstacles = game_map.getObstacles()
    towers = []
    turn = player1

    def clean():
        # Parameters: no parameters.
        # Cleans class parameters.
        Main.moving_object = None
        Main.position_castle1 = random.choice(Main.castle1_pos)
        Main.position_castle2 = random.choice(Main.castle2_pos)
        Main.castle1 = Castle(Main.imager, Main.position_castle1, Main.screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        Main.castle2 = Castle(Main.imager, Main.position_castle2, Main.screen, 1, [(0, 0, 0), (0, 0, 255), (255, 0, 0)])
        Main.player1 = Player(Main.screen, Main.game_map_data, Main.castle1, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        Main.player2 = Player(Main.screen, Main.game_map_data, Main.castle2, [(0, 0, 0), (0, 0, 255), (255, 0, 0)])
        Main.game_map = GameMap(Main.game_map_data, Main.tile_size, Main.screen, imager=Main.imager)
        Main.obstacles = Main.game_map.getObstacles()
        Main.turn = Main.player1

    def win(player):
        # Parameters: player - the number of the player who won.
        # Creates a window saying who won the game.
        screen = pygame.display.set_mode((400, 280))
        clock = pygame.time.Clock()
        FPS = 60
        if player == 1:
            bg_img = Main.imager.getBackgroundImage(3)  # pygame.image.load("Images/Background/winner-1.png")
        else:
            bg_img = Main.imager.getBackgroundImage(4)  # pygame.image.load("Images/Background/winner-2.png")
        bg_img = pygame.transform.scale(bg_img, (400, 220))
        menu_button = Button(25, 200, "Menu")
        while True:
            clock.tick(FPS)
            screen.blit(bg_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if menu_button.draw_Button(screen):
                    Main.main_menu()
            pygame.display.update()

    def main_menu():
        # Parameters: no parameters.
        # Creates the menu of the game.
        screen = pygame.init()
        SCREEN_HEIGHT, SCREEN_WIDTH = 850, 650
        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption("Defence Tower")
        #  -----------Adjusting the Frame of the Game------------#
        clock = pygame.time.Clock()
        FPS = 60
        # -----------BG Image---------------------#
        bg_img = pygame.image.load("Images/Background/bg_2.png")
        bg_img = pygame.transform.scale(bg_img, (SCREEN_HEIGHT, SCREEN_WIDTH))
        # ----------------Background music--------------
        mixer.music.load('Music/background.wav')
        mixer.music.play(1)
        pygame.mixer.music.set_volume(0.05)
        # Using Button class
        Continue_game = Button(240, 80, "Continue")
        Start_game = Button(240, 155, "New game")
        instruction = Button(240, 230, "Instructions")
        map_editor = Button(240, 305, "Map editor")
        quit_button = Button(240, 380, "Quit")
        is_game = True
        while is_game:
            clock.tick(FPS)
            screen.blit(bg_img, (0, 0))
            if Continue_game.draw_Button(screen):
                pygame.mixer.music.stop()
                Main.game_start()
            if Start_game.draw_Button(screen):
                pygame.mixer.music.stop()
                Main.clean()
                Main.game_start()
            if instruction.draw_Button(screen):
                game_instruction()
            if map_editor.draw_Button(screen):
                pygame.mixer.music.stop()
                editor =  MapEditor(Main.imager, screen, Main.turn, Main.player1, Main.player2, Main.tower_images,
                 Main.fire_tower_images, Main.ice_tower_images, Main.tile_size, clock, Main.bg_img)
                Main.player1, Main.player2, Main.turn, Main.towers, Main.obstacles = editor.run()
                if Main.player1.castle is None or Main. player2.castle is None:
                    Main.player1.setCastle(Main.castle1)
                    Main.player2.setCastle(Main.castle2)
                Main.main_menu()

            if quit_button.draw_Button(screen):
                pygame.quit()
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def game_start():
        # Parameters: no parameters.
        # Creates the game.
        is_game = True

        sideMenu = menu.VerticalMenu(750, 120, pygame.transform.scale(pygame.image.load('Images/menu.png')
                                                                      .convert_alpha(), (200, 650)))
        sideMenu.add_btn(Main.imager.getTowerImage(0, 0, 0), "Towers", 0)
        sideMenu.add_btn(Main.imager.getUnitImage(0, 0), "Units", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/turn.png').convert_alpha(), (120, 50)),
                         "Turn", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)),
                         "Gold", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)),
                         "Menu", 0)

        def displayBullets(tower_list):
            # Parameters: building_list - the list of towers. 
            # Draws bullets.
            for tower in tower_list:
                if type(tower) == FireTower:
                    for bullet in tower.bulletList:
                        if bullet.target is not None:
                            bullet.drawBullets(Main.screen)

        def clearBullets(tower_list):
            # Parameters: towerList - the list towers.
            # Clears the bullets from the map.If bullets hits or miss the enemy , they will be deleted.
            for tower in tower_list:
                if type(tower) == FireTower:
                    for bullet in tower.bulletList:
                        if bullet.hitEnemy == True:
                            tower.bulletList.remove(bullet)
                        if tower.current_target is None:
                            tower.bulletList.remove(bullet)

        def clearObjects(safe_player, enemy_player, goldMines):
            # Parameters: safe_player - the current player; enemy_player - another player. 
            # Removes dead units, towers and obstacles from the lists.
            unit_list = safe_player.getUnits()
            tower_list = safe_player.getTowers()
            for unit in unit_list:
                if unit.health <= 0:
                    unit_list.remove(unit)
                    unit.remove()
                if type(unit) != UvsU and type(unit) != UvsB and type(unit) != UvsO:
                    if unit.pos == enemy_player.castle_pos:
                        enemy_player.castle.reduceHealth()
                        if unit.health > 0:
                            unit_list.remove(unit)
                            unit.remove()
            for tower in tower_list:
                if tower.health <= 0:
                    tower_list.remove(tower)
            for mine in goldMines:
                if mine.health <= 0:
                    goldMines.remove(mine)
                    mine.remove()
            for obs in Main.obstacles:
                if obs.health <= 0:
                    Main.obstacles.remove(obs)

        def findTargetforTowers(unit_list, tower_list):
            # Parameters: unit_list - the list of units; tower_list - the list of towers.
            # Gets the target for each tower in the list of targetable units.
            for tower in tower_list:
                if type(tower) == FireTower or type(tower) == IceTower:
                    tower.targetList = []
                    for unit in unit_list:
                        if tower.hitbox.colliderect(unit.hitbox):
                            tower.targetList.append(unit)

        def currentTowerTarget(tower_list):
            # Parameters: building_list - the list of towers.
            # Gets the target for each tower in the list of targetable units.
            for tower in tower_list:
                if type(tower) == FireTower or type(tower) == IceTower:
                    for target in tower.targetList:
                        if tower.current_target is None:
                            tower.current_target = target
                        if tower.current_target.health < 0:
                            tower.targetList.remove(target)
                        if tower.current_target.pos[0] <= target.pos[0]:
                            tower.current_target = target
                    if len(tower.targetList) == 0:
                        tower.current_target = None

        def shootTowers(tower_list):
            # Parameters: towerList - the list of towers.
            # If tower detects an enemy , this function will be activated and shoot to the enemies.
            for tower in tower_list:
                if type(tower) == FireTower:
                    if tower.current_target is not None:
                        tower.shoot()
                if type(tower) == IceTower:
                    if tower.current_target is not None and not tower.current_target.isStopped:
                        tower.current_target.setStopped(True)
                    elif tower.current_target is not None and tower.current_target.isStopped:
                        tower.current_target.setStopped(False)

        def findMoveforUnits(safe, enemy, goldmines):
            # Parameters: unit list, tower list, obstacle list. 
            # Depending on the unit type, defines possible enemies for units, adding them to the target list.
            obstacle_list = []
            safe.move_target = None
            for mine in goldmines:
                obstacle_list.append(mine)
            for obs in Main.obstacles:
                obstacle_list.append(obs)
            safe_units = safe.getUnits()
            enemy_units = enemy.getUnits()
            enemy_towers = enemy.getTowers()
            n = len(safe_units)
            for i in range(n):
                safe_units[i].moveList = []
                if type(safe_units[i]) == UvsU:
                    for j in range(len(enemy_units)):
                        safe_units[i].moveList.append(enemy_units[j])
                if type(safe_units[i]) == UvsB:
                    for m in enemy_towers:
                        safe_units[i].moveList.append(m)
                if type(safe_units[i]) == UvsO:
                    for m in obstacle_list:
                        safe_units[i].moveList.append(m)

        def findTargetforUnits(safe, enemy, goldmines):
            # Parameters: safe - the current player; enemy - second player; goldmines - the list of gold mines.
            # The function defines possible targets for units withing the attack range.
            safe_units = safe.getUnits()
            enemy_units = enemy.getUnits()
            enemy_towers = enemy.getTowers()
            obstacle_list = []
            for mine in goldmines:
                obstacle_list.append(mine)
            for obs in Main.obstacles:
                obstacle_list.append(obs)
            unitLength = len(safe_units)
            for i in range(unitLength):
                safe_units[i].targetList = []
                safe_units[i].current_target = None
                if type(safe_units[i]) == UvsU:
                    for enemy in enemy_units:
                        if safe_units[i].hitbox.colliderect(enemy.hitbox):
                            safe_units[i].targetList.append(enemy)
                if type(safe_units[i]) == UvsB:
                    for enemy in enemy_towers:
                        if safe_units[i].hitbox.colliderect(enemy.hitbox):
                            safe_units[i].targetList.append(enemy)
                if type(safe_units[i]) == UvsO:
                    for obs in obstacle_list:
                        if safe_units[i].hitbox.colliderect(obs.hitbox):
                            safe_units[i].targetList.append(obs)

        def currentUnitTarget(unit_list):
            # Parameters: unit_list - the list of units. 
            # The function defines the target of the current turn, adds it to the current target list.  
            for unit in unit_list:
                unit.current_target = None
                if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
                    for target in unit.targetList:
                        if unit.current_target is None:
                            unit.current_target = target
                            if unit.current_target.health < 0:
                                unit.targetList.remove(target)
                        if unit.current_target.pos[0] <= target.pos[0]:
                            unit.current_target = target
                    if len(unit.targetList) == 0:
                        unit.current_target = None

        def shootUnits(unit_list):
            # Parameters: unit_list - the list of units.
            # The function makes units attack the objects.   
            for unit in unit_list:
                if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
                    if unit.current_target is not None:
                        unit.attack(type(unit))
                        if unit.current_target.health < 0:
                            unit.current_target = None

        def create_tower(name, x, y, screen):
            # Parameters: name - name of the button; x - x position; y - y position; screen - the screen. 
            # Creates a tower object and adds it to tower list.
            tower = None
            if Main.turn == Main.player1:
                color = Main.player1.color
            else:
                color = Main.player2.color
            if name == "BasicTower" and Main.turn.checkCost("BasicTower"):
                tower = Tower.createTower((x, y), Main.tower_images, screen, color)
            elif name == "FireTower" and Main.turn.checkCost("FireTower"):
                tower = FireTower.createTower((x, y), Main.fire_tower_images, screen, color)
            elif name == "SlowingTower" and Main.turn.checkCost("SlowingTower"):
                tower = IceTower.createTower((x, y), Main.ice_tower_images, screen, color)
            else:
                return None
            return tower

        def upgrade_tower(turn):
            # Parameters: turn - the current player.
            # The function upgrades the first ready to be upgraded basic tower.
            for tower in turn.getTowers():
                if type(tower) != FireTower and type(tower) != IceTower:
                    if tower.maxUp == 0:
                        break
                    if turn.checkCost("UpgradeTower"):
                        tower.upgrade()

        def add_tower(name, screen):
            # Parameters: name - the name of the clicked button; screen - the screen.
            # Checks if the tower can be created. If yes, calls create_tower function. If no, prints an error
            global obj
            x, y = pygame.mouse.get_pos()
            try:
                obj = create_tower(name, x, y, screen)
                if obj is not None:
                    Main.moving_object = obj
                    obj.moving = True
            except Exception as e:
                print(str(e) + " NOT VALID NAME")

        def add_gold_mine(screen):
            # Parameters: screen - the screen.
            # Checks if the gold mine can be created. If yes, creats it. If no, prints the error.
            global obj
            x, y = pygame.mouse.get_pos()
            if Main.turn == Main.player1:
                color = Main.player1.color
            else:
                color = Main.player2.color
            try:
                if Main.turn.checkCost("GoldMine"):
                    obj = GoldMine((x, y), screen, color)
                    Main.moving_object = obj
                    obj.moving = True
            except Exception as e:
                print(str(e) + " Gold Mine Cannot Be Created")

        def addGolds(goldmineList, player):
            # Parameters: goldmineList - the list of gold mines; player - the player name
            # Adds additional to the player according to his gold mines.
            for mine in goldmineList:
                mine.addGold(player)

        def castlePos(turn):
            # Parameters: turn - the current player. 
            # Return: current player`s castle position.
            if turn == Main.player1:
                return Main.player1.getCastlePos()
            else:
                return Main.player2.getCastlePos()

        def targeting():
            # Calls function for units and towers to define enemies.
            findTargetforUnits(Main.player1, Main.player2, Main.player2.getGoldMines())
            findTargetforUnits(Main.player2, Main.player1, Main.player1.getGoldMines())
            findTargetforTowers(Main.player1.getUnits(), Main.player2.getTowers())
            findTargetforTowers(Main.player2.getUnits(), Main.player1.getTowers())
            currentUnitTarget(Main.player1.getUnits())
            currentUnitTarget(Main.player2.getUnits())
            currentTowerTarget(towers)

        def turnSwitch(turn):
            # Parameters: current_turn - the current player.
            # Switches turn to another player.
            if turn == Main.player2:
                Main.player1.gold += 200
                Main.player2.gold += 200
                addGolds(Main.player1.getGoldMines(), Main.player1)
                addGolds(Main.player2.getGoldMines(), Main.player2)
            findMoveforUnits(Main.player1, Main.player2, Main.player2.getGoldMines())
            findMoveforUnits(Main.player2, Main.player1, Main.player1.getGoldMines())
            for unit in Main.player1.getUnits():
                if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
                    if len(unit.moveList) > 0:
                        unit.move(Main.obstacles)
                else:
                    unit.move(Main.player2.castle_pos, Main.obstacles)

            for unit in Main.player2.getUnits():
                if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
                    if len(unit.moveList) > 0:
                        unit.move(Main.obstacles)
                else:
                    unit.move(Main.player1.castle_pos, Main.obstacles)
            targeting()
            # Attack
            shootUnits(Main.player1.getUnits())
            shootUnits(Main.player2.getUnits())
            shootTowers(Main.player1.getTowers())
            shootTowers(Main.player2.getTowers())
            # Draw bullets
            displayBullets(towers)
            # Delete bullets and dead objects from the game
            clearBullets(towers)
            clearObjects(Main.player1, Main.player2, Main.player1.getGoldMines())
            clearObjects(Main.player2, Main.player1, Main.player2.getGoldMines())

        def buttons(side_menu_button, player):
            # Parameters: side_menu_button - the name of the button from the side menu; player - the current player.
            # Vertical menu implementation, draws and clears the buttons.
            if side_menu_button == "BackT":
                sideMenu.clear_btn("BasicTower")
                sideMenu.clear_btn("FireTower")
                sideMenu.clear_btn("SlowingTower")
                sideMenu.clear_btn("UpgradeTower")
                sideMenu.add_btn(Main.imager.getTowerImage(0, 0, 0), "Towers", 0)
                sideMenu.add_btn(Main.imager.getUnitImage(0, 0), "Units", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)), "Menu",
                    0)
                sideMenu.clear_btn("BackT")
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/turn.png').convert_alpha(), (120, 50)), "Turn", 0)
            elif side_menu_button == "BackG":
                sideMenu.clear_btn("GoldMine")
                sideMenu.clear_btn("BackG")
                sideMenu.add_btn(Main.imager.getTowerImage(0, 0, 0), "Towers", 0)
                sideMenu.add_btn(Main.imager.getUnitImage(0, 0), "Units", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/turn.png').convert_alpha(), (120, 50)), "Turn", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)), "Menu",
                    0)
            elif side_menu_button == "BackU":
                sideMenu.clear_btn("BasicUnit")
                sideMenu.clear_btn("vsObstacles")
                sideMenu.clear_btn("vsTowers")
                sideMenu.clear_btn("vsUnits")
                sideMenu.add_btn(Main.imager.getTowerImage(0, 0, 0), "Towers", 0)
                sideMenu.add_btn(Main.imager.getUnitImage(0, 0), "Units", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
                sideMenu.clear_btn("BackU")
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/turn.png').convert_alpha(), (120, 50)), "Turn", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/mainmenu.png').convert_alpha(), (120, 50)), "Menu",
                    0)
            elif side_menu_button == "Towers":
                sideMenu.clear_btn("Towers")
                sideMenu.clear_btn("Units")
                sideMenu.clear_btn("Gold")
                sideMenu.clear_btn("Turn")
                sideMenu.clear_btn("Menu")
                sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)),
                                 "BackT", 0)
                sideMenu.add_btn(Main.imager.getTowerImage(0, 0, 0), "BasicTower", 200)
                sideMenu.add_btn(Main.imager.getTowerImage(0, 1, 0), "FireTower", 200)
                sideMenu.add_btn(Main.imager.getTowerImage(2, 2, 0), "SlowingTower", 200)
                sideMenu.add_btn(Main.imager.getTowerImage(1, 1, 0), "UpgradeTower", 200)
            elif side_menu_button == "Units":
                sideMenu.clear_btn("Towers")
                sideMenu.clear_btn("Units")
                sideMenu.clear_btn("Gold")
                sideMenu.clear_btn("Turn")
                sideMenu.clear_btn("Menu")
                sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)),
                                 "BackU", 0)
                sideMenu.add_btn(Main.imager.getUnitImage(0, 0), "BasicUnit", 100)
                sideMenu.add_btn(Main.imager.getUnitImage(1, 0), "vsObstacles", 100)
                sideMenu.add_btn(Main.imager.getUnitImage(3, 0), "vsTowers", 150)
                sideMenu.add_btn(Main.imager.getUnitImage(2, 0), "vsUnits", 100)
            elif side_menu_button == "Gold":
                sideMenu.clear_btn("Towers")
                sideMenu.clear_btn("Units")
                sideMenu.clear_btn("Turn")
                sideMenu.clear_btn("Gold")
                sideMenu.clear_btn("Menu")
                sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)),
                                 "BackG", 0)
                sideMenu.add_btn(
                    pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "GoldMine",
                    100)
            elif side_menu_button in ["BasicTower", "FireTower", "SlowingTower"]:
                add_tower(side_menu_button, Main.screen)
            elif side_menu_button == "UpgradeTower":
                upgrade_tower(player)
            elif side_menu_button == "GoldMine":
                add_gold_mine(Main.screen)
            elif side_menu_button == "Turn":
                pygame.font.init()
                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                if Main.turn == Main.player1:
                    next_turn = "TURN OF Player 1"
                else:
                    next_turn = "TURN OF Player 2"
                text_surface = my_font.render(next_turn, False, (0, 0, 0))
                Main.screen.blit(text_surface, (0, 0))  # It displays just for a moment.
                turnSwitch(Main.turn)
                if Main.turn == Main.player1:
                    return Main.player2
                else:
                    return Main.player1
            elif side_menu_button in ["BasicUnit", "vsObstacles", "vsTowers", "vsUnits"]:
                player.addUnit(side_menu_button)
            elif side_menu_button == "Menu":
                Main.main_menu()

        # Main Game cycle
        while is_game:
            Main.clock.tick(Main.FPS)
            Main.screen.blit(Main.bg_img, (0, 0))
            Main.player1.castle.draw_castle()
            Main.player1.castle.draw_health_bar()
            Main.player2.castle.draw_castle()
            Main.player2.castle.draw_health_bar()
            sideMenu.draw(Main.screen)
            Main.game_map.draw_tiles()
            for obs in Main.obstacles:
                obs.draw()
                obs.draw_health_bar()
            pos = pygame.mouse.get_pos()
            my_font = pygame.font.SysFont('Comic Sans MS', 20)
            next_turn = "Your amount of Gold: " + str(Main.turn.gold)
            text_surface = my_font.render(next_turn, False, (0, 0, 0))
            if Main.turn == Main.player1:
                Main.screen.blit(text_surface, (400, 0))
            else:
                Main.screen.blit(text_surface, (0, 600))
            if Main.moving_object:
                Main.moving_object.move(pos[0], pos[1])
            for event in pygame.event.get():
                if event.type == QUIT:
                    Main.main_menu()
                elif event.type == MOUSEBUTTONUP:
                    if Main.moving_object is not None:
                        not_allowed = False
                        check_list = Main.towers + Main.obstacles + Main.player1.getGoldMines() + \
                                     Main.player2.getGoldMines() + [Main.castle1, Main.castle2]
                        for mov_obj in check_list:
                            if mov_obj.collide(Main.moving_object) or Main.moving_object.isInappropriate:
                                not_allowed = True
                                break
                        if not not_allowed:
                            if Main.turn == Main.player1:
                                if "tower" in Main.moving_object.getType().lower():
                                    Main.player1.tower_list.append(Main.moving_object)
                                else:
                                    Main.player1.getGoldMines().append(Main.moving_object)
                            else:
                                if "tower" in Main.moving_object.getType().lower():
                                    Main.player2.tower_list.append(Main.moving_object)
                                else:
                                    Main.player2.getGoldMines().append(Main.moving_object)
                            Main.moving_object.moving = False
                            Main.moving_object = None
                # draw images at positions
                elif event.type == MOUSEBUTTONDOWN:
                    side_menu_button = sideMenu.get_clicked(event.pos[0], event.pos[1])
                    if Main.turn == Main.player1:
                        rt = buttons(side_menu_button, Main.player1)
                    else:
                        rt = buttons(side_menu_button, Main.player2)
                    if rt is not None:
                        Main.turn = rt
            # Find possible targets for units and towers
            units = Main.player1.getUnits() + Main.player2.getUnits()
            towers = Main.player1.getTowers() + Main.player2.getTowers()
            for tower in towers:
                tower.draw_tower()
                tower.draw_health_bar()
            for unit in units:
                unit.draw()
                unit.draw_health_bar()
            for mine in Main.player1.getGoldMines():
                mine.draw()
                mine.draw_health_bar()
            for mine in Main.player2.getGoldMines():
                mine.draw()
                mine.draw_health_bar()
            pygame.display.flip()
            pygame.display.update()
            if Main.castle1.isDead() or Main.castle2.isDead():
                is_game = False
        if Main.castle1.isDead():
            print("Player 2 Won!!!!")
            Main.clean()
            Main.win(2)
        else:
            print("Player 1 Won!!!")
            Main.clean()
            Main.win(1)


Main.main_menu()
