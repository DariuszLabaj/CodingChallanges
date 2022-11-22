from typing import Tuple
from random import randint
import pygame

from GraphicEngine import random2DVector


class Particle:
    @property
    def __rect(self):
        return pygame.Rect(0, 0, self.size, self.size)

    @property
    def done(self):
        return self.lifespan < 1

    @property
    def __color(self):
        if self.lifespan < 0:
            self.lifespan = 0
        return pygame.Color(self.r, self.g, self.b, self.lifespan)

    @property
    def Color(self):
        return (self.r, self.g, self.b)

    def __init__(
        self,
        x: float,
        y: float,
        firework: bool,
        size: float = 4,
        color: Tuple[int, int, int] = (255, 255, 255),
        canvasHeight: int = 480,
    ):
        if firework:
            maxspeed = canvasHeight * 0.017437365 + 3.670064875
            self.vel = pygame.Vector2(0, -randint(int(maxspeed * 0.75), int(maxspeed)))
        else:
            self.vel = random2DVector()
            self.vel *= randint(1, 20)
        self.firework = firework
        self.lifespan = 255
        self.acc = pygame.Vector2(0, 0)
        self.size = size
        self.pos = pygame.Vector2(x, y - self.size)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    def applyForce(self, force: pygame.Vector2):
        self.acc += force

    def update(self):
        if not self.firework:
            self.vel *= 0.85
            self.lifespan -= 4
        self.vel += self.acc
        self.pos += self.vel
        self.acc.x = 0
        self.acc.y = 0

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        surf = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.__color, self.__rect)
        window.blit(surf, self.pos)
