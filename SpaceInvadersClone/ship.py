import pygame


class Ship:
    @property
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 20, 40)

    def __init__(self, width, height):
        self.__w = width
        self.__h = height
        self.x = int(self.__w / 2)
        self.y = self.__h - 40

    def update(self):
        pass

    def move(self, dir: int):
        self.x += dir*5

    def show(self, window: pygame.Surface):
        color = (255, 255, 255)
        pygame.draw.rect(window, color, self.getRect)
