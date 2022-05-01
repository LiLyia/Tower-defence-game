import unittest
from castle import Castle
import imageCreator
import pygame
from obstacle import Obstacle
class TESTGAME(unittest.TestCase):

    def test_castle(self):
        #####################
        SCREEN_HEIGHT, SCREEN_WIDTH = 650, 850
        screen = pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        imager = imageCreator.ImageCreator.createImageCreator('Images')
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
