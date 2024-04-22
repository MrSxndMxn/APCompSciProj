#Code for all enemies
import pygame
class npc:
    def __init__(self, game, size, maxLife, maxDam, maxSpeed, targetPosX, targetPosY, myPos):
        self.game = game
        self.size = size
        self.maxLife = maxLife
        self.maxDam = maxDam
        self.maxSpeed = maxSpeed
        self.target = [targetPosX, targetPosY]
        self.myPos = myPos
        #self.maxLife = 10
        #self.maxDam = 1
        #self.maxSpeed = 1

    def NPCCollision(self):
        return pygame.Rect(self.myPos[0], self.myPos[1], self.size[0], self.size[1])
    
    def locatePlayer(targetPosX, targetPosY, myPos):
        distance = (targetPosX - myPos[0]) ** 2 + (targetPosY - myPos[1]) ** 2
        return distance
    
    def renderNPC(self, surface, offset=(0, 0)):
        surface.blit(self.game.assets["ant"], (self.myPos[0] - offset[0], self.myPos[1] - offset[1]))
    
class player:
    def __init__(self, game, size, maxLife, maxDam, maxSpeed, myPos):
        self.game = game
        self.maxLife = maxLife
        self.maxDam = maxDam
        self.maxSpeed = maxSpeed
        self.myPos = myPos
        self.size = size

    def playerCollision(self):
        return pygame.Rect(self.myPos[0], self.myPos[1], self.size[0], self.size[1])

    def renderPlayer(self, surface, offset=(0,0)):
        surface.blit(self.game.assets['player'], (self.myPos[0] - offset[0], self.myPos[1] - offset[1]))
    