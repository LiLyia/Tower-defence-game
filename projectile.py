import pygame
class Projectile:
    def __init__(self, x, y,target, damage):
        self.x = x
        self.y = y
        self.target = target
        self.damage = damage
        self.hitbox = pygame.Rect(self.x,self.y,40,40)
        self.status = False
        dest = (self.target.pos[0],self.target.pos[1])
        src = (self.x,self.y)
        self.path = self.calculatePoints(src,dest,5)
        self.path_x = 0

    def calculatePoints(self,src,dest,count):
        points = []
        dX = dest[0]-src[0]
        dY =  dest[1]-src[1]
        interX = dX/ (count+1)
        interY = dY / (count +1)

        for i in range(count):
            points.append((src[0] + interX * i, src[1] + interY * i))
        return points

    def drawToTarget(self):
        if self.path_x >= len(self.path):

            dest = (self.target.pos[0]+3, self.target.pos[1]+8)
            src = (self.x, self.y)
            self.path = self.calculatePoints(src, dest, 2)
            self.path_x = 1

        self.x = self.path[self.path_x][0]
        self.y = self.path[self.path_x][1]

        self.path_x+= 1
        self.hitbox = pygame.Rect(self.x,self.y,40,40)

    def hitEnemy(self):
        if self.hitbox.colliderect(self.target.hitbox):
            if self.target.health - self.damage <0 :
                self.target.health = 0
                self.status = False
            else:
                self.target.health = self.target.health - self.damage
                self.status = True
        #print(self.target.health)
                
    def hitTower(self):
        if self.hitbox.colliderect(self.target.hitbox):
            if (self.target.health - self.damage) < 0:
                self.target.setHealth(0)
                self.status = False
            else:
                self.target.setHealth(self.target.health-self.damage)
        #print(self.target.health)
        
            
