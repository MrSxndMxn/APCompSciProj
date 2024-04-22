import sys

import os

import pygame
import NPC
import camera

class Game():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Wave Survivor")
        self.width = 1920
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.Surface((int(self.width), int(self.height)))

        

        self.clock = pygame.time.Clock()

        #assets stored in dictionary
        self.assets = {
            'player': pygame.image.load("assets/semiImgs/Aquatic Scourge Style Ant-1.png.png"),
            'ant': pygame.image.load("assets/semiImgs/Aquatic Scourge Style Ant-1.png.png")
        }

        #Player code
        self.player = pygame.image.load("assets/semiImgs/Aquatic Scourge Style Ant-1.png.png")

        

        self.movement = [False, False, False, False]
        self.scroll = [0, 0]

        self.playerStats = NPC.player(self, (160, 160), 100, 3, 2, [1280, 400])

        #enemy code
        self.enemy = NPC.npc(self, (160, 160), 10, 2, 1, self.playerStats.myPos[0], self.playerStats.myPos[1], [100, 10])
        self.enemyImg = pygame.image.load("assets/semiImgs/Aquatic Scourge Style Ant-1.png.png")

        #function to update the position of npcs
    def updateNPCPos(self):
        distance = NPC.npc.locatePlayer(self.playerStats.myPos[0], self.playerStats.myPos[1], self.enemy.myPos)
        #find the directions to normalize the magnitude
        #distance cannot be specifically used because we need to know the 
        #individual directions to actually move the npc
        #because of the use of lists.
        directionX = (self.playerStats.myPos[0] - self.enemy.myPos[0]) * self.playerStats.maxSpeed
        directionY = (self.playerStats.myPos[1] - self.enemy.myPos[1]) * self.playerStats.maxSpeed

        #magnitude and normalization in one.
        magnitude = ((directionX) ** 2 + (directionY) ** 2) ** 0.5

        #the code below stops the npc movement if the npc is directly inside of and/or a pos 0
        if magnitude != 0:
            directionX /= magnitude
            directionY /= magnitude
            
        if distance > 0:
            self.enemy.myPos[0] += directionX * self.enemy.maxSpeed
            self.enemy.myPos[1] += directionY * self.enemy.maxSpeed
        

    def run(self):
        while True:
            self.display.fill((0, 50, 100))

            self.scroll[0] += (self.playerStats.playerCollision().centerx - self.display.get_width() / 2- self.scroll[0])  / 1
            self.scroll[1] += (self.playerStats.playerCollision().centery - self.display.get_height() / 2 - self.scroll[1])  / 1
            renderScroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.playerStats.myPos[1] += self.movement[3] - self.movement[2]
            self.playerStats.myPos[0] += self.movement[1] - self.movement[0]

            self.playerStats.renderPlayer(self.display, offset=renderScroll)
            self.enemy.renderNPC(self.display, offset=(renderScroll))
            #updates npc position
            self.updateNPCPos()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[3] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()