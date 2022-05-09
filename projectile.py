import pygame


DEFAULT_SCALE = 0.09
class Projectile:
    def __init__(self, x, y,target, damage):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/bullet.png')
        self.image = self.scaleImage(self.image , DEFAULT_SCALE)
        self.target = target
        self.damage = damage
        self.hitbox = pygame.Rect(self.x,self.y,40,40)
        self.status = False
        dest = (self.target.pos[0],self.target.pos[1])
        src = (self.x,self.y)
        self.rect = self.image.get_rect()
        self.path = self.calculatePoints(src,dest,5)
        self.path_x = 0

    def calculatePoints(self,src,dest,count):
        """
        Calculates the path for bullets.
        :return: array
        """
        points = []
        dX = dest[0]-src[0]
        dY =  dest[1]-src[1]
        interX = dX/ (count+1)
        interY = dY / (count +1)

        for i in range(count):
            points.append((src[0] + interX * i, src[1] + interY * i))
        return points

    def drawToTarget(self):
        """
        Draws bullets to the target.
        :return: None
        """
        if self.path_x >= len(self.path):

            dest = (self.target.pos[0]+ 20, self.target.pos[1]+20)
            src = (self.x, self.y)
            self.path = self.calculatePoints(src, dest, 2)
            self.path_x = 1

        self.x = self.path[self.path_x][0]
        self.y = self.path[self.path_x][1]

        self.path_x+= 1
        self.hitbox = pygame.Rect(self.x,self.y,40,40)


    def hitEnemy(self):
        """
        Reduces the enemy health by self damage.
        :return: None
        """
        if (self.target.health - self.damage) < 0:
            self.target.setHealth(0)
            self.status = False
        else:
            self.target.reduceHealth(self.damage)

    def drawBullets(self,screen):
        """
        Draws bullets.
        :return: None
        """
        screen.blit(self.image,(self.x,self.y))

    def scaleImage(self, img: pygame.Surface, scale: float = DEFAULT_SCALE) -> pygame.Surface:
        '''
        The function that scales tower image according to some scale
        :param img: pygame.Surface
        :param scale: float
        :return: pygame.Surface
        '''
        width = img.get_width()
        height = img.get_height()
        return pygame.transform.scale(img, (int(width * scale), int(height * scale)))
