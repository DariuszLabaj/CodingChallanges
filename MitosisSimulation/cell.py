from __future__ import annotations
import random
from typing import Optional, Tuple
import pygame


class Cell:
    @property
    def Rect(self):
        return pygame.Rect(
            self.pos.x - self.radius / 2,
            self.pos.y - self.radius / 2,
            self.radius,
            self.radius,
        )

    @staticmethod
    def RandomCell(limitV: Tuple[int, int], limitH: tuple[int, int]) -> Cell:
        return Cell(Cell.getPosition(limitV, limitH), 80)

    def __init__(self, vector: pygame.Vector2, radius: int, color: Optional[pygame.Color] = None):
        self.__rng = random.Random()
        self.pos = vector
        if color:
            self.color = color
        else:
            self.color = pygame.Color(
                self.__rng.randint(100, 255), 0, self.__rng.randint(100, 255), 10
            )
        self.radius = radius
        self.__nextRandomVector = None

    @staticmethod
    def getPosition(limitV: Tuple[int, int], limitH: tuple[int, int]) -> pygame.Vector2:
        rng = random.Random()
        x = rng.randint(limitV[0], limitV[1])
        y = rng.randint(limitH[0], limitH[0])
        return pygame.Vector2(x, y)

    @staticmethod
    def random2DVector() -> pygame.Vector2:
        rng = random.Random()
        return pygame.Vector2(rng.random() * 2 - 1, rng.random() * 2 - 1)

    def split(self) -> Cell:
        if self.__nextRandomVector:
            return Cell(self.__nextRandomVector, self.radius*0.75, self.color)
        else:
            rngVector = Cell.random2DVector()
            newVector = pygame.Vector2(self.pos.x, self.pos.y) + rngVector * (self.radius/2)
            self.__nextRandomVector = pygame.Vector2(self.pos.x, self.pos.y) - rngVector * (self.radius/2)
            return Cell(newVector, self.radius*0.75, self.color)

    def move(self):
        rngVect = self.random2DVector()
        self.pos += rngVect

    def show(self, window: pygame.Surface):
        pygame.draw.ellipse(window, self.color, self.Rect)
