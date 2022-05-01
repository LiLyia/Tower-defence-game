import unittest
from castle import Castle
import tower
import imageCreator
import pygame
from obstacle import Obstacle
from gui_button import Button


SCREEN_HEIGHT, SCREEN_WIDTH = 650, 850
screen = pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
imager = imageCreator.ImageCreator.createImageCreator('Images')

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

    

