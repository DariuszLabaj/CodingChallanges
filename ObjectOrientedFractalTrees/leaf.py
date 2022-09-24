from functools import cached_property
import pygame
import random


class Leaf:
    @cached_property
    def diameter(self):
        return self.radius * 2

    @property
    def Rect(self):
        return pygame.Rect(
            self.poz.x - self.radius,
            self.poz.y - self.radius,
            self.diameter,
            self.diameter,
        )

    def __init__(self, x: int, y: int):
        self.poz = pygame.Vector2(x, y)
        self.radius = 4
        self.__rect = pygame.Rect(0, 0, self.diameter, self.diameter)
        self.rng = random.Random()

    def fall(self):
        self.poz.x += self.rng.randint(-1, 1)
        self.poz.y += self.rng.randint(0, 2)

    def __createSurface(self):
        return pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)

    def show(self, window: pygame.Surface):
        surface = self.__createSurface()
        pygame.draw.ellipse(surface, (255, 0, 100, 100), self.__rect)
        window.blit(surface, self.Rect)
