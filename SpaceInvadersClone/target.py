import pygame


class Target:
    @property
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 60, 60)

    def __init__(self, x: int, y: int, width: int, height: int):
        self.__w = width
        self.__h = height
        self.dir = -1
        self.bounce = -1
        self.x = x
        self.minx = x - 60
        self.maxx = x + 60
        self.y = y

    def __moveDown(self):
        self.dir *= -1
        self.y += 30

    def update(self):
        self.x += 30 * self.dir
        self.y += 10 * self.bounce
        self.bounce *= -1
        if self.x <= self.minx:
            self.x = self.minx
            self.__moveDown()
        elif self.x >= self.maxx:
            self.x = self.maxx
            self.__moveDown()

    def show(self, window: pygame.Surface):
        color = (255, 0, 200)
        pygame.draw.ellipse(window, color, self.getRect)
