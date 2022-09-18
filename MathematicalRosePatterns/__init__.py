from typing import List, Tuple
import pygame
import math
import GraphicEngine

TWO_PI = math.pi * 2


def floatRange(start: float, end: float, step: float) -> List[float]:
    if not start:
        start = 0.0
    if not step:
        step = 0.001
    a = 0
    while step < 1:
        step *= 10
        a += 1
    b = math.pow(10, a)
    return [x / b for x in range(int(start * b), int(end * b), int(step))]


class Window(GraphicEngine.PygameGFX):
    points: List[Tuple[float, float]]
    index: int

    def Setup(self):
        self.points = []
        self.index = 0
        # for a in [x / 10 for x in range(0, int(TWO_PI * 9 * 10), 1)]:
        for a in floatRange(0, (TWO_PI * 9), 0.1):
            r: float = math.cos(4 / 9 * a) * 300
            x = r * math.cos(a) + self.Width / 2
            y = r * math.sin(a) + self.Height / 2
            self.points.append((x, y))

    def Draw(self):
        self.background(r=51, g=51, b=51)
        color = (255, 255, 255)
        if self.index < len(self.points):
            for i in range(1, self.index % len(self.points)):
                pygame.draw.line(
                    self.DisplaySurface,
                    color,
                    self.points[i - 1],
                    self.points[i],
                    width=1,
                )
        else:
            for i in range(1, len(self.points)):
                pygame.draw.line(
                    self.DisplaySurface,
                    color,
                    self.points[i - 1],
                    self.points[i],
                    width=1,
                )
            pygame.draw.line(
                self.DisplaySurface, color, self.points[-1], self.points[0], width=1
            )
        color = (255, 0, 0)
        pygame.draw.circle(
            self.DisplaySurface, color, self.points[self.index % len(self.points)], 8
        )
        self.index += 1
