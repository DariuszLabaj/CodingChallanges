import random
from typing import Tuple
import pygame

from GraphicEngine import mathMap


class Star:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self._maxR = 6
        self.__initStar(True)

    def __initStar(self, randomizeZ: bool = False):
        rng = random.Random()
        self.x = rng.randint(-self.__width, self.__width)
        self.y = rng.randint(-self.__height, self.__height)
        if randomizeZ:
            self.z = rng.random() * self.__width
        else:
            self.z = self.__width
        self.pz = self.z

    def update(self):
        speed = mathMap(pygame.mouse.get_pos()[0], 0, self.__width, 1, 50)
        self.z = self.z - speed
        if self.z < 1:
            self.__initStar()

    def __calcNewpos(self, z) -> Tuple[float, float]:
        sx: float = mathMap(self.x / z, 0, 1, 0, self.__width)
        sy: float = mathMap(self.y / z, 0, 1, 0, self.__height)
        return sx + self.__width / 2, sy + self.__height / 2

    def show(self, window: pygame.Surface):
        newPoint = self.__calcNewpos(self.z)
        lastPoint = self.__calcNewpos(self.pz)
        self.pz = self.z
        self._r = int(mathMap(self.z, 0, self.__width, self._maxR, 1))
        pygame.draw.line(
            window,
            (255, 255, 255),
            lastPoint,
            newPoint,
            self._r,
        )
