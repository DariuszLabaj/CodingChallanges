import random
from typing import Tuple
import pygame


class Food:
    @property
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.scale, self.scale)

    def __init__(
        self, scale: int, constrainsX: Tuple[int, int], constrainsY: Tuple[int, int]
    ):
        self.scale = scale
        self.constrainsX = constrainsX
        self.constrainsY = constrainsY
        self.x, self.y = self.pickLocation()

    def pickLocation(self) -> Tuple[int, int]:
        rng = random.Random()
        cols = int(self.constrainsX[1] / self.scale)
        rows = int(self.constrainsY[1] / self.scale)
        x = int(rng.random() * cols) * self.scale
        y = int(rng.random() * rows) * self.scale
        return (x, y)

    def show(self, window: pygame.Surface):
        color = (255, 0, 100)
        pygame.draw.rect(window, color, self.getRect)
