from __future__ import annotations
from functools import cached_property
import math
from typing import List
import pygame


class Branch:
    @cached_property
    def endPoz(self):
        x = math.cos(self.angle) * self.len
        y = math.sin(self.angle) * self.len
        return pygame.Vector2(x + self.startPoz.x, y + self.startPoz.y)

    def __init__(self, poz: pygame.Vector2, length: float, angle: float):
        self.startPoz = poz
        self.len = length
        self.angle = angle
        self.finished = False

    def branch(self) -> List[Branch]:
        if self.finished:
            return []
        right = Branch(self.endPoz, self.len*0.63, self.angle+math.pi/6)
        left = Branch(self.endPoz, self.len*0.63, self.angle-math.pi/6)
        self.finished = True
        return [right, left]

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        pygame.draw.line(window, (255, 255, 255), self.startPoz, self.endPoz)
