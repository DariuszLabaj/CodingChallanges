import pygame
from Fireworks.firework import Firework
import GraphicEngine
from random import random
import time


class Window(GraphicEngine.PygameGFX):
    fireworks: list[Firework]
    gravity = pygame.Vector2(0, 0.2)

    def Setup(self):
        self.fireworks = []
        self.background(0)
        self.startTime = time.time()

    def Draw(self):
        if time.time() - self.startTime > 10:
            self.Stop()
        self.background((0, 25))
        if random() < 0.1:
            self.fireworks.append(Firework(self.Width, self.Height, self.gravity))
        print(int(self.FramePerSec.get_fps()), end="\r")
        for i in range(len(self.fireworks) - 1, -1, -1):
            self.fireworks[i].update()
            self.fireworks[i].show(self.DisplaySurface)
            if self.fireworks[i].offScreen:
                self.fireworks.pop(i)
