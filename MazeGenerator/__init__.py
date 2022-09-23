import math
from typing import List
import GraphicEngine
from MazeGenerator.cell import Cell


class Window(GraphicEngine.PygameGFX):
    cols: int
    rows: int
    size: int
    cells: List[Cell]
    stack: List[Cell]
    current = Cell

    def Setup(self):
        self.size = 10
        self.cols = math.floor(self.Width / self.size)
        self.rows = math.floor(self.Height / self.size)
        self.cells = []
        self.stack = []
        for j in range(self.rows):
            for i in range(self.cols):
                self.cells.append(Cell(i, j, self.size, self.cols, self.rows))
        self.current = self.cells[0]

    def Draw(self):
        self.background(51)
        for cell in self.cells:
            cell.show(self.DisplaySurface)
        self.current.visited = True
        self.current.highlight(self.DisplaySurface)
        next = self.current.checkNeighbors(self.cells)
        if next:
            self.stack.append(self.current)
            Window.removeWalls(self.current, next)
            self.current = next
        elif self.stack:
            self.current = self.stack.pop()

    @staticmethod
    def removeWalls(a: Cell, b: Cell):
        x = a.i - b.i
        y = a.j - b.j
        if x == 1:
            a.walls["Left"] = False
            b.walls["Right"] = False
        elif x == -1:
            b.walls["Left"] = False
            a.walls["Right"] = False

        if y == 1:
            a.walls["Top"] = False
            b.walls["Bottom"] = False
        elif y == -1:
            b.walls["Top"] = False
            a.walls["Bottom"] = False
