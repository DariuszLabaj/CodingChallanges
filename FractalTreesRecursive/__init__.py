import math
import GraphicEngine
import pygame


class Window(GraphicEngine.PygameGFX):
    startLenght: float
    white = pygame.Color(255, 255, 255)

    def Setup(self):
        self.startLenght = self.Width/3
        self.minLenght = 4
        self.branchAngle = math.pi/6

    def Draw(self):
        self.background(51)
        self.branch(pygame.Vector2(self.Width/2, self.Height), self.startLenght, -math.pi/2)

    def branch(self, poz: pygame.Vector2, length: float, angle: float):
        if length < self.minLenght:
            return
        size = int(GraphicEngine.mathMap(length, self.startLenght, self.minLenght, 9, 1))
        x = math.cos(angle) * length
        y = math.sin(angle) * length
        pygame.draw.line(
            self.DisplaySurface,
            self.white,
            poz,
            (x + poz.x, y + poz.y), size
        )
        self.branch(pygame.Vector2(x + poz.x, y + poz.y), length*0.67, angle+self.branchAngle)
        self.branch(pygame.Vector2(x + poz.x, y + poz.y), length*0.67, angle-self.branchAngle)
