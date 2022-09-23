from __future__ import annotations
from functools import cached_property
from typing import List, Union
import pygame
import random


class Cell:
    @cached_property
    def Rect(self):
        return pygame.Rect(self.i * self.size, self.j * self.size, self.size, self.size)

    @cached_property
    def __Rect(self):
        return pygame.Rect(0, 0, self.size, self.size)

    def __init__(self, i: int, j: int, size: int, noColums: int, noRows: int):
        self.i = i
        self.j = j
        self.noCols = noColums
        self.noRows = noRows
        self.size = size
        self.__surface = self.__createSurface()
        self.__color = (255, 255, 255, 255)
        self.walls = {"Top": True, "Right": True, "Bottom": True, "Left": True}
        self.visited = False

    def __createSurface(self) -> pygame.Surface:
        return pygame.Surface((self.size, self.size), pygame.SRCALPHA)

    def drawWalls(self):
        if self.walls["Top"]:
            pygame.draw.line(
                self.__surface,
                self.__color,
                (self.__Rect.x, self.__Rect.y),
                (self.__Rect.width, self.__Rect.y),
            )
        if self.walls["Right"]:
            pygame.draw.line(
                self.__surface,
                self.__color,
                (self.__Rect.width, self.__Rect.y),
                (self.__Rect.width, self.__Rect.height),
            )
        if self.walls["Bottom"]:
            pygame.draw.line(
                self.__surface,
                self.__color,
                (self.__Rect.x, self.__Rect.height),
                (self.__Rect.width, self.__Rect.height),
            )
        if self.walls["Left"]:
            pygame.draw.line(
                self.__surface,
                self.__color,
                (self.__Rect.x, self.__Rect.y),
                (self.__Rect.x, self.__Rect.height),
            )

    def index(self, i, j) -> int:
        return i + j * self.noCols

    def __getNeigbor(self, grid: List[Cell], i: int, j: int):
        if i < 0 or j < 0 or i > self.noCols - 1 or j > self.noRows - 1:
            return None
        return grid[self.index(i, j)]

    def checkNeighbors(self, grid: List[Cell]) -> Union[Cell, None]:
        neighbors = []
        checkdata = [
            self.__getNeigbor(grid, self.i, self.j - 1),
            self.__getNeigbor(grid, self.i + 1, self.j),
            self.__getNeigbor(grid, self.i, self.j + 1),
            self.__getNeigbor(grid, self.i - 1, self.j),
        ]
        for chk in checkdata:
            if chk and not chk.visited:
                neighbors.append(chk)
        if len(neighbors) > 0:
            rng = random.Random()
            return neighbors[rng.randint(0, len(neighbors) - 1)]
        else:
            return None

    def show(self, window: pygame.Surface):
        self.__surface = self.__createSurface()
        if self.visited:
            pygame.draw.rect(self.__surface, (255, 0, 255, 100), self.__Rect)
        self.drawWalls()
        window.blit(self.__surface, self.Rect)

    def highlight(self, window: pygame.Surface):
        pygame.draw.rect(self.__surface, (0, 0, 255, 100), self.__Rect)
        window.blit(self.__surface, self.Rect)