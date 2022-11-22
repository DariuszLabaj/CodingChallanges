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
    def RandomCell(limitV: Tuple[float, float], limitH: tuple[float, float]) -> Cell:
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
    def getPosition(limitV: Tuple[float, float], limitH: tuple[float, float]) -> pygame.Vector2:
        rng = random.Random()
        x = rng.randint(int(limitV[0]), int(limitV[1]))
        y = rng.randint(int(limitH[0]), int(limitH[0]))
        return pygame.Vector2(x, y)

    @staticmethod
    def random2DVector() -> pygame.Vector2:
        rng = random.Random()
        return pygame.Vector2(rng.random() * 2 - 1, rng.random() * 2 - 1)

    def split(self) -> Cell:
        if self.__nextRandomVector:
            return Cell(self.__nextRandomVector, int(self.radius*0.75), self.color)  # type: ignore
        else:
            rngVector = Cell.random2DVector()
            newVector = pygame.Vector2(self.pos.x, self.pos.y) + rngVector * (self.radius/2)
            self.__nextRandomVector = pygame.Vector2(self.pos.x, self.pos.y) - rngVector * (self.radius/2)
            return Cell(newVector, int(self.radius*0.75), self.color)  # type: ignore

    def move(self):
        rngVect = self.random2DVector()
        self.pos += rngVect

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        pygame.draw.ellipse(window, self.color, self.Rect)
