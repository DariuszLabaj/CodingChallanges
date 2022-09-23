from typing import List
import GraphicEngine
from MitosisSimulation.cell import Cell


class Window(GraphicEngine.PygameGFX):
    __cells: List[Cell]

    def Setup(self):
        self.__cells = []
        cell = Cell.RandomCell(
            (self.Width / 3, self.Width / 3 * 2), (self.Height / 3, self.Height / 3 * 2)
        )
        self.__cells.append(cell)

    def Draw(self):
        self.background(41)
        for cell in self.__cells:
            cell.move()
            cell.show(self.DisplaySurface)

    def mouseReleased(self):
        for i in range(len(self.__cells) - 1, -1, -1):
            if self.__cells[i].Rect.collidepoint(self.mousePosition):
                self.__cells.append(self.__cells[i].split())
                self.__cells.append(self.__cells[i].split())
                self.__cells.pop(i)
