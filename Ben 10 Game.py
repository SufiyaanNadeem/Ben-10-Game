"""
Main Game for File. This file is where all scripts are imported and main function is called.

Author: Sufiyaan Nadeem
"""

#Importing Pygame, Scripts,Time, etc.
import pygame
from pygame import *
from Scripts.Keyboard_Input import KeyInput_Handler
from Globals import*
from Scripts.Player_Sprites import *
from Scripts.Enemy_Sprites import *
from Scripts.GameObject_Sprites import *
from Scripts.Projectile_Sprites import *
from Scripts.UltraColor import *
from Scripts.GameObject_Sprites import*
from Scripts.Buttons import *
from time import sleep
from pygame import Rect
from random import randint,choice
from Scripts.GUI import *
import os

#Setting Window Height and Width
WIN_WIDTH = 1040
WIN_HEIGHT = 576
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

#Setting up Display Settings
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

#Initialize Pygame
pygame.init()


pygame.mixer.music.load("Music\\BGMusic.mp3")#Loading Background Music
pygame.mixer.music.play(-1) # -1 for infinite music

btnSound = pygame.mixer.Sound("Music\\Button_Sound.wav") #Loading Button Sound Effect. They have to be wav

#Loading Fonts
font_130pt = pygame.font.SysFont("Exo-ExtraBold", 130)
font_30pt = pygame.font.SysFont("Exo", 30)
font_15pt = pygame.font.SysFont("Exo", 15)

#Coordinates for Stats of Player
stats_coordinates=(5,WIN_HEIGHT-200)

#Initializing all sprite groups Globally
entities = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
bossgroup=pygame.sprite.Group()
powerupgroup=pygame.sprite.Group()
projectilegroup=pygame.sprite.Group()

#Restart Function is not in Button Class because main() needs to be called
def Restart():
    Globals.scene = "Game"
    Globals.current_level = 1
    Globals.player_health = 100
    Globals.boss_health = 100
    main()
# Restart Button
btnRestart = Menu.Button(text="Restart", rect=(0, 0, 160, 60),
                         bg=UltraColor.Gray, fg=UltraColor.White, bgr=UltraColor.Green, tag=("GameOver", None))
btnRestart.Left = WIN_WIDTH - 600
btnRestart.Top = WIN_HEIGHT - 300 + 30
btnRestart.Command = Restart

#Main Function that runs game
def main():

    #Emptying Sprite Lists so that when game is Restarted, all previous sprites are deleted
    entities.empty()
    enemygroup.empty()
    powerupgroup.empty()
    projectilegroup.empty()
    bossgroup.empty()

    #Setting Game Window to the Middle of the Screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)
    
    #Initializing Screen, Window Icon, Timer, etc.
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Ben 10")
    icon=pygame.image.load("Graphics\\Game_Icon.png")
    pygame.display.set_icon(icon)
    timer = pygame.time.Clock()

    #Creating Platforms list that will be 
    platforms = []
    x = y = 0

    #Setting Current Level and Adding Enemies to Groups, Powerups to Powerup group, Hearts to Powerup groups
    if Globals.current_level==1:
        player = Player(64*2, 64*1)
        enemygroup.add(Megawatt(64*30, 64*5))
        powerupgroup.add(PowerUp(64*10, 64*5.5))
        powerupgroup.add(Instructions(64*1.5,64*3))
        powerupgroup.add(GoldKey(64*6, 64*4))  
        powerupgroup.add(GoldKey(64*20, 64*2)) 
        powerupgroup.add(GoldKey(64*35, 64*4))    
        level = [
            "L                                         l",
            "L                                         l",
            "L                                         l",
            "L                                         l",
            "L                                         l",
            "L                                      E  l",
            "L                                         l",
            "L                                         l",
            "PPPPCAAAADPPPPPPPPPPPPPPPPPPCAAAADPPPPPPPPP", 
            "ppppcaaaadppppppppppppppppppcaaaadppppppppp"]
    elif Globals.current_level==2:
        player = Player(64*2, 64*7)
        powerupgroup.add(Heart(64*12.5, 64*7)) 

        enemygroup.add(Megawatt(64*25, 64*9.25))
        enemygroup.add(Megawatt(64*26, 64*9.25))
        enemygroup.add(Megawatt(64*27, 64*9.25))
        enemygroup.add(Megawatt(64*25, 64*19))
        enemygroup.add(Megawatt(64*26, 64*19))
        enemygroup.add(Megawatt(64*27, 64*19))
        powerupgroup.add(GoldKey(64*31, 64*17.5))
        powerupgroup.add(GoldKey(64*4, 64*4.5))     
        powerupgroup.add(GoldKey(64*25, 64*10.5))  
        powerupgroup.add(PowerUp(64*40, 64*14))

        level = [
            "L                                            l",
            "L                                            l",
            "L                                            l",
            "L                                            l",
            "L                                  E         l",
            "L                                            l",
            "L  ghj                                       l",
            "L                               ghhhhhj      l",
            "L                                            l",
            "L          ghhj                              l",
            "L                                            l",
            "L                   gh       hj              l",
            "L                     hhhhhhh                l",
            "L                                            l",
            "PPPP                                         l",
            "pppp        ghhj                             l",
            "pppp                                  ghhj   l",
            "pppp ghj                                     l",
            "pppp                                         l",
            "pppp                          ghj            l",
            "ppppPPPPPPPPPPPPPPPCAAAAAAAAAAAAAAAAAAAADPPPPP", 
            "pppppppppppppppppppcaaaaaaaaaaaaaaaaaaaadppppp"]   
    elif Globals.current_level==3:        
        bossgroup.add(Wolf(64*20, 64*5))
        player = Player(64*2, 64*7)
        powerupgroup.add(PowerUp(64*choice(range(1,25)), 64*choice(range(1,3))))
        powerupgroup.add(PowerUp(64*choice(range(1,30)), 64*3))
        powerupgroup.add(PowerUp(64*choice(range(1,30)), 64*choice(range(8,10))))
        powerupgroup.add(Heart(64*choice(range(1,28)), 64*choice(range(2,10)))) 
        level = [
            "L                              E    l",
            "L                                   l",
            "L                                   l",
            "L                         ghhhhhj   l",
            "L                                   l",
            "L       ghhhhj                      l",
            "L                                   l",
            "L                         ghhj      l",
            "L                                   l",
            "L                                   l",
            "L                                   l",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", 
            "ppppppppppppppppppppppppppppppppppppp"]        
    
    # Building the level by checking where each tile is in the list
    for row in level:
        for col in row:
            if col == "P" or col == "E" or col == "p" or col=="C"or col=="A" or col=="D"  or col=="L"  or col=="l" or col=="c"or col=="a" or col=="d"or col=="g"or col=="h" or col=="j":
                p = Platform(x, y,col)
                platforms.append(p)
                entities.add(p)
            x += 64
        y += 64
        x = 0

    #Setting window height and width using Level list that is sent to Camera Class
    total_level_width = len(level[0]) * 64
    total_level_height = len(level) * 64
    camera = Camera(complex_camera, total_level_width, total_level_height)

    #Adding Player to entities class
    entities.add(player)
    Globals.keys=0

    #Main Game loop
    while Globals.isRunning:
        timer.tick(60)#Limiting FPS to 60

        #Processing Keyboard and Button Inputs
        for e in pygame.event.get():
            if e.type == QUIT:
                Globals.isRunning = False
            KeyInput_Handler(e)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1: 
                    for btn in Menu.Button.All:
                        if btn.Tag[0] == Globals.scene and btn.Rolling:
                            if btn.Command != None:
                                btn.Command() 
                            btnSound.play()
                            btn.Rolling == False
                            break  
        
        #Depending on the Current Scene, Display different things
        if Globals.scene=="Menu":
            Globals.menu_counter+=1
            screen.blit(GameObject_Sprites.Home_Screen_img,(0,0))
            for btn in Menu.Button.All:
                if btn.Tag[0] == "Menu":
                    btn.Render(screen)
            pygame.display.update()
        elif Globals.scene=="Pause":
            pygame.mixer.music.pause()
            for btn in Menu.Button.All:
                if btn.Tag[0] == "Pause":
                    btn.Render(screen)
           
            Globals.pause_counter+=1
            pygame.display.update()
        elif Globals.scene=="GameOver":
            pygame.mixer.music.pause()
            if Globals.boss_health<=0:
                End_Top_Message=font_130pt.render("Amazing!", 1, UltraColor.Black)
                End_Message=font_30pt.render("You Beat the Game!", 1, UltraColor.Black)
            else:
                End_Top_Message=font_130pt.render("Nice Try!", 1, UltraColor.Black)
                End_Message=font_30pt.render("You Reached Level "+str(Globals.current_level), 1, UltraColor.Black)
            screen.blit(GameObject_Sprites.Game_Over_img,(0,0))
            for btn in Menu.Button.All:
                if btn.Tag[0] == "GameOver":
                    btn.Render(screen)
            screen.blit(End_Top_Message, (365,100))
            screen.blit(End_Message, (480,250))
            pygame.display.update()
        elif Globals.scene=="Game":
            
            #Changing background depending on the Scene
            if Globals.current_level==1:
                screen.blit(GameObject_Sprites.Background_1,(0,0))
            elif Globals.current_level==2:
                screen.blit(GameObject_Sprites.Background_2,(0,0))
            elif Globals.current_level==3:
                screen.blit(GameObject_Sprites.Background_3,(0,0))
            
            pygame.mixer.music.unpause()
            
            camera.update(player)

            #Blitting Sprites from different Groups
            for e in powerupgroup:
                screen.blit(e.image,camera.apply(e))
                e.update(platforms,entities)

            # update player, draw everything else
            player.update(Globals.up, Globals.down, Globals.left,
                        Globals.right, Globals.attack,Globals.isRunning, platforms, powerupgroup,enemygroup,bossgroup)

            for e in entities:
                screen.blit(e.image, camera.apply(e))

            for e in enemygroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, entities)

            for e in bossgroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, powerupgroup,enemygroup,entities)

            for e in projectilegroup:
                screen.blit(e.image,camera.apply(e))
                e.update(platforms,entities)

            for btn in Menu.Button.All:
                if btn.Tag[0] == "Game":
                    btn.Render(screen)

            #Drawing Player Health Bar
            pygame.draw.rect(screen,UltraColor.Green,(10,10,Globals.player_health*1.5,30))

            #Blitting Enemy Health Bar if on level 3
            if Globals.current_level==3:
                pygame.draw.rect(screen,(97,97,97),(1030-Globals.boss_health*1.5,10,Globals.boss_health*1.5,30))  
            
            #Displaying Keys depending on how many keys have been collected
            if Globals.keys>=1:
                screen.blit(GameObject_Sprites.Door_Key,(5,35))  
            if Globals.keys>=2:
                screen.blit(GameObject_Sprites.Door_Key,(70,35))     
            if Globals.keys>=3:
                screen.blit(GameObject_Sprites.Door_Key,(135,35))  
            
            #Blitting Watch that hold timer
            screen.blit(GameObject_Sprites.Watch_5,(480,2))
            
            #Setting Timer Text Variable and Blitting it
            time = font_30pt.render(str(round(Globals.timer)), 1, UltraColor.Black)
            text_coordinates = time.get_rect(center=(WIN_WIDTH/2+0.9, 42))
            screen.blit(time, text_coordinates)
            
            #If timer is more than 6s, then blit Alien's stats
            if Globals.timer>=6:
                if Globals.selected_alien==0:
                    screen.blit(GameObject_Sprites.Wildmutt_Stats,stats_coordinates)
                elif Globals.selected_alien==1:
                    screen.blit(GameObject_Sprites.Fourarms_Stats,stats_coordinates)
                elif Globals.selected_alien==2:
                    screen.blit(GameObject_Sprites.Heatblast_Stats,stats_coordinates)
                elif Globals.selected_alien==3:
                    screen.blit(GameObject_Sprites.XLR8_Stats,stats_coordinates)
                elif Globals.selected_alien==4:
                    screen.blit(GameObject_Sprites.Ghostfreak_Stats,stats_coordinates)
                elif Globals.selected_alien==5:
                    screen.blit(GameObject_Sprites.Ripjaws_Stats,stats_coordinates)
                elif Globals.selected_alien==6:
                    screen.blit(GameObject_Sprites.Stinkfly_Stats,stats_coordinates)
                elif Globals.selected_alien==7:
                    screen.blit(GameObject_Sprites.Greymatter_Stats,stats_coordinates)
                elif Globals.selected_alien==8:
                    screen.blit(GameObject_Sprites.Diamondhead_Stats,stats_coordinates)
                elif Globals.selected_alien==9:
                    screen.blit(GameObject_Sprites.Upgrade_Stats,stats_coordinates)

            #Setting Game Scene to Game Over when player dies or boss dies
            if Globals.player_health<=0 and not player.alive() or Globals.boss_health<=-20 :
                Globals.scene="GameOver"

            pygame.display.update()

"""
Below is a Camera Class that targets the Player.  
The Camera Class and Complex Camera function were borrowed from Anthony Biron(https://www.youtube.com/watch?v=FpufbRZxKRM).
This complex camera function follows my player until he hits the edge of the map
"""
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
#Complex Camera That follows the Player
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    # stop scrolling at the right edge
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

#Entity Class that helps with collisions etc
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

#Player Class that handles collisions, animations, transformations, etc
class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = True

        self.x=x
        self.y=y

        self.onGround = False
        self.airborne = True
        self.counter_walk = 0
        self.counter_idle=0
        self.counter_walk = 0
        self.counter_jump = 0
        self.counter_attack=0
        self.counter_attackR=0
        self.first_roll=True
        self.counter_transform=0
        self.counter_dead=0
        self.destroyed=False

        self.fade=True
        self.image = Player_Sprites.Ben_Idle1
        # self.image = pygame.image.load(
        #"Graphics/Ben_SpriteSheet.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (22 * 3, 60 * 3))
        self.rect = Rect(x, y, 22 * 2, 60 * 2)

        self.alien_transform=False
        self.transformed=False
        self.attack=False
        self.health=Globals.player_health
    def update(self, up, down, left, right, attack, running, platforms, powerupgroup,enemygroup,bossgroup):

        if not self.destroyed:
            if Globals.selected_alien!=11:
                self.transformed=True
            if self.transformed:
                Globals.timer-=0.01
            
            if Globals.timer<=0:
                Globals.timer=0
                Globals.selected_alien=11
            if up:

                if Globals.selected_alien==6:
                        self.yvel=-8
                                        
                # only jump if on the ground
                
                elif self.onGround:
                    if Globals.selected_alien==2:
                        self.yvel -= 15
                    elif Globals.selected_alien==7:
                        self.yvel -=18
                    else:
                        if not Globals.selected_alien==9:
                            self.yvel -= 12
            if down:
                pass

            if left:
                if Globals.selected_alien==0:
                    self.xvel = -10
                elif Globals.selected_alien==1  or Globals.selected_alien==4 or Globals.selected_alien==8 or Globals.selected_alien==9:
                    self.xvel = -6
                elif Globals.selected_alien==3:
                    if self.attack:
                        self.xvel=-20
                    else:
                        self.xvel=-10
                else:
                    self.xvel = -8
                
                self.faceright = False
            if right:
                if Globals.selected_alien==0:
                    self.xvel = 10
                elif Globals.selected_alien==1 or Globals.selected_alien==4 or Globals.selected_alien==8 or Globals.selected_alien==9:
                    self.xvel = 6
                elif Globals.selected_alien==3:
                    if self.attack:
                        self.xvel=20
                    else:
                        self.xvel=10
                else:
                    self.xvel = 8

                self.faceright = True
            if not self.onGround:
                self.yvel += 0.3
                # max falling speed
                if self.yvel > 100:
                    self.yvel = 100
            if not(left or right):
                self.xvel = 0

            if self.yvel < 0 or self.yvel > 1.2:
                self.airborne = True
            
            if not self.airborne or self.onGround:
                self.attack=attack

            # increment in x direction
            self.rect.left += self.xvel
            # do x-axis collisions
            self.collide(self.xvel, 0, platforms, powerupgroup,enemygroup,bossgroup,up,down,left,right)
            # increment in y direction
            self.rect.top += self.yvel
            # assuming we're in the air
            self.onGround = False

            if self.health<=0:
                self.destroyed=True

            # do y-axis collisions
            self.collide(0, self.yvel, platforms, powerupgroup,enemygroup,bossgroup,up,down,left,right)
        if self.fade==False:
            for p in platforms:
                if p.tile=="E":
                    p.change_loop()        
        # self.updatecharacter(Player_Sprites.Ben_Walk1)
        self.animate()

        #Globals.selected_alien=1
        #print(Globals.selected_alien)
    def collide(self, xvel, yvel, platforms, powerupgroup,enemygroup,bossgroup,up,down,left,right):
        for p in platforms:
            

            if pygame.sprite.collide_rect(self, p):
              #  if isinstance(p, ExitBlock):
               #     pygame.event.post(pygame.event.Event(QUIT))
                if p.tile=="E" and (Globals.keys>=3 or Globals.boss_health<=0):
                    p.change_loop()
                    self.fade=False
                    self.destroyed=True
                    self.rect.midbottom=p.rect.midbottom           
                else:
                    if xvel==0 and yvel==0 and self.faceright:
                        self.rect.right=p.rect.left
                    if xvel > 0:
                        self.rect.right = p.rect.left
                    if xvel < 0:
                        self.rect.left = p.rect.right
                    if yvel > 0:
                        if p.tile=="A" and Globals.selected_alien!=5:
                            self.health-=10
                            Globals.player_health=self.health
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.counter_jump=0
                        self.airborne = False
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
            else:
                if p.tile=="E" and (Globals.keys>=3 or Globals.boss_health<=0):
                    p.door_ready()

        for enemy in enemygroup:
            if pygame.sprite.collide_rect(self, enemy):
                diffy = self.rect.bottom - enemy.rect.top
                diffx1 = enemy.rect.left - self.rect.right
                diffx2 = enemy.rect.right - self.rect.left
                if diffy <= 9:
                    self.yvel = -8
                elif (self.attack or self.counter_attack!=0) and self.faceright and diffx1<=10 or self.attack and  not self.faceright and diffx2<=10:
                    pass 
                else:
                    if self.health!=0:
                        self.health-=0.20
                        Globals.player_health=self.health
                    else:
                        self.health=0
                        Globals.player_health=self.health
                        self.destroyed=True

        for enemy in bossgroup:
            if pygame.sprite.collide_rect(self, enemy):
                diffy = self.rect.bottom - enemy.rect.top
                diffx1 = enemy.rect.left - self.rect.right
                diffx2 = enemy.rect.right - self.rect.left
                if diffy <= 9:
                    self.yvel = -8
                elif (self.attack or self.counter_attack!=0) and self.faceright and diffx1<=10 or self.attack and  not self.faceright and diffx2<=10:
                    pass 
                else:
                    if self.health>0:
                        self.health-=0.24
                        Globals.player_health=self.health
                    else:
                        self.health=0
                        Globals.player_health=self.health
                        self.destroyed=True


        for powerup in powerupgroup:
            if pygame.sprite.collide_rect(self, powerup):
                if hasattr(powerup,"name"):
                    self.alien_transform=True

              #      if self.counter_transform==0:
               #         self.move=False
    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf
    def animate(self):
        
        if not self.destroyed:
            if self.xvel > 0 or self.xvel < 0:
                self.counter_idle=0
                # self.updatecharacter(Player_Sprites.Ben_Walk1)
                if self.alien_transform  or self.counter_transform!=0:
                    self.transformloop()
                    self.first_roll=True
                elif self.attack or self.counter_attackR!=0:
                    self.attackloop()
                    self.counter_walk=0
                elif self.airborne:
                    self.move=True
                    self.jumploop()
                    self.counter_walk=0
                else:
                    self.first_roll=True
                    self.counter_attack=0
                    self.walkloop()
            else:
                self.counter_attackR=0
                if self.alien_transform or self.counter_transform!=0:
                    self.transformloop()
                elif self.attack or self.counter_attack!=0:
                    self.attackloop()
                    self.counter_walk=0
                elif self.airborne:
                    self.jumploop()
                    self.counter_walk=0
                else:
                    self.attack=False
                    self.idleloop()
        else:
            self.destroyloop()  
    def idleloop(self):
        if Globals.selected_alien==0:
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Wildmutt_Idle1)
                self.rect.size=(49*3,38*3)
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.Wildmutt_Idle2)
                self.rect.size=(49*3,38*3)
            elif self.counter_idle==20:
                self.counter_idle=0
        elif Globals.selected_alien==1:
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Fourarms_Idle1)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.Fourarms_Idle2)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_idle==20:
                self.updatecharacter(Player_Sprites.Fourarms_Idle3)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_idle==30:
                self.updatecharacter(Player_Sprites.Fourarms_Idle4)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_idle==40:
                self.counter_idle=0
        elif Globals.selected_alien == 2: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Heatblast_Idle1)
                self.rect.size=(30*3,44*3)
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.Heatblast_Idle2)
                self.rect.size=(31*3,44*3)
            elif self.counter_idle==20:
                self.updatecharacter(Player_Sprites.Heatblast_Idle3)
                self.rect.size=(30*3,44*3)
            elif self.counter_idle==30:
                self.updatecharacter(Player_Sprites.Heatblast_Idle4)
                self.rect.size=(30*3,44*3)     
            elif self.counter_idle==40:
                self.counter_idle=0 
        elif Globals.selected_alien == 3: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.XLR8_Idle1)
                self.rect.size=(45*3,42*3)
            elif self.counter_idle==5:
                self.updatecharacter(Player_Sprites.XLR8_Idle2)
                self.rect.size=(45*3,42*3)
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.XLR8_Idle3)
                self.rect.size=(45*3,42*3)
            elif self.counter_idle==15:
                self.updatecharacter(Player_Sprites.XLR8_Idle4)
                self.rect.size=(45*3,42*3)
            elif self.counter_idle==20:
                self.counter_idle=0
        elif Globals.selected_alien == 4: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Ghostfreak_Idle1)
                self.rect.size=(39*2,83*2)
            elif self.counter_idle==5:
                self.updatecharacter(Player_Sprites.Ghostfreak_Idle2)
                self.rect.size=(41*2,83*2)
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.Ghostfreak_Idle3)
                self.rect.size=(44*2,83*2)
            elif self.counter_idle==15:
                self.updatecharacter(Player_Sprites.Ghostfreak_Idle4)
                self.rect.size=(49*2,83*2)
            elif self.counter_idle==20:
                self.updatecharacter(Player_Sprites.Ghostfreak_Idle5)
                self.rect.size=(42*2,83*2)		
            elif self.counter_idle==25:
                self.counter_idle=0
        elif Globals.selected_alien == 5: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle1)
                self.rect.size=(int(52*2.5),int(63*2.5))
            elif self.counter_idle==5:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle2)
                self.rect.size=(int(50*2.5),int(63*2.5))
            elif self.counter_idle==10:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle3)
                self.rect.size=(int(52*2.5),int(63*2.5))
            elif self.counter_idle==15:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle4)
                self.rect.size=(int(53*2.5),int(63*2.5))
            elif self.counter_idle==20:
                self.counter_idle=0
        elif Globals.selected_alien == 6: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Stinkly_Idle1)
                self.rect.size=(78*2,112*2)
            elif self.counter_idle==5:
                self.counter_idle=0
        elif Globals.selected_alien == 7: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Greymatter_Idle)
                self.rect.size=(int(38/2),int(64/2))
            elif self.counter_idle==5:
                self.counter_idle=0
        elif Globals.selected_alien == 8: 
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle1)
                self.rect.size=(39*3,74*3)
            elif self.counter_idle==7:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle2)
                self.rect.size=(41*3,74*3)
            elif self.counter_idle==14:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle3)
                self.rect.size=(39*3,74*3)
            elif self.counter_idle==21:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle4)
                self.rect.size=(38*3,74*3)
            elif self.counter_idle==28:
                self.counter_idle=0
        elif Globals.selected_alien==9:
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Upgrade_Idle)
                self.rect.size=(67*2,97*2)
            elif self.counter_idle==5:
                self.counter_idle=0
        else:
            if self.counter_idle==1:
                self.updatecharacter(Player_Sprites.Ben_Idle1)
                self.rect.size=(28 * 3, 48 * 3)
            elif self.counter_idle==7:
                self.updatecharacter(Player_Sprites.Ben_Idle2)
                self.rect.size=(28 * 3, 48 * 3)
            elif self.counter_idle==14:
                self.updatecharacter(Player_Sprites.Ben_Idle3)
                self.rect.size=(29 * 3, 48 * 3)
            elif self.counter_idle==21:
                self.updatecharacter(Player_Sprites.Ben_Idle4)
                self.rect.size=(29 * 3, 48 * 3)
            elif self.counter_idle==28:
                self.counter_idle=0
        self.counter_idle += 1
    def walkloop(self):
        if Globals.selected_alien==0:
            if self.counter_walk == 1:
                self.updatecharacter(Player_Sprites.Wildmutt_Walk1)
                self.rect.size=(48*3,38*3)
            elif self.counter_walk == 5:
                self.updatecharacter(Player_Sprites.Wildmutt_Walk2)
                self.rect.size=(56*3,38*3)
            elif self.counter_walk == 10:
                self.updatecharacter(Player_Sprites.Wildmutt_Walk3)
                self.rect.size=(65*3,38*3)
            elif self.counter_walk == 15:
                self.updatecharacter(Player_Sprites.Wildmutt_Walk4)
                self.rect.size=(62*3,38*3)
            elif self.counter_walk == 20:
                self.updatecharacter(Player_Sprites.Wildmutt_Walk5)
                self.rect.size=(48*3,38*3)
            elif self.counter_walk==25:
                self.counter_walk = 0     
        elif Globals.selected_alien==1:
            if self.counter_walk == 1:
                self.airborne=False
                self.updatecharacter(Player_Sprites.Fourarms_Walk1)
                self.rect.size=(43*3,54*3)
            elif self.counter_walk == 8:
                self.updatecharacter(Player_Sprites.Fourarms_Walk2)
                self.rect.size=(52 * 3, 54 * 3)
            elif self.counter_walk == 16:
                self.updatecharacter(Player_Sprites.Fourarms_Walk3)
                self.rect.size=(35 * 3, 54 * 3)
            elif self.counter_walk == 24:
                self.updatecharacter(Player_Sprites.Fourarms_Walk4)
                self.rect.size=(41 * 3, 54 * 3)
            elif self.counter_walk == 32:
                self.updatecharacter(Player_Sprites.Fourarms_Walk5)
                self.rect.size=(51 * 3, 54 * 3)
            elif self.counter_walk == 40:
                self.updatecharacter(Player_Sprites.Fourarms_Walk6)
                self.rect.size=(35 * 3, 54 * 3)
            elif self.counter_walk==48:
                self.counter_walk = 0
        elif Globals.selected_alien == 2: 
            if self.counter_walk == 1:
                self.updatecharacter(Player_Sprites.Heatblast_Walk1)
                self.rect.size=(34*3,44*3)
            elif self.counter_walk == 9:
                self.updatecharacter(Player_Sprites.Heatblast_Walk2)
                self.rect.size=(40*3,44*3)
            elif self.counter_walk == 18:
                self.updatecharacter(Player_Sprites.Heatblast_Walk3)
                self.rect.size=(23*3,44*3)
            elif self.counter_walk == 27:
                self.updatecharacter(Player_Sprites.Heatblast_Walk4)
                self.rect.size=(33*3,44*3)
            elif self.counter_walk == 36:
                self.updatecharacter(Player_Sprites.Heatblast_Walk5)
                self.rect.size=(40*3,44*3)
            elif self.counter_walk == 45:
                self.updatecharacter(Player_Sprites.Heatblast_Walk6)
                self.rect.size=(23*3,44*3)
            elif self.counter_walk==54:
                self.counter_walk = 0
        elif Globals.selected_alien == 3: 

            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.XLR8_Walk1)
                self.rect.size=(52*3,42*3)
            elif self.counter_walk == 5:
                self.updatecharacter(Player_Sprites.XLR8_Walk2)
                self.rect.size=(52*3,42*3)
            elif self.counter_walk==10:
                self.updatecharacter(Player_Sprites.XLR8_Walk3)
                self.rect.size=(52*3,42*3)
            elif self.counter_walk==15:
                self.updatecharacter(Player_Sprites.XLR8_Walk4)
                self.rect.size=(52*3,42*3)
            elif self.counter_walk==20:
                self.counter_walk=0
        elif Globals.selected_alien == 4: 
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Ghostfreak_Walk1)
                self.rect.size=(51*2,83*2)
            elif self.counter_walk==5:
                self.updatecharacter(Player_Sprites.Ghostfreak_Walk2)
                self.rect.size=(51*2,83*2)
            elif self.counter_walk==10:
                self.updatecharacter(Player_Sprites.Ghostfreak_Walk3)
                self.rect.size=(55*2,83*2)
            elif self.counter_walk==15:
                self.updatecharacter(Player_Sprites.Ghostfreak_Walk4)
                self.rect.size=(60*2,83*2)
            elif self.counter_walk==20:
                self.updatecharacter(Player_Sprites.Ghostfreak_Walk5)
                self.rect.size=(53*2,83*2)
            elif self.counter_walk==25:
                self.counter_walk=0
        elif Globals.selected_alien == 5: 
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk1)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==5:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk2)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==10:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk3)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==15:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk4)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==20:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk5)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==25:
                self.updatecharacter(Player_Sprites.Ripjaws_Walk6)
                self.rect.size=(int(66*2.5),int(63*2.5))
            elif self.counter_walk==30:
                self.counter_walk=0
        elif Globals.selected_alien==6:
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Stinkly_Walk1)
                self.rect.size=(86*2,112*2)
            elif self.counter_walk==5:
                self.updatecharacter(Player_Sprites.Stinkfly_Walk2)
                self.rect.size=(94*2,112*2)
            elif self.counter_walk==9:
                self.updatecharacter(Player_Sprites.Stinkfly_Walk3)
                self.rect.size=(74*2,112*2)
            elif self.counter_walk==14:
                self.counter_walk=0
        elif Globals.selected_alien == 7: 
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Greymatter_Walk1)
                self.rect.size=(int(73/2),int(64/2))
            elif self.counter_walk==5:
                self.updatecharacter(Player_Sprites.Greymatter_Walk2)
                self.rect.size=(int(39/2),int(64/2))
            elif self.counter_walk==10:
                self.updatecharacter(Player_Sprites.Greymatter_Walk3)
                self.rect.size=(int(71/2),int(64/2))
            elif self.counter_walk==15:
                self.updatecharacter(Player_Sprites.Greymatter_Walk4)
                self.rect.size=(int(36/2),int(64/2))
            elif self.counter_walk==20:
                self.counter_walk=0
        elif Globals.selected_alien == 8: 
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk1)
                self.rect.size=(52*3,74*3)
            elif self.counter_walk==8:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk2)
                self.rect.size=(55*3,74*3)
            elif self.counter_walk==16:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk3)
                self.rect.size=(33*3,74*3)
            elif self.counter_walk==24:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk4)
                self.rect.size=(50*3,74*3)
            elif self.counter_walk==32:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk5)
                self.rect.size=(57*3,74*3)
            elif self.counter_walk==40:
                self.updatecharacter(Player_Sprites.Diamondhead_Walk6)
                self.rect.size=(33*3,74*3)
            elif self.counter_walk==48:
                self.counter_walk=0
        elif Globals.selected_alien == 9: 
            if self.counter_walk==1:
                self.updatecharacter(Player_Sprites.Upgrade_Walk1)
                self.rect.size=(62*2,97*2)
            elif self.counter_walk==8:
                self.updatecharacter(Player_Sprites.Upgrade_Walk2)
                self.rect.size=(29*2,97*2)
            elif self.counter_walk==16:
                self.updatecharacter(Player_Sprites.Upgrade_Walk3)
                self.rect.size=(54*2,97*2)
            elif self.counter_walk==24:
                self.updatecharacter(Player_Sprites.Upgrade_Walk4)
                self.rect.size=(30*2,97*2)
            elif self.counter_walk==32:
                self.counter_walk=0
        else:
            if self.counter_walk == 1:
                self.updatecharacter(Player_Sprites.Ben_Walk1)
                self.rect.size=(31 * 3, 48 * 3)
            elif self.counter_walk == 5:
                self.updatecharacter(Player_Sprites.Ben_Walk2)
                self.rect.size=(41 * 3, 48 * 3)
            elif self.counter_walk == 10:
                self.updatecharacter(Player_Sprites.Ben_Walk3)
                self.rect.size=(40 * 3, 48 * 3)
            elif self.counter_walk == 15:
                self.updatecharacter(Player_Sprites.Ben_Walk4)
                self.rect.size=(32 * 3, 48 * 3)
            elif self.counter_walk == 20:
                self.updatecharacter(Player_Sprites.Ben_Walk5)
                self.rect.size=(33 * 3, 48 * 3)
            elif self.counter_walk == 25:
                self.updatecharacter(Player_Sprites.Ben_Walk6)
                self.rect.size=(39 * 3, 48 * 3)
            elif self.counter_walk == 30:
                self.updatecharacter(Player_Sprites.Ben_Walk7)
                self.rect.size=(38 * 3, 48 * 3)
            elif self.counter_walk == 35:
                self.updatecharacter(Player_Sprites.Ben_Walk8)
                self.rect.size=(30 * 3, 48 * 3)
            elif self.counter_walk==40:
                self.counter_walk = 0
        self.counter_walk += 1
    def jumploop(self):
        self.counter_jump+=1

        if Globals.selected_alien==1:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Fourarms_Jump1)  # Change to Jump
                self.rect.size=(49*3,57*3)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Fourarms_Jump2)  # Change to Jump
                self.rect.size=(40*3,54*3)
        elif Globals.selected_alien==0:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Wildmutt_Jump1)  # Change to Jump
                self.rect.size=(64*3,40*3)
            elif self.yvel>=0 and self.yvel<-10:
                self.updatecharacter(Player_Sprites.Wildmutt_Jump2)  # Change to Jump
                self.rect.size=(63*3,42*3)
            elif self.yvel>=-10:
                self.updatecharacter(Player_Sprites.Wildmutt_Jump3)  # Change to Jump
                self.rect.size=(47*3,38*3)
        elif Globals.selected_alien==2:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Heatblast_Jump1)
                self.rect.size=(38*3,45*3)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Heatblast_Fall4)
                self.rect.size=(38*3,44*3)     
        elif Globals.selected_alien == 3: 
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.XLR8_Jump)
                self.rect.size=(32*3,42*3)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.XLR8_Fall)
                self.rect.size=(32*3,42*3) 
        elif Globals.selected_alien == 4: 
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Ghostfreak_Jump)
                self.rect.size=(51*2,83*2)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Ghostfreak_Fall)
                self.rect.size=(60*2,83*2)
        elif Globals.selected_alien == 5: 
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Ripjaws_Jump)
                self.rect.size=(int(45*2.5),int(62*2.5))
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Ripjaws_Fall)
                self.rect.size=(int(32*2.5),int(63*2.5))
        elif Globals.selected_alien == 6: 
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Stinkfly_Fly1)
                self.rect.size=(76*2,112*2)
            elif self.counter_jump==6:
                self.updatecharacter(Player_Sprites.Stinkfly_Fly2)
                self.rect.size=(82*2,112*2)
            elif self.counter_jump==12:
                self.counter_jump=0
        elif Globals.selected_alien==7:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Greymatter_Walk3)
                self.rect.size=(int(71/2),int(64/2))
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Greymatter_Walk4)
                self.rect.size=(int(36/2),int(64/2))  
        elif Globals.selected_alien == 8: 
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Diamondhead_Jump)
                self.rect.size=(58*3,74*3)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Diamondhead_Fall)
                self.rect.size=(40*3,74*3)   
        elif Globals.selected_alien==9:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Upgrade_Idle)
                self.rect.size=(67*2,97*2)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Upgrade_Idle)
                self.rect.size=(67*2,97*2) 
        else:
            if self.counter_jump==1 and self.yvel<0:
                self.updatecharacter(Player_Sprites.Ben_Jump2)  # Change to Jump
                self.rect.size=(39 * 3, 50 * 3)
            elif self.yvel>=0:
                self.updatecharacter(Player_Sprites.Ben_Jump3)  # Change to Jump
                self.rect.size=(34 * 3, 48 * 3)               
    def attackloop(self):
        #Globals.selected_alien=0
        self.counter_attack += 1
        if Globals.selected_alien == 0: 
            #self.xvel+=2
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll2)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==6:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll3)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==11:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll4)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==16:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll5)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==21:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll6)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==26:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll7)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==31:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll8)
                self.rect.size=(50*3,38*3)
            elif self.counter_attack==36:
                self.updatecharacter(Player_Sprites.Wildmutt_Roll9)
                self.rect.size=(50*3,38*3)
                self.counter_attack=0
        
        elif Globals.selected_alien==1:
            if self.counter_attack == 1:
                self.updatecharacter(Player_Sprites.Fourarms_Punch1)
                self.rect.size=(42 * 3, 54 * 3)
            elif self.counter_attack == 6:
                self.updatecharacter(Player_Sprites.Fourarms_Punch2)
                self.rect.size= (42 * 3, 54 * 3)
            elif self.counter_attack == 12:
                self.updatecharacter(Player_Sprites.Fourarms_Punch3)
                self.rect.size=(59 * 3, 54 * 3)
            elif self.counter_attack==18:
                self.updatecharacter(Player_Sprites.Fourarms_Punch4)
                self.rect.size=(59 * 3, 54 * 3)
                
            elif self.counter_attack==21:
                self.counter_attack=0
        elif Globals.selected_alien == 2: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Heatblast_Punch1)
                self.rect.size=(32*3,44*3)
            elif self.counter_attack==6:
                self.updatecharacter(Player_Sprites.Heatblast_Punch2)
                self.rect.size=(54*3,44*3)
            elif self.counter_attack==12:
                self.updatecharacter(Player_Sprites.Heatblast_Punch3)
                self.rect.size=(56*3,44*3)
            elif self.counter_attack==18:
                self.updatecharacter(Player_Sprites.Heatblast_Punch4)
                self.rect.size=(53*3,44*3)
                projectilegroup.add(Fireball(self.rect.x, self.rect.y,self.faceright))
            elif self.counter_attack==21:
                self.counter_attack = 0
        elif Globals.selected_alien == 3: 
            if self.xvel==20 or self.xvel==-20:
                self.counter_attack=0
                if self.counter_attackR==1:
                    self.updatecharacter(Player_Sprites.XLR8_Run1)
                    self.rect.size=(45*3,42*3)
                elif self.counter_attackR==5:
                    self.updatecharacter(Player_Sprites.XLR8_Run2)
                    self.rect.size=(52*3,42*3)
                elif self.counter_attackR==10:
                    self.updatecharacter(Player_Sprites.XLR8_Run3)
                    self.rect.size=(53*3,42*3)
                elif self.counter_attackR==15:
                    self.updatecharacter(Player_Sprites.XLR8_Run4)
                    self.rect.size=(67*3,42*3)
                #elif self.counter_attackR==20:
                   # self.counter_attackR=0
                self.counter_attackR+=1
            else:            
                self.counter_attackR=0
                if self.counter_attack==1:
                    self.updatecharacter(Player_Sprites.XLR8_Kick1)
                    self.rect.size=(44*3,42*3)
                elif self.counter_attack==5:
                    self.updatecharacter(Player_Sprites.XLR8_Kick2)
                    self.rect.size=(37*3,42*3)
                elif self.counter_attack==10:
                    self.updatecharacter(Player_Sprites.XLR8_Kick3)
                    self.rect.size=(31*3,42*3)
                elif self.counter_attack==15:
                    self.updatecharacter(Player_Sprites.XLR8_Kick4)
                    self.rect.size=(49*3,42*3)
                elif self.counter_attack==20:
                    self.updatecharacter(Player_Sprites.XLR8_Kick5)
                    self.rect.size=(33*3,42*3)
                elif self.counter_attack==25:
                    self.updatecharacter(Player_Sprites.XLR8_Kick6)
                    self.rect.size=(33*3,42*3)
                elif self.counter_attack==28:
                    self.counter_attack = 0
        elif Globals.selected_alien == 4:
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Ghostfreak_Attack1)
                self.rect.size=(87*2,83*2)
                projectilegroup.add(Wind(self.rect.x, self.rect.y,self.faceright))
            elif self.counter_attack==10:
                self.counter_attack=0
        elif Globals.selected_alien == 5: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Ripjaws_Attack1)
                self.rect.size=(int(49*2.5),int(63*2.5))
            elif self.counter_attack==5:
                self.updatecharacter(Player_Sprites.Ripjaws_Attack2)
                self.rect.size=(int(84*2.5),int(63*2.5))
            elif self.counter_attack==10:
                self.updatecharacter(Player_Sprites.Ripjaws_Attack3)
                self.rect.size=(int(68*2.5),int(63*2.5))
            elif self.counter_attack==15:
                self.counter_attack=0
        elif Globals.selected_alien == 6: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Stinkfly_Attack1)
                self.rect.size=(84*2,112*2)
            elif self.counter_attack==10:
                self.updatecharacter(Player_Sprites.Stinkfly_Attack2)
                self.rect.size=(84*2,112*2)
            elif self.counter_attack==15:
                self.updatecharacter(Player_Sprites.Stinkfly_Attack3)
                self.rect.size=(82*2,112*2)
                projectilegroup.add(StinkShot(self.rect.x, self.rect.y,self.faceright))
            elif self.counter_attack==18:
                self.counter_attack=0
        elif Globals.selected_alien == 7: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Greymatter_Attack1)
                self.rect.size=(int(40/2),int(64/2))
            elif self.counter_attack==5:
                self.updatecharacter(Player_Sprites.Greymatter_Attack2)
                self.rect.size=(int(70/2),int(64/2))
            elif self.counter_attack==10:
                self.counter_attack=0
        elif Globals.selected_alien == 8: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Diamondhead_Attack1)
                self.rect.size=(62*3,74*3)
            elif self.counter_attack==5:
                self.updatecharacter(Player_Sprites.Diamondhead_Attack2)
                self.rect.size=(58*3,74*3)
            elif self.counter_attack==10:
                self.updatecharacter(Player_Sprites.Diamondhead_Attack3)
                self.rect.size=(50*3,74*3)
                projectilegroup.add(Diamond(self.rect.x, self.rect.y,self.faceright,4))
            elif self.counter_attack==15:
                self.updatecharacter(Player_Sprites.Diamondhead_Attack4)
                projectilegroup.add(Diamond(self.rect.x, self.rect.y,self.faceright,3))
            elif self.counter_attack==20:
                projectilegroup.add(Diamond(self.rect.x, self.rect.y,self.faceright,2))
            elif self.counter_attack==25:
                
                projectilegroup.add(Diamond(self.rect.x, self.rect.y,self.faceright,1))
            elif self.counter_attack==30:
                self.counter_attack=0
        elif Globals.selected_alien == 9: 
            if self.counter_attack==1:
                self.updatecharacter(Player_Sprites.Upgrade_Attack1)
                self.rect.size=(63*2,97*2)
            elif self.counter_attack==5:
                self.updatecharacter(Player_Sprites.Upgrade_Attack2)
                self.rect.size=(63*2,97*2)
            elif self.counter_attack==10:
                self.updatecharacter(Player_Sprites.Upgrade_Attack3)
                self.rect.size=(60*2,97*2)
            elif self.counter_attack==15:
                self.updatecharacter(Player_Sprites.Upgrade_Attack4)
                self.rect.size=(110*2,97*2)
            elif self.counter_attack==20:
                self.updatecharacter(Player_Sprites.Upgrade_Attack5)
                self.rect.size=(66*2,97*2)
                projectilegroup.add(Beam(self.rect.x, self.rect.y,self.faceright))
            elif self.counter_attack==25:
                self.updatecharacter(Player_Sprites.Upgrade_Attack6)
                self.rect.size=(60*2,97*2)
            elif self.counter_attack==30:
                self.counter_attack=0
        else:
            if self.counter_attack == 1:
                self.updatecharacter(Player_Sprites.Ben_Punch1)
                self.rect.size=(29 * 3, 48 * 3)
            elif self.counter_attack == 6:
                self.updatecharacter(Player_Sprites.Ben_Punch2)
                self.rect.size= (38 *3, 48 *3)
            elif self.counter_attack == 12:
                self.updatecharacter(Player_Sprites.Ben_Punch3)
                self.rect.size=(43 * 3, 48 * 3)
            elif self.counter_attack==15:
                self.counter_attack = 0
    def transformloop(self):
        self.counter_transform+=1
        if self.counter_transform==1 and Globals.selected_alien==6:
            if self.faceright:
                self.rect.left+=100

        if self.counter_transform==1 and Globals.previous_alien==0 :
            self.updatecharacter(Player_Sprites.Wildmutt_Transform)
            self.rect.size=(49*3,38*3)
        elif self.counter_transform==1 and Globals.previous_alien==1 :
            self.updatecharacter(Player_Sprites.Fourarms_Transform)
            self.rect.size=(46*3,54*3)
        elif self.counter_transform==1 and Globals.previous_alien==2 :
            self.updatecharacter(Player_Sprites.Heatblast_Transform)
            self.rect.size=(30*3,44*3)
        elif self.counter_transform==1 and Globals.previous_alien==3 :
            self.updatecharacter(Player_Sprites.XLR8_Transform)
            self.rect.size=(45*3,42*3)        
        elif self.counter_transform==1 and Globals.previous_alien==4 :
            self.updatecharacter(Player_Sprites.Ghostfreak_Transform)
            self.rect.size=(57*2,83*2)       
        elif self.counter_transform==1 and Globals.previous_alien==5 :
            self.updatecharacter(Player_Sprites.Ripjaws_Transform)
            self.rect.size=(int(53*2.5),int(63*2.5))      
        elif self.counter_transform==1 and Globals.previous_alien==6:
            self.updatecharacter(Player_Sprites.Stinkfly_Transform)
            self.rect.size=(76*2,112*2)
        elif self.counter_transform==1 and Globals.previous_alien==7:
            self.updatecharacter(Player_Sprites.Greymatter_Transform)
            self.rect.size=(int(38/2),int(64/2))
        elif self.counter_transform==1 and Globals.previous_alien==8:
            self.updatecharacter(Player_Sprites.Diamondhead_Transform)
            self.rect.size=(38*3,74*3)
        elif self.counter_transform==1 and Globals.previous_alien==9:
            self.updatecharacter(Player_Sprites.Upgrade_Transform)
            self.rect.size=(67*2,97*2)
        if self.counter_transform==1 and Globals.previous_alien==11 :
            self.updatecharacter(Player_Sprites.Ben_Transform)
            self.rect.size=(28 * 3, 48 * 3)

        if self.counter_transform==10 and Globals.selected_alien==0:
            self.updatecharacter(Player_Sprites.Wildmutt_Transform)
            self.rect.size=(49*3,38*3)
        elif self.counter_transform==10 and Globals.selected_alien==1:
            self.updatecharacter(Player_Sprites.Fourarms_Transform)
            self.rect.size=(46*3,54*3)
        elif self.counter_transform==10 and Globals.selected_alien==2:
            self.updatecharacter(Player_Sprites.Heatblast_Transform)
            self.rect.size=(30*3,44*3)
        elif self.counter_transform==10 and Globals.selected_alien==3:
            self.updatecharacter(Player_Sprites.XLR8_Transform)
            self.rect.size=(45*3,42*3)
        elif self.counter_transform==10 and Globals.selected_alien==4:
            self.updatecharacter(Player_Sprites.Ghostfreak_Transform)
            self.rect.size=(57*2,83*2)
        elif self.counter_transform==10 and Globals.selected_alien==5 :
            self.updatecharacter(Player_Sprites.Ripjaws_Transform)
            self.rect.size=(int(53*2.5),int(63*2.5))    
        elif self.counter_transform==10 and Globals.selected_alien==6:
            self.updatecharacter(Player_Sprites.Stinkfly_Transform)
            self.rect.size=(76*2,112*2)
        elif self.counter_transform==10 and Globals.selected_alien==7:
            self.updatecharacter(Player_Sprites.Greymatter_Transform)
            self.rect.size=(int(38/2),int(64/2))
        elif self.counter_transform==10 and Globals.selected_alien==8:
            self.updatecharacter(Player_Sprites.Diamondhead_Transform)
            self.rect.size=(38*3,74*3)
        elif self.counter_transform==10 and Globals.selected_alien==9:
            self.updatecharacter(Player_Sprites.Upgrade_Transform)
            self.rect.size=(67*2,97*2)
        elif self.counter_transform==10 and Globals.selected_alien==11:
            self.updatecharacter(Player_Sprites.Ben_Transform)
            self.rect.size=(28 * 3, 48 * 3)

        if self.counter_transform>=15:
            self.alien_transform=False
            self.counter_transform=0            
    def destroyloop(self):
        self.counter_dead += 1
        #self.kill()
        if Globals.selected_alien==1:
            if self.counter_dead == 0:
                self.updatecharacter(Player_Sprites.Fourarms_Idle3)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.Fourarms_Idle4)
                self.rect.size=(45 * 3, 54 * 3)
            elif self.counter_dead == 10:
                self.updatecharacter(Player_Sprites.Fourarms_Dead)
                self.rect.size=(46*3,54*3)
            elif self.counter_dead == 15 and self.fade:
                self.kill()
        elif Globals.selected_alien==0:
            if self.counter_dead == 0:
                self.updatecharacter(Player_Sprites.Wildmutt_Idle1)
                self.rect.size=(49*3,38*3)
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.Wildmutt_Idle2)
                self.rect.size=(49*3,38*3)
            elif self.counter_dead == 10 and self.fade:
                self.kill()
        elif Globals.selected_alien==2:
            if self.counter_dead == 0:
                self.updatecharacter(Player_Sprites.Heatblast_Idle3)
                self.rect.size=(30*3,44*3)
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.Heatblast_Idle4)
                self.rect.size=(30*3,44*3)
            elif self.counter_dead == 10:
                self.updatecharacter(Player_Sprites.Heatblast_Dead)
                self.rect.size=(30*3,44*3)
            elif self.counter_dead == 15 and self.fade:
                self.kill()
        elif Globals.selected_alien == 3: 
            if self.counter_dead==0:
                self.updatecharacter(Player_Sprites.XLR8_Walk1)
                self.rect.size=(52*3,42*3)                
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.XLR8_Walk2)
                self.rect.size=(52*3,42*3)
            elif self.counter_dead == 10:
                self.updatecharacter(Player_Sprites.XLR8_Walk3)
                self.rect.size=(52*3,42*3)
            elif self.counter_dead == 15:
                self.updatecharacter(Player_Sprites.XLR8_Dead)
                self.rect.size=(45*3,42*3)
            elif  self.counter_dead == 25 and self.fade:
                self.kill()
        elif Globals.selected_alien == 4: 
            if self.counter_dead==0:
                self.updatecharacter(Player_Sprites.Ghostfreak_Dead1)
                self.rect.size=(44*2,88*2)                
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.Ghostfreak_Dead2)
                self.rect.size=(44*2,88*2)
            elif self.counter_dead == 10 and self.fade:
                self.kill()
        elif Globals.selected_alien == 5: 
            if self.counter_dead==0:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle2)
                self.rect.size=(int(50*2.5),int(63*2.5))
            elif self.counter_dead==5:
                self.updatecharacter(Player_Sprites.Ripjaws_Idle3)
                self.rect.size=(int(52*2.5),int(63*2.5))
            elif self.counter_dead==10:
                self.updatecharacter(Player_Sprites.Ripjaws_Dead)
                self.rect.size=(int(53*2.5),int(63*2.5))
            elif  self.counter_dead == 15 and self.fade:
                self.kill()
        elif Globals.selected_alien == 6: 
            if self.counter_dead==0:
                self.updatecharacter(Player_Sprites.Stinkfly_Dead1)
                self.rect.size=(73*2,69*2)
            elif self.counter_dead==5:
                self.updatecharacter(Player_Sprites.Stinkfly_Dead2)
                self.rect.size=(73*2,69*2)
            elif self.counter_dead == 10 and self.fade:
                self.kill()
        elif Globals.selected_alien==7:
            if self.counter_dead == 0:
                self.updatecharacter(Player_Sprites.Greymatter_Idle)
                self.rect.size=(int(38/2),int(64/2))
            elif self.counter_dead == 10:
                self.updatecharacter(Player_Sprites.Greymatter_Dead)
                self.rect.size=(int(38/2),int(64/2))
            elif self.counter_dead == 20 and self.fade:
                self.kill()
        elif Globals.selected_alien==8:
            if self.counter_dead==5:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle2)
                self.rect.size=(41*3,74*3)
            elif self.counter_dead==10:
                self.updatecharacter(Player_Sprites.Diamondhead_Idle3)
                self.rect.size=(39*3,74*3)
            elif self.counter_dead==15:
                self.updatecharacter(Player_Sprites.Diamondhead_Dead)
                self.rect.size=(38*3,74*3)
            elif self.counter_dead == 20 and self.fade:
                self.kill()
        elif Globals.selected_alien ==9: 
            if self.counter_dead==0:
                self.updatecharacter(Player_Sprites.Upgrade_Idle)
                self.rect.size=(67*2,97*2)
            elif self.counter_dead==5:
                self.updatecharacter(Player_Sprites.Upgrade_Dead)
                self.rect.size=(67*2,97*2)
            elif self.counter_dead == 10 and self.fade:
                self.kill()
        else:
            if self.counter_dead == 0:
                self.updatecharacter(Player_Sprites.Ben_Idle2)
                self.rect.size=(28 * 3, 48 * 3)
            elif self.counter_dead == 5:
                self.updatecharacter(Player_Sprites.Ben_Idle1)
                self.rect.size=(28 * 3, 48 * 3)
            elif self.counter_dead == 10:
                self.updatecharacter(Player_Sprites.Ben_Dead)
                self.rect.size=(28 * 3, 48 * 3)
            elif self.counter_dead == 20 and self.fade:
                self.kill()

#Megawatt Class that randomly assigns xvel, and Handles collisions with player
class Megawatt(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = choice([-1,1,-2,2,-3,3])
        self.yvel = 0
        self.faceright = False

        self.onGround = False
        self.destroyed = False
        self.airborne = True
        self.counter_idle=0
        self.counter_walk=0
        self.counter_dead=0
        self.image = Enemy_Sprites.Megawatt_Idle1
        self.rect = Rect(x, y, 14 * 4, 20 * 4)

    def update(self, platforms, entities):
        if not self.destroyed:
            if not self.onGround:
                self.yvel += 0.3

            self.rect.left += self.xvel
            self.collide(self.xvel, 0, platforms, entities)
            self.rect.top += self.yvel

            self.collide(0, self.yvel, platforms, entities)
            if self.xvel >= 0:
                self.faceright = True 
            elif self.xvel<0:
                self.faceright=False
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)
                    self.faceright = True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)
                    self.faceright = False
                if yvel > 0:
                    self.rect.bottom = p.rect.top-25
                    self.airborne = False
                    self.onGround=True
                    self.yvel = 0
                    self.counter_jump=0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                self.destroyed = True
                self.counter_walk = 0
                self.xvel = 0   
                projectiles.destroyed=True


        for player in entities:
            if hasattr(player,"destroyed"):
                if pygame.sprite.collide_rect(self, player):
                    diffy = player.rect.bottom - self.rect.top
                    diffx1 = player.rect.left - self.rect.right
                    diffx2 = player.rect.right - self.rect.left
                    if player.attack or player.counter_attack!=0:
                        
                        self.destroyed=True

                    if diffy <= 8:  # how high above
                        self.destroyed = True
                        self.counter = 0
                        self.xvel = 0
                        enemygroup.remove(self)
                    
                    if player.attack or player.counter_attack!=0:
                        if diffx1<=8 and not player.faceright:
                            self.destroyed = True
                            
                            #self.counter = 0
                            
                            self.xvel = 0
                        elif diffx2<=8 and  player.faceright:
                            self.destroyed = True
                            
                            #self.counter = 0
                            self.xvel = 0
    
    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            if self.counter_walk!=1 or self.xvel!=0:
                self.walkloop()
            if self.airborne:
                self.updatecharacter(Enemy_Sprites.Megawatt_Fall) 
                self.rect.size=(18 * 4, 18 * 4)
        else:
            self.destroyloop()

    def walkloop(self):
        if self.counter_walk==1:
            self.updatecharacter(Enemy_Sprites.Megawatt_Fly1)
            self.rect.size=(17*4,18*4)
        elif self.counter_walk==10:
            self.updatecharacter(Enemy_Sprites.Megawatt_Fly2)
            self.rect.size=(17*4,18*4)
        elif self.counter_walk==15:
            self.updatecharacter(Enemy_Sprites.Megawatt_Fly3)
            self.rect.size=(17*4,18*4)
        elif self.counter_walk==20:
            self.updatecharacter(Enemy_Sprites.Megawatt_Fly4)
            self.rect.size=(17*4,18*4)
        elif self.counter_walk==25:
            self.counter_walk=0
        self.counter_walk += 1

    def destroyloop(self):
        if self.counter_dead==1:
            self.updatecharacter(Enemy_Sprites.Megawatt_Dead1)
            self.rect.size=(18*4,20*4)
        elif self.counter_dead==5:
            self.updatecharacter(Enemy_Sprites.Megawatt_Dead2)
            self.rect.size=(18*4,20*4)
        elif self.counter_dead==10:
            self.updatecharacter(Enemy_Sprites.Megawatt_Dead3)
            self.rect.size=(18*4,20*4)
        elif self.counter_dead == 15:
            enemygroup.remove(self)
            self.kill()
        self.counter_dead += 1

#Wolf Class that handles following player, and attacking when in range
class Wolf(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.move=True
        self.faceright = True
        self.attack_speed=100
        self.x=x
        self.y=y

        self.onGround = False
        self.airborne = True
        self.counter_walk = 0
        self.counter_idle=0
        self.counter_walk = 0
        self.counter_jump = 0
        self.counter_attack=0
        self.counter_attackR=0
        self.counter_shoot=1
        self.first_shot=True
        self.counter_transform=0
        self.counter_dead=0

        self.up=False
        self.down=False
        self.right=False
        self.left=False

        self.fade=True
        self.image = Enemy_Sprites.Wolf_Idle1
        # self.image = pygame.image.load(
        #"Graphics/Ben_SpriteSheet.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (22 * 3, 60 * 3))
        self.rect = Rect(x, y, 56 * 3, 58 * 3)

        self.alien_transform=False
        self.attack=False
        self.health=Globals.boss_health
    def update(self, platforms, powerupgroup,enemygroup,entities):
        if self.move:
            attack=False
            for player in entities:
                if hasattr(player,"x") or hasattr(player,"y"):
                    diffx_R=player.rect.left-self.rect.left
                    diff_y=self.rect.bottom-player.rect.bottom

                    if Globals.selected_alien==2 or Globals.selected_alien==9:
                        if diffx_R>=8 and diffx_R<=240:
                            attack=True
                            self.faceright=True
                            self.left=False
                            self.right=False
                        elif diffx_R<=8 and diffx_R>=-192:
                            self.faceright=False
                            attack=True 
                            self.left=False
                            self.right=False
                        elif diffx_R<=-192:
                            self.left=True
                            self.right=False
                        elif diffx_R>=240:
                            self.left=False
                            self.right=True
                    else:
                        if diffx_R>=8 and diffx_R<=500:
                            attack=True
                            self.faceright=True
                            self.left=False
                            self.right=False
                        elif diffx_R<=8 and diffx_R>=-492:
                            self.faceright=False
                            attack=True 
                            self.left=False
                            self.right=False
                        elif diffx_R<=-492:
                            self.left=True
                            self.right=False
                        elif diffx_R>=500:
                            self.left=False
                            self.right=True

                    if diff_y>0:
                        self.up=True
                        self.down=False
                    elif diff_y<0:
                        self.up=False
                        self.down=True
                        self.left=True

            if self.up:
                if self.onGround:
                    self.yvel -= 12
            

            if self.left:
                if Globals.selected_alien==0 or Globals.selected_alien==3:
                    self.xvel = -10
                elif Globals.selected_alien==1  or Globals.selected_alien==4 or Globals.selected_alien==8 or Globals.selected_alien==9:
                    self.xvel = -6
                else:
                    self.xvel = -8
                
                self.faceright = False
            if self.right:
                if Globals.selected_alien==0 or Globals.selected_alien==3:
                    self.xvel = 10
                elif Globals.selected_alien==1  or Globals.selected_alien==4 or Globals.selected_alien==8 or Globals.selected_alien==9:
                    self.xvel = 6
                else:
                    self.xvel = 8

                self.faceright = True
            if not self.onGround:
                self.yvel += 0.3
                # max falling speed
                if self.yvel > 100:
                    self.yvel = 100
            if not self.left and not self.right:
                self.xvel = 0

            if self.yvel < 0 or self.yvel > 1.2:
                self.airborne = True
            
            if not self.airborne or self.onGround:
                self.attack=attack

            # increment in x direction
            self.rect.left += self.xvel
            # do x-axis collisions
            self.collide(self.xvel, 0, entities,platforms, powerupgroup,enemygroup,self.up,self.down,self.left,self.right)
            # increment in y direction
            self.rect.top += self.yvel
            # assuming we're in the air
            
            self.onGround = False

            self.destroyed=False

            # do y-axis collisions
            self.collide(0, self.yvel, entities,platforms, powerupgroup,enemygroup,self.up,self.down,self.left,self.right)
        self.animate()

    def collide(self, xvel, yvel,entities, platforms, powerupgroup,enemygroup,up,down,left,right):

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if p.tile=="E" and Globals.keys>=3:
                    p.change_loop()
                    self.fade=False
                    self.destroyloop()
                    self.rect.midbottom=p.rect.midbottom
                    
                else:
                    if xvel==0 and yvel==0 and self.faceright:
                        self.rect.right=p.rect.left
                    if xvel > 0:

                        self.rect.right = p.rect.left
                        if self.airborne and left:
                            self.xvel=-8
                            self.yvel = -8
                        # print "collide right"
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        if right:
                            self.xvel =8
                            self.yvel = -8
                        # print "collide left"
                    if yvel > 0:
                        if p.tile=="A":
                            self.rect.bottom = p.rect.top+25
                            self.health=0
                            self.destroyed=True
                            
                        else:
                            self.rect.bottom = p.rect.top
                            
                        self.onGround = True
                        self.counter_jump=0
                        self.airborne = False
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
            else:
                if p.tile=="E" and Globals.keys>=3:
                    p.door_ready()

        for player in entities:
            if hasattr(player,"xvel"):
                if pygame.sprite.collide_rect(self, player):
                    diffy = self.rect.bottom - player.rect.top
                    diffx1 = player.rect.left - self.rect.right
                    diffx2 = player.rect.right - self.rect.left
                    if player.attack:
                        
                        if self.health>0:
                            if Globals.selected_alien==1 or Globals.selected_alien==9:
                                self.health-=0.15
                            else:
                                self.health-=0.05
                            Globals.boss_health=self.health
                        else:
                            self.health=0
                            Globals.boss_health=self.health
                            self.destroyed=True

        for projectile in projectilegroup:
            if not hasattr(projectile,"name"):
                if pygame.sprite.collide_rect(self, projectile):
                    if self.health>0:
                        if Globals.selected_alien==9:
                            self.health-=0.10
                        else:
                            self.health-=0.05
                        Globals.boss_health=self.health
                        #self.move=False
                    else:
                        self.health=0
                        Globals.boss_health=self.health
                        self.destroyed=True

        for powerup in powerupgroup:
            if pygame.sprite.collide_rect(self, powerup):
                
                self.alien_transform=True

        
    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf
    def animate(self):
        
        if not self.destroyed and self.counter_dead==0:
            if self.xvel > 0 or self.xvel < 0:
                self.counter_idle=0
                self.first_shot=True
                # self.updatecharacter(Player_Sprites.Ben_Walk1)
                if self.attack or self.counter_attackR!=0:
                    self.attackloop()
                    self.counter_walk=0
                elif self.airborne:
                    self.jumploop()
                    self.counter_walk=0
                else:
                    self.walkloop()
            else:

                self.counter_attackR=0
                
                if self.attack or self.counter_attack!=0:
                    self.attackloop()
                    self.counter_walk=1
                elif self.airborne:
                    self.jumploop()
                    self.counter_walk=1
                else:
                    self.idleloop()

        else:
            self.destroyloop()  
    def idleloop(self):
        if self.counter_idle==1:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle1)
            self.rect.size=(56*3,58*3)
        elif self.counter_idle==5:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle2)
            self.rect.size=(54*3,58*3)
        elif self.counter_idle==10:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle3)
            self.rect.size=(60*3,58*3)
        elif self.counter_idle==15:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle4)
            self.rect.size=(63*3,58*3)
        elif self.counter_idle==20:
            self.counter_idle=0
        
        self.counter_idle += 1
    def walkloop(self):
        if self.counter_walk==1:
            self.updatecharacter(Enemy_Sprites.Wolf_Walk1)
            self.rect.size=(82*3,58*3)
        elif self.counter_walk==5:
            self.updatecharacter(Enemy_Sprites.Wolf_Walk2)
            self.rect.size=(90*3,58*3)
        elif self.counter_walk==10:
            self.updatecharacter(Enemy_Sprites.Wolf_Walk3)
            self.rect.size=(75*3,58*3)
        elif self.counter_walk==15:
            self.updatecharacter(Enemy_Sprites.Wolf_Walk4)
            self.rect.size=(71*3,58*3)
        elif self.counter_walk==20:
            self.counter_walk=0
        self.counter_walk += 1
    def jumploop(self):
        self.counter_jump+=1

        if self.counter_jump==1 and self.yvel<0:
            self.updatecharacter(Enemy_Sprites.Wolf_Jump)
            self.rect.size=(54*3,62*3)
        elif self.yvel>=0:
            self.updatecharacter(Enemy_Sprites.Wolf_Fall)
            self.rect.size=(35*3,58*3)
            self.counter_jump=0
    def attackloop(self):
        #Attack only happens when ever the counter is divisible by 100. But, if alien=Upgrade, then frequency of waves increases because Upgrade is strong
        if Globals.selected_alien==9:
            self.attack_speed=50
        else:
            self.attack_speed=100
        
        if self.counter_shoot%self.attack_speed==0:
            self.counter_attack += 1  
            if self.counter_attack==1:
                self.updatecharacter(Enemy_Sprites.Wolf_Attack1)
                self.rect.size=(55*3,58*3)
            elif self.counter_attack==3:
                self.updatecharacter(Enemy_Sprites.Wolf_Attack2)
                self.rect.size=(58*3,58*3)
            elif self.counter_attack==5:
                self.updatecharacter(Enemy_Sprites.Wolf_Attack3)
                self.rect.size=(63*3,58*3)     
            elif self.counter_attack==7:
                self.updatecharacter(Enemy_Sprites.Wolf_Attack4)
                self.rect.size=(64*3,58*3)
                projectilegroup.add(Wave(self.rect.x, self.rect.y,self.faceright))
            elif self.counter_attack==10:
                self.updatecharacter(Enemy_Sprites.Wolf_Idle1)
            elif self.counter_attack==12:
                self.counter_attack=0
                self.counter_shoot+=1
        else:
            self.idleloop()
            if self.first_shot:
                self.counter_shoot=0
                self.first_shot=False
            else:
                self.counter_shoot+=1
    def destroyloop(self):
        self.counter_dead += 1
        if self.counter_dead == 0:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle1)
            self.rect.size=(56*3,58*3)
        elif self.counter_dead == 5:
            self.updatecharacter(Enemy_Sprites.Wolf_Idle2)
            self.rect.size=(54*3,58*3)
        elif self.counter_dead == 10:
            self.updatecharacter(Enemy_Sprites.Wolf_Dead)
            self.rect.size=(54*3,58*3)
        elif self.counter_dead == 20 and self.fade:
            Globals.boss_health=-20
            self.kill()

#Wave Class for Boss(Wolf) that handles shooting the player when in range. 
class Wave(Entity):
    def __init__(self, x, y,faceright):
        Entity.__init__(self)
        self.name="Wave"#Added to differentiate from other projectiles
        self.xvel = 0
        self.yvel = 0
        self.faceright = faceright
        ansurf=Enemy_Sprites.Wave_Shoot
        if self.faceright==True:
            self.xvel=5
            self.rect = Rect(x+160, y+5,61 * 3, 39 * 3)
        else:
            self.xvel=-5
            self.rect = Rect(x-170, y+5, 61 * 3, 39 * 3)
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf
        self.destroyed = False
        self.airborne = False
        self.counter_dead=0
        self.range_left=50

        # self.image = pygame.image.load(
        #"Graphics/Ben_SpriteSheet.png").convert_alpha()
        

    def update(self, platforms, entities):
        if not self.destroyed:
            self.rect.left += self.xvel
            self.collide(self.xvel, 0, platforms, entities)
            self.rect.top += self.yvel

            self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.counter_spin = 0
                self.xvel = 0
                if hasattr(player,"xvel"):
                    if player.health!=0:
                        player.health-=10
                        Globals.player_health=player.health
                        
                    else:
                        player.destroyed=True   
                        Globals.player_health=player.health
  

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.counter_walk = 0
                    self.xvel = 0   
                    projectiles.destroyed=True

    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
            self.range_left-=1
        else:
            pass

    def destroyloop(self):
        if self.counter_dead==5:
            self.kill()
        self.counter_dead+=1

#PowerUp Class that Handles collisions with player and switching aliens.
class PowerUp(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.name="Watch"
        self.destroyed = False
        self.counter_dead=0

        self.image = GameObject_Sprites.Watch_1
        self.rect = Rect(x, y, 80, 80)

    def update(self, platforms, entities):
        self.collide(platforms, entities)
        self.collide( platforms, entities)
        self.animate()

    def collide(self, platforms, entities):
        for player in entities:
            if hasattr(player,"attack"):
                if pygame.sprite.collide_rect(self, player):
                    self.destroyed = True
                    self.counter_walk = 0
                
    def updatecharacter(self, ansurf):
        self.image = ansurf

    def animate(self):
        if self.destroyed:
            self.destroyloop()

    def destroyloop(self):
        Globals.previous_alien=Globals.selected_alien
        aliens_available=[GameObject_Sprites.Wildmutt,GameObject_Sprites.Fourarms,GameObject_Sprites.Heatblast,GameObject_Sprites.XLR8,GameObject_Sprites.Ghostfreak,GameObject_Sprites.Ripjaws,GameObject_Sprites.Stinkfly,GameObject_Sprites.GreyMatter,GameObject_Sprites.Diamondhead,GameObject_Sprites.Upgrade]
        aliens_ready=[GameObject_Sprites.Wildmutt_Ready,GameObject_Sprites.Fourarms_Ready,GameObject_Sprites.Heatblast_Ready,GameObject_Sprites.XLR8_Ready,GameObject_Sprites.Ghostfreak_Ready,GameObject_Sprites.Ripjaws_Ready,GameObject_Sprites.Stinkfly_Ready,GameObject_Sprites.GreyMatter_Ready,GameObject_Sprites.Diamondhead_Ready,GameObject_Sprites.Upgrade_Ready]
        if self.counter_dead == 0:
            Globals.selected_alien=randint(0,9)
            Globals.timer=10
            self.updatecharacter(GameObject_Sprites.Watch_1)
        elif self.counter_dead == 3:
            self.updatecharacter(GameObject_Sprites.Watch_2)
        elif self.counter_dead == 6:
            self.updatecharacter(GameObject_Sprites.Watch_3)
        elif self.counter_dead == 9:
            self.updatecharacter(GameObject_Sprites.Watch_4)
        elif self.counter_dead == 12:
            self.updatecharacter(GameObject_Sprites.Watch_5)
        elif self.counter_dead == 15:
            self.updatecharacter(aliens_available[Globals.selected_alien])
        elif self.counter_dead == 18:
            self.updatecharacter(aliens_ready[Globals.selected_alien])
        elif self.counter_dead == 21:
            self.kill()
        self.counter_dead += 1

#Heart Class that handles boosting player's health upon collision
class Heart(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.destroyed = False
        self.counter_dead=0

        self.image = GameObject_Sprites.Heart_1
        self.rect = Rect(x, y, int(194 / 3), int(176 / 3))

    def update(self, platforms, entities):
        if not self.destroyed:
            self.collide( platforms, entities)
            self.collide( platforms, entities)
        self.animate()

    def collide(self, platforms, entities):
        for player in entities:
            if hasattr(player,"attack"):
                if pygame.sprite.collide_rect(self, player):
                    self.destroyed = True
                    Globals.player_health+=20
                    player.health=Globals.player_health
    def updatecharacter(self, ansurf):
        self.image = ansurf                
    def animate(self):
        if self.destroyed:
            self.destroyloop()

    def destroyloop(self):
        if self.counter_dead == 1:
            self.updatecharacter(GameObject_Sprites.Heart_2)
        elif self.counter_dead==30:
            self.kill()
        self.counter_dead += 1

#Gold Key Class that handles updating keys variable. This leads to opening doors to next level 
class GoldKey(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.destroyed = False
        self.counter_dead=0
        self.x=x
        self.y=y
        self.image = GameObject_Sprites.Door_Key
        self.rect = Rect(x, y,64, 49)

    def update(self, platforms, entities):
        self.collide(platforms, entities)
        self.collide( platforms, entities)
        self.animate()
        
    def collide(self, platforms, entities):
        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                powerupgroup.remove(self)

    def animate(self):
        if self.destroyed:
            self.destroyloop()

    def destroyloop(self):
        if self.counter_dead == 0:
            Globals.keys+=1
            self.kill()

#Instructions Class that just prints the instructions on Level 1. This could have been done without classes but I just got used to it
class Instructions(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = GameObject_Sprites.Instructions
        self.rect = Rect(x, y,195, 155)

#Fireball Class for Heatblast that handles shooting enemies and animating Fireball spin
class Fireball(Entity):
    def __init__(self, x, y,faceright):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = faceright
        if self.faceright==True:
            self.xvel=5
            self.rect = Rect(x+160, y+37, 14*3,14*3)
        else:
            self.xvel=-5
            self.rect = Rect(x-37, y+37, 14*3,14*3)
        self.onGround = True
        self.destroyed = False
        self.airborne = False
        self.counter_spin = 0
        self.counter_dead=0
        self.range_left=50

        self.image = Projectile_Sprites.Fireball_Spin1
        
    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = True

        self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.counter_spin = 0
                self.xvel = 0

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.counter_walk = 0
                    self.xvel = 0   
                    projectiles.destroyed=True
            
    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
            if self.counter_spin==1:
                self.updatecharacter(Projectile_Sprites.Fireball_Spin1)
            elif self.counter_spin==5:
                self.updatecharacter(Projectile_Sprites.Fireball_Spin2)
            elif self.counter_spin==10:
                self.updatecharacter(Projectile_Sprites.Fireball_Spin3)
            elif self.counter_spin==15:
                self.updatecharacter(Projectile_Sprites.Fireball_Spin4)
            elif self.counter_spin==20:
                self.counter_spin=0
            self.counter_spin += 1
            self.range_left-=1

    def destroyloop(self):
        self.kill()

#Wind Class for Ghostfreak that handles shooting enemies and animating the Wind
class Wind(Entity):
    def __init__(self, x, y,faceright):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = faceright
        if self.faceright==True:
            self.xvel=8
            self.rect = Rect(x+170, y, 36*2,78*2)
        else:
            self.xvel=-8
            self.rect = Rect(x-90, y, 36*2,78*2)
        self.onGround = True
        self.destroyed = False
        self.airborne = False
        self.counter_blow = 0
        self.counter_dead=0
        self.range_left=100

        self.image=Projectile_Sprites.Wind_Blow1

    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = True

        self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.counter_blow = 0
                self.xvel = 0

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.counter_walk = 0
                    self.xvel = 0   
                    projectiles.destroyed=True


                


    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
      
            if self.counter_blow==1:
                
                self.updatecharacter(Projectile_Sprites.Wind_Blow1)
                self.rect.size=(36*2,78*2)
            elif self.counter_blow==5:
                self.updatecharacter(Projectile_Sprites.Wind_Blow2)
                self.rect.size=(61*2,78*2)
            elif self.counter_blow==10:
                self.updatecharacter(Projectile_Sprites.Wind_Blow3)
                self.rect.size=(63*2,78*2)
            elif self.counter_blow==15:
                self.updatecharacter(Projectile_Sprites.Wind_Blow4)
                self.rect.size=(68*2,78*2)
            elif self.counter_blow==20:
                self.updatecharacter(Projectile_Sprites.Wind_Blow5)
                self.rect.size=(69*2,78*2)
            elif self.counter_blow==25:
                self.updatecharacter(Projectile_Sprites.Wind_Blow6)
                self.rect.size=(68*2,78*2)
            elif self.counter_blow==30:
                self.range_left=0
            self.counter_blow += 1
            self.range_left-=1
        else:
            pass

    def destroyloop(self):
        self.kill()

#StinkShot Class for Stinkfly that handles shooting enemies
class StinkShot(Entity):
    def __init__(self, x, y,faceright):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = faceright
        if self.faceright==True:
            self.xvel=5
            self.rect = Rect(x+160, y+80,36 * 2, 12 * 2)
        else:
            self.xvel=-5
            self.rect = Rect(x-90, y+80, 36 * 2, 12 * 2)
        self.onGround = True
        self.destroyed = False
        self.airborne = False
        self.counter_dead=0
        self.range_left=50
        self.image = Projectile_Sprites.Stink_Shoot

    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = True

        self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.xvel = 0

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.xvel = 0   
                    projectiles.destroyed=True

    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
            self.updatecharacter(Projectile_Sprites.Stink_Shoot)
            self.range_left-=1
        else:
            pass

    def destroyloop(self):
        self.kill()

#Diamond Class for Diamondhead that handles shooting 4 different types of diamonds at different locations
class Diamond(Entity):
    def __init__(self, x, y,faceright,diamond_type):
        Entity.__init__(self)
        self.yvel = 0
        self.faceright = faceright
        self.diamond_type=diamond_type
        if self.diamond_type==1:
            ansurf=Projectile_Sprites.Diamond1
            self.range_left=120
        elif self.diamond_type==2:
            ansurf=Projectile_Sprites.Diamond2
            self.range_left=106
        elif self.diamond_type==3:
            ansurf=Projectile_Sprites.Diamond3
            self.range_left=87
        elif self.diamond_type==4:
            ansurf=Projectile_Sprites.Diamond4
            self.range_left=50
        if self.faceright==True:
            self.xvel=5
            if self.diamond_type==1:
                self.rect = Rect(x+160, y+191,14 * 3, 10 * 3)
            elif self.diamond_type==2:
                self.rect = Rect(x+190, y+117,25 * 3, 35 * 3)
            elif self.diamond_type==3:
                self.rect = Rect(x+250, y+27,41 * 3, 65 * 3)
            elif self.diamond_type==4:
                self.rect = Rect(x+360, y-102,60 * 3, 108 * 3)
        else:
            self.xvel=-5
            if self.diamond_type==1:
                self.rect = Rect(x-40, y+191,14 * 3, 10 * 3)
            elif self.diamond_type==2:
                self.rect = Rect(x-100, y+117,25 * 3, 35 * 3)
            elif self.diamond_type==3:
                self.rect = Rect(x-214, y+27,41 * 3, 65 * 3)
            elif self.diamond_type==4:
                self.rect = Rect(x-385, y-102,60 * 3, 108 * 3)
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf
        self.onGround = True
        self.destroyed = False
        self.airborne = False
        self.counter_dead=0
        

        # self.image = pygame.image.load(
        #"Graphics/Ben_SpriteSheet.png").convert_alpha()
        

    def update(self, platforms, entities):
        # if right:
        # self.xvel = 8
         #   self.faceright = True
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3

      # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, entities)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = True

        # do y-axis collisions
        self.collide(0, self.yvel, platforms, entities)
        # self.updatecharacter(Player_Sprites.Ben_Walk1)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.counter_spin = 0
                self.xvel = 0

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.counter_walk = 0
                    self.xvel = 0   
                    projectiles.destroyed=True

                

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
            self.range_left-=1
        else:
            pass

    def destroyloop(self):
        self.kill()

#Beam Class for Upgrade
class Beam(Entity):
    def __init__(self, x, y,faceright):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = faceright
        if self.faceright==True:
            self.xvel=5
            self.rect = Rect(x+160, y+80,36 * 2, 12 * 2)
        else:
            self.xvel=-5
            self.rect = Rect(x-90, y+80, 36 * 2, 12 * 2)
        self.destroyed = False
        self.airborne = False
        self.counter_spin = 0
        self.counter_dead=0
        self.range_left=100

        self.image = Projectile_Sprites.Beam_Shot

    def update(self, platforms, entities):
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.destroyed=True

        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                self.counter_spin = 0
                self.xvel = 0

        for projectiles in projectilegroup:
            if pygame.sprite.collide_rect(self, projectiles):   
                if self!=projectiles:
                    self.destroyed = True
                    self.counter_walk = 0
                    self.xvel = 0   
                    projectiles.destroyed=True

    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def animate(self):
        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.xvel!=0:
            if self.range_left<=0:
                self.destroyed=True
            self.updatecharacter(Projectile_Sprites.Beam_Shot)
            self.range_left-=1

    def destroyloop(self):
        self.kill()

#Platform Class that handles blitting specific tiles depending on the type of letter in the levels list
class Platform(Entity):
    def __init__(self, x, y,tile):
        Entity.__init__(self)
        self.counter_change = 0
        self.tile=tile
        if self.tile=="E":
            self.image = pygame.image.load("Graphics/DoorLocked.png")
        elif self.tile=="P":
            self.image = pygame.image.load("Graphics/Tile (2).png").convert()
        elif self.tile=="C":
            self.image = pygame.image.load("Graphics/Tile (3a).png").convert()
        elif self.tile=="A":
            self.image = pygame.image.load("Graphics/Acid (1).png")
        elif self.tile=="D":
            self.image = pygame.image.load("Graphics/Tile (1a).png").convert()
        elif self.tile=="L":
            self.image = pygame.image.load("Graphics/BGTile (4).png").convert()
        elif self.tile=="l":
            self.image = pygame.image.load("Graphics/BGTile (3).png").convert()
        elif self.tile=="g":
            self.image = pygame.image.load("Graphics/Tile (12).png")
        elif self.tile=="h":
            self.image = pygame.image.load("Graphics/Tile (13).png")
        elif self.tile=="j":
            self.image = pygame.image.load("Graphics/Tile (14).png")
        elif self.tile=="c":
            self.image = pygame.image.load("Graphics/Tile (6a).png")
        elif self.tile=="a":
            self.image = pygame.image.load("Graphics/Acid (2).png")
        elif self.tile=="d":
            self.image = pygame.image.load("Graphics/Tile (4a).png")
        elif self.tile=="p":
            self.image = pygame.image.load("Graphics/Tile (5).png")
        
        if self.tile=="E":
            self.image = pygame.transform.scale(self.image, (116,192))
        else:
            self.image = pygame.transform.scale(self.image, (64,64))
        

        if self.tile=="E":
            self.rect = Rect(x, y,116,192)

        elif self.tile=="g" or  self.tile=="h" or  self.tile=="j":
            self.rect = Rect(x, y, 64, 32)  # change according to pic width
        else:
            self.rect = Rect(x, y, 64, 64)  # change according to pic width
    def door_ready(self):
        self.image= GameObject_Sprites.Door_Ready

    #Changing Door sprite when player collects 3 keys
    def change_loop(self):
        if self.counter_change==1:
            self.image= GameObject_Sprites.Door_Open
        elif self.counter_change==20:
            Globals.current_level+=1
            main()     
        self.counter_change+=1
    def update(self):
        pass

#Calling main() on initialization
if __name__ == "__main__":
    main()

#Quiting game when main is exited
pygame.quit()