import pygame
import random

import GraphicEngine


class Drop:
    def __init__(self, windowWidth: int, widnowHeight: int):
        self.__rng = random.Random()
        self.__w = windowWidth
        self.__h = widnowHeight
        self.x = int(self.__rng.random() * self.__w)
        self.y = int(GraphicEngine.mathMap(self.__rng.random(), 0, 1, -500, -50))
        self.__getStarVals()

    def __getStarVals(self):
        self.z = GraphicEngine.mathMap(self.__rng.random(), 0, 1, 0, 20)
        self.ySpeed = GraphicEngine.mathMap(self.z, 0, 20, 4, 10)
        self.length = GraphicEngine.mathMap(self.z, 0, 20, 10, 20)
        self.width = int(GraphicEngine.mathMap(self.z, 0, 20, 1, 3))

    def update(self):
        self.y += self.ySpeed
        self.ySpeed += 0.01
        if self.y > self.__h:
            self.y = int(GraphicEngine.mathMap(self.__rng.random(), 0, 1, -200, -100))
            self.__getStarVals()

    def show(self, window: pygame.Surface):
        color = (138, 43, 226)
        pygame.draw.line(
            window, color, (self.x, self.y), (self.x, self.y + self.length), self.width
        )
