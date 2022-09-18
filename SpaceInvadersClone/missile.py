import pygame


class Missile:
    @property
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 16, 16)

    def __init__(self, x: int, y: int, width: int, height: int):
        self.__w = width
        self.__h = height
        self.x = x
        self.y = y
        self.diable = False

    def show(self, window: pygame.Surface):
        color = (150, 0, 255)
        pygame.draw.ellipse(window, color, self.getRect)

    def update(self):
        self.y -= 5

    def hits(self, target: pygame.Rect) -> bool:
        if target.colliderect(self.getRect) and not self.diable:
            self.diable = True
            return True
        return False
