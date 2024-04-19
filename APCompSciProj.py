import sys

import os

import pygame

class Game():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Wave Survivor")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.player = pygame.image.load("assets/semiImgs/Aquatic Scourge Style Ant-1.png.png")

        self.playerPos = [160, 260]

        self.movement = [False, False, False, False]

    def run(self):
        while True:
            self.screen.fill((0, 50, 100))

            self.playerPos[1] += self.movement[3] - self.movement[2]
            self.playerPos[0] += self.movement[1] - self.movement[0]
            self.screen.blit(self.player, self.playerPos)

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

            pygame.display.update()
            self.clock.tick(60)

Game().run()