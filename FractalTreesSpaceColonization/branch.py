from __future__ import annotations
import pygame


class Branch:
    count = 0
    lenght = 40

    def __init__(
        self, parent: Branch | None, position: pygame.Vector2, direction: pygame.Vector2
    ):
        self.pos: pygame.Vector2 = position
        self.parent: Branch | None = parent
        self.dir: pygame.Vector2 = direction
        self.orgDir: pygame.Vector2 = direction

    def next(self):
        nextDir = pygame.Vector2(self.dir.x, self.dir.y)
        nextPos: pygame.Vector2 = self.pos + (self.dir*self.lenght)  # type: ignore
        nextBranch = Branch(self, nextPos, nextDir)
        return nextBranch

    def show(self, window: pygame.Surface | pygame.surface.Surface):
        if self.parent:
            pygame.draw.line(window, (255, 255, 255), self.parent.pos, self.pos)

    def reset(self):
        self.count = 0
        self.dir = pygame.Vector2(self.orgDir.x, self.orgDir.y)
