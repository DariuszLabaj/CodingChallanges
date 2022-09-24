from __future__ import annotations
import pygame


class Branch:
    count = 0
    lenght = 40

    def __init__(
        self, parent: Branch | None, position: pygame.Vector2, direction: pygame.Vector2
    ):
        self.pos = position
        self.parent = parent
        self.dir = direction
        self.orgDir = direction

    def next(self):
        nextDir = pygame.Vector2(self.dir.x, self.dir.y)
        nextPos = self.pos + (self.dir*self.lenght)
        nextBranch = Branch(self, nextPos, nextDir)
        return nextBranch

    def show(self, window: pygame.Surface):
        if self.parent:
            pygame.draw.line(window, (255, 255, 255), self.parent.pos, self.pos)

    def reset(self):
        self.count = 0
        self.dir = pygame.Vector2(self.orgDir.x, self.orgDir.y)
