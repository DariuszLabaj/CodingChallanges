from typing import Tuple
from GraphicEngine import random2DVector
import pygame


class Leaf:
    reched = False

    def __init__(self, canvasDimmensions: Tuple[int, int]):
        self.pos = random2DVector(canvasDimmensions[0], canvasDimmensions[1] - 100)

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        pygame.draw.circle(window, (255, 0, 100), (self.pos.x, self.pos.y), 4)
