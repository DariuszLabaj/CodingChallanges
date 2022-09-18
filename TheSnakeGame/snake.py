from typing import List, Tuple
import pygame

from GraphicEngine import constrain


class Snake:
    @property
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.scale, self.scale)

    def __init__(
        self, scale: int, constrainsX: Tuple[int, int], constrainsY: Tuple[int, int]
    ):
        self.xDir = 1
        self.yDir = 0
        self.scale = scale
        self.constrainsX = constrainsX
        self.constrainsY = constrainsY
        self.x, self.y = self.__getStatingLocation()
        self.total: int = 0
        self.tail: List[pygame.Rect] = []

    def __getStatingLocation(self) -> Tuple[int, int]:
        cols = int(self.constrainsX[1] / self.scale)
        rows = int(self.constrainsY[1] / self.scale)
        x = int(cols/2)*self.scale
        y = int(rows/2)*self.scale
        return (x, y)

    def update(self):
        if self.total == len(self.tail):
            for i in range(self.total - 1):
                self.tail[i] = self.tail[i + 1]
        if self.total:
            self.tail[self.total - 1] = pygame.Rect(
                self.x, self.y, self.scale, self.scale
            )
        self.x += self.xDir * self.scale
        self.y += self.yDir * self.scale
        self.x = int(constrain(self.x, *self.constrainsX))
        self.y = int(constrain(self.y, *self.constrainsY))
        self.clodied()

    def dir(self, xdir: int, ydir: int):
        if (xdir and xdir != -self.xDir) or (ydir and ydir != -self.yDir):
            self.xDir = xdir
            self.yDir = ydir

    def show(self, window: pygame.Surface):
        color = (255, 255, 255)
        for v in self.tail:
            pygame.draw.rect(window, color, v)
        pygame.draw.rect(window, color, self.getRect)

    def eat(self, food: pygame.Rect):
        if food.colliderect(self.getRect):
            self.total += 1
            self.tail.append(pygame.Rect(self.x, self.y, self.scale, self.scale))
            return True
        return False

    def clodied(self) -> bool:
        colided = False
        for v in self.tail:
            if v.colliderect(self.getRect):
                colided = True
                break
        if colided:
            self.total = 0
            self.tail = []
            self.x, self.y = self.__getStatingLocation()
        return colided
