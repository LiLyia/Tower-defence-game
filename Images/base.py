from unit import *

"""
 Base class is the connection point for all the classes that Player can create. 
"""


class Base:
    def __init__(self, pos, screen):
        self.pos = pos
        self.screen = screen

    def create(self, class_type):
        """
        This function can create every class a player can place.
        :param class_type: type of the class
        :return: related class type
        """
        match class_type:
            case 'Basic Unit':
                return Unit(self.pos, self.screen)
            case 'UvsU':
                return UvsU(self.pos, self.screen)
            case 'UvsB':
                return UvsB(self.pos, self.screen)
            case 'UvsO':
                return UvsB(self.pos, self.screen)
            case 'Basic Tower':
                ...
            case 'Fire Tower':
                ...
            case 'Strong Tower':
                ...
            case 'Obstacle':
                ...
            case 'Gold Mine':
                ...
