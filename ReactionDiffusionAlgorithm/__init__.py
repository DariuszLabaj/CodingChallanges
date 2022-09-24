from dataclasses import dataclass
import math
from typing import List
import GraphicEngine

DA = 1.0
DB = 0.5
FEED = 0.055
K = 0.062


@dataclass(slots=True)
class pixelObj:
    a: float
    b: float


class Window(GraphicEngine.PygameGFX):
    grid: List[List[pixelObj]]
    next: List[List[pixelObj]]

    def Setup(self):
        self.grid = []
        self.next = []
        self.background(51)
        for x in range(self.Width):
            self.grid.append([])
            self.next.append([])
            for y in range(self.Height):
                self.grid[x].append(pixelObj(1, 0))
                self.next[x].append(pixelObj(1, 0))
        for i in range(int(self.Width / 2 - 10), int(self.Width / 2 + 10), 1):
            for j in range(int(self.Height / 2 - 10), int(self.Height / 2 + 10), 1):
                self.grid[i][j].b = 1

    def Draw(self):
        for x in range(self.Width):
            for y in range(self.Height):
                a = self.grid[x][y].a
                b = self.grid[x][y].b
                self.next[x][y].a = (
                    a + (DA * self.laplaceA(x, y)) - (a * b * b) + (FEED * (1 - a))
                )
                self.next[x][y].b = (
                    b + (DB * self.laplaceB(x, y)) + (a * b * b) - ((K + FEED) * b)
                )
                apart = self.next[x][y].a * 255
                bpart = self.next[x][y].b * 255
                cpart = apart - bpart
                if cpart > 255:
                    cpart = 255
                elif cpart < 0:
                    cpart = 0
                elif math.isnan(cpart):
                    cpart = 0
                else:
                    cpart = int(cpart)
                self.DisplaySurface.set_at((x, y), (cpart, cpart, cpart))

        self.swap()

    def laplaceA(self, x: int, y: int):
        sumA = 0
        adjesetnWeight = 0.2
        diagonalWeight = 0.05

        sumA += self.grid[x][y].a * -1

        sumA += self.grid[x - 1][y].a * adjesetnWeight if x > 0 else 0
        sumA += self.grid[x + 1][y].a * adjesetnWeight if x < self.Width - 1 else 0
        sumA += self.grid[x][y - 1].a * adjesetnWeight if y > 0 else 0
        sumA += self.grid[x][y + 1].a * adjesetnWeight if y < self.Height - 1 else 0

        sumA += self.grid[x - 1][y - 1].a * diagonalWeight if x > 0 and y > 0 else 0
        sumA += self.grid[x + 1][y + 1].a * diagonalWeight if x < self.Width - 1 and y < self.Height - 1 else 0
        sumA += self.grid[x + 1][y - 1].a * diagonalWeight if x < self.Width - 1 and y > 0 else 0
        sumA += self.grid[x - 1][y + 1].a * diagonalWeight if x > 0 and y < self.Height - 1 else 0

        return sumA

    def laplaceB(self, x: int, y: int):
        sumB = 0
        adjesetnWeight = 0.2
        diagonalWeight = 0.05

        sumB += self.grid[x][y].b * -1

        sumB += self.grid[x - 1][y].b * adjesetnWeight if x > 0 else 0
        sumB += self.grid[x + 1][y].b * adjesetnWeight if x < self.Width - 1 else 0
        sumB += self.grid[x][y - 1].b * adjesetnWeight if y > 0 else 0
        sumB += self.grid[x][y + 1].b * adjesetnWeight if y < self.Height - 1 else 0

        sumB += self.grid[x - 1][y - 1].b * diagonalWeight if x > 0 and y > 0 else 0
        sumB += self.grid[x + 1][y + 1].b * diagonalWeight if x < self.Width - 1 and y < self.Height - 1 else 0
        sumB += self.grid[x + 1][y - 1].b * diagonalWeight if x < self.Width - 1 and y > 0 else 0
        sumB += self.grid[x - 1][y + 1].b * diagonalWeight if x > 0 and y < self.Height - 1 else 0

        return sumB

    def swap(self):
        temp = self.grid
        self.grid = self.next
        self.next = temp
