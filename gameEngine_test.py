import unittest
from castle import Castle
import tower
import unit
from imageCreator import *
import pygame
from obstacle import Obstacle
import FireTower
import ice_tower
import goldmine
import obstacle
import player
from gui_button import Button

game_map_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
import platform

if platform.system() == "Windows":
    SCREEN_HEIGHT, SCREEN_WIDTH = 650, 850
    screen = pygame.display.init()
    ##screen = pygame.display.set_mode(size=(0,0),flags=0,depth=0,display=0,vsync=0)
    print(pygame.display.list_modes())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    imager = ImageCreator.createImageCreator('Images')


class TESTGAME(unittest.TestCase):
    # Test Function for the Castle
    def test_castleCreation(self):
        castle1 = Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(castle1.health, 1200)
        self.assertEqual(castle1.player_number, 0)

    def test_castleDead(self):

        castle1 = Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_dead = castle1.isDead()
        expected_dead = False
        self.assertEqual(actual_dead, expected_dead)


    def test_castleCollide(self):
        castle1 = Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        tempObj = Obstacle.createObstacle((450, 300), screen, imager, 50, image_number=0, health=200, max_health=200)
        actual_collide = castle1.collide(tempObj)
        expected_collide = False
        self.assertEqual(actual_collide, expected_collide)


    def test_castlePositioning(self):
        castle1 = Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        if castle1.pos[0] > 600 - 25 or castle1.pos[1] > 600 - 35 or castle1.pos[0] < 50 or castle1.pos[1] < 50:
            actual_pos = False
        else:
            actual_pos = True

        expected_pos = True
        self.assertEqual(actual_pos, expected_pos)


    def test_castleType(self):
        castle1 = Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_type = castle1.getType()
        expected_type = "Castle"
        self.assertEqual(actual_type, expected_type)


    # Test for the BasicTower
    def test_towerCreation(self):

        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(tower1.health, 600)
        self.assertEqual(tower1.price, 100)
        self.assertEqual(tower1.healthLevel, 0)
        self.assertEqual(tower1._max_up, 3)


    def test_towerDead(self):
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_dead = tower1.isDead()
        expected_dead = False
        self.assertEqual(actual_dead, expected_dead)


    def test_towerUpgrade(self):
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_upgrade = tower1.upgrade()
        expected_upgrade = True
        self.assertEqual(actual_upgrade, expected_upgrade)



    def test_towerCollide(self):
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        tempObj = Obstacle.createObstacle((450, 300), screen, imager, 50, image_number=0, health=200, max_health=200)
        actual_collide = tower1.collide(tempObj)
        expected_collide = False
        self.assertEqual(actual_collide, expected_collide)


    def test_towerType(self):
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_type = tower1.getType()
        expected_type = "BasicTower"
        self.assertEqual(actual_type, expected_type)


    def test_towerPos(self):
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200, 100), tower_images, screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        if tower1.pos[0] > 600 - 25 or tower1.pos[1] > 600 - 35 or tower1.pos[0] < 50 or tower1.pos[1] < 50:
            actual_pos = False
        else:
            actual_pos = True

        expected_pos = True
        self.assertEqual(actual_pos, expected_pos)

    # Test for the FireTower

    def test_firetowerCreation(self):
        fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png')]]

        firetower1 = FireTower.FireTower.createTower((350, 400), fire_tower_images, screen,
                                                     [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(firetower1.health, 600)
        self.assertEqual(firetower1._price, 150)
        self.assertEqual(firetower1.range, 60)
        self.assertEqual(firetower1.damage, 110)
        self.assertEqual(firetower1.cd, 300)

        actual_currentTarget = firetower1.current_target
        expected_currentTarget = None
        self.assertEqual(actual_currentTarget, expected_currentTarget)


    def test_firetowerCd(self):
        fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png')]]

        firetower1 = FireTower.FireTower.createTower((350, 400), fire_tower_images, screen,
                                                     [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_cd = firetower1.check_cd()
        expected_cd = True
        self.assertEqual(actual_cd, expected_cd)


    def test_fireTowerCollid(self):
        fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png')]]

        firetower1 = FireTower.FireTower.createTower((350, 400), fire_tower_images, screen,
                                                     [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_collide = firetower1.collide(
            unit.Unit((300, 450), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)]))
        expected_collide = True
        self.assertEqual(actual_collide, expected_collide)

    def test_fireTowerTyep(self):
        fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png'),
                              pygame.image.load('Images/Towers/firetower.png')]]

        firetower1 = FireTower.FireTower.createTower((350, 400), fire_tower_images, screen,
                                                     [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_type = firetower1.getType()
        expected_type = "FireTower"
        self.assertEqual(actual_type, expected_type)

        if firetower1.pos[0] > 600 - 25 or firetower1.pos[1] > 600 - 35 or firetower1.pos[0] < 50 or firetower1.pos[
            1] < 50:
            actual_pos = False

        else:
            actual_pos = True

        expected_pos = True
        self.assertEqual(actual_pos, expected_pos)


    # Test for the IceTower
    def test_iceTowerCreation(self):


        ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')]]
        icetower1 = ice_tower.IceTower.createTower((200, 300), ice_tower_images, screen,
                                                   [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(icetower1.health, 600)
        self.assertEqual(icetower1.price, 200)
        self.assertEqual(icetower1.level, 0)


    def test_iceTowerDead(self):
        ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')]]
        icetower1 = ice_tower.IceTower.createTower((200, 300), ice_tower_images, screen,
                                                   [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_isDead = icetower1.isDead()
        expected_isDead = False
        self.assertEqual(actual_isDead, expected_isDead)


    def test_iceTowerType(self):

        ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')]]
        icetower1 = ice_tower.IceTower.createTower((200, 300), ice_tower_images, screen,
                                                   [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_type = icetower1.getType()
        expected_type = "SlowingTower"
        self.assertEqual(actual_type, expected_type)


    def test_iceTower_Collide(self):
        ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')]]
        icetower1 = ice_tower.IceTower.createTower((200, 300), ice_tower_images, screen,
                                                   [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        tempObj = Obstacle.createObstacle((175, 250), screen, imager, 50, image_number=0, health=200, max_health=200)
        actual_collide = icetower1.collide(tempObj)
        expected_collide = True
        self.assertEqual(actual_collide, expected_collide)
        #####################

        actual_pos_x = icetower1.pos[0]
        actual_pos_y = icetower1.pos[1]
        if actual_pos_x > 600 - 25 or actual_pos_y > 600 - 25 or actual_pos_x < 50 or actual_pos_y < 50:
            expected_pos = True
        else:
            expected_pos = False

        self.assertFalse(expected_pos)


    # Test for the Units
    def test_unitCreation(self):


        unit1 = unit.Unit((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_stopped = unit1.isStopped
        expected_stopped = False
        self.assertEqual(actual_stopped, expected_stopped)

    def test_unitMove(self):
        unit1 = unit.Unit((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_moveTarget = unit1.move_target
        expected_moveTarget = None
        self.assertEqual(actual_moveTarget, expected_moveTarget)



    def test_UvsUCreation(self):
        unit_uvsu = unit.UvsU((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(unit_uvsu.health, 500)  ## 800 at first
        self.assertEqual(unit_uvsu.max_health, 500)  ## 800 at first
        self.assertEqual(unit_uvsu.price, 100)
        self.assertEqual(unit_uvsu.attack_range, 50)
        self.assertEqual(unit_uvsu.cd, 150)

    def test_UvsUTargeting(self):
        unit_uvsu = unit.UvsU((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_lastTarget = unit_uvsu.last_target
        expected_lastTarget = None
        self.assertEqual(actual_lastTarget, expected_lastTarget)

        actual_currentTarget = unit_uvsu.current_target
        expected_currenTarget = None
        self.assertEqual(actual_currentTarget, expected_currenTarget)

    def test_UvsOCreation(self):
        unit_uvso = unit.UvsO((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(unit_uvso.health, 400)  ## 500 at first
        self.assertEqual(unit_uvso.max_health, 400)  ## 500 at first
        self.assertEqual(unit_uvso.price, 100)
        self.assertEqual(unit_uvso.attack_range, 50)
        self.assertEqual(unit_uvso.cd, 150)


    def test_UvsBCreation(self):
        unit_uvsb = unit.UvsB((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(unit_uvsb.health, 800)  ## 500 at first
        self.assertEqual(unit_uvsb.max_health, 800)  ## 500 at first
        self.assertEqual(unit_uvsb.price, 150)  ##100 at first
        self.assertEqual(unit_uvsb.attack_range, 50)
        self.assertEqual(unit_uvsb.cd, 150)


    # Test for the GoldMines

    def test_goldmineCreation(self):
        goldmine1 = goldmine.GoldMine((250, 300), screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(goldmine1.health, 300)
        self.assertEqual(goldmine1.price, 200)
        self.assertEqual(goldmine1.gold_amount, 50)  # 100 at first


    def test_goldmineCollid(self):
        goldmine1 = goldmine.GoldMine((250, 300), screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_collide = goldmine1.collide(
            Obstacle.createObstacle((175, 250), screen, imager, 50, image_number=0, health=200, max_health=200))
        expected_collide = True
        self.assertEqual(actual_collide, expected_collide)


    def test_goldminePosition(self):
        goldmine1 = goldmine.GoldMine((250, 300), screen, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_pos_x = goldmine1.pos[0]
        actual_pos_y = goldmine1.pos[1]
        if actual_pos_x > 575 or actual_pos_y > 565 or actual_pos_x < 50 or actual_pos_y < 50:
            expected_pos = True
        else:
            expected_pos = False

        self.assertFalse(expected_pos)


    def test_obstacleCreation(self):
        obstacle1 = obstacle.Obstacle.createObstacle((220, 120), screen, imager, tile_size=50)
        self.assertEqual(obstacle1.health, 200)


    def test_ObstacleType(self):
        obstacle1 = obstacle.Obstacle.createObstacle((220, 120), screen, imager, tile_size=50)
        actual_type = obstacle1.getType()
        expected_type = "Hurdle"
        self.assertEqual(actual_type, expected_type)


    def test_obstacleDeath(self):
        obstacle1 = obstacle.Obstacle.createObstacle((220, 120), screen, imager, tile_size=50)
        actual_isDead = obstacle1.isDead()
        expected_isDead = False
        self.assertEqual(actual_isDead, expected_isDead)


    def test_obstacleCollide(self):
        obstacle1 = obstacle.Obstacle.createObstacle((220, 120), screen, imager, tile_size=50)
        actual_collide = obstacle1.collide(
            unit.Unit((200, 100), screen, game_map_data, [(0, 0, 0), (255, 0, 0), (0, 255, 0)]))
        expected_collide = True
        self.assertEqual(actual_collide, expected_collide)


    def test_obstaclePos(self):
        obstacle1 = obstacle.Obstacle.createObstacle((220, 120), screen, imager, tile_size=50)
        actual_pos_x = obstacle1.pos[0]
        actual_pos_y = obstacle1.pos[1]

        if actual_pos_x > 575 or actual_pos_y > 565 or actual_pos_x < 50 or actual_pos_y < 50:
            expected_pos = True
        else:
            expected_pos = False

        self.assertFalse(expected_pos)


    # Test for the Player

    def test_playerCreate(self):
        player1 = player.Player(self, game_map_data,
                                Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)]),
                                [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(player1.gold, 500)


    def test_playerCosts(self):

        player1 = player.Player(self, game_map_data,
                                Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)]),
                                [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_costForBasic = player1.checkCost(tower.Tower.price)
        actual_costForFire = player1.checkCost(FireTower.FireTower.price)
        actual_costForUpgrade = player1.checkCost(200)
        actual_costForSlowing = player1.checkCost(ice_tower.IceTower.price)
        actual_costForGoldMine = player1.checkCost(player1.getGoldMines())

        expected_costForBasic = 200
        expected_costForFire = 200
        expected_costForIce = 200
        expected_costForUpgrade = 200
        expected_costForSlowing = 200
        expected_costForGoldMine = 100

        ######################
        if actual_costForGoldMine - expected_costForGoldMine >= 0:
            expected_Gold = True
        else:
            expected_Gold = False

        self.assertFalse(expected_Gold)
        ######################

        ######################
        if actual_costForSlowing - expected_costForIce >= 0:
            expected_Slow = True
        else:
            expected_Slow = False

        self.assertFalse(expected_Slow)
        ######################

        ######################
        if actual_costForBasic - expected_costForBasic >= 0:
            expected_Basic = True
        else:
            expected_Basic = False

        self.assertFalse(expected_Basic)
        ######################

        ######################
        if actual_costForFire - expected_costForFire >= 0:
            expected_Fire = True
        else:
            expected_Fire = False

        self.assertFalse(expected_Fire)
        ######################

        ######################
        if actual_costForUpgrade - expected_costForUpgrade >= 0:
            expected_upgrade = True
        else:
            expected_upgrade = False

        self.assertFalse(expected_upgrade)
        ######################

        ######################

        if actual_costForSlowing - expected_costForSlowing >= 0:
            expected_upgrade = True
        else:
            expected_upgrade = False

        self.assertFalse(expected_upgrade)
        ######################

    def test_playerCastleDelete(self):
        player1 = player.Player(self, game_map_data,
                                Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)]),
                                [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_delete = player1.deleteCastle()
        expected_delete = None
        self.assertEqual(actual_delete, expected_delete)

    def test_button(self):
        text = 'Start'
        button = Button(50, 50, text)
        self.assertEqual(button.hover_color, "#5480f0")
        self.assertFalse(button.clicked)
        self.assertEqual(button.mouse_clicked_color, "#0E6655")

        self.assertEqual((button.btn_width, button.btn_height), (350, 60))




