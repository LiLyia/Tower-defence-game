import unittest
from castle import Castle
import tower
import imageCreator
import pygame
from obstacle import Obstacle
from gui_button import Button

##################################################################
SCREEN_HEIGHT, SCREEN_WIDTH = 650, 850
screen = pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
imager = imageCreator.ImageCreator.createImageCreator('Images')
game_map_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
            [1, 0, 2, 2, 0, 0, 0, 0, 0, 3, 2, 0, 1],
            [1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
##################################################################

class TESTGAME(unittest.TestCase):

    #Test Function for the Castle
    def test_castle(self):
        #####################
        castle1 =Castle(imager, (150, 100), screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(castle1.health,1200)
        self.assertEqual(castle1.player_number,0)
        #####################



        #####################
        actual_dead = castle1.isDead()
        expected_dead = False
        self.assertEqual(actual_dead,expected_dead)
        #####################



        #####################
        tempObj = Obstacle.createObstacle((450,300),screen,imager,50,image_number=0,health=200,max_health=200)
        actual_collide = castle1.collide(tempObj)
        expected_collide = False
        self.assertEqual(actual_collide,expected_collide)
        #####################


        #####################
        if castle1.pos[0] > 600 - 25 or castle1.pos[1] > 600 - 35 or castle1.pos[0] < 50 or castle1.pos[1] < 50:
            actual_pos = False
        else:
            actual_pos = True

        expected_pos = True
        self.assertEqual(actual_pos,expected_pos)
        #####################

        #####################
        actual_type = castle1.getType()
        expected_type = "Castle"
        self.assertEqual(actual_type,expected_type)
        #####################

    #Test for the BasicTower
    def test_tower(self):

        #####################
        tower_images = [[pygame.image.load('Images/Towers/tower1.png'),
                         pygame.image.load('Images/Towers/tower2.png'),
                         pygame.image.load('Images/Towers/tower3.png')]]
        tower1 = tower.Tower.createTower((200,100),tower_images,screen,[(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        self.assertEqual(tower1.health,600)
        self.assertEqual(tower1.price,100)
        self.assertEqual(tower1.healthLevel,0)
        self.assertEqual(tower1._max_up,3)
        #####################


        #####################
        actual_dead = tower1.isDead()
        expected_dead = False
        self.assertEqual(actual_dead,expected_dead)
        #####################

        #####################
        actual_upgrade = tower1.upgrade()
        expected_upgrade = True
        self.assertEqual(actual_upgrade,expected_upgrade)
        #####################

        #####################
        tempObj = Obstacle.createObstacle((450,300),screen,imager,50,image_number=0,health=200,max_health=200)
        actual_collide = tower1.collide(tempObj)
        expected_collide = False
        self.assertEqual(actual_collide,expected_collide)
        #####################

        #####################
        actual_type = tower1.getType()
        expected_type = "BasicTower"
        self.assertEqual(actual_type,expected_type)
        #####################

        #####################
        if tower1.pos[0] > 600 - 25 or tower1.pos[1] > 600 - 35 or tower1.pos[0] < 50 or tower1.pos[1] < 50:
            actual_pos = False
        else:
            actual_pos = True

        expected_pos = True
        self.assertEqual(actual_pos,expected_pos)
        #####################



    # Test for the Units
    def test_unit(self):

        #####################
        unit1 = unit.Unit((200,100),screen,game_map_data,[(0, 0, 0), (255, 0, 0), (0, 255, 0)])
        actual_stopped = unit1.isStopped
        expected_stopped = False
        self.assertEqual(actual_stopped,expected_stopped)

        actual_moveTarget = unit1.move_target
        expected_moveTarget = None
        self.assertEqual(actual_moveTarget,expected_moveTarget)

        #####################

        #####################
        unit_uvsu = unit.UvsU(unit1.pos,screen,game_map_data,unit1.color)
        self.assertEqual(unit_uvsu.health,500) ## 800 at first
        self.assertEqual(unit_uvsu.max_health, 500) ## 800 at first
        self.assertEqual(unit_uvsu.price, 100)
        self.assertEqual(unit_uvsu.attack_range, 50)
        self.assertEqual(unit_uvsu.cd , 150)

        actual_lastTarget = unit_uvsu.last_target
        expected_lastTarget = None
        self.assertEqual(actual_lastTarget,expected_lastTarget)

        actual_currentTarget = unit_uvsu.current_target
        expected_currenTarget = None
        self.assertEqual(actual_currentTarget,expected_currenTarget)

        #####################
        unit_uvso = unit.UvsO(unit1.pos,screen,game_map_data,unit1.color)
        self.assertEqual(unit_uvso.health, 400)  ## 500 at first
        self.assertEqual(unit_uvso.max_health, 400)  ## 500 at first
        self.assertEqual(unit_uvso.price, 100)
        self.assertEqual(unit_uvso.attack_range, 50)
        self.assertEqual(unit_uvso.cd, 150)
        ######################


        ######################
        unit_uvsb = unit.UvsB(unit1.pos,screen,game_map_data,unit1.color)
        self.assertEqual(unit_uvsb.health, 800)  ## 500 at first
        self.assertEqual(unit_uvsb.max_health, 800)  ## 500 at first
        self.assertEqual(unit_uvsb.price, 150) ##100 at first
        self.assertEqual(unit_uvsb.attack_range, 50)
        self.assertEqual(unit_uvsb.cd, 150)
        ######################
    

    

