import pygame
from pygame.locals import *
from castle import Castle
from game_map import GameMap
from tower import *
from unit import *
from FireTower import *
from imageCreator import *
from player import *
from ice_tower import *
import menu
import random


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

#--------------SideMenu--------------------
imager = ImageCreator.createImageCreator('Images')
sideMenu = menu.VerticalMenu(750, 120, pygame.transform.scale(pygame.image.load('Images/menu.png').convert_alpha(), (200, 650)))
sideMenu.add_btn(imager.getTowerImage(0, 0, 0), "Towers", 0)
sideMenu.add_btn(imager.getUnitImage(0, 0), "Units", 0)
sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/turns.png').convert_alpha(), (120, 50)), "Turn", 0)
sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)

# -------------castle-class-----------------------
# image of castle1 with 100% health
castle1_100_img = pygame.image.load('Images/Castle/castle1_100.png').convert_alpha()
# image of castle1 with 50% health
castle1_50_img = pygame.image.load('Images/Castle/castle1_50.png').convert_alpha()
# image of castle1 with 25% health
castle1_25_img = pygame.image.load('Images/Castle/castle1_25.png')
# image of castle2 with 100% health
castle2_100_img = pygame.image.load('Images/Castle/castle2_100.png').convert_alpha()
# image of castle2 with 50% health
castle2_50_img = pygame.image.load('Images/Castle/castle2_50.png').convert_alpha()
# image of castle2 with 25% health
castle2_25_img = pygame.image.load('Images/Castle/castle2_25.png')
# declearing tower positions
tower_pos = [(150, 150), (200, 200), (300, 300), (400, 400), (200, 500)]
position_tower = random.choice(tower_pos)
position_tower_2 = random.choice(tower_pos)
while position_tower_2 == position_tower:
    position_tower_2 = random.choice(tower_pos)

# creating towers
tower_images = [[pygame.image.load('Images/Towers/tower1.png'),pygame.image.load('Images/Towers/tower2.png'),pygame.image.load('Images/Towers/tower3.png')],[None,None,None],[None,None,None]]
fire_tower_images = [[pygame.image.load('Images/Towers/firetower.png'),pygame.image.load('Images/Towers/firetower.png'),pygame.image.load('Images/Towers/firetower.png')],[None,None,None],[None,None,None]]
ice_tower_images = [[pygame.image.load('Images/Towers/slowertower.png')],[None],[None]]


# randomly picking the position of castle 1 position
castle1_pos = [(150, 100), (200, 100), (250, 100), (300, 100), (350, 100), (400, 100), (450, 100)]
position_castle1 = random.choice(castle1_pos)
# randomly picking the position of castle 2 position
castle2_pos = [(150, 450), (200, 450), (250, 450), (300, 450), (350, 450), (400, 450), (450, 450)]
position_castle2 = random.choice(castle2_pos)
castle1 = Castle(imager, position_castle1, screen, 0, [(0, 0, 0), (255, 0, 0), (0, 255, 0)])
castle2 = Castle(imager, position_castle2, screen, 1, [(0, 0, 0), (0, 0, 255), (255, 0, 0)])


#soldier = Unit((100, 400),screen,'Images/soldier.png', 0.07 )
# ------------creating grid for game map --------------#
tile_size = 50
# def create_grid():
#     for line in range(13):
#         pygame.draw.line(screen, WHITE, (0, line*tile_size), (SCREEN_WIDTH, line* tile_size))
#         pygame.draw.line(screen,WHITE, (line*tile_size, 0),(line * tile_size,SCREEN_HEIGHT))

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
# for i in range(len(game_map_data)):
#     for j in range(len(game_map_data[0])):
#         if game_map_data[i][j] != 0:
#             obstacles.append((j*50, i*50))

#towers.append(tower_2)
is_game = True
moving_object = None
#Parameters: list of buildings. Draws bullets
def displayBullets(building_list):
    for b in building_list:
        if type(b) == FireTower:
            for p in b.bulletList:
                if p.target != None:
                    p.drawBullets(screen)
#Clear the bullets from the map.If bullets hits or miss the enemy , they will be deleted.
def clearBullets(towerList):
    for i in towerList:
        if type(i) == FireTower:
            for j in i.bulletList:
                if j.hitEnemy == True:
                    i.bulletList.remove(j)
                if i.current_target == None:
                    i.bulletList.remove(j)
#Parameters:unit list. Removes units and towers from the lists.
def clearObjects(unit_list, tower_list, obstacle_list):
    for e in unit_list:
        if e.health <= 0:
            unit_list.remove(e)
            e.remove()
    for t in tower_list:
        if t.health <= 0:
            tower_list.remove(t)
            t.remove()
    for g in obstacle_list:
        if g.health <= 0:
            obstacle_list.remove(g)
            g.remove()

#Get the target for each tower in the list of targetable units.
def findTargetforTowers(unit_list, tower_list):
    for b in tower_list:
        if type(b) == FireTower or type(b) == IceTower:
            b.targetList = []
            for m in unit_list:
                if b.hitbox.colliderect(m.hitbox) == True:
                    b.targetList.append(m)

# Get the target for each tower in the list of targetable units.
def currentTowerTarget(building_list):
    for b in building_list:
        if type(b) == FireTower or type(b) == IceTower:
            for m in b.targetList:
                if b.current_target == None:
                   b.current_target = m
                   if b.current_target.health < 0:
                        #print("Yes")
                        b.targetList.remove(m)
                if b.current_target.pos[0] <= m.pos[0]:
                    b.current_target = m

            if len(b.targetList) == 0:
               b.current_target = None

#If tower detects an enemy , this function will be activated and shoot to the enemies.
def shootTowers(towerList):
    for i in towerList:
        if type(i) == FireTower:
            if i.current_target != None:
                i.shoot()
        if type(i) == IceTower:
            if i.current_target != None and i.current_target.isStopped == False:
                i.current_target.setStopped(True)
            elif i.current_target != None and i.current_target.isStopped == True:
                i.current_target.setStopped(False)

#Parameters: unit list, tower list, obstacle list. Depending on the unit type, defines possible enemies for units, adding them to the target list.
def findMoveforUnits(safe, enemy, goldmines):
    obstacle_list = []

    for mine in goldmines:
        obstacle_list.append(mine)

    for obs in obstacles:
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

    """safe_units = safe.getUnits()
    enemy_units = enemy.getUnits()
    enemy_towers = enemy.getTowers()
    n = len(safe_units)
    for i in range(n):
        safe_units[i].moveList = []
        safe_units[i].move_target = None
        if type(safe_units[i]) == UvsU:
            for j in enemy_units:
                safe_units[i].moveList.append(j)
        elif type(safe_units[i]) == UvsB:
            for m in enemy_towers:
                safe_units[i].moveList.append(m)
        elif type(safe_units[i]) == UvsO:
            for m in obstacle_list:
                safe_units[i].moveList.append(m)
        closest = None
        closest_num = 999999
        x,y = safe_units[i].pos
    
        for k in safe_units[i].moveList:
            q,w = k.pos
            num = abs(x-q) + abs(y-w)
            if (num < closest_num):
                closest_num = num
                closest = k
        safe_units[i].move_target  = closest """


def findTargetforUnits(safe, enemy, obstacle_list):
    safe_units = safe.getUnits()
    enemy_units = enemy.getUnits()
    enemy_towers = enemy.getTowers()

    n = len(safe_units)
    for i in range(n):
        safe_units[i].targetList = []
        safe_units[i].current_target = None
        if type(safe_units[i]) == UvsU:
            for j in enemy_units:
                if safe_units[i].hitbox.colliderect(j.hitbox) == True:
                        safe_units[i].targetList.append(j)

        if type(safe_units[i]) == UvsB:
            for m in enemy_towers:
                if safe_units[i].hitbox.colliderect(m.hitbox) == True:
                    safe_units[i].targetList.append(m)

        if type(safe_units[i]) == UvsO:
            for m in obstacle_list:
                if safe_units[i].hitbox.colliderect(m.hitbox) == True:
                    safe_units[i].targetList.append(m)

        
#Parameters: unit list. Defines the target of the current turn, adds it to the current target list.             
def currentUnitTarget(unit_list):
    for u in unit_list:
        if type(u) == UvsU or type(u) == UvsB or type(u) == UvsO:
            for t in u.targetList:
                if u.current_target == None:
                    u.current_target = t
                    if u.current_target.health < 0:
                        u.targetList.remove(t)
                if u.current_target.pos[0] <= t.pos[0]:
                   u.current_target = t
            if len(u.targetList) == 0:
                u.current_target = None

#Parameters: unit list. Attacks the unit.         
def shootUnits(unit_list):
    for u in unit_list:
        if type(u) == UvsU or type(u) == UvsB or type(u) == UvsO:
            if u.current_target != None:
                u.attack(type(u))
                if u.current_target.health <0:
                    u.current_target = None

#Parameters: name of the button, screen. Creates a tower object and adds it to tower list.
def create_tower(name, x, y, screen):
    tower = None
    if turn == player1:
        color = player1.color
    else:
        color = player2.color
    if name == "BasicTower" and turn.checkCost("BasicTower") == True:
        tower = Tower.createTower((x, y), tower_images, screen, color)
    elif name == "FireTower" and turn.checkCost("FireTower") == True:
        tower = FireTower.createTower((x, y), fire_tower_images, screen, color)
    elif name == "SlowingTower" and turn.checkCost("SlowingTower") == True:
        print("Trying to create SlowingTower")
        tower = IceTower.createTower((x, y), ice_tower_images, screen, color)
    else:
        return None
    return tower

def upgrade_tower(turn):
    for t in turn.getTowers():
        if type(t) != FireTower and type(t) != IceTower:
            res = t.upgrade()
            print(t.maxHealth)
            if res == True:
                break

def add_tower(name, screen):
    global moving_object
    global obj
    x, y = pygame.mouse.get_pos()
    try:
        obj = create_tower(name, x, y, screen)
        if obj != None:
            moving_object = obj
            obj.moving = True
    except Exception as e:
        print(str(e) + " NOT VALID NAME")
def add_gold_mine(screen):
    global moving_object
    global obj
    x, y = pygame.mouse.get_pos()
    if turn == player1:
        color = player1.color
    else:
        color = player2.color
    try:
        if turn.checkCost("GoldMine") == True:
            obj = GoldMine((x, y), screen, color)
            moving_object = obj
            obj.moving = True
    except Exception as e:
        print(str(e) + " NOT VALID NAME")

def addGolds(goldmineList, player):
    for mine in goldmineList:
        mine.addGold(player)

#Parameters: player`s turn, returns player`s castle position.
def castlePos(turn):
    if turn == player1:
        return player1.getCastlePos()
    else:
        return player2.getCastlePos()

def targeting():

    findTargetforUnits(player1, player2, player2.goldmines_list)
    findTargetforUnits(player2, player1, player1.goldmines_list)
    findTargetforTowers(player1.getUnits(),player2.getTowers())
    findTargetforTowers(player2.getUnits(),player1.getTowers())
    currentUnitTarget(player1.getUnits())
    currentUnitTarget(player2.getUnits())
    currentTowerTarget(towers)

def turnSwitch(current_turn):
    if current_turn == player2:
        player1.gold += 200
        player2.gold += 200
        addGolds(player1.getGoldMines(), player1)
        addGolds(player2.getGoldMines(), player2)
    findMoveforUnits(player1, player2, player2.goldmines_list)
    findMoveforUnits(player2, player1, player1.goldmines_list)
    for unit in player1.getUnits():
        if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
            if (len(unit.targetList) > 0):
                unit.move(obstacles)
        else:
            unit.move(player2.castle_pos, obstacles)

    for unit in player2.getUnits():
        if type(unit) == UvsU or type(unit) == UvsB or type(unit) == UvsO:
            if (len(unit.targetList) > 0):
                unit.move(obstacles)
        else:
            unit.move(player1.castle_pos,obstacles)

    targeting()
    #Attack
    shootUnits(player1.getUnits())
    shootUnits(player2.getUnits())
    shootTowers(player1.getTowers())
    shootTowers(player2.getTowers())

    #Draw bullets
    displayBullets(towers)
    #Delete bullets and dead objects from the game
    clearBullets(towers)
    clearObjects(player1.getUnits(), player1.getTowers(), player1.getGoldMines())
    clearObjects(player2.getUnits(), player2.getTowers(), player2.getGoldMines())

   

#Vertical menu implementation, takes chosen button as a parameter, draws and clears the buttons.
def buttons(side_menu_button, player):
    if side_menu_button == "BackT":
        sideMenu.clear_btn("BasicTower")
        sideMenu.clear_btn("FireTower")
        sideMenu.clear_btn("SlowingTower")
        sideMenu.clear_btn("UpgradeTower")
        sideMenu.add_btn(imager.getTowerImage(0, 0, 0), "Towers", 0)
        sideMenu.add_btn(imager.getUnitImage(0, 0), "Units", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
        sideMenu.clear_btn("BackT")
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/turns.png').convert_alpha(), (120, 50)), "Turn", 0)

    elif side_menu_button == "BackG":
        sideMenu.clear_btn("GoldMine")
        sideMenu.clear_btn("BackG")
        sideMenu.add_btn(imager.getTowerImage(0, 0, 0), "Towers", 0)
        sideMenu.add_btn(imager.getUnitImage(0, 0), "Units", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/turns.png').convert_alpha(), (120, 50)), "Turn", 0)

    elif side_menu_button == "BackU":
        sideMenu.clear_btn("BasicUnit")
        sideMenu.clear_btn("vsObstacles")
        sideMenu.clear_btn("vsTowers")
        sideMenu.clear_btn("vsUnits")
        sideMenu.add_btn(imager.getTowerImage(0, 0, 0), "Towers", 0)
        sideMenu.add_btn(imager.getUnitImage(0, 0), "Units", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "Gold", 0)
        sideMenu.clear_btn("BackU")
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/turns.png').convert_alpha(), (120, 50)), "Turn", 0)

    elif side_menu_button == "Towers":
        sideMenu.clear_btn("Towers")
        sideMenu.clear_btn("Units")
        sideMenu.clear_btn("Gold")
        sideMenu.clear_btn("Turn")
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)), "BackT", 0)
        sideMenu.add_btn(imager.getTowerImage(0, 0, 0), "BasicTower", 500)
        sideMenu.add_btn(imager.getTowerImage(0, 1, 0), "FireTower", 600)
        sideMenu.add_btn(imager.getTowerImage(2, 2, 0), "SlowingTower", 800)
        sideMenu.add_btn(imager.getTowerImage(1, 1, 0), "UpgradeTower", 200)

    elif side_menu_button == "Units":
        sideMenu.clear_btn("Towers")
        sideMenu.clear_btn("Units")
        sideMenu.clear_btn("Gold")
        sideMenu.clear_btn("Turn")
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)), "BackU", 0)
        sideMenu.add_btn(imager.getUnitImage(0, 0), "BasicUnit", 500)
        sideMenu.add_btn(imager.getUnitImage(1, 0), "vsObstacles", 500)
        sideMenu.add_btn(imager.getUnitImage(3, 0), "vsTowers", 700)
        sideMenu.add_btn(imager.getUnitImage(2, 0), "vsUnits", 700)

    elif side_menu_button == "Gold":
        sideMenu.clear_btn("Towers")
        sideMenu.clear_btn("Units")
        sideMenu.clear_btn("Turn")
        sideMenu.clear_btn("Gold")
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/back.png').convert_alpha(), (50, 50)), "BackG", 0)
        sideMenu.add_btn(pygame.transform.scale(pygame.image.load('Images/Gold.png').convert_alpha(), (100, 80)), "GoldMine", 400)

    elif side_menu_button == "BasicTower" or side_menu_button == "FireTower" or side_menu_button == "SlowingTower":
        add_tower(side_menu_button, screen)

    elif side_menu_button == "UpgradeTower" and turn.checkCost("UpgradeTower") == True:
        upgrade_tower(player)

    elif side_menu_button == "GoldMine":
        add_gold_mine(screen)

    elif side_menu_button == "Turn":
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        if turn == player1:
            next_turn = "TURN OF Player 1"
        else:
            next_turn = "TURN OF Player 2"
        text_surface = my_font.render(next_turn, False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))  #It displays just for a moment.
        turnSwitch(turn)
        if (turn == player1):
            return player2
        else:
            return player1

    elif side_menu_button in ["BasicUnit", "vsObstacles", "vsTowers", "vsUnits"]:
        player.addUnit(side_menu_button)
towers = []
turn = player1
#Game cycle
while is_game:

    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))
    castle1.draw_castle()
    castle1.draw_health_bar()
    castle2.draw_castle()
    castle2.draw_health_bar()
    sideMenu.draw(screen)
    # create_grid()
    game_map.draw_tiles()
    pos = pygame.mouse.get_pos()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    next_turn = "Your amount of Gold: " + str(turn.gold)
    text_surface = my_font.render(next_turn, False, (0, 0, 0))
    if turn == player1:
        screen.blit(text_surface, (400, 0))
    else:
        screen.blit(text_surface, (0, 600))

    if moving_object:
        moving_object.move(pos[0], pos[1])
        collide = False
        for tower in player1.getTowers() + player2.getTowers():
            if tower.collide(moving_object):
                collide = True

    for event in pygame.event.get():
        if event.type == QUIT:
            is_game = False
        elif event.type == MOUSEBUTTONUP:
            if moving_object:
                not_allowed = False
                for tower in towers:
                    if tower.collide(moving_object):
                        not_allowed = True

                if not not_allowed:
                    if turn == player1:
                        if "tower" in moving_object.getType().lower():
                            player1.tower_list.append(moving_object)
                        else:
                            player1.getGoldMines().append(moving_object)
                    else:
                        if "tower" in moving_object.getType().lower():
                            player2.tower_list.append(moving_object)
                        else:
                            player2.getGoldMines().append(moving_object)

                    moving_object.moving = False
                    moving_object = None


        # draw images at positions
        if event.type == MOUSEBUTTONDOWN:
            side_menu_button = sideMenu.get_clicked(event.pos[0], event.pos[1])
            if turn == player1:
                rt = buttons(side_menu_button, player1)
            else:
                rt = buttons(side_menu_button, player2)
            if rt is not None:
                turn = rt
        #print(turn)

    #Find possible targets for units and towers
    units = player1.getUnits() + player2.getUnits()
    towers = player1.getTowers() + player2.getTowers()
    goldmines = player1.getGoldMines() + player2.getGoldMines()



    for tower in towers:
        tower.draw_tower()
        tower.draw_health_bar()

    for unit in units:
        unit.draw()
        unit.draw_health_bar()

    for mine in goldmines:
        mine.draw()
        mine.draw_health_bar()


    pygame.display.flip()
    pygame.display.update()
pygame.quit()
