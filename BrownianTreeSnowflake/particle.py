from __future__ import annotations
from math import dist
import random
from typing import List, Optional
import pygame


class Particle(pygame.sprite.Sprite):
    __pos: pygame.Vector2
    __home: pygame.Vector2
    __start: pygame.Vector2
    _r: int
    __surf: pygame.Surface
    __disabled: bool

    @property
    def Finished(self) -> bool:
        dis = self.__home.distance_to(self.__pos)+self._r*2
        if dis < self.__lastDist:
            self.__lastDist = dis
            return False
        else:
            return True

    @property
    def Position(self) -> pygame.Vector2:
        return self.__pos

    @property
    def WasValid(self) -> bool:
        return self.__start.distance_to(self.__pos) > self._r * 2

    def __init__(
        self,
        x: float,
        y: float,
        home: pygame.Vector2,
        rotate: float = 0,
        radius: Optional[float] = 3.0,
    ):
        super().__init__()
        self.__disabled = False
        self.__pos = pygame.Vector2(x, y)
        self.__start = pygame.Vector2(x, y)
        self._r = radius
        self.__surf = pygame.Surface([self._r * 2, self._r * 2], pygame.SRCALPHA)
        pygame.draw.circle(
            self.__surf, (255, 255, 255), (self._r, self._r), radius=self._r
        )
        self.__rect = self.__surf.get_rect()
        self.__rect.center = self.__pos
        self.__home = home
        self.__lastDist = self.__home.distance_to(self.__pos) + 4*self._r
        self.__angle = rotate

    def update(self):
        if self.__disabled:
            return
        rng = random.Random()
        newVect = pygame.Vector2(-1, float((rng.randrange(-1000, 1000) / 1000))).rotate(
            self.__angle
        )
        self.__pos.x += newVect.x
        self.__pos.y += newVect.y
        self.__rect.center = self.__pos

    def disable(self):
        self.__disabled = True

    def show(self, window: pygame.Surface):
        window.blit(self.__surf, self.__rect)

    def Intersect(self, sonwflake: List[Particle]) -> bool:
        result: bool = False
        for p in sonwflake:
            d: float = dist((self.__pos.x, self.__pos.y), (p.Position.x, p.Position.y))
            if d < self._r * 2:
                result = True
                break
        return result
